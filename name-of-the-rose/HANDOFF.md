# HANDOFF — The Name of the Rose, Book One

**Last updated:** 2026-05-24 (eighth update — user-led audit pass complete. Six pages regenerated (P4, P8, P10, P17, P18, P20) with text-clarity / bubble-order / composition fixes. **P10 still flagged — composition awkward, needs another regen in fresh session.** Reader (`index.html`) built and quiz written. Landing card + memory retrospective deferred to next session for handoff.)

## ⚡ FRESH-SESSION ENTRY POINT (read this first)

**State at this handoff:**
- Reader done: `name-of-the-rose/index.html` — 25 images wired, persistent bells-strip footer (Matins → Compline), end interstitial, 5-question quiz with shuffled correct positions (b, c, b, c, b) following CRITICAL QUIZ RULE.
- ✅ Page repairs landed this session (kept v1 siblings for all six):
  - P4 — bier added in background (still ambiguous but accepted)
  - P8 — Jorge / William / Jorge bubble reading order corrected
  - P10 — three fixes (body upended with arm hanging, William looking at blackened fingertips, Abbot bubble clearer) — **but composition still awkward; user flagged at handoff. Regen this first in next session.**
  - P17 — Berengar-stole-the-spectacles explanation rewritten for clarity
  - P18 — cloister conversation bubble order corrected
  - P20 — Severinus stacked-centerline bubble layout
- 🟡 **P10 needs another regen.** The dead body in the barrel reads as cartoonish feet-up + a "handshake" with the dangling arm. Try: only the dangling arm visible (blackened fingertips), body completely concealed inside the barrel under linen (no feet sticking up), William crouched outside the barrel reading the hand from below, Abbot opposite with the cross, Adso behind. Keep `page-10-v1.png` AND `page-10-v2.png` (current accepted-but-awkward) on disk. New regen becomes `page-10.png`.
- 🟡 Liturgical-hours gloss — deferred to reader-side, already shipped as persistent bells-strip footer in `index.html`. No image regens needed.
- ⏳ **Remaining ship steps** (do these after the P10 regen lands):
  1. Add landing card to `~/Documents/nano/index.html` (thumbnail = `pages/page-00-cover.png`, tags: graphic novel, mystery, medieval, literary-adaptation, illustrated). See HOA / Newton / da Vinci cards for pattern.
  2. Update `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md` — mark Name of the Rose as shipped in the Story Inventory table; note "in-image Latin always has an English helper" as project-wide rule; note 4-prototype + 20-bulk pattern validated outside biography mode; bump cost-envelope (~$8.61 with the six repairs, $0.84 over the $7.77 envelope, similar to Newton vol 2).
  3. Write `memory/project_name_of_the_rose_retrospective.md` (template per the existing retrospectives — what worked single-shot, what the new canonical rule bought us, the cost envelope, plant for Book Two).
  4. Do NOT commit — wait for explicit user request.

**Budget watch:** through this session ≈ $8.61 (41 image calls × ~$0.21). One more P10 regen → ~$8.82. Inside the Newton-vol2-precedent overrun.

**Reader pattern note:** the `index.html` adds a persistent bells-strip footer that lists all eight canonical hours (Matins · before dawn / Lauds · sunrise / Prime · 6am / Terce · 9am / Sext · noon / None · 3pm / Vespers · sunset / Compline · before sleep). It hides on the end-interstitial and quiz pages. Page-info label sits above the bells-strip. This resolves the user's audit question on Vespers/Matins/Lauds without an image regen.

## ⚠️ MODEL LOCK — do NOT use Google

**Use `mcp__openai-image-2__{generate_image,edit_image}` (gpt-image-2 standard) for every repair in this volume.** User explicitly reconfirmed at handoff: **NOT Google Gemini.** All 35 calls in this volume have used gpt-image-2 standard.

- ✅ Pages without locked characters: `mcp__openai-image-2__generate_image`
- ✅ Pages with one locked character: `mcp__openai-image-2__edit_image` (attach the ref)
- ✅ Multi-character pages: `mcp__openai-image-2__edit_image` anchored on the harder secondary face, describe the protagonist richly in prose. (No `compose_images` on gpt-image-2.)
- ❌ Do NOT swap to `mcp__gemini-pro-thin__*` even if a page fails. Repair on gpt-image-2 instead. Flag explicitly to user before any model swap.

## Status

**All 25 images generated and on disk** (`pages/page-00-cover.png` + `pages/page-01.png` through `pages/page-24.png`). All 8 refs in `refs/`. Cost ≈ **$7.35** of $7.77 envelope. **Zero retries across the 20-page bulk batch** (Wave 1 + Wave 2 both landed single-shot using the template locked from the 4 prototypes).

