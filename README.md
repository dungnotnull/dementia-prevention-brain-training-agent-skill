# Dementia Prevention Brain Training (Skill 236)

Evidence-based 12-week personalized cognitive training program for dementia and Alzheimer's prevention in older adults, grounded in FINGER/ACTIVE trial protocols and neuroplasticity science.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Status: Production Ready](https://img.shields.io/badge/Status-Production--Ready-green.svg)](https://github.com/your-org/dementia-prevention-brain-training)

## ⚠️ IMPORTANT MEDICAL DISCLAIMER

**This skill provides educational wellness guidance only. It is NOT a medical diagnosis, clinical assessment, or medical treatment. It does NOT replace consultation with a licensed neurologist, geriatrician, or neuropsychologist.**

If you experience sudden confusion, disorientation, new headaches, vision changes, speech difficulties, dizziness, or any new neurological symptoms, **stop all exercises and consult a physician immediately.**

## Overview

This skill is a clinically-grounded, safety-first cognitive training planner for older adults seeking evidence-based interventions to prevent or delay dementia and Alzheimer's disease. It combines:

- **5-domain cognitive assessment** (Memory, Attention, Executive Function, Language, Visuospatial)
- **Personalized 12-week progressive training program** grounded in peer-reviewed research
- **Multidomain lifestyle integration** (MIND diet, aerobic exercise, sleep hygiene, social engagement)
- **Safety-gated architecture** with mandatory medical screening
- **Continuous knowledge updates** via weekly PubMed/Cochrane/Lancet crawls

## Key Features

### 🧠 Evidence-Based Training Protocols
- **FINGER Trial Protocol**: Multidomain lifestyle intervention (25% cognitive improvement)
- **ACTIVE Study Framework**: 10-year lasting benefits from targeted cognitive training
- **N-Back Training**: Working memory enhancement with progressive difficulty
- **Method of Loci**: Episodic memory technique (97% improvement in word-list recall)
- **Dual-Task Training**: Combined physical-cognitive sessions for real-world transfer
- **BrainHQ-Inspired Exercises**: Speed-of-processing training validated by Posit Science

