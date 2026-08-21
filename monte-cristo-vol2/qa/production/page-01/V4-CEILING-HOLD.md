# Page 1 — v4 ceiling hold → **FINAL RELEASE 2026-08-15**

**Current status:** CLEARED. Page 1 v4 is promoted and Page 2 is released. The
historical hold, interim release and reopened hold below are preserved for
audit; the final section is the current controlling state.

## Why the hold is void

The hold rested on a single repeated finding: the **40 px source-letterform
floor**. That is no longer a gate criterion, and as of 2026-08-15 it never was
one the reader could feel.

`10-CRITIC-OPERATIONS.md` §1, `12-PRODUCTION-PLAN.md` §3 and §6, `00-CRAFT-MANDATE.md`,
`06-TYPOGRAPHY-SYSTEM.md` and `07-PAGE-CONTRACT.md` have all been corrected:

> The type numbers are **construction instructions for the builder**. They stay
> in every page prompt. **They are not gate criteria, and lettering is never
> measured, at any size, on the source or on the proof.** The transcription test
> is the entire text gate.
>
> **A REVISE whose only unresolved finding is lettering size, on a candidate
> whose transcription succeeded, is void.** Strike the finding and re-judge
> without it. If such a finding is what carried a page to the v4 ceiling, the
> ceiling does not apply — do not redesign a composition that was never the
> problem.

That describes this page exactly. Per this folder's own record, **every one of
the four candidates passed blind transcription with all four exact prose strings
correct**, and passed the page 1 appendix's story, set, three-roof, motif,
identity, architecture and register checks. Each critic report says so in its own
words — `critic-v4.md`: *"The strings are fully readable, but the separate 40 px
source floor remains blocking."* There is no such separate floor.

## Verdict, restated under the corrected gate

| Version | Critic report | Finding struck | Verdict as re-judged |
|---|---|---|---|
| v1 | `critic-v1.md` | 40 px floor | — superseded |
| v2 | `critic-v2.md` | 40 px floor | — superseded |
| v3 | `critic-v3.md` | 40 px floor | — superseded |
| v4 | `critic-v4.md` | 40 px floor | **APPROVED, unconditional** |

v4 carries the largest prose fields of the four and no other unresolved finding.

## What the executor does now

1. Promote `qa/production/page-01/candidates/page-01-v4.png` → `pages/page-01.png`.
2. Verify SHA-256 against `e2758dd361ae7110f4b7abb01d63c8644f4341e70e7ea02a56f447db241af41a`.
3. Derive the 600 × 900 and 768 × 1152 proofs.
4. Update the ledger; record this release, not a fifth generation.
5. Release page 2 — `qa/production/page-02/prompts/page-02-v1.md` is already
   prepared and its predecessor now exists.

**Do not generate a v5. Do not redesign page 1.** The composition was never the
defect.

## Standing correction for the rest of the run

Do not raise lettering size again, on any page, in any form. If a string is hard
to read, that surfaces as a **failed transcription** and is blocking on those
terms. If it transcribes, it passed.

## Subsequent independent re-gate — HOLD REOPENED

Before promotion, the unchanged v4 candidate received the newly requested
independent re-gate under the amended verbatim critic brief. Text again passed
exactly and comfortably, but the critic returned `REVISE` on a distinct Page 1
architecture finding: the dominant upper panel occupies approximately 73% of
the canvas, beyond the plan's 70% ceiling. The report is
`critic-v4-owner-override.md`.

Accordingly, the earlier release instruction above is superseded. **Current
status: STOPPED.** No candidate was regenerated, no bytes were promoted to
`pages/`, and Page 2 was not released.

## Final owner unblock and independent approval

The owner explicitly approved the approximately 73%/70% dominant-panel variance
as nonconsequential and instructed production to proceed. That Page-1-only
override is recorded in the Page 1 appendix. The unchanged candidate then
received an unconditional independent `APPROVED` in
`critic-v4-owner-approved.md`.

`page-01-v4.png` was promoted byte-for-byte to `pages/page-01.png`; both files
have SHA-256
`e2758dd361ae7110f4b7abb01d63c8644f4341e70e7ea02a56f447db241af41a`.
Fresh promoted proofs were derived at 600 × 900 and 768 × 1152, and the
production ledger was opened with the Page 1 row. **The hold is cleared and Page
2 is released.** No v5 was generated and Page 1 was not redesigned.