**Action card for the next session is at the bottom of this doc.** Headline: user is doing a visual-audit pass on the 25 images, then the next agent should go page-by-page, flag anything that needs repair, repair on `mcp__openai-image-2__edit_image`, then build the reader.

### Generation history this volume

| Round | Date | What landed | Calls | Cost |
|-------|------|-------------|-------|------|
| Refs | 2026-05-23 | 8 refs (William / Adso / Abbot / Jorge / Salvatore / Gui / village girl / Aedificium) + 1 girl moderation retry | 9 | $1.89 |
| Prototypes | 2026-05-23 | P2 / P13 / P15 / P24 + 1 P24 v2 (English helper column folded in mid-session) | 5 | $1.05 |
| Wave 1 | 2026-05-23 | P1, P3, P4, P5, P6, P7, P8, P9, P10, P11 — all single-shot | 10 | $2.10 |
| Wave 2 | 2026-05-23 | P12, P14, P16, P17, P18, P19, P20, P21, P22, P23 — all single-shot | 10 | $2.10 |
| Cover | 2026-05-24 | `page-00-cover.png` — gilt title block, Aedificium with corner-towers, dawn band at horizon, two tiny mounted figures on the switchback road, Eco credit | 1 | $0.21 |
| **Total** | | **35 calls** | | **≈ $7.35** |

**Budget remaining for repairs:** ~$0.42 (about 2 repair calls before the ~$7.77 envelope is breached; if more are needed, just flag — Newton vol 2 had a similar envelope and shipped clean).

### Wave-by-wave audit notes (first pass, by the agent that ran them)

These are the agent's own quick reads, not the user's audit. Use them as a starting point — they may be wrong, and the user's review trumps them.

**Wave 1 (P1, P3–P11):**
- P1 (frame opener): illuminated folio, fox-in-monk's-habit marginalia at lower corners, "I" historiated initial with the tiny abbey-in-snow, OLD ADSO at the writing-desk, Latin Gospel of John verbatim with English helper, ~170-word old-Adso narration caption renders. Strong.
- P3 (Aedificium first sight): William + Adso scale + posture clean, tower dominates. Tower architecture reads as a Romanesque abbey complex; possible nit — the four-corner-towers + octagonal core could be more emphatic.
- P4 (Abbot meeting + bier): three speech bubbles render, bier visible in the background as a covered shape, top + bottom caption render verbatim, Abbot's garnet cross prominent.
- P5 (scriptorium hybrid): left-half painted scriptorium with Adso + empty Adelmo desk, right-half parchment panel with gilt-and-lapis "A" initial and all ~140 words readable.
- P6 (refectory): five name labels readable, faces distinct, William seated next to Adso, top caption verbatim. Possible nit — verify each labelled monk matches the described visual (Malachi gaunt + key-ring, Berengar plump + blond, Severinus stained hands, Salvatore two-color eyes + half-grin, Remigio heavy-set).
- P7 (library forbidden): Malachi (key-ring) vs William at the red curtain, three bubbles + top caption render. Atmospheric dusk.
- P8 (Jorge laughter debate): Jorge's milky blind eyes hold against the candlelight, William opposite, Adso half in shadow behind, all three speech bubbles + top + bottom captions render.
- P9 (Day 2 chapter break): illuminated, fox marginalia, "D" initial with fist-from-barrel-rim, central pigsty miniature with legs above the barrel rim, Latin "Dies secundus" blackletter + English helper + bottom caption.
- P10 (Venantius pig blood): Abbot center, William at the barrel with sleeve rolled examining the BLACKENED-FINGERED hand, Adso behind, legs in the barrel — body never explicit. Caption + two bubbles render.
- P11 (coded manuscript): zodiac row across top (verify all 12 glyphs are correct + in order), Latin cipher centered with English helper ribbon below, William's marginal Latin note + helper ribbon, William's spectacles held above the page in lower-left corner, top + bottom caption.

