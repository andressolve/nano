# Production QA - Foundation, Part Two

## Status

**All raster, reader, and local catalog gates passed as of 2026-07-26.**

The accepted set contains one cover and 28 story pages, all generated through
the subscription-backed Codex image path with story lettering baked into the
rasters. Every final image was inspected in reading order and independently
dimension-checked at exactly 1536x1024. The Part Two reader, notes, quiz, and
catalog entry passed desktop and 390x844 browser QA. Publication verification
is recorded separately after the release commit reaches GitHub Pages.

## Scope Gate

- [x] Source boundary is Part II, "The Encyclopedists."
- [x] Opening states the fifty-year jump and changed generation explicitly.
- [x] Ending resolves the first balance-of-power crisis.
- [x] Anacreonian troops may occupy empty land, not Terminus City.
- [x] No Apple-only character, Vault mechanic, ship, occupation plot, or event.
- [x] No religion-of-science system or Part Three crisis.
- [x] Part One and the three compressed Foundation folders remain untouched.

## Source and Causality Gate

Before accepting production, recheck the following chain against
`00-PROJECT-BRIEF.md` and `04-SCRIPT.md`:

1. Fifty years have passed; Terminus has become a city and still believes in
   the Encyclopedia mission.
2. Anacreon becomes a kingdom and stops the metal route.
3. Rodric asks for a base, taxes, and land under the word "protection."
4. Hardin's obsolete plutonium request exposes Anacreon's lost atomic science.
5. The Board trusts Imperial protection and the official mission.
6. Dorwin demonstrates both Imperial scholarly stagnation and diplomatic
   evasion.
7. Symbolic analysis shows that the treaty and five days of reassurance promise
   no action.
8. Anacreon's seven-day ultimatum leaves the Vault opening one day earlier.
9. Hardin identifies the deliberate absence of psychohistorians and acts without
   knowing the recording's answer.
10. Lee's coup transfers civic power without bloodshed.
11. Seldon's timed message reveals the Encyclopedia cover, constrained crises,
    and Second Empire purpose without reacting to individuals.
12. Smyrno, Konom, and Daribow oppose exclusive Anacreonian control because
    Terminus alone retains nearby atomic knowledge.
13. Anacreon withdraws; the Foundation survives without battle and begins
    looking outward.

Reject any page sequence that requires the reader to infer one of these links
without text or a visible system.

## Reference Gate

All twenty production references must exist and pass full-resolution inspection
before any dependent story page is generated.

### Identity and group refs

- [x] `refs/ref_hardin.png`
- [x] `refs/ref_pirenne.png`
- [x] `refs/ref_rodric.png`
- [x] `refs/ref_dorwin.png`
- [x] `refs/ref_fara.png`
- [x] `refs/ref_yohan_lee.png`
- [x] `refs/ref_seldon_recording.png`
- [x] `refs/ref_board.png`
- [x] `refs/ref_civic_wardens.png`
- [x] `refs/ref_anacreon_group.png`
- [x] `refs/ref_three_kingdom_envoys.png`

### Environment and object refs

- [x] `refs/ref_terminus_city.png`
- [x] `refs/ref_encyclopedia_building.png`
- [x] `refs/ref_four_kingdoms_model.png`
- [x] `refs/ref_anacreon_arrival.png`
- [x] `refs/ref_atomic_contrast.png`
- [x] `refs/ref_board_and_city_hall.png`
- [x] `refs/ref_dorwin_and_logic_room.png`
- [x] `refs/ref_anacreon_base.png`
- [x] `refs/ref_time_vault.png`

Every ref must pass:

1. Exact 1536x1024 canvas.
2. Expanded Part One visual-register compatibility.
3. Correct face, age, skin tone, hair, build, costume, and object geometry.
4. Distinct recurring silhouettes; no cloned faces within group sheets.
5. No labels, pseudo-writing, watermarks, page numbers, or speech balloons.
6. No Apple-series design language.
7. No split-sheet arrangement accidentally reused as a story-page layout.
8. Seldon's recording preserves the exact Part One identity while changing only
   age-state, seated apparatus, and projection treatment.
9. Four Kingdoms model communicates three states without relying on generated
   map labels.
10. Terminus reads as a functioning small frontier city surrounded by vast empty
    land, not a camp, metropolis, medieval town, or Apple Terminus.

Reference audit record: all twenty files were visually inspected and returned
1536x1024 via `sips` on 2026-07-20. Seldon's recording initially encountered a
generation moderation false positive; the accepted image was produced through
the same subscription-backed Codex path by composing the exact expanded Part
One face source with the earlier seated-hologram apparatus reference.

