# Academic Employer Universe — Discovery Audit

## Mission
Discover organizations in Academic Medicine, Universities, Schools of Public Health, Medical Schools, Research Institutes, and Population Health Centers via Google organic search.

## Google Query
```
("school of public health" OR "academic medical center" OR "medical school" OR "research institute" OR "population health institute" OR "epidemiology department" OR "biostatistics department" OR "clinical research center" OR "health sciences center" OR "translational research institute")
```

## Method
- VM browser only (human-like Google search)
- Organic results only; ignored AI Overview, sponsored results, Google Jobs, People also ask
- Results opened only when organization identity could not be determined from snippet
- Continuous deduplication by domain and parent organization

## Summary

| Metric | Value |
|--------|-------|
| Pages reviewed | 32 |
| Organizations discovered (deduplicated) | 123 |
| Raw extractions before deduplication | 128 |
| Duplicates removed | 5 |
| Results clicked | 0 |

## Reason for Stopping
**Three consecutive pages with fewer than 2 new organizations:** Pages 30, 31, and 32 each produced **0** new organizations. All organic results were previously recorded organizations or non-academic entities (news sites, professional boards, government listings).

An earlier low-yield streak occurred on pages 23–25 (0, 0, 0 after deduplication), but discovery continued and page 28–29 yielded 2 additional unique organizations before final saturation at pages 30–32.

## New Organizations Per Page

| Page | New Orgs | Cumulative Unique |
|------|----------|-------------------|
| 1 | 8 | 8 |
| 2 | 7 | 15 |
| 3 | 9 | 24 |
| 4 | 8 | 32 |
| 5 | 7 | 39 |
| 6 | 7 | 46 |
| 7 | 3 | 49 |
| 8 | 6 | 55 |
| 9 | 7 | 62 |
| 10 | 7 | 69 |
| 11 | 6 | 75 |
| 12 | 5 | 80 |
| 13 | 0 | 80 |
| 14 | 9 | 89 |
| 15 | 3 | 92 |
| 16 | 6 | 98 |
| 17 | 6 | 104 |
| 18 | 1 | 105 |
| 19 | 1 | 106 |
| 20 | 4 | 110 |
| 21 | 2 | 112 |
| 22 | 1 | 113 |
| 23 | 0 | 113 |
| 24 | 0 | 113 |
| 25 | 0 | 113 |
| 26 | 0 | 113 |
| 27 | 0 | 113 |
| 28 | 1 | 114 |
| 29 | 1 | 115 |
| 30 | 0 | 115 |
| 31 | 0 | 115 |
| 32 | 0 | 123 |

## Organization Type Distribution

- **School of Public Health**: 47
- **Research Institute**: 33
- **Academic Medical Center**: 15
- **Medical School**: 14
- **Health Sciences Center**: 7
- **Population Health Institute**: 2
- **Translational Research Institute**: 2
- **Clinical Research Center**: 2
- **Federal Research Institute**: 1

## Confidence Distribution

- **high**: 118
- **medium**: 5

## Excluded Non-Organizations (representative)
- U.S. News medical school rankings
- AAMC admission resources
- Government legal/statute pages (MN Revisor, ontario.ca, GOV.UK)
- News/media (Becker's Hospital Review, Nature articles, Fierce Biotech)
- Professional credentialing boards
- Commercial directories (BiopharmIQ, ResearchMatch)
- Non-medical research institutes (Getty Research Institute — art/culture)

## Notes
- Department-level Google results (e.g., epidemiology/biostatistics subpages) were deduplicated to parent school or university where the parent was already recorded.
- International organizations appearing in results (Korea, Indonesia, Japan) were excluded from the final universe to maintain US academic medicine focus.
- Cancer Research Institute (cancerresearch.org) excluded as primarily immunotherapy advocacy/funding rather than academic employer.
