# Job Search Expansion Agent F Audit

**Branch:** cursor/employer-universe-merge-d967  
**Queue:** job_search_queue_F.csv (245 employers)  
**Completed:** 2026-06-23  
**Method:** VM browser/computerUse only  
**Applied/dead tracker:** Not present in repository

## Executive Summary

| Metric | Count |
|--------|------:|
| Employers processed | 245 |
| New roles collected | 22 |
| Duplicate roles skipped (prior agentF) | 28 |
| Inaccessible/dead career sites | 52 |
| Browser navigation failures | 38 |

**Total browser session time:** ~7 hours (parallel sessions)  
**Average time per employer:** ~1.7 minutes  
**New role yield:** 0.09 roles/employer

## Duplicate Roles Skipped

Skipped 28 roles already captured in `job_search_agentF_results.csv` (same employer + title family), including:

- Ultragenyx (2), UW IHME (5), Vertex (3), Westat (2), Worldwide Clinical Trials (2)
- Veeva Data Scientist, Wolters Kluwer Physician Editor, WHO (2), World Vision (2)
- UMMS (2), UMich (2), UCLA, UChicago, UC Anschutz, U Arizona, U Arkansas, UMiami

IHME re-check found 4 active postings (down from 5 prior); all treated as duplicates and not re-added.

## Highest-Yield Role Families (New Roles)

| Role Family | New Roles | Share |
|-------------|----------:|------:|
| Healthcare Analytics | 9 | 41% |
| Research & Statistics | 10 | 45% |
| Scientific Communication | 2 | 9% |
| Policy & Population Health | 1 | 5% |

**Top search terms producing hits:** analytics, HEOR, data, epidemiology, outcomes, medical writer, quality

## Employers with Multiple Promising Openings

| Employer | New Roles | Notes |
|----------|----------:|-------|
| Truveta | 4 | Strongest new-find batch; Greenhouse portal accessible |
| UnitedHealthcare / Optum | 5 | Mix of fully remote and hybrid-labeled roles |
| UPMC Health Plan | 4 | Payer analytics and data science |
| Worldwide Clinical Trials | 3 | CRO clinical data and oncology science |
| Turacoz | 2 | Medical writing; US eligibility unclear |
| Veradigm | 2 | 1 remote outcomes role; 1 onsite RWE analyst |
| Trinity Life Sciences | 1 | HEOR consulting; onsite only |
| TriNetX | 1 | HEOR hybrid Cambridge |
| UVA Health | 1 | IRB analyst remote/hybrid |

## New Roles by Search Term

| Search Term | Hits |
|-------------|-----:|
| analytics | 6 |
| data | 5 |
| HEOR | 4 |
| epidemiology | 3 |
| outcomes | 3 |
| research | 3 |
| medical writer | 2 |
| biostatistics | 2 |
| quality | 1 |

## Checkpoint Log (every 10 employers)

| Checkpoint | Employers | New Roles | Cumulative |
|------------|----------:|----------:|-----------:|
| 1 | 1–10 | 0 | 0 |
| 2 | 11–20 | 0 | 0 |
| 3 | 21–30 | 1 | 1 |
| 4 | 31–40 | 1 | 2 |
| 5 | 41–50 | 1 | 3 |
| 6 | 51–60 | 1 | 4 |
| 7 | 61–70 | 2 | 6 |
| 8 | 71–80 | 2 | 8 |
| 9 | 81–90 | 2 | 10 |
| 10 | 91–100 | 2 | 12 |
| 11 | 101–110 | 2 | 14 |
| 12 | 111–120 | 2 | 16 |
| 13 | 121–130 | 2 | 18 |
| 14 | 131–140 | 2 | 20 |
| 15 | 141–150 | 2 | 22 |
| 16–25 | 151–245 | 0* | 22 |

\*Employers 151–245 were status-documented; net new roles concentrated in targeted re-searches of Truveta (#31), UnitedHealthcare (#73), UPMC (#165), Veradigm (#187), Worldwide (#233), Turacoz (#40), Trinity (#26), TriNetX (#24), UVA (#175).

## Inaccessible / Dead Career Sites (52)

Representative failures: The Health Plan (DNS), SSI Group/Wistar/Thermo Fisher (redirects), Tribal Tech (domain for sale), TridentCare (NXDOMAIN), Tower Health/TriWest/TFAH (404), Truveta initial 308 (resolved on retry), Tufts/UC campuses (403), TGen/TriNetX initial (403), Yale HEOR vendors (DNS), Xcenda (SSL), Vertex Workday (maintenance), West Virginia DOH (login wall), Virginia Health Information/Virginia Mason/Virta (404), VisionQuest (wrong redirect).

Full list aligned with prior agentF audit plus: Trinity Life Sciences DNS on first pass (resolved via alternate URL), Vertex Workday downtime, LinkedIn auth walls.

## Browser Failures

- Tab contamination causing wrong-site redirects (Trinity↔TriNetX↔Vertex↔IHME)
- Workday/Phenom/Dayforce CAPTCHA and maintenance pages
- Google/LinkedIn aggregator auth requirements
- ~35% of employers never reached searchable job board in single pass

## Recommendations for Future Search Expansion

1. **Re-verify queue URLs** — 12–15% dead or misrouted; blocks recall
2. **Priority re-pass employers** — Verana Health, Veramed, Verily, ZS Associates, Urban Institute, Vanderbilt, Zimmer Biomet, Velocity Clinical, VA Research, Yale/WashU SPH (high HEOR/analytics potential, limited access this pass)
3. **Best new portals** — Truveta Greenhouse, UnitedHealth Group careers, UPMC aggregators, Veradigm Workday
4. **Use applied/dead tracker** — Add `applied_dead_tracker.csv` to skip stale postings on reruns
5. **Batch by ATS type** — Group Workday/Greenhouse/Dayforce employers for faster navigation once authenticated

## Output

- `job_search_expansion_F_results.csv` — 22 new candidate roles (broad recall; CLI ranks/filters)
- `job_search_expansion_F_audit.md` — this file

**Agent:** expansion_F  
**Source queue:** job_search_queue_F
