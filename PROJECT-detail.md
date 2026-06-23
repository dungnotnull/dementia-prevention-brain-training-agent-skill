# PROJECT-detail.md — Skill 236: Brain Training Exercises for Dementia/Alzheimer Prevention

## Executive Summary

This skill is a clinically-grounded, safety-first cognitive training planner for older adults seeking evidence-based interventions to prevent or delay dementia and Alzheimer's disease. The skill fuses neuroplasticity science with established clinical trial protocols (FINGER, ACTIVE, MAPT) to generate individualized, progressive 12-week brain training programs that address five key cognitive domains. It is continuously updated via PubMed and Cochrane crawls, runs a mandatory safety screen before any advice, and produces professional-grade training schedules with peer-reviewed citations.

---

## Problem Statement

### Domain Context
Dementia is the 7th leading cause of death globally, with Alzheimer's accounting for 60-70% of cases. The WHO estimates 55 million people live with dementia worldwide (2023), with a new case every 3 seconds. Despite evidence that modifiable lifestyle factors (cognitive activity, physical exercise, diet, sleep, social engagement) can reduce risk by 40% (Lancet Commission 2020 — 12 modifiable risk factors), structured prevention programs remain inaccessible to most older adults.

### The Evidence Gap
Commercial brain-training apps (Lumosity, CogniFit) lack grounding in validated clinical protocols and produce narrow, transfer-limited gains. What clinical research shows works:
- **FINGER Trial (2015, Ngandu et al., Lancet):** Multidomain lifestyle intervention (cognitive training + exercise + diet + vascular risk management) reduced cognitive decline by 25-150% across domains.
- **ACTIVE Study (2014, Rebok et al., JAMA Internal Medicine):** 10 years post-training, targeted cognitive training showed lasting benefits — memory training reduced memory decline, reasoning training reduced reasoning decline.
- **Cognitive Reserve Theory (Stern, 2002):** Lifelong cognitive engagement builds reserve that delays symptom onset.
- **Neuroplasticity via BDNF:** Aerobic exercise increases Brain-Derived Neurotrophic Factor, directly supporting hippocampal neurogenesis and synaptic plasticity.

### Motivation
This skill provides what neither apps nor brief medical consultations can: a comprehensive, personalized, evidence-grounded cognitive maintenance program with safety screening, progress tracking, and lifestyle integration.

---

## Target Users & Use Cases

### Primary Users
- Adults aged 55+ concerned about cognitive decline
- Family caregivers designing activities for older relatives
- Occupational therapists and geriatric care coordinators (as a decision-support tool)
- Retirement community activity directors

### Trigger Examples
| User Says | Skill Does |
|-----------|-----------|
| "I'm 68 and my mother had Alzheimer's. What brain exercises should I do?" | Runs safety screen → profile intake → cognitive assessment → 12-week training plan with family history risk notes |
| "My father scored 26 on MoCA. Design a brain training program for him." | Validates MoCA score → profiles health conditions → assesses domain-specific weaknesses → tailored moderate-intensity program |
| "I keep forgetting names and feel my memory slipping." | Safety screen → episodic memory assessment → method of loci + spaced retrieval training → progress tracking |
| "What's the evidence for N-back training in preventing Alzheimer's?" | Retrieves PubMed/Cochrane evidence → presents evidence hierarchy → recommends protocol if appropriate after screening |
| "Design a weekly brain training schedule for my 72-year-old neighbor who lives alone." | Full harness with social engagement component emphasized; safety flags re: social isolation as risk factor |

---

