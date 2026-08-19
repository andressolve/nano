# Image prompts

Generated with `mcp__gemini-pro-thin__compose_images` (Gemini image endpoint), not the OpenAI/Codex path used for the two prior comics — see `00-PROJECT-BIBLE.md` provenance note.

## Finished page — `pages/page-01.png`

**Input images:**
1. `french/les-jeux-video/refs/ref-hugo-leo-gaming.png` — Hugo/Léo identity lock.
2. `french/demain-il-fait-beau/refs/ref-rain-cafe-football.png` — register/style guide only; none of its scene content (rain, café, football) appears on this page.

**Prompt (v1, sent to `compose_images`):**

> Use case: illustration-story. Asset type: finished one-page beginner-French comic.
>
> Input images: Image 1 is the approved Hugo/Léo identity reference. Image 2 is the approved supplemental reference from a prior comic (register/style guide only). Preserve Hugo's and Léo's faces, hair, skin tone, ages, proportions, everyday clothing, and the established clear-line visual register from these references. The references are identity and style guides, not edit targets. Do not include any rainwear, café interior, football, hot chocolate, or croissant from Image 2 in this new page.
>
> Primary request: Create one polished portrait comic page with exactly four large rectangular panels in a clean 2×2 grid. Tell one simple natural scene: Hugo and Léo stop a friendly older neighbor on a sunny street to ask where the library is; she tells them to go straight, then to turn left; they follow the directions and arrive at the library.
>
> Scene/backdrop: A pleasant, sunny contemporary French-feeling neighborhood — warm-stone and pale-stucco low buildings, planters, a few trees, blue sky. Panels 1–3 share one bright sidewalk corner. Panel 4 shows a quieter side street with a modest two-storey neighborhood library: warm-stone façade, tall arched ground-floor windows with clearly visible books on display inside, a plain wooden door, and a small unmarked round plaque above the door bearing only a simple open-book pictogram. No shop signage or lettering anywhere on any building.
>
> Subject/character locks: Hugo matches Image 1 exactly: ten years old, pale olive skin, tousled dark-brown hair, green overshirt over an orange T-shirt, charcoal trousers, red canvas trainers. Curious, friendly, slightly reserved. Léo matches Image 1 exactly: eleven years old, deep brown skin, short tight black curls, mustard-yellow hoodie, dark navy jeans, white trainers. Relaxed, expressive, warm. The neighbor is a friendly local woman in her sixties: light skin with soft weathered warmth, silver hair in a short neat bob, kind eyes, small silver earrings. She wears a moss-green knit cardigan over a cream blouse, a soft mid-grey skirt to just below the knee, and comfortable brown low-heeled shoes. She holds a slim leather lead attached to one small tan short-haired terrier that stays calmly at her side. She appears only in Panels 1, 2, and 3.
>
> Style/medium: Original all-ages Franco-Belgian clear-line adventure-comic illustration matching Image 1 and Image 2 — clean confident uniform black ink contours, flat warm colors, precise readable silhouettes, lively natural child and adult acting. No painterly gradients, no sketch lines, no hatching, no cross-hatching, no animation-still rendering.
>
> Composition/framing: Portrait 2:3 page (1024×1536). Exactly four large rectangular panels with clean white gutters, read top-left, top-right, bottom-left, bottom-right. No title bar, no page number, no inset panels, no bleed panels, no splash panel.
>
> Panel 1, top-left — The question: [balloon, Hugo] `Bonjour ! Où est la bibliothèque ?`
> Panel 2, top-right — Straight ahead: [balloon, woman] `Va tout droit.`
> Panel 3, bottom-left — Then left: [balloon, woman] `Puis, tourne à gauche.`
> Panel 4, bottom-right — There it is: [balloon, Léo] `La bibliothèque est là !`
>
> (Full panel-by-panel blocking, lettering block, constraints block, and avoid block as drafted by the planning agent — see agent transcript; condensed here for the record.)

**Result:** v1 generated successfully but failed critic review — see `QA.md`.

## Repair pass — `pages/page-01-candidate-v2.png` → promoted to `pages/page-01.png`

**Input images:**
1. `pages/page-01-candidate-v1.png` — the draft to preserve and repair.
2. `french/les-jeux-video/refs/ref-hugo-leo-gaming.png` — correct-identity reference for Léo.

**Prompt (repair, sent to `compose_images`):**

> Image 1 is the current draft of a four-panel French-language comic page; Image 2 is the locked character reference sheet for Hugo and Léo. Recreate Image 1 exactly, panel for panel, preserving the composition, the four panels' layout, the woman's identity and gestures, the library exterior, Hugo's appearance, and all four speech balloons with their exact existing text and tail placement unchanged. The ONLY corrections to make: (1) In every panel where Léo (the boy in the mustard-yellow hoodie) appears, correct his skin tone to deep brown and his hair to short tight black curls, exactly matching Léo's appearance in Image 2 — his clothing and pose stay as in Image 1. (2) Remove the small stray numeral "2" visible in the bottom white margin of Image 1, outside the panel grid — the page must have no text anywhere except the four existing speech balloons. (3) In Panel 1 (top-left), adjust the speech balloon tail so it clearly touches the speaking boy's mouth rather than ending in empty space above his head. Keep the exact same Franco-Belgian clear-line art register, flat colors, black contours, portrait 2:3 layout, and white gutters as Image 1. Do not alter panel count, balloon count, balloon text, the woman, the dog, or the library.

**Result:** approved on second critic pass — see `QA.md`.
