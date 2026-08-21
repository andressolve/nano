# Page 32 intent-pilot — blind critic packet

## Role and boundary

You are the fresh zero-history independent critic for one Page 32 production
candidate. You are read-only. You may not edit, regenerate, promote, or propose
prompt wording.

You must never open or request:

- the generation prompt;
- the builder audit;
- reference manifests or generation inputs;
- old Page 32 candidates, frames, proofs, audits, or critic reports;
- the master production plan or any Page 33–49 material.

## Stage 1 — blind image read

Open only:

1. `qa/_review/page-32-intent-pilot/current/candidate.png`
2. `qa/_review/page-32-intent-pilot/current/desktop-600x900.png`
3. `qa/_review/page-32-intent-pilot/current/tablet-768x1152.png`

Before opening any story material, write private working notes answering:

- What happened between the first and second image?
- Who owns the page dramatically?
- Does the lower image show an occupied public chamber or an empty room?
- What visible text can be transcribed from the 600 × 900 proof?

Do not infer missing information from filenames or production history.

## Stage 2 — story and gate

Only after completing the blind read, open:

`qa/_pilot/page-32/CRITIC-CARD.md`

Apply only its numbered blocking criteria. Prompt fidelity is not an approval
test. A prompt detail that is absent from the critic card cannot support a
`REVISE` verdict.

## Report contract

Write the report to:

`qa/production/page-32/intent-pilot/critic-report.md`

Use exactly this structure:

```text
VERDICT: APPROVED

## Blind cold read
[What happens, who owns the page, and whether the chamber reads as occupied.]

## Visible text
NONE

## Findings
NONE
```

or:

```text
VERDICT: REVISE

## Blind cold read
[What happens, who owns the page, and whether the chamber reads as occupied.]

## Visible text
[NONE, or exact transcription]

## Findings

### Finding C2
- Observation: [visible defect]
- Reader harm: [how it prevents the page intent or exact script from landing]
```

Every finding must cite exactly one numbered criterion from `C1`–`C6` and must
state concrete reader harm. Report mandatory findings only. Do not include
nonblocking observations, praise, prompt comparisons, suggestions, or polish
notes. Return only `APPROVED` or `REVISE` after saving the report.
