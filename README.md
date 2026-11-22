# formai-templates

Every public Form app's templates and demos, gathered in one place, so that FormPortal can offer them per app as an
optional download. Each file is a copy of what the app ships in its own repository at its newest release, under that
app's own licence. FormSculpt's are not gathered for now.

## What is here

| App | Version | Templates | Demos | Size |
| --- | --- | ---: | ---: | ---: |
| FormAT | 0.32.0 | 0 | 3 | 756 KB |
| FormCel | 0.48.0 | 9 | 1 | 9.0 MB |
| FormCut | 2.20.1 | 0 | 4 | 72.4 MB |
| FormDesign | 0.93.1 | 71 | 0 | 529 KB |
| FormEncoder | 0.13.1 | 0 | 3 | 35.3 MB |
| form.ext | 0.10.0 | 36 | 13 | 417 KB |
| FormFabric | 0.30.0 | 0 | 4 | 1.7 MB |
| FormLit | 0.56.0 | 0 | 3 | 14.9 MB |
| FormPDF | 0.66.0 | 0 | 3 | 2.4 MB |
| FormRef | 0.46.1 | 0 | 3 | 3.8 MB |
| FormDeck | 0.46.3 | 0 | 2 | 2.6 MB |
| FormTxt | 0.38.0 | 0 | 3 | 62 KB |
| FormVFX | 0.60.0 | 1 | 3 | 12.3 MB |
| FormVis | 2.8.1 | 0 | 3 | 3.5 MB |
| FormWav | 2.31.1 | 0 | 3 | 7.8 MB |
| FormWeb | 0.27.0 | 50 | 3 | 10.9 MB |
| **All 16 apps** | | **167** | **54** | **178.2 MB** |

Some files hold many: FormCel's nine template files hold 90 workbook templates and its demo file three demos, and
FormVFX's text animators file holds 169 presets. `python3 -I scripts/build_index.py --table` prints this table.

```text
index.json                      every file, its size and SHA-256 (below)
sources.json                    per app: its repository, licence, credits and which paths are templates or demos
apps/[app id]/templates/        one file per template; a template that is a folder is one .zip of it
apps/[app id]/demos/            the same for demos
apps/[app id]/previews/         a picture, only where the app itself ships one for that item
apps/[app id]/LICENSE           the app's own licence (LICENSE-* beside it for parts under another one)
apps/[app id]/CREDITS.md        the app's own credits for third-party material, where there is any
apps/[app id]/app.json          what scripts/collect.py read from the app, for scripts/build_index.py
scripts/                        collect.py, build_index.py, check.py
```

`[app id]` is the app's id in the family catalogue (`formslide` for FormDeck, `formext` for form.ext, `format` for
FormAT).

## How FormPortal uses it

FormPortal's Stock & templates page has a section per app, each closed until you open it. Nothing is fetched until
you ask: the page first says what this is and offers one button to get the list. Then it reads `index.json` from
`https://raw.githubusercontent.com/nodemode-dev/formai-templates/main/index.json`, a plain request to GitHub with no
account. A file is downloaded only when you press its Download (or an app's Download all), from the same place, and
FormPortal keeps it only when its size and SHA-256 match the index. A mismatch keeps nothing.

`index.json`:

```json
{
  "format": "formai-templates",
  "format_version": 1,
  "generated": "2026-11-22T02:04:32Z",
  "apps": [
    { "id": "formweb", "name": "FormWeb", "licence": "Apache-2.0", "version": "0.27.0",
      "items": [
        { "id": "formweb/demos/lowlight", "kind": "demo", "name": "Lowlight", "description": "",
          "path": "apps/formweb/demos/lowlight.fweb", "bytes": 3588882, "sha256": "64 hex characters",
          "licence": "Apache-2.0; NASA media guidelines; CC BY 4.0 (ESA/Hubble)", "credit": "...",
          "preview": "apps/formweb/previews/lowlight.webp" }
      ] }
  ]
}
```

`kind` is `template` or `demo`. `path` always names one file under `apps/`. `name` and `description` come from the
template's own metadata where it has them, otherwise the name is its file name in title case and the description is
empty. `preview` is present only when the app ships a picture for that item. Apps are sorted by id, items by kind,
then name. `generated` (a timestamp for machines) is the only field that changes between two runs on the same files.

## How a template gets here

A template or demo ships in its app's repository first. After the app publishes a release, formadaptor runs
`scripts/collect.py` against that release and proposes the copy here as a pull request; the `check` workflow runs
`scripts/check.py` on it, and an owner reviews and merges. There are no direct uploads: a pull request that adds or
edits files under `apps/` by hand is closed ([CONTRIBUTING.md](CONTRIBUTING.md)). A new app is one entry in
`sources.json`.

```sh
# DIR holds one checkout per app at its released tag, named for its repository (DIR/formcut, DIR/form.ext, ...)
python3 -I scripts/collect.py --apps-root DIR [--family family.json] [--only formcut ...] [--check]
python3 -I scripts/build_index.py           # collect.py runs it; --table prints the table above
python3 -I scripts/check.py                 # fails when the index and the files disagree
```

All three use the Python standard library only and need no network. `collect.py` takes each app's version from the
family spec given with `--family`, from `DIR/releases.json`, or from the checkout's tag; it removes files that are no
longer in the source and writes each folder as a `.zip` with sorted entries and fixed times, so the same release
gives the same bytes. With `--family` it gathers only apps the spec lists as public with a release, and keeps the
spec it was run with at `scripts/family.spec.json`, rewritten only when the gathered files change. `--check` writes
nothing and names each file that would change. `check.py` fails when a file is missing, extra, of another size or
hash, outside `apps/` or without a licence, when a file is over 50 MB, or when a text file (also inside a `.zip`)
holds an emoji or a path from a person's machine.

## Licences

This repository's own scripts, `sources.json` and `index.json` are under the Apache License 2.0 ([LICENSE](LICENSE)).
Each app's templates and demos stay under that app's own licence, whose file sits in its folder, and third-party
material in them keeps the credit and licence its app's credits file gives: [LICENSES.md](LICENSES.md) has the table.

[SECURITY.md](SECURITY.md) · [CONTRIBUTING.md](CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ·
[CHANGELOG.md](CHANGELOG.md)
