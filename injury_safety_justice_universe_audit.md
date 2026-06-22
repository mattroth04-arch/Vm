# Injury / Safety / Justice Employer Universe — Discovery Audit

## Mission
Build a master employer universe for injury prevention, violence prevention, criminal justice, public safety, law enforcement policy, firearm injury prevention, traffic safety, trauma, safety outcomes, justice policy, correctional health, and emergency medicine research organizations.

## Method
- **Search engine:** Google (built-in VM browser only)
- **Query:**
  ```
  ("injury prevention organization" OR "violence prevention research" OR "criminal justice research organization" OR "public safety research" OR "law enforcement policy research" OR "firearm injury prevention" OR "traffic safety research" OR "trauma research center" OR "safety outcomes research" OR "justice policy institute" OR "correctional health research" OR "emergency medicine research center")
  ```
- **Ignored:** AI Overview, sponsored results, Google Jobs, People Also Ask
- **Source:** Organic Google results only
- **Excluded types:** Job boards, individual postings, blogs, news articles, directories, conference pages, degree programs, journal articles, government initiative pages, program pages within larger institutions (where clearly subordinate)

## Stopping Criterion
Stop when **three consecutive pages** each produce **fewer than two** new organizations.

## Pagination Summary

| Page | New Orgs | Cumulative Unique | Streak (<2 new)? |
|------|----------|-------------------|------------------|
| 1 | 3 | 3 | — |
| 2 | 1 | 4 | 1 |
| 3 | 2 | 6 | streak broken |
| 4 | 1 | 7 | 1 |
| 5 | 2 | 9 | streak broken |
| 6 | 4 | 13 | streak broken |
| 7 | 1 | 14 | 1 |
| 8 | 3 | 17 | streak broken |
| 9 | 1 | 18 | 1 |
| 10 | 2 | 20 | streak broken (2 is not <2) |
| 11 | 1 | 21 | 1 |
| 12 | 2 | 23 | streak broken (2 is not <2) |
| 13 | 0 | 23 | 1 (search exhausted) |

**Result:** Stopping criterion **not met** — no three consecutive pages with fewer than two new organizations. Search **exhausted at page 13** (Google returned zero organic results; pages 11–12 showed repeated entries).

## Page-by-Page Log

### Page 1 — 3 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| Institute for Firearm Injury Prevention (U Michigan) | firearminjury.umich.edu | University institute homepage |
| Justice Policy Institute | macfound.org grantee page | Policy research org; direct homepage justicepolicy.org used in final CSV |
| Center for Violence Prevention Research | scienceofviolence.org | Independent research center |

**Excluded:** URochester program page; Traffic Safety Research journal; ACS advocacy page; NIH OBSSR initiative; CU Anschutz program page; NEJM article collection; Google Scholar section

### Page 2 — 1 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| VCU Health IVPRL | vcuhealth.org | Academic injury/violence prevention lab |

**Excluded:** Yale program page; ACEP article; VAWnet publisher page; Handshake job board; Congress.gov bill; SAVIR job posting; UC Davis program page; Michigan .gov initiative; JPI LinkedIn (duplicate)

### Page 3 — 2 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| Gun Violence Prevention Research Roundtable | researchgunviolence.org | National research coalition |
| Center for Firearm Injury Prevention (UW) | cfip.uw.edu | UW Medicine research center |

**Excluded:** Boston Children's news; Springer article; CT .gov OFIP; JPI Instagram; NCGVR conference; education program page; ZoomInfo directory; Michigan .gov page

### Page 4 — 1 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| CIRP (CHOP) | injury.research.chop.edu | Pediatric injury/violence research center |

**Excluded:** JAMA article; Baker Institute program; NIH PubMed; National Academy report; Pediatric Trauma Society clinical society; Begun Center (broader violence, added page 9); Glassdoor; U Michigan duplicate

### Page 5 — 2 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| OHSU Gun Violence Prevention Research Center | ohsu-psu-sph.org | University research center |
| Center for Public Safety Research (Clemson) | clemson.edu | Public safety / criminal justice research |

**Excluded:** AMA Ed Hub; AAFP; AAP article; BayShoreEM blog; Grants.gov; MacArthur/JPI duplicate; CDC; Facebook JPI

