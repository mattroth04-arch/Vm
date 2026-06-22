# Behavioral / Mental Health Discovery Agent — Audit Report

## Mission

Build a master employer universe for behavioral health, mental health, digital mental health, substance use treatment, addiction research, suicide prevention, veterans health, PTSD research, military health research, trauma-informed care, behavioral health analytics, and employee mental health benefit organizations.

## Method

- **Search engine:** Google (built-in VM browser only)
- **Query:**

```
("behavioral health company" OR "mental health company" OR "digital mental health platform" OR "substance use treatment organization" OR "addiction research organization" OR "suicide prevention organization" OR "veterans health organization" OR "PTSD research organization" OR "military health research" OR "trauma informed care organization" OR "behavioral health analytics" OR "employee mental health benefit")
```

- **Results read:** Organic Google results only
- **Ignored:** AI Overview, Sponsored results, Google Jobs, People Also Ask
- **Excluded categories:** Job boards, individual job postings, blogs (third-party), news articles, generic directories, conference pages, degree programs, `.gov` sites, academic papers, YouTube videos
- **Included:** Company or organization homepages (including org domains where Google surfaced a subpath such as `/blog/`)

## Pagination Summary

| Page | New Organizations | Cumulative Total |
|------|-------------------|------------------|
| 1 | 4 | 4 |
| 2 | 4 | 8 |
| 3 | 2 | 10 |
| 4 | 5 | 15 |
| 5 | 1 | 16 |
| 6 | 0 | 16 |
| 7 | 1 | 17 |
| 8 | 0 | 17 |
| 9 | 0 | 17 |
| 10 | 0 | 17 |
| 11 | 1 | 18 |
| 12 | 1 | 19 |
| 13 | 0 | 19 |

### Stop Condition

**Met on pages 11, 12, and 13** — three consecutive pages each produced fewer than two new organizations (1, 1, and 0 respectively).

An earlier stretch (pages 8–10) also yielded zero new organizations, but pagination continued because the stop rule requires three consecutive sub-threshold pages and was reset when page 11 surfaced GOBHI.

## Organizations Discovered

**Total unique organizations:** 19

| # | Organization | Domain | First Seen (Page) |
|---|-------------|--------|-------------------|
| 1 | King's Centre for Military Health Research | kcmhr.org | 1 |
| 2 | Hazelden Betty Ford Foundation | hazeldenbettyford.org | 1 |
| 3 | National Network for Youth | nn4youth.org | 1 |
| 4 | Reno Behavioral Healthcare Hospital | renobehavioral.com | 1 |
| 5 | National Veterans Foundation | nvf.org | 2 |
| 6 | Trauma Informed Oregon | traumainformedoregon.org | 2 |
| 7 | Inspira Health | inspirahealthnetwork.org | 2 |
| 8 | Peace Over Violence | peaceoverviolence.org | 2 |
| 9 | Traumatic Stress Institute | traumaticstressinstitute.org | 3 |
| 10 | Alberta Health Services | albertahealthservices.ca | 3 |
| 11 | Trauma Informed Care Project | traumainformedcareproject.org | 4 |
| 12 | CAI Global | caiglobal.org | 4 |
| 13 | University Health System | universityhealth.com | 4 |
| 14 | Newport Healthcare | newporthealthcare.com | 4 |
| 15 | VisionQuest National | vq.com | 4 |
| 16 | Children and Family Futures | cffutures.org | 5 |
| 17 | Pinnacle Treatment Centers | pinnacletreatment.com | 7 |
| 18 | Greater Oregon Behavioral Health Inc. (GOBHI) | gobhi.org | 11 |
| 19 | Bridge to Treatment | bridgetotreatment.org | 12 |

## Exclusion Audit (Representative Samples)

### Government Sites (.gov) — Excluded

- SAMHSA (library.samhsa.gov)
- MO DMH (dmh.mo.gov)
- DHCS (dhcs.ca.gov)
- CDC (stacks.cdc.gov)
- PTSD.gov
- State and local health departments (IN.gov, Maine.gov, CT GOV, Kentucky Cabinet, Ohio Department, City of San Antonio, franklincountypa.gov)
- U.S. Government Accountability Office
- HUD Exchange (hudexchange.info)

### Academic / Educational — Excluded

- Harvard, Georgetown University, University at Buffalo, Case Western Reserve
- State University of New York at Fredonia (fredonia.edu)
- UNC School of Medicine (med.unc.edu)
- PennWest Global Online (degree program)
- Sage Journals, EBSCO, Springer Nature Link
- MedEdPORTAL (mededportal.org)
- AAP National Center (aap.org) — professional association resource page

### News / Blogs / Media — Excluded

- ABC7 New York, Penn State Health News
- NeuroFlow blog, Medium articles, The Conversation
- TED Talks (ted.com)

### Directories / Lists / Reports — Excluded

- Shortlister "Best 29 Mental Health Companies" list
- AVIA Health report

### Conference / Event Pages — Excluded

- American Lung Association "Tobacco in Behavioral Health: Company List" event

### Videos — Excluded

- YouTube and Vimeo trauma-informed care videos

### Job-Related — Excluded

- Google Jobs panels
- Individual job postings and career pages surfaced in results

## Query Yield Observations

1. **Low commercial yield:** The combined OR query with quoted phrases skewed heavily toward trauma-informed care educational and governmental content rather than commercial digital mental health platforms (e.g., Lyra Health, Headspace, Talkspace, Spring Health did not appear in organic results across 13 pages).

2. **Dominant result types:** Government resources, academic papers, university training programs, professional association guidance, and informational articles about trauma-informed care concepts.

3. **Valid organization types found:** Treatment facilities, research organizations, veterans nonprofits, regional behavioral health providers, youth services nonprofits, and health systems with behavioral health lines.

4. **Geographic spread:** Primarily U.S.-based with some Canadian (Alberta Health Services) and U.K. (King's Centre for Military Health Research) organizations.

## Deduplication

Deduplication was performed continuously by normalized domain. No duplicate domains appear in the final universe file.

## Output Files

- `behavioral_mental_health_universe.csv` — 19 organizations with full metadata fields
- `behavioral_mental_health_universe_audit.md` — this audit report
