---
name: dementia-prevention-brain-training/sub-improvement-roadmap
description: Builds a progress tracking system, difficulty escalation schedule, lifestyle synergy plan (MIND diet, sleep, social engagement, aerobic exercise), re-assessment timeline, and warning signs for the 12-week brain training program
---

## Purpose

A training program without a progress tracking and lifestyle integration plan has poor adherence and unclear outcomes. This sub-skill transforms the training calendar from `sub-training-designer` into a complete wellness plan: defining what to measure, when to escalate difficulty, how to synchronize lifestyle changes (the proven synergies that amplify cognitive training benefit), when to formally re-assess, and when to stop and seek medical help. It also provides motivational scaffolding grounded in behavioral science to support 12-week adherence.

---

## Inputs

- 12-week training calendar from `sub-training-designer`
- Cognitive domain profile from `sub-cognitive-assessment` (baseline ratings)
- Lifestyle baseline from `sub-profile-intake` (physical activity, diet, sleep, social engagement)
- Safety flags from `sub-safety-screener`

---

## Workflow

### Phase 1: Define Progress Tracking Metrics

Define 5 key progress metrics the user will self-track throughout the program.

**Metric 1: Memory Recall Accuracy**
- **What to measure:** In each memory exercise session (method of loci, spaced retrieval), record the number of correctly recalled items vs. total attempted
- **Tracking unit:** % recall accuracy per session
- **How to log:** Simple tally sheet or notebook entry after each session
- **Target trajectory:**
  - Week 4 target: 60% accuracy on 5-item lists
  - Week 8 target: 70% accuracy on 10-item lists
  - Week 12 target: 75% accuracy on 12-15 item lists
- **Escalation trigger:** 3 consecutive sessions at >= 80% accuracy → advance to next difficulty level

**Metric 2: N-Back Level Achieved**
- **What to measure:** Highest N-back level sustained at >= 80% accuracy over 3 consecutive sessions
- **Tracking unit:** N-back level (1 / 2 / 3 / dual)
- **Target trajectory:** Level 1 (Week 4) → Level 2 (Week 8) → Level 3 (Week 12)
- **Escalation trigger:** >= 80% accuracy for 3 consecutive sessions → advance to next N level

**Metric 3: Verbal Fluency Score**
- **What to measure:** Number of correct items named in 60-second category fluency task (animals, fruits, tools)
- **Tracking unit:** Number of correct items per 60-second trial
- **How to log:** Count items, note category, date
- **Normative reference:** Age 65-74 adults: average ~17 words in 60 seconds (semantic fluency, animals); < 12 suggests significant language decline (Kempler et al., 1998, Clinical Neuropsychologist)
- **Target trajectory:**
  - Week 4: Baseline established (measure 3x, average)
  - Week 8: 10% improvement vs. baseline
  - Week 12: 20% improvement vs. baseline

**Metric 4: Dual-Task Performance Rating**
- **What to measure:** Self-rated difficulty of combined physical-cognitive dual-task session (1-10 scale: 1 = extremely difficult, 10 = easy)
- **Tracking unit:** Self-rated ease score per dual-task session
- **Target trajectory:** Scores improve (become easier) over weeks; target average of 7/10 by Week 12
- **Escalation trigger:** Average >= 7/10 for 3 sessions → increase cognitive task difficulty or walking pace

**Metric 5: Subjective Cognitive Confidence (SCC)**
- **What to measure:** Weekly self-assessment using a 5-item confidence questionnaire:
  1. "I felt confident in my memory today" (1-5 scale)
  2. "I could focus when needed" (1-5 scale)
  3. "I found words easily when speaking" (1-5 scale)
  4. "I felt mentally sharp" (1-5 scale)
  5. "I felt good about my overall cognitive health this week" (1-5 scale)
- **Tracking unit:** SCC Score = sum of 5 items (5-25 scale)
- **Target trajectory:** Establish baseline Week 1; target +15% improvement by Week 12
- **Evidence:** SCC correlates with both objective performance and emotional wellbeing; improvement in SCC is itself an outcome (Troyer & Rich, 2002, Neuropsychological Rehabilitation)