## Harness Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  MAIN HARNESS: dementia-prevention-brain-training │
└────────────────────┬────────────────────────────────────────────┘
                     │
          ┌──────────▼──────────┐
          │  STEP 1: SAFETY GATE │
          │  sub-safety-screener │
          │  • Contraindications  │
          │  • Current Rx screen  │
          │  • Medical disclaimer │
          │  • Supervision flags  │
          └──────────┬──────────┘
                     │ [PASS — may continue]
          ┌──────────▼──────────┐
          │  STEP 2: PROFILE    │
          │  sub-profile-intake │
          │  • Demographics      │
          │  • Health history    │
          │  • Lifestyle baseline│
          │  • Social support    │
          └──────────┬──────────┘
                     │
          ┌──────────▼──────────────┐
          │  STEP 3: ASSESSMENT     │
          │  sub-cognitive-assessment│
          │  • Memory domain         │
          │  • Attention domain      │
          │  • Executive function    │
          │  • Language domain       │
          │  • Visuospatial domain   │
          │  • MMSE/MoCA proxy       │
          └──────────┬──────────────┘
                     │
          ┌──────────▼────────────┐
          │  STEP 4: TRAINING     │
          │  sub-training-designer│
          │  • 12-week schedule    │
          │  • Domain prioritization│
          │  • Exercise selection  │
          │  • Intensity calibration│
          │  • Dual-task sessions  │
          └──────────┬────────────┘
                     │
          ┌──────────▼──────────────┐
          │  STEP 5: ROADMAP        │
          │  sub-improvement-roadmap│
          │  • Progress metrics      │
          │  • Difficulty escalation │
          │  • Lifestyle synergies   │
          │  • Re-assessment schedule│
          └──────────┬──────────────┘
                     │
          ┌──────────▼────────────────────┐
          │  STEP 6: FINAL DELIVERABLE    │
          │  (main harness synthesizes)   │
          │  • Professional training plan  │
          │  • Weekly schedule table       │
          │  • Evidence citations          │
          │  • Lifestyle recommendations   │
          │  • Medical disclaimer          │
          └───────────────────────────────┘
