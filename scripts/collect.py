#!/usr/bin/env python3
"""Copy every app's templates and demos into apps/, as sources.json names them.

    python3 -I scripts/collect.py --apps-root DIR [--family family.json] [--only ID ...] [--check]

DIR holds one checkout (or extracted archive) per app, at its released tag,
in a folder named for the app's repository (DIR/formcut, DIR/form.ext, ...).

The app's version is read, in this order, from the family spec given with
--family (release.version), from DIR/releases.json ({"repo": "vX.Y.Z"}), or
from `git describe --tags --exact-match` in the checkout.

With --family, only apps the spec lists as public with a published release
are collected, and the spec is kept at scripts/family.spec.json, rewritten
only when the collected files change (formadaptor's generator contract).

The copy is deterministic: a folder is stored as one .zip with sorted
entries and fixed times, so the same inputs give the same bytes; hidden
files (.gitkeep, .DS_Store) are left out of it. Files that
are no longer in the source are removed. index.json is then written by
scripts/build_index.py.

--check writes nothing: it exits 0 when apps/ and index.json equal what a
run would write, and 1, naming each file that differs, when they do not.
Standard library only. No network.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.json"
SPEC_COPY = ROOT / "scripts" / "family.spec.json"
MAX_BYTES = 50 * 1024 * 1024
ZIP_TIME = (1980, 1, 1, 0, 0, 0)
STORED = {
    ".mp4", ".webm", ".mov", ".mp3", ".m4a", ".ogg", ".opus", ".flac",
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif", ".zip", ".woff", ".woff2",
    ".pdf", ".formpkg",
}
META_FILES = ("app.json", "LICENSE", "CREDITS.md")


class CollectError(Exception):
    pass


def fail(message: str) -> None:
    raise CollectError(message)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def title_case(stem: str) -> str:
    words = stem.replace("_", " ").replace("-", " ").split()
    return " ".join(w[:1].upper() + w[1:] for w in words)


def fill(template: str, item: Path, root: Path) -> str:
    rel = item.relative_to(root).as_posix()
    name = item.name if item.is_dir() else item.stem
    ext = "" if item.is_dir() else item.suffix
    parent_rel = item.parent.relative_to(root).as_posix()
    return (template.replace("{name}", name).replace("{stem}", name)
            .replace("{parent}", item.parent.name).replace("{ext}", ext)
            .replace("{dir}", parent_rel).replace("{path}", rel))


def read_meta(item: Path, meta: str | None) -> dict:
    if not meta:
        return {}
    target = item if meta == "." else item / meta
    if not target.is_file() or target.suffix != ".json":
        return {}
    try:
        data = load_json(target)
    except (ValueError, UnicodeDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def first_text(data: dict, keys: tuple[str, ...]) -> str:
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            return " ".join(value.split())
    return ""


def list_count(item: Path) -> int:
    try:
        data = load_json(item)
    except (ValueError, UnicodeDecodeError):
        return 0
    return len(data) if isinstance(data, list) else 0


def folder_files(folder: Path) -> list[Path]:
    files = [p for p in folder.rglob("*")
             if p.is_file() and not p.is_symlink()
             and not any(part.startswith(".") for part in p.relative_to(folder).parts)]
    return sorted(files, key=lambda p: p.relative_to(folder).as_posix())


def write_zip(folder: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w") as archive:
        for path in folder_files(folder):
            info = zipfile.ZipInfo(path.relative_to(folder).as_posix(), date_time=ZIP_TIME)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            if path.suffix.lower() in STORED:
                info.compress_type = zipfile.ZIP_STORED
                archive.writestr(info, path.read_bytes())
            else:
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes(), compresslevel=9)


def match(root: Path, pattern: dict) -> list[Path]:
    globs = pattern["glob"] if isinstance(pattern["glob"], list) else [pattern["glob"]]
    excludes = pattern.get("exclude", [])
    want_dir = pattern["type"] == "folder"
    found: dict[str, Path] = {}
    for glob in globs:
        for path in root.glob(glob):
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() or (path.is_dir() != want_dir) or (not want_dir and not path.is_file()):
                continue
            if any(fnmatch.fnmatch(rel, ex) for ex in excludes):
                continue
            found[rel] = path
    return [found[k] for k in sorted(found)]


def release_version(app: dict, checkout: Path, apps_root: Path, family: dict | None) -> str:
    if family is not None:
        entry = family.get(app["id"])
        if entry and entry.get("release"):
            return str(entry["release"]["version"])
    releases = apps_root / "releases.json"
    if releases.is_file():
        tag = load_json(releases).get(app["repo"])
        if tag:
            return str(tag).lstrip("v")
    if (checkout / ".git").exists():
        out = subprocess.run(["git", "-C", str(checkout), "describe", "--tags", "--exact-match"],
                             capture_output=True, text=True)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip().lstrip("v")
    fail(f"{app['id']}: no release version (give --family, {releases}, or a checkout at its tag)")
    return ""


def collect_app(app: dict, checkout: Path, version: str, out: Path) -> None:
    if not checkout.is_dir():
        fail(f"{app['id']}: no checkout at {checkout}")
    dest = out / app["id"]
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    licence_file = checkout / "LICENSE"
    if not licence_file.is_file():
        fail(f"{app['id']}: the checkout has no LICENSE")
    shutil.copyfile(licence_file, dest / "LICENSE")
    for extra in app.get("extra", []):
        shutil.copyfile(checkout / extra["from"], dest / extra["to"])
    credits = [c for c in app.get("credits", []) if (checkout / c).is_file()]
    missing = [c for c in app.get("credits", []) if c not in credits]
    if missing:
        fail(f"{app['id']}: credits file not found: {', '.join(missing)}")
    if credits:
        parts = [f"# {app['name']}: credits for its templates and demos\n\n"
                 f"Copied unchanged from the {app['repo']} repository at its release {version}. "
                 "Each part below is one credits file of that repository, named by its path there.\n"]
        for rel in credits:
            body = (checkout / rel).read_text(encoding="utf-8").rstrip("\n")
            parts.append(f"\n## From `{rel}`\n\n{body}\n")
        (dest / "CREDITS.md").write_text("".join(parts), encoding="utf-8")

    items: list[dict] = []
    stored_names: set[str] = set()
    for pattern in app["patterns"]:
        kind = pattern["kind"]
        if kind not in ("template", "demo"):
            fail(f"{app['id']}: kind must be template or demo, not {kind}")
        folder = "templates" if kind == "template" else "demos"
        for item in match(checkout, pattern):
            is_dir = item.is_dir()
            default_store = "{name}.zip" if is_dir else "{name}{ext}"
            stored = fill(pattern.get("store", default_store), item, checkout)
            rel_store = f"{folder}/{stored}"
            if rel_store in stored_names:
                fail(f"{app['id']}: two items would be stored as {rel_store}")
            stored_names.add(rel_store)
            target = dest / rel_store
            target.parent.mkdir(parents=True, exist_ok=True)
            if is_dir:
                write_zip(item, target)
            else:
                shutil.copyfile(item, target)
            if target.stat().st_size > MAX_BYTES:
                fail(f"{app['id']}: {rel_store} is over 50 MB")
            meta = read_meta(item, pattern.get("meta"))
            if pattern.get("name_from") == "parent":
                name = title_case(item.parent.name)
            else:
                name = first_text(meta, ("name", "title")) or title_case(item.name if is_dir else item.stem)
            description = first_text(meta, ("description", "summary", "blurb"))
            if not description and pattern.get("describe_list"):
                count = list_count(item)
                if count:
                    noun = pattern["describe_list"]
                    if count == 1:
                        noun = noun[:-1]
                    description = f"Holds {count} {noun}."
            record = {
                "file": rel_store,
                "kind": kind,
                "name": name,
                "description": description,
                "licence": pattern.get("licence", app["licence"]),
                "credit": pattern.get("credit", ""),
                "source": item.relative_to(checkout).as_posix(),
            }
            if pattern.get("preview"):
                picture = checkout / fill(pattern["preview"], item, checkout)
                if picture.is_file():
                    slug = Path(stored).stem
                    rel_prev = f"previews/{slug}{picture.suffix.lower()}"
                    (dest / "previews").mkdir(exist_ok=True)
                    shutil.copyfile(picture, dest / rel_prev)
                    record["preview"] = rel_prev
            items.append(record)
    if not items:
        fail(f"{app['id']}: no templates or demos matched")
    meta_out = {
        "id": app["id"],
        "name": app["name"],
        "repo": app["repo"],
        "licence": app["licence"],
        "version": version,
        "items": sorted(items, key=lambda r: r["file"]),
    }
    with (dest / "app.json").open("w", encoding="utf-8") as handle:
        json.dump(meta_out, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def tree_files(base: Path) -> dict[str, bytes]:
    if not base.is_dir():
        return {}
    return {p.relative_to(base).as_posix(): p.read_bytes()
            for p in sorted(base.rglob("*")) if p.is_file()}


def index_without_generated(path: Path):
    if not path.is_file():
        return None
    data = load_json(path)
    data.pop("generated", None)
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apps-root", required=True, type=Path)
    parser.add_argument("--family", type=Path)
    parser.add_argument("--only", nargs="+", default=[])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    sources = load_json(SOURCES)
    apps = sources["apps"]
    family = None
    if args.family:
        spec = load_json(args.family)
        family = {a["id"]: a for a in spec.get("apps", []) if a.get("public") is True}
        apps = [a for a in apps if a["id"] in family and family[a["id"]].get("release")]
    known = {a["id"] for a in sources["apps"]}
    for wanted in args.only:
        if wanted not in known:
            print(f"collect: unknown app id {wanted}", file=sys.stderr)
            return 2
    if args.only:
        apps = [a for a in apps if a["id"] in args.only]

    live_apps = ROOT / "apps"
    live_index = ROOT / "index.json"
    with tempfile.TemporaryDirectory(prefix="formai-templates-") as tmp:
        stage = Path(tmp) / "repo"
        stage_apps = stage / "apps"
        if live_apps.is_dir():
            shutil.copytree(live_apps, stage_apps)
        else:
            stage_apps.mkdir(parents=True)
        if live_index.is_file():
            shutil.copyfile(live_index, stage / "index.json")
        try:
            wanted_ids = {a["id"] for a in apps}
            if not args.only:
                for old in stage_apps.iterdir():
                    if old.is_dir() and old.name not in wanted_ids:
                        shutil.rmtree(old)
            for app in apps:
                checkout = args.apps_root / app["repo"]
                version = release_version(app, checkout, args.apps_root, family)
                collect_app(app, checkout, version, stage_apps)
                print(f"collect: {app['id']} {version}")
        except CollectError as error:
            print(f"collect: {error}", file=sys.stderr)
            return 2
        build = subprocess.run([sys.executable, "-I", str(ROOT / "scripts" / "build_index.py"),
                                "--root", str(stage)])
        if build.returncode != 0:
            return 2

        before = tree_files(live_apps)
        after = tree_files(stage_apps)
        differ = sorted(f"apps/{k}" for k in set(before) | set(after) if before.get(k) != after.get(k))
        if index_without_generated(live_index) != index_without_generated(stage / "index.json"):
            differ.append("index.json")

        if args.check:
            for name in differ:
                print(name)
            return 1 if differ else 0

        if differ:
            if live_apps.exists():
                shutil.rmtree(live_apps)
            shutil.copytree(stage_apps, live_apps)
            shutil.copyfile(stage / "index.json", live_index)
            if args.family:
                shutil.copyfile(args.family, SPEC_COPY)
            print(f"collect: {len(differ)} file(s) changed")
        else:
            print("collect: nothing changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
