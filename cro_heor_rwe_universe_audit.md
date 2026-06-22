# CRO / HEOR / RWE Discovery Agent C — Audit Report

## Mission

Build a master employer universe for Contract Research Organizations (CROs), Health Economics & Outcomes Research (HEOR), Real World Evidence (RWE), Medical Communications, Scientific Communications, Health Research Consulting, Clinical Research Consulting, Evidence Generation, Market Access, and Epidemiology Consulting.

## Methodology

- **Search engine:** Google (VM browser, human-style navigation)
- **Query:**

```
(
"CRO"
OR
"contract research organization"
OR
"clinical research organization"
OR
"health economics"
OR
HEOR
OR
"real world evidence"
OR
RWE
OR
"outcomes research"
OR
"medical communications"
OR
"scientific communications"
OR
"market access"
OR
"evidence generation"
OR
"epidemiology consulting"
OR
"health research consulting"
OR
"clinical consulting"
)
```

- **Included:** Organic search results only (company homepages acceptable)
- **Excluded:** AI Overview, sponsored results, Google Jobs, People Also Ask, LinkedIn, Indeed, Glassdoor, ZipRecruiter, job postings, directories, blogs, news articles, conference pages, vendor listings
- **Click policy:** Results opened only when organization legitimacy could not be determined from visible snippet
- **Deduplication:** Continuous by organization name and domain

## Stopping Rule

Stop when **three consecutive pages** each produce **fewer than two** new organizations.

**Triggered on pages 14–16** (0, 1, 0 new organizations respectively).

---

## Summary Statistics

| Metric | Value |
|---|---|
| Pages reviewed | 16 |
| Organizations discovered | 53 |
| Duplicates removed | 18 |
| Reason for stopping | Three consecutive pages (14, 15, 16) each produced fewer than 2 new organizations |

---

## New Organizations Per Page

| Page | New Orgs | Running Total | Notable Additions |
|---:|---:|---:|---|
| 1 | 5 | 5 | Worldwide Clinical Trials, PPD, Parexel, Emergent CRO, Amarex Clinical Research |
| 2 | 6 | 11 | ICON, Medpace, Clario, Analysis Group, IQVIA, Novotech CRO |
| 3 | 2 | 13 | Premier Research, Emmes Group |
| 4 | 4 | 17 | Certara, PharPoint Research, PSI CRO, OPEN Health |
| 5 | 6 | 23 | Flatiron Health, Costello Medical, Rho, Digital Health Outcomes, Ergomed, Atropos Health |
| 6 | 2 | 25 | CIBMTR, SCRI |
| 7 | 2 | 27 | Tranquil Clinical Research, Cromos Pharma |
| 8 | 3 | 30 | Total Trials, Komodo Health, Syneos Health |
| 9 | 5 | 35 | Sermes CRO, Allucent, Cytel, Cardinal Health |
| 10 | 6 | 41 | TFS HealthScience, Aurevia, KMK Consulting, Axina, Magnolia Market Access, Alira Health |
| 11 | 7 | 48 | Perisphere, Southern Research, MCT CRO, CMIC, CTI, Genesis Research Group, Verantos |
| 12 | 2 | 50 | Criterium CRO, Medicover Integrated Clinical Services |
| 13 | 3 | 53 | Avalere Health Advisory, Cencora, Veradigm |
| 14 | 0 | 53 | — |
| 15 | 1 | 54 → 53* | Advarra |
| 16 | 0 | 53 | — |

\*Final count adjusted to 53 after post-processing exclusion of NCBiotech CRO Collaborative (directory, not an employer).

**Trend:** `[5, 6, 2, 4, 6, 2, 2, 3, 5, 6, 7, 2, 3, 0, 1, 0]`

---

## Category Counts

Primary category assignment (organizations with multiple capabilities counted once by primary type):

| Category | Count |
|---|---|
| CRO | 27 |
| HEOR | 11 |
| RWE | 9 |
| Medical Communications | 2 |
| Research Consulting | 4 |
| Other | 0 |

### Category Notes

- **Research Consulting** includes market access consultancies (Magnolia Market Access, Genesis Research Group), CRO/regulatory consulting (Aurevia, Advarra), and hybrid consulting firms.
- **Medical Communications** entries (OPEN Health, Costello Medical) also provide HEOR/RWE services; primary type assigned from visible snippet emphasis.
- Organizations spanning multiple categories retain full type labels in the CSV `organization_type` field.

---

## Exclusions Applied During Post-Processing

| Excluded Item | Reason |
|---|---|
| NCBiotech — North Carolina CRO Collaborative | Directory/network listing, not a single employer |
| LinkedIn, Indeed, Glassdoor, ZipRecruiter results | Job boards (excluded per mission) |
| News articles, blogs, conference pages | Non-employer content |
| Duplicate appearances of major CROs | Deduplicated (18 removals across 16 pages) |

---

## Observations

1. **Early pages** surfaced large global CROs (PPD, ICON, Parexel, IQVIA, Medpace) and established HEOR firms (Analysis Group, Certara).
2. **Mid pages** added specialized RWE players (Flatiron Health, Komodo Health, Verantos, Perisphere) and regional CROs (MCT CRO, CMIC, Cromos Pharma).
3. **Late pages** showed diminishing returns — repeated mentions of already-cataloged firms and increasing share of job boards, news, and definitional content.
4. **Geographic diversity** includes US, European (Sermes, CMIC), and regional specialists (MCT CRO for Middle East/Africa).
5. **Industry convergence** is evident: many organizations span CRO, HEOR, and RWE (e.g., IQVIA, PPD, Ergomed, Genesis Research Group).

---

## Output Files

- `cro_heor_rwe_universe.csv` — 53 deduplicated organization records
- `cro_heor_rwe_universe_audit.md` — this audit report
