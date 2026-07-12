# Production QA - Part Three

## Final inventory

- 1 cover and 32 numbered finished pages in `pages/`.
- 7 locked 1536x1024 reference sheets in `refs/`.
- 3 accepted hard-page prototypes in `research/prototypes/`.
- Reader, afterword, five-question why quiz, and seven-stop route strip in `index.html`.
- Shared catalog entry at the top of `../stories.js`.
- Every production and reference PNG is exactly 1536x1024.
- No page lettering is supplied by HTML, SVG, or a post-generation overlay.

## Generation path

All raster artwork was generated with the built-in, subscription-backed Codex image-generation path. No API key, image-generation CLI, or separately billed API request was used.

Each page used the relevant identity sheets and one or more accepted Expanded Earthsea pages for visual continuity. Captions and dialogue were baked into the generated raster page from `04-SCRIPT.md`.

## Reference gate

- Reused approved Part Two Ged and Hoeg references.
- Reused the approved legacy Yevaud reference.
- Generated and approved Pechvarry, the Low Torning family/witch group, the Low Torning people group, and the juvenile-dragon brood.
- Human skin-tone gate passed: Low Torning remains a brown- and black-skinned Archipelagan community.
- Creature gate passed: Hoeg remains small and the juvenile brood shares Yevaud's lean anatomy without his tower scale.

## Prototype gate

- **Page 15, Dry Land threshold:** accepted with the wall, shadow, and lamp in clear Ged/wall/shadow/lamp order; the shadow is flat matte black and the setting remains starless and spare.
- **Page 27, dragon change:** required two full-page restagings. The accepted page removes false shark-fin silhouettes, keeps the staff in the boat, and reads as a continuous dangerous change rather than a separate summoned dragon.
- **Page 30, Yevaud temptation:** accepted with exactly four balloons, one visible speaker per panel, correct text, and clear Ged/Yevaud attribution.

## Accepted full-page replacements

Every correction below replaced the complete page. No crop patch, tail patch, composite, or text overlay was used.

- Page 10: corrected Ged's malformed left hand in Panel 1, then fully restaged the page after the first correction still clustered too many hands around the child. The accepted `page-10-v3.png` isolates one restrained touch in Panel 1, removes hands from Panel 3, and uses one staff hand in Panel 4. The original and superseded first correction remain as `page-10-v1.png` and `page-10-v2.png`.
- Page 11: restored Pechvarry to the sickroom vigil.
- Page 14: replaced a cloaked adult-like shadow with the small shapeless matte-black absence used by the accepted Dry Land pages.
- Page 18: removed a duplicated township witch and preserved Hoeg's small scale.
- Page 19: restored Ged's and Pechvarry's identities to their correct lines across the one-speaker panels.
- Page 23: reduced a five-panel drift to the scripted four-panel departure sequence.
- Page 32: removed literal chains from the dragon oath; the binding is verbal and magical, not physical.

## Full-resolution visual pass

The active run was inspected page by page for:

1. Exact caption and dialogue text.
2. Declared balloon count, speaker identity, reading order, tail direction, and silent characters.
3. Ged's copper skin, age, clothing, staff, and scar lock.
4. Pechvarry, family, witch, Head Isle-Man, Hoeg, juvenile brood, and Yevaud continuity.
5. Dry Land restraint and matte-black shadow treatment.
6. Child-illness and dragon-combat moderation.
7. Scene-to-scene action, reaction, location, weather, and emotional continuity.
8. Exact 1536x1024 canvas dimensions.

## Reader and catalog checks

- Inline reader JavaScript passes `node --check`.
- Reader HTML, cover, Page 32, and shared catalog all return HTTP 200 from the workspace server.
- Reader title array contains cover plus Pages 1-32.
- Page labels end at `Page 32 of 32`.
- Route strip contains all seven values: Ninety Isles, Low Torning, Sickroom, Dry Land, Hut, Pendor, and Oath.
- Five quiz questions have explicit answer keys: `b`, `c`, `b`, `a`, `c`.
- Root catalog entry points to the active cover and reader slug.
- Interactive browser clicking, resizing, and screenshot QA were not performed; validation used the static reader, JavaScript, asset, and HTTP checks.

## Source limitation

The complete Chapter 5 novel text is not present in the workspace. Story chronology was cross-checked against the legacy adaptation, the National Endowment for the Arts guide, and detailed chapter summaries. All production lettering is original adaptation prose. A future novel-in-hand pass can still correct a factual detail by regenerating the affected full page.
