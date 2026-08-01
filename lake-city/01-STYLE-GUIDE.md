# 01 — STYLE GUIDE

Register approved by the user 2026-07-25 from a three-way style test. The winning sample is **`style-samples/sample-A-codex-inkline.png`** — look at it before generating anything, and look at it again if a page starts to feel off. Rejected: painted-cinematic (too close to the rest of the collection, and painted realism cannot hold across four small dialogue panels a page) and mural-on-plaster (beautiful, too muted for action, bubbles untested).

---

## STYLE BLOCK — paste verbatim into every prompt, block 2

> STYLE: Bold ink-line comic art with FLAT vivid color — clean confident black linework, flat saturated color fills, minimal soft rendering, graphic and heroic. The linework and shape language are informed by Mesoamerican codex painting: strong black contours, stylized stepped and scrolling forms for water, smoke and cloud, ornament rendered as clean flat pattern. Palette: turquoise and jade, cochineal red, ochre and maize yellow, lime-white, obsidian black.

## ANTI-DRIFT DIRECTIVE — paste verbatim into every prompt, block 3

> NOT a children's book. Serious mature graphic novel, realistic heroic proportions, no cuteness, no oversized eyes, no pastel softness.

For any panel featuring the protagonist or another youth, append to the character lock:

> Realistic teenage anatomy. NOT cute, NOT mascot proportions, NOT oversized eyes.

These two blocks are non-negotiable. Without them the model drifts toward children's-book aesthetics within three pages.

---

## What the register refuses

- NO painterly rendering, NO oil-paint brushwork, NO photographic realism.
- NO halftone dots, NO screentone, NO manga speed-lines.
- NO airbrushed gradients. Color arrives in flat fields; modelling is done with line, not blur.
- NO watercolor bleed, NO sketchy scratchy linework. The line is confident and closed.
- NO modern anything: no logos, no watermarks, no signatures, no anachronistic objects.

## Palette

| Role | Color | Where it lives |
|---|---|---|
| **The city / the water** | turquoise + jade | The lake, canals, jade ornament, the feathers of rank. **The volume's signature accent.** |
| Blood, rank, the temple | cochineal red | Painted architectural bands, warrior devices, the shrine of the war god |
| Earth, cloth, the road | ochre, maize yellow, warm brown | Commoner cloth, dust, maguey, plaster in shadow |
| Stone, light | lime-white | The city's whitewashed buildings — the city should read as *pale and clean* against the blue |
| Line, hair, glass | obsidian black | All contour; obsidian blades read as black mirrors |

**The turquoise is the book's meaning, not just its color.** It saturates the city pages and it is at its most intense on the arrival pages. In Books Two and Three it drains. Do not spend it early on dull scenes — Tlaxcala and the road are ochre-and-dust country, and the lake should hit like a slap.

## Page format & panel geometry

- **1536×1024, 3:2 landscape, `quality: "high"`.** Never portrait. Never `low`/`medium` (caption legibility collapses).
- **3–4 panels per page.** State the grid explicitly in the prompt every time. Vague layouts render inconsistently.
- Validated layouts to draw from:
  - `THREE panels: two equal panels across the TOP, one WIDE panel across the BOTTOM. Reading order: top-left, top-right, then the wide bottom panel.`
  - `THREE panels in a ROW, equal width. Reading order: left, center, right.`
  - `FOUR panels: one WIDE panel across the TOP, three equal panels across the BOTTOM.`
  - `TWO panels: one tall narrow panel on the LEFT, one large panel on the RIGHT.`
  - **Splash** (single full-bleed image, no gutters) — reserved for the four hero pages listed in the script. Do not spend splashes casually; their power is scarcity.
- Always include: `clean solid-black panel borders and clear white gutters between all panels.`
- **One-shot whole-page bake.** The entire page — every panel and every piece of lettering — is produced in a SINGLE call. Never generate panels separately and composite. Never add text via code; the user's standing note is that code-lettering never works for him, and gpt-image-2's in-image text is strong enough.

## Lettering

Open the lettering section with this exact trigger phrase, always:

> LETTERING — verbatim, render exactly:

Then list every text element with its panel, its speaker, and the exact quoted string. Close every prompt with the restrictions block:

> All words spelled correctly. Do not duplicate text. Do not invent extra captions. DO NOT include any quotation marks inside speech bubbles — the bubble shape is the quote. NO modern logos, NO watermarks, NO spurious signage.

Rules:

