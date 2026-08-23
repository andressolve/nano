# Dialogue Plan

**Recorded:** 2026-08-21
**Status:** Implemented and independently approved.
**Completed:** 2026-08-21.

**Upstream extension completed:** 2026-08-23. The studio now includes a
research-and-adaptation phase whose target is ultra-premium storytelling for a
named audience rather than academic completeness or default source fidelity.
It adds a persistent default audience profile, bounded research handoffs,
explicit adaptation liberties, a source-blind-first audience critic, graphical
direction, an owner-facing greenlight proposal, a project initializer, and a
deterministic adaptation-readiness gate before production.

## Objective

Create `nano/dialogue/` as a self-contained production studio for future
long-form, dialogue-driven graphic novels following the successful post-Page 32
*Monte Cristo Volume II* framework.

Existing published projects, including both *Monte Cristo* volumes, remain in
their current locations. Do not move their folders, assets, readers, or public
URLs.

## 1. Workspace structure

```text
nano/dialogue/
  AGENTS.md
  README.md
  PLAYBOOK.md
  PROMPTING.md
  templates/
    project/
    roles/
    gates/
  tools/
  case-studies/
    monte-cristo-vol2.md
  works/
```

Future projects live in `nano/dialogue/works/<project-slug>/`. Production
sessions launch from the individual project folder, not from generic `nano/`.

## 2. Authority hierarchy

`dialogue/AGENTS.md` will enforce this order:

1. owner-approved project script, page contract, and references;
2. `dialogue/PLAYBOOK.md` for production procedure;
3. `dialogue/PROMPTING.md` for builder prompt construction;
4. the project's page intent, builder-only generation prompt, and numbered
   critic card;
5. case studies as historical evidence only, never production authority.

Each project has exactly one active `SESSION-START.md` and one dynamic
`HANDOFF.md`.

## 3. Preserve post-Page 32 prompting practice

`PROMPTING.md` will make the successful prompt method explicit:

- begin with the reader-facing event and dominant dramatic relationship;
- preserve exact text, attribution, essential action, named identity, and
  consequential continuity;
- use only the minimum approved references genuinely needed;
- make a few page essentials unmistakable while leaving the generator room to
  solve the image;
- use moderate composition guidance rather than exact percentages,
  coordinates, or fragile geometry;
- remove decorative precision, microscopic proof lists, and tiny-prop
  legibility unless the reader must understand that prop;
- never make prompt compliance the approval standard;
- never build cumulative correction monster-prompts.

Revision policy:

1. first material failure receives a targeted correction that protects the
   reader-facing facts that already succeeded;
2. a repeated numbered failure triggers a clean rewrite of the complete prompt
   and composition strategy;
3. rejected images are never fed back as generation inputs;
4. the critic never sees or judges the generation prompt.

Preserve a small annotated gold-prompt library drawn from the Page 32 revision
and successful Pages 33–49 work:

- the revised Page 32 approach;
- one first-pass dramatic prompt;
- one successful targeted correction;
- Page 38's successful clean-reset prompt;
- one successful quiet or final-page prompt.

These examples demonstrate density, priorities, and tone without requiring a
future builder to ingest the complete Volume II archive.

## 4. Reusable role and gate packets

Create project-neutral templates for:

- project and session start;
- reader-facing page intent;
- builder packet and generation prompt;
- numbered critic card;
- blind-first critic packet and critic report;
- bounded batch orchestrator;
- sequence, cold-read, visual-continuity, and final-release gates;
- project handoff.

Extract and parameterize the proven packet assembler, preflight verifier,
candidate checker, critic-report validator, and numbered retry router. The
reusable versions must contain no Monte-specific names, characters, paths, or
page numbers.

## 5. Efficient orchestration contract

The playbook will require:

- one bounded orchestrator for approximately ten pages;
- a brand-new orchestrator at every batch boundary;
- a fresh builder context for every candidate;
- a fresh zero-history critic for every review;
- only one page in flight;
- state derived from disk rather than conversational memory;
- no production images, master plans, old transcripts, or large historical
  files in orchestrator context;
- one event-driven wait instead of repeated polling;
- compact receipts and role packets;
- parallel milestone critics only when their work is independent;
- no image generation during framework setup or testing.

