# Handoff - Expanded Earthsea Part Three

## Status

**Complete and user-approved, 2026-07-12.** The folder contains the full production plan, seven locked references, three accepted prototypes, cover + 32 finished pages, responsive reader, afterword, five-question why quiz, seven-stop route strip, QA record, and shared catalog integration for Chapter 5, "The Dragon of Pendor."

## New-session continuation state

- Working branch: `codex/expanded-earthsea-part3`.
- Draft pull request: [andressolve/nano#1](https://github.com/andressolve/nano/pull/1), targeting `main`.
- Production commit: `19e3ff2` (`Add Expanded Earthsea Part Three`).
- The branch and remote were verified aligned after push. The pull request had no configured automated checks at handoff time.
- Volume 3 is finished and approved. Do not regenerate, revise, or relabel its pages unless the user explicitly requests a new change.
- The final active Page 10 is `pages/page-10.png`, byte-identical to the approved `pages/page-10-v3.png`. It was reimagined as a full-page regeneration to avoid the earlier crowd of converging hands. Keep `page-10-v1.png` and `page-10-v2.png` only as production history.
- The repository also contains numerous unrelated modified and untracked files from other projects. They were deliberately excluded from the Volume 3 commit. Never stage them as part of this work; inspect `git status` and stage explicit paths only.
- If the user asks to continue the expanded Earthsea sequence, the next story boundary is Part Four, Chapter 6, "Hunted." Start it as a separate production folder and preserve this volume unchanged.

## Story boundary

- Begins with Ged arriving among the Ninety Isles for his first post as a wizard.
- Covers Low Torning, his friendship with Pechvarry, Ioeth's illness, the failed journey into the Dry Land, the shadow finding him, his decision to discharge his duty before fleeing, the young-dragon fight, Yevaud's temptation, the true-name leverage, and the oath.
- Ends with Ged sailing east from Pendor. The islands are safe; Ged is not.
- Chapter 6, "Hunted," is Part Four. Do not add Osskil, Skiorh, or the Court of the Terrenon to this volume.

## Read order before production

1. `00-PROJECT-BRIEF.md`
2. `01-STYLE-GUIDE.md`
3. `02-CHARACTERS.md`
4. `03-SETTINGS.md`
5. `04-SCRIPT.md`
6. `05-PRODUCTION-QA.md`
7. `06-GENERATION-PROMPT-SET.md`
8. `../earthsea-wizard-part2/HANDOFF.md`
9. `../earthsea-wizard-part2/05-PRODUCTION-QA.md`
10. `../earthsea-wizard-part1/05-SPEECH-ATTRIBUTION-STUDY.md`

## Shipped artifacts

- `00-PROJECT-BRIEF.md` through `06-GENERATION-PROMPT-SET.md` — scope, style, identities, settings, full page script, QA, and reproducible prompt system.
- `refs/` — seven locked 1536x1024 identity and creature sheets.
- `research/prototypes/` — accepted Dry Land, dragon-change, and Yevaud-dialogue prototypes.
- `pages/` — cover plus Pages 1-32, all 1536x1024 with native lettering.
- `index.html` — responsive flipper, zoom, afterword, route strip, and quiz.
- `../stories.js` — Part Three published at the top of the shared catalog.

## Production record

- Built-in subscription-backed Codex image generation only.
- New references passed the Archipelagan skin-tone, Hoeg-scale, and dragon-anatomy gates.
- Page 27 required two full-page prototype restagings.
- Pages 10, 11, 14, 18, 19, 23, and 32 received accepted full-page replacements during QA. Page 10's accepted reimagining is `page-10-v3.png`; the original and superseded first correction remain as `page-10-v1.png` and `page-10-v2.png`.
- No crop patches, tail patches, composites, HTML lettering, or SVG lettering were used.
- See `05-PRODUCTION-QA.md` for the complete acceptance record and the source-text limitation.

## Non-negotiables

1. Use the built-in subscription-backed Codex image-generation path only, unless the user explicitly authorizes separate API billing.
2. Attach every relevant identity ref and an approved finished-page style reference to every generation.
3. Bake all dialogue and captions into the raster page.
4. Keep Low Torning's people brown- and black-skinned.
5. Keep Hoeg at large-rat/tiny-cat scale.
6. Keep the Dry Land starless, windless, grey, and visually spare.
7. Keep the shadow flat matte black, faceless, and textureless.
8. Keep child illness and dragon combat non-gory.
9. Treat speech attribution as scene blocking; use the exact maps in the script.
10. Regenerate the full page for any failure. Never crop-patch, tail-patch, or letter in HTML/SVG.

## Reader specification

- Reuse the responsive Part Two reader chassis.
- Furnace-gold accent: `#c58a3a`.
- Route strip: `THE NINETY ISLES · LOW TORNING · THE SICKROOM · DRY LAND · THE HUT · PENDOR · THE OATH`.
- Strip label: `A wizard's first charge`.
- Reader sequence: cover, Pages 1-32, afterword, quiz.

## WHY quiz

1. Ged follows Ioeth because Pechvarry's trust and Ged's own difficulty accepting a limit make refusal feel like failure.
2. Hoeg matters because ordinary living companionship reaches Ged where command and technique cannot.
3. Ged cannot simply flee because the dragons remain a danger he freely agreed to answer; flight would move his private danger away but abandon his public duty.
4. The shadow's name offers control over the one thing Ged most fears, making it more dangerous to him than treasure.
5. Ged spends his advantage on the oath because his power belongs first to the people in his charge. That refusal of self-saving is the proof that he has changed.

## Billing path

- Built-in Codex image generation under the user's ChatGPT/Codex entitlement.
- No `OPENAI_API_KEY`, bundled image-generation CLI, or direct API request.