```

---

## Full Sub-Skill Catalog

### 1. sub-safety-screener
- **Purpose:** Identify contraindications, active diagnoses, and medications that affect cognitive training safety; issue mandatory medical disclaimer; flag cases requiring physician supervision before starting.
- **Inputs:** User-reported diagnoses, medications, recent cognitive test scores, presence of dementia diagnosis
- **Outputs:** Safety clearance status (CLEAR / CONDITIONAL / REFER); specific flags; mandatory medical disclaimer text
- **Tools:** Read (SECOND-KNOWLEDGE-BRAIN.md), WebSearch (drug-cognition interactions if needed)
- **Quality Gate:** Must issue disclaimer on every run. If active dementia diagnosis detected, output is modified to caregiver-focused and physician referral is mandatory. Never skip this step.

### 2. sub-profile-intake
- **Purpose:** Gather a comprehensive user profile to personalize all downstream recommendations.
- **Inputs:** Free-form user description OR structured Q&A
- **Outputs:** Structured profile: age, sex, education level, occupation history, health conditions (cardiovascular, diabetes, hypertension, hearing loss, depression, sleep disorders), current medications, lifestyle (physical activity level, diet quality, sleep quality, alcohol/smoking), social engagement level, self-reported cognitive concerns, any prior cognitive test scores (MMSE/MoCA if available), family history of dementia
- **Tools:** Read (SECOND-KNOWLEDGE-BRAIN.md for risk factor weighting)
- **Quality Gate:** Must capture age, at least 3 health condition data points, cognitive concern description, and physical activity baseline before proceeding.

### 3. sub-cognitive-assessment
- **Purpose:** Evaluate the user's current cognitive status across five domains and determine which areas need the most targeted training.
- **Inputs:** Profile from sub-profile-intake; any available MMSE/MoCA scores; self-reported functional difficulties
- **Outputs:** Domain profile (5-domain radar): Memory (episodic, semantic, working), Attention (sustained, divided, selective), Executive Function (planning, inhibition, cognitive flexibility), Language (word-finding, comprehension), Visuospatial (navigation, object recognition); estimated cognitive tier (Robust / Mild Concern / Significant Concern); domain priority ranking for training
- **Tools:** Read (SECOND-KNOWLEDGE-BRAIN.md for validated screening tools); WebSearch (current MoCA/MMSE normative data if needed)
- **Quality Gate:** Must produce a 5-domain profile with at least one evidence-based reasoning per domain rating. If MoCA < 18 or MMSE < 20, must trigger mandatory physician referral flag.

### 4. sub-training-designer
- **Purpose:** Design a structured, progressive 12-week brain training program tailored to the user's cognitive domain profile, health status, and lifestyle.
- **Inputs:** Domain priority ranking from sub-cognitive-assessment; health/lifestyle profile from sub-profile-intake; safety flags from sub-safety-screener
- **Outputs:** 12-week training calendar with: daily session type (15-30 min), specific exercises per domain with instructions, weekly themes, progressive difficulty structure (Weeks 1-4: Foundation, Weeks 5-8: Development, Weeks 9-12: Mastery/Integration), dual-task sessions, social engagement activities, physical exercise recommendations synchronized with cognitive training (aerobic + cognitive = dual benefit), rest day schedule; evidence citation for each exercise type
- **Tools:** Read (SECOND-KNOWLEDGE-BRAIN.md), WebSearch (latest exercise protocols from FINGER/ACTIVE/BrainHQ literature)
- **Quality Gate:** Must include at least 4 distinct cognitive domains in the training schedule; all exercises must have at least one peer-reviewed citation; must include aerobic exercise integration; must include dual-task training component.

### 5. sub-improvement-roadmap
- **Purpose:** Establish a progress tracking system, difficulty escalation milestones, lifestyle synergy recommendations, and re-assessment schedule.
- **Inputs:** Training plan from sub-training-designer; current cognitive domain profile; user lifestyle baseline
- **Outputs:** Progress tracking metrics (what to track, how often, using which proxy measures); difficulty escalation rules (when and how to increase challenge); lifestyle synergy plan — MIND diet principles, aerobic exercise schedule, sleep hygiene protocol, social engagement calendar, stress management (because cortisol damages hippocampus); re-assessment schedule (recommend formal MoCA/MMSE re-test at 12 weeks and 6 months); warning signs that warrant stopping and consulting a physician; motivational scaffolding for adherence
- **Tools:** Read (SECOND-KNOWLEDGE-BRAIN.md), WebSearch (MIND diet evidence, sleep and amyloid clearance, social engagement studies)
- **Quality Gate:** Must include re-assessment milestone; must list at least 3 lifestyle synergies with evidence; must include warning signs for discontinuation.

---

## Skill File Format Specification

### Frontmatter Schema
```yaml
---
name: dementia-prevention-brain-training
description: Evidence-based 12-week cognitive training program designer for dementia/Alzheimer prevention
---
```

### Required Main Skill Sections
1. Role & Persona
2. Safety Gate Declaration
3. Workflow (numbered, 6 steps)
4. Sub-skills Available (table)
5. Tools
6. Output Format (exact structure)
7. Quality Gates (checklist)

---

## E2E Execution Flow

```
1. User invokes: /dementia-prevention-brain-training [optional: user description]
2. Main harness announces role and SAFETY GATE activation
3. sub-safety-screener runs:
   a. Ask for: existing dementia diagnosis, medications (anticholinergics, sedatives), history of seizures, recent neurological events (stroke < 6 months), severe depression
   b. Check all answers against contraindication list
   c. Issue mandatory medical disclaimer (always)
   d. If REFER condition detected → output modified plan for caregiver + physician referral required
   e. If CLEAR or CONDITIONAL → proceed
4. sub-profile-intake runs:
   a. Collect 15-point profile (age, sex, education, occupation, health conditions, medications, lifestyle, social engagement, family history, cognitive concerns, prior test scores)
   b. Validate completeness
5. sub-cognitive-assessment runs:
   a. Present 5-domain self-assessment questions
   b. Map MMSE/MoCA scores if provided
   c. Produce domain radar + priority ranking
   d. If severe impairment detected → escalate to physician referral
6. sub-training-designer runs:
   a. Select exercises per prioritized domain
   b. Build 12-week calendar (Weeks 1-4 Foundation, 5-8 Development, 9-12 Mastery)
   c. Integrate dual-task sessions
   d. Add physical exercise sync
   e. Cite evidence for each exercise type
7. sub-improvement-roadmap runs:
   a. Define metrics to track
   b. Set escalation rules
   c. Build lifestyle synergy recommendations
   d. Set re-assessment calendar
