# Production Topology — intent-first Pages 33–49

## Roles and context lifetime

| Role | Lifetime | Owns | Never owns |
|---|---|---|---|
| Batch orchestrator | one bounded batch | state, dispatch, deterministic checks, routing, promotion, holds | visual judgment, image payloads, prompt authorship |
| Builder | one candidate | generation, issued prompt, non-gating audit, proofs | approval, promotion, private variants |
| Page critic | one candidate | blind reader judgment, numbered findings, verdict | generation prompt, builder audit, editing, promotion |
| Milestone reviewer | one gate | sequence, cold-read, continuity, or release verdict | prior reports, prompt fidelity, cosmetic collection |

Every builder and critic starts with no inherited task history and is discarded
after one job. The Pages 33–40 orchestrator stops after the Page 40 milestone;
Pages 41–49 start in a brand-new task.

## Current paths

```text
monte-cristo-vol2/
  SESSION-START.md                    Pages 33–40 entry point
  SESSION-START-PAGES-41-49.md        fresh final-batch entry point
  14-INTENT-FIRST-BUILDER-CRITIC-RULES.md
  pages/page-NN.png                   promoted bytes only
  refs/approved/                      approved image inputs only
  qa/
    _assembly/
      intent-first-intents-33-49.md   page-intent source
      intent-first-prompts-33-49.md   builder-only prompt source
      intent-first-cards-33-49.md     critic-card source
      assemble.py                     emits plans and compact role packets
      verify.py                       coherent-system preflight
    _intent-first/
      ORCHESTRATOR.md                 shared nonvisual state machine
      check-candidate.py              deterministic image/file/hash check
      validate-report.py              critic-contract check
      route-after-critic.py           numbered retry/reset/hold router
    _run/
      page-NN-builder.md
      page-NN-critic.md               blind entrypoint only
      page-NN-critic-card.md          opened after blind read
    _review/page-NN/current/
      candidate.png
      desktop-600x900.png
      tablet-768x1152.png
      critic-report.md
    production/page-NN/
      prompts/page-NN-vK.md
      candidates/page-NN-vK.png
      audits/page-NN-vK.md
      proofs/page-NN-vK-600x900.png
      proofs/page-NN-vK-768x1152.png
      critic-vK.md
    production-ledger.md
```

The neutral review capsule never contains a prompt or builder audit. Its report
is archived only after mechanical validation, keeping the critic blind to
version history.

## Page loop

```text
canonical Page N-1
        ↓
fresh builder: one candidate + audit + proofs
        ↓
deterministic check; neutral image capsule
        ↓
fresh blind critic → numbered report
        ↓
report validator → mechanical router
        ├── APPROVED → byte-identical promotion → release N+1
        ├── TARGETED → fresh builder, latest prompt + report
        ├── FULL PROMPT RESET → fresh builder, base packet + compact findings
        └── INVALID / RESISTANT / v4 → stop for owner
```

Only one page is in flight. Generation never outruns promotion. A rejected
candidate is evidence and never a continuity or generation input.

## Retry ceiling

- v1 finding → targeted v2.
- a v1/v2 repeated numbered criterion → clean v3 prompt rewrite.
- persistence after the clean rewrite → resistant-defect hold before v4.
- if repetition first appears on v3, v4 may be the clean rewrite.
- any v4 `REVISE` → owner hold; no v5, redesign, split, or component work.

The builder may rethink composition during a reset but may not change the page
intent, exact strings, story facts, approved references, critic card, page
count, `07-PAGE-CONTRACT.md`, or `08-FULL-SCRIPT.md`.

## Promotion

1. Copy the approved candidate to `pages/page-NN.png`.
2. Verify source and destination SHA-256 match.
3. Derive promoted desktop/tablet proofs.
4. Append the authoritative ledger row with version, report, and hash.
5. Run the bundled verifier once.
6. Release the next page.

No conditional approval exists. An owner tolerance is recorded explicitly and
does not rewrite the critic's original report.

## Holds

| Hold | Trigger |
|---|---|
| Invalid critic report | out-of-card criterion, missing material harm, or missing redraw justification |
| Resistant defect | same numbered criterion survives targeted correction and clean reset |
| v4 ceiling | any valid v4 `REVISE` |
| Batch milestone | after Page 40 and after Page 49 |
| Protected authority | any proposed edit to the page contract or full script |

The orchestrator does not solve a hold by looking at the artwork. It stops with
the compact evidence and asks the owner.

## Communication and billing discipline

- Use subscription-backed Codex in-app image generation only.
- Never reuse an image-bearing child context.
- Wait once per builder or critic; do not poll or narrate unchanged state.
- The orchestrator opens no production image, master plan, old task transcript,
  or large per-page plan.
- Report only starts, submissions, verdicts, promotions, holds, and blockers.
