---
name: dementia-prevention-brain-training/sub-profile-intake
description: Collects a comprehensive 15-point user profile to personalize the brain training program — covering demographics, health conditions, lifestyle, cognitive concerns, and available time
---

## Purpose

This sub-skill gathers all the personalization data needed to make the brain training program specific to the individual. A generic brain training program has weak effects; a program tailored to the user's age, cognitive concerns, health conditions, lifestyle baseline, and available time produces meaningful, sustained engagement and better outcomes. This profile also maps the user's modifiable risk factors against the Lancet Commission 2020 list, so the improvement roadmap can target the highest-impact changes.

---

## Inputs

- Safety classification and flags from `sub-safety-screener` (must run first)
- Any information the user shared in their initial query or during the safety screen
- User's free-form or Q&A responses to the 15-point profile

---

## Workflow

### Phase 1: Set Intake Context

State: "Now I'd like to learn more about you so I can design a program that truly fits your life. I'll ask about your health history, daily habits, and cognitive concerns. You can answer in your own words — I'll organize the information. Please be as specific as you feel comfortable."

### Phase 2: Collect 15 Profile Data Points

Work through the following 15 data points, adapting the questions naturally to the conversation. Not all need to be rigid Q&A — extract information from free-form responses where possible.

**Data Point 1 — Age and Sex:**
"How old are you, and what is your biological sex? (This helps calibrate the program to age-appropriate norms — e.g., normative MoCA scores differ by age group.)"

**Data Point 2 — Education Level:**
"How many years of formal education have you completed? (For example: 12 years = high school graduate; 16 = bachelor's degree; 18+ = graduate degree.) This is important because education is a key driver of cognitive reserve."

**Data Point 3 — Occupational History:**
"What type of work did/do you do? Was it cognitively demanding — for example, requiring reading, analysis, planning, teaching, or creative work? Or was it primarily manual/routine? This shapes how much occupational cognitive reserve you've built."

**Data Point 4 — Current Health Conditions:**
"Do you have any of the following health conditions? (Please select all that apply, or describe in your own words)
- High blood pressure (hypertension)
- Type 2 diabetes
- Heart disease or atrial fibrillation
- Significant hearing loss (not corrected by hearing aids)
- Thyroid disorder (hypothyroidism)
- Chronic pain conditions
- Obesity (BMI > 30)
- Vision impairment that affects daily activities
- None of the above"

**Data Point 5 — Current Medications:**
"Which medications do you take regularly? (Include prescriptions, over-the-counter, and supplements if relevant.) If you listed any during the safety screen, you can skip those."

**Data Point 6 — Physical Activity Level:**
"How physically active are you on a typical week?
- Sedentary (mostly sitting; less than 30 min of walking per week)
- Lightly active (some walking; 30-90 min of light activity per week)
- Moderately active (150+ min of moderate activity per week — walking, swimming, cycling)
- Very active (vigorous exercise 5+ days per week)"

**Data Point 7 — Diet Quality:**
"How would you rate your current diet?
- Poor (frequent fast food, processed foods, few vegetables)
- Fair (some healthy choices; inconsistent)
- Good (mostly whole foods; vegetables most days; limited processed food)
- Excellent (closely following Mediterranean, DASH, or MIND diet principles)"

**Data Point 8 — Sleep Quality & Quantity:**
"How many hours of sleep do you typically get per night? Do you feel rested when you wake up? Do you have any sleep problems (insomnia, sleep apnea, restless sleep)?"

**Data Point 9 — Social Engagement Level:**
"How often do you interact meaningfully with other people (conversations, group activities, volunteering, clubs, family gatherings)?
- Rarely (less than once per week)
- Occasionally (1-2 times per week)
- Regularly (3-4 times per week)
- Frequently (nearly every day)"

**Data Point 10 — Tobacco and Alcohol Use:**
"Do you currently smoke or use tobacco products? How many drinks of alcohol do you consume per week on average? (This is important because both are modifiable dementia risk factors.)"

**Data Point 11 — Family History of Dementia:**
"Has a parent, sibling, or other close relative been diagnosed with Alzheimer's disease or another type of dementia? If yes, at what age did they develop symptoms?"

**Data Point 12 — Primary Cognitive Concerns:**
"What cognitive changes worry you most? (Please describe in your own words — examples: 'I forget names of people I've known for years,' 'I get confused in unfamiliar places,' 'I lose track of conversations,' 'I have trouble focusing on books or TV programs I used to enjoy,' 'I misplace things often')"

