# Employer Universe Merge Summary

Generated: 2026-06-22

## Branches and PRs Included

- `cursor/academic-employer-discovery-0c53`
- `cursor/ai-clinical-datascience-universe-b799`
- `cursor/behavioral-mental-health-discovery-b6f4`
- `cursor/clinical-informatics-healthit-universe-78ec`
- `cursor/consulting-federal-universe-0daa`
- `cursor/cro-heor-rwe-discovery-307f`
- `cursor/digital-health-universe-discovery-c955`
- `cursor/environmental-occupational-health-discovery-886b`
- `cursor/global-health-ngo-discovery-e8a1`
- `cursor/google-career-harvest-faa3`
- `cursor/hospital-discovery-agent-b-d6aa`
- `cursor/injury-safety-justice-universe-a058`
- `cursor/med-device-diagnostics-universe-e384`
- `cursor/medical-communications-discovery-87dc`
- `cursor/nutrition-consumer-health-universe-880a`
- `cursor/org-universe-harvest-faa3`
- `cursor/payer-vbc-discovery-ed6b`
- `cursor/pharma-biotech-universe-bfec`
- `cursor/rwd-registry-universe-b89c`
- `cursor/survey-policy-research-universe-e49c`

## Branches Inspected but Excluded from Merge

Browser agent branches contain individual job postings (excluded per merge policy):
- `cursor/browser-agent-d-employers-651-835-5de7` (job posting results, not employer universe)
- `cursor/browser-agentA-51-250-07f2` (job posting results, not employer universe)
- `cursor/browser-recovery-agent-b-b261` (job posting results, not employer universe)
- `cursor/browser-recovery-agentc-c17f` (job posting results, not employer universe)
- `cursor/phase3c-browser-batch03a-6eee` (job posting results, not employer universe)

## Main-Branch Files Inspected

- `extracted/Jobs/employer_database/employer_database_master.csv` (1523 raw records)
- `extracted/Jobs/runs/phase3c_browser_queue_20260620.json` (835 raw records)

Additional main context: `phase3c_sync_minimum.zip` on main (no standalone CSVs committed on main).

## Merge Statistics

| Metric | Count |
|--------|------:|
| Total raw rows ingested | 3,337 |
| Rows excluded (filters) | 324 |
| Duplicates merged | 1,568 |
| **Total unique employers** | **1,445** |

### Exclusion Breakdown

- placeholder domain: 302
- job board: 22

### Category Counts

| Primary Category | Employers |
|------------------|----------:|
| academic | 110 |
| Academic Medical Centers | 106 |
| Digital Health | 97 |
| hospital_system | 75 |
| Federal Contractors | 67 |
| global_health_ngo | 66 |
| Hospital Systems | 64 |
| Government / Public Health | 61 |
| clinical_informatics_healthit | 58 |
| medical_communications | 53 |
| cro_heor_rwe | 50 |
| payer_vbc | 50 |
| med_device_diagnostics | 47 |
| Biotech Companies | 46 |
| org_harvest | 44 |
| pharma_biotech | 42 |
| environmental_occupational_health | 42 |
| survey_policy_research | 40 |
| Medical Communications | 40 |
| ai_clinical_datascience | 38 |
| HEOR / RWE / Consulting | 38 |
| digital_health | 37 |
| rwd_registry | 33 |
| Pharmaceutical Companies | 29 |
| google_harvest | 26 |
| consulting_federal | 19 |
| behavioral_mental_health | 19 |
| injury_safety_justice | 17 |
| Research Organizations | 12 |
| Schools of Public Health | 7 |
| Federal Healthcare Contractors | 4 |
| HEOR Consulting | 4 |
| Universities | 2 |
| nutrition_consumer_health | 1 |
| browser_queue | 1 |

### Confidence Distribution

| Confidence | Employers |
|------------|----------:|
| high | 758 |
| medium | 686 |
| low | 1 |

## High-Confidence Employers (758)

Employers with `confidence=high` across all merged sources.

- **10x Genomics** (10xgenomics.com) — pharma_biotech
- **1st Providers Choice** (1stproviderschoice.com) — clinical_informatics_healthit
- **4Medica** (4medica.com) — clinical_informatics_healthit
- **Abbott Core Laboratory** (abbott.com) — med_device_diagnostics
- **AbbVie** (abbvie.com) — pharma_biotech
- **Abridge** (abridge.com) — ai_clinical_datascience
- **AcademyHealth** (academyhealth.org) — org_harvest
- **Accenture** (accenture.com) — consulting_federal
- **Accountability and Reform Research Consortium (Volcker Alliance)** (volckeralliance.org) — consulting_federal
- **Accuhealth** (accuhealth.tech) — digital_health
- **AdventHealth Translational Research Institute** (adventhealth.com) — academic
- **Adventist Health** (adventisthealth.org) — org_harvest
- **Aetna** (aetna.com) — payer_vbc
- **Africa Policy Research Institute** (afripoli.org) — survey_policy_research
- **Agency for Healthcare Research and Quality** (ahrq.gov) — org_harvest
- **Agilent Technologies** (agilent.com) — med_device_diagnostics
- **Agilify Health** (agilifyhealth.com) — clinical_informatics_healthit
- **AI Care** (care-iq.com) — ai_clinical_datascience
- **AI Care Standard** (aicarestandard.com) — ai_clinical_datascience
- **AiCare** (aicare.co) — ai_clinical_datascience
- **Aidoc** (aidoc.com) — ai_clinical_datascience
- **Aim** (weaim.io) — ai_clinical_datascience
- **Alabama Department of Public Health** (alabamapublichealth.gov) — google_harvest
- **Alcanza Clinical Research** (alcanzaclinical.personio.com) — google_harvest
- **Alexion** (alexion.com) — med_device_diagnostics
- **Alignment Health Plan** (alignmenthealthplan.com) — payer_vbc
- **Alira Health** (alirahealth.com) — cro_heor_rwe
- **Alliance Health** (alliancehealthplan.org) — payer_vbc
- **Alliance Medical** (alliancemedical.com) — med_device_diagnostics
- **Allucent** (allucent.com) — cro_heor_rwe
- ... and 728 more (see `employer_universe_master.csv`)

## Recommended Next Step: Career-Page Verification

1. **Prioritize high-confidence employers lacking verified career pages** — cross-check `visible_url` against each organization's official careers portal.
2. **Run browser verification on `browser_queue` employers** (514 recoverable of 835 queued) using homepage URLs rather than stale Workday/Greenhouse job links.
3. **Resolve multi-domain duplicates** flagged in `notes` (parent/subsidiary or acquisition relationships).
4. **Backfill sparse categories** — `nutrition_consumer_health` contributed only 1 employer; consider a follow-up discovery pass.
5. **Exclude job-posting URLs** during verification — update `visible_url` to official org/careers homepages where currently pointing at ATS job detail pages.