### 🛡️ Safety First Architecture
- **Non-bypassable safety gate** screens for contraindications before any guidance
- **Mandatory medical disclaimer** in all outputs
- **Physician referral triggers** for active dementia, recent stroke, severe impairment
- **Conditional modifications** for health conditions (hypertension, Parkinson's, medications)
- **Caregiver guidance mode** for REFER cases

### 📊 Personalized Assessment
- **15-point user profile** covering demographics, health, lifestyle, and cognitive concerns
- **5-domain cognitive radar** with self-assessment and MoCA/MMSE integration
- **Lancet Commission 2020** modifiable risk factor mapping
- **Priority-based training** targeting most impaired cognitive domains

### 🔄 Continuous Improvement
- **Automated knowledge pipeline** crawls PubMed, Cochrane, Lancet weekly
- **Relevance-scoring algorithm** filters for high-impact research
- **Deduplication system** prevents duplicate entries
- **Version tracking** for all knowledge updates

### 🌱 Holistic Lifestyle Integration
- **MIND Diet Protocol**: 15-component brain-protective nutrition plan
- **Sleep Hygiene**: 7-point protocol for glymphatic amyloid clearance
- **Aerobic Exercise**: BDNF-boosting physical activity synchronized with cognitive training
- **Social Engagement**: Activity calendar targeting 3+ meaningful interactions/week
- **Progress Tracking**: 5 key metrics with escalation rules and weekly logging

## Installation

### Requirements
```bash
pip install crawl4ai requests beautifulsoup4 lxml
playwright install chromium
```

### Optional: NCBI API Key
For higher PubMed rate limits (10 req/sec vs 3 req/sec):
```bash
export NCBI_API_KEY="your-key-here"
```

### Setup
1. Clone this repository
2. All skill files are ready to use — no additional configuration required
3. For automatic knowledge updates, set up cron job (see below)

## Usage

### Basic Invocation
```
/dementia-prevention-brain-training
```

### With Initial Context
```
/dementia-prevention-brain-training I'm 68 and my mother had Alzheimer's. What brain exercises should I do?
```

### Knowledge Update Pipeline
```bash
# Manual update
python tools/knowledge_updater.py

# Dry run (preview without writing)
python tools/knowledge_updater.py --dry-run

# Limit entries per run
python tools/knowledge_updater.py --max 20
```

### Automated Weekly Updates
**Crontab (Unix/Linux/Mac):**
```cron
0 8 * * 0 cd /path/to/dementia-prevention-brain-training/tools && /usr/bin/python3 knowledge_updater.py >> knowledge_updater.log 2>&1
```

**Windows Task Scheduler:**
```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "D:\path\to\tools\knowledge_updater.py"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 8am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "BrainTrainingKnowledgeUpdater"
```

## File Structure

```
dementia-prevention-brain-training/
├── README.md                           # This file
├── CLAUDE.md                           # Skill-level memory and instructions
├── PROJECT-detail.md                   # Full technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md # Development milestone tracking
├── SECOND-KNOWLEDGE-BRAIN.md           # Domain knowledge base (auto-updated)
├── docs/
│   └── CROSS-SKILL-INTEGRATION.md      # Integration with health-wellness cluster
├── skills/
│   ├── main.md                         # Main harness (orchestrates all sub-skills)
│   ├── sub-safety-screener.md          # Safety gate (non-bypassable)
│   ├── sub-profile-intake.md           # 15-point user profile collection
│   ├── sub-cognitive-assessment.md     # 5-domain cognitive assessment
│   ├── sub-training-designer.md        # 12-week program designer
│   └── sub-improvement-roadmap.md      # Progress tracking & lifestyle plan
├── tools/
│   └── knowledge_updater.py            # PubMed/Cochrane crawl pipeline
└── tests/
    └── test-scenarios.md               # 7 test scenarios with expected outputs
```

## Workflow

The skill follows a 6-step process:

1. **Safety Gate** → Screen for contraindications, issue disclaimer
2. **Profile Intake** → Collect 15-point user profile
3. **Cognitive Assessment** → Evaluate 5 domains, establish baseline
4. **Training Design** → Build personalized 12-week progressive program
5. **Improvement Roadmap** → Add progress tracking and lifestyle plan
6. **Final Deliverable** → Synthesize professional training document

## Test Scenarios

Seven comprehensive test scenarios cover:
- ✅ Healthy older adult with family history
- ✅ Mild cognitive impairment (MoCA 24) with hypertension
- ✅ Recent TIA → REFER trigger
- ✅ Active dementia → REFER + caregiver mode
- ✅ Borderline impairment (MoCA 18) → REFER
- ✅ Caregiver-designed program (low-tech, bereavement)
- ✅ Graceful degradation (WebSearch unavailable)

See `tests/test-scenarios.md` for complete details.

## Evidence Base

This skill cites only peer-reviewed research (Tier 4+ evidence hierarchy):

**Core Clinical Trials:**
- FINGER Trial (Ngandu et al., 2015, Lancet) — 25% cognitive improvement
- ACTIVE Study (Rebok et al., 2014, JAMA Internal Medicine) — 10-year benefits
- MAPT Trial (Vellas et al., 2014) — Multidomain prevention

**Foundational Science:**
- Cognitive Reserve Theory (Stern, 2002, Neurology)
- BDNF and Exercise (Erickson et al., 2011, PNAS)
- Glymphatic Clearance (Xie et al., 2013, Science)
- Method of Loci (Dresler et al., 2017, Neuron)

**Lifestyle Research:**
- MIND Diet (Morris et al., 2015, Alzheimer's & Dementia) — 53% risk reduction
- Social Engagement (Kelly et al., 2017, Ageing Research Reviews) — 38% risk reduction
- Lancet Commission 2020 — 12 modifiable risk factors

See `SECOND-KNOWLEDGE-BRAIN.md` for complete bibliography.

## Cross-Skill Integration

This skill integrates with the health-wellness cluster:

**Shared Components:**
- MIND Diet Module (clinical-nutrition skills)
- Sleep Hygiene Protocol (sleep-wellness skills)
- Social Engagement Calendar (mental-health skills)
- Aerobic Exercise for Brain Health (fitness skills)
- Cognitive Screening Framework (cognitive-assessment skills)

See `docs/CROSS-SKILL-INTEGRATION.md` for integration specifications.

## Contributing

Contributions are welcome! Please:

1. **Clinical Review**: This skill should be reviewed by geriatric specialists
2. **Evidence Updates**: Submit new peer-reviewed research via PRs to SECOND-KNOWLEDGE-BRAIN.md
3. **Translation**: Localization for different languages and cultures
4. **Accessibility**: Improve accessibility for users with disabilities

## License

MIT License — See LICENSE file for details

**Attribution Requirements:**
- Cite FINGER trial, ACTIVE study, and referenced papers
- Maintain medical disclaimer in all distributions
- Include liability limitation

## Acknowledgments

**Research Foundations:**
- FINGER Study Group (Ngandu et al.)
- ACTIVE Trial Investigators (Rebok et al.)
- Posit Science / BrainHQ (Merzenich et al.)
- Cochrane Dementia and Cognitive Improvement Group

**Clinical Guidelines:**
- WHO Dementia Action Plan
- Lancet Commission on Dementia Prevention, Intervention, and Care
- Alzheimer's Association

## Citation

If you use this skill in research or clinical work, please cite:

```
Dementia Prevention Brain Training Skill (Skill 236).
Evidence-based cognitive training for dementia prevention.
Version 1.0. 2026.
https://github.com/your-org/dementia-prevention-brain-training
```

## Support

- **Issues**: Report bugs via GitHub Issues
- **Clinical Questions**: Consult with licensed healthcare professionals
- **Emergency**: Call emergency services for acute neurological symptoms

## Disclaimer

**THIS IS NOT MEDICAL ADVICE.** This skill provides educational wellness information based on published peer-reviewed research. Individual responses to cognitive training vary. Some conditions require medical supervision before starting any new cognitive training program. Always consult with qualified healthcare professionals for medical advice, diagnosis, or treatment.

---

**Last Updated:** 2026-06-23  
**Version:** 1.0  
**Status:** Production Ready ✅
