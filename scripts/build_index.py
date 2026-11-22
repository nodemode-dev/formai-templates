#!/usr/bin/env python3
"""Write index.json from what is in apps/.

    python3 -I scripts/build_index.py [--root DIR] [--now] [--table]

Each apps/[id]/app.json (written by scripts/collect.py) names the app, its
licence and version, and each item's file, kind, name, description, licence,
credit and preview. This script adds each file's size and SHA-256 and writes
index.json at the root. Apps are sorted by id, items by kind, then name.

`generated` is the only field that can change between two runs on the same
files. When nothing else changed, the existing index.json is left as it is;
--now writes a fresh `generated` anyway.

--table prints the Markdown table of apps, counts and sizes for README.md
and writes nothing.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def build(root: Path) -> dict:
    apps = []
    apps_dir = root / "apps"
    for app_dir in sorted(p for p in apps_dir.iterdir() if p.is_dir()) if apps_dir.is_dir() else []:
        meta_path = app_dir / "app.json"
        if not meta_path.is_file():
            raise SystemExit(f"build_index: {app_dir.name} has no app.json")
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        items = []
        for record in meta["items"]:
            path = app_dir / record["file"]
            if not path.is_file():
                raise SystemExit(f"build_index: {meta['id']}: {record['file']} is missing")
            stem = Path(record["file"]).stem
            folder = record["file"].split("/", 1)[0]
            item = {
                "id": f"{meta['id']}/{folder}/{stem}",
                "kind": record["kind"],
                "name": record["name"],
                "description": record.get("description", ""),
                "path": f"apps/{meta['id']}/{record['file']}",
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "licence": record["licence"],
                "credit": record.get("credit", ""),
            }
            if record.get("preview"):
                if not (app_dir / record["preview"]).is_file():
                    raise SystemExit(f"build_index: {meta['id']}: {record['preview']} is missing")
                item["preview"] = f"apps/{meta['id']}/{record['preview']}"
            items.append(item)
        items.sort(key=lambda i: (i["kind"] != "template", i["name"].casefold(), i["id"]))
        apps.append({
            "id": meta["id"],
            "name": meta["name"],
            "licence": meta["licence"],
            "version": meta["version"],
            "items": items,
        })
    return {"format": "formai-templates", "format_version": 1, "generated": "", "apps": apps}


def human(size: int) -> str:
    if size >= 1_000_000:
        return f"{size / 1_000_000:.1f} MB"
    return f"{size / 1000:.0f} KB"


def table(index: dict) -> str:
    lines = ["| App | Version | Templates | Demos | Size |", "| --- | --- | ---: | ---: | ---: |"]
    total = [0, 0, 0]
    for app in index["apps"]:
        t = sum(1 for i in app["items"] if i["kind"] == "template")
        d = sum(1 for i in app["items"] if i["kind"] == "demo")
        size = sum(i["bytes"] for i in app["items"])
        total[0] += t
        total[1] += d
        total[2] += size
        lines.append(f"| {app['name']} | {app['version']} | {t} | {d} | {human(size)} |")
    lines.append(f"| **All {len(index['apps'])} apps** | | **{total[0]}** | **{total[1]}** | **{human(total[2])}** |")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--now", action="store_true")
    parser.add_argument("--table", action="store_true")
    args = parser.parse_args()

    index = build(args.root)
    if args.table:
        print(table(index))
        return 0
    target = args.root / "index.json"
    if target.is_file() and not args.now:
        previous = json.loads(target.read_text(encoding="utf-8"))
        kept = previous.get("generated", "")
        if kept and dict(previous, generated="") == index:
            print("build_index: index.json unchanged")
            return 0
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    index["generated"] = stamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(index, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    count = sum(len(a["items"]) for a in index["apps"])
    print(f"build_index: {len(index['apps'])} apps, {count} items")
    return 0


if __name__ == "__main__":
    sys.exit(main())
