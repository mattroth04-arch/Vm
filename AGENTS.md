# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **data-only "Job Search Workspace"**, not a deployable software
project. Future agents should not expect a runnable application, services, or a build.

### Repository contents
- `Readme.md` — single line ("Job Search Workspace").
- `Test.py` — a stub containing the literal word `test`; it is **not** a real test and
  raises `NameError` if executed. Do not treat it as a test target.
- `phase3c_sync_minimum.zip` — a **data-only** archive (no source code) containing:
  - `JOB_SEARCH_HANDOFF.md` — the authoritative project description / handoff.
  - `Jobs/employer_database/employer_database_master.csv` (~1,523 employers).
  - `Jobs/current_results.csv` (~62 actionable roles — single source of truth).
  - `Jobs/applied_jobs.csv` (~22 applied roles — excluded from results).
  - `Jobs/runs/phase3c_browser_queue_20260620.json` (Phase 3C queue).

### Environment / tooling
- **Runtime:** Python 3 only (3.12 present in this VM). The project's data can be read
  with the Python **standard library** (`csv`, `json`) — no third-party packages required.
- **No dependencies:** there is no `requirements.txt`, `pyproject.toml`, `package.json`,
  lockfile, or any package manager configured. There is nothing to install. The startup
  update script is intentionally a no-op runtime check.
- **No services:** no web server, API, database, queue, or frontend. It is a flat-file
  (CSV/JSON) batch/CLI pipeline driven by an AI agent.
- **No lint/build/test setup:** no linter, no build system, and no working test suite.

### Important caveat
- The Python pipeline scripts referenced throughout `JOB_SEARCH_HANDOFF.md`
  (`phase4_audit_rescore.py`, `round23_complete_search.py`,
  `phase3b_browser_recovery.py`, etc., expected under a `scripts/` folder) are **NOT
  present** in this repo or in the zip. The workspace cannot be run end-to-end until those
  scripts are recovered. Only the data artifacts are synced.
- To work with the data, extract the zip to a scratch location (e.g.
  `unzip phase3c_sync_minimum.zip -d /tmp/jobs_data`) rather than into the repo root; the
  handoff doc requires the workspace root to stay clean.
- Phase 3C browser automation (Playwright) is documented as failing under Docker seccomp
  (SIGTRAP) and is optional/blocked — not needed to read the existing data.
