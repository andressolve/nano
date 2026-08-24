# Dialogue Studio Pre-production Standard

This is the canonical bridge from owner-approved adaptation to story-page
production. It generalizes the workflow proven in `monte-cristo-vol2/`:
`07-PAGE-CONTRACT.md`, `08-FULL-SCRIPT.md`, `09-REFERENCE-PLAN.md`,
`10-CRITIC-OPERATIONS.md`, `11-PRODUCTION-TOPOLOGY.md`, the compact
`qa/_plan/` page files, and the intent-first packets. Those artifacts are
evidence; this standard and project-local locked authority govern new works.

Pre-production is complete only when the story can be executed page by page by
fresh roles without reopening sources, inventing dialogue, guessing continuity,
or loading the whole book into a one-page task.

## 1. Two non-transitive gates

The gates answer different questions:

1. `check_adaptation.py`: is the complete story, graphical direction,
   panel-by-panel script, page contract, and whole-script readability result
   owner approved at exact hashes? A clean result opens bounded reference
   preparation only.
2. `check_preproduction.py`: are casting, settings, consequential objects,
   approved reference bytes, every intent/prompt/card sibling, context map,
   production authorization, and compact handoff complete and hash-bound? Only
   this clean result opens story-page production.

Story approval does not approve casting. Casting/reference approval does not
approve page production. A page approval does not approve a sequence. No file
may claim that an earlier approval silently crossed one of those boundaries.

## 2. Production-complete full script

Write one locked `script/FULL-SCRIPT.md` in page order. Every page declares
mode, entering state, dominant event, exiting state, reason to turn, and panel
count. Every numbered panel declares its causal purpose, setting/time, all
visible characters including silent roles, action, reader order, continuity,
reader inference, and every exact rendered string with kind and owner. Silent
panels say `NONE`; summaries such as “they argue” are not production scripts.
Modes are limited to `DRAMATIC`, `ILLUSTRATED_PROSE`, and
`SPECTACLE_SILENCE`; exact-text kinds are limited to `DIALOGUE`, `CAPTION`,
`NARRATION`, `SOUND`, `LETTER`, and `OBJECT`. Unknown fields, empty owners, or
builder/reference/history instructions invalidate the script.

The script owns exact text and story facts. It never embeds generation
references, correction history, model compensation, or critic suggestions.
Changing page count, dialogue, action, or causal state invalidates the
readability result, owner hashes, every sibling hash, and both gates.

## 3. Whole-script readability builder–critic loop

The script builder reads the locked adaptation and architecture and may revise
the script and contract together. It never approves its own work.

A fresh critic reads the complete script in order, not a representative scene
or isolated page. Before maker rationale, it records a plain-language first
read and checks:

- character knowledge, desire, causal transitions, and reasons to turn;
- body, time, travel, setting, document, and consequential-object mechanics;
- speaker presence and order, natural read-aloud dialogue, and distinct voices;
- emotional duration, density, breathing, and text that would require
  rereading;
- every page's entering/event/exiting state and accurate paraphrase.

“Recoverable after rereading” means `REVISE`. The final
`preproduction/READABILITY-REPORT.md` names the exact full-script hash, covers
every page, records a byte-bound allowlist capsule containing only the script
and contract, says `APPROVED`, and has exactly `NONE` findings. Any script
change requires a fresh complete-script review.

## 4. Page contract

`contract/PAGE-CONTRACT.md` contains one row-like block per script page. It
declares mode, entering state, dominant event, decisive continuity, exiting
state, reason to turn, location count, and panel count. Shared fields must match
the script exactly. Exact dialogue remains only in the script.

The contract is a reader-state and execution boundary, not a geometry rubric.
Panel shares, coordinates, and numeric lettering targets may guide a builder
prompt but never become rendered-page gates. More than two locations is
blocked; a second dramatic turn returns to story design rather than prompt
patching.

## 5. Complete page siblings

Before page production, every page has three locked sibling files:

- `intent/page-NN.md`: event, dramatic owner/relationship, state change,
  essential causality, and deliberately subordinate detail. It contains no
  references, maker/builder instructions, discarded-attempt history, or
  generation instructions, and records `CURRENT_PAGE_STORY_ONLY`.
- `prompts/page-NN.md`: builder-only use case, minimum approved references,
  event, ordered moments, every exact string and owner, concise style/output
  constraints, consequential exclusions, demoted detail, and native completion
  requirements. Renderable-text directives exist only in its exact-text section.
- `cards/page-NN.md`: three to eight page-specific reader failure criteria
  with stable numbers, category, blocking reader harm, and explicit
  nonblocking tolerance. It contains no prompt, audit, reference manifest,
  version, history, rejected art, panel-share rule, or type measurement.

All siblings bind the exact full-script and contract hashes. The card also
binds its intent hash. The checker requires every page, exact prompt
text/ownership parity with the script, approved-reference parity with the lock
manifest, and the required `EVENT`, `TEXT`, and `INTEGRITY` critic
categories.

## 6. Casting, settings, objects, and references

Lock `CASTING-LEDGER.md` before making references. Design separation through
skull, jaw, nose, eye, hairline, apparent age, body mass, posture, silhouette,
and behavior—not costume color. Record recurring identities, silent roles,
age/disguise states, reserved identity stacks, and a collision matrix.

