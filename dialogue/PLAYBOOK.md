# Dialogue Studio Playbook

This is the canonical production procedure for long-form narrative graphic
novels whose story depends on dialogue, sequential causality, recurring
identities, and native lettering. It does not govern biographical comics.

## 1. Authority and scope

Authority descends in this order:

1. owner-approved script, page contract, and approved references;
2. this playbook;
3. `PROMPTING.md` for builder-only prompt construction;
4. the current page's three siblings: intent, builder prompt, critic card;
5. case studies, which are evidence rather than instructions.

The script and page contract are owner-controlled. Agents may not edit them to
make generation easier. Model-compensation geometry belongs only in a builder
prompt. No prompt, candidate, audit, critic preference, or historical example
may silently rewrite story facts.

All production images use the subscription-backed Codex in-app generation path.
An API key, bundled image CLI, or separately billed fallback requires explicit
owner approval in the current conversation.

## 2. Preparation gates

Do not start page generation from an outline. Lock:

- a complete page-by-page script with exact text, speaker/source, causal order,
  silent visible roles, and the reason to turn each page;
- a page contract identifying mode, dominant event, decisive continuity, and
  reader entering/exiting state;
- character identities, setting locks, and consequential objects;
- the output canvas, proof sizes, style anchors, QA paths, promotion ledger,
  reader target, and approximately ten-page batch boundaries.

### Script and readability

A fresh complete-script critic reads the whole sequence, not isolated scenes.
It checks character knowledge, causal transitions, body/time/travel/document
mechanics, natural dialogue, speaker presence and order, and whether a normal
first read supports an accurate plain-language paraphrase. “Recoverable after
rereading” is a revision signal. Add words, panels, prose, or pages when they
create causality and emotional duration; terseness is not a virtue by itself.

### Casting and references

A separate critic judges casting as a system. Test likely lookalikes together
in neutral shared lineups, face crops, silhouettes, grayscale, varied lighting,
profiles, reactions, age/disguise states, and the hardest live pairings. Build
separation through skull, jaw, nose, eye, hairline, apparent age, body mass, and
posture—not costume color alone. Approve recurring setting and story-object
locks only when their continuity actually carries reader understanding.

Preparation gates are non-transitive: script approval does not approve casting;
reference approval does not approve pages; page approvals do not approve an
uninterrupted sequence.

### No throwaway prototypes

Do not generate prototype story pages, academic exercises, or noncanonical
page proofs. Validate a risky page type on the first real page that needs it;
if approved, promote that exact candidate. A previously approved, script-faithful
image may be reused when the owner directs, regardless of an old folder name.

## 3. The three page siblings

Derive three separate artifacts from the owner script:

- **Reader intent:** what happens, who owns the page, what changes, and why the
  reader turns. It contains no generation directions or reference manifest.
- **Builder-only prompt:** exact strings and ownership, essential action,
  minimum approved references, moderate staging, style/output constraints, and
  consequential exclusions.
- **Numbered critic card:** short reader-facing failure criteria derived from
  script plus intent—not from builder prompt compliance.

The prompt and builder audit never travel to the critic. The card never becomes
a list of every instruction used to generate the image.

## 4. Roles and context boundaries

### Builder

Use one fresh builder per candidate. It reads only the compact builder packet
and listed approved references. It produces one complete flattened page, saves
the exact issued prompt, records a concise non-gating audit, derives 600x900 and
768x1152 proofs, hashes the image files, and submits.

Every technically valid completed candidate reaches the critic. The only
pre-critic rerun is a failed generation: wrong canvas, corrupt/truncated output,
or gross focal anatomical breakage. Missing text, attribution, identity,
continuity, hierarchy, prompt variance, typography, margins, and cosmetic
finish are critic questions, not builder reroll authority.

Lettering and captions are baked into the flattened page. Never repair a page
with HTML/SVG overlays, crop patches, composites, swapped balloons, or post-hoc
relettering. Treat attribution as blocking: speaker order, side, vertical tier,
and tail/source endpoint must make ownership clear.

### Critic

Use one fresh zero-history critic per candidate. Stage 1 exposes only a neutral
candidate and reduced proofs, using names that reveal no version or history.
The critic records the event, dramatic owner, turn, and every visible string
with attribution. Stage 2 opens only exact script, reader intent, and numbered
card.

The critic is a reader-facing release gate, not a defect collector. A visible
issue blocks only when it materially harms the page event, exact comfortable
transcription/order/attribution, named identity, consequential continuity,
focal integrity, or dominant dramatic relationship. Repeated anonymous faces,
minor background hands, tiny non-story props, exact hue/coordinates/panel
shares, prompt variance, and numeric type targets are nonblocking when the
reader event survives. Exact comfortable blind transcription from the 600x900
proof is the complete lettering-size test.

Every `REVISE` finding must cite one numbered criterion and state:

1. the visible observation;
2. the material reader harm;
3. why that harm is substantial enough to risk replacing the entire page.

If the redraw justification cannot be made concretely, approve and omit the
minor observation. The critic never edits, generates, promotes, or writes the
next prompt.

### Orchestrator

The orchestrator is nonvisual. It derives state from disk, assembles compact
packets, checks candidate files, builds the version-neutral review capsule,
validates the critic report, routes numbered findings, promotes approved bytes,
updates the ledger, and releases the next page. It never substitutes its own
art judgment for the critic and never treats an invalid report as permission to
regenerate.

Only one page is in flight. Generation never outruns promotion. Rejected art is
evidence and never a reference. Wait once for each dispatched role; do not poll,
read transcripts for progress, or narrate unchanged state.

## 5. Retry router and holds

The numbered criteria are stable defect signatures:

1. `v1 REVISE` → targeted `v2` using the current prompt and validated report.
2. A criterion repeated on `v1` and `v2` → clean `v3` prompt/composition reset
   from locked intent, exact strings, facts, and references—not earlier prompt
   wording or rejected art.
3. That repeated criterion surviving the clean reset → resistant-defect owner
   hold before `v4`.
4. If `v2` contains only new criteria, `v3` is targeted; a `v2`/`v3` repeat may
   receive the clean reset at `v4`.
5. Any `v4 REVISE` → owner hold. Never generate `v5`.

After three failed critic rounds, propose splitting the page before adding a
sixth panel, but do not redesign, split, or change page count without owner
direction. An owner tolerance is recorded beside the critic report; it never
rewrites the critic's historical verdict.

## 6. Promotion and milestone gates

On unconditional approval, copy the candidate byte-for-byte into `pages/`,
verify the SHA-256 match, derive promoted proofs, append the ledger, and only
then release the next page. Run the mechanical verifier once per promotion.

At approximately ten-page boundaries, stop the batch and use fresh independent
reviewers for:

- uninterrupted sequence and emotional continuity;
- script-blind cold reading at reduced size;
- identity, setting, object, and style continuity.

Start the next batch in a brand-new orchestrator task from one compact handoff.
At the final partial batch, add whole-book and release gates. Sequence findings
must name pages, reader harm, and why full-page replacement is warranted;
cosmetic drift alone does not reopen promoted work.

## 7. Reader and publication

Reader/publication is a separate bounded task after story art closes. It may
build navigation, contents, bookmarks, zoom, ending, quiz, catalog integration,
and deployment checks, but it may not alter story artwork. Ending and quiz are
non-story routes such as `#end` and `#quiz`, never invented Page 50 states, and
only real story pages may be persisted as reading positions.

Use one implementation builder, deterministic verification, and fresh reader
critics with an explicit correction ceiling. Publish only after local approval,
then verify the public catalog, assets, routes, quiz, links, console, and 404
behavior.
