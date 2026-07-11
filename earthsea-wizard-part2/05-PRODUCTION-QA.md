# Production QA - Part Two

## Final inventory

- 1 cover and 30 numbered finished pages in `pages/`.
- 7 locked reference sheets in `refs/`.
- 3 accepted hard-page prototypes in `research/prototypes/`.
- Every production and reference PNG is 1536x1024.
- No page lettering is supplied by HTML, SVG, or a post-generation overlay.

## Generation path

All raster artwork was generated with the built-in, subscription-backed Codex image-generation path. No API key, image-generation CLI, or separately billed API request was used.

Each finished page used multiple native image references: the relevant Part Two identity sheets, a finished Part One page as the visual-register source, and, after the prototype gate, an accepted Part Two page where useful for local continuity. The exact page text, panel construction, and attribution map came from `04-SCRIPT.md`.

## Prototype gate

The full run began only after three difficult page types passed:

- Page 6, threshold dialogue: revised to preserve the five-balloon entrance exchange and ordinary Doorkeeper identity.
- Page 14, technical teaching: accepted with a restrained candle/stone demonstration and one visible speaker per panel.
- Page 26, summoning catastrophe: revised so the summoned figure is young Elfarran, the shadow remains matte black, and Vetch and Nemmerle own the only two speech balloons.

## Accepted full-page regenerations

Every correction below replaced the full page. No tail patch, crop composite, or text overlay was used.

- Cover: changed a corpse-like foreground form into an elongated, flat, impossible shadow.
- Page 2: restored the captain as a dark copper-brown working sailor.
- Page 6: restaged the threshold exchange and Doorkeeper identity.
- Page 7: isolated Nemmerle's single speech balloon from silent Ged and the raven.
- Page 10: placed Vetch alone in his speaking panel instead of assigning his line to another student.
- Page 13: restored the omitted line, `Again. This time without force.`
- Page 15: regenerated a square output at the required 1536x1024 landscape canvas.
- Pages 18 and 19: reduced Hoeg from dog scale to a large-rat/tiny-cat scale.
- Page 23: restored Vetch's deep-black-skinned adolescent identity.
- Page 24: corrected a Ged/Jasper identity substitution.
- Page 26: replaced an elderly summoned spirit with young Elfarran.
- Page 27: replaced a village-witch rendering with a plain male Roke healer.
- Page 28: restored Gensher's cropped-hair, deep-brown-skinned identity instead of drifting toward Ogion.
- Page 30: restored the small, clean-shaven, cropped-grey-haired Doorkeeper instead of a bearded mage.

## Reading-order and attribution pass

The finished run was read visually in page order against `04-SCRIPT.md` and the Part One speech-attribution study. The pass checked:

1. Exact balloon count and declared silent characters.
2. Speaker position, balloon tier, reading order, and tail endpoint.
3. Duplicate, omitted, paraphrased, or invented text.
4. Orphan tail fragments and tails ending at torsos or empty space.
5. Recurring identity, skin tone, age, clothing, scar side, Hoeg scale, and shadow treatment.
6. Scene-to-scene time, location, reaction, and emotional continuity.
7. Exact 1536x1024 canvas size.

Where a short tail was visually imperfect but the only visible speaker, panel blocking, and reading order made attribution unambiguous, the page was accepted under the rule established by `../earthsea-wizard-part1/05-SPEECH-ATTRIBUTION-STUDY.md`. No page with a wrong speaker or ambiguous exchange was accepted.

## Reader and catalog QA

Checked in the Codex in-app browser at `http://127.0.0.1:8765/earthsea-wizard-part2/`:

- Cover and Pages 1-30 all loaded at natural size 1536x1024.
- Previous/next navigation reached the cover, every page, afterword, and quiz.
- The active route moved through Sea, Thwil, Great House, Isolate Tower, Roke Knoll, Healing, and West.
- Tap/click zoom opened and closed correctly.
- At 390x844, the reader had no body-level horizontal overflow; the page fit at 374 pixels wide and zoom expanded to 1092 pixels.
- All five correct quiz answers locked their groups, displayed correct feedback, and produced `5 of 5`.
- Browser console reported no warnings or errors.
- The root collection card loaded and linked to the reader. The later shared catalog redesign keeps Part Two in the latest 12 automatically.
