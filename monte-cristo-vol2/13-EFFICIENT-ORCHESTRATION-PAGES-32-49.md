# Efficient production orchestration — Pages 32–49

**Status:** implemented for the remaining run on 2026-08-21. The original cost
analysis below is retained, while `14-INTENT-FIRST-BUILDER-CRITIC-RULES.md` and
`qa/_intent-first/ORCHESTRATOR.md` record the post-pilot critic threshold and
retry router.

**Current checkpoint:** Pages 1–32 are canonical. Page 32 was promoted from the
intent-first pilot and later received `APPROVED` from the revised materiality
critic. Page 33 is next.

## 1. What today proved

The builder–critic loop is working and must remain intact.

- Every completed candidate after the early grandfathered failures has reached
  an independent critic.
- The critic is finding reader-facing defects: attribution, order, costume,
  object state, identity, and continuity.
- The v4 ceiling and owner gate worked on Pages 30–31.
- Promotion remained byte-for-byte and rejected candidates were preserved.

The cost problem is the transport around that loop, not the loop itself.

### The avoidable cost

1. **Three long-lived contexts were reused.** The production lead, builder, and
   critic all accumulated the run from the beginning. The builder context is
   especially expensive because image-generation results live in its task
   history. A recent single builder turn serializes to more than one million
   transcript tokens because it contains the generated-image payload. That is
   not an exact Codex billing measurement, but it is decisive evidence that an
   image-bearing builder should not be reused for another candidate.
2. **The page-specific plan is still too large.** The remaining `qa/_plan/`
   files are 65–70 KB each. The actual page prompt plus appendix is only
   7.5–12.6 KB. A role packet can therefore be roughly **82–89% smaller** than
   the file currently opened by both roles.
3. **Unchanged work was polled and narrated repeatedly.** Several renders and
   reviews produced multiple “still processing” turns. Every such turn makes a
   long-running task pay for accumulated context again while adding no state.
4. **The production lead duplicated visual judgment.** It repeatedly inspected
   candidates while the independent critic was already performing the binding
   image review. The lead should validate files, hashes, counters, and holds;
   it should not load production images unless a critic report is internally
   inconsistent or the owner asks.
5. **Dynamic state is duplicated across stale documents.** The live ledger is
   current through Page 31, but `RUN-LOG.md`, `NEXT-STEPS-CODEX.md`,
   `RESUME-PROMPT-CODEX.md`, and the old root handoff describe earlier resume
   points. A fresh task should not have to reconcile several contradictory
   narratives.
6. **The current build gate is not clean.** `verify.py` reports that
   `qa/_plan/` is older than the master plan. Assembly and verification must be
   clean before Page 32.

The repository had already measured the earlier form of this problem: three
long-running sessions consumed 334 million input tokens against 21 generated
images, with the project record attributing roughly 97% of the spend to repeated
plan/context loading. Today's task reused the same basic session shape.

## 2. The decision

Use **two user-visible production tasks**, not eighteen:

| Task | Production scope | Gate before stopping |
|---|---|---|
| **A** | Pages 33–40 | Pages 31–40 sequence gate; fresh blind Pages 1–40 read; visual-continuity pass |
| **B** | Pages 41–49 | Pages 41–49 sequence gate; fresh blind Pages 1–49 read; final visual-continuity and whole-book gates |

Inside each task, use a **fresh child-agent context for every candidate**:

- one fresh builder for Page N vK;
- one fresh critic for Page N vK;
- if `REVISE`, a new builder for vK+1 and a new critic for vK+1;
- a fresh cold reader at each milestone;
- fresh batch and continuity reviewers.

Every child agent is spawned with **no inherited conversation history**
(`fork_turns: "none"`). It receives a bounded task and exact local file paths.
No page or candidate shares an agent context with another candidate.

This is the useful form of the “new orchestrator every ten pages” idea. The
outer dispatcher can safely cover one natural batch because it never loads
images or page plans. The contexts that actually hold images are discarded
after one candidate.

## 3. Model allocation

Recommended starting point:

| Role | Model / effort | Reason |
|---|---|---|
| Batch orchestrator | GPT-5.6 Luna, medium | Bounded dispatch, bookkeeping, deterministic validation |
| Builder | GPT-5.6 Luna, low | Executes a locked prompt; image quality comes from the in-app image generator |
| Page critic | GPT-5.6 Sol, medium | Visual/story judgment is the product |
| Batch, continuity, cold-read, whole-book critics | GPT-5.6 Sol, medium | Independent sequential judgment |

Do not use maximum reasoning by default. Raise critic effort only after a
representative review shows a measurable quality gain. Official OpenAI guidance
describes Luna as the efficient high-volume tier, medium as the balanced effort
starting point, and lean prompts as materially more token-efficient:
<https://developers.openai.com/api/docs/guides/latest-model>.

Image generation remains the built-in Codex/ChatGPT subscription path. No API
key, bundled image CLI, or separately billed OpenAI API path is authorized.

## 4. Context boundaries

| Role | May read | Must not read |
|---|---|---|
| Orchestrator | `SESSION-START.md`, `HANDOFF.md`, ledger tail, current manifest, critic verdict/report, deterministic check output | master plan, per-page plan, candidate images, proofs, image tool output, old task transcript |
| Builder | compact builder packet, exact issued prompt, approved reference paths, canonical predecessor; for a revision, the one critic report | master plan, other pages' plans, rejected candidate as an image input, prior builder task, prior candidate image |
| Critic | neutral current candidate/proofs; after the blind read, exact script, page intent and numbered critic card | generation prompt, builder audit, references, builder task/history, prior candidates/reports, version number, master plan, other page plans |
| Cold reader | promoted 600 × 900 proofs only, in order | script, prompt, appendices, reports, handoff, previous cold reads |

The builder audit remains production evidence but never enters the neutral
critic capsule. The Page 32 pilot showed that separating it completely is both
cleaner and cheaper.

## 5. Lean role packets

Before the next image, extend the deterministic assembly step to emit:

```text
qa/_run/
  page-33-builder.md
  page-33-critic.md
  page-33-critic-card.md
  ...
  page-49-builder.md
  page-49-critic.md
  page-49-critic-card.md
```

The builder packet contains only:

- the compact generate-and-submit contract;
- that page's exact prompt and reference manifest;
- output paths and the failed-generation exception;
- the v4 and no-API rules.

The blind critic entrypoint contains only:

- the compact transcription-first essentials gate;
- neutral input and report paths;
- the verdict contract.

The separate critic-card packet, opened only after the blind read, contains the
exact script, page intent, materiality threshold, and numbered blocking card.

The assembly verifier must prove that each packet matches its source prompt,
script page, and appendix, leaks no neighbouring page, and is newer than its
sources. Target size is under 15 KB per role packet. Production agents never
open `12-PRODUCTION-PLAN.md` or `qa/_plan/page-NN.md`.

For revisions, do not rebuild a large packet. The fresh builder reads the base
builder packet, the issued v1 prompt, and the current critic report, then writes
vK with only the mandatory correction and preservation clause.

## 6. One-candidate state machine

For Page N candidate K:

1. The orchestrator derives N and K from disk, never from conversational
   memory. It verifies the previous page is canonical and every manifest input
   exists in `refs/approved/`.
2. Spawn a zero-history builder. The task contains only page, candidate number,
   builder-packet path, output directory, and authority to use subscription-backed
   in-app image generation.
3. Wait for the builder's final receipt. Do not poll its task or read its
   transcript. The receipt is at most: candidate path, prompt path, audit path,
   proof paths, dimensions, and hashes.
4. Run one bundled deterministic check for file existence, dimensions, mode,
   candidate/report count, manifest inputs, and version ceiling.
5. Expose the candidate to the critic through a neutral review capsule such as
   `qa/_review/page-NN/current/`, using names that do not disclose v1/v2/v3/v4.
6. Spawn a fresh zero-history critic. It reads the neutral capsule and compact
   critic packet, writes one report, and returns only `APPROVED` or `REVISE`
   plus the report path.
