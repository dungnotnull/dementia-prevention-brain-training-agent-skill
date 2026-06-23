# CLAUDE.md — Skill 236: Brain Training Exercises for Dementia/Alzheimer Prevention

## Skill Identity
- **Skill Name:** dementia-prevention-brain-training
- **Tagline:** Evidence-based neuroplasticity training to prevent cognitive decline in older adults
- **Current Phase:** Phase 6 — Integration & Cross-Skill Wiring (Complete)
- **Source Idea:** #236 (ideas.md)
- **Cluster:** health-wellness
- **Safety Classification:** SAFETY-GATED — sub-safety-screener MUST run before any guidance is issued

## Cross-Skill Integration
This skill shares components with other health-wellness cluster skills:
- **MIND Diet Module:** Clinical nutrition skills can reuse the 15-component MIND diet protocol
- **Sleep Hygiene Protocol:** Sleep wellness skills can integrate the 7-point sleep hygiene checklist
- **Social Engagement Calendar:** Loneliness prevention and mental health skills can share social activity frameworks
- **Aerobic Exercise for Brain Health:** Fitness skills can integrate BDNF-based exercise prescriptions
- **Cognitive Screening Framework:** Cognitive assessment skills can reuse the 5-domain assessment structure

See `docs/CROSS-SKILL-INTEGRATION.md` for detailed integration specifications and shared data structures.

## Problem This Skill Solves

Dementia and Alzheimer's disease affect over 55 million people worldwide, with incidence doubling every 20 years. Despite this, the vast majority of older adults lack access to structured, evidence-based cognitive training programs tailored to their individual cognitive profile, health conditions, and lifestyle. Generic brain games (Lumosity, etc.) lack personalization and do not follow validated clinical protocols such as the FINGER trial or the ACTIVE study framework. This skill bridges that gap: it screens for safety contraindications, assesses the user's current cognitive domain strengths and weaknesses, then designs a personalized, progressive 12-week brain training program grounded in neuroscience research on neuroplasticity (Hebb's Rule, BDNF pathways, synaptic pruning), continuously updated via PubMed and Cochrane crawls.

## Harness Flow Summary

```
Step 1: SAFETY GATE → sub-safety-screener
         Screen for contraindications, active diagnoses, medications; issue medical disclaimer

Step 2: PROFILE INTAKE → sub-profile-intake
         Collect age, education, health history, cognitive concerns, lifestyle, social support

Step 3: COGNITIVE ASSESSMENT → sub-cognitive-assessment
         Evaluate 5 cognitive domains (memory, attention, executive function, language, visuospatial)
         Apply MMSE/MoCA proxies; flag domains needing most intervention

Step 4: TRAINING DESIGN → sub-training-designer
         Select evidence-based exercises per domain; build 12-week progressive schedule
         Apply FINGER/ACTIVE protocols; dual-task training; N-back; method of loci; etc.

Step 5: IMPROVEMENT ROADMAP → sub-improvement-roadmap
         Progress tracking metrics; difficulty escalation schedule; lifestyle synergies
         (MIND diet, aerobic exercise, sleep hygiene, social engagement)

Step 6: SYNTHESIZE FINAL DELIVERABLE → main harness
         Produce professional weekly training schedule with citations, lifestyle plan, re-assessment timeline
```

## Sub-Skills List

| File | One-line Description |
|------|---------------------|
| `skills/sub-safety-screener.md` | Screen for medical contraindications and issue mandatory safety disclaimers before any guidance |
| `skills/sub-profile-intake.md` | Gather comprehensive user profile: age, health history, cognitive concerns, lifestyle baseline |
| `skills/sub-cognitive-assessment.md` | Evaluate 5 cognitive domains using MMSE/MoCA proxies and self-reported performance indicators |
| `skills/sub-training-designer.md` | Design a personalized 12-week progressive brain training program grounded in FINGER/ACTIVE protocols |
| `skills/sub-improvement-roadmap.md` | Build a progress tracking system, difficulty escalation schedule, and lifestyle synergy recommendations |

## Tools Required
- **WebSearch** — search PubMed, Cochrane, Lancet Neurology, Alzheimer's Association for latest research
- **WebFetch** — fetch full papers, abstracts, and clinical guideline PDFs
- **Read** — read SECOND-KNOWLEDGE-BRAIN.md for cached domain knowledge
- **Write** — write final training program deliverable
- **Bash** — run knowledge_updater.py pipeline

## Knowledge Sources (for crawl pipeline)
- PubMed: queries "dementia prevention cognitive training", "neuroplasticity elderly", "FINGER trial", "dual-task training dementia", "N-back working memory aging"
- Cochrane Reviews: "cognitive training dementia prevention"
- Lancet Neurology: dementia special issues (thelancet.com/journals/laneur)
- Alzheimer's Association: alz.org/research/science/alzheimers-dementia-research
- AAIC proceedings: alz.org/aaic
- WHO Dementia Action Plan: who.int/docs/default-source/dementia/who-dementia-report-2023

## Supporting Python Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that fetches PubMed/Cochrane/Lancet updates weekly, parses and scores entries, appends to SECOND-KNOWLEDGE-BRAIN.md

## Active Development Tasks
- [ ] Phase 0: Research & Architecture (this file + PROJECT-detail.md + SECOND-KNOWLEDGE-BRAIN.md skeleton)
- [ ] Phase 1: Core sub-skills — sub-safety-screener, sub-profile-intake, sub-cognitive-assessment
- [ ] Phase 2: Training design sub-skills — sub-training-designer, sub-improvement-roadmap
- [ ] Phase 3: Main harness wiring (skills/main.md)
- [ ] Phase 4: SECOND-KNOWLEDGE-BRAIN pipeline (tools/knowledge_updater.py)
- [ ] Phase 5: Testing & Validation (tests/test-scenarios.md)

## Reference Documents
- `PROJECT-detail.md` — full technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — build roadmap with milestones
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving domain knowledge base
