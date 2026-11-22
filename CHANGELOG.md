# Changelog

## 0.1.0 (2026-11-21)

- The first gathering: 167 templates and 54 demos from 16 public Form apps, each at its newest release, under
  `apps/[catalogue id]/` with that app's licence and credits, and `index.json` listing every file with its size and
  SHA-256 for FormPortal's Stock & templates page. FormSculpt is not gathered for now.
- `sources.json` says, per app, which paths are templates and which are demos. `scripts/collect.py` copies them
  (a folder as one deterministic `.zip`), `scripts/build_index.py` writes the index, and `scripts/check.py` fails
  when the index and the files disagree, a file is over 50 MB, or a text file holds an emoji or a path from a
  person's machine. The `check` workflow runs it on every pull request and push to `main`.
