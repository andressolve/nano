# Monte Cristo Volume II — current production handoff

**Updated:** 2026-08-21

## Canonical state

- Pages **1–49** are promoted in `pages/`. Page 49 is the final scripted story
  page; there is no Page 50 production packet.
- Pages 33–40 were produced under the intent-first builder–critic workflow.
  Promoted versions: Page 33 v1, Page 34 v1, Page 35 v2, Page 36 v1,
  Page 37 v2, Page 38 v3, Page 39 v2, and Page 40 v1.
- Pages 41–49 were produced under the same workflow. Promoted versions:
  Page 41 v2, Page 42 v1, Page 43 v3, Page 44 v1, Page 45 v2, Page 46 v2,
  Page 47 v1, Page 48 v4, and Page 49 v1.
- The authoritative byte hashes and promotion history are in
  `qa/production-ledger.md`.

Page 32 remains the owner-promoted intent-pilot candidate. Its original critic
returned `REVISE` only for repeated crowd faces; the owner judged that real
defect nonblocking, and a fresh materiality critic approved the unchanged page.
The complete evidence remains in `qa/production/page-32/intent-pilot/`.

## Final-gate state

Pages **1–49 are complete and all final gates are cleared**. Three of the four
required final reviews returned `APPROVED` directly:

1. `qa/batches/batch-41-49.md` — canonical Pages 41–49 sequence;
2. `qa/cold-reads/cold-read-49.md` — script-blind Pages 1–49 cold read;
3. `qa/whole-book.md` — whole-book release review.

The fourth report, `qa/continuity/continuity-pass-01-49.md`, returned `REVISE`
for the Page 30 Chamber exterior. Independent adjudication in
`qa/continuity/continuity-pass-01-49-adjudication.md` returned
`CLEARED — APPROVED`, clearing the continuity gate.

The reported defect is disputed rather than accepted automatically:

- the report says Page 30 has only a single frontal staircase, but the page
  visibly includes a second stair rising along the building's right side;
- Page 30 and the approved Chamber lock both show a stone columned portico,
  broad entry steps, and a side stair; the lock's dome is outside Page 30's
  close side-street crop;
- Page 30 explicitly names the Chamber of Peers, and both the script-blind cold
  reader and whole-book release reviewer followed the Page 30–31 transition
  without location confusion.

The adjudication found that the original report misstated the visible side
stair and did not establish material reader harm or full-redraw justification.

## Reader/publication state

The 49-page reader, ending, five-question comprehension quiz, and public
library card are complete. Deterministic assembly and reader verification both
returned `CLEAN`. The fresh independent desktop/tablet critic returned
`APPROVED`; the final verification is recorded in
`READER-PUBLICATION-VERIFICATION.md`.

The reader uses dedicated `#end` and `#quiz` routes, persists only real story
pages, and normalizes legacy `#page-50` / `#page-51` routes. No story artwork
was changed during publication work.

## Next task — publication follow-up

The reader/publication task is complete locally and is being published directly
to `main`, followed by GitHub Pages verification. No further story-page
generation is authorized.

## Binding production record

- Intent-first rules: `14-INTENT-FIRST-BUILDER-CRITIC-RULES.md`
- Shared state machine: `qa/_intent-first/ORCHESTRATOR.md`
- Promotion ledger: `qa/production-ledger.md`
- Final adjudication card:
  `qa/_intent-first/ADJUDICATE-FINAL-CONTINUITY.md`
- Reader builder packet: `qa/_publication/BUILDER.md`
- Reader critic packet: `qa/_publication/CRITIC.md`
- Reader verifier: `qa/_publication/verify-reader.py`

Never edit `07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`. Never use anything
from `monte-cristo-vol2-abandoned/`. Image generation remains subscription-only;
no API-billed fallback is authorized.

## Superseded production entry points

`SESSION-START.md` and `SESSION-START-PAGES-41-49.md` describe completed
production batches, and `SESSION-START-FINAL-CONTINUITY-ADJUDICATION.md`
describes the completed final adjudication. Do not execute them again. `RUN-LOG.md`,
`NEXT-STEPS-CODEX.md`, and `RESUME-PROMPT-CODEX.md` also have stale resume
points and must not be used as current state.
