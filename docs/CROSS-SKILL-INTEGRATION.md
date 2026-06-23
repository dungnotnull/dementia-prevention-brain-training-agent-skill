# Cross-Skill Integration Documentation

## Health-Wellness Cluster Integration

This skill (ID 236: dementia-prevention-brain-training) is part of the health-wellness cluster and shares common components with other skills in this cluster.

---

## Shared Components Identified

### 1. MIND Diet Module (Shared with clinical-nutrition skill)
- **Source:** dementia-prevention-brain-training `sub-improvement-roadmap.md` and SECOND-KNOWLEDGE-BRAIN.md
- **Reference:** Morris et al. (2015, Alzheimer's & Dementia)
- **Reusable Components:**
  - 15-component MIND diet checklist
  - Dietary guidelines with serving targets
  - Brain-protective nutrients (omega-3, flavonoids, vitamin E, B vitamins)
- **Integration Point:** The MIND diet protocol defined in this skill could be imported by:
  - Clinical nutrition skills (general brain health nutrition)
  - Cardiovascular prevention skills (MIND diet also benefits heart health)
  - Diabetes management skills (nutrition for cognitive protection in diabetics)

### 2. Sleep Hygiene Protocol (Shared with sleep-wellness skill)
- **Source:** `sub-improvement-roadmap.md` - Sleep Hygiene Protocol (7-point)
- **Reference:** Xie et al. (2013, Science) - glymphatic clearance
- **Reusable Components:**
  - 7-point sleep hygiene checklist
  - Amyloid clearance mechanism explanation
  - Sleep tracking prompts
- **Integration Point:** Could be shared with:
  - General sleep improvement skills
  - Mental health skills (sleep-depression connection)
  - Chronic pain management skills (sleep quality impact)

### 3. Social Engagement Calendar (Shared with mental-health, loneliness skills)
- **Source:** `sub-improvement-roadmap.md` - Social Engagement Calendar
- **Reference:** Kelly et al. (2017, Ageing Research Reviews)
- **Reusable Components:**
  - Social engagement frequency targets (3x/week minimum)
  - Activity type classification (in-person, group, teaching, volunteer)
  - Social isolation risk assessment
- **Integration Point:** Could be integrated with:
  - Loneliness prevention skills
  - Depression management skills
  - Senior wellness skills

### 4. Aerobic Exercise for Brain Health (Shared with fitness skills)
- **Source:** `sub-training-designer.md` and SECOND-KNOWLEDGE-BRAIN.md
- **Reference:** Erickson et al. (2011, PNAS) - BDNF and hippocampal volume
- **Reusable Components:**
  - Moderate-intensity aerobic exercise prescription (50-70% max HR)
  - BDNF mechanism explanation
  - Exercise-cognitive training synchronization (dual-task)
- **Integration Point:** Could be shared with:
  - General fitness skills
  - Cardiac rehabilitation skills
  - Post-stroke recovery skills

### 5. Cognitive Screening Framework (Shared with cognitive-assessment skills)
- **Source:** `sub-cognitive-assessment.md` and SECOND-KNOWLEDGE-BRAIN.md
- **Reference:** MoCA/MMSE clinical assessment instruments
- **Reusable Components:**
  - 5-domain cognitive framework (Memory, Attention, Executive, Language, Visuospatial)
  - Self-assessment questionnaire templates
  - MMSE/MoCA threshold interpretation
- **Integration Point:** Could be used by:
  - General cognitive assessment skills
  - ADHD/attention evaluation skills
  - Post-concussion cognitive monitoring skills

---

## Shared Data Structures

### User Health Profile Format
```yaml
user_profile:
  demographics:
    age: integer
    sex: "M" | "F"
    education_years: integer
    occupation: string
    cognitive_demand: "low" | "moderate" | "high"
  
  health_status:
    conditions: list of strings
    medications: list of strings
    lancet_risk_factors: list of strings
    risk_classification: "low" | "moderate" | "high"
  
  lifestyle_baseline:
    physical_activity: "sedentary" | "light" | "moderate" | "very"
    diet_quality: "poor" | "fair" | "good" | "excellent"
    sleep_hours: float
    sleep_quality: string
    social_engagement: "rare" | "occasional" | "regular" | "frequent"
    tobacco_use: boolean
    alcohol_units_per_week: integer
  
  cognitive_profile:
    concerns: list of strings
    mmse_score: integer | null
    moca_score: integer | null
    domain_ratings:
      memory: 1-5
      attention: 1-5
      executive: 1-5
      language: 1-5
      visuospatial: 1-5
    priority_ranking: [domain1, domain2, ...]
  
  constraints:
    daily_training_minutes: integer
    preferred_time: "morning" | "afternoon" | "evening"
    technology_access: "none" | "basic" | "smartphone" | "full"
```

This profile structure could be standardized across the health-wellness cluster to enable data sharing between skills.

---

## Potential Cross-Skill Workflows

### Workflow A: Nutrition + Brain Training
1. User completes clinical-nutrition skill assessment
2. User profile with diet data is passed to dementia-prevention-brain-training
3. Brain training program is customized with MIND diet focus areas
4. Progress tracking reports back to both skills

### Workflow B: Sleep + Cognitive Performance
1. User completes sleep-wellness skill program
2. Sleep quality metrics are passed to cognitive assessment
3. Cognitive training intensity is adjusted based on sleep quality
4. Joint recommendations for sleep hygiene and cognitive timing

### Workflow C: Exercise + Brain Training (Dual-Task)
1. User completes fitness skill assessment
2. Physical capability profile is passed to brain training
3. Dual-task exercises are calibrated to user's fitness level
4. Combined exercise-cognitive sessions are scheduled

### Workflow D: Social Engagement + Cognitive Reserve
1. User completes loneliness-prevention skill program
2. Social activity calendar is shared with brain training
3. Cognitive exercises incorporate social elements
4. Social engagement goals are tracked alongside cognitive progress

---

## Future Harmonization Opportunities

### 1. Common Assessment Module
- Develop a shared `health-profile-intake` sub-skill across cluster
- Standardize the 15-point profile format
- Enable profile passing between skills without re-assessment

### 2. Unified Progress Tracking
- Develop a shared `progress-tracker` component
- Standardize metrics across health-wellness skills
- Enable cross-skill progress visualization

### 3. Shared Evidence Base
- Consolidate SECOND-KNOWLEDGE-BRAIN.md files across cluster
- Create a unified `HEALTH-WELLNESS-KNOWLEDGE.md`
- Implement shared knowledge_updater pipeline

### 4. Common Safety Gate
- Standardize `sub-safety-screener` across cluster
- Shared contraindication database
- Unified medical disclaimer format

---

## Integration API Specification (Future)

### Export Format
```json
{
  "skill_id": "236",
  "skill_name": "dementia-prevention-brain-training",
  "export_type": "user_profile | cognitive_profile | training_plan",
  "data": { ... },
  "timestamp": "ISO-8601",
  "version": "1.0"
}
```

### Import Format
```json
{
  "source_skill_id": "XXX",
  "source_skill_name": "clinical-nutrition",
  "import_type": "dietary_profile",
  "data": {
    "mind_diet_adherence": 0.73,
    "protective_foods_frequency": {...},
    "limit_foods_frequency": {...}
  },
  "timestamp": "ISO-8601",
  "version": "1.0"
}
```

---

## Notes for Future Development

1. **Profile Compatibility:** When designing other health-wellness skills, use the same 15-point profile structure to enable seamless data sharing.

2. **Evidence Source Reuse:** The SECOND-KNOWLEDGE-BRAIN.md contains foundational papers that are relevant to multiple skills (e.g., MIND diet for nutrition skills, sleep studies for sleep skills).

3. **Exercise Library Reuse:** The exercise library in `sub-training-designer.md` includes physical exercises and lifestyle interventions that could be extracted into separate modules.

4. **Caregiver Mode:** The caregiver guidance and referral resources developed for REFER cases could be standardized across all health-wellness skills that work with vulnerable populations.

5. **Progress Metrics:** The 5 progress metrics (memory accuracy, N-back, verbal fluency, dual-task, SCC) could be adapted for other cognitive-focused skills.

---

**Document Version:** 1.0
**Last Updated:** 2026-06-23
**Skill ID:** 236
**Cluster:** health-wellness