8. Main harness synthesizes:
   a. Combines all outputs into professional deliverable
   b. Adds mandatory final medical disclaimer
   c. Formats with tables, schedules, citations
   d. Presents final output to user
```

### Error Handling
- **Missing profile data:** Prompt for specific missing fields before proceeding
- **Conflicting information:** Ask clarifying question; flag inconsistency in output
- **WebSearch unavailable:** Fall back to SECOND-KNOWLEDGE-BRAIN.md with explicit "Evidence from cached knowledge base" note
- **Severe impairment flags:** Always route to physician referral; do not generate training program; generate caregiver guidance only

---

## SECOND-KNOWLEDGE-BRAIN Integration

### Sources for Crawl Pipeline
| Source | URL Pattern | Query |
|--------|------------|-------|
| PubMed | pubmed.ncbi.nlm.nih.gov | "dementia prevention cognitive training" OR "neuroplasticity elderly" OR "FINGER trial" |
| Cochrane | cochranelibrary.com | "cognitive training dementia" OR "brain training older adults" |
| Lancet Neurology | thelancet.com/journals/laneur | dementia prevention |
| Alzheimer's Association | alz.org | research updates, AAIC proceedings |
| WHO | who.int | dementia prevention guidelines |
| AAIC | alz.org/aaic | conference proceedings |

### Append Format (per entry)
```markdown
### [Title]
- **Authors:** [names]
- **Year:** [year]
- **Venue:** [journal/conference]
- **DOI/Link:** [url]
- **Key Finding:** [1-2 sentence summary]
- **Relevance Score:** [1-10]
- **Date Added:** [YYYY-MM-DD]
```

---

## Quality Gates (Global)

Before presenting ANY guidance output, the following must all be true:

- [ ] sub-safety-screener has run and issued medical disclaimer
- [ ] No active dementia diagnosis in user profile without physician referral flag
- [ ] No stroke < 6 months without physician referral flag
- [ ] User profile completeness >= 80% (12/15 data points collected)
- [ ] Cognitive domain profile covers all 5 domains with at least one evidence-based note per domain
- [ ] Training plan cites at least one peer-reviewed source per exercise type
- [ ] Medical disclaimer appears in final output
- [ ] Re-assessment schedule is included
- [ ] Warning signs for discontinuation are listed

---

## Test Scenarios

See `tests/test-scenarios.md` for full scenario descriptions. Summary:
1. Healthy 65-year-old woman, strong family history, no cognitive symptoms
2. 72-year-old man with MoCA score 24, mild word-finding difficulty, hypertension
3. 78-year-old woman, active smoker, recent TIA (3 months ago) — safety gate should trigger REFER
4. 68-year-old man, active dementia diagnosis — safety gate should trigger REFER + caregiver mode
5. 70-year-old woman, MoCA 18, significant memory concerns, otherwise healthy
6. Caregiver designing program for 80-year-old parent with no test scores available
7. 60-year-old man, WebSearch unavailable — graceful degradation to cached knowledge

---

## Key Design Decisions

1. Safety first: sub-safety-screener is non-bypassable — the harness halts and redirects if REFER is triggered.
2. 12-week is the validated minimum intervention duration in FINGER and ACTIVE studies.
3. Dual-task training (simultaneous physical + cognitive) is included because it mimics real-life demands and shows superior transfer effects vs. cognitive-only training.
4. MMSE/MoCA are used as proxies only — not diagnostic tools. Any score suggesting cognitive impairment triggers physician referral.
5. All exercise recommendations must cite systematic reviews or RCTs above case studies or expert opinion.
6. MIND diet is included as the only diet shown to specifically reduce Alzheimer's risk (Morris et al., 2015, Alzheimer's & Dementia).
7. Social engagement is treated as a core "pillar" of the program — not an afterthought — because social isolation is one of the 12 modifiable Lancet Commission risk factors.
8. The program is written in accessible language (avoid clinical jargon in user-facing output).
9. Knowledge base is updated weekly to incorporate AAIC conference findings (the primary venue for cutting-edge dementia prevention research).
10. Output is structured as a professional artifact (tabular weekly schedule, domain scores, roadmap table) that the user can share with their physician.
