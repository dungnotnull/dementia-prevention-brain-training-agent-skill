---
name: dementia-prevention-brain-training/sub-training-designer
description: Designs a personalized 12-week progressive brain training program grounded in FINGER/ACTIVE protocols, selecting evidence-based exercises across 5 cognitive domains with dual-task integration and aerobic exercise synchronization
---

## Purpose

This sub-skill is the core deliverable engine of the harness. Using the cognitive domain profile and priority ranking from `sub-cognitive-assessment` and the health/lifestyle profile from `sub-profile-intake`, it selects appropriate exercises for each domain and builds a structured 12-week training calendar that progressively increases in complexity and integration. All exercise recommendations are grounded in peer-reviewed evidence.

---

## Inputs

- Cognitive domain profile + priority ranking from `sub-cognitive-assessment`
- User health/lifestyle profile from `sub-profile-intake`
- Safety flags and conditional modifications from `sub-safety-screener`
- Available daily training time and best time of day
- Technology access level

---

## Workflow

### Phase 1: Exercise Library Selection

For each cognitive domain, select exercises based on priority rank (higher priority = more weekly sessions) and user constraints (time, technology access, health conditions).

---

#### DOMAIN 1: MEMORY EXERCISES

**1A. Method of Loci (Memory Palace)**
- **What:** Visualize a familiar route; associate memory items with vivid landmarks along the route
- **Protocol:** Daily 10-min sessions; start with 5-item lists; progress to 10-item (week 5) then 15-item (week 9)
- **Best for:** Episodic memory (name-face, appointment recall, shopping lists)
- **Evidence:** Dresler et al. (2017, Neuron) — 97% improvement in word-list recall at 72 hours; hippocampal-cortical connectivity changes confirmed by fMRI
- **Materials needed:** None — entirely mental

**1B. Spaced Retrieval Practice**
- **What:** Study a piece of information; test recall after 1 min → 5 min → 20 min → 1 hour → 1 day (expanding intervals)
- **Protocol:** 10-15 min/session; use flashcards (physical or digital); apply to names, facts, or daily information
- **Best for:** Episodic memory + semantic memory
- **Evidence:** Cermak et al. (1996, Neuropsychological Rehabilitation) — spaced retrieval outperforms massed practice for amnestic memory disorders; Baddeley & Wilson (1994) for errorless learning
- **Materials needed:** Flashcards or a spaced repetition app (Anki — free)

**1C. Story Method (Narrative Chaining)**
- **What:** Link items to be remembered into a vivid, absurd story (each item interacts dramatically with the next)
- **Protocol:** 10 min/session; start with 5-item chains; progress to 10-item (week 5-8) then 15-item (week 9-12)
- **Best for:** Sequential memory, word lists
- **Evidence:** Bower & Clark (1969, Psychonomic Science) — 93% recall vs. 13% rote memorization; narrative encoding activates hippocampal-parahippocampal complex

**1D. Working Memory N-Back Task**
- **What:** Hear or see a sequence; determine whether the current item matches the item N positions back
- **Protocol:** 
  - Weeks 1-4: 1-back (does this match the one right before it?) — 15 min, 3x/week
  - Weeks 5-8: 2-back — 15-20 min, 4x/week
  - Weeks 9-12: 3-back or dual n-back (visual + auditory simultaneously) — 20 min, 4x/week
- **Best for:** Working memory, sustained attention
- **Evidence:** Olesen et al. (2004, Brain) — N-back training modulates dorsolateral prefrontal cortex and parietal cortex; meta-analysis: Melby-Lervag (2016, Psychological Bulletin) — near-transfer effects confirmed
- **Apps:** Dual N-Back (free, Android/iOS), BrainWorkshop (free, PC)
- **Paper alternative:** Read a list aloud, pause, ask user to state what was 2 items ago

---

#### DOMAIN 2: ATTENTION EXERCISES

**2A. Sustained Attention — Mindful Reading**
- **What:** Read for a set period without distraction; after each page, summarize 3 key points from memory
- **Protocol:** 15 min/session; no phone or background TV; comprehension check after each session
- **Best for:** Sustained attention + episodic memory (dual benefit)
- **Evidence:** Oken et al. (2010, Psychological Science) — mindfulness-based attention training improves sustained attention in older adults

