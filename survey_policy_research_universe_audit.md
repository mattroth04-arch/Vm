# Survey / Policy Research Employer Universe — Discovery Audit

## Mission

Build a master employer universe for survey research, program evaluation, policy research, health services research, social science research, statistical consulting, and related applied research organizations using Google organic search discovery via the VM browser.

## Search Query

```
("survey research organization" OR "program evaluation firm" OR "policy research institute" OR "health services research organization" OR "social science research organization" OR "statistical consulting firm" OR "applied research institute" OR "independent research organization" OR "public policy research organization" OR "evaluation consulting firm" OR "research and evaluation organization" OR "research contractor" OR "survey methodology organization")
```

## Methodology

- Used the built-in VM browser (Chrome) to search Google and read organic results only.
- Ignored AI Overview, sponsored results, Google Jobs, and People Also Ask.
- Opened result links only when the organization could not be identified from the visible snippet.
- Excluded LinkedIn, Indeed, Glassdoor, ZipRecruiter, job postings, blogs, directories, conference pages, news articles, and generic resource lists.
- Deduplicated continuously by organization name and domain.
- Paginated through Google results until the stop condition was met.

## Stop Condition

Stop when **three consecutive pages** each produce **fewer than two new organizations**.

**Stop condition met on pages 15, 16, and 17:**

| Page | New organizations (raw discovery) |
|------|-----------------------------------|
| 15   | 1                                 |
| 16   | 0                                 |
| 17   | 0                                 |

## Pages Reviewed

**17 pages total** (Google results pages 1 through 17).

## New Organizations Per Page (Raw Discovery)

| Page | New orgs | Notes |
|------|----------|-------|
| 1    | 6        | Strong initial yield of policy and evaluation firms |
| 2    | 6        | University policy institutes and IFPRI |
| 3    | 7        | Evaluation consulting firms |
| 4    | 4        | Health and state policy institutes |
| 5    | 7        | Education and border policy institutes |
| 6    | 4        | Social policy and Japan policy institutes |
| 7    | 7        | Health policy and international institutes |
| 8    | 5        | Statistical consulting and health services research |
| 9    | 4        | Criminal justice and child policy institutes |
| 10   | 6        | International and applied research institutes |
| 11   | 4        | Additional university and international policy institutes |
| 12   | 3        | Japan ocean policy and evaluation consulting |
| 13   | 1        | USC homelessness policy institute |
| 14   | 2        | University applied research profiles |
| 15   | 1        | Statistical/program evaluation firm |
| 16   | 0        | All duplicates or excluded results |
| 17   | 0        | All duplicates or excluded results |

**Trend:** High yield on pages 1–12 (3–7 new orgs per page), declining on pages 13–15 (1–2 new orgs), then zero new orgs on pages 16–17.

## Summary Statistics

| Metric | Count |
|--------|-------|
| Pages reviewed | 17 |
| Raw organizations discovered (before cleanup) | ~54 |
| Final unique organizations (after dedup and exclusion cleanup) | **41** |
| Duplicates removed (encountered during pagination) | **67** |
| Excluded results (not counted as organizations) | **~75** |

## Exclusion Cleanup Applied to Final Universe

The following raw discoveries were removed during final curation:

| Result | Reason excluded |
|--------|-----------------|
| Homelessness Policy Research Institute (research.usc.edu/news) | News article, not organization homepage |
| Defense Innovation Unit (diu.mil) | Government defense unit, not target research employer type |
| HEI Health Education Research Evaluation (highergov.com) | Government contract directory |
| Applied Research Institute (govtribe.com) | Vendor directory listing |
| Applied Research Institute (sossecinc.com) | Consortium directory listing |
| SPRI Global (devex.com) | Directory listing; kept spriglobal.org homepage |
| Community Advocacy Research & Evaluation (idealist.org) | Directory listing without org homepage |
| Applied Research Institute Illinois (experts.illinois.edu) | Institutional profile directory |
| Ocean Policy Research Institute (tethys.pnnl.gov) | Project database page at national lab |
| Policy Research Institute (mof.go.jp) | Government ministry page, not independent institute |
| Porsesh Policy Research Institute (Facebook only) | Social media listing; kept prresearch.us |

## Category Counts (Final Universe)

| Category | Count |
|----------|-------|
| Survey Research | 0 |
| Program Evaluation | 9 |
| Policy Research | 26 |
| Health Services Research | 2 |
| Social Science Research | 1 |
| Statistical Consulting | 2 |
| Applied Research | 1 |
| Other | 0 |
| **Total** | **41** |

## Confidence Distribution

| Confidence | Count |
|------------|-------|
| High | 41 |
| Medium | 0 |
| Low | 0 |

## Reason for Stopping

Three consecutive Google result pages (15, 16, 17) each produced fewer than two new organizations (1, 0, and 0 respectively). Pages 16 and 17 contained only previously discovered organizations or excluded result types (job sites, news, directories, social media, academic articles). The search query was sufficiently exhausted for meaningful new employer discovery.

## Output File

- `survey_policy_research_universe.csv` — 41 deduplicated organization records with organization name, visible URL, domain, type, specialty, confidence, and notes.
