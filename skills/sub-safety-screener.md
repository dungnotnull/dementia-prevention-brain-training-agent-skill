---
name: dementia-prevention-brain-training/sub-safety-screener
description: Mandatory safety gate for the dementia-prevention-brain-training skill — screens for medical contraindications, flags high-risk medications, and issues a mandatory medical disclaimer before any cognitive training guidance is produced
---

## Purpose

This sub-skill is the non-bypassable first step in the `dementia-prevention-brain-training` harness. Its sole function is to:
1. Identify medical conditions and medications that contraindicate or complicate cognitive training
2. Determine the safety classification (CLEAR / CONDITIONAL / REFER)
3. Issue a mandatory medical disclaimer on every run
4. In REFER cases, switch to caregiver guidance mode and halt the training program workflow

**CRITICAL:** This sub-skill must run before ANY cognitive training guidance is produced. It cannot be skipped, abbreviated, or run after Step 2.

---

## Inputs

- User's response to safety screening questions (collected via structured Q&A below)
- Any diagnoses already mentioned in the initial user query
- Any MMSE/MoCA scores already mentioned

---

## Workflow

### Phase 1: Issue Preamble & Collect Safety Information

Present the following statement before asking questions:

> "Before we design your personalized brain training program, I need to ask you some important health and safety questions. This is a required step that I follow for every person I work with — it helps me make sure the program I design is safe and appropriate for your specific situation. Please answer as honestly and completely as you can. If you are unsure about any medical detail, it is always best to check with your doctor.
>
> **Important:** This tool provides educational wellness guidance only. It does not replace consultation with a licensed neurologist, geriatrician, or neuropsychologist."

Then ask the following structured questions (may be asked all at once or one by one depending on context):

**Q1 — Existing Cognitive/Neurological Diagnosis:**
"Have you (or the person you are designing this program for) been formally diagnosed by a doctor with any of the following? (Select all that apply, or say 'None')
- Alzheimer's disease
- Vascular dementia, Lewy body dementia, or any other type of dementia
- Mild Cognitive Impairment (MCI) — diagnosed by a doctor
- Parkinson's disease with cognitive symptoms
- Recent stroke or transient ischemic attack (TIA / 'mini-stroke') — if yes, when was it?
- Traumatic brain injury — if yes, how recent?
- Epilepsy or seizure disorder (currently active or uncontrolled)
- Severe clinical depression or psychosis currently being treated or untreated"

**Q2 — Recent Neurological Events:**
"In the past 12 months, have you experienced any of the following? (Select all that apply, or say 'None')
- Sudden loss of speech, vision, or motor function (even briefly)
- Unexplained seizures or blackouts
- A sudden, severe headache unlike any previous headache
- Recent neurosurgery or brain radiation therapy"

**Q3 — Current Medications:**
"Are you currently taking any of the following types of medication? (A healthcare provider or pharmacist can help you identify if you are unsure)
- Sleeping pills, sedatives, or anti-anxiety medications (e.g., Valium, Xanax, Ativan, Ambien)
- Strong pain medications (opioids such as morphine, oxycodone, fentanyl)
- Bladder or allergy medications (e.g., Benadryl/diphenhydramine, Unisom, oxybutynin/Ditropan)
- Antidepressants that a doctor has noted may cause memory side effects
- More than 5 different prescription medications daily"

**Q4 — Functional Independence:**
"On a normal day, are you (or the person this program is for) able to:
- Manage your own finances and bills?
- Drive or use public transport independently?
- Take medications without reminders?
- Answer 'yes' to at least 2 of 3?"

### Phase 2: Classify Safety Status

Apply the following decision logic:

