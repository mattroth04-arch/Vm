# Payer / VBC Universe Discovery Audit

## Mission Summary

Built a master employer universe for health insurance, managed care, Medicare Advantage, Medicaid managed care, value-based care, population health, risk adjustment, quality measurement, care management, payer analytics, and health plan technology organizations using organic Google search results only.

**Google query used:**

```
("health insurance company" OR "managed care organization" OR "Medicare Advantage plan" OR "Medicaid managed care" OR "value based care company" OR "population health management" OR "risk adjustment company" OR "quality measurement organization" OR "care management company" OR "payer analytics" OR "health plan technology" OR "ACO company" OR "accountable care organization")
```

**Method:** VM browser Google search; organic results only. Excluded AI Overview, sponsored results, Google Jobs, People Also Ask, job boards, blogs, news articles, conference pages, and generic comparison sites.

---

## Final Report

| Metric | Value |
|--------|-------|
| Pages reviewed | 17 |
| Organizations discovered | 52 |
| Duplicates removed | 14 |
| Reason for stopping | Three consecutive pages (15, 16, 17) each produced fewer than 2 new organizations |

---

## New Organizations Per Page

| Page | New orgs | Cumulative total |
|------|----------|------------------|
| 1 | 6 | 6 |
| 2 | 4 | 10 |
| 3 | 4 | 14 |
| 4 | 5 | 19 |
| 5 | 4 | 23 |
| 6 | 2 | 25 |
| 7 | 3 | 28 |
| 8 | 5 | 33 |
| 9 | 2 | 35 |
| 10 | 4 | 39 |
| 11 | 2 | 41 |
| 12 | 6 | 47 |
| 13 | 2 | 49 |
| 14 | 2 | 51 |
| 15 | 1 | 52 |
| 16 | 0 | 52 |
| 17 | 0 | 52 |

### Trend

- Pages 1–10: steady yield (2–6 new orgs per page); high discovery phase.
- Pages 11–14: moderate yield (2–6 new orgs per page).
- Pages 15–17: diminishing returns (1, 0, 0 new orgs) — stopping condition met.

---

## Duplicates Removed

14 duplicate or re-listed entries were excluded during deduplication:

| Duplicate / excluded repeat | Reason |
|-----------------------------|--------|
| The Health Plan (page 2) | Already captured on page 1 |
| UnitedHealthcare (pages 2, 4) | Already captured on page 1 |
| Humana (page 5) | Already captured on page 3 |
| Aetna (page 6) | Already captured on page 4 |
| Geisinger Health (page 6) | Already captured on page 5 |
| Medicaid.gov (multiple pages) | Government informational site, not an employer |
| Medicare.gov (multiple pages) | Government informational site, not an employer |
| KFF / NCSL / NIH articles | Educational articles, excluded |
| Indeed / LinkedIn listings | Job boards, excluded |
| American Hospital Association | Hospital trade association, not a health plan |
| Health Plan of San Mateo (page 12) | Duplicate domain listing of existing regional plan context |

---

## Category Counts

| Category | Count |
|----------|-------|
| Health Insurance | 23 |
| Managed Care | 1 |
| Medicare Advantage | 10 |
| Medicaid Managed Care | 11 |
| Value-Based Care | 0 |
| Population Health | 2 |
| Risk Adjustment | 0 |
| Quality Measurement | 0 |
| Care Management | 1 |
| Payer Analytics | 1 |
| Other | 3 |

**Other** includes: Washington Healthplanfinder (state exchange), Health Plan One (insurance broker), MagnaCare (third-party administrator).

---

## Exclusions Applied

- AI Overview, sponsored results, Google Jobs, People Also Ask
- LinkedIn, Indeed, Glassdoor, ZipRecruiter
- Individual job postings
- Blogs and educational articles (KFF, NCSL, NIH, ScienceDirect, MedTrainer, Georgetown University)
- News articles and conference pages
- Generic insurance comparison pages
- Government informational portals without distinct employer identity (Medicaid.gov, Medicare.gov, HHS.gov)

---

## Confidence Distribution

| Confidence | Count |
|------------|-------|
| High | 48 |
| Medium | 4 |

Medium-confidence entries: Jai Medical Systems, Trusted Health Plan Inc, NALC Health Benefit Plan, Health Plan One (broker).

---

## Output

- **CSV:** `payer_vbc_universe.csv` — 52 organizations with organization, visible URL, domain, type, specialty, confidence, and notes.
- **Audit:** `payer_vbc_universe_audit.md` — this file.
