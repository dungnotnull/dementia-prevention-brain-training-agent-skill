---
name: dementia-prevention-brain-training/sub-cognitive-assessment
description: Evaluates five cognitive domains through self-assessment questions and MMSE/MoCA proxy mapping, producing a domain radar and training priority ranking to personalize the 12-week program
---

## Purpose

This sub-skill establishes the user's current cognitive profile across the five domains most sensitive to dementia-related decline: memory, attention, executive function, language, and visuospatial processing. It uses a structured self-assessment questionnaire validated against MoCA sub-domain constructs, maps any available formal test scores, and produces a domain radar that drives training prioritization in the next sub-skill. This is an educational screening tool — not a clinical diagnostic.

---

## Inputs

- Completed user profile from `sub-profile-intake`
- Any MMSE/MoCA scores provided by the user
- Any specific cognitive concerns noted during profile intake
- Safety classification from `sub-safety-screener` (must be CLEAR or CONDITIONAL)

---

## Workflow

### Phase 1: Set Assessment Context

State: "Now I'd like to understand your current cognitive strengths and areas of concern across five key brain domains. I'll ask you a series of questions about your day-to-day experience. There are no right or wrong answers — just honest reflection on what you notice. This is not a medical test; it is an educational tool to help me design the right training program for you.

If you have received an MMSE or MoCA score from your doctor, please share it — I'll incorporate it into this assessment."

### Phase 2: Domain Self-Assessment Questionnaire

For each domain, rate each question on a 1-5 scale:
5 = No difficulty / fully intact
4 = Minor occasional difficulty
3 = Noticeable difficulty that sometimes affects daily life
2 = Frequent difficulty that often affects daily life
1 = Significant difficulty requiring help from others

**DOMAIN 1: MEMORY (Episodic + Working Memory)**

"In your day-to-day life, how often do you experience the following?"

M1. "Forgetting the names of people you've known for a long time (e.g., neighbors, acquaintances)"
M2. "Forgetting where you placed common items (keys, glasses, phone)"
M3. "Forgetting appointments, meetings, or events you planned"
M4. "Struggling to remember a conversation you had earlier the same day"
M5. "Losing track of what you were about to do or say mid-task ('going into a room and forgetting why')"
M6. "Difficulty remembering a phone number or a short list of items without writing it down"

Memory Domain Score = Average of M1-M6 ratings

**DOMAIN 2: ATTENTION & CONCENTRATION**

A1. "Finding it hard to focus on reading a book, article, or TV program that you used to enjoy"
A2. "Getting distracted easily when multiple things are happening at once"
A3. "Losing your place while doing a task and struggling to return to it"
A4. "Finding it harder to do two things at once (e.g., talk while cooking)"
A5. "Feeling mentally fatigued after tasks that used to feel easy"

Attention Domain Score = Average of A1-A5 ratings

**DOMAIN 3: EXECUTIVE FUNCTION (Planning, Flexibility, Inhibition)**

E1. "Having difficulty planning a complex task (like organizing a trip, a family event, or a project)"
E2. "Finding it harder than before to switch between tasks or adjust plans when something changes"
E3. "Struggling to manage finances, schedules, or paperwork as well as you used to"
E4. "Having difficulty making decisions — especially when there are many options"
E5. "Acting impulsively or saying things without thinking (more than before)"

Executive Function Score = Average of E1-E5 ratings

**DOMAIN 4: LANGUAGE (Word-Finding, Verbal Fluency)**

L1. "Having words 'on the tip of your tongue' — knowing what you want to say but not finding the word"
L2. "Substituting wrong words when speaking (e.g., saying 'chair' when you meant 'table')"
L3. "Finding it harder to follow a long or complex conversation"
L4. "Reading the same sentence multiple times to understand it"
L5. "Feeling that your vocabulary or ability to express yourself has decreased"

Language Score = Average of L1-L5 ratings

**DOMAIN 5: VISUOSPATIAL PROCESSING**

V1. "Getting confused in familiar environments or taking wrong turns in places you know well"
V2. "Having difficulty judging distances or depth (e.g., misjudging where a step is)"
V3. "Finding it harder to recognize faces of people you know in photographs"
V4. "Struggling to read maps, follow directions, or navigate to new places"
V5. "Noticing changes in your ability to park a car, reverse, or judge spacing"

Visuospatial Score = Average of V1-V5 ratings

### Phase 3: Integrate Formal Test Scores (If Available)

#### MMSE Score Integration
| MMSE Score | Classification | Training Implication |
|-----------|---------------|---------------------|
| 28-30 | Normal | Proceed with standard intensity program |
| 24-27 | Low-Normal | Proceed with enriched program; monitor closely |
| 20-23 | Mild Impairment | CONDITIONAL — proceed with low intensity; physician awareness required; re-assessment at 6 weeks |
| < 20 | Moderate/Severe Impairment | REFER — trigger physician referral; no training program |

