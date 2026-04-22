# The Invisible Forces — Style Guide

## Style Block (COPY VERBATIM TO EVERY PROMPT)

```
Art Style: 17th-century English and Dutch natural-philosophy painterly realism — austere farmhouse interiors, severe Cambridge chambers, grounded historical graphic novel aesthetic. Think Dutch Golden Age light filtered through Lincolnshire winter and Restoration science culture.
Color palette: Woolsthorpe stone gray, winter pewter, orchard moss, oak brown, parchment cream, candle amber, iron black, prism-spectrum accents used sparingly
Effects: Cool daylight through leaded windows, candlelit chiaroscuro, glass refractions, dust in the air, measured geometric line-work and orbital arcs emerging from real surfaces
```

## Visual Identity

This story spans 1642–1687 across rural Lincolnshire, Grantham, Cambridge, and London. It should not look like *Cogito* or *Relativity* copied over. It belongs to a harsher English world: limewashed walls, dark timber, cold seasons, plain rooms, orchard branches, black gowns, polished lenses, ink-stained paper.

The dominant visual register is **austere early-modern realism**. Newton's world is less socially warm than Descartes' and less urban-modern than Einstein's. The beauty comes from restraint: cold daylight, the amber of a candle, a sudden burst of spectral color through glass, the clean sweep of a geometric arc over rough paper.

### Palette by Movement

| Movement | Pages | Dominant Colors | Light Quality |
|----------|-------|-----------------|---------------|
| Broken beginnings | 2–4 | Winter gray, hearth brown, pale wool, frost white | Cold daylight softened by interior firelight |
| Grantham / formation | 5–6 | Schoolroom oak, market brown, field green, weather gray | Brighter outdoors, practical interior light |
| Cambridge awakening | 7–8 | Ink black, vellum cream, chapel stone, muted academic brown | Tall window light, disciplined shadow |
| Plague years / discovery | 9–15 | Woolsthorpe gray, orchard bark, prism color, candle amber | Quiet room light, sharp experimental highlights |
| Recognition and recoil | 16–18 | Royal Society dark wood, brass, paper cream, wary shadow | Public interiors, more contrast, less warmth |
| Halley to Principia | 19–24 | Deep ink black, manuscript cream, midnight blue, measured gold | Focused desk light, world shrinking to argument |

### Atmosphere Notes

- **Solitude is structural.** Newton should often be the only fully rendered figure in a room.
- **Color is rare, then meaningful.** The spectrum should feel astonishing because the rest of the book is restrained.
- **Objects matter.** Prism, quill, compass, pendulum, telescope tube, handwritten diagrams, orchard branch, apple, lunar arc.
- **Order emerges from matter.** Diagrams should appear on paper, slate, glass, or in the physical air of the page — never as generic classroom overlays.
- **Newton is not theatrical.** His intensity is mostly inward. The art should respect restraint.

## Science-Page Rules

These pages carry the book. They need their own discipline.

- Each science page should answer one main question.
- Prefer one experiment or one inference chain per page.
- Keep labels sparse and purposeful.
- If a diagram is needed, anchor it to a material object: a notebook page, chalkboard, sheet of vellum, windowpane reflection.
- Use captions to move the reasoning forward, not to summarize what the picture already shows.
- Let geometry feel exact but handmade.

### Text Density Guidance

Even with the stronger `gpt-image-2` text handling, do not overpack the page.

- **Speech bubbles:** ideally under 12 words
- **Caption boxes:** usually 1–3 per page
- **Science labels:** minimal, large, legible, and only if essential
- **Avoid:** dense paragraphs, tiny labels, textbook-style callout clutter

If a science page needs too much verbal scaffolding, split it into two pages rather than forcing it.

## Panel Style

- **Borders:** Thin dark lines, slightly rough, like inked edges on laid paper
- **Gutters:** Dark brown or near-black, 4–6px
- **Caption boxes:** Warm cream or pale parchment with dark serif text
- **Speech bubbles:** White with black outlines; short and direct
- **Thought text:** Use italicized caption boxes rather than thought bubbles
- **Mathematical notation:** Inked or chalked, precise, restrained, historically grounded in appearance

## Typography Guidance

- **Narration:** Third person, present tense, lucid and unsentimental
- **Newton's words:** Italicized in caption boxes; use only when they sharpen the page rather than decorate it
- **Dialogue:** Plain, accessible English; no fake archaic speech
- **Scientific text:** Exact where exactness matters (`white light`, `fluxions`, `the moon falls`, `inverse-square`) but never pseudo-technical for atmosphere alone

## What This Should NOT Look Like

- Children's book illustration
- Manga or anime styling
- Generic fantasy alchemy imagery
- Modern glossy concept art sheen
- Flat educational infographic aesthetics
- Excessive rainbow color everywhere because Newton worked on light
- An elderly wigged Newton in Book One unless explicitly foreshadowing much later life

## Anti-Drift Directive

If any page begins drifting toward softness, cuteness, or generic educational art, add this reinforcement:

```
STYLE REINFORCEMENT: NOT a children's book. Serious mature graphic novel. Austere 17th-century English historical realism. Realistic human proportions. Restrained palette. Cool window light, candlelit shadow, tactile wood, glass, paper, and stone.
```

Monitor especially for drift on:

- Young Newton pages — the model will try to sentimentalize him
- Prism pages — the model will over-saturate the spectrum if not restrained
- Fluxions and gravity pages — the model will try to flatten them into generic educational diagrams
- The final *Principia* page — the model may become pompous or overly celestial

## Continuity Markers For Newton Across Ages

1. Narrow face, not round even in childhood
2. Deep-set, watchful eyes
3. Long straight nose that becomes more prominent with age
4. Controlled mouth — often compressed, rarely open in broad expression
5. Dark brown hair through Book One, worn naturally rather than with a formal wig
6. Long, precise hands that look made for instruments, paper, and writing

## GPT Image 2 Production Notes

The current design assumes:

- reference-first workflow remains mandatory
- recurring character continuity is improved but not solved
- page lettering is improved but still should stay sparse
- multi-turn editing is useful for correcting local failures rather than regenerating entire pages
- hard science pages may need an initial composition pass and then a targeted refinement pass

Plan pages accordingly.
