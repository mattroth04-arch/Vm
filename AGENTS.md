# Job Search Workspace

This repository is a **data workspace**, not a runnable software application. There is
no service to build/serve. It holds a job-search inventory and an agent handoff doc.

Repo contents:
- `Readme.md` — title only.
- `Test.py` — placeholder (a bare `test` token); it is **not** real code and raises
  `NameError` if run. Do not treat it as an app entrypoint.
- `phase3c_sync_minimum.zip` — the actual data, bundled as a zip. Unzipping it yields
  `JOB_SEARCH_HANDOFF.md` (full project context) plus the `Jobs/` data tree
  (`current_results.csv`, `applied_jobs.csv`, `employer_database/...csv`,
  `runs/phase3c_browser_queue_*.json`).

The Python processing scripts referenced in the handoff (e.g. `phase4_audit_rescore.py`,
`round23_complete_search.py`) live on an external server and are **not committed here**.

## Cursor Cloud specific instructions

- The data lives only inside `phase3c_sync_minimum.zip`. To work with it, extract first:
  `unzip -o phase3c_sync_minimum.zip` (creates untracked `Jobs/` + `JOB_SEARCH_HANDOFF.md`;
  the zip is the source of truth — do not commit the extracted files). This is a setup
  step, intentionally kept out of the startup update script.
- Data tooling is `pandas` (installed via the update script with `pip3 install --user`).
  On this Ubuntu 24.04 image, `--user` installs to `~/.local` and works without a venv
  (no PEP 668 block on user installs).
- There is no lint/test/build/serve target. "Running" the workspace means loading and
  processing the CSV/JSON data with Python + pandas. Sanity check after extracting:
  `python3 -c "import pandas as pd; print(len(pd.read_csv('Jobs/current_results.csv')))"`
  (expect `62` actionable roles; applied=22; employers=1523).
- Core invariant to preserve when editing the inventory: no URL from
  `applied_jobs.csv` may appear in `current_results.csv` (applied/rejected jobs are
  excluded), and `current_results.csv` URLs must be unique.
