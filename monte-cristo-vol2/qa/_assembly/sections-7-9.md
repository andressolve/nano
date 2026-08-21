# 7 · Revision, routing, and promotion

## Valid redraw authority

Only a mechanically valid independent `REVISE` authorizes another candidate.
Every finding must cite a numbered page-card criterion, state material reader
harm, and justify risking a complete redraw. An out-of-card, cosmetic, numeric,
or harm-free finding is an invalid critic report—not an art defect.

The builder audit never authorizes a redraw. It records the intent read,
transcription, and technical facts, then submits every completed candidate.

## Targeted correction

A targeted builder receives the base builder packet, immediately preceding
issued prompt, and latest validated critic report. It corrects only the cited
material criteria and protects the successful reader facts from the blind read.
No unrelated polish pass, patch, crop, composite, inpaint, or rejected-image
input is allowed.

## Clean prompt reset

If the same numbered criterion survives v1 and targeted v2, v3 is a full
clean-slate rewrite of the generation prompt and composition strategy. The
fresh builder receives the base packet, last two compact reports, and repeated
criterion numbers. It does not receive earlier issued prompts, candidates,
proofs, audits, or builder history.

The reset may rethink framing, staging, hierarchy, and panel composition. It
may not change exact strings, page intent, story facts, approved references,
critic card, page count, `07-PAGE-CONTRACT.md`, or `08-FULL-SCRIPT.md`.

If that repeated criterion survives the clean reset, stop before another
generation as a resistant-defect owner hold. If repetition first appears from
v2 to targeted v3, v4 may be the clean prompt reset.

## The v4 ceiling

The count is total completed candidates from v1 and never resets. Any v4
`REVISE` stops the run. No v5, autonomous redesign, split, component generation,
or story-document change. The owner decides what happens next.

## Mechanical routes

After the critic report is validated, the router returns exactly one:

- `PROMOTE`
- `TARGETED`
- `FULL_PROMPT_RESET`
- `RESISTANT_DEFECT_HOLD`
- `V4_OWNER_HOLD`
- `INVALID_CRITIC_REPORT`

The orchestrator never opens the art or substitutes its own visual judgment.

## Promotion

On unconditional validated `APPROVED` only:

1. copy the exact candidate bytes into `pages/page-NN.png`;
2. verify source and destination SHA-256 match;
3. derive promoted 600 × 900 and 768 × 1152 proofs;
4. append the authoritative ledger row with version, report, and hash;
5. run the bundled verifier once;
6. release Page N+1.

An owner tolerance is recorded beside the unchanged original critic report; it
is never rewritten as critic approval.

## Holds

| Hold | Trigger |
|---|---|
| Invalid critic report | report violates the numbered material-harm contract |
| Resistant defect | same criterion survives targeted correction and clean reset |
| v4 ceiling | any valid v4 `REVISE` |
| Batch milestone | after Page 40 and Page 49 |
| Protected authority | proposed edit to page contract or full script |

---

# 8 · Evidence and ledger

The append-only running record is `qa/production-ledger.md`. One row is added
only after promotion.

```text
qa/production/page-NN/
  prompts/page-NN-vK.md
  candidates/page-NN-vK.png
  audits/page-NN-vK.md
  proofs/page-NN-vK-600x900.png
  proofs/page-NN-vK-768x1152.png
  critic-vK.md
```

The neutral review capsule contains only the current candidate and two proofs,
plus the critic's neutral report path. It never contains a prompt or audit and
is not historical evidence; the archived production folder is.

Rejected candidates and their evidence remain on disk but never become image
inputs or continuity anchors.

---

# 9 · Remaining-run failure watchlist

At each batch boundary verify:

1. Every completed candidate has exactly one archived independent critic report.
2. No builder or critic context was reused.
3. No critic received a generation prompt, builder audit, prior report, or
   version history.
4. No orchestrator opened a candidate, proof, or image-tool result.
5. No rejected candidate was attached as an image input.
6. Every `REVISE` passed the numbered material-harm/redraw validator.
7. Every repeated criterion followed targeted → clean reset → owner-hold
   routing, with no improvised extra attempts.
8. Nobody measured lettering or panel shares; blind transcription and the
   reader event remained the gates.
9. No “still processing” polling turns were emitted.
10. Canonical bytes match the approved candidate hashes.

---

# 10 · Current executor entry point

Do not execute this large master plan inside production. It is the assembled
authority and audit artifact. The remaining run begins from the compact current
entry point:

```text
SESSION-START.md
```

That starts one fresh Luna-medium orchestrator for Pages 33–40. After the Page
40 milestone passes, it stops. A brand-new task begins from:

```text
SESSION-START-PAGES-41-49.md
```

All image generation is subscription-backed Codex in-app. No API-key, bundled
CLI, or separately billed API fallback is authorized.