**Data Point 13 — Prior Cognitive Test Results:**
"Have you had any formal cognitive tests done by a doctor or neuropsychologist? If yes, what was your score? Common tests are:
- MMSE (Mini-Mental State Examination) — score out of 30
- MoCA (Montreal Cognitive Assessment) — score out of 30
- Any neuropsychological evaluation"

**Data Point 14 — Daily Routine & Available Time:**
"How much time can you realistically commit to brain training each day? And when during the day works best for you? (Morning, afternoon, evening?) This helps design a schedule you'll actually stick to."

**Data Point 15 — Technology Access & Comfort:**
"Do you have access to a smartphone, tablet, or computer? How comfortable are you using technology for activities like apps, video calls, or online exercises? This determines whether we can include app-based exercises (e.g., BrainHQ-style) or focus on pen-and-paper / in-person activities."

### Phase 3: Completeness Check

After collecting responses, check that at least 12 of 15 data points have been collected. If fewer than 12 are available:
- Identify the most critical missing points (health conditions, activity level, cognitive concerns, age are highest priority)
- Prompt once more for missing critical data points
- If user cannot or will not provide, proceed with noted gaps and flag them in the profile

### Phase 4: Map Modifiable Risk Factors

Map the user's profile against the Lancet Commission 2020 twelve modifiable risk factors. For each risk factor present, note:
- Risk factor name
- User's status (present / absent / unknown)
- Weight (population attributable fraction from Lancet 2020)
- Modifiable through this program (yes / partly / no — physician required)

| Risk Factor | Lancet Weight | User Status | Modifiable Here |
|-------------|-------------|-------------|----------------|
| Low education (lifelong) | 7% | [from DP2] | Partly (cognitive enrichment) |
| Hypertension (midlife) | 2% | [from DP4] | No (physician) / lifestyle |
| Obesity (midlife) | 1% | [from DP4] | Partly (MIND diet + exercise) |
| Hearing loss | 8% | [from DP4] | No (hearing aid) / note |
| Depression | 4% | [from DP4] | Partly (exercise + social) |
| Physical inactivity | 2% | [from DP6] | Yes (aerobic exercise plan) |
| Diabetes | 1% | [from DP4] | Partly (diet + exercise) |
| Excessive alcohol | 1% | [from DP10] | Yes (education) |
| Head injury history | 3% | [safety screen] | N/A |
| Air pollution exposure | 2% | [context] | Limited |
| Social isolation | 4% | [from DP9] | Yes (social engagement plan) |
| Smoking | 5% | [from DP10] | Yes (cessation recommendation) |

### Phase 5: Output Structured Profile

Produce a structured profile summary in the following format:

```
=== USER COGNITIVE WELLNESS PROFILE ===

DEMOGRAPHICS
- Age: [X] | Sex: [X]
- Education: [X years / equivalent degree]
- Occupational Cognitive Demand: [High / Moderate / Low]

HEALTH STATUS
- Key Conditions: [list]
- Medications of Note: [list or 'None flagged']
- Lancet 2020 Modifiable Risk Factors Present: [list with weights]
- Overall Risk Profile: [Low / Moderate / High]

LIFESTYLE BASELINE
- Physical Activity: [level]
- Diet Quality: [level + MIND diet adherence estimate]
- Sleep: [hours per night + quality note]
- Social Engagement: [frequency]
- Tobacco/Alcohol: [status]

FAMILY HISTORY
- [Present / Absent] — [relationship], onset age [X]

COGNITIVE CONCERNS (User-Reported)
- Primary concern: [quoted or paraphrased]
- Secondary concerns: [list]

PRIOR TEST SCORES
- MMSE: [score / not available]
- MoCA: [score / not available]
- Other: [note]

PRACTICAL CONSTRAINTS
- Daily training time available: [X minutes]
- Best time of day: [morning / afternoon / evening]
- Technology access: [level]

COMPLETENESS
- Data points collected: [X]/15
- Missing/uncertain: [list]
```

---

## Outputs

- Structured 15-point user profile (formatted summary above)
- Modifiable risk factor map (table)
- Overall cognitive risk classification: Low / Moderate / High
- Profile completeness score (X/15)
- Missing data points flagged (if any)

---

## Quality Gate

- [ ] At least 12 of 15 data points have been collected and documented
- [ ] Age has been collected (required for all downstream scoring)
- [ ] At least one cognitive concern has been stated by the user
- [ ] Physical activity level has been assessed
- [ ] Modifiable risk factor map has been completed (even with unknowns noted)
- [ ] Profile completeness score is documented
- [ ] Output profile is structured and ready to pass to `sub-cognitive-assessment`