#### Weekly Progress Log Template
```
Week [X] — Progress Log
========================
Date: _______________

MEMORY RECALL ACCURACY
Session 1: ___/total = ___%  | Session 2: ___/total = ___% | Session 3: ___/total = ___%
Weekly Average: ___%

N-BACK PERFORMANCE
Current Level: __ | Sessions this week: __ | Average Accuracy: ___%
Ready to advance? (>= 80% for 3 sessions): YES / NO

VERBAL FLUENCY
Category: ________ | Items named in 60 sec: ___
Baseline (Week 1): ___ | Change from baseline: ____%

DUAL-TASK EASE RATING
Session 1: __/10 | Session 2: __/10 | Session 3: __/10 | Average: __/10

SUBJECTIVE COGNITIVE CONFIDENCE
Q1: __ Q2: __ Q3: __ Q4: __ Q5: __ | Total: __/25
Change from last week: ___

AEROBIC EXERCISE THIS WEEK
Sessions completed: __ | Total minutes: __

SLEEP THIS WEEK
Average hours per night: __ | Nights with 7+ hours: __/7

SOCIAL ENGAGEMENTS THIS WEEK
Number of meaningful social interactions: __

NOTES / OBSERVATIONS:
_______________________________________
```

---

### Phase 2: Difficulty Escalation Rules

**Global Escalation Rule:**
A user is ready to advance to the next difficulty level within any exercise when:
- Performance meets the escalation trigger (defined per metric above), AND
- At least 1 week has passed at the current level (no rushing)

**Exercise-Specific Escalation:**

| Exercise | Current Level | Escalation Trigger | Next Level |
|----------|-------------|-------------------|-----------|
| N-back | 1-back | >= 80% accuracy, 3 sessions | 2-back |
| N-back | 2-back | >= 80% accuracy, 3 sessions | 3-back or dual |
| Method of Loci | 5-item list | >= 75% recall, 3 sessions | 10-item list |
| Method of Loci | 10-item list | >= 75% recall, 3 sessions | 15-item list |
| Tower of Hanoi | 3 discs | Completed puzzle in <= 7 moves, 3 sessions | 4 discs |
| Verbal Fluency | Common categories | >= 20 items/60 sec, 3 sessions | Uncommon categories |
| Jigsaw Puzzle | 100-200 pieces | Completed in target time | 300-500 pieces |
| Dual-Task Walk | Easy cognitive overlay | Ease rating >= 7/10, 3 sessions | More complex overlay |
| Stroop | Standard color-word | < 30 sec completion with <= 2 errors | Number-letter variant |

**Deceleration Rule:** If performance drops more than 20% from personal best for 2 consecutive sessions, return to the previous difficulty level. This is not a failure — it is adaptive training.

---

### Phase 3: Lifestyle Synergy Plan

**Evidence foundation:** The FINGER trial's success came from a multidomain intervention — cognitive training alone produces modest effects; combined with physical exercise, diet improvement, and vascular risk management, the benefit roughly doubles (Ngandu et al., 2015).

#### 3A: MIND Diet Implementation Plan

