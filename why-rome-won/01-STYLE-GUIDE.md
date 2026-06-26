# 01 — STYLE GUIDE

## Visual register (two sub-registers, one palette)

All images share ONE palette so the volume reads as a single piece:
**warm parchment / sun-bleached stone / bronze / iron-grey / oxblood-red (the legion's red),** with
Mediterranean sky. Muted, period, museum-quality — NOT bright, NOT cartoonish.

**Anti-drift directive — paste into every prompt:**
> NOT a children's book. NOT a comic. Serious, realistic, museum-quality historical reconstruction.
> Realistic proportions, natural light, no cel shading, no halftones, no ink outlines.

### Sub-register A — PAINTED SCENES (cover, P1, P2, P6, P7, P8)
> Painted historical reconstruction in the style of a fine museum / National-Geographic ancient-Rome
> illustration. Oil/gouache brushwork, cinematic natural light, atmospheric depth, accurate Roman
> military detail. Muted warm palette: parchment, stone, bronze, iron, legionary oxblood-red.

### Sub-register B — MAPS & TACTICAL DIAGRAMS (P4 socii map, P5 Cannae)
> Elegant antique cartography / engraved tactical-map style on aged parchment. Sepia and iron-ink line
> work, subtle hand-colored fills, compass rose, restrained. Clean and legible like a museum exhibit
> map. VERY FEW words — single-word labels only (see text rule below).

## TEXT-IN-IMAGE RULE (critical — gpt-image-2 still fumbles dense labels)
Keep in-image lettering to an absolute minimum. The PROSE in the reader carries every explanation; the
image is never asked to teach through labels.
- Maps/diagrams: at most a few **single-word** labels (e.g. `ROMA`, `HANNIBAL`, `CARTHAGE`). No
  sentences, no callout paragraphs, no numbered keys baked into the image.
- Scenes: NO text at all.
- The four-part synthesis (P8) is built in HTML/CSS, so it carries NO in-image text burden.
- If an image seems to need more than ~3 words, redesign it so the reader's caption does the talking.

## Reader theme (clone shock-of-florence, re-skinned "Roman")
- Light parchment body, serif display (Cormorant Garamond), Inter for labels — same as shock-of-florence.
- **Accent color: Roman oxblood/imperial red `#9a2f2f`** (shock used Florence-orange; ours is legion-red).
- Section labels in three parts:
  - Part One · The Answer Everyone Gives  (muted stone grey)
  - Part Two · The Real Reason  (oxblood red)
  - Part Three · What It Means  (bronze `#9c6b2e`)
- Dark cover + dark end page (same as shock).
- Fact boxes = white cards with red `FACT` / `DID YOU KNOW?` label. Pull-quotes = red left-border.
- A custom **four-pillar CSS block** on P8 (Discipline / Manpower / Resilience / Adaptation) — four
  equal cards, each with a one-line summary.
- Progress bar, prev/next nav, keyboard arrows, 5-question quiz, score box — all inherited.

## Tone of the prose
Vivid, concrete, confident; builds an argument step by step like shock-of-florence. Assume the reader
has never studied Rome — explain Hannibal, the socii, the corvus from scratch. No age-pitching; clarity
is the standard. Let the dramatic facts (the Alps, the trap at Cannae, the refusal to surrender) carry
the feeling — don't editorialize emotion.