- **Density: do not hold back.** ~8 text elements and ~75 words per page is validated and safe. Multiple bubbles per panel plus caption boxes is normal and wanted. The earlier volumes in this collection were too terse; this one should breathe. Keep each *individual* element legible — no single 40-word bubble.
- **Speech bubbles:** rounded, off-white, dark serif text, tail explicitly described and pointed at a named visible figure (`tail pointing to the boy in the white cloak on the LEFT`). Never leave a tail unassigned — that is how bubbles get attached to the wrong speaker.
- **Caption boxes:** small rectangles, off-white / pale bark-paper, dark serif text, anchored to a stated corner of a stated panel. Our narrator's voice lives here, past tense, first person.
- **Nahuatl words always carry an English helper in the same panel**, formatted as an em-dash gloss: `tlatoani — the Speaker, their king`. Ornamental text too small to read needs no helper.
- No sound effects. No shouted display lettering. This book is carried by talk, not bangs.

## Camera & staging

- The city is shot **from below and from far away**; our boy is shot **close**. That contrast is the whole visual argument of the volume — a small person inside an enormous thing.
- Faces must be readable when identity matters. If a locked character is smaller than about a fifth of the panel height, the model will drift; either move the camera in or accept them as an unnamed silhouette.
- Crowds are a *texture*, not a cast. Never put a locked face in the middle of a crowd panel.
- Recurring compositional motif: **straight lines.** The causeways, the canals, the grid of the city — the Mexica world is ruled, geometric, engineered. Tlaxcala is crooked and hilly. Let the panels say this without a caption saying it.

## Sacrifice, violence, and moderation

The subject is genuinely violent and the book will not lie about it. It also will not depict it.

- **Human sacrifice is real in this world and is handled through aftermath, implication, and testimony** — a scrubbed stone, a stain, a priest's stained hands, the boy's face while he listens, someone's flat description of what happened to his father. Never the act, never a body on the stone, never a blade at a chest.
- **The skull rack** may appear as architecture at distance, in silhouette, described by a caption. Never a close study.
- The Cholula pages are told through **the boy outside the courtyard**: smoke over a wall, sound described in a caption, faces of people listening. No massacre depicted.
- Battle pages: motion, dust, silhouette, and the moment *before* or *after*. No wounds, no gore.
- Known moderation trap from prior volumes: **a page whose entire subject is a killing will be rejected even when softened.** The fix is never more softening — it is to reframe the page's subject onto the artifact, the witness, or the aftermath. If a page gets refused, change what the page is *about*, then regenerate.

## Reader (built last)

- Dark theme, `#15171c`, Palatino serif, off-white text, `max-width: min(1400px, 96vw)`.
- Accent: **turquoise `#35a7a0`.**
- Edge-anchored circular ←/→ arrows, vertically centered; keyboard arrows + spacebar; click-left-third / click-right-two-thirds; swipe on mobile; top progress bar; lazy-prefetch of the next page.
- **Footer concept-strip: the four acts** — `The Hatred · The Road · The City · The Silence` — lighting the active act per page, hidden on the cover.
- End interstitial before the quiz, then a 5-question **WHY** quiz: substantive distractors of similar length, shuffled correct-answer positions, no answer guessable by length or specificity.

---

## The prompt template — six blocks, do not reorder

```text
LAYOUT:
Landscape multi-panel comic page. [PANEL GRID, verbatim from the script.]
Clean solid-black panel borders and clear white gutters between all panels.

STYLE:
[STYLE BLOCK, verbatim from above.]

ANTI-DRIFT:
NOT a children's book. Serious mature graphic novel, realistic heroic
proportions, no cuteness, no oversized eyes, no pastel softness.

RECURRING CHARACTERS — keep them IDENTICAL in every panel:
[Character lock blocks, verbatim from 02-CHARACTERS.md. Visual description
only — never the historical name.]

PANELS:
PANEL 1 — [who / where / action / camera]
PANEL 2 — [...]
PANEL 3 — [...]

LETTERING — verbatim, render exactly:
PANEL 1, caption box, upper left: "..."
PANEL 1, speech bubble, tail pointing to [named visible figure]: "..."
[...]

All words spelled correctly. Do not duplicate text. Do not invent extra
captions. DO NOT include any quotation marks inside speech bubbles — the
bubble shape is the quote. NO modern logos, NO watermarks, NO spurious signage.
```

Block order is load-bearing. Layout and style first pin the register before subject content can pull it. Anti-drift early so it dominates when a teenage protagonist enters the lock. Lettering last so caption words don't bleed onto clothing and props.
