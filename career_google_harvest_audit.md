# Career Google Harvest Audit

## Summary

| Metric | Count |
|--------|-------|
| Google result pages reviewed | 20 |
| Raw organic URLs collected | ~205 |
| Unique domains | 45 |
| Likely official career pages | 45 |
| Excluded job boards | ~105 |
| Excluded individual postings | ~25 |
| Excluded other (blogs, programs, articles) | ~30 |
| Duplicate domains merged | 0 |

## Search Query

```
(careers OR jobs OR employment OR opportunities) (epidemiology OR biostatistics OR "public health" OR HEOR OR "health economics" OR "outcomes research" OR "real world evidence" OR RWE OR "medical writer" OR "clinical research" OR "research scientist" OR "healthcare analytics" OR "health data science" OR "population health" OR bioinformatics OR pharmaceutical OR pharma OR biotech OR CRO OR hospital OR university OR "academic medical center" OR "research institute" OR "digital health" OR "health technology" OR "medical communications" OR consulting OR insurance)
```

## Methodology

- Used **built-in VM browser only** (computerUse) — no Selenium, Playwright, Python, JavaScript automation, or HTML scraping.
- Operated exactly like a human: read visible organic Google results (title, URL, snippet).
- Ignored AI Overview, Google Jobs widget, and sponsored results.
- Did not click into employer websites; stayed on Google result pages.
- Scrolled through each page and clicked **Next** to paginate through pages 1–20.
- Recorded only URLs that appeared to be official employer career pages.
- Deduplicated by employer/domain.

## Category Counts

| Category | Count |
|----------|-------|
| Academic Medical Center | 11 |
| University | 11 |
| Government | 9 |
| CRO | 3 |
| Research Institute | 3 |
| Pharmaceutical | 2 |
| Medical Device | 2 |
| Medical Communications | 1 |
| HEOR | 1 |
| Biotechnology | 1 |
| Consulting | 1 |
| Hospital System | 1 |
| Health Technology | 1 |
| Public Health Organization | 1 |

## Exclusion Breakdown

### Job boards excluded (~105)

LinkedIn (~50), Indeed (~50), Glassdoor, ZipRecruiter (~20), BioSpace, PublicHealthCareers.org (~10), careerplacement.org, careerwebsite.com, and similar aggregator sites. Job boards dominated pages 12–20 especially.

### Individual job postings excluded (~25)

Specific role postings at Amgen, Boston Scientific, Novo Nordisk, Stanford, Beth Israel Lahey, various myworkdayjobs.com listings, SEEK postings, and other single-position URLs.

### Other excluded (~30)

RWE energy company (non-healthcare), Flatiron Health article, YouTube videos, academic publications, ExploreHealthCareers.org (educational), Georgia State career exploration page, Bureau of Labor Statistics occupational handbook, Federal Reserve Bank articles, NCI training pages, Coursera articles, and similar non-career-page content.

## Recommended High-Value Employer Categories

Based on density and relevance to epidemiology, biostatistics, public health, HEOR, and clinical research roles:

1. **Academic Medical Center** (11) — Mayo Clinic, UVA, University of Chicago, Dana-Farber, City of Hope, Beth Israel Lahey
2. **University / Public Health Schools** (11) — Johns Hopkins, Yale, Columbia, UC Berkeley, Tulane, NYU, UAB
3. **Government / Public Health** (10) — WHO, NIEHS, NY State, NYC, Alabama, Tennessee, King County, Colorado DPHE, District 4 GA
4. **CRO** (3) — IQVIA, Velocity Clinical Research, Alcanza Clinical Research
5. **Pharmaceutical / Biotech** (3) — Merck, Thermo Fisher, ImmunityBio
6. **HEOR / Medical Communications** (2) — OPEN Health, Columbia Data Analytics
7. **Medical Device** (2) — Boston Scientific, Becton Dickinson

## Pages Searched

| Page range | New career pages found | Notes |
|------------|------------------------|-------|
| 1–10 | 41 | Diverse mix of employers across all categories |
| 11 | 4 | King County, UAB, District 4 GA, Colorado DPHE |
| 12–20 | 0 | Heavily dominated by job board aggregators; diminishing new employer discovery |
