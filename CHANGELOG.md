# Changelog

## 0.2.1 (2026-11-25)

- `collect.py` finds an app's checkout whatever the letter case of its folder. `sources.json` names FormAT, FormPDF and
  FormVFX as GitHub shows them (`formAT`, `formPDF`, `formVFX`); the family spec that formadaptor fetches the apps from
  writes the three in lower case, so on a case-sensitive disk the collection stopped at "format: no checkout at
  ../formai-templates-apps/formAT". The exact name is still tried first, and two folders that differ only in case are
  not guessed between.
- No collected file changes with this version; the tag `v0.2.0` stays what FormPublisher reads.

- FormWeb 0.28.0: its eight whole-site demos, the three before and five new starters (Coldmere Plumbing, Northfold
  Studio, The Slow Allotment, Wenlow Type Day, Fernhollow Pottery), each with its cover picture. 167 templates and 59
  demos from 16 apps, 226 items in all.
- Each index item gains `type` when its metadata names the kind of site (`business`, `portfolio`, `blog`, `event` or
  `shop`), and every item with a preview gains `preview_sha256`, for every app; `format_version` stays 1. FormPublisher
  0.10.0 reads both from the tag `v0.2.0` and shows no preview without a matching hash. `check.py` now fails on a
  preview whose hash is missing or differs, and on an unknown type.
- `collect.py` reads a meta path with placeholders (FormWeb's `{dir}/demo.json`) from the checkout root, takes the
  name, description and type from it, and prefers a licence and credit the meta file gives to the pattern's.
- FormWeb's demos carry their own licence and credit: only Lowlight names NASA and the ESA/Hubble picture, only
  Looking Back NASA, and every demo names the OFL fonts it embeds.
- Collected from FormWeb's branch `feat/whole-site-starters` at 5f630ae, version 0.28.0, before its tag exists. Before
  `v0.2.0` is tagged, the collection is run again at FormWeb's tag `v0.28.0` once FormWeb's pull request merges; it
  must give the same files, or the changes are committed with it.

## 0.1.0 (2026-11-21)

- The first gathering: 167 templates and 54 demos from 16 public Form apps, each at its newest release, under
  `apps/[catalogue id]/` with that app's licence and credits, and `index.json` listing every file with its size and
  SHA-256 for FormPortal's Stock & templates page. FormSculpt is not gathered for now.
- `sources.json` says, per app, which paths are templates and which are demos. `scripts/collect.py` copies them
  (a folder as one deterministic `.zip`), `scripts/build_index.py` writes the index, and `scripts/check.py` fails
  when the index and the files disagree, a file is over 50 MB, or a text file holds an emoji or a path from a
  person's machine. The `check` workflow runs it on every pull request and push to `main`.
