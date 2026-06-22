# AI / Clinical AI / Biomedical Data Science Discovery Agent — Audit Report

## Mission

Build a master employer universe for healthcare AI, clinical AI, biomedical data science, and related organization categories using organic Google search results only.

## Search Query

```
("healthcare AI company" OR "clinical AI company" OR "biomedical data science company" OR "machine learning healthcare company" OR "AI drug discovery company" OR "clinical NLP company" OR "predictive analytics healthcare" OR "AI imaging company" OR "AI diagnostics company" OR "AI care navigation" OR "AI clinical documentation" OR "AI evidence generation" OR "AI medical research company")
```

## Methodology

- **Browser:** VM Chrome only (human-like Google search; no Selenium, Playwright, Python scraping, HTML inspection, or employer-site crawling)
- **Included:** Organic Google results pointing to company homepages
- **Excluded:** AI Overview, Sponsored results, Google Jobs, People Also Ask, LinkedIn, Indeed, Glassdoor, ZipRecruiter, individual job postings, blogs, news articles, directories, conference pages, generic AI tool lists
- **Deduplication:** Continuous by organization name and domain across all pages
- **Stopping rule:** Three consecutive pages each producing fewer than two new organizations

## Summary

| Metric | Value |
|--------|-------|
| Pages reviewed | 18 |
| Organizations discovered | 38 |
| Duplicates removed | 0 |
| High confidence | 35 |
| Medium confidence | 3 |
| Low confidence | 0 |

## New Organizations Per Page

| Page | New Orgs | Cumulative Total |
|------|----------|------------------|
| 1 | 5 | 5 |
| 2 | 6 | 11 |
| 3 | 1 | 12 |
| 4 | 1 | 13 |
| 5 | 2 | 15 |
| 6 | 0 | 15 |
| 7 | 0 | 15 |
| 8 | 3 | 18 |
| 9 | 2 | 20 |
| 10 | 2 | 22 |
| 11 | 2 | 24 |
| 12 | 4 | 28 |
| 13 | 2 | 30 |
| 14 | 3 | 33 |
| 15 | 3 | 36 |
| 16 | 1 | 37 |
| 17 | 1 | 38 |
| 18 | 0 | 38 |

### Trend Analysis

- **Pages 1–2:** Highest yield (5–6 new organizations per page); dense concentration of company homepages in top results.
- **Pages 3–5:** Declining yield (1–2 per page) as news, blogs, and directories increase.
- **Pages 6–7:** Zero new organizations; results dominated by excluded content types.
- **Pages 8–10:** Partial recovery (2–3 per page) from sporadic valid company homepages.
- **Pages 11–15:** Second productive band (2–4 per page) before final decline.
- **Pages 16–18:** 1, 1, 0 new organizations — stopping criteria met.

## Reason for Stopping

Search stopped after **page 18** because **three consecutive pages (16, 17, 18)** each produced **fewer than two** new organizations:

- Page 16: 1 new (Healx)
- Page 17: 1 new (Karias Health)
- Page 18: 0 new

## Category Counts

| Category | Count |
|----------|-------|
| Healthcare AI | 24 |
| Clinical AI | 6 |
| Biomedical Data Science | 1 |
| AI Drug Discovery | 2 |
| Clinical NLP | 1 |
| Predictive Analytics | 2 |
| Imaging AI | 1 |
| Diagnostics AI | 1 |
| Other | 0 |
| **Total** | **38** |

## Exclusion Log (Representative)

Throughout pages 6–7 and 18, organic results were dominated by:

- News and press coverage (BusinessWire, Pulse2, Transform Capital, Y Combinator listings)
- Academic publications and research papers
- Government and regulatory pages
- Conference and event listings
- Job boards and career aggregators
- Generic AI tool directories and listicles

Organizations referenced in news articles were included only when the company homepage could be identified and verified from the SERP snippet or result context.

## Output Files

- `ai_clinical_datascience_universe.csv` — 38 deduplicated organization records
- `ai_clinical_datascience_universe_audit.md` — this audit report

## Confidence Notes

- **High (35):** Direct company homepage in organic results
- **Medium (3):** Prognos Health (press release SERP reference), Ufonia (limited SERP context), Inbound Health (limited SERP context)