### Page 6 — 4 new (2 retained after curation)
**Included in crawl**
| Organization | URL | Retained in CSV? |
|---|---|---|
| Health Alliance for Violence Intervention | thehavi.org | Yes |
| WSU Adolescent Health Promotion Lab | hd.wsu.edu | No — university program/lab page |
| Orthopaedic Trauma Association | ota.org | No — professional association grant page, not primary research org |
| CU Anschutz Firearm Injury Prevention Initiative | cuanschutz.edu | No — program within medical school |

**Excluded:** WAPediatrics webinar; Berkeley News traffic article; The Hill news; Instagram JPI; U Michigan duplicate; Milbank article

### Page 7 — 1 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| Johns Hopkins Center for Gun Policy and Research | jhu.edu | Academic gun policy research center |

**Excluded:** NIH article; NCGVR conference; National Academies publication; Agree to Agree directory; Emergency Physicians statement; Columbia news; Ad Council campaign; JPI PDF duplicate; MiCME course module

### Page 8 — 3 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| Everytown Research & Policy | everytownresearch.org | Gun violence policy research |
| Sandy Hook Promise | sandyhookpromise.org | Violence prevention with research arm |
| National Offices of Violence Prevention Network | ovpnetwork.org | State firearm injury prevention offices network |

**Excluded:** MiCME course; AMA news; OHSU duplicate; AHCJ article; ClinicalTrials.gov; ACP journal; Memorial Hermann health system

### Page 9 — 1 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| Begun Center for Violence Prevention | case.edu/socialwork/begun | CWRU violence prevention research center |

**Excluded:** Governors State course catalog; The Trace news; AANS press release; Secret Service .gov; AAFP advocacy; SSRN paper; Sandy Hook duplicate; USA Football partnership news

### Page 10 — 2 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| Everytown for Gun Safety | everytown.org | Parent advocacy org (distinct from Research & Policy) |
| Public Safety Research Center (UC) | ucdigitalfutures.com/public-safety-lab | Law enforcement / public safety research |

**Excluded:** Sandy Hook duplicate; GW Today news; GovInfo legislation; Federal Register; UNH conference; ACP letter; PR Newswire; OHSU Foundation news

### Page 11 — 1 new
**Included**
| Organization | URL | Notes |
|---|---|---|
| NAPSPS | napsps.org | Public safety professional association |

**Excluded:** Public Safety Network vendor; advocacy coalitions; Police1 article; NJPSAC accreditation; Instagram PSFN; IBM think tank; Coalition for Public Safety; Cause IQ directory

### Page 12 — 2 new (0 retained after curation)
**Crawled**
| Organization | URL | Retained in CSV? |
|---|---|---|
| American Coalition of Public Safety | acops.org | No — law enforcement coalition, not research org |
| United Coalition of Public Safety | ucops.org | No — legislative advocacy coalition |

**Excluded:** OJP .gov (×2); PSF Network Facebook duplicate

### Page 13 — 0 new
Google returned **no organic results**. Pagination exhausted. Pages 11–12 contained repeated entries.

## Deduplication Rules Applied
- Same organization on multiple pages counted once (e.g., Institute for Firearm Injury Prevention, Justice Policy Institute, Sandy Hook Promise)
- Everytown for Gun Safety and Everytown Research & Policy kept as related but distinct entities
- Program pages within universities excluded when not standalone research centers (CU Anschutz, WSU lab, UC Davis VPRP, Yale center)
- Professional associations and advocacy coalitions excluded unless primary mission is research in target domains (OTA, ACOPS, UCOPS excluded; NAPSPS retained with low confidence as borderline public-safety employer)

## Final Universe
- **Raw discoveries across 13 pages:** 23 unique candidates before curation
- **Final curated employers:** 17 organizations in `injury_safety_justice_universe.csv`

## Coverage Gaps
The single broad OR-query skewed heavily toward **firearm injury prevention** and **gun violence** results. Limited organic discovery for:
- Traffic safety research organizations
- Trauma research centers (beyond pediatric CIRP)
- Correctional health research organizations
- Emergency medicine research centers (as standalone entities)
- Dedicated law enforcement policy research centers (beyond UC PSRC and Johns Hopkins)

Additional targeted queries would be needed to expand those specialty segments.

## Files Produced
- `injury_safety_justice_universe.csv` — curated employer universe
- `injury_safety_justice_universe_audit.md` — this audit trail
