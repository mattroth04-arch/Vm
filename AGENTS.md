# AGENTS.md

## Cursor Cloud specific instructions

### Repository overview
This repository ("Job Search Workspace") is currently a placeholder. It contains
only:
- `Readme.md` — a one-line title.
- `Test.py` — a placeholder file containing the bare token `test`. Running it
  (`python3 Test.py`) intentionally raises `NameError: name 'test' is not
  defined`. This is expected; do not treat it as a bug to fix unless asked.

There is no application, dependency manifest, package manager, build system,
lint config, test framework, or service in this repo yet.

### Environment / runtime
- The only relevant runtime is Python 3 (Python `3.12.x` is preinstalled at
  `/usr/bin/python3`, with `pip3` available). No dependency installation is
  required.
- Because there are no dependency manifests, the startup update script is a
  minimal no-op-style runtime check (`python3 --version`). When real
  dependencies are added (e.g. `requirements.txt` / `pyproject.toml`), update
  the startup script to install them.

### Running / testing
- There is no app to run and no test suite. To verify the environment works,
  run a Python one-liner, e.g.:
  `python3 -c "print('hello')"`
