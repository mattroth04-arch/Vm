# Job Search Queue Split Summary

Source: `employer_universe_master.csv` on `cursor/employer-universe-merge-d967`

## Filtering

- Master rows: 1,445
- Rows excluded: 0
- Rows queued: 1,445

No rows excluded — master universe already deduplicated with valid domains and URLs.

## Queue Files

| File | Master row range | Employers |
|------|------------------|----------:|
| `job_search_queue_A.csv` | 1–240 | 240 |
| `job_search_queue_B.csv` | 241–480 | 240 |
| `job_search_queue_C.csv` | 481–720 | 240 |
| `job_search_queue_D.csv` | 721–960 | 240 |
| `job_search_queue_E.csv` | 961–1200 | 240 |
| `job_search_queue_F.csv` | 1201–1445 | 245 |

**Total queued employers:** 1,445

## Columns preserved

organization, domain, visible_url, primary_category, secondary_categories, confidence, notes

## Ready for agents

Queues A–F are ready for parallel job-search agents. Do not begin job searches until agents are assigned.