7. Archive the report as `critic-vK.md` after the critic exits.
8. On `APPROVED`, promote the exact candidate bytes, verify the hash, derive
   promoted proofs, append the ledger and run-log row, and run the bundled
   verifier once.
9. On `REVISE`, validate the numbered material-harm/redraw contract and run the
   deterministic router. v1 normally receives a targeted v2. A criterion
   repeated on v1/v2 triggers a clean v3 prompt rewrite; persistence after that
   reset is an owner hold before v4. If repetition first appears on v3, v4 may
   be the clean reset. Never attach the rejected image.
10. On any v4 `REVISE`, stop and come to the owner. No v5, redesign, split, or
    story-document change.

The orchestrator does not visually approve or reject. If a critic report
contradicts its own transcription or invokes a void numeric gate, stop for
adjudication rather than having the orchestrator silently become another critic.

## 7. Wait and communication policy

- Use one event-driven long wait after dispatching a builder or critic.
- Do not repeatedly call status/list/read tools while the role is active.
- Do not send “still rendering” or “still reviewing” updates.
- Send a user update only when state changes: generation started, candidate
  submitted, verdict received, page promoted, hold reached, or blocker found.
- Never read a child task merely to obtain progress already represented by its
  final receipt.

This removes no useful feedback. It removes repeated turns whose only content is
that nothing changed.

## 8. Batch boundaries

### Task A — Pages 33–40

1. Preflight: rebuild assembly outputs and lean packets; `verify.py` must be
   `CLEAN`.
2. Produce Pages 33–40 sequentially under the per-candidate fresh-context loop.
3. After Page 40 promotion, run in separate fresh contexts:
   - sequence review of canonical Pages 31–40;
   - blind cold read of promoted Pages 1–40;
   - visual-continuity review of Pages 31–40, including the v4 Page 31 anchor.
4. Update `HANDOFF.md`, rewrite `SESSION-START.md` as the lean Task B entry point,
   and stop. Do not generate Page 41 in this task.

### Task B — Pages 41–49

1. Start from the clean Task A handoff, not by forking Task A.
2. Produce Pages 41–49 sequentially under the same loop.
3. After Page 49 promotion, run in separate fresh contexts:
   - sequence review of Pages 41–49;
   - blind cold read of Pages 1–49;
   - whole-book visual-continuity review;
   - whole-book gate.
4. Only after all gates pass, proceed to reader/final-publication work under its
   own bounded task.

The batch critics and blind reader may run in parallel because they are
independent and have non-overlapping context. Page generation never runs in
parallel.

## 9. Implemented preflight before Page 33

Completed on 2026-08-21:

1. `assemble.py` emits the intent-first role packets and `verify.py` is clean.
2. Backfill `RUN-LOG.md` through Page 31 in a separate low-cost bookkeeping
   task, or append one explicit correction that the production ledger and
   per-page critic reports are authoritative. Do not burden the production
   orchestrator with reconstructing twenty pages of history.
3. Mark `NEXT-STEPS-CODEX.md` and `RESUME-PROMPT-CODEX.md` as superseded by
   `SESSION-START.md`.
4. Keep one dynamic handoff only: `HANDOFF.md`.
5. `SESSION-START.md` confirms canonical Page 32's hash before spawning the Page
   33 builder.

## 10. Success criterion

The optimization succeeds only if page quality and evidence stay unchanged
while repeated context falls:

- every completed candidate still reaches an independent critic;
- every critic still transcribes from the 600 × 900 proof first;
- all page-specific numbered critic-card checks still run;
- no rejected candidate becomes an input;
- promotion remains byte-identical;
- the v4 and batch holds remain binding;
- builders, critics, and cold readers never carry earlier candidate history;
- the outer orchestrator completes one natural batch without loading a single
  production image or full page plan.

Exact credit savings cannot be inferred from repository artifacts. The useful
measurement for the next run is: generated images, child-agent count, outer-task
turn count, context compactions, and whether any child context is reused. Record
those at each batch close.
