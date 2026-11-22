# Contributing to formai-templates

Thank you for helping. This repository gathers the templates and demos that each public Form app ships, so that
FormPortal can offer them per app as an optional download. It is a copy, not a source: every template here lives in
its app's own repository first, and this repository is only ever changed by copying from those.

## Which contribution you are making

| You want to | How |
| --- | --- |
| Add or change a template or demo | In **its app's repository**, as that app's own CONTRIBUTING says. After the app's next release, formadaptor proposes the copy here as a pull request. Pull requests that add or edit files under `apps/` by hand are closed. |
| Have a new app's templates gathered here | A pull request that adds one entry for the app to `sources.json` (its catalogue id, repository, licence, credits files and the paths of its templates and demos). The app must be public and released. |
| Report a broken, wrong or unlicensed file | An issue that names the file. Something harmful is reported privately, as [SECURITY.md](SECURITY.md) says. |
| Improve the scripts, the index or the workflow | A pull request, described below. |

## Changing the scripts

`scripts/collect.py`, `scripts/build_index.py` and `scripts/check.py` use the Python standard library only and need
no network. FormPortal reads `index.json` exactly as README.md describes it, so a change to its fields or meaning
needs a change in FormPortal first, and a new `format_version` here.

Before you open the pull request, run the check:

```sh
python3 -I scripts/check.py
```

The `check` workflow runs the same on every pull request and push to `main`, with read-only permissions and no
secrets; it must pass. `@nodemode-ai` or `@gbarnai` reviews and merges.

- One coherent change per pull request.
- No secrets anywhere, and nothing fetched or run from outside the repository.
- Every file keeps its app's licence and credits; nothing whose licence is unknown, or forbids redistribution or
  changes (NC, ND), is gathered.
