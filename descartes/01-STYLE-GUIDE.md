# Cogito — Style Guide

## Style Block (COPY VERBATIM TO EVERY PROMPT)

```
Art Style: Dutch Golden Age painterly realism — Rembrandt-Vermeer interior lighting, rich chiaroscuro, serious historical graphic novel aesthetic
Color palette: Warm amber candlelight, deep Dutch brown, cool Delft blue, parchment cream, ink black, stone gray
Effects: Dramatic chiaroscuro, natural light from tall windows, dust motes in sunlight, mathematical line-work emerging from shadow
```

## Visual Identity

This story spans 1601–1650 across France, the Netherlands, Germany, and Sweden. The dominant visual register is **Dutch Golden Age** — warm interiors, dramatic lighting, dark backgrounds with pools of warm light. Think Rembrandt's portraits, Vermeer's rooms, de Hooch's domestic spaces.

### Palette by Era

| Era | Pages | Dominant Colors | Light Quality |
|-----|-------|----------------|---------------|
| Childhood (La Haye) | 2 | Soft ochre, morning cream, warm stone | Gentle, diffused — a grandmother's house |
| La Flèche | 3–5 | Library amber, stone gray, candlelight gold | Candlelit interiors, tall stone corridors |
| Military / Beeckman | 6 | Outdoor green, marketplace warmth, Dutch sky | Bright overcast, marketplace bustle |
| The Dreams | 7–8 | Deep indigo, firelight orange, surreal violet | Flickering stove-light, dreamscape unreality |
| Wandering Years | 9 | Varied — Italian warmth, Parisian gray | Travel montage, shifting light |
| Netherlands | 10–11 | Vermeer amber, Delft blue, linen white | Window light falling on solitary rooms |
| Mathematics | 12 | Cream parchment, precise ink black, amber | Clean and luminous — geometric purity |
| Philosophy | 13–14 | Deep shadow, single candle, parchment | Near-darkness with one source of light |
| Stockholm | 15 | Ice blue, pre-dawn gray, cold white, dark wood | Bitter cold, early morning darkness |
| Legacy | 16 | Warm amber dissolving into clean white grid | Painterly world giving way to mathematical clarity |

### Atmosphere Notes

- **Interiors dominate.** Descartes lived indoors, in his mind. Most pages are interior scenes.
- **Solitude is visual.** Single figures in rooms. Empty chairs. A desk and a candle. Let negative space do the work.
- **Mathematical intrusions.** On certain pages (especially 12, 13, 16), geometric lines, coordinates, and equations should appear as if drawn in light or ink over the painterly surface — precise and clean against textured backgrounds.
- **Aging is visible.** René ages from 5 to 53. His face should change: softening childhood features → angular student → energetic young man → composed philosopher with deepening lines.

## Panel Style

- **Borders:** Thin dark lines, slightly rough — as if drawn with a reed pen
- **Gutters:** Dark brown or near-black, 4-6px
- **Caption boxes:** Parchment-colored with dark text, placed at top or bottom of panels. Used for narration and Descartes' own words.
- **Speech bubbles:** Traditional white with black outlines. Tail points to speaker. Keep dialogue under 15 words.
- **Thought text:** Italicized in caption boxes, attributed to Descartes. Not in thought bubbles.
- **Mathematical notation:** Clean serif font or hand-drawn style. Equations and diagrams rendered in black ink on cream/parchment surfaces.

## Typography Guidance

- **Narration (caption boxes):** Third person, present tense, concise. "He stares at the ceiling. He is five years old and already asking questions no one around him can answer."
- **Descartes' own words (caption boxes, italic):** Direct quotes from his letters, the Discourse, or reliably attributed statements. Always in italics to distinguish from narration.
- **Dialogue (speech bubbles):** Natural, era-appropriate but accessible. No archaic "thee/thou." Keep it conversational.
- **Mathematical text:** Equations, labels (x, y), and geometric terms rendered in clean notation.

## What This Should NOT Look Like

- ❌ Children's book illustration (soft, rounded, bright, cute)
- ❌ Manga or anime styling
- ❌ Modern digital art / concept art sheen
- ❌ Flat colors or cel-shading
- ❌ Steampunk or fantasy elements
- ❌ Oversimplified "educational" graphics

This should look like a serious, beautiful graphic novel that happens to be about a real person. The Dutch Golden Age palette grounds it in Descartes' actual world.

## CRITICAL: Anti-Drift Directive

If any generated page shows signs of children's book aesthetic (oversized eyes, rounded features, bright saturated palette, soft focus, cartoon proportions), add this reinforcement line to the prompt:

```
STYLE REINFORCEMENT: NOT a children's book. Serious mature graphic novel. Dutch Golden Age painterly realism. Realistic human proportions. Muted, warm chiaroscuro palette. Rembrandt lighting.
```

Monitor especially for drift on:
- Pages with young René (child or student) — model will want to make him cute
- Pages with Francine (page 11) — resist sentimentality in the art
- The dreams page (page 8) — keep surreal but painterly, not fantastical/cartoonish
