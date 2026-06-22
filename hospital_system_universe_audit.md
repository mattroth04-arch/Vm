# Hospital & Health System Discovery Agent B — Audit Report

**Mission:** Discover hospital systems, academic hospitals, children's hospitals, IDNs, VA medical centers, specialty hospitals, and regional health systems via Google organic search.

**Method:** VM browser only (human-like Google search). No Selenium, Playwright, Python scraping, HTML inspection, or employer website crawling.

**Search Query:**
```
("hospital system" OR "health system" OR "medical center" OR "children's hospital" OR "academic hospital" OR "integrated delivery network" OR "VA medical center" OR "regional medical center" OR "community health system" OR "teaching hospital") (epidemiology OR research OR population health OR analytics OR biostatistics OR quality OR public health)
```

**Exclusions Applied:** AI Overview, sponsored results, Google Jobs, People Also Ask, LinkedIn, Indeed, Glassdoor, ZipRecruiter, job boards, job postings, directories, blogs, articles, software vendors (Epic, Oracle Health), government agencies (CDC, AHRQ), academic schools/departments, social media, professional associations.

---

## Summary

| Metric | Value |
|--------|-------|
| **Pages reviewed** | 22 |
| **Organizations discovered** | 75 |
| **Duplicates removed** | 58 |
| **Reason for stopping** | Three consecutive pages (19, 20, 21) each produced fewer than 2 new organizations |

---

## New Organizations Per Page Trend

| Page | New Orgs | Notes |
|------|----------|-------|
| 1 | 5 | UVA Health, VA, NIH Clinical Center, VCU, Children's National |
| 2 | 4 | MedStar, Cheshire, Walter Reed, Dartmouth-Hitchcock |
| 3 | 5 | CentraCare, HCA Midwest, Inova, KU Medical Center, UMMS |
| 4 | 6 | CHOP, Cincinnati Children's, RWJBarnabas, Georgetown, Montefiore CHAM, Seattle Children's |
| 5 | 7 | Boston Children's, NYU Langone, Lurie, Mississippi Medical Center, Cheyenne Regional, Cedar Hill Regional |
| 6 | 7 | Mount Sinai, Penn Medicine, Boston Medical Center, Arkansas Children's, Vanderbilt, Utah Health, Northwell |
| 7 | 4 | Penn State Health, Cedars-Sinai, Rush, Hackensack Meridian |
| 8 | 4 | Rutgers Health, Care New England, Valley Health, Atrium Health |
| 9 | 7 | NYP, Mayo Clinic, Rady Children's, MaineHealth, UT Southwestern, Mass General Brigham, UC San Diego Health |
| 10 | 0 | All results duplicated page 9 organizations |
| 11 | 4 | Harris Health, Augusta Health, CHRIM Manitoba, UF Health |
| 12 | 5 | Nemours, Henry Ford, Lehigh Valley, Flushing Hospital, UNM Health |
| 13 | 3 | Baystate Health, Denver Health, Beacon Health System |
| 14 | 7 | Novant, Yale New Haven, SCRMC, Johns Hopkins, UW Health, Mount Carmel, Cambridge Health Alliance |
| 15 | 0 | Google pagination duplicate of page 14 results |
| 16 | 5 | Atlantic Health, Sutter Health, Tampa General, Virginia Mason Franciscan, Children's Nebraska |
| 17 | 1 | Marshfield Clinic Health System |
| 18 | 1 | Saint Alphonsus Health System |
| 19 | 0 | All major systems already captured |
| 20 | 0 | All major systems already captured |
| 21 | 1 | Wooster Community Hospital |
| 22 | 0 | Cambridge Health Alliance duplicate; session ended |

**Stopping trigger:** Pages 19 (0 new), 20 (0 new), and 21 (1 new) = three consecutive pages with fewer than 2 new organizations.

---

## Organization Type Breakdown

| Type | Count |
|------|-------|
| Academic Hospital | 28 |
| Hospital System | 18 |
| Children's Hospital | 14 |
| Regional Health System | 13 |
| VA Medical Center | 2 |
| Specialty Hospital | 1 |

---

## Duplicates Removed (58 total)

Duplicates were identified continuously by organization name and domain across all pages. Notable duplicate clusters:

- **VA / Walter Reed / military:** VA appeared on pages 1, 2, 17, 21
- **Academic giants:** Mayo, Mass General Brigham, NYP, Johns Hopkins, Penn Medicine appeared on multiple late pages
- **Children's hospitals:** CHOP, Cincinnati Children's, Seattle Children's, Rady Children's recurred frequently
- **Regional systems:** UVA Health, VCU, MedStar, Dartmouth-Hitchcock, Valley Health, Cheshire Medical Center
- **Page 15:** Entire page was a Google pagination duplicate of page 14 (7 duplicate results, 0 new)

---

## Top New Health Systems Discovered

Ranked by prominence and confidence from late-discovery pages and high-impact systems found across the search:

1. **Johns Hopkins Medicine** (Page 14) — Major academic medical center with children's hospitals
2. **Mayo Clinic** (Page 9) — National multi-state academic health system and research enterprise
3. **Mass General Brigham** (Page 9) — Largest Massachusetts integrated academic system ($2B+ research)
4. **Northwell Health** (Page 6) — Largest NY tri-state health system
5. **Atrium Health** (Page 8) — Major Southeast integrated delivery network
6. **Hackensack Meridian Health** (Page 7) — New Jersey's largest integrated health system
7. **Sutter Health** (Page 16) — Major California not-for-profit regional system
8. **Henry Ford Health** (Page 12) — Detroit integrated delivery network with major research
9. **Novant Health** (Page 14) — Southeast regional system with clinical research focus
10. **Saint Alphonsus Health System** (Page 18) — Last meaningful new regional Catholic IDN before diminishing returns

---

## Session Notes

- Results were extracted from visible Google organic snippets without clicking unless legitimacy could not be determined from the snippet alone.
- HCA Healthcare parent system was noted on page 11 but only HCA Midwest Research Medical Center was captured as a distinct entry from page 3.
- Cedar Hill Regional Medical Center and CHRIM Manitoba included with medium confidence due to indirect URL visibility in snippets.
- Wooster Community Hospital included with medium confidence as an independent community hospital.
- International organization (CHRIM Manitoba) included as a legitimate children's hospital research institute discovered in organic results.

---

## Output Files

- `hospital_system_universe.csv` — 75 deduplicated organization records
- `hospital_system_universe_audit.md` — This audit report
