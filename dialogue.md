# dialogue.md — Dialogue-Driven Graphic Novel Playbook

A workspace-wide production playbook for long-form narrative graphic novels
whose story is carried substantially by dialogue, speech balloons, sound cues,
memory scenes, and sequential page-to-page causality.

This playbook was validated on the 55-page `monte-cristo-expanded/` production
run. Its exact source orchestration is preserved in
`monte-cristo-expanded/36-BUILDER-CRITIC-RUN-NOTES.md`.

## Scope

Use this playbook for dialogue-driven literary adaptations, myth/epic stories,
fiction, and other sequential comics where:

- dialogue and captions are baked into generated page images;
- speaker ownership and reading order are load-bearing;
- characters, settings, and story objects recur across many pages;
- the reader must understand causal and emotional transitions without filling
  in missing story;
- a long run benefits from separate builder and critic agents.

Do **not** apply this playbook to biographical graphic novels merely because
they contain some dialogue. The existing biographical workflow in `bio.md` and
the `honda-soichiro/` model remains unchanged and authoritative for that format.

## Core principle

Separate making, judging, and promotion:

- the **builder** makes one practical candidate;
- the **critic** independently judges it;
- the **production lead** controls state, promotion, and release of the next
  page.

The builder must not become a second critic and generate private variants in
search of perfection. The critic must not edit the art. Neither agent may
promote a page.

## Required authorities before production

Lock these before starting the page run:

1. an approved page-by-page script with exact text and story order;
2. a character identity ledger and approved reference images;
3. setting and decisive-object references where continuity matters;
4. a style guide and accepted canonical style anchors;
5. the output format and actual reader targets;
6. a QA directory and canonical `pages/` directory;
7. the batch boundaries for uninterrupted sequence review.

The script is the highest authority. A prompt, candidate, builder preference,
or critic preference cannot rewrite it silently.

## Pre-production critic gates

The Monte Cristo run did not wait until finished pages existed to introduce an
independent critic. Separate critic passes were used for the script, character
references, and the continuous prototype. Keep these gates separate: each one
answers a different question, and none grants automatic approval to the next
kind of artifact.

### Complete-script critic

The first full-script critic cold-read the entire script in order before
consulting the production mandates. It then checked:

- character knowledge against what that character had actually learned;
- body, document, travel, time, and financial mechanics across pages;
- every page-to-page causal transition;
- speaker presence, balloon order, side, silence, and tail/source maps;
- movement-level comprehension for a first-time reader;
- whether the language could be followed by the actual age range.

Approval was withheld until the complete revised script was resubmitted and
all original blockers were re-audited. Script approval explicitly did not
approve any rendered page.

After reader QA exposed technically decodable but effortful storytelling, the
same complete-script gate was strengthened. The critic re-read all pages and
all transitions for effortless first-read orientation, natural dialogue,
dominant dramatic turns, complete causal chains, over-terse or ambiguous
lines, tiny-prop dependencies, emotional duration, and the ability to
paraphrase what happened after one normal read. The script could add words,
panels, prose, or pages; low word count was not rewarded. The critic gave a
concrete repair for each blocking finding and withheld approval through
successive full or targeted verification rounds until the whole script passed.

### Character-reference critic

The reference critic judged casting and anti-collision before page production.
It did not ask whether individual portraits were attractive. It tested whether
recurring characters remained instantly distinguishable through:

- costume-free face crops;
- full-body silhouettes and grayscale value patterns;
- warm, cold, and near-black lighting;
- profile, three-quarter, and reaction views;
- age progression, beard growth, formal dress, and deliberate disguise;
- same-panel opposition, silent memory insets, long absences, mobile size, and
  page-thumbnail size.

The critic built a collision matrix, named blocking near-neighbor pairs,
identified missing recurring-role locks, and required explicit positive locks
and forbidden-lookalike rules. After redesign, it independently re-inspected
the native reference sheets, neutral full-cast boards, grayscale silhouettes,
adversarial near-neighbor boards, and the hardest live-pair proof. Reference
approval meant only that the casting system was ready to use; it did not waive
identity or attribution review on finished pages.

### Continuous-prototype critic

The first rendered continuous range received a cold read before the critic
consulted its script or internal QA. The critic judged first-read causality,
speaker attribution balloon by balloon, character/role continuity, page turns,
and real reduced-size readability across the sequence. This caught a political
orientation weakness and a balloon visually assigned to a silent memory figure
even though the internal prototype audit had passed.

The useful rule is: prototype a continuous causal range, not isolated glamour
pages, and let the critic encounter it like a reader before showing production
explanations.

### What was not conflated with critic approval

The readability mandate, page-intelligence contract, typography system,
format proofs, builder audits, and QA boards were preparation authorities and
evidence. They helped define or test the work, but their existence did not
substitute for the independent script, reference, prototype, page, or sequence
verdicts.

