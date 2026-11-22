#!/usr/bin/env python3
"""Check that index.json matches the files, and that the files are fit to publish.

    python3 -I scripts/check.py [--root DIR]

Fails (exit 1, one line per problem) when:
- an indexed file is missing, has another size or SHA-256, or its path is not
  a plain relative path under apps/; a preview without a preview_sha256, or
  with one its file does not match;
- an item's type is given and is not business, portfolio, blog, event or shop;
- a file under apps/ is not in the index (other than an app's app.json,
  LICENSE, LICENSE-* and CREDITS.md), or an app has no LICENSE;
- an item has no licence, an unknown kind, or an id used twice;
- any file is over 50 MB;
- a text file, or a text file inside a .zip, holds an emoji or a path from a
  person's machine (a home folder with a user name in it).

Standard library only. No network.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 50 * 1024 * 1024
BINARY = {
    ".mp4", ".webm", ".mov", ".mp3", ".m4a", ".wav", ".ogg", ".opus", ".flac",
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif", ".woff", ".woff2", ".ttf", ".otf",
    ".pdf", ".ico", ".icns",
}
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B50\U00002B55\U0000FE0F\U0001F1E6-\U0001F1FF]"
)
HOME = re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\\\?Users\\\\?)([A-Za-z0-9._-]+)")
ALLOWED_HOMES = {"user", "runner", "username", "name", "you", "me", "example"}
META = {"app.json", "LICENSE", "CREDITS.md"}
SITE_TYPES = {"business", "portfolio", "blog", "event", "shop"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_path(value: str) -> bool:
    if not isinstance(value, str) or not value.startswith("apps/") or "\\" in value:
        return False
    parts = PurePosixPath(value).parts
    return not PurePosixPath(value).is_absolute() and ".." not in parts and "" not in parts


def text_of(name: str, data: bytes) -> str | None:
    if PurePosixPath(name).suffix.lower() in BINARY or b"\0" in data[:8192]:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan_text(label: str, text: str, problems: list[str]) -> None:
    hit = EMOJI.search(text)
    if hit:
        line = text.count("\n", 0, hit.start()) + 1
        problems.append(f"{label}:{line}: emoji or pictograph U+{ord(hit.group()):04X}")
    for found in HOME.finditer(text):
        if found.group(1).lower() not in ALLOWED_HOMES:
            line = text.count("\n", 0, found.start()) + 1
            problems.append(f"{label}:{line}: a path from a person's machine")
            break


def scan_file(root: Path, path: Path, problems: list[str]) -> None:
    rel = path.relative_to(root).as_posix()
    if path.stat().st_size > MAX_BYTES:
        problems.append(f"{rel}: over 50 MB")
    if path.suffix.lower() in {".zip", ".formpkg"}:
        try:
            with zipfile.ZipFile(path) as archive:
                for info in archive.infolist():
                    if info.is_dir() or info.file_size > MAX_BYTES:
                        continue
                    text = text_of(info.filename, archive.read(info))
                    if text is not None:
                        scan_text(f"{rel}!{info.filename}", text, problems)
        except zipfile.BadZipFile:
            if path.suffix.lower() == ".zip":
                problems.append(f"{rel}: not a readable zip")
        return
    if path.stat().st_size > 8 * 1024 * 1024:
        return
    text = text_of(rel, path.read_bytes())
    if text is not None:
        scan_text(rel, text, problems)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    problems: list[str] = []

    try:
        index = json.loads((root / "index.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"index.json: cannot be read: {error}")
        return 1
    if index.get("format") != "formai-templates" or index.get("format_version") != 1:
        problems.append("index.json: format must be formai-templates, format_version 1")

    indexed: set[str] = set()
    ids: set[str] = set()
    app_ids: list[str] = []
    for app in index.get("apps", []):
        app_id = app.get("id", "")
        app_ids.append(app_id)
        for key in ("id", "name", "licence", "version"):
            if not app.get(key):
                problems.append(f"index.json: app {app_id or '?'} has no {key}")
        if not (root / "apps" / app_id / "LICENSE").is_file():
            problems.append(f"apps/{app_id}: no LICENSE")
        for item in app.get("items", []):
            item_id = item.get("id", "?")
            if item_id in ids:
                problems.append(f"index.json: item id {item_id} is used twice")
            ids.add(item_id)
            if item.get("kind") not in ("template", "demo"):
                problems.append(f"index.json: {item_id}: kind must be template or demo")
            if not str(item.get("licence", "")).strip():
                problems.append(f"index.json: {item_id}: no licence")
            if "type" in item and item["type"] not in SITE_TYPES:
                problems.append(f"index.json: {item_id}: type must be business, portfolio, blog, event or shop")
            for key in ("path", "preview"):
                if key == "preview" and key not in item:
                    continue
                value = item.get(key, "")
                if not safe_path(value) or not value.startswith(f"apps/{app_id}/"):
                    problems.append(f"index.json: {item_id}: {key} {value!r} is not a plain path under apps/{app_id}/")
                    continue
                target = root / value
                if not target.is_file():
                    problems.append(f"{value}: missing")
                    continue
                indexed.add(value)
                if key == "path":
                    if target.stat().st_size != item.get("bytes"):
                        problems.append(f"{value}: {target.stat().st_size} bytes, the index says {item.get('bytes')}")
                    elif sha256(target) != item.get("sha256"):
                        problems.append(f"{value}: SHA-256 differs from the index")
                elif sha256(target) != item.get("preview_sha256"):
                    problems.append(f"{value}: no preview_sha256 in the index, or one the file does not match")
    if app_ids != sorted(app_ids):
        problems.append("index.json: apps are not sorted by id")

    apps_dir = root / "apps"
    if apps_dir.is_dir():
        for path in sorted(apps_dir.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(root).as_posix()
            parts = rel.split("/")
            is_meta = len(parts) == 3 and (parts[2] in META or parts[2].startswith("LICENSE-"))
            if not is_meta and rel not in indexed:
                problems.append(f"{rel}: not in index.json")

    for path in sorted(root.rglob("*")):
        if ".git" in path.relative_to(root).parts or not path.is_file():
            continue
        scan_file(root, path, problems)

    for line in problems:
        print(line)
    if problems:
        print(f"check: {len(problems)} problem(s)")
        return 1
    print(f"check: {len(ids)} items in {len(app_ids)} apps match their files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
