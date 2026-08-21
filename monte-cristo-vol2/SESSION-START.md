# Monte Cristo Volume II — completed Pages 33–40 entry point

> **SUPERSEDED:** Pages 33–40 are complete. Do not execute this production
> entry point again. Read `HANDOFF.md` for current state.

This is the sole production entry point for the next fresh Codex task. Page 32
is canonical. Produce Pages **33–40 sequentially**, run the Pages 31–40
milestone gates, update the handoff, and stop. Do not generate Page 41 in this
task.

## Start

1. Read `HANDOFF.md`.
2. Read `14-INTENT-FIRST-BUILDER-CRITIC-RULES.md`.
3. Read `qa/_intent-first/ORCHESTRATOR.md`.
4. Run `python3 qa/_assembly/assemble.py` and
   `python3 qa/_assembly/verify.py`. Both must finish cleanly before production.
5. Confirm `pages/page-32.png` has SHA-256
   `ccc6332d2f1fb7bbb1b3da21f265fbb82e6e5ea8c47304960ce21155c0da5d6d`.
6. Begin with the first unpromoted page in the bounded range 33–40, deriving
   state from canonical files, the production ledger, and validated reports on
   disk—not from conversational memory.

Do not open `12-PRODUCTION-PLAN.md`, `qa/_plan/page-NN.md`, candidate images,
proofs, old production tasks, or historical Page 32 materials. The compact
`qa/_run/` packets contain the complete role inputs.

## Models and context

- Orchestrator: GPT-5.6 Luna, medium.
- Builder: fresh GPT-5.6 Luna, low, no inherited task history, one candidate.
- Page critic: fresh GPT-5.6 Sol, medium, no inherited task history, one review.
- Milestone reviewers: fresh GPT-5.6 Sol, medium, no inherited task history.

Every image-bearing or image-reviewing role is discarded after that one job.
Use only subscription-backed Codex in-app image generation. No API key, bundled
image CLI, or API fallback.

## Batch close after Page 40

After Page 40 is promoted, run three independent fresh reviews:

1. canonical Pages 31–40 from `qa/_intent-first/GATE-31-40-SEQUENCE.md`;
2. a script-blind Pages 1–40 read from
   `qa/_intent-first/GATE-1-40-COLD-READ.md`;
3. Pages 31–40 continuity from
   `qa/_intent-first/GATE-31-40-CONTINUITY.md`.

These reviews may run in parallel. None sees generation prompts, builder audits,
rejected candidates, or prior review reports. A finding blocks only with
material reader harm and redraw justification; minor cosmetic observations are
omitted.

If all three approve, update `HANDOFF.md` with Page 40 and the gate results and
stop. Tell the owner to begin a brand-new Luna task from
`SESSION-START-PAGES-41-49.md`. Do not create or start that task automatically.

## Communication

Report only state changes: preflight clean, candidate started, candidate
submitted, validated verdict, promotion, invalid report, resistant-defect hold,
v4 hold, milestone verdict, or blocker. Never poll or send unchanged-progress
updates.