## Agent roles

### Builder

The builder:

1. reads the authoritative page record and current continuity state;
2. prepares a prompt with exact text, action/panel sequence, speaker staging,
   silent roles, identity locks, story objects, exclusions, and output format;
3. uses the latest approved canonical page plus the minimum required identity
   and object references;
4. generates one complete flattened page with native lettering;
5. performs one practical essentials audit;
6. creates desktop and tablet proofs;
7. submits the candidate without promoting it.

The builder normally stops at the first plausible candidate. It does not reroll
for nominal typography size, tiny margins, exact panel percentages,
microscopic tail distances, phone-only readability, or cosmetic finish.

The builder may replace a candidate before critic review only when it sees an
actual essentials failure such as missing required text, reversed causal order,
wrong speaker ownership, a broken decisive object, or obvious actor/anatomy
failure. The rejected image remains preserved, and the redraw targets only the
named defect.

### Critic

The critic is a separate agent. It receives:

- the candidate path;
- the sibling page-generation prompt;
- the builder audit;
- the desktop and tablet proofs;
- the locked authorities or their relevant page-specific requirements;
- an explicit page-specific checklist from the production lead.

The builder audit is context, not approval evidence. The critic independently
inspects the image and returns its own verdict.

### Production lead

The production lead:

- maintains the authority order and current canonical state;
- writes the builder and critic task briefs;
- distills each page's material script/prompt commitments into the critic's
  page-specific checklist;
- inspects the candidate while the critic works;
- promotes only an unconditional critic approval;
- verifies that canonical bytes match the approved candidate;
- updates the QA ledger, reader, and handoff;
- releases the next page;
- starts batch sequence gates.

## Builder task template

Use this task shape:

> Generate Page NN from the prepared prompt. Generate one candidate, run one
> practical essentials audit, make desktop/tablet proofs, and submit it to the
> critic. Do not reroll for cosmetic or numeric reasons. Stop after the first
> plausible candidate unless there is an actual story, attribution, or anatomy
> failure. Do not promote or edit the reader.

While the critic reviews the current page, the production lead may send:

> Prepare only the Page NN+1 prompt from the exact approved script with the
> minimum references. Hold generation until the current page is approved,
> promoted, and explicitly released. Protect story order, attribution,
> identity, and consequential continuity; avoid cosmetic constraints that
> invite rerolls.

Preparation may overlap review. Generation may not outrun approval.

## Critic task template

Use this core task shape:

> Independently review Page NN under the corrected essentials gate: exact
> script/story, clear attribution, obvious generation/anatomy integrity,
> consequential identity/continuity, and actual desktop/tablet comfort.
> Typography/cosmetic/numeric prompt deviations are nonblocking unless they
> materially harm reading or story. The candidate path is supplied; the prompt,
> builder audit, and desktop/tablet proofs are sibling files. Write a concise
> critic report in the QA folder and return APPROVED or REJECTED/REVISE with
> mandatory findings only. Do not edit or promote the production art.

Append a short, concrete page-specific checklist. This is essential: it puts
the material visual commitments from the script and prompt directly in front
of the critic.

Examples of page-specific checks:

- required action and balloon order;
- which character is left/right and who speaks first;
- where a sound cue falls relative to the response it triggers;
- whether a memory inset is silent and separate from live action;
- continuity and destination of a body, letter, weapon, purse, diamond, map, or
  evidence papers;
- whether an identity change still reads as the same person;
- whether a reveal is withheld until the correct panel or page;
- whether a declared silent actor remains silent;
- whether explicitly forbidden figures, objects, labels, or later-page actions
  are absent.

The critic is not asked merely whether the page looks good. It is asked whether
this image performs this scripted and prompted page.

## Reasonable essentials gate

A finding blocks promotion when it creates a material failure in one of these
areas:

1. **Script and story** — missing, duplicated, altered, or invented text; wrong
   fact; wrong action; reversed cause/response; premature reveal; contradiction.
2. **Page-specific prompt commitments** — a named staging, source, object,
   silence, reveal, handoff, or exclusion that materially carries the story is
   not present in the image.
3. **Attribution** — a balloon, narration field, memory line, or sound cannot be
   assigned confidently to the intended speaker or source on a normal read.
4. **Generation integrity** — an extra, missing, duplicated, or fused actor,
   face, limb, hand, digit, or decisive object changes or disrupts the action.
5. **Consequential continuity** — a recurring identity, setting, costume, or
   story object changes enough to confuse the narrative.
6. **Actual reader comfort** — required text or order is cropped, malformed,
   tiring, or unclear at the real desktop target or secondary tablet target.

These are not independent vetoes when the page remains clear and faithful:

