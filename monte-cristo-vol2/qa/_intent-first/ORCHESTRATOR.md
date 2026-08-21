# Intent-first production orchestrator — shared contract

## Boundary

The orchestrator owns state, dispatch, deterministic validation, retry routing,
byte-identical promotion, the append-only ledger, and holds. It is nonvisual.
Never open candidate images, proofs, image-tool output, generation prompts,
builder audits, master/per-page plans, rejected candidates, or child-task
transcripts.

Open only the current session start, current handoff, ledger tail, compact role
packet paths, deterministic helper output, validated critic report text, and
file metadata/hashes. Do not approve or reject artwork.

## One-candidate loop

For Page N candidate vK:

1. Derive N and K from disk. Confirm Page N−1 is canonical and matches the
   ledger. Confirm vK is at most v4 and the output paths do not already exist.
2. Choose the builder mode from the last mechanical route: `BASE` for v1,
   `TARGETED`, or `FULL_PROMPT_RESET`.
3. Spawn one fresh zero-history GPT-5.6 Luna-low builder with only
   `qa/_run/page-NN-builder.md`, N, K, the mode, and any exact revision inputs
   allowed below. It generates one candidate, audit, issued prompt, and two
   proofs, then returns paths/dimensions/hashes only.
4. Wait once for completion. Do not poll, list repeatedly, read the child task,
   or send unchanged-progress updates.
5. Run `python3 qa/_intent-first/check-candidate.py N K`. A builder audit never
   gates review. A failed deterministic check stops; it does not authorize an
   art judgment by the orchestrator.
6. Copy only the candidate and two proofs behind the fixed neutral names in
   `qa/_review/page-NN/current/`. Remove/replace only those three named neutral
   files and any old neutral `critic-report.md`. Never copy the issued prompt or
   audit into the review capsule.
7. Spawn one fresh zero-history GPT-5.6 Sol-medium critic with only
   `qa/_run/page-NN-critic.md`. It completes the blind read before opening
   `qa/_run/page-NN-critic-card.md`, writes the neutral report, and returns only
   `APPROVED` or `REVISE`.
8. Wait once. Run
   `python3 qa/_intent-first/validate-report.py N qa/_review/page-NN/current/critic-report.md`.
   If invalid, stop as `INVALID_CRITIC_REPORT`. Do not repair the report or
   regenerate art.
9. Archive the validated report byte-for-byte as
   `qa/production/page-NN/critic-vK.md`. Run
   `python3 qa/_intent-first/route-after-critic.py N K`.
10. Follow exactly the emitted route. No visual reinterpretation and no route
    outside the list below.

## Revision inputs

`TARGETED` gives the fresh builder only:

- its base builder packet;
- the immediately preceding issued prompt;
- the latest validated critic report;
- a one-line instruction to correct its cited criteria while preserving the
  successful facts in the blind read.

`FULL_PROMPT_RESET` gives the fresh builder only:

- its base builder packet;
- the last two short validated critic reports;
- the repeated criterion numbers emitted by the router;
- a one-line instruction to replace the entire prompt and composition strategy.

For a reset, never provide an earlier issued prompt, candidate, proof, audit, or
builder history. The builder may rethink framing, staging, hierarchy, and panel
composition, but not exact strings, page intent, story facts, reference
manifest, critic card, or page count.

## Mechanical routes

- `PROMOTE`: copy the exact candidate bytes to `pages/page-NN.png`; verify the
  hashes match; derive promoted proofs; append the ledger with version, report,
  and SHA; then run the assembly verifier once. Only now release Page N+1.
- `TARGETED`: start the next allowed version with the targeted inputs above.
- `FULL_PROMPT_RESET`: start the next allowed version with reset inputs above.
- `RESISTANT_DEFECT_HOLD`: the same numbered criterion survived a targeted
  correction and clean prompt reset. Stop before another generation and bring
  the evidence to the owner.
- `V4_OWNER_HOLD`: stop. No v5, redesign, split, component generation, or
  story-document change.
- `INVALID_CRITIC_REPORT`: stop. An out-of-card, harm-free, or unjustified
  finding is a failed critic contract, not an art defect.

Never create frames, crops, composites, inpaints, prompt experiments, or
parallel variants. Never use rejected art as a reference. Never modify
`07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`.

## Context and communication discipline

- One orchestrator covers only its bounded natural batch.
- One fresh builder and one fresh critic cover one candidate each.
- The orchestrator never loads image payloads.
- One event-driven wait follows each dispatch; no status polling.
- Report only actual state changes.
- The ledger and canonical files, not prose memory, define progress.
