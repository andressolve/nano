# Monte Cristo Volume II — start Pages 41–49

> **SUPERSEDED:** Pages 41–49 are complete. Do not execute this production
> entry point again. Read `HANDOFF.md` for current state.

This file is the entry point for a **new** production task after the Pages
31–40 milestone gates have passed. It is not executable before then.

Run the task with the directory containing this file as the workspace and
current working directory. All paths below are relative to that directory.

## Start

1. Read `HANDOFF.md` and confirm it records Page 40 plus approved Pages 31–40
   sequence, Pages 1–40 cold-read, and Pages 31–40 continuity gates.
2. Read `14-INTENT-FIRST-BUILDER-CRITIC-RULES.md`.
3. Read `qa/_intent-first/ORCHESTRATOR.md`.
4. Run `python3 qa/_assembly/assemble.py` and
   `python3 qa/_assembly/verify.py`. Both must finish cleanly.
5. Confirm canonical Page 40 matches the SHA-256 prefix recorded in
   `qa/production-ledger.md`.
6. Produce Pages **41–49 sequentially**, beginning with the first unpromoted
   page in that bounded range and deriving state from disk.

Do not open the previous production task, `12-PRODUCTION-PLAN.md`,
`qa/_plan/page-NN.md`, candidate images, proofs, or historical Page 32
materials. Use only the compact `qa/_run/` packets and deterministic receipts.

## Models and context

- Orchestrator: GPT-5.6 Luna, medium.
- Builder: fresh GPT-5.6 Luna, low, no inherited task history, one candidate.
- Page critic: fresh GPT-5.6 Sol, medium, no inherited task history, one review.
- Final reviewers: fresh GPT-5.6 Sol, medium, no inherited task history.

Every image-bearing or image-reviewing role is discarded after that one job.
All image generation is subscription-backed Codex in-app. No API key, bundled
image CLI, or API fallback.

## Final gates after Page 49

After Page 49 is promoted, run four independent fresh reviews:

1. canonical Pages 41–49 from `qa/_intent-first/GATE-41-49-SEQUENCE.md`;
2. script-blind Pages 1–49 from
   `qa/_intent-first/GATE-1-49-COLD-READ.md`;
3. whole-book continuity from
   `qa/_intent-first/GATE-1-49-CONTINUITY.md`;
4. whole-book release from `qa/_intent-first/GATE-WHOLE-BOOK.md`.

The independent reviews may run in parallel. They never see generation prompts,
builder audits, rejected candidates, or prior reports. Minor cosmetic findings
are omitted; every blocking finding requires material reader harm and complete-
page redraw justification.

If all four approve, update `HANDOFF.md` and stop. Reader/publication work begins
in a separate bounded task.

## Communication

Report only state changes: preflight clean, candidate started, candidate
submitted, validated verdict, promotion, invalid report, resistant-defect hold,
v4 hold, final-gate verdict, or blocker. Never poll or send unchanged-progress
updates.