## Prototype Gate

The following three pages are generated, inspected together, and copied to
`research/prototypes/` only after all their refs pass.

### Page 1 - Fifty Years Later

- [x] Immediate, legible fifty-year jump.
- [x] Stable city plus enormous frontier emptiness.
- [x] Colony-ship continuity from Part One without copying its composition.
- [x] Hardin and Lee correct and clearly attributed.
- [x] Exactly five text blocks.
- [x] Exact 1536x1024 canvas.

### Page 12 - The Board

- [x] Three equal vertical panels.
- [x] Exactly six balloons, two per panel.
- [x] Left speaker reads before right speaker in every panel.
- [x] Pirenne, Fara, and Hardin remain distinct and consistent.
- [x] Sutt, Fulham, and Bort remain silent.
- [x] Every tail reaches the correct visible speaker mouth corridor.
- [x] The political turn is understandable without outside explanation.
- [x] Exact 1536x1024 canvas.

### Page 23 - The Time Vault

- [x] Practical room geography and glass cubicle are immediately readable.
- [x] Seldon recording matches expanded Part One identity.
- [x] Pale blue-white recording is the only dominant light.
- [x] Exactly three Seldon balloons and no Trustee/Hardin speech.
- [x] The recording appears timed, not interactive or supernatural.
- [x] No Apple Vault exterior, null field, floating polyhedron, or psychic effect.
- [x] Exact 1536x1024 canvas.

Do not begin the full page run until all three prototypes pass as a set for
register, identity, text, attribution, spatial clarity, and dimensions.

Prototype audit record: accepted rasters are stored in both
`research/prototypes/` and their reserved `pages/` positions. Page 1 passed on
its first generation. Page 12 and Page 23 required complete-page regenerations
to shorten speaker-tail corridors; rejected generations were not copied into
the project. No crop patches or post-generation lettering were used.

## Cover QA

- [x] `FOUNDATION` spelled exactly.
- [x] `PART TWO · THE ENCYCLOPEDISTS` spelled exactly.
- [x] `after the novel by ISAAC ASIMOV` rendered once.
- [x] Hardin is the clear viewpoint lead.
- [x] Pirenne, Terminus, Seldon recording, and Four Kingdoms balance are present
  without overcrowding.
- [x] Cover promises political pressure, not a fleet battle.
- [x] Exact 1536x1024 canvas.

## Full-Page QA

Inspect the cover and every final page at full resolution in reading order
against `04-SCRIPT.md` for:

- [x] exact panel number, shape, placement, and reading order;
- [x] exact story text, punctuation, spelling, and capitalization;
- [x] no invented, omitted, duplicated, or paraphrased text;
- [x] intended balloon count, speaker, position, and tail endpoint;
- [x] silent-character discipline;
- [x] no blank balloons, empty captions, or orphan tail fragments;
- [x] stable recurring identity, costume, age, and body build;
- [x] stable environment, ship, reactor, Vault, and strategic-model language;
- [x] correct state of the Four Kingdoms model for that page;
- [x] visible evidence before each major Hardin deduction;
- [x] no Apple-only object, costume, character, or event;
- [x] no priesthood, Galactic Spirit, miracle, interdict, Wienis, Lepold, Aporat,
  or repaired battlecruiser from Part Three;
- [x] no production heading, prompt fragment, filename, watermark, or fake label;
- [x] no post-production HTML, SVG, or crop-patched lettering;
- [x] exact 1536x1024 dimensions.

## Page-Specific Narrative QA

- [x] P1 orients time, place, generation, and mission.
- [x] P2-P4 make resource dependence, political isolation, and divided authority
  legible.
- [x] P5-P8 show Rodric discovering Terminus's weakness and asking for control.
- [x] P9-P10 explain that plutonium was a test and why Rodric failed it.
- [x] P11-P12 establish Hardin's public mandate and the Board's inward focus.
- [x] P13-P15 show that Dorwin has knowledge and diplomatic skill but supplies
  neither experiment nor help.
- [x] P16 makes "nothing" visible without unreliable formula text.
- [x] P17-P18 distinguish a base from harmless compromise.
- [x] P19-P20 show Hardin's deduction and uncertainty before the coup.
- [x] P21-P22 keep the transfer of power bloodless, procedural, and civic.
- [x] P23-P25 keep Seldon recorded, noninteractive, and population-scale.
- [x] P24 preserves Pirenne's dignity while breaking his understanding.
- [x] P25 states why foreknowledge would endanger the Plan.
- [x] P26 shows both the internal and external crises clearly.
- [x] P27 gives each of the three rival kingdoms its own visible answer.
- [x] P28 resolves the base withdrawal without battle and stops before religion.

