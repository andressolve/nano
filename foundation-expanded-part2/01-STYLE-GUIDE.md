# Style Guide - Foundation, Part Two

## Fixed Style Block

Paste this near the beginning of every image prompt:

> Serious cinematic mid-century science-fiction graphic-novel realism, descended from 1970s British SF paperback airbrush. Controlled dark inked contours with smooth painterly airbrush and cel-shaded color, hazy atmospheric depth, monumental but readable environments, realistic anatomy, and natural expressive faces. Saturated teal, amber, scarlet, ivory, ochre, and deep space-black. Period analog-futurist machinery with chrome and enamel surfaces. Not modern glossy concept art, not photoreal live action, not flat vector art, not halftones, not cute, and not parody.

## Register and Anti-Drift

> Match the attached finished Foundation Part One page as the visual-register source: cinematic multi-panel storytelling, clean solid-black panel borders, clear off-white gutters, cream rectangular caption boxes with dark readable hand-lettered serif text, and off-white rounded speech balloons. Preserve the same serious family-reading register and the same physical reality. The page is a new unified composition, not a copy of the reference layout.

The strongest pixel references are:

- `../foundation-expanded-part1/pages/page-24.png` for series continuity and
  the departure into the time jump;
- `../foundation-expanded-part1/pages/page-06.png` and `page-12.png` for
  two-person dialogue;
- `../foundation-expanded-part1/pages/page-18.png` for political blocking;
- `../foundation-expanded-part1/pages/page-11.png` for analytical systems;
- `../foundation/pages/page-13.png` only as provenance for the earlier Vault
  design until the new Part Two Vault reference is approved.

## Page Geometry

- Exactly 1536x1024, 3:2 landscape.
- Usually three panels: one wide and two smaller, or two smaller and one wide.
- Use four panels only for genuine sequence, comparison, or analysis.
- Use a single full-bleed image only for the cover and the final image on Page
  28 if production lettering remains readable.
- State panel shapes and reading order explicitly.
- Maintain clean solid-black borders and off-white gutters.
- Never render a production heading, page number, script label, filename,
  prompt instruction, or reference-sheet label.

## Lettering

- All captions and dialogue are baked into the generated page image.
- Captions: cream/ivory rectangular boxes, dark readable serif or hand-lettered
  text.
- Dialogue: off-white rounded balloons, dark text, short triangular tails.
- Electronic communications: cream boxes with a thin teal or scarlet keyline;
  they are still normal story text, never pseudo-writing on a screen.
- Render only supplied text, verbatim, once each.
- No quotation marks inside ordinary speech balloons.
- No empty balloons, empty captions, decorative pseudo-writing, watermarks, or
  invented signs.
- Prefer one idea per balloon. Put long explanations into captions or give them
  a panel.
- Preserve punctuation and capitalization from `04-SCRIPT.md`.

Close every page prompt with:

> All words spelled correctly. Do not duplicate, omit, paraphrase, or invent text. Render only the quoted captions and dialogue. No modern logos, no watermarks, no page number, no title heading, no blank balloons, no decorative pseudo-writing, and no Apple-series characters, costumes, ships, Vault effects, or technology.

## Speech Attribution

Speech attribution is built through blocking:

1. Stage speakers left-to-right in speaking order whenever possible.
2. Map every balloon by ordinal, speaker, verbatim text, balloon position,
   character position, and tail endpoint.
3. Keep mouths visible and leave a clean tail corridor.
4. Name silent characters and give them no balloons.
5. For A-B-A in one panel, use upper-left A, upper-right B, lower-left A.
6. When an exchange remains risky, use one visible speaker and one balloon per
   panel.
7. Reject tails aimed at torsos, hands, props, chairs, or empty space.
8. Reject duplicate figures, duplicate balloons, silent-character speech, and
   orphan tail fragments.

## Part Two Palette and Material Logic

### Terminus daylight

- bleached pale-blue sky;
- ochre and rust-red plain;
- low ivory concrete/ceramic buildings;
- teal-painted steel, amber glass, modest chrome;
- dry wind, long shadows, very little vegetation.

Terminus must feel functional and inhabited, but tiny against the empty planet.
Its technology is compact, clean, and repairable. Avoid utopian glass towers,
dense Trantor scale, medieval huts, or a dusty western costume register.

### Encyclopedia interiors

- warm ivory walls, tall teal data-stack machinery, amber task lights;
- ordered desks, data cylinders, diagrams, indexing equipment;
- impressive intellectual labor, but repetitive and inward-facing.

The Encyclopedia is not fake work. Its work is real; its official historical
purpose is the cover.

### Civic government

- practical city hall, broad windows onto the plain, dark teal tables, paper and
  tape analysis machines, minimal ornament;
- Hardin's spaces are outward-facing and full of maps, freight data, and public
  messages.

### Anacreon

- maroon, black, brass, faded gold, heavy leather, heraldic sunburst motifs;
- impressive uniforms and bulky old Imperial-derived ships;
- visible repairs, mismatched armor plates, oil/coal auxiliary machinery, no
  glowing atomic miniaturization;
- grandeur that has outlived understanding.

### The Empire / Lord Dorwin

- lavender, cream, polished gold, jewel tones, immaculate fabric and lacquer;
- refined courier craft and ceremonial escort;
- physical perfection at the surface, followed by words rather than resources.

### Time Vault

- near-black neutral room, low seats, central glass cubicle;
- Seldon as a pale blue-white recorded projection in a practical powered chair;
- the projector is mechanical and timed, not a supernatural monolith;
- no null field, floating polyhedron, psychic effect, or interactive response.

## Strategic and Technical Visual Language

Maps and analysis must be readable without unexplained writing:

- Terminus is one bright teal/amber point at the center.
- Anacreon is the largest maroon vector, closest and strongest.
- Smyrno, Konom, and Daribow are three distinct smaller colored vectors.
- Former Imperial routes are broken, dim, or absent.
- The atomic asymmetry is one clean bright reactor symbol on Terminus versus
  four dark or obsolete reactor silhouettes.
- The balance-of-power resolution shows three vectors converging on Anacreon's
  exclusive claim, not four friendly planets or a battle formation.

Do not fill maps with fake labels, fantasy runes, unexplained numerals, or
Apple-series iconography. When names are needed, keep them in caption text.

## Violence and Physical Danger

- Troop transports may land and temporary bases may rise on empty land.
- Civilians may watch in fear; civic wardens may hold stations during the coup.
- No firefight, bombing, gore, execution, city occupation, or heroic armed
  charge.
- The tension comes from control of land, infrastructure, and authority.

## Reference Roles

Every production prompt labels each input as one of:

- identity reference;
- environment/object reference;
- finished-page visual-register reference.

Reference sheets are not layouts. Prompts must direct the model to paint one
new unified page and not reproduce split-sheet arrangements or labels.
