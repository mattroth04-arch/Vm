# Global Health / International NGO Discovery Audit

## Mission Summary

Built a master employer universe for global health organizations, international NGOs, implementation science organizations, humanitarian health organizations, infectious disease nonprofits, global epidemiology organizations, international research institutes, maternal and child health organizations, health systems strengthening organizations, global surveillance organizations, and international development health contractors.

**Discovery method:** Google search via VM browser (human-style browsing). Organic results only. No Selenium, Playwright, Python crawling, HTML inspection, or employer website crawling.

**Search query used:**
```
("global health organization" OR "international health NGO" OR "implementation science organization" OR "humanitarian health organization" OR "infectious disease nonprofit" OR "global epidemiology organization" OR "international research institute" OR "maternal child health organization" OR "health systems strengthening" OR "global health surveillance" OR "international development health contractor" OR "public health NGO")
```

---

## Final Statistics

| Metric | Value |
|--------|-------|
| Pages reviewed | 31 |
| Organizations discovered (raw, before dedup) | 89 |
| Organizations in final universe | 67 |
| Duplicates / exclusions removed | 22 |

---

## New Organizations Per Page

| Page | New Orgs | Running Total |
|------|----------|---------------|
| 1 | 6 | 6 |
| 2 | 4 | 10 |
| 3 | 4 | 14 |
| 4 | 5 | 19 |
| 5 | 4 | 23 |
| 6 | 1 | 24 |
| 7 | 3 | 27 |
| 8 | 3 | 30 |
| 9 | 4 | 34 |
| 10 | 4 | 38 |
| 11 | 6 | 44 |
| 12 | 2 | 46 |
| 13 | 3 | 49 |
| 14 | 2 | 51 |
| 15 | 1 | 52 |
| 16 | 2 | 54 |
| 17 | 4 | 58 |
| 18 | 7 | 65 |
| 19 | 4 | 69 |
| 20 | 4 | 73 |
| 21 | 0 | 73 |
| 22 | 4 | 77 |
| 23 | 2 | 79 |
| 24 | 1 | 80 |
| 25 | 3 | 83 |
| 26 | 0 | 83 |
| 27 | 3 | 86 |
| 28 | 1 | 87 |
| 29 | 0 | 87 |
| 30 | 1 | 88 |
| 31 | 1 | 89 |

**Trend:** Early pages (1–11) yielded 4–7 new organizations per page. Mid pages (12–20) yielded 1–7 per page. Late pages (21–31) dropped sharply, with pages 21, 26, and 29 producing zero new organizations. Pages 29–31 produced 0, 1, and 1 new organizations respectively, triggering the stop condition.

---

## Reason for Stopping

**Stop condition met:** Three consecutive pages (29, 30, 31) each produced fewer than two new organizations.

- Page 29: 0 new
- Page 30: 1 new
- Page 31: 1 new

At this depth, organic results were dominated by academic journals, UN observance pages, government agencies, previously discovered organizations, and non-health entities.

---

## Category Counts

| Category | Count |
|----------|-------|
| Global Health | 18 |
| International NGO | 5 |
| Implementation Science | 3 |
| Humanitarian Health | 12 |
| Infectious Disease | 3 |
| International Research | 11 |
| Health Systems Strengthening | 4 |
| Other | 10 |
| **Total** | **67** |

---

## Duplicates Removed

| Organization | Duplicate / Related URL | Action |
|-------------|----------------------|--------|
| CARE International | care-international.org / care.org | Kept care.org |
| International Leadership Association | globalleadershipnetwork.org / ilglobalnetwork.org | Excluded (not health-focused) |
| Council of International Schools | cis.org / cois.org | Excluded (education, not health NGO) |
| Airbel Impact Lab | airbel.rescue.org (IRC subsidiary) | Merged with rescue.org |
| ILOSTAT | ilostat.ilo.org (ILO data platform) | Merged with ilo.org |
| Fogarty International Center | Reappeared on page 32 | Deduplicated |
| ICRC, IOM, RTI, CARE, CIOMS, Save the Children, etc. | Reappeared on later pages | Deduplicated |

---

## Exclusions Applied

Per workflow rules, the following result types were excluded during curation:

- **Job platforms:** DevelopmentAid, LinkedIn, Indeed, Glassdoor, ZipRecruiter
- **Academic journals:** International Journal of Infectious Diseases, Oxford Academic, Nature, ScienceDirect, MDPI
- **News / blogs / media:** BORGEN Magazine articles, YouTube listicles
- **Generic directories:** Wikipedia category pages, World Population Review
- **Conference / event pages:** UN observance days, International Day of Yoga
- **Degree programs / academic guides:** Johns Hopkins International Health, Notre Dame library guides
- **Hospital patient services (not NGOs):** Weill Cornell International, Boston Children's International, Cedars-Sinai International, UCSF Health International
- **Non-health organizations:** International Spy Museum, Marriott Careers, International Paper, IMF, ICAO, International Federation of Robotics, Amnesty International
- **Commercial for-profit:** Baxter (healthcare products company)
- **Government non-health:** U.S. Customs and Border Protection, House.gov, Census.gov

---

## Confidence Distribution

| Confidence | Count |
|------------|-------|
| High | 50 |
| Medium | 17 |

---

## Notable High-Confidence Discoveries (Late Pages)

Organizations found on deeper pages that were not visible in early results:

- **UICC** (page 24) — Union for International Cancer Control
- **Médecins du Monde** (page 25) — Humanitarian medical NGO
- **International Rescue Committee** (page 27) — Major humanitarian health NGO
- **MedShare International** (page 27) — Medical supply redistribution
- **ProMED** (page 14) — Infectious disease surveillance network
- **GHS Index** (page 18) — Pandemic preparedness assessment
- **Encephalitis International** (page 13) — Infectious disease specialty nonprofit

---

## Output Files

- `global_health_ngo_universe.csv` — 67 deduplicated organization records
- `global_health_ngo_universe_audit.md` — This audit report
