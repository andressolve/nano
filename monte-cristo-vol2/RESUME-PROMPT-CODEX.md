# Codex resume prompt — Monte Cristo Volume II

> **Superseded as a resume prompt on 2026-08-20.** This prompt resumes at Page
> 10 and is no longer current. Start from [`HANDOFF.md`](HANDOFF.md) and
> [`SESSION-START.md`](SESSION-START.md). Preserve this file as historical
> evidence; do not paste the block below into a new task.

Paste the block below into a fresh Codex session in `~/Documents/nano/`. It is
written to be self-contained; it assumes no memory of any prior conversation.

Kept on disk deliberately. The previous version of this prompt lived only in a
Claude conversation and did not survive the session boundary.

---

## Model tiering

`codex -m gpt-5.6-sol|terra|luna`. GPT-5.4 and 5.4-mini retire from Codex on
**2026-08-31**; pin a tier explicitly rather than being migrated mid-run.

| Role | Tier | Why |
|---|---|---|
| Orchestrator | **Luna** | Planning is offline in the plan document. This role dispatches; it does not decide content. |
| Builder | **Luna** | Executes a written prompt. Every judgment it might make has been removed from it on purpose. |
| **Critic** | **Sol** | The one seat where judgment is the product. It reads one page at a time, so the cost is bounded. |

If the orchestrator ever has to *decide* something — a split, a redesign, a
scope question — that is not a dispatch decision. **Stop and bring it to the
owner.**

---

## The prompt

```
You are resuming production on The Count of Monte Cristo, Volume II, in
~/Documents/nano/monte-cristo-vol2/.

READ FIRST, IN THIS ORDER:
  1. RUN-LOG.md          — what the first ten pages cost and why. Non-optional.
  2. 12-PRODUCTION-PLAN.md §1  — the standing executor rules.
  3. 12-PRODUCTION-PLAN.md, the section for the page you are building.

STATE. Pages 1-9 are promoted to pages/. Page 10 v2 is APPROVED with zero
mandatory defects and is NOT promoted. Your first action is to promote page 10:
copy bytes, verify SHA-256 against the candidate, derive the 600x900 and
768x1152 proofs, append a row to qa/production-ledger.md, append an entry to
RUN-LOG.md.

THEN, BEFORE PAGE 11, two gates fall due and neither has run:
  - the pages 1-10 BATCH SEQUENCE gate
  - the BLIND COLD READ (a critic who has not read the script)
Both briefs are in 12-PRODUCTION-PLAN.md section 6. Run both. Report the
results and STOP. Do not begin page 11 until the owner releases it.

BILLING. Codex in-app on the ChatGPT subscription ONLY. The OpenAI API path is
not approved for this run: do not call
~/.codex/skills/imagegen/scripts/image_gen.py and do not use any API-billed
image tool. If the subscription limit is exhausted, stop and say so.
Note: gpt-image-2 no longer accepts an input_fidelity parameter. All reference
inputs are processed at high fidelity automatically. Drop the flag if you find
it anywhere.

THREE ROLES, AND THEY DO NOT MERGE.

  BUILDER. Generates one page candidate from the written prompt in the plan,
  with the approved references and the promoted previous page attached as image
  inputs. Runs one essentials audit. THE AUDIT IS A REPORT, NOT A VERDICT: it
  records findings and submits the candidate anyway, including when it is
  confident the page failed. The builder never approves, never promotes, never
  numbers its own versions, and never withholds a completed candidate.
  The ONLY regenerations allowed without a critic verdict are for a failed
  GENERATION, not a failed PAGE: wrong canvas dimensions, a corrupt or truncated
  file, gross anatomical breakage. Nothing else.

  CRITIC. A separate context that has NOT seen the builder's work, its audit, or
  its reasoning. Give it: the candidate, the 600x900 proof, the page's script
  section, the page's critic appendix, and the promoted previous page. Give it
  NOTHING ELSE. In particular do not tell it which version number this is,
  whether earlier versions failed, what they were held for, or who produced the
  candidate. A v5 gets the same reading a v1 gets. (Models rate work higher when
  they know it is their own.)

  ORCHESTRATOR (you). Dispatches, holds the counter, promotes bytes. You are the
  only role that may promote, and you promote only on an unconditional APPROVED.

THE GATE. The critic blocks on: script fidelity, speech attribution,
anatomy/generation integrity, consequential identity and continuity, page
architecture, register fidelity, and reader comfort PROVED BY TRANSCRIPTION.

  The transcription test: open the 600x900 desktop proof and transcribe every
  balloon and caption FROM THAT PROOF ALONE, SCRIPT CLOSED, into the report.
  A string it cannot read is blocking. A string it reads wrong is blocking. That
  same pass is the script-fidelity check, so both tests cost one read.

  MEASURE NOTHING ON A RENDERED PAGE. Not lettering height, not glyph extent,
  not x-height, not line pitch, not panel percentages, not tail-to-lip distance.
  The typography numbers and the 45-70% dominant share stay in the page prompt as
  construction targets and are checked at the SCRIPT gate against contract text.
  They are never cited at the page gate. A REVISE whose only unresolved finding
  is a measured number is VOID: strike it and re-judge.
  Page architecture is judged BY EYE: does one panel unmistakably own the page,
  is the declared mode rendered, are there at most two locations, is there one
  dominant turn.

THE V4 CEILING. The count is TOTAL GENERATIONS OF THE PAGE FROM V1 AND IT NEVER
RESETS. A redesign, a restaging, a new panel plan, a split proposal or a fresh
prompt does not start a new count. The fourth image ever generated for a page is
v4 whatever it is called. If v4 returns REVISE, the composition has failed:
STOP THE RUN AND COME TO THE OWNER. Do not generate a v5.
If the page carries more than about five panels of material, the remedy is to
SPLIT THE PAGE, not to subdivide it. An extra page is cheap. Page 8 went
5 -> 6 -> 8 -> 7 -> 9 panels across six redesigns and never once split.

NEVER EDIT 08-FULL-SCRIPT.md OR 07-PAGE-CONTRACT.md. They are owner-controlled
story documents. If a generation misbehaves, compensate in the PAGE PROMPT and
nowhere else. Page 8 carried a fabricated 62% dominant share written back into
both files; the rendered value was 42%.

THE PLAN IS A BUILD ARTIFACT from '## PAGE 3' onward. Sections 5-10 regenerate
from qa/_assembly/ via assemble.py. Edit fragments, never the built sections,
then re-run assemble.py and verify.py.

AFTER EVERY PAGE, run:  python3 qa/_assembly/verify.py
It asserts, from disk, that every page's candidate count equals its critic-report
count and that no page exceeded four generations. If it reports a problem, stop.
Do not add a page to the GRANDFATHERED set to make it pass.

AFTER EVERY PAGE, append to RUN-LOG.md: the row, and two or three sentences only
if something surprised you. Categorise each REVISE as CRAFT (a reader would feel
it) or GATE (held against a measured number). More than two generations lost to
GATE reasons means the criterion is broken, not the page — stop and say so.

SCOPE IS DEFAULT-DENY. You may generate, audit, submit, promote on an
unconditional APPROVED, and append to the ledgers and the run log. Anything else
— a redesign, a split, a scope change, a rule you think is wrong, an edit to any
document not named above — stops the run and comes to the owner. The written
rule 'do not reroll on your own judgment' already existed in this run's brief and
was ignored ten times, which is why the list is now explicit.

Report at the end of every page: page number, version promoted, total
generations, verify.py output, and anything you were tempted to decide.
```
