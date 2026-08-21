# The Count of Monte Cristo — Volume II

**Story-page production is complete. Reader/publication begins from
[`monte-cristo-vol2/SESSION-START-READER-PUBLICATION.md`](monte-cristo-vol2/SESSION-START-READER-PUBLICATION.md)
and [`monte-cristo-vol2/HANDOFF.md`](monte-cristo-vol2/HANDOFF.md).**

Everything a fresh agent needs is inside `monte-cristo-vol2/`. This root file is
a signpost and holds no authority of its own.

## State — 2026-08-21

Phases 1 through 5 of the `monte` skill are complete, and story-page production
is complete through the scripted ending. Execution remains **Codex in-app,
billed to the ChatGPT subscription**. The OpenAI API path is not approved.

The volume is **49 portrait pages**, 1024 × 1536.

**Pages 1–49 are complete, and Page 49 is the final scripted story page.** The
Pages 41–49 sequence gate, script-blind Pages 1–49 cold read, and whole-book
release gate returned `APPROVED`. Independent adjudication of the one disputed
Page 30 Chamber continuity finding returned `CLEARED — APPROVED`; all final
gates are cleared. Reader/publication work is next in a separate task.

No production or adjudication task remains active. The reader/publication task
is complete locally: the 49-page reader, ending, quiz, and library card passed
deterministic verification and fresh independent desktop/tablet review. The
reader uses dedicated `#end` and `#quiz` routes, persists only real story pages,
and normalizes legacy `#page-50` / `#page-51` routes. The final verification is
recorded in `monte-cristo-vol2/READER-PUBLICATION-VERIFICATION.md`; no story
artwork was altered. The optimized orchestration design and binding
post-pilot correction are recorded in
[`monte-cristo-vol2/13-EFFICIENT-ORCHESTRATION-PAGES-32-49.md`](monte-cristo-vol2/13-EFFICIENT-ORCHESTRATION-PAGES-32-49.md)
and
[`monte-cristo-vol2/14-INTENT-FIRST-BUILDER-CRITIC-RULES.md`](monte-cristo-vol2/14-INTENT-FIRST-BUILDER-CRITIC-RULES.md).

`RUN-LOG.md`, `NEXT-STEPS-CODEX.md`, and `RESUME-PROMPT-CODEX.md` retain useful
historical evidence but have stale resume points. Do not use them as current
state. `qa/production-ledger.md` and the new local handoff are authoritative.

The v4 ceiling still counts total completed candidates from v1 and never resets;
**neither lettering size nor panel share is a gate on a rendered page**; and the
builder submits every completed candidate to an independent critic.

| File | What it is |
|---|---|
| `12-PRODUCTION-PLAN.md` | the deliverable — every page prompt, the builder/critic architecture, 49 critic appendices |
| `RUN-LOG.md` | Historical learning record with a stale resume point. Do not open or backfill it inside the production orchestrator. |
| `qa/production-ledger.md` | the append-only promotion record: one row per promoted page, SHA, gate rounds |
| `08-FULL-SCRIPT.md` | the script, after five gate rounds and one page split |
| `07-PAGE-CONTRACT.md` | per-page mode, dominant turn, dominant share, locations, text inventory |
| `09-REFERENCE-PLAN.md` | the cast and sets as a system; the reference gate |
| `10-CRITIC-OPERATIONS.md` · `11-PRODUCTION-TOPOLOGY.md` | the briefs and the topology in source form — both are reproduced inside the plan |
| `qa/_assembly/` | the fragments the plan is built from, plus `assemble.py` and `verify.py` |

**`08-FULL-SCRIPT.md` and `07-PAGE-CONTRACT.md` are owner-controlled.** The
executor may not edit either.

`verify.py` is the mechanical gate on the plan and compact intent-first packets.
Run it after any edit to a fragment, and re-run `assemble.py` first — the plan is
a build artifact, so **never hand-edit sections 5 through 10.** Sections 1
through 4 live in the plan file itself and are safe to edit directly. Story-page
production and final adjudication are closed; do not reopen them during the
task in `SESSION-START-READER-PUBLICATION.md`.

## The abandoned run

`monte-cristo-vol2-abandoned/` is a previous attempt, kept only as evidence. Its
script was rejected. **Do not inherit, copy, adapt, or cite anything in it, and
do not reuse its references or pages.** If you found this file by grepping the
repo root, that folder is the thing this note exists to steer you away from.

## Volume I

`monte-cristo-expanded/` shipped at 55 pages and is the register anchor and the
parent authority. Returning characters must read as the same people, aged
forward.