#### MoCA Score Integration
| MoCA Score | Classification | Training Implication |
|-----------|---------------|---------------------|
| 26-30 | Normal | Proceed with standard intensity program |
| 22-25 | Mild Cognitive Impairment Range | CONDITIONAL — proceed with moderate intensity; physician awareness |
| 18-21 | MCI / Early Decline | CONDITIONAL — low intensity; physician supervision strongly recommended |
| < 18 | Probable Dementia | REFER — trigger physician referral; no training program |

**If MoCA < 18 or MMSE < 20:** Immediately issue REFER escalation. Do not generate training program. Output caregiver guidance and physician referral resources (same as sub-safety-screener REFER mode).

#### MoCA Sub-Domain Mapping
If MoCA sub-scores are available, map them:
| MoCA Sub-Score | Maps To | Flag if Low |
|---------------|---------|------------|
| Short-term memory (0-5) | Memory domain | < 3 = Significant Concern |
| Visuospatial/executive (0-5) | Visuospatial + Executive | < 3 = Significant Concern |
| Language (0-3) | Language domain | < 2 = Significant Concern |
| Attention (0-6) | Attention domain | < 4 = Significant Concern |
| Abstraction (0-2) | Executive function | < 1 = Significant Concern |
| Orientation (0-6) | Memory + Attention | < 5 = Significant Concern |

### Phase 4: Synthesize Domain Ratings

Convert questionnaire scores to domain ratings:

| Average Score | Rating | Color Code |
|-------------|--------|-----------|
| 4.0 - 5.0 | Robust | Green |
| 3.0 - 3.9 | Mild Concern | Yellow |
| 2.0 - 2.9 | Significant Concern | Orange |
| 1.0 - 1.9 | Marked Concern | Red — consider CONDITIONAL or REFER |

**Cross-reference rule:** If self-assessment rating conflicts significantly with formal MoCA/MMSE score (e.g., self-rates Robust but MoCA = 22), defer to the formal score and note the discrepancy (some individuals have poor insight into cognitive changes — anosognosia).

### Phase 5: Produce Domain Radar & Priority Ranking

**Domain Radar:**
```
COGNITIVE DOMAIN PROFILE
========================
Domain              | Self-Assessment | MoCA Sub | Composite Rating | Priority Rank
--------------------|----------------|----------|-----------------|---------------
Memory              | [score]/5      | [sub]    | [rating]        | [1-5]
Attention           | [score]/5      | [sub]    | [rating]        | [1-5]
Executive Function  | [score]/5      | [sub]    | [rating]        | [1-5]
Language            | [score]/5      | [sub]    | [rating]        | [1-5]
Visuospatial        | [score]/5      | [sub]    | [rating]        | [1-5]
```

Priority Rank 1 = Most impaired / most needs training attention
Priority Rank 5 = Strongest / least urgent

**Narrative interpretation:** Provide 2-3 paragraphs interpreting the profile, explaining:
- Which domains show the most concern and why this matters for daily life
- Which domains are intact and should be maintained (not neglected)
- How the profile relates to the user's self-reported cognitive concerns
- Which dementia risk pathways are most active based on the profile (e.g., hippocampal/memory pathway vs. executive/prefrontal pathway)

**Evidence reference for domain interpretation:**
- Memory: Hippocampal vulnerability to amyloid pathology (Jack et al., 2010, Lancet Neurology — amyloid cascade)
- Language: Temporal lobe semantic networks affected in posterior cortical atrophy and AD
- Executive: Frontal lobe vulnerable to vascular contributions (VCID)
- Attention: Cholinergic system loss (basal forebrain) drives attention deficits in early AD
- Visuospatial: Parietal lobe involvement; also primary symptom in posterior cortical atrophy (PCA) variant

---

## Outputs

- 5-domain cognitive radar table with composite ratings
- Training priority ranking (Priority 1-5 per domain)
- MMSE/MoCA integration note (if scores provided)
- Severity classification: Normal / Mild Concern / Significant Concern / REFER
- Narrative domain interpretation (2-3 paragraphs)
- Escalation flag if MoCA < 18 or MMSE < 20 (triggers REFER)

---

## Quality Gate

- [ ] All 5 cognitive domains have been assessed with at least 4 questions each
- [ ] Domain ratings (Robust / Mild Concern / Significant Concern) have been assigned for all 5 domains
- [ ] If MMSE/MoCA score available: it has been integrated and any conflict with self-assessment noted
- [ ] If MoCA < 18 or MMSE < 20: REFER escalation has been triggered; no training program generated
- [ ] Priority ranking has been produced (1-5 for all domains)
- [ ] Narrative interpretation includes at least one evidence reference per domain
- [ ] Output is structured and ready to pass to `sub-training-designer`