The MIND diet (Morris et al., 2015, Alzheimer's & Dementia) is the only diet directly shown to reduce Alzheimer's risk specifically (not just cardiovascular risk). Strict adherence reduces risk by 53%; even moderate adherence by 35%.

**Weekly MIND Diet Checklist:**

| Component | Target | Priority |
|-----------|--------|---------|
| Green leafy vegetables (spinach, kale, lettuce) | 6+ servings/week | HIGH |
| Other vegetables (non-leafy) | 7+ servings/week (1/day) | HIGH |
| Berries (blueberries, strawberries) | 2+ servings/week | HIGH |
| Nuts (walnuts, almonds, pistachios) | 5+ servings/week | HIGH |
| Olive oil | Primary cooking fat | HIGH |
| Whole grains (oats, quinoa, whole wheat) | 3+ servings/day | MEDIUM |
| Fish (salmon, tuna, sardines) | 1+ serving/week | HIGH |
| Beans/legumes | 4+ meals/week | MEDIUM |
| Poultry (chicken, turkey) | 2+ servings/week | MEDIUM |
| Wine (optional) | 1 glass/day maximum | LOW (optional) |
| Red meat | Limit to < 4 servings/week | AVOID excess |
| Butter/margarine | < 1 tablespoon/day | LIMIT |
| Cheese | < 1 serving/week | LIMIT |
| Pastries/sweets | < 5 servings/week | LIMIT |
| Fried/fast food | < 1 serving/week | AVOID |

**Practical implementation:** Don't overhaul diet all at once. Week 1-2: Focus on adding 2 daily vegetable servings and switching to olive oil. Week 3-4: Add berries 3x/week and a fish dinner. Week 5-8: Add nuts as snacks; reduce red meat frequency. Week 9-12: Full MIND diet adherence goal.

**Key nutrients for brain health:**
- **Omega-3 fatty acids (DHA/EPA):** Found in fatty fish; associated with reduced amyloid deposition (Calon et al., 2004, Neuron)
- **Flavonoids (berries, dark chocolate):** Increase cerebral blood flow and BDNF (Devore et al., 2012, Annals of Neurology)
- **Vitamin E (nuts, leafy greens):** Antioxidant protection for neurons (Morris et al., 2002, JAMA)
- **B vitamins (B6, B12, folate):** Reduce homocysteine, a vascular risk factor (Douaud et al., 2013, PNAS — B vitamins slow brain atrophy in MCI)

#### 3B: Sleep Hygiene Protocol

Amyloid-beta clearance occurs primarily during slow-wave sleep via the glymphatic system (Xie et al., 2013, Science). Chronic sleep deprivation accelerates amyloid accumulation and is a significant modifiable dementia risk factor.

**7-Point Sleep Hygiene Protocol:**

1. **Consistent schedule:** Go to bed and wake up at the same time every day (including weekends) — within 30-minute variation. Target: 7-9 hours for adults 65+.
2. **Pre-sleep wind-down:** Begin a 30-45 minute wind-down routine: no screens, dim lights, light reading or gentle stretching.
3. **Blue light elimination:** No smartphones, tablets, or computers within 90 minutes of sleep time (blue light suppresses melatonin — Harvard Medical School guidelines).
4. **Alcohol avoidance:** No alcohol within 3 hours of bedtime — alcohol suppresses slow-wave sleep and impairs glymphatic clearance.
5. **Bedroom environment:** Dark (use blackout curtains), cool (65-68°F / 18-20°C), quiet (or use white noise if needed).
6. **Afternoon caffeine cutoff:** No caffeinated beverages after 2 PM (caffeine half-life ~5-6 hours).
7. **Sleep-wake anchor:** Expose yourself to bright natural light within 30 minutes of waking — this anchors circadian rhythm and ensures deeper slow-wave sleep the following night.

**Sleep Tracking Prompt (Weekly Log):**
"Rate your sleep for the week:
- Average hours per night: ___
- How many nights did you get 7+ hours? ___ /7
- How often did you feel rested on waking? (1-7 days): ___"

#### 3C: Social Engagement Calendar

Social isolation is responsible for 4% of dementia cases (Lancet Commission 2020). High social engagement reduces dementia risk by 38% (Kelly et al., 2017, Ageing Research Reviews). Social activities also provide natural cognitive dual-tasking (attending to others, responding appropriately, remembering names and context).

**Weekly Social Engagement Targets:**

| Activity Type | Frequency | Cognitive Benefit |
|--------------|-----------|-----------------|
| In-person conversations (family, friends, neighbors) | 3-5x/week | Language, episodic memory, emotional processing |
| Group activity (book club, church, community class) | 1-2x/week | Attention, executive function, social cognition |
| Teaching or explaining something to another person | 1x/week | Memory consolidation, verbal fluency |
| Telephone/video calls (if mobility-limited) | 3-5x/week | Language, processing speed |
| Volunteer work or mentoring | 1-2x/week | Sense of purpose, executive function |

**Month-by-Month Social Calendar:**
- Month 1: Commit to 3 regular social interactions per week (any type)
- Month 2: Add one new group activity (class, club, volunteer opportunity)
- Month 3: Aim to teach or mentor someone at least twice this month

#### 3D: Stress Management

Chronic psychological stress increases cortisol, which damages hippocampal neurons and impairs neurogenesis (McEwen, 2000, Annual Review of Neuroscience — glucocorticoid neurotoxicity). Stress management is therefore a dementia prevention strategy.

**Evidence-Based Stress Reduction Recommendations:**

1. **Mindfulness-Based Stress Reduction (MBSR):** Even 10 minutes/day of guided mindfulness meditation reduces cortisol and improves attention (Hölzel et al., 2011, Psychiatry Research — MBSR increases hippocampal gray matter density)
2. **Aerobic exercise:** Already in the training plan — direct cortisol-lowering effect; increases BDNF
3. **Progressive Muscle Relaxation (PMR):** 10-15 min before sleep; reduces nighttime cortisol; improves sleep quality

---

### Phase 4: Re-Assessment Schedule

**Why re-assess formally:** Self-tracking metrics measure relative improvement within the program. A formal cognitive assessment with a healthcare provider measures absolute cognitive status against normative benchmarks. The re-assessment at 12 weeks allows the physician to determine whether the training is working, whether the program should continue, modify, or escalate.

**Recommended Re-Assessment Schedule:**

| Milestone | Action | Who Administers |
|-----------|--------|----------------|
| Week 12 (End of Program) | MoCA or MMSE re-test | Physician, neuropsychologist, or trained clinic nurse |
| 6 Months Post-Program | MoCA or MMSE | Same as above |
| 12 Months Post-Program | Full neuropsychological battery (if concerns persist) | Neuropsychologist |
| Annually (ongoing) | Annual cognitive wellness check | Primary care physician |

**What to bring to the re-assessment appointment:**
1. Your Week 12 Progress Log (print and bring)
2. List of all cognitive exercises completed (training calendar with completion notes)
3. This AI-generated program document
4. Notes on any concerning changes observed during the 12 weeks
5. List of all current medications

**Informing re-assessment goal:** The target is not a specific score — it is stability or improvement compared to your baseline. In the FINGER trial, the intervention group showed 25% better cognitive composite performance vs. controls at 2 years. In a 12-week program, modest improvement (5-10% on objective measures) or stable scores (no decline) is a meaningful, positive outcome.

---

### Phase 5: Warning Signs — When to Stop and Consult a Doctor

Include the following warning signs list in the final deliverable. These are conditions under which the user should stop all training exercises and contact their physician promptly.

**STOP EXERCISES AND CONTACT YOUR DOCTOR IF YOU EXPERIENCE:**

1. **Sudden worsening of confusion or disorientation** — especially if it appears abruptly rather than gradually
2. **New or sudden headaches** — especially severe or "thunderclap" headaches unlike any previous headache
3. **New changes in speech or language** — difficulty finding words suddenly worsens significantly, or you have trouble understanding others
4. **Vision changes** — blurry or double vision, visual field loss
5. **New weakness or numbness** — in face, arm, or leg (possible TIA/stroke — seek emergency care immediately)
6. **Seizure-like episodes** — uncontrolled shaking, loss of consciousness, blank staring spells
7. **Significant emotional distress from exercises** — if exercises consistently cause severe frustration, distress, anxiety, or sadness
8. **Falls or balance problems increasing** — especially during dual-task walking sessions; may indicate vestibular or neurological issues
9. **Marked and rapid cognitive decline** — if you or your family notice cognitive function worsening rapidly (not just bad days, but a clear decline over 2-4 weeks)
10. **Any new neurological symptom** that was not present before starting the program

---

### Phase 6: Motivational Scaffolding

**Adherence is the #1 predictor of cognitive training outcomes** — a perfect 12-week program with 50% adherence produces weaker effects than a moderate program with 95% adherence.

**Behavioral strategies for adherence:**

1. **Implementation intentions:** Don't just decide to train — write down exactly WHEN and WHERE (e.g., "Every morning at 9 AM at my kitchen table before breakfast")
2. **Habit stacking:** Attach training to an existing routine (e.g., N-back practice while waiting for morning coffee to brew)
3. **Progress visibility:** Keep your Weekly Progress Log visible — on the refrigerator, bathroom mirror, or bedside table
4. **Social accountability:** Tell one trusted person about your program; brief them weekly on progress
5. **Celebrate micro-wins:** Mark every session completed with a checkmark. Review your progress log every Sunday
6. **Forgiveness rule:** Missing 1-2 days does not break the program. Just resume the next session. Evidence shows that intermittent training (5 of 7 days) produces similar outcomes to daily training

---

## Outputs

- Progress tracking system (5 metrics + weekly log template)
- Difficulty escalation rules (per exercise)
- Lifestyle synergy plan:
  - MIND diet implementation plan with weekly checklist
  - Sleep hygiene protocol (7 points)
  - Social engagement calendar (monthly targets)
  - Stress management recommendations
- Re-assessment schedule (12-week + 6-month + annual)
- Warning signs list (when to stop and seek medical help)
- Motivational scaffolding strategies

---

## Quality Gate

- [ ] All 5 progress metrics are defined with baseline, targets, and escalation triggers
- [ ] Weekly Progress Log template is provided (user-ready format)
- [ ] Difficulty escalation rules are defined for at least 5 exercise types
- [ ] MIND diet checklist includes all 15 components with targets
- [ ] Sleep hygiene protocol includes the glymphatic clearance mechanism citation
- [ ] Social engagement targets are specified (minimum 3x/week)
- [ ] Re-assessment schedule recommends formal MMSE/MoCA via physician at 12 weeks
- [ ] At least 3 lifestyle synergies include evidence citations
- [ ] Warning signs list contains at least 8 items
- [ ] Motivational scaffolding includes at least 4 strategies