- nominal source-pixel font targets;
- one-to-several-pixel margin differences;
- exact panel percentages or prompt coordinates;
- microscopic tail-to-lip distance;
- minor balloon-shape variation;
- phone-only performance when phone is not the target;
- tiny palette, texture, or finish variation;
- cosmetic preferences that do not change story, attribution, continuity,
  integrity, or reading comfort.

## Critic output contract

The critic must:

1. save a concise report beside the candidate;
2. return `APPROVED` or `REJECTED`/`REVISE`;
3. state only mandatory findings in the blocking verdict;
4. separate nonblocking observations;
5. make no edit, regeneration, promotion, reader change, or file substitution.

Approval means no mandatory defect remains. A recoverable-from-context defect
is not automatically acceptable; the question is whether a normal reader sees
the intended page correctly.

## Revision rule

When the critic returns `REJECTED` or `REVISE`:

1. preserve the failed candidate and report;
2. send the mandatory finding to the builder;
3. change staging or prompt only as needed for that finding;
4. regenerate the complete page;
5. submit the replacement to a fresh critic review.

Never crop-patch, repaint, composite, reletter, tail-swap, or reuse a failed
candidate as a reference. A legitimate correction is not permission for an
unrelated polish pass.

## Promotion rule

When the critic returns `APPROVED`, the production lead:

1. copies the exact candidate into the canonical page path;
2. verifies byte identity;
3. records the accepted version and hash;
4. updates the QA ledger, reader, and handoff;
5. uses the new canonical page as the immediate anchor for the next page;
6. explicitly releases the prepared next prompt.

Rejected pages stay in QA. Only critic-approved pages enter the canonical
sequence.

## Production state machine

```text
approved Page N-1
        ↓
prepare Page N prompt
        ↓
builder: one candidate + one audit + proofs
        ↓
critic: independent image review
        ├── REVISE → preserve → one complete targeted redraw → fresh critic
        └── APPROVED
                 ↓
production lead: byte-identical promotion + reader/QA/handoff update
                 ↓
release Page N+1
```

At most one page is awaiting approval and one next-page prompt is being
prepared. No unapproved image becomes a continuity anchor.

## Batch sequence gate

After each ten-page batch, and after the final shorter batch, give the critic a
separate uninterrupted-sequence task:

> Review the canonical pages as one uninterrupted reader sequence under the
> corrected essentials gate: story and emotional continuity; identity,
> setting, and object continuity; speech/source attribution across transitions;
> obvious generation/anatomy integrity; and actual desktop/tablet comfort.
> Typography pixels, cosmetic polish, and nonconsequential variation are
> nonblocking. Create a contact sheet and concise sequence report. Return
> APPROVED or REJECTED with mandatory findings only. Do not edit or promote art
> or the reader.

The next batch remains held until this gate passes. A sequence gate can find a
cross-page failure that isolated page reviews missed.

## Required evidence per page

Keep these artifacts together:

- generation prompt;
- candidate image;
- builder essentials audit;
- desktop proof;
- tablet proof;
- critic report;
- preserved rejected candidate and correction note, if any;
- approved candidate hash;
- canonical byte-identity confirmation.

At the batch level, keep the contact sheet and sequence-gate report.

## Reference discipline

- Reference the latest approved canonical predecessor, not a failed candidate.
- Add only the minimum identity and decisive-object references needed.
- Use approved contact boards when the image tool's reference limit makes them
  necessary; do not manufacture a new visual interpretation inside the board.
- Treat references as identity/continuity evidence, not as permission to copy a
  rejected layout.

## Anti-patterns

Do not:

- let the builder generate dozens of private variants;
- ask the builder to predict every possible critic objection;
- treat nominal typography or coordinate targets as engineering tolerances;
- let the critic edit, regenerate, or promote;
- approve from the builder audit without inspecting the image;
- omit the page-specific critic checklist;
- generate Page N+1 before Page N is canonical;
- use rejected art as a reference;
- patch one piece of a failed comic page;
- skip batch sequence review because individual pages passed.

## Validated source run

The source implementation is:

- `monte-cristo-expanded/29-PAGES-21-55-BUILDER-CRITIC-WORKFLOW.md`
- `monte-cristo-expanded/36-BUILDER-CRITIC-RUN-NOTES.md`
- `monte-cristo-expanded/30-PAGES-21-30-PRODUCTION-QA.md`
- `monte-cristo-expanded/32-PAGES-31-40-PRODUCTION-QA.md`
- `monte-cristo-expanded/33-PAGES-41-50-PRODUCTION-QA.md`
- `monte-cristo-expanded/34-PAGES-51-55-PRODUCTION-QA.md`

The canonical outcome was 55 complete portrait pages, independently approved
page by page and again at four uninterrupted sequence gates.

*Added 2026-08-08 from the completed Monte Cristo expanded production run.*
