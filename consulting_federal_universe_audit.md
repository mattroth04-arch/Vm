# Consulting & Federal Contractor Universe — Discovery Audit

**Agent:** Federal Contractor Discovery Agent G  
**Date:** 2026-06-22  
**Method:** Organic Google search via VM browser (human-like navigation; no automation, scraping, or HTML inspection)

## Search Query

```
("healthcare consulting firm" OR "health economics consulting" OR "health policy consulting" OR "policy research organization" OR "federal contractor" OR "government contractor" OR "CMS contractor" OR "CDC contractor" OR "NIH contractor" OR "AHRQ contractor" OR "program evaluation firm" OR "health services research contractor" OR "public sector consulting firm" OR "social science research contractor" OR "data analytics consulting firm")
```

## Summary

| Metric | Value |
|--------|-------|
| Pages reviewed | 14 |
| Organizations discovered | 19 |
| Duplicates removed | 1 |
| Output file | `consulting_federal_universe.csv` |

## New Organizations Per Page

| Page | New orgs | Duplicates skipped | Notes |
|------|----------|-------------------|-------|
| 1 | 6 | 0 | PHF, FTI Consulting, Public Policy Institute, Nava PBC, PHI, BCG |
| 2 | 2 | 0 | RAND Corporation, Council on Education for Public Health |
| 3 | 4 | 0 | Annenberg Public Policy Center, PwC (Strategy&), Open Contracting Partnership; Frontiers journal excluded |
| 4 | 3 | 0 | Korn Ferry, PA Consulting; Google Public Sector excluded (not an org) |
| 5 | 1 | 0 | Governors Public Health Alliance |
| 6 | 1 | 0 | Centre for Public Impact |
| 7 | 1 | 0 | Kaiser Permanente |
| 8 | 0 | 0 | Government agency pages only |
| 9 | 0 | 0 | Government pages, libraries, schools only |
| 10 | 3 | 0 | ARRC/Volcker Alliance, Empire Center, Accenture |
| 11 | 0 | 0 | Schools and OMNIA Partners (excluded) |
| 12 | 0 | 0 | Gallagher (insurance), universities, government agencies |
| 13 | 0 | 1 | Annenberg Public Policy Center (duplicate) |
| 14 | 0 | 0 | Government agencies and universities only |

### Trend

Early pages (1–7) yielded steady new organizations (1–6 per page). Pages 8–9 produced zero new qualifying organizations as results shifted toward government agencies and educational institutions. Page 10 briefly resurfaced relevant organizations. Pages 11–14 produced zero new organizations across four consecutive pages.

## Reason for Stopping

**Stop condition met:** Three consecutive pages each produced fewer than two new organizations.

Pages 11, 12, 13, and 14 each produced **0** new organizations (four consecutive pages below the threshold of 2). The search results at this depth were dominated by educational institutions, government agency pages, and non-employer content rather than consulting firms, research organizations, or federal contractors.

## Exclusions Applied

- AI Overview, sponsored results, Google Jobs, People Also Ask
- LinkedIn, Indeed, Glassdoor, ZipRecruiter
- Individual job postings, blogs, news articles, conference pages
- Generic government procurement pages
- Educational institutions (universities, schools of public health)
- Directories without a specific employer (e.g., OMNIA Partners marketplace)
- Insurance/risk firms not matching target categories (e.g., Gallagher)

## Category Counts

| Category | Count |
|----------|-------|
| Healthcare Consulting | 1 |
| Health Economics Consulting | 0 |
| Policy Research | 8 |
| Federal Contractor | 1 |
| Program Evaluation | 0 |
| Public Sector Consulting | 7 |
| Data Analytics Consulting | 0 |
| Health Services Research | 0 |
| Other | 2 |
| **Total** | **19** |

## Organizations by Category

### Healthcare Consulting (1)
- Kaiser Permanente

### Health Economics Consulting (0)
- None discovered in this search pass

### Policy Research (8)
- Public Policy Institute (Elevance Health)
- Public Health Institute
- RAND Corporation
- Annenberg Public Policy Center
- Governors Public Health Alliance
- Centre for Public Impact
- Accountability and Reform Research Consortium (Volcker Alliance)
- Empire Center for Public Policy

### Federal Contractor (1)
- Nava PBC

### Program Evaluation (0)
- None discovered in this search pass

### Public Sector Consulting (7)
- Public Health Foundation
- FTI Consulting
- Boston Consulting Group
- PwC (Strategy&)
- Korn Ferry
- PA Consulting
- Accenture

### Data Analytics Consulting (0)
- None discovered in this search pass

### Health Services Research (0)
- None discovered in this search pass

### Other (2)
- Council on Education for Public Health
- Open Contracting Partnership

## Confidence Distribution

| Confidence | Count |
|------------|-------|
| High | 15 |
| Medium | 4 |
| Low | 0 |

## Notes

- Most organizations were identified directly from Google organic result titles, URLs, and snippets without clicking through.
- One duplicate (Annenberg Public Policy Center on page 13) was skipped during deduplication by domain.
- Results skewed toward large public-sector consulting firms and policy research think tanks; fewer niche healthcare economics, CMS/NIH/CDC/AHRQ-specific contractors, and program evaluation firms appeared in organic results for this compound query at pages 1–14.
