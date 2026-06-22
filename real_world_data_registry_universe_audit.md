# Real-World Data / Registry / Health Data Network Discovery Audit

## Mission Summary

Built a master employer universe for real-world data companies, clinical and patient registries, health data networks, claims/EHR data companies, health information exchanges, and evidence generation platforms using Google organic search results only (VM browser, human-style workflow).

**Search query:**

```
("real world data company" OR "real world evidence platform" OR "clinical registry" OR "patient registry" OR "health data network" OR "clinical quality registry" OR "observational research network" OR "claims data company" OR "EHR data company" OR "patient data platform" OR "health information exchange" OR "clinical data research network" OR "specialty registry" OR "evidence generation platform" OR "health data collaborative")
```

## Final Statistics

| Metric | Value |
|---|---|
| Pages reviewed | 20 |
| Organizations discovered | 44 |
| Duplicates removed | 8 |
| Output records (unique) | 44 |

## Reason for Stopping

**Stopping criteria met:** three consecutive pages (18, 19, 20) each produced fewer than two new organizations (0, 0, 0).

Earlier pages still yielded occasional new state HIEs and registry organizations (e.g., page 17 added 2), but by page 18 results were dominated by educational institutions, generic government pages, statutes, and previously captured duplicates.

## New Organizations Per Page

| Page | New orgs | Running total | Duplicates skipped |
|---:|---:|---:|---:|
| 1 | 6 | 6 | 0 |
| 2 | 7 | 13 | 1 |
| 3 | 6 | 19 | 0 |
| 4 | 4 | 23 | 0 |
| 5 | 2 | 25 | 0 |
| 6 | 1 | 26 | 2 |
| 7 | 4 | 30 | 0 |
| 8 | 2 | 32 | 1 |
| 9 | 1 | 33 | 1 |
| 10 | 3 | 36 | 0 |
| 11 | 1 | 37 | 0 |
| 12 | 2 | 39 | 0 |
| 13 | 0 | 39 | 0 |
| 14 | 4 | 43 | 0 |
| 15 | 0 | 43 | 0 |
| 16 | 0 | 43 | 1 |
| 17 | 2 | 44 | 2 |
| 18 | 0 | 44 | 1 |
| 19 | 0 | 44 | 2 |
| 20 | 0 | 44 | 1 |

**Trend:** `[6, 7, 6, 4, 2, 1, 4, 2, 1, 3, 1, 2, 0, 4, 0, 0, 2, 0, 0, 0]`

## Category Counts

| Category | Count |
|---|---:|
| Real-World Data | 6 |
| Clinical Registry | 5 |
| Patient Registry | 10 |
| Health Data Network | 6 |
| Claims Data | 0 |
| EHR Data | 1 |
| Health Information Exchange | 14 |
| Evidence Generation | 2 |
| Other | 0 |

## Methodology Notes

### Included
- Organic Google result snippets where organization identity was clear without clicking
- Government registry programs, state HIEs, specialty society patient registries, and commercial RWE/RWD platforms
- Organization homepages or clearly organizational landing pages when the visible result pointed to a subpage but the employer was unambiguous

### Excluded
- Sponsored results, AI Overviews, Google Jobs, People Also Ask
- LinkedIn, Indeed, Glassdoor, ZipRecruiter, and job postings
- News articles, academic journals, conference pages, and market-research listicles
- Generic directories (e.g., Datarade health data marketplace listing)
- Educational institutions, social media, and individual healthcare clinics unless they operate a distinct HIE/registry program
- Blogs used only as evidence of exclusion; legitimate employers discovered via blog snippets were retained with homepage URLs

### Deduplication
Duplicates matched primarily by registrable domain (e.g., NIH/NCBI, repeated IQVIA, WHO, ONC, Veradigm, WeGuide, ECFS, H1, Pro Pharma).

## Notable Gaps

- **Claims Data (0):** No dedicated claims-data vendors surfaced as distinct organic results under this query phrasing; several RWD platforms (Scalence, IntuitionLabs, Veradigm) reference claims integration but were classified by primary type.
- **Late-page saturation:** Pages 13–16 and 18–20 were dominated by colleges, generic .gov pages, and duplicates—indicating query exhaustion for net-new employers.

## Deliverables

- `real_world_data_registry_universe.csv` — 44 unique organization records
- `real_world_data_registry_universe_audit.md` — this audit report