**2B. Selective Attention — Stroop Task**
- **What:** Color-word interference task — name the ink color, ignoring the written word (e.g., the word "RED" printed in blue ink; answer is "blue")
- **Protocol:** 10 min/session, 3x/week; timed; progress by adding speed goal (weeks 5-8: beat your best time) or switching to number-letter Stroop variants (weeks 9-12)
- **Best for:** Selective attention, inhibitory control
- **Evidence:** Bohbot et al. (2012, Neuropsychology) — Stroop training improves prefrontal inhibitory control; sensitive marker of early cognitive decline
- **Materials:** Free printable Stroop cards; online tools (Stroop Effect Test)

**2C. Divided Attention — Dual Auditory-Cognitive Task**
- **What:** Listen to an audiobook or podcast while sorting playing cards by color. Rate comprehension after. Progress to sorting by suit (harder)
- **Protocol:** 10 min/session, 2-3x/week; increase complexity progressively
- **Best for:** Divided attention (precursor to dual-task training)
- **Evidence:** Eggenberger et al. (2015, BMC Geriatrics) — divided attention training improves dual-task walking performance

**2D. Attention Tracking — Visual Search**
- **What:** Find specific items in a busy visual scene (e.g., "Where's Waldo" type; or find all instances of a target letter in a dense text)
- **Protocol:** 10 min/session, 2x/week; timed; increase density of distractors progressively
- **Best for:** Selective + spatial attention
- **Evidence:** Ball et al. (2002, JAMA) — speed-of-processing/attention training (ACTIVE study) improved IADLs at 5 years

---

#### DOMAIN 3: EXECUTIVE FUNCTION EXERCISES

**3A. Tower of Hanoi / Peg Puzzle**
- **What:** Move a stack of discs from one peg to another, one at a time, never placing a larger disc on a smaller one
- **Protocol:** 15 min/session, 2x/week; start with 3 discs (week 1-4); add 4-disc (week 5-8); 5-disc (week 9-12)
- **Best for:** Planning, working memory, inhibitory control
- **Evidence:** Unterrainer et al. (2004, Neuropsychologia) — Tower tasks activate prefrontal cortex planning circuits; sensitive to frontal lobe integrity
- **Materials:** Physical Tower of Hanoi (inexpensive toy) or free online app

**3B. Cognitive Flexibility — Task-Switching Drills**
- **What:** Alternate between two simple tasks on a signal — e.g., naming animals starting with A, then switching to naming fruits starting with B, back and forth every 30 seconds
- **Protocol:** 10-15 min/session, 3x/week; increase switching speed in weeks 5-8; add 3-way switching in weeks 9-12
- **Best for:** Cognitive flexibility, task-switching ability
- **Evidence:** Karbach & Kray (2009, Psychological Aging) — task-switching training improves executive functions and transfers to fluid intelligence in older adults

**3C. Planning Exercise — Weekly Scheduling**
- **What:** Plan a complex multi-step week (e.g., "Plan a 3-day trip to a new city with a budget") in writing, anticipating obstacles and alternatives
- **Protocol:** 20-30 min/session, 1x/week; evaluate against criteria (completeness, conflict-free scheduling, contingency planning)
- **Best for:** Planning, prospective memory, organization
- **Evidence:** Boosted by real-life cognitive engagement (Valenzuela & Sachdev, 2006 — complexity of daily life predicts cognitive reserve accumulation)

**3D. Working Memory Update — Mental Arithmetic Progressions**
- **What:** Count backward from 100 by 7s (Serial-7s); count backward from 200 by 13s; perform multi-step mental arithmetic
- **Protocol:** 5-10 min/session, 4x/week; introduce progressively harder sequences
- **Best for:** Working memory updating, inhibitory control
- **Evidence:** Serial-7s is a standard MMSE sub-item; training this task improves working memory update speed (Jaeggi et al., 2010)

---

#### DOMAIN 4: LANGUAGE EXERCISES

**4A. Verbal Fluency Drills**
- **What:** Name as many items as possible in a category within 60 seconds (semantic fluency: animals, tools, fruits) or starting with a letter (phonemic fluency: F-A-S test)
- **Protocol:** 5-10 min/session, 4x/week; track number of correct items; switch categories each session; progress from common to unusual categories (weeks 5-8: musical instruments; 9-12: items in a hardware store)
- **Best for:** Verbal fluency, semantic memory, word retrieval speed
- **Evidence:** Standard MoCA item; decline in verbal fluency is an early marker of semantic network degradation in AD (Henry et al., 2004, Neuropsychologia — meta-analysis)

