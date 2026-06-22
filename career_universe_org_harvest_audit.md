# Career Universe Organization Harvest Audit

## Summary

| Metric | Count |
|--------|-------|
| Google result pages reviewed | 15 |
| Raw organic results reviewed | ~125 |
| Unique organizations found | 90 |
| Duplicates removed | 12 |
| Excluded job boards | ~20 |
| Excluded individual postings | ~15 |
| Excluded non-employers (blogs, directories, irrelevant) | ~18 |

## Search Query

```
("company" OR "organization" OR "institute" OR "center" OR "laboratory" OR "firm" OR "agency" OR "foundation" OR "consulting" OR "solutions" OR "services" OR "partners" OR "group" OR "school of public health" OR "academic medical center" OR "hospital system" OR "CRO" OR "biotech" OR "pharma" OR "medical communications" OR "digital health" OR "health analytics" OR "health technology") ("epidemiology" OR "biostatistics" OR "public health" OR "health economics" OR HEOR OR RWE OR "real world evidence" OR "outcomes research" OR "medical writing" OR "clinical research" OR "research scientist" OR "healthcare analytics" OR "health data science" OR "population health" OR bioinformatics OR "program evaluation")
```

## Methodology

- Used **built-in VM browser only** (computerUse) — no Selenium, Playwright, Python harvesting, console, page source, or HTML scraping.
- Organization-focused query (not job-focused); accepted homepages, about pages, and organization pages.
- Ignored AI Overview, Google Jobs widgets, and sponsored results.
- Read visible organic results (title, URL, snippet) across pages 1–15.
- Did not open result links unless ambiguous.
- Deduplicated by domain; excluded job boards, individual postings, blogs, and non-health employers.

## Category Counts

| Category | Count |
|----------|-------|
| University | 26 |
| Academic Medical Center | 18 |
| Research Institute | 9 |
| Hospital System | 7 |
| Government | 7 |
| Nonprofit | 5 |
| CRO | 4 |
| Public Health Organization | 3 |
| Consulting | 3 |
| Pharmaceutical | 2 |
| Insurance | 2 |
| Medical Device | 1 |
| Healthcare Analytics | 1 |
| Digital Health | 1 |
| Health Technology | 1 |

## Exclusions Applied During Curation

- **Job boards:** LinkedIn, Indeed, Glassdoor, ZipRecruiter (~20 instances)
- **Individual postings:** Specific role listings excluded (~15)
- **Non-health employers:** Xerces Society, Statue of Liberty Foundation, NCHEMS, WMO
- **Peripheral/low relevance:** INFORMS, CAHIIM, AAHRPP, Global Institute ASU
- **Duplicate domains merged:** Cedars-Sinai, National Academy of Medicine, UCLA Fielding, UCI Health, UIC, ONC/healthit.gov, UNC Health, UC Health

## High-Confidence New Employer Examples

- **Syneos Health** (`syneoshealth.com`) — Major global CRO for epidemiology, biostatistics, HEOR, and RWE
- **IQVIA** (`iqvia.com`) — World's largest healthcare data and analytics company
- **Johns Hopkins Bloomberg School of Public Health** (`publichealth.jhu.edu`) — Premier global school of public health
- **PPD (Thermo Fisher)** (`ppd.com`) — Major contract research organization
- **RAND Corporation** (`rand.org`) — Policy research with major health economics division
- **McKinsey Health Institute** (`mckinsey.com`) — Healthcare consulting employing health economists
- **Partners In Health** (`pih.org`) — Global health nonprofit for program evaluation
- **Ipsen** (`ipsen.com`) — Mid-size pharmaceutical with HEOR and clinical development
- **AcademyHealth** (`academyhealth.org`) — Professional organization for health services research
- **NCQA** (`ncqa.org`) — Healthcare quality and outcomes measurement organization
- **Mayo Clinic** (`college.mayo.edu`) — Premier academic medical center and research
- **MD Anderson Cancer Center** (`mdanderson.org`) — Top cancer center for epidemiology and biostatistics
- **Bain & Company** (`bain.com`) — Management consulting with healthcare practice
- **Bloomberg Philanthropies** (`bloomberg.org`) — Major public health funder and data initiatives
- **City of Hope** (`cityofhope.org`) — NCI-designated comprehensive cancer center

## Recommended High-Value Categories

1. **University / School of Public Health** — Densest category; top employers for epidemiology and biostatistics faculty/research
2. **Academic Medical Center** — Clinical research, population health, outcomes research roles
3. **CRO** — IQVIA, Syneos Health, PPD, Labcorp for clinical trials and RWE
4. **Government** — NIH, NCI, AHRQ, HRSA, state health departments
5. **Research Institute** — RAND, MD Anderson, Roswell Park, Wistar, City of Hope
6. **Consulting** — McKinsey Health Institute, Bain, EY for health economics and analytics
7. **Pharmaceutical / Biotech** — BMS, Ipsen for HEOR, medical affairs, clinical development
