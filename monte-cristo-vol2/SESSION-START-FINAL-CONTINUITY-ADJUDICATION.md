# Monte Cristo Volume II — final continuity adjudication

> **SUPERSEDED:** The adjudication returned `CLEARED — APPROVED`. Do not execute
> this entry point again. Read `HANDOFF.md` for current state.

Run this as a new bounded task with the directory containing this file as the
workspace and current working directory.

## Role and models

- Orchestrator: GPT-5.6 Luna, medium.
- Adjudicator: one fresh zero-history GPT-5.6 Sol, medium.
- No builder and no image generation.

## Execute

1. Read `HANDOFF.md`.
2. Confirm canonical Pages 1–49 exist and Page 49 is the final scripted page.
3. Confirm these reports say `APPROVED`:
   - `qa/batches/batch-41-49.md`
   - `qa/cold-reads/cold-read-49.md`
   - `qa/whole-book.md`
4. Confirm `qa/continuity/continuity-pass-01-49.md` contains the single disputed
   Page 30 Chamber finding.
5. Launch one fresh Sol-medium adjudicator with only
   `qa/_intent-first/ADJUDICATE-FINAL-CONTINUITY.md` as its instruction packet.
6. Require the exact output path and verdict contract from that packet.

## Route the verdict

If the report says `CLEARED — APPROVED`:

- preserve both the original continuity report and adjudication;
- update `HANDOFF.md` and `../MONTE-CRISTO-VOLUME-2-HANDOFF.md` to state that
  Pages 1–49 are complete and all final gates are cleared, with continuity
  cleared by independent adjudication;
- state that reader/publication work is next in a separate task;
- stop.

If the report says `SUSTAINED — OWNER HOLD`:

- update `HANDOFF.md` and `../MONTE-CRISTO-VOLUME-2-HANDOFF.md` with the owner
  hold;
- do not generate Page 30 v5, redesign, split, or alter the protected script or
  contract;
- stop and report the hold to the owner.

Communicate only the final adjudication outcome or an actual blocker. Do not
poll, open the previous production tasks, or inspect unrelated pages.