**Wave 2 (P12, P14, P16–P23):**
- P12 (labyrinth first attempt): LEONES carved above the doorway + helper ribbon both render, William + Adso with candle, depth into rooms beyond, top + speech + bottom caption. Mirror element subtle but the doubled-silhouette effect reads.
- P14 (Day 3 chapter break): illuminated, fox marginalia, "T" initial with hunched-figure-by-fire, Salvatore + Adso firelit miniature, Latin "Dies tertius" blackletter + English helper + bottom caption. Verify Salvatore's two-color eyes hold in the small miniature.
- P16 (Adso meets girl): tone exactly right — peasant directness, no romanticization, dim kitchen lit by lamp + hearth coals + Adso's candle, cellarer's door slightly ajar with strip of snow-light, top + speech + bottom caption render. No moderation issue.
- P17 (Berengar bathtub): restraint held — body half-glimpsed under linen and dark water, blackened-fingered arm draped over the tub edge, William crouched reading the evidence with spectacles back on, Adso visible at the doorway, top + two bubbles + bottom caption render. Empty spectacle case on the floor.
- P18 (cloister method): Romanesque arcade chiaroscuro, William + Adso walking, central garden with stone fountain, all four bubbles + top + bottom caption (with the Roger Bacon / Ockham / "science" line) render.
- P19 (Day 4 chapter break): illuminated, "V" initial with the riders-up-the-snowy-road, central miniature of the Dominican-and-soldier procession, fox marginalia, Latin "Dies quartus" + English helper + bottom caption.
- P20 (Severinus poison): Severinus with green-stained hands pointing at the open herbal page (tall thin plant with dark berries), William with spectacles leaning in, clay jar between them. Top + two bubbles + bottom caption.
- P21 (delegation + girl seized): big multi-character page — Gui anchored at center walking with his leather-bound manual, Dominican delegation around, two captives (girl + Salvatore) being dragged through the snow in upper-right, Adso at the cloister window upper-left. Top caption + two speech bubbles + bottom caption all render. The composition held — biggest risk on this volume and it landed.
- P22 (three orders teaching, hybrid): left-half three-figure portrait (BENEDICTINE / FRANCISCAN / DOMINICAN with feet-labels readable), right-half ivory parchment panel with gilt-and-lapis "I" initial and all ~150 words of the three-orders explainer.
- P23 (William explains Gui at night): Adso on his bed wrapped in a blanket, William on a low stool leaning forward holding spectacles, beeswax candle on the wooden chest. All five speech bubbles + top caption + bottom caption render.

**Cover:** gilt-with-red-inner-shadow title block dominates the upper third, "Book One: The Abbey" subtitle directly below, "after the novel by Umberto Eco" credit lower-left. Aedificium with four corner-towers + octagonal core, dawn pink band at horizon, dark pines + snow + mist around tower base, two tiny mounted figures (one in brown, one in black) on the switchback road — readable as figures-in-landscape, not portraits.

## Lessons from this volume (folded into skill + bio.md on ship)

These are durable, not session-specific. Worth keeping accessible for the next biography.

- **In-image Latin always has an English helper** (new canonical rule, already in `01-STYLE-GUIDE.md`). Chapter-break tags, primary-source columns, in-scene signage, Latin speech bubbles — every case now has a documented helper treatment. Applied uniformly across the four chapter breaks, P11 (cipher + marginal note), P12 (carved LEONES), P15 (Salvatore Latin bubble), P24 (Practica bilingual columns). Held single-shot.
- **The 4-prototype + 20-bulk pattern held perfectly on a non-biography volume.** Newton / Honda / da Vinci all hit single-shot bulk-batching on biographical content. Name of the Rose is the first non-biography in this register (a literary adaptation), and the same pattern worked — both 10-page parallel waves landed single-shot, zero retries. The discipline isn't biography-specific; it's "oil-painting register + locked character refs + canonical six-block prompt + prototype-validate-then-bulk-batch."
- **gpt-image-2 standard quality `high` 1536×1024 with the six-block prompt order is durable across literary, biographical, and teaching-page registers.** Same model, same size, same scaffold, same template — three different genre registers (Newton biography, Honda biography, da Vinci biography, Name of the Rose adaptation) all shipping clean.
- **Multi-character page on a real-historical face works when anchored on the visual, not the name.** P21 (the delegation page) is the most complex page in this volume — Gui + two captives (Salvatore + girl) + Adso at the window + delegation behind — and the lock-the-visual-not-the-name discipline (no "Bernard Gui" in the prompt, describe the Dominican habit + hooked nose + iron-grey hair + Practica book) carried it single-shot.
- **Hybrid teaching-page format, validated twice:** P5 (scriptorium-making-of-a-book) and P22 (three orders) work on the same scaffold as P13 INTERLUDE and P15 — left/right halves, painted edge as gutter, gilt-and-lapis decorated initial, ~140–165-word parchment panel. The format absorbed both a portrait-row (P22) and a single-scene (P5) without drift.
- **Cover-as-establishing-shot with title block as the only large text is durable.** Same pattern as Newton / Honda / da Vinci covers. The gilt + deep-red inner shadow on display serif renders cleanly when there's no other large text competing with it.