Record the models used successfully in the Volume II case study. Keep the
timeless playbook capability-based so model-name changes do not obsolete it.

## 6. Critic and redraw contract

The critic is a reader-facing release gate, not a prompt-compliance checker or
defect collector. It receives a neutral candidate and proofs, performs a blind
read, and only then opens the exact script, page intent, and numbered critic
card. It never receives the generation prompt, builder audit, rejected
candidates, version number, prior reports, or task history.

Every `REVISE` finding must:

1. cite a numbered blocking criterion;
2. state the visible observation;
3. explain the material reader harm;
4. explain why that harm justifies risking a complete-page redraw.

The nonvisual orchestrator validates that contract mechanically. Invalid or
out-of-scope criticism does not authorize another generation.

Retry routing remains:

- `v1 REVISE` -> targeted `v2`;
- the same criterion on `v1` and `v2` -> clean-slate `v3` prompt rewrite;
- persistence after the clean rewrite -> resistant-defect owner hold;
- if repetition first arises on `v2`/`v3`, `v4` may be the clean rewrite;
- any `v4 REVISE` -> owner hold; no `v5`.

## 7. Volume II case study

Create `dialogue/case-studies/monte-cristo-vol2.md` as a concise factual record
covering:

- the original Page 32 seal and repeated-face findings;
- why technically true criticism produced the wrong production decision;
- the owner's materiality correction and revised critic approval of the
  unchanged page;
- Pages 33–49 completing 17 pages in 30 candidates;
- eight first-candidate approvals;
- Page 38's successful clean prompt reset;
- Page 48 resolving at `v4`;
- the successful batch, cold-read, continuity, and whole-book gates;
- which lessons are general and which remain Monte-specific.

The case study supplies evidence but is not loaded during ordinary production.

## 8. Retire contradictory root guidance

After migrating all still-valid material:

- replace root `dialogue.md` with a short compatibility pointer to the new
  authority;
- replace root `builder-critic.md` with a pointer to the new templates;
- reduce the dialogue-specific section of root `AGENTS.md` to a routing rule;
- preserve unrelated owner changes already present in those files;
- verify that no active document still instructs the critic to receive the
  generation prompt or builder audit.

## 9. Verification

Before declaring the workspace ready:

1. instantiate one text-only sample project under `dialogue/works/`;
2. assemble its compact role packets without generating any image;
3. verify that prompt and builder-audit material cannot leak into critic
   transport;
4. replay archived Volume II report scenarios through the generic validator and
   router;
5. verify approval, targeted correction, clean reset, resistant-defect hold,
   `v4` hold, and invalid-report routes;
6. confirm that a fresh orchestrator can start from the sample project's
   `SESSION-START.md` without reading outside the project and framework;
7. run contradiction and broken-link checks;
8. confirm that no existing production image, reader, project folder, or public
   path changed.

## Completion standard

The work is complete only when a future project can be started inside
`dialogue/works/<project-slug>/` from one compact entry point, use the proven
intent/prompt/critic separation and bounded builder-critic loop, and reach a
mechanically verified handoff without depending on the wider `nano/` history or
obsolete pre-Page 32 rules.

## Implementation result

- The specialized workspace now lives in `dialogue/` with scoped instructions,
  canonical playbook, prompting standard, executable project/role/gate
  templates, generic validators/router, Volume II case study, and an image-free
  rehearsal project.
- The prompting record preserves distinct annotated structures from the revised
  Page 32 prompt, Page 33 v1, Page 35 v2 targeted correction, Page 38 v3 clean
  reset, and Page 49 v1.
- Exact-script authority transport, critic-context separation, complete
  PNG/dimension/mode/hash validation, material critic-report schema, all six
  retry outcomes, and derived receipt/handoff verification are enforced by 15
  passing tests.
- Root `dialogue.md` and `builder-critic.md` are compatibility pointers. Root
  `AGENTS.md` retains global rules and routes new dialogue-driven work into the
  specialized studio.
- One Luna-medium builder created the initial workspace; one fresh Sol-medium
  critic returned `REVISE`; the bounded corrections were re-audited until the
  same independent critic returned `APPROVED`.
- No story image, prototype, existing reader, published project path, or
  existing project asset was changed by this implementation.