**4B. Crossword Puzzles & Word Games**
- **What:** Standard crossword (Beginner → Intermediate); Wordle-type deduction games; vocabulary building through reading unfamiliar words in context
- **Protocol:** 20-30 min/session, 4x/week; aim for systematic difficulty increase
- **Best for:** Semantic memory, verbal reasoning, vocabulary maintenance
- **Evidence:** Pillai et al. (2011, Neuroepidemiology) — crossword puzzle participation delays onset of accelerated memory decline by ~2.5 years in a prospective cohort (N=488)

**4C. Learning New Vocabulary in Context**
- **What:** Learn 5 new words per session by reading them in sentences, creating an original sentence, and using them in conversation the same day
- **Protocol:** 15 min/session, 3x/week; vocabulary domain can rotate (cooking, history, science, art)
- **Best for:** Semantic network enrichment, language production
- **Evidence:** Cognitive enrichment through language acquisition (Bialystok et al., 2007, Neuropsychologia — bilingualism delays dementia onset by ~5 years)

**4D. Storytelling & Oral History**
- **What:** Recall and tell a personal story (childhood memory, career event, travel story) in full detail — with setting, characters, sequence, and emotional tone; record and listen back
- **Protocol:** 10-15 min/session, 2x/week; progress from recent events to distant memories (weeks 5-8); add fictional story improvisation (weeks 9-12)
- **Best for:** Episodic + semantic memory, language production, emotional processing
- **Evidence:** Reminiscence therapy shows benefits for autobiographical memory retrieval in older adults (Woods et al., 2018, Cochrane Review — 22 studies, N=1972)

---

#### DOMAIN 5: VISUOSPATIAL EXERCISES

**5A. Mental Map Drawing**
- **What:** Draw from memory: your neighborhood, your town center, a familiar building's floor plan. Compare with actual map after; identify errors; redraw
- **Protocol:** 15-20 min/session, 2x/week; progress from small spaces (one room) to larger environments (whole neighborhood)
- **Best for:** Hippocampal spatial navigation, place cell networks
- **Evidence:** Woollett & Maguire (2011, Current Biology) — spatial navigation learning causes gray matter increase in hippocampal gray matter

**5B. Jigsaw Puzzles**
- **What:** Complete jigsaw puzzles of increasing piece count and complexity
- **Protocol:** 20-30 min/session, 3x/week; start with 100-200 pieces; progress to 300-500 pieces (weeks 5-8); 750+ with complex imagery (weeks 9-12)
- **Best for:** Visuospatial processing, attention, pattern recognition
- **Evidence:** Friedman et al. (2014, Neuropsychology) — puzzle completion activates parietal-occipital visuospatial networks; associated with cognitive reserve maintenance

**5C. Mental Rotation Practice**
- **What:** Look at a 2D or 3D shape; determine how it would look rotated 90°/180°. Use worksheets or apps
- **Protocol:** 10-15 min/session, 2x/week; start with 2D shapes; progress to 3D objects (weeks 5-8); add time pressure (weeks 9-12)
- **Best for:** Parietal lobe visuospatial processing, mental manipulation
- **Evidence:** Shepard & Metzler (1971, Science) — foundational study on mental rotation; training effects demonstrated in multiple follow-up studies

---

### Phase 2: Build 12-Week Calendar

#### Week Theme Structure

**WEEKS 1-4: FOUNDATION PHASE**
- Goal: Establish training habits; build baseline in each domain; introduce techniques at low intensity
- Session duration: 15-20 min
- Daily structure: 1 session/day, 6 days/week (1 rest day)
- N-back: 1-back
- No dual-task sessions yet — single-domain focus
- Aerobic: 3x/week, 30 min moderate (50-60% max heart rate: 220 - age × 0.55)

**WEEKS 5-8: DEVELOPMENT PHASE**
- Goal: Increase difficulty; introduce multi-domain and dual-task sessions; build stamina
- Session duration: 20-25 min
- Daily structure: 1 session/day, 6 days/week
- N-back: 2-back; pass rate criterion (>= 80% accuracy before advancing)
- Introduce 3 dual-task sessions/week (cognitive exercise while walking at brisk pace)
- Aerobic: 3-4x/week, 40-45 min moderate-vigorous (60-70% max heart rate)

