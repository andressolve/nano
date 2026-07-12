# Handoff - Expanded Earthsea Part Four

## Status

**Complete, 2026-07-12.** `earthsea-wizard-part4/` contains the full Chapter 6 adaptation: production plan, eleven locked references, three accepted prototypes, cover + 30 finished pages, responsive reader, afterword, five-question why quiz, seven-stop route strip, QA record, and shared catalog integration.

Open the reader at `http://127.0.0.1:8765/earthsea-wizard-part4/` while the workspace server is running.

## Story boundary

- Begins on Low Torning after Yevaud's oath.
- Covers the thanksgiving song, Pechvarry's private reproach, Ged's attempt to return to Roke, the warding wind, Serd, Orrimy, the grey stranger, the north-ship passage, Skiorh's first wrongness, Neshum, the Osskil moor, the gebbeth reveal, the spoken true name, the failed staff defense, the chase, and the open gate.
- Ends with Ged unconscious just inside the Court of the Terrenon while the doors close against the gebbeth.
- Chapter 7, "The Hawk's Flight," is Part Five. Do not add Serret's welcome, the Stone of Terrenon, Benderesk, Hoeg's death, the bird-flight escape, or Ged's return to Ogion to this volume.

## Editorial result

The volume's through-line is fear narrowing choice. Ged still sacrifices his own safety to protect Low Torning and the Roke-bound crew, but isolation removes the clarity he had at Pendor. By the time a stranger offers one specific road, fear has made direction feel like wisdom. The north-ship and moor sequences progressively remove rest, equality, privacy, language, and human company until the shadow can arrive wearing the guide Ged reluctantly accepted.

## Shipped artifacts

- `00-PROJECT-BRIEF.md` - story boundary, editorial center, pacing, source policy, and reader concept.
- `01-STYLE-GUIDE.md` - exact visual, horror, and lettering register.
- `02-CHARACTERS.md` - identity locks and reference prompts.
- `03-SETTINGS.md` - route, ship, Osskil, and Terrenon environment locks.
- `04-SCRIPT.md` - cover, 30 pages, exact lettering, and attribution maps.
- `05-PRODUCTION-QA.md` - reference, prototype, correction, visual, browser, and catalog record.
- `06-GENERATION-PROMPT-SET.md` - fixed prompt and page reference matrix.
- `refs/` - eleven locked 1536x1024 identity, object, and environment sheets.
- `research/prototypes/` - accepted Roke-wind, empty-hood, and gate prototypes plus Page 25 production history.
- `pages/` - cover plus Pages 1-30, all 1536x1024 with native lettering.
- `index.html` - responsive reader, zoom, afterword, route strip, and quiz.
- `../stories.js` - Part Four published at the top of the shared catalog.

## Production record

- Built-in subscription-backed Codex image generation only.
- No `OPENAI_API_KEY`, bundled image-generation CLI, or direct API billing.
- All seven new refs passed before prototype work.
- Page 25 required two complete prototype corrections to remove an invented mouse-like Hoeg, restore exact Skiorh clothing, and eliminate exposed gebbeth skin.
- Page 27 received one accepted complete replacement to keep Hoeg hidden and restore open-moor continuity.
- No crop patches, tail patches, composites, HTML lettering, or SVG lettering were used.
- See `05-PRODUCTION-QA.md` for the complete acceptance and browser record.

## Non-negotiables for Part Five

1. Preserve this volume unchanged unless the user explicitly requests a revision.
2. Use the built-in subscription-backed Codex image-generation path unless the user explicitly approves separate API billing.
3. Reuse the locked Ged, Hoeg, gebbeth, and Terrenon exterior references.
4. Generate and approve Serret, Benderesk, the Servants of the Stone, the Stone chamber, and any required hawk/gull transformation references before pages.
5. Preserve skin-tone canon: Ged remains deep copper; Serret and Benderesk are pale Osskilians.
6. Bake all dialogue and captions into the raster page.
7. Treat speech attribution as scene blocking and map every balloon before generation.
8. Regenerate the full page for any identity, text, staging, attribution, or dimension failure. Never crop-patch or overlay lettering.
9. Keep the Stone of Terrenon an ancient imprisoned power, not a friendly oracle, gemstone, magic console, or glowing crystal.
10. Handle Hoeg's death without gore or sentimental spectacle; its loss matters because ordinary living companionship is destroyed by the trap.

## Reader specification

- Reuses the Part Three reader chassis.
- Frost-silver accent: `#9aa9b4`.
- Route strip: `LOW TORNING · ROKE-WIND · SERD · ORRIMY · NORTH SHIP · OSSKIL · THE GATE`.
- Strip label: `A road chosen by fear`.
- Reader sequence: cover, Pages 1-30, afterword, quiz.

## WHY quiz

1. Ged leaves Low Torning because the coming shadow would turn the community he protected into shelter for his hunter.
2. Ged turns from Roke because the warding wind has sensed the shadow, and forcing it would break the ship and endanger the crew.
3. The stranger's advice works because exhaustion and fear make the first specific direction feel like an answer.
4. Hoeg's unease matters because ordinary living instinct feels the danger Ged's exhausted mind has buried.
5. The gebbeth's use of Ged's true name closes transformation and summons while draining the self it names.

## Billing path

- Built-in Codex image generation under the user's ChatGPT/Codex entitlement.
- No `OPENAI_API_KEY`, bundled image-generation CLI, or direct API request.
