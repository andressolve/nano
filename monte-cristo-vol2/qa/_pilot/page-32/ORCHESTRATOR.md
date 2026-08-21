# Page 32 intent-pilot — Luna orchestrator prompt

This is the complete entry point for the Page 32 pilot. When the owner starts a
new task with this file, run exactly one builder → critic pass and stop after the
validated verdict. Do not generate or inspect Pages 33–49.

## Scope and model allocation

- Orchestrator: GPT-5.6 Luna, medium.
- Builder: fresh GPT-5.6 Luna, low, no inherited task history.
- Critic: fresh GPT-5.6 Sol, medium, no inherited task history.

Keep the separate builder and critic sessions. Never reuse either agent. The
owner has authorized one new Page 32 production candidate specifically to test
this revised setup. There is no automatic second candidate.

## Orchestrator boundary

You own dispatch, paths, deterministic validation, and stopping. You do not
open the candidate or proofs, perform visual judgment, approve the art, promote
anything into `pages/`, or update the production ledger.

Open only:

- `qa/_pilot/page-32/ORCHESTRATOR.md`
- the tail of `HANDOFF.md` solely to confirm Page 31 remains canonical
- file metadata needed for path, dimension, and hash checks
- the completed critic report for structural validation

Do not open the old Page 32 prompt, appendix, candidates, component frames,
proofs, audits, reports, `12-PRODUCTION-PLAN.md`, `SESSION-START.md`, another
page packet, or another task transcript.

## One-pass sequence

1. Confirm the four builder image inputs exist and `pages/page-31.png` is still
   canonical. Confirm `qa/production/page-32/intent-pilot/` does not already
   contain output; never overwrite a prior pilot.
2. Spawn one fresh builder with only `qa/_pilot/page-32/BUILDER.md` and
   `qa/_pilot/page-32/INTENT.md`. It generates exactly one candidate and returns
   paths, dimensions, mode, and hashes.
3. Wait once for completion. Do not poll or read the builder's task history.
4. Deterministically verify the candidate is a readable 1024 × 1536 RGB PNG,
   both proofs exist with the declared dimensions, all five required output
   files exist, and the returned hashes match disk.
5. Copy only the candidate and two proofs behind these neutral names:
   `qa/_review/page-32-intent-pilot/current/candidate.png`,
   `desktop-600x900.png`, and `tablet-768x1152.png`. Do not expose the builder
   audit or issued prompt to the critic.
6. Spawn one fresh critic with only `qa/_pilot/page-32/CRITIC.md`. The critic
   performs its blind read, then opens `CRITIC-CARD.md` and `INTENT.md`, saves one
   report, and returns one verdict.
7. Run:
   `python3 qa/_pilot/page-32/validate-critic-report.py qa/production/page-32/intent-pilot/critic-report.md`
8. If validation fails, label the result `INVALID CRITIC REPORT` and stop. Do
   not treat it as `APPROVED`, do not regenerate, and do not silently repair the
   report. An out-of-card finding is a failed critic contract, not an art defect.
9. If validation passes, report the validated `APPROVED` or `REVISE` verdict and
   stop. Do not promote or regenerate. The owner reviews the pilot result before
   any further action.

## Update contract

Send only state changes: pilot preflight passed, candidate started, candidate
submitted, critic started, validated verdict, or invalid-report stop. No polling
updates and no discussion of Pages 33–49.