**WEEKS 9-12: MASTERY & INTEGRATION PHASE**
- Goal: Complex integration; challenge all domains simultaneously; build resilience
- Session duration: 25-30 min
- Daily structure: 1 session/day, 6 days/week
- N-back: 3-back or dual n-back
- 3+ dual-task sessions/week; introduce novel challenges (new routes, new games)
- Aerobic: 4x/week, 45-50 min; consider adding mind-body exercise (Tai Chi: dual cognitive-balance benefit)
- Social cognitive sessions: 2x/week (teach someone a skill, group discussion, quiz game)

#### Sample Weekly Schedule Template

```
WEEK [X] SCHEDULE — Theme: [Phase Theme]
===========================================

MON: PRIORITY DOMAIN 1 — [Exercise Name]
     Duration: [X] min | Domain: [Domain] | Evidence: [Citation]
     Instructions: [Brief how-to]

TUE: PRIORITY DOMAIN 2 — [Exercise Name] + AEROBIC
     Cognitive: [X] min | Aerobic: 30-45 min walk/cycle
     [Dual-task note if applicable: "Do N-back during the first 10 min of walk"]

WED: LANGUAGE + SOCIAL
     Verbal Fluency: 10 min
     Social engagement: 30-60 min (book club, video call with family, volunteer activity)

THU: PRIORITY DOMAIN 3 — [Exercise Name]
     Duration: [X] min | Domain: [Domain]

FRI: DUAL-TASK SESSION (Weeks 5-12 only)
     Physical: 30 min brisk walk
     Cognitive overlay: [Specific dual-task — e.g., count backward by 7s while walking; name a category item with each step]
     Evidence: Beurskens & Bock (2012, European Journal of Ageing)

SAT: VISUOSPATIAL + ATTENTION
     [Exercise combination session]

SUN: REST / LIGHT ACTIVITY
     Optional: 20 min relaxed reading; sleep hygiene review
```

### Phase 3: Apply Conditional Safety Modifications

Apply any modifications triggered by `sub-safety-screener` CONDITIONAL flags:
- **Parkinson's disease:** Remove all dual-task walking exercises; replace with seated dual-task (auditory + hand movement); reduce intensity of executive function tasks; avoid frustration-inducing tasks
- **Cardiovascular disease:** Limit aerobic intensity to 50-60% max HR (physician clearance required for higher); focus on low-impact aerobic (walking, swimming)
- **Significant hearing loss:** Replace all auditory-based exercises (auditory N-back) with visual equivalents (visual N-back); emphasize visuospatial and reading-based tasks
- **Anticholinergic medications:** Note reduced working memory training benefit; recommend physician medication review; increase social and language components
- **Polypharmacy (5+ meds):** Add medication management sessions as a real-life cognitive exercise

### Phase 4: Produce Training Calendar Output

Produce the full 12-week calendar as a structured table for each week, listing:
- Day, Session Type, Exercise Name, Duration, Cognitive Domain(s), Instructions Summary, Evidence Citation

---

## Outputs

- Complete 12-week training calendar (tabular format, week by week)
- Exercise instructions for each selected activity (concise, accessible)
- Aerobic exercise schedule synchronized with cognitive sessions
- Social engagement activities (at least 2x/week from Week 1)
- Evidence citations for all exercise types
- Conditional modification notes (if any CONDITIONAL flags applied)

---

## Quality Gate

- [ ] 12-week calendar covers all 3 phases (Foundation, Development, Mastery)
- [ ] At least 4 of 5 cognitive domains are addressed with specific exercises
- [ ] Priority Domain 1 receives at minimum 3 sessions/week in Weeks 1-4 and 4 sessions/week in Weeks 5-12
- [ ] N-back progression is present: 1-back (Weeks 1-4) → 2-back (5-8) → 3-back (9-12)
- [ ] Dual-task sessions begin in Week 5 and occur at least 3x/week from Week 5 onward
- [ ] Aerobic exercise is scheduled 3x/week minimum throughout
- [ ] Social engagement is included at minimum 2x/week
- [ ] Every exercise type cites at least one peer-reviewed study (Tier 4 or higher evidence)
- [ ] All conditional safety modifications are applied
- [ ] Calendar is formatted clearly for non-clinical user comprehension
