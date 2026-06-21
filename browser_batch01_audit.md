# Phase 3C Browser Pilot — Batch 01 Audit

**Date:** 2026-06-21
**Source queue:** `Jobs/runs/phase3c_browser_queue_20260620.json` (835 employers total; 514 browser-recoverable)
**Scope:** First 25 employers (priority bucket: Workday), processed via the `computerUse` desktop Chrome browser as a human user.
**Method:** For each employer — navigate to career URL, reach the JS-rendered job-listing/search page, run keyword searches, open matching postings, and record results. Anchor search terms: epidemiology, HEOR / health economics, biostatistics, public health, medical writing, health analytics, research scientist, outcomes research, data scientist.
**Output data:** `browser_batch01_results.csv` (25 employers, 14 captured role rows).

> Note: The queue classified all 25 as "Workday", but live inspection showed several are actually on other systems (Greenhouse, Oracle Cloud HCM, Avature, CGI Njoyn, custom portals). The observed system is recorded per employer in the `ats_observed` column.

---

## 1. Results summary

| Outcome (per employer) | Count |
|------------------------|------:|
| ROLES_FOUND (≥1 keyword match opened) | 11 |
| SEARCHED_NO_MATCH | 12 |
| BLOCKED | 1 |
| DEAD_URL | 1 |
| **Total processed** | **25** |

- **Employers searched successfully (UI search completed):** 21 / 25
- **Total role rows captured:** 14 (across the 11 ROLES_FOUND employers)

## 2. Browser failures (could not complete a UI search)

| Employer | Type | Reason |
|----------|------|--------|
| Atrium Health | BLOCKED | Cloudflare "Verify you are human" CAPTCHA — not bypassed per protocol |
| CMI Media Group | DEAD_URL | SSL error `NET::ERR_CERT_COMMON_NAME_INVALID` — site did not load |

**Degraded / partial (loaded but search impaired):** CGI Federal (search form cleared, non-functional), CHI Health (search redirected to homepage), CSULB Health Science (careers URL 404; fell back to 4 PDF postings), Apellis (custom page, category filters only — no keyword search).

So: **2 hard browser failures** (1 blocked, 1 dead URL) + **4 degraded/partial** sites where a normal keyword search was not possible.

## 3. Qualifying roles (strict filter: fully remote-US + on-target role)

| Employer | Title | Remote | Salary | Verdict |
|----------|-------|--------|--------|---------|
| AdventHealth | Health Economist | Fully Remote (US) | $91,313.86 – $169,845.73 | **Qualifying** — strong target-role + remote-US match |
| Argenx | Medical Safety Lead | United States – Remote | n/a | Borderline — remote-US but pharmacovigilance/safety role (evaluate fit) |

**Result: 1 clearly qualifying remote-US target role (AdventHealth Health Economist), plus 1 borderline remote-US match (Argenx Medical Safety Lead).**

Other roles surfaced but did **not** qualify under the strict remote/role gate:
- On-site: Abbott (HEOR Manager, CA), BAE (Data Scientist, VA, TS/SCI), BCBSA (Data Engineer / Product Strategy Lead, Chicago), Beth Israel (Sr AI Data Scientist, MA), CSL Behring (Assoc Dir Biostatistics, MA).
- Hybrid: Broad Institute (Computational Scientist I, Cambridge MA).
- Non-US: ApotheCom (Sr Medical Writer, UK), Argenx (Biomarker Biostatistics Lead, Belgium), Capgemini (Lead Data Scientist, UK).
- Remote but non-target role: Bausch Health (Sr Brand Manager, NJ), Castlight/Mosaic (RN Care Guide — clinical).

## 4. ATS reality vs. queue classification

| Observed system | Employers |
|-----------------|-----------|
| Workday (confirmed tenant) | AdventHealth, Agilon, Argenx, Auburn, BAE, BCBSA, Bausch, BioCryst, Castlight/Vera |
| Custom / corporate portal | Abbott, Accenture, Amentum, Apellis, CSL, Capgemini |
| Greenhouse | ApotheCom |
| Oracle Cloud HCM / Taleo | Atlantic Health, Baylor |
| Avature | Broad Institute |
| CGI Njoyn | CGI Federal |
| CommonSpirit (custom) | CHI Health |
| Unknown (blocked) | Atrium Health |
| Dead URL | CMI Media Group |

**Takeaway:** ~36% of this "Workday" batch was not actually Workday on the live site. Browser recovery is system-agnostic (it worked across Workday, Greenhouse, Oracle, Avature), which is the core value this pilot was meant to validate.

## 5. Timing & extrapolation

- **Wall-clock for 25 employers:** ~85 min (≈ **3.4 min/employer**). This includes ~16 min of orchestration/idle time between batches; effective active browser time is ≈ **2.8 min/employer**.
- **Remaining queue:** 835 − 25 = **810 employers**.

| Basis | Per-employer | Remaining employers | Estimated runtime |
|-------|-------------:|--------------------:|------------------:|
| Full remaining queue @ wall-clock | 3.4 min | 810 | ~46 hours |
| Full remaining queue @ active | 2.8 min | 810 | ~38 hours |
| Browser-recoverable only @ wall-clock | 3.4 min | ~489 | ~28 hours |
| Browser-recoverable only @ active | 2.8 min | ~489 | ~23 hours |

These are sequential single-browser estimates; parallelizing browser workers would reduce wall-clock proportionally.

## 6. Pilot validation verdict

The browser-driven discovery approach **works** and recovers searchable inventory that the API/HTTP phases (3A/3B) could not:
- Reached JS-rendered job boards, executed keyword searches, opened postings, and extracted title / remote status / salary across 21 of 25 employers and multiple ATS types.
- Surfaced a genuine net-new qualifying remote-US role (AdventHealth Health Economist) plus a borderline remote-US match (Argenx).
- Correctly honored CAPTCHA/bot-protection and dead-URL rules (no bypass), and revealed that the queue's ATS labels are unreliable on live sites.

**Recommendation:** Proceed to scale, prioritizing the ~489 remaining browser-recoverable employers first. Expect a low qualifying-hit rate (~1 strong qualifying role per ~25 employers in this batch), so the value is in coverage completeness, consistent with the project's coverage-maximization goal.

## 7. Constraints honored

- Did **not** modify `current_results.csv`, `applied_jobs.csv`, `master_seen_jobs.csv`, or any authoritative inventory.
- Did **not** modify PythonAnywhere.
- Did **not** bypass CAPTCHA, login walls, or bot protection.
- Committed only `browser_batch01_results.csv` and `browser_batch01_audit.md`.