## Repair pipeline (use only if user audit flags drift)

For each flagged page:
1. Re-read the script entry in `04-SCRIPT.md` to confirm the verbatim text and composition.
2. Re-read the prompt from this HANDOFF or rebuild from `01-STYLE-GUIDE.md` (six-block order: Style → register → anti-drift → character lock → composition → lettering → restrictions).
3. **Keep the existing page as a sibling** (`page-NN-v1.png`) before regenerating — do not overwrite a sibling until the user approves the replacement. (Precedent: `page-24-v1-no-english.png` kept on the disk.)
4. Repair on `mcp__openai-image-2__edit_image` if the page locks a character; `generate_image` if not. **Do NOT swap models.**
5. Same size (`1536x1024`), same quality (`high`), same standard mode.
6. Cost per repair: ~$0.21. Budget remaining ≈ $0.42 → 2 repairs comfortable. If more needed, flag to user (Newton vol 2 had a similar envelope and shipped clean — small overruns are fine if user OK).

## Common drift to look for (per-page checklist for the audit pass)

- **William:** riveted-leather spectacles (NOT modern wire-frame), brown Franciscan habit, rope belt with three knots, reddish-grey tonsure + beard, sharp light-blue eyes. Drift risk: spectacles render as modern frames or as round metal frames.
- **Adso:** age 18, sandy-blond tonsure, smooth beardless face, black Benedictine habit, dark cloth belt. Drift risk: age too young (child) or too old (adult monk).
- **Abbot Abo:** garnet pectoral cross on heavy gold chain, finer-cut black habit, well-fed round face, enameled ring. Drift risk: cross missing or wrong color.
- **Jorge:** milky white blind eyes, ashwood staff, 85 years old, gaunt. Drift risk: eyes render as normal blue/grey.
- **Salvatore:** ONE milky blue eye AND ONE dark eye, knife scar across cheek, half-grin showing missing teeth, sparse red-brown beard, dirty short black habit, bare feet. Drift risk: both eyes the same color, or scar missing.
- **Bernard Gui:** Dominican habit (white tunic + white scapular + BLACK mantle + hood over), iron-grey tonsure, hooked aquiline nose, pale grey-green eyes, leather-bound Practica book at hip. Drift risk: habit color wrong (often renders all-black or all-white), or his name has bled into a generic portrait.
- **Village girl:** rag-wrapped feet (NOT shoes), patched brown wool dress, coarse brown headscarf, faint scratch on cheek, dark eyes. Drift risk: shoes appearing, or face too clean/glamorized.
- **Aedificium:** Romanesque (ROUND arches), four square corner-towers, octagonal core, three storeys, narrow slit windows, slate roof under snow. Drift risk: Gothic pointed arches, modern proportions, only one or two corner-towers visible.

**Period accuracy:**
- Round arches only (no Gothic pointed arches).
- Vellum codices only (no printed books — Gutenberg is 130 years away).
- Riveted-leather spectacles only (no modern metal frames).
- Snow on every exterior shot.
- Breath visible in the cold.

**Text-rendering drift:**
- Latin tags rendered verbatim per script (no paraphrase).
- English helper always present where Latin is meant to be read.
- Speech bubble tails point to the correct speaker.
- No duplicated captions, no spurious text inside captions.

## Pipeline (locked, do NOT swap without flagging)

- **Image model:** `mcp__openai-image-2__{generate_image,edit_image}` — gpt-image-2 standard
- **Aspect ratio:** 3:2 landscape (1536×1024). Biographical-mode default.
- **Style register:** oil-painting realism. NOT a comic. NO halftones, NO cel shading, NO ink linework.
- **Anti-drift directive** (every prompt): "NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting, cinematic composition."
- **Multi-character pages** (no `compose_images` on gpt-image-2): lock to the harder-to-describe secondary face via `edit_image`, describe the protagonist richly in prose with explicit age + signature marks.

## Action card for the next session

**Goal:** finish shipping Name of the Rose Book One.

**Step 1 — Visual audit pass (PRE-AUTHORIZED).** Go through all 25 images (`pages/page-00-cover.png` + `page-01.png` through `page-24.png`) with the Read tool, viewing each. For each, cross-check against:
- `04-SCRIPT.md` for verbatim text and composition
- The per-page checklist above for common drift
- The user's own audit notes (they will provide separately when you land in the next session)

