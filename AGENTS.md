# AGENTS.md

## Cursor Cloud specific instructions

This repository ("Job Search Workspace") is currently a placeholder with no real
application. It contains only `Readme.md` (a title) and `Test.py` (a placeholder
containing the literal word `test`).

- There are no dependencies, package manager files, build system, automated tests,
  or lint configuration.
- The only relevant runtime is Python (Python 3.12.x is preinstalled). No install
  step is required to run Python code.
- `Test.py` is not a runnable program: it contains the bare word `test`, so
  `python3 Test.py` exits non-zero with `NameError: name 'test' is not defined`.
  This is expected; do not treat it as a broken build.
- When real code is added, update this section with how to install dependencies and
  run/lint/test the application.
