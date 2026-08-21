# Monte Cristo Volume II — intent-first builder/critic rules

**Recorded:** 2026-08-21  
**Status:** owner-approved design decisions for the Page 33–49 production
rewrite. No image generation is authorized by this file.

This file records the lessons from the Page 32 intent pilot. It does not alter
the owner-controlled page contract or script.

## 1. Every remaining generation prompt is rewritten

Pages 33–49 do not merely receive new critic instructions. Each page receives:

1. a concise reader-facing page intent;
2. a moderately simplified, page-specific generation prompt for the builder;
3. a short, independent critic card containing only reader-facing blocking
   criteria.

The revised generation prompt must preserve exact script strings, essential
staging, attribution, named-character identity, consequential continuity, and
the approved reference manifest. It must remove or demote microscopic proof
demands, decorative precision, exact coordinates, numeric geometry, tiny-prop
legibility, and other details that do not carry the page's meaning.

The generation prompt remains builder-only. The critic never sees or grades it.

## 2. A true defect is not automatically a blocking defect

The Page 32 seal and repeated crowd faces demonstrate the distinction:

- The seal criticism was technically accurate, but the seal did not carry Page
  32's reader event.
- The repeated anonymous crowd faces were visible, but the collective turn,
  occupied chamber, Haydée reveal, Fernand's diminishment, and silent spectacle
  all landed clearly.

In both cases, the observation could be true while `REVISE` was still the wrong
production decision.

The critic is not a defect collector. It is a reader-facing release gate. A
finding blocks only when the visible problem materially harms at least one of:

- what happens on the page or why the reader turns;
- exact text and comfortable transcription;
- clear speech ownership and reading order;
- recognition or separation of named/focal characters;
- a consequential object or continuity state needed to understand the story;
- focal anatomy or generation integrity;
- the page's dominant emotional or narrative relationship.

Technical correctness alone is insufficient. The critic must state the
material reader harm.

## 3. Full-page redraw cost changes the threshold

Every correction requires regenerating the complete page and risks destroying
already successful story, text, identity, and composition. Therefore a critic
must not demand a redraw for a minor issue merely because the issue is real.

Return `APPROVED` when the defect is background, cosmetic, tiny, or visible only
under inspection and the page's reader event remains intact. This includes:

- repeated or similar anonymous background crowd faces;
- minor background anatomy or texture artifacts;
- a tiny prop that is indistinct when the reader does not need to identify it;
- exact hue, scale, coordinate, percentage, or decorative differences;
- prompt variance without material reader harm.

Background repetition becomes blocking only when it duplicates a named or focal
character, creates a grotesque attention-dominating pattern, changes who is in
the scene, or otherwise materially breaks the reader event.

The critic does not calculate money or generation difficulty. It simply applies
the correct production threshold: **do not risk an otherwise successful full
page to repair a nonconsequential flaw.**

## 4. Mandatory critic test

The critic first performs a blind read from the 600 × 900 proof and states:

1. what happened;
2. who owns the page dramatically;
3. what changed or motivates the turn;
4. the exact visible text and attribution.

Only then does it open the exact script, page intent, and numbered critic card.
It never opens the generation prompt or builder audit.

Every `REVISE` finding must cite one numbered criterion and include:

- the visible observation;
- the material reader harm;
- why the harm is substantial enough to justify risking a full-page redraw.

If the last explanation cannot be made concretely, the verdict is `APPROVED`.
Reports contain mandatory findings only; minor observations are omitted rather
than converted into optional polish work.

## 5. Orchestrator rule

The orchestrator remains nonvisual. It checks the critic's report contract
mechanically. A `REVISE` without a numbered card criterion, material reader harm,
and redraw justification is an invalid critic report—not an instruction to
generate again.

Valid `REVISE` proceeds to a fresh builder for the named defect only, preserving
all successful essentials. Valid `APPROVED` promotes byte-for-byte. A v4
`REVISE` remains an owner hold.

## 6. Resistant-defect routing

The numbered critic-card criteria are stable defect signatures. The
orchestrator compares criterion numbers between validated critic reports; it
does not interpret the artwork or decide whether two visual observations look
similar.

The retry sequence is:

1. `v1 REVISE` → `v2` receives a targeted prompt correction for the cited
   criteria, while preserving the reader-facing successes named in the report.
2. If `v2` repeats any criterion cited on `v1`, `v3` is a **clean-slate rewrite
   of the complete generation prompt and composition strategy**. The fresh
   builder starts from the page intent, exact strings, approved references, and
   compact validated findings. It does not open or patch the earlier issued
   prompts or rejected candidates.
3. If the same repeated criterion survives that clean rewrite on `v3`, stop
   before `v4` and bring the page to the owner as a resistant-defect hold.
4. If `v2` contains only new criteria, `v3` may be a targeted correction. If a
   criterion then repeats from `v2` to `v3`, `v4` is the clean-slate rewrite.
5. If a clean rewrite resolves the repeated criterion but introduces a new
   material criterion, the next available version may target the new finding.
   Any `v4 REVISE` still triggers the existing owner hold.

A full rewrite may rethink framing, staging, visual hierarchy, and panel
composition within the locked page. It may not alter the page intent, exact
script strings, approved reference manifest, story facts, critic card, page
count, or owner-controlled documents. It is a reset, not a longer accumulation
of corrective clauses.

The orchestrator records the next route as exactly one of:
`PROMOTE`, `TARGETED`, `FULL_PROMPT_RESET`, `RESISTANT_DEFECT_HOLD`,
`V4_OWNER_HOLD`, or `INVALID_CRITIC_REPORT`. There is no automatic redesign,
split, component generation, or extra attempt outside those routes.

## 7. Page 32 evidence

The original pilot prompt, critic card, critic report, candidate, and proof files
remain unchanged as historical evidence. The owner's promotion record explains
the accepted Page 32 variance. This document is the post-pilot correction that
governs the remaining-page rewrite.

## 8. Implementation record

Completed before Page 33 generation on 2026-08-21:

1. every Page 33–49 generation prompt was individually rewritten under §1;
2. every page received a reader-facing intent and numbered critic card;
3. the shared builder, blind critic, report validator, retry router, and
   nonvisual orchestrator contracts enforce §§2–6;
4. compact builder/critic/card role packets rebuild mechanically and pass a
   clean deterministic preflight;
5. `SESSION-START.md` begins at Page 33, and a separate held entry point exists
   for the fresh Pages 41–49 task.

The assembly sources live in `qa/_assembly/intent-first-*.md`; emitted production
packets live in `qa/_run/`. No image was generated during implementation.
