# Production QA - Part Four

## Final inventory

- 1 cover and 30 numbered finished pages in `pages/`.
- 11 locked 1536x1024 reference sheets in `refs/`: 4 reused Part Three identities and 7 new character, object, and environment sheets.
- 3 accepted hard-page prototypes in `research/prototypes/`, plus two preserved rejected Page 25 prototype attempts.
- Reader, afterword, five-question why quiz, and seven-stop route strip in `index.html`.
- Shared catalog entry at the top of `../stories.js`.
- Every active production and reference PNG is exactly 1536x1024.
- No page lettering is supplied by HTML, SVG, or a post-generation overlay.

## Generation path

All raster artwork was generated with the built-in, subscription-backed Codex image-generation path. No API key, image-generation CLI, or separately billed API request was used.

Each page used the relevant locked identity or environment sheets plus an accepted finished Expanded Earthsea page as a visual-register reference. Captions and dialogue were baked into the generated raster page from `04-SCRIPT.md`.

## Reference gate

- Reused approved Part Three Ged, Hoeg, Pechvarry, and Low Torning people sheets.
- Generated and approved southern sailors, the Orrimy grey stranger, the north-ship crew, the Skiorh/gebbeth dual state, Osskil workers, the north ship, and the Court of the Terrenon exterior.
- Southern Archipelagan skin-tone gate passed: Low Torning and southern sailors remain brown- and black-skinned.
- Osskil gate passed: northern characters are pale and wind-chapped without Viking, elf, or fantasy-master-race coding.
- Skiorh gate passed: living and gebbeth states share the same clothing; the gebbeth hood is a featureless matte-black absence.
- Vehicle and environment gates passed: the north galley and Terrenon keep have reproducible silhouettes and construction.

## Prototype gate

- **Page 6, Roke-wind reversal:** accepted on the first generation. The wind reads as purposeful ordinary weather, ship danger is clear, shipmaster/Ged attribution is correct, and Ged's decision protects the crew.
- **Page 25, empty hood:** required two complete prototype regenerations. The first invented a mouse-like Hoeg on Ged's shoulder. The second hid Hoeg but exposed human skin on the gebbeth and drifted Skiorh's coat toward Ged's cloak. The accepted page removes visible Hoeg, restores Skiorh's exact coat and peaked hood, uses dark gloves, and keeps the hood entirely featureless.
- **Page 29, open gate:** accepted on the first generation. Chase geography, gate light, unseen-voice attribution, exact lettering, and Chapter 7 restraint all passed.

## Accepted full-page replacement

Every correction below replaced the complete page. No crop patch, tail patch, composite, or text overlay was used.

- Page 27: the original exposed Hoeg on the snow, gave the rising sleeves wing-like shapes, and moved the action prematurely to the keep wall. The accepted replacement keeps Hoeg fully hidden, removes all architecture, stages the action on open moor, and makes the attacking sleeve visibly hollow. The original remains as `pages/page-27-v1.png`; the accepted production copy is also preserved as `pages/page-27-v2.png`.

## Full-resolution visual pass

The active run was inspected page by page in reading order for:

1. Exact caption and dialogue text.
2. Declared balloon count, speaker identity, reading order, tail direction, and silent characters.
3. Ged's copper skin, age, clothing, plain staff, and left-cheek scars.
4. Hoeg scale and role as an ordinary living companion.
5. Pechvarry, Low Torning, southern sailor, grey stranger, north-crew, Skiorh, and Osskil continuity.
6. The transition from living Skiorh to the featureless gebbeth.
7. Roke-wind restraint, labor depiction, winter geography, chase continuity, and gate ambiguity.
8. The Chapter 6 ending boundary: no Serret, Benderesk, Stone of Terrenon, interior court, bird escape, or Ogion material.
9. Exact 1536x1024 canvas dimensions.

## Reader and catalog checks

The reader was exercised in the Codex in-app browser at `http://127.0.0.1:8765/earthsea-wizard-part4/`.

- Cover and Pages 1-30 all loaded at natural size 1536x1024.
- Previous/next navigation reached cover, every numbered page, afterword, and quiz.
- Active route changed at the intended boundaries: Low Torning, Roke-Wind, Serd, Orrimy, North Ship, Osskil, and The Gate.
- Page labels end at `Page 30 of 30`.
- Tap/click zoom opened and closed correctly.
- At 390x844, body width equaled viewport width, the page fit at 374 pixels, and zoom expanded to 1092 pixels for horizontal panning.
- All five correct quiz answers locked their groups, displayed correct feedback, and produced `5 of 5`.
- Browser console reported no warnings or errors.
- Root catalog lists Part Four first and its card opens the reader successfully.
- Inline reader JavaScript and `stories.js` both pass Node syntax checks.

## Source limitation

The complete Chapter 6 novel text is not present in the workspace. Story chronology was cross-checked against the legacy adaptation, the National Endowment for the Arts guide, LitCharts, SuperSummary, Course Hero, and the Earthsea reread discussion. All production lettering is original adaptation prose. A future novel-in-hand pass can correct a factual detail by regenerating the complete affected page.
