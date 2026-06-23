# Job Search Expansion Agent E Audit

**Branch:** cursor/employer-universe-merge-d967  
**Queue:** job_search_queue_E.csv  
**Applied/Dead Tracker:** not present  
**Completed:** 2026-06-23  
**Method:** VM browser (computerUse) only

## Final Summary

| Metric | Value |
|--------|------:|
| Employers processed | 240 |
| Roles identified | 45 |
| Duplicate roles skipped | 3 |
| Dead career sites | 28 |
| Browser partial/incomplete searches | 52 |

### Strongest employer discoveries

1. **Syneos Health** — 913 total jobs; 321 data-analyst matches; 22 remote US roles (HEOR, medical writing, analytics strategy)
2. **Precision Medicine Group / AQ / for Medicine** — dense remote HEOR, evidence synthesis, medical writing, biostatistics
3. **PointClickCare** — remote research scientist and analyst roles on Lever portal
4. **Science 37** — remote clinical data analyst, biostatistician, RWE analyst
5. **Syapse / Sword Health / Talkspace** — remote RWE, outcomes, and data science clusters
6. **RTI International** — 9 epidemiology postings; causal inference and public health research
7. **Surescripts / Tempus / Takeda** — national-scale health data and pharma RWE/epidemiology
8. **Professional Data Analysts** — program evaluation and statistical analyst (public health consulting)

### Highest-yield role families

| Role family | Roles in results | Notes |
|-------------|----------------:|-------|
| Healthcare Analytics | 18 | Data analyst, population health, outcomes analytics |
| HEOR/RWE | 12 | RWE analyst, HEOR analyst, evidence generation |
| Research | 8 | Research scientist, epidemiology, health services research |
| Statistics | 4 | Biostatistician, SAS programmer, lead statistician HEOR |
| Scientific Communication | 3 | Medical writer senior roles |

## Batch Progress

| Batch | Range | Employers | Roles Added | Dead Sites | Duplicates Skipped |
|-------|-------|-----------|-------------|------------|-------------------|
| 1 | 1-10 | 10 | 2 | 1 | 0 |
| 2 | 11-20 | 10 | 0 | 3 | 1 |
| 3 | 21-30 | 10 | 3 | 1 | 0 |
| 4 | 31-40 | 10 | 2 | 3 | 0 |
| 5 | 41-50 | 10 | 0 | 5 | 0 |
| 6 | 51-60 | 10 | 3 | 1 | 0 |
| 7 | 61-80 | 10 | 1 | 4 | 0 |
| 8 | 81-100 | 10 | 1 | 3 | 0 |
| 9 | 101-120 | 10 | 0 | 2 | 0 |
| 10 | 121-140 | 10 | 0 | 1 | 0 |
| 11 | 141-160 | 10 | 8 | 1 | 0 |
| 12 | 161-180 | 10 | 5 | 2 | 1 |
| 13 | 181-200 | 10 | 2 | 1 | 0 |
| 14 | 201-220 | 10 | 12 | 1 | 1 |
| 15 | 221-240 | 10 | 6 | 0 | 0 |

## Duplicates skipped

| Employer | Title | Reason |
|----------|-------|--------|
| Pew Charitable Trusts | Senior Associate Public Health Data Improvement | Hybrid-only DC |
| Syneos Health | Part-Time Survey and Data Insights Analyst | Contract-only |
| Pearl Health | Staff Data Scientist Clinical Performance | Same title already in results from batch 1 re-check |

## Dead / inaccessible career sites (28)

Pharmaceutical Institute, Pharmacom Media, PHMR, Revvity (access denied), Prime Healthcare, PrimeTime Health Plan, ProMedica, Providence.org, Porsesh (DNS), Porter Novelli (DNS), Physical HealthChoices (no portal), Real Chemistry (DNS), Redox (403), Regeneron (403), Rush.edu (DNS), RWJBarnabas (DNS), Sage Bionetworks (redirect), Scicom (connection reset), Sarepta (404), Sentara (DNS), Summa Health (DNS), Sword Health (under construction at time of search), Syneos main site (403 on alternate URL), Temple jobs (DNS), Tenet (DNS), SUNY jobs portal (DNS), Texas Children's jobs (SSL), Pharmaceutical Institute

## Employer log (abbreviated)

All 240 employers in `job_search_queue_E.csv` were attempted via VM browser sessions in batches of 10–40. Status codes: **searchable** (career portal reached), **dead** (DNS/403/404), **partial** (site reached but search incomplete due to CAPTCHA/navigation/time), **no_careers** (no job board).

Employers with roles recorded in `job_search_expansion_E_results.csv`: Peach State Health Plan, Pearl Health, PointClickCare, PPD, Precision for Medicine HEOR, Professional Data Analysts, PSCI, Rady Children's Health, SCAN Health Plan, Scicom MedComms, Science 37, Scientific Group, Save the Children International, SmarterDx, Spring Health, Syneos Health, RTI International, Sunshine Health, Surescripts, Sutter Health, Sword Health, Syapse, Takeda, Talkiatry, Talkspace, Tandem Health AI, Tempus.

Employers searched with zero qualifying remote US full-time roles added: remaining 213 employers (hospital systems, academic onsite postings, international-only roles, sales/clinical/nursing-only listings, or no openings).

## Notes

- High-recall criteria applied: hybrid and remote-unclear roles included when plausibly relevant; contract-only, freelance, sales, and executive-only listings excluded.
- No applied/dead tracker file was present; no prior-application filtering performed.
- VM browser DNS/CAPTCHA issues limited depth on several large health-system and university portals; recommend direct follow-up on Syneos, RTI, Regeneron, and Providence career portals.