**Step 2 — Repair anything flagged.**
- Keep the original as `page-NN-v1.png` sibling.
- Use the same scaffold (six-block prompt order from `01-STYLE-GUIDE.md`).
- Same tool, size, quality.
- Budget: ~2 repairs comfortable inside the envelope; flag if more needed.

**Step 3 — Build the reader (`name-of-the-rose/index.html`).**
- Pattern matches Newton / Honda / da Vinci / Newton vol 2 readers.
- Dark theme, page-flipping with progress bar.
- Fixed side-arrow nav, vertically centered, click-zone nav, keyboard nav (left/right arrows + space).
- `max-width: min(1400px, 96vw)` on the page image container.
- Lazy-prefetch the next page.
- All 25 images in order (cover → 1 → 24).
- Bottom of reader: 5-question quiz.

**Step 4 — Write the 5-question quiz.**
- Per the **CRITICAL QUIZ RULE** in `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md`: correct answer must NOT be the longest. Distractors substantive (period detail, similar length). Shuffle correct positions across the five questions (mix a/b/c). Test WHY not WHAT.
- Suggested topics, all driven by the book itself:
  1. Why did the Abbot want William to investigate quietly? (papal delegation arriving)
  2. What was the common factor across the three deaths? (a book in the forbidden library)
  3. Why did Bernard Gui ride up to the abbey? (the meeting + the manual)
  4. Why was William's method new? (do not invent angels and demons — simplest cause; Roger Bacon / Ockham → science)
  5. Why was the village girl arrested for witchcraft and not for stealing bread? (the Inquisition framing — the powerful needed her to be a heretic, not a hungry girl)
- All five questions test understanding of WHY, not lookup of WHAT.

**Step 5 — Add landing card to `~/Documents/nano/index.html`.**
- Match the existing card layout in the landing page.
- Thumbnail = `name-of-the-rose/pages/page-00-cover.png`.
- Title, subtitle, short description, tag chips (graphic novel, mystery, medieval, literary-adaptation, illustrated).

**Step 6 — Update memory + write retrospective.**
- Update `MEMORY.md`:
  - Mark Name of the Rose as shipped in the Story Inventory table.
  - Note the new "in-image Latin always has an English helper" canonical rule as a project-wide rule (it's a sibling to the CAPTION CLARITY RULE — same audience-respect logic, different failure mode).
  - Note that the 4-prototype + 20-bulk pattern is now validated outside biographical mode.
  - Bump cost-envelope confirmation: ~$7.35–$7.77 on a 25-image volume with 4 prototypes.
- Write `project_name_of_the_rose_retrospective.md` next to the existing retrospectives in `memory/`:
  - What worked single-shot (the four prototype categories: cinematic / hybrid-map / hybrid-character-scene / primary-source-frame).
  - What the new canonical rule (in-image Latin helper) bought us — readable Latin without breaking the first-time-reader rule.
  - How the 20-page bulk batch landed with zero retries on a literary adaptation (not just biography).
  - Cost envelope landed.
  - Plant for Book Two (the burning of the library, the labyrinth resolved, Adso's farewell to the girl, William's quiet exit) — keep plantable, do not promise.

**Step 7 — Commit (only after user explicit commit request).**
- Per default Claude Code behavior: do NOT auto-commit. Ask the user when the volume looks ready to ship.

## Non-negotiables (from the brief, repeated here so they don't get lost)

- **No sex** in the Adso / village girl scene (P16). Reframed as meeting + sharing bread — confirmed in P16 as generated.
- **Do not soften or skip** the village girl's arrest in P21 — confirmed in P21 as generated.
- **Do not frame the period as "dark" or "ignorant."** Framing is *constrained intelligence*.
- **Do not paraphrase Latin tags.** Render verbatim and translate in caption.
- **Body of Berengar in the bathtub** (P17): half-glimpsed, half-covered, dim morning light. Confirmed restrained in P17 as generated.
- **Adelmo's fall** (P4): referenced via the bier in the background, body not shown. Confirmed in P4 as generated.

## Sibling page on disk (kept intentionally)

`pages/page-24-v1-no-english.png` — the pre-canonical-rule version of P24, kept as a sibling. `pages/page-24.png` is the v2 with the English helper column. Do not delete the v1 sibling without explicit user instruction.

## Where to land in the next session

```
cd ~/Documents/nano/name-of-the-rose
# Read this HANDOFF.md first — has the Action card, the per-page audit checklist,
# the lessons block, and the ship-step list.
# Then ask the user for their visual-audit notes from the review they will have
# done between sessions.
```
