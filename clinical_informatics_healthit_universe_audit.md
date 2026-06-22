# Clinical Informatics / Health IT Employer Universe — Discovery Audit

## Mission

Build a master employer universe for clinical informatics, EHR, health IT, interoperability, FHIR, clinical decision support, HIE, clinical data platform, healthcare software, patient data infrastructure, and population health technology organizations.

## Method

- **Search engine:** Google (built-in VM browser only)
- **Query:**
  ```
  ("clinical informatics company" OR "EHR company" OR "electronic health record company" OR "health IT company" OR "healthcare interoperability company" OR "FHIR company" OR "clinical decision support company" OR "health information exchange" OR "clinical data platform" OR "healthcare software company" OR "patient data infrastructure" OR "population health technology" OR "clinical analytics platform")
  ```
- **Results processed:** Organic Google results only
- **Excluded:** AI Overview, sponsored results, Google Jobs, People Also Ask, LinkedIn, Indeed, Glassdoor, ZipRecruiter, job postings, blogs, news articles, generic directories, conference pages, government-only pages, academic papers, foreign-only entities without US healthcare IT relevance

## Stopping Condition

Stop when **three consecutive pages** each produce **fewer than two** new organizations (0 or 1 new per page).

**Status: MET on page 21**

| Page | New Orgs | Cumulative Unique |
|------|----------|-------------------|
| 1 | 3 | 3 |
| 2 | 3 | 6 |
| 3 | 4 | 10 |
| 4 | 5 | 15 |
| 5 | 3 | 18 |
| 6 | 6 | 24 |
| 7 | 2 | 26 |
| 8 | 3 | 29 |
| 9 | 1 | 30 |
| 10 | 4 | 34 |
| 11 | 2 | 36 |
| 12 | 3 | 39 |
| 13 | 5 | 44 |
| 14 | 6 | 50 |
| 15 | 3 | 53 |
| 16 | 3 | 56 |
| 17 | 0 | 56 |
| 18 | 2 | 58 |
| 19 | 0 | 58 |
| 20 | 0 | 58 |
| 21 | 0 | 58 |

Pages **19, 20, and 21** each produced **0** new organizations, satisfying the stopping rule.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Pages reviewed | 21 |
| Organizations discovered | 58 |
| Duplicates removed | 13 |
| Reason for stopping | Three consecutive pages (19–21) each produced fewer than 2 new organizations |

### New Organizations Per Page Trend

```
Page:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
New:   3  3  4  5  3  6  2  3  1  4  2  3  5  6  3  3  0  2  0  0  0
```

Early pages (1–6, 12–16) yielded strong discovery rates (3–7 new orgs/page). Discovery tapered after page 17, with pages 17, 19, 20, and 21 yielding 0–1 new orgs. The three-page zero-yield streak on pages 19–21 triggered stop.

### Duplicates Removed (13 total)

Organizations encountered on multiple pages and deduplicated by domain/name:

- Trenton Health Team (pages 3, 4)
- Healthix (pages 5, 6)
- CRISP (pages 4, 5)
- Orion Health (pages 4, 6)
- Florida HIE Services (pages 6, 7)
- Indiana HIE / IHIE (pages 6, 7)
- Metriport (pages 6, 8)
- Health Gorilla (pages 8, 9)
- OpenHIE (pages 10, 11)
- NextGen Healthcare (pages 10, 11)
- Edenlab (pages 11, 12)
- Osplabs (pages 10, 14)

### Excluded During Review

| Entity | Reason |
|--------|--------|
| Datalink Software | Blog/content page, not organization homepage |
| Wikipedia, NIH, CMS, HHS pages | Government/academic reference, not employer |
| LinkedIn, Indeed, Glassdoor results | Job board exclusion |
| UK NHS Digital, foreign-only entities | Non-US or non-qualifying on pages 19–21 |

## Category Counts

| Organization Type | Count |
|-------------------|-------|
| Clinical Informatics | 0 |
| EHR | 5 |
| Health IT | 4 |
| Interoperability | 7 |
| FHIR | 4 |
| Clinical Decision Support | 0 |
| HIE | 25 |
| Clinical Data Platform | 3 |
| Healthcare Software | 10 |
| Other | 0 |

### Category Notes

- **HIE (25):** Dominant category; query heavily matched "health information exchange" phrasing in organic results.
- **EHR (5):** Epic, Oracle Health, MEDITECH, Azalea Health, NextGen Healthcare.
- **Interoperability (7):** Orion Health, Health Gorilla, OpenHIE, InterSystems, 4Medica, Lifepoint Informatics, Forum Systems.
- **FHIR (4):** Metriport, Edenlab, Telstra Health, Outcome Healthcare.
- **Clinical Data Platform (3):** IQVIA, Decipher, Inovalon.
- **Healthcare Software (10):** The SSI Group, MDinteractive, JetBase, ScienceSoft, Osplabs, 1st Providers Choice, GRM Document Management, Mindbowser, PointClickCare, Glorium Technologies.
- **Health IT (4):** Synapse Health, Datavant, Cloudticity, Verato.
- **Clinical Informatics / Clinical Decision Support / Other:** No qualifying organic homepage results surfaced with sufficient confidence on reviewed pages; these categories may require alternate search queries in future passes.

## Confidence Distribution

| Confidence | Count |
|------------|-------|
| High | 52 |
| Medium | 7 |
| Low | 0 |

## Output Files

- `clinical_informatics_healthit_universe.csv` — 58 unique organizations with URL, domain, type, specialty, confidence, and notes
- `clinical_informatics_healthit_universe_audit.md` — This audit report

## Limitations

1. Query phrasing skewed results toward HIE organizations; EHR vendors and clinical informatics consultancies were underrepresented relative to HIE.
2. Some consulting/software-development firms (ScienceSoft, Mindbowser, Glorium Technologies) included where HIE software was a stated specialty.
3. Organization type assigned from visible Google snippet and homepage domain; not all homepages were visited.
4. US-focused discovery; limited international vendors retained only where clearly health-IT relevant (e.g., Telstra Health, Orion Health).