**REFER — Mandatory Physician Referral (No Training Program Generated):**
Trigger REFER if ANY of the following is true:
- Q1: Formal dementia diagnosis of any type (Alzheimer's, vascular, Lewy body, etc.)
- Q1: Stroke or TIA within the last 6 months
- Q1: Active, uncontrolled seizure disorder
- Q1: Severe psychiatric illness (psychosis, severe depression with safety concerns)
- Q2: Recent neurosurgery or brain radiation therapy within 12 months
- Q2: Unexplained seizures in the past 12 months
- Cognitive assessment later in the session reveals MoCA < 18 or MMSE < 20 (must flag REFER at that point)
- Q4: Unable to function independently in 2+ of 3 basic ADL categories

**CONDITIONAL — Proceed with Physician Awareness Flags:**
Trigger CONDITIONAL if ANY of the following is true (and REFER conditions are NOT met):
- Q1: MCI diagnosis (proceed, but note — program should be supervised and shared with physician)
- Q1: Parkinson's disease (proceed with low-intensity program; avoid balance-stressing dual-task exercises)
- Q1: Stroke or TIA MORE THAN 6 months ago (proceed, with aerobic exercise modified per cardiac tolerance)
- Q3: High-dose benzodiazepines or opioids (note reduced cognitive training benefit; recommend medication review with physician)
- Q3: Multiple anticholinergic medications (flag Anticholinergic Cognitive Burden; recommend physician review)
- Q3: 5+ medications daily (polypharmacy flag — recommend physician medication reconciliation)
- Any combination of 3+ significant health conditions

**CLEAR — Proceed Normally:**
All safety questions answered with no REFER or CONDITIONAL triggers.

### Phase 3: Issue Output

#### If REFER:
```
=== SAFETY ASSESSMENT RESULT: PHYSICIAN REFERRAL REQUIRED ===

Based on your responses, I have identified one or more health conditions that require 
you to speak with a licensed physician (neurologist or geriatrician) BEFORE beginning 
any structured cognitive training program.

SPECIFIC REASON(S) FOR REFERRAL:
[List which conditions triggered REFER]

THIS DOES NOT MEAN YOU CANNOT BENEFIT FROM BRAIN TRAINING.
It means that the specific type, intensity, and starting point of your program needs 
to be determined in collaboration with a qualified healthcare provider who can review 
your full medical history.

RECOMMENDED NEXT STEPS:
1. Schedule an appointment with your neurologist or geriatrician
2. Request a formal cognitive assessment (MoCA or neuropsychological evaluation)
3. Bring this AI-generated program design request to share your goals with your doctor
4. Once cleared by your doctor, return to this skill for a personalized program design

FOR CAREGIVERS:
If you are designing this program for a family member, please do not start cognitive 
training without your loved one's doctor's guidance. Caregiver resources:
- Alzheimer's Association 24/7 Helpline: 1-800-272-3900
- alz.org/help-support/caregiving
- WHO Dementia Action Plan: who.int/news/item/02-09-2017-worlds-first-global-dementia-action-plan

[MANDATORY MEDICAL DISCLAIMER — see below]
```

#### If CONDITIONAL or CLEAR:

```
=== SAFETY ASSESSMENT RESULT: [CLEAR / CONDITIONAL] ===

[If CONDITIONAL, list all flags with their implications:]
CONDITIONAL FLAGS:
- [Flag 1]: [Specific implication and modification for training]
- [Flag 2]: [Specific implication and modification for training]

PROCEED WITH: [List any modifications to the training program these flags require]

[MANDATORY MEDICAL DISCLAIMER — see below]
```

### Phase 4: Issue Mandatory Medical Disclaimer (Always — Every Run)

Emit the following disclaimer verbatim on every run, regardless of classification:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MEDICAL DISCLAIMER — PLEASE READ CAREFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The brain training program and information provided by this skill are for 
EDUCATIONAL AND WELLNESS PURPOSES ONLY. This content:

• IS NOT a medical diagnosis, clinical assessment, or medical treatment
• DOES NOT replace consultation with, or treatment by, a licensed neurologist,
  geriatrician, neuropsychologist, or other qualified healthcare professional
• SHOULD NOT be used as the sole basis for any health decision
• CANNOT definitively prevent, treat, or cure Alzheimer's disease or dementia

The exercises and recommendations in this program are based on published peer-reviewed 
research in cognitive neuroscience and dementia prevention. However:
- Individual responses to cognitive training vary significantly
- What works for one person may not work for another
- Some conditions require medical supervision before starting any new cognitive training

IF YOU EXPERIENCE ANY OF THE FOLLOWING, STOP ALL EXERCISES AND 
CONSULT A PHYSICIAN IMMEDIATELY:
- Sudden confusion, disorientation, or significantly worsened memory
- New headaches, vision changes, or speech difficulties
- Dizziness, fainting, or falls during or after exercise sessions
- Significant emotional distress or anxiety triggered by exercises
- Any new neurological symptom not previously present

This skill is a supportive educational tool. Your health team is your 
primary partner in dementia prevention.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Outputs

- **Safety Classification:** CLEAR / CONDITIONAL / REFER
- **Flag List:** Specific conditions/medications flagged with implications for training
- **Mandatory Medical Disclaimer:** Full text (always emitted)
- **Referral Resources:** (REFER cases only) — physician contact guidance, caregiver resources
- **Conditional Modifications:** (CONDITIONAL cases) — specific training modifications required

---

## Quality Gate

- [ ] All 4 safety question blocks have been asked and answered
- [ ] Safety classification (CLEAR / CONDITIONAL / REFER) has been determined and stated
- [ ] If REFER: no training program content has been generated; caregiver guidance and referral resources provided
- [ ] Medical disclaimer has been emitted (verbatim, full text)
- [ ] If CONDITIONAL: all flag-specific modifications are documented and will be applied downstream
- [ ] Output is passed to main harness before any other sub-skill runs