## Full-Page Regeneration Record

Every accepted correction was a complete-page regeneration. No crop patch,
balloon swap, HTML/SVG lettering, or direct API path was used.

- Page 4: regenerated because Hardin's final line was staged with his back to
  the reader; the accepted page keeps a readable three-quarter profile.
- Page 7: regenerated because Pirenne's mouth was obscured in the veranda panel.
- Page 8: regenerated after Rodric and Hardin identities were swapped.
- Page 16: regenerated to remove an invented document title.
- Page 22: regenerated twice until the central group contained exactly five
  Trustees, visibly separate from the civic wardens.
- Page 25: regenerated so the visible specialist categories match the script:
  engineer, scientist, chemist, historian, and one empty place.
- Page 26: regenerated after Hardin drifted into Yohan Lee's identity.
- Prototype Pages 12 and 23 were regenerated during the prototype gate to
  improve speech-tail corridors.
- Cover, 2026-07-26: the original and two correction directions were rejected
  first for leathery, over-aged facial rendering and then for a thin, undersized
  body and unnatural pose. The accepted cover was generated from a blank
  composition using only the five locked character, city, recording, and
  political-model references. Hardin now has a healthy medium build, conventional
  head-to-body proportions, a grounded full-body stance, natural arms and hands,
  and the locked frontier costume. The political composition and all three exact
  cover text elements remain intact at 1536x1024.

## Regeneration Policy

All corrections are complete-page regenerations.

When QA fails:

1. Record the exact observed failure.
2. Decide whether the cause is script density, speaker staging, reference drift,
   composition, or model text rendering.
3. Change only the necessary prompt/staging constraint.
4. Regenerate the full 1536x1024 page with the full script and all refs.
5. Reinspect the entire page, not only the corrected region.

Never crop-patch, swap balloons, redraw a tail, overlay lettering, or move story
text into HTML/SVG.

## Reader Gate

After all rasters pass, build `index.html` from the expanded Part One reader
pattern and verify:

- [x] cover and Pages 1-28 load in order;
- [x] location strip follows `TERMINUS`, `ENVOY`, `BOARD`, `EMPIRE`, `SIX DAYS`,
  `VAULT`, `FOUR KINGDOMS`;
- [x] previous/next, keyboard, swipe handler, progress, counter, and disabled end
  states;
- [x] click/tap zoom opens and closes without leaving body scroll locked;
- [x] desktop and 390x844 mobile layouts have no body-level horizontal overflow;
- [x] afterword explains decay through lost systems and expertise;
- [x] five WHY-quiz answers lock, explain causality, and score correctly;
- [x] no browser console errors.

Browser audit record: the local reader loaded all 29 rasters at natural
1536x1024 dimensions, exposed all seven route states in order, reached the
Afterword and then the quiz, and produced a 5-of-5 locked quiz score. Keyboard
navigation and zoom/body-scroll recovery passed interactively.
The touch handler was code-audited because the desktop browser's device-size
override does not synthesize touch events. Desktop and 390x844 layouts were
visually inspected with zero body-level horizontal overflow.

Potential quiz concepts:

1. Why did the missing metal shipments matter more than Anacreon's new royal
   title?
2. Why did Rodric's plutonium reaction reveal lost atomic knowledge?
3. Why did Dorwin's treaty offer no real protection?
4. Why did Seldon keep psychohistorians off Terminus?
5. Why did the other three kingdoms force Anacreon to leave without a battle?

## Catalog and Publishing Gate

Do not edit `../stories.js` until every production and reader item passes.

When the user requests publication:

- [ ] confirm checkout is `main`;
- [ ] stage only Part Two files and the exact intended catalog files;
- [ ] commit directly to `main` under the repository rule;
- [ ] push `origin main` without a feature branch or pull request;
- [ ] verify local `HEAD` equals `origin/main`;
- [ ] wait for GitHub Pages;
- [ ] verify the public index and Part Two reader on desktop and mobile.

## Generation Path

All raster production must use the built-in subscription-backed Codex
image-generation path. Do not use `OPENAI_API_KEY`, the bundled imagegen CLI,
or a separately billed direct API route unless the user explicitly authorizes
that change in this conversation.
