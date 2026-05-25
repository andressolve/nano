# Name of the Rose Vol 2 — HANDOFF

**Status as of 2026-05-25:** Production run complete from this Codex session. Planning docs, refs, cover, all 24 story pages, reader, quiz, and landing-card integration are in place. Not committed or pushed.

**Billing correction for future work:** This production run used the bundled imagegen CLI with `OPENAI_API_KEY`, which means the image calls may be billed as OpenAI API usage rather than covered by the user's Codex/ChatGPT subscription. Do not repeat that. For future image production in this repo, use the Codex in-app image generation path intended for subscription-backed usage. Use API-key CLI/direct API image generation only if the user explicitly approves separate API billing in that conversation.

**Production exception:** P19's original self-poisoning caption/speech wording was rejected twice by the image safety filter. The final image keeps the fire/book-destruction beat with safer in-image text; details are logged in `05-PRODUCTION-LOG.md`.

## What's done

All 5 planning docs are written at `~/Documents/nano/name-of-the-rose-vol2/`:

- `00-PROJECT-BRIEF.md` — 25-page window (Days 5–7 + Aged Adso epilogue). 6 illuminated pages (Book One had 4 — user explicitly asked for more). Cost envelope ~$7.35–$7.77. RULE 1/2/3 from Book One retrospective applied from day one.
- `01-STYLE-GUIDE.md` — Delta only over Book One. Two new illuminated tag types (Continuatio Manuscripti, Epilogus). Closing Stat Rosa frontispiece. Dream register (P12 Coena Cypriani). Fire palette (P19/P20/cover). Old Adso continuity-checked against Book One P1's historiated initial.
- `02-CHARACTERS.md` — Delta. Reuse 8 Book One refs. **5 new singles to build:** Old Adso, Remigio, Malachi, Severinus, Aristotle codex. **3 composites to build UPFRONT (RULE 1):** composite_chapter_house_disputation, composite_condemnation, composite_finis_africae.
- `03-SETTINGS.md` — Delta. Reuse 8 Book One settings. 10 new (Matins chapel, catalogue table, Abbot's chamber, mirror door, finis Africae interior, library burning, abbey burning at night, road at dawn, Melk writing-cell, ruins decades later).
- `04-SCRIPT.md` — Full 24-page + cover script. Verbatim lettering for every caption and bubble.
- `05-PRODUCTION-LOG.md` — Image-generation tool path, ref observations, accepted prototype/bulk outputs, P19 exception, and reader/static checks.

Produced assets:
- `refs/` — 5 new single refs + 3 composite refs.
- `pages/` — `page-00-cover.png` + `page-01.png` through `page-24.png`, all 1536x1024.
- `index.html` — Book Two reader copied from the Book One UX pattern, with Book Two page metadata and quiz.
- `../index.html` — landing card and folder-list entry added for `name-of-the-rose-vol2/`.

## User decisions captured

From AskUserQuestion during the planning sub-session:
1. **Ending scope:** Eco-faithful — abbey burns + Aged Adso epilogue. (NOT a soft ending.)
2. **Folder naming:** `name-of-the-rose-vol2/` (parallel to `newton-vol2/`).
3. **More illuminated pages:** Explicit user ask. Book One had 4 (P1, P9, P14, P19); Vol 2 has **6** (P1, P2, P9, P15, P21, P24). Two new tag types — Continuatio Manuscripti and Epilogus — plus closing Stat Rosa frontispiece.
4. **Image production from this Codex session.** User intent was subscription-backed Codex image generation, not separate API-key billing. This run incorrectly used bundled imagegen CLI/API calls; do not use that path again without explicit billing approval.

## Editorial calls already made (don't relitigate)

- **Village girl's burning + Salvatore's + Remigio's executions:** Summarized on P7 parchment panel. NOT rendered on-page. Restraint per Book One moderation lessons.
- **Abbot's death:** Offscreen. Referenced only in Old Adso's narration on P22.
- **Jorge:** Ascetic-dignified-severity, NOT cartoon villain. Tragic-fanatic register.
- **Old Adso:** Continuity-checked against Book One P1's historiated initial (old monk at writing desk in Melk cell). Same hair, same room, same posture register. Do NOT drift.

## Completed production sequence

### Step 1 — Built refs (8 calls)
**5 new single refs** via the current Codex image-generation path:
- `ref_old_adso.png` — continuity to Book One P1's historiated initial
- `ref_remigio.png`
- `ref_malachi.png`
- `ref_severinus.png`
- `ref_aristotle_codex.png` (object ref)

**3 composite refs** via reference-conditioned image editing (RULE 1 — build UPFRONT, do not wait for drift). In this Codex session the bundled imagegen CLI supports repeated `--image` inputs for `gpt-image-2`; use all component refs directly. If a future tool path only accepts one reference image, fall back to anchoring on the trickiest single ref named below:
- `refs/composite_chapter_house_disputation.png` — William + Abbot + Bernard Gui (fallback anchor: `ref_gui.png`)
- `refs/composite_condemnation.png` — Gui + Remigio + Salvatore + village girl (fallback anchor: `ref_gui.png`)
- `refs/composite_finis_africae.png` — William + Adso + Jorge (fallback anchor: `ref_william.png`)

### Step 2 — RULE 2 before every prompt
**Re-Read every involved character ref PNG** and write a one-line verbatim observation per character into working notes BEFORE writing the prompt prose. Never describe from memory. Specifically: Adso is 18, BLOND, TONSURED (shaved crown + side fringe + bangs only), black novice habit, hood down. William has near-bald crown with grey fringe. Get these wrong in prose and the model obeys the wrong prose (Book One P10 burned 4 regens on exactly this).

### Step 3 — Prototypes (5 pages)
Prototyped across format AND density:
- **P3** — multi-character composite test (composite_chapter_house_disputation)
- **P11** — diagrammatic labyrinth-map teaching page
- **P12** — dream register test (Coena Cypriani)
- **P18** — Greek primary-source page (Aristotle's Poetics II as artifact)
- **P24** — closing illuminated Stat Rosa frontispiece

Three-question check on each (same person? right text? right mood?) passed before proceeding.

### Step 4 — Bulk batch
Generated remaining story pages in controlled waves. All accepted except P19 required safety-shaped wording.

### Step 5 — Cover last
Fire palette. Night exterior. Single glowing window — Jorge's library lamp. Accepted.

### Step 6 — Reader + quiz + landing card
- `index.html` with prayer-hours-strip footer from Day One (don't bolt on later). Mirror Book One reader UX.
- 5-question quiz per CRITICAL QUIZ RULE (correct answer NOT longest, distractors substantive, positions shuffled, test WHY not WHAT).
- Add card to `~/Documents/nano/index.html` mirroring existing card style. Append folder name to footer's folder list. Completed.

### Step 7 — Remaining ship tasks
- Update `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md` — move Vol 2 from active to RECENT SHIP, bump landing-page count.
- Write `project_name_of_the_rose_vol2_retrospective.md`.
- Commit + push only when user asks. Stage only project files + landing-page diff.

## Hard rules to NOT violate (from Book One retrospective)

1. **RULE 1 — Composite refs UPFRONT, not panic-fix.** Three composites listed above. Build them BEFORE first edit_image call for any page using them. P10 of Book One burned 7 regens and ~$2.50 because composite was a panic-fix at v6 instead of upfront.
2. **RULE 2 — Re-Read every ref before writing prose.** Don't describe from memory. Don't trust the lock block alone — the ref is the truth.
3. **RULE 3 — Surface tool constraints LOUDLY the moment they're load-bearing.** The Book One production path had a one-reference-image limit. If the current tool path has any reference-input limit, stop, name the constraint to the user once, and use the composite-plate workaround. User's standing instruction: *PLEASE, SURFACE BIG ISSUES LIKE THAT.*
4. **In-image Latin always has an English helper.** Chapter tags, speech bubbles, primary-source pages, carved signage. Ornamental Latin too small to read is decoration and needs no helper.
5. **CAPTION CLARITY — every line stands alone.** No cryptic teaser captions. Period vocab gets inline gloss on first use. Names get one-sentence grounding role on first use. Read every caption aloud, alone, as a first-time reader before finalizing.
6. **Quote-marks-in-bubbles:** Strip wrapping quotes from verbatim strings. Add to lettering block: `DO NOT include any quotation marks inside speech bubbles. The bubble shape is the quote.`
7. **One defect per regen.** Don't bundle fixes.
8. **Don't name the famous figure in the lock block.** Visual description is the lock. The name belongs in the script and the ref filename, not in the prompt the model sees.
9. **Quality `high` only.** Don't downgrade to save cost — caption legibility collapses.
10. **Moderation softening for village-girl pages:** "young Italian peasant" / "weathered by cold and wind" / "patched coarse wool" — do NOT combine explicit-age + thinness + bareness.

## Reusable assets from Book One (`~/Documents/nano/name-of-the-rose/refs/`)

8 single refs reusable directly: `ref_william.png`, `ref_adso.png`, `ref_abbot.png`, `ref_jorge.png`, `ref_salvatore.png`, `ref_gui.png`, `ref_girl.png`, `ref_aedificium.png`. Verify each file exists before passing to image generation/editing (missing refs poison the output).

Existing Book One composites such as `refs/composite_p10_william_adso_abbot.png` are useful as lessons, not as inputs for Vol 2 composites. Do not use the William + Adso + Abbot P10 composite for the `finis_africae` scene; it would import the wrong third character.

## Cost envelope

- 5 new refs × $0.21 ≈ $1.05
- 3 composites × $0.21 ≈ $0.63
- 25 pages × $0.21 ≈ $5.25
- reserve for 2-3 prototype/audit regens × $0.21 ≈ $0.42-$0.63
- **Target: ~$7.55**
- **Risk: composite slippage.** If composites aren't built upfront, expect ~$2.50 overrun per multi-character-page slog (Book One P10 was the proof).

## Open questions to NOT ask the user

These were either decided in the planning sub-session or are agent judgement calls — do NOT re-ask:
- Whether to include the Aged Adso epilogue (yes, user picked Eco-faithful)
- Whether to render the executions (no, restraint — see Editorial calls above)
- Folder name (`name-of-the-rose-vol2/`)
- How many illuminated pages (6, per explicit user ask)
- Whether to use composite refs (yes, RULE 1 — non-negotiable)

## Files to read on fresh-session pickup

In order:
1. This HANDOFF.md
2. `~/Documents/nano/bio.md` (biographical-mode playbook, applies to oil-painting register projects regardless of genre)
3. `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/project_name_of_the_rose_retrospective.md` (RULES 1/2/3 with full context)
4. `~/Documents/nano/name-of-the-rose/01-STYLE-GUIDE.md` (Book One Style Block — Vol 2 style guide is a delta over this)
5. `~/Documents/nano/name-of-the-rose/02-CHARACTERS.md` (reused refs' lock blocks)
6. The 5 Vol 2 planning docs in this folder