Lock `SETTING-OBJECT-LEDGER.md` for geography, time, recurring settings,
consequential objects, and their page-to-page state. Decorative accuracy does
not become a continuity obligation.

`REFERENCE-PLAN.md` maps only necessary identity, setting, object, style, and
immediate-continuity locks to pages. The fresh reference critic first reads
neutral artifacts as a system, using shared lineups, face crops, profiles,
silhouettes, grayscale, varied light, reactions, age/disguise states, and the
hardest live pairings. It then opens the ledgers and plan. Lookalike boards are
critic-only and never negative image inputs. Rejected art never becomes a lock.
The report records
`Context receipt: NEUTRAL_ARTIFACTS_THEN_LOCKED_AUTHORITY_ONLY`; generation
prompts, builder audits, and rejected history invalidate the reference review.
The locked plan itself may not carry those materials either.

Only unconditional approval permits byte-for-byte promotion under
`refs/approved/`. `REFERENCE-LOCKS.toml` records each path, SHA-256, kind,
binding purpose, and page set. `REFERENCE-REPORT.md` binds the ledgers, plan,
and lock-manifest hashes and ends with `NONE` findings.
It also binds one allowlist-capsule hash over the ledgers, plan, lock manifest,
and approved reference bytes actually reviewed.
Neither independent critic may be the manifest owner. An `APPROVED` report
containing material failure language is mechanically contradictory and blocked.
The image-free zero-reference state exists only for the rehearsal fixture; a
real project needs at least one byte-verified approved lock bound to every page
before production. Unused locks and empty page-binding lists do not qualify.

## 7. Owner decisions

`adaptation/OWNER-APPROVAL.md` binds page count plus exact audience,
adaptation, architecture, graphical direction, audience-report, greenlight,
script, contract, and readability hashes. `Approved by` must match the owner
named in `manifest.toml`. It opens reference preparation only.

After reference and packet approval,
`preproduction/OWNER-PRODUCTION-APPROVAL.md` separately binds the script,
contract, readability, casting, setting/object, reference plan, reference
report, reference locks, context map, and combined page-packet digest. Its
authorization must be exactly `PAGE_PRODUCTION`. Tolerated risks are explicit;
they never rewrite critic history, and the approver must again match the
manifest owner.

## 8. Context boundaries

Use fresh roles and disk artifacts:

| Role | Reads | Never reads/does |
|---|---|---|
| Script builder | locked adaptation, architecture, visual direction | self-approve, generate images |
| Readability critic | complete script and contract | builder history, sources, references, prompts |
| Packet builder | one page block, its contract block, visual direction, binding map | neighboring pages unless continuity requires one compact fact; sources; rejected history |
| Casting/reference builder | casting and setting/object ledgers, reference plan, approved anchors | edit story authority, approve outputs |
| Reference critic | neutral artifacts first; then ledgers, plan, numbered gate | generation prompts, audits, rejected history |
| Production orchestrator | clean receipts, production approval, compact handoff, current page packet | research, whole-book context, visual judgment, story edits |

The complete script stays whole on disk, but assembly extracts only the current
page block. A page critic sees neutral proofs first and then only that exact
page block, intent, and card. `CONTEXT-MAP.md` records these boundaries
project-locally. Both assembly and preflight rerun the pre-production gate and
reject missing contracts, cross-wired page siblings, stale project authority,
or any byte outside the three canonical transport envelopes.

## 9. Deterministic handoff

`PREPRODUCTION-HANDOFF.md` is the one active resume point. It records both
gate states, exact page count, packet digest, production-approval path/hash,
first page, batch boundaries, open holds, and the next bounded action. It
passes disk state, never task transcripts. Its closed canonical envelope rejects
extra prose or appended instructions. A ready real project has one exact next
action: assemble and preflight Page 01 only from the locked current-page packet.
READY requires `Open holds: NONE`; its batch ranges are derived mechanically in
ten-page chunks, never replaced by an all-pages instruction.

After production begins, a page may use only its immediate promoted predecessor
for continuity. The predecessor must be a complete PNG whose bytes match the
single `production/PROMOTION-LEDGER.toml` record and hashed, closed
`production/page-NN/PROMOTION.md` receipt. The receipt records independent
critic approval, owner approval, and release of only the immediate next page.

From the project directory:

```sh
python3 -B ../../tools/preproduction_receipt.py .
python3 -B ../../tools/check_adaptation.py .
python3 -B ../../tools/check_preproduction.py .
```

The first command prints stable hashes for the two owner records without
granting approval or writing files. Only the final command's exact
`PREPRODUCTION READY FOR PAGE PRODUCTION` result permits
`SESSION-START.md` to assemble Page 01. A failure stops; it never authorizes a
best-effort production run.

`works/sample-dialogue/` is explicitly marked `fixture = true`. Its second
authorization is `FRAMEWORK_REHEARSAL`, never `PAGE_PRODUCTION`; it retains no
run, review, reference, proof, page, or image artifacts. Real projects cannot pass this gate without the separate
`PAGE_PRODUCTION` owner authorization.
