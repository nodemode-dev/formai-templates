# Security policy

## Supported versions

This repository has no releases to install: what counts is what `main` holds. FormPortal reads `index.json` and the
files from `main`, so a fix goes into `main` and is what every copy of FormPortal sees on its next "Check again".

| What | Supported |
| --- | --- |
| `index.json`, the files under `apps/` and the scripts on `main` | Yes |
| Anything an older commit held | No: only `main` is read |

## Reporting a problem

If a template or demo here holds something harmful (a script that does more than its app's demo should, a file that
is not what its name says, a person's private information), if a file does not match its SHA-256 in the index, or if
the scripts or the workflow are at fault, tell the owners privately: use GitHub's **Report a vulnerability** on this
repository (Security, Advisories), or email `mackin@nodemode.ai`. Please do not open a public issue for something
that could be abused before it is fixed. Say which file, what happens, and how to see it happen.

You get an answer within three working days. A harmful file is removed first and investigated after. We keep you
informed while it is fixed and credit you in the changelog, unless you would rather not be named.

A problem in an app itself, or in how it opens one of its own templates, belongs to that app's repository. A problem
in how FormPortal downloads, checks or unpacks these files belongs to
[FormPortal's security policy](https://github.com/nodemode-dev/formportal/security).

## What counts

- **The files**: a template or demo that runs code its app would not run for its own demos, hides what it is, or
  carries someone's private data or a path from their machine.
- **The index**: a way to get a file listed with a size or SHA-256 it does not have, a path outside `apps/`, or an
  item without a licence, past `scripts/check.py`.
- **How files get here**: a way to change a file without a pull request that the `check` workflow runs on and an
  owner approves, or to make the workflow run with more than read access.

A template that is merely broken or out of date is an ordinary bug: open an issue that names it, or fix it in its
app's repository (see [CONTRIBUTING.md](CONTRIBUTING.md)).
