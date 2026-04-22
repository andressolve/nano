# Ratio: The Seeker — Style Guide (Vol 1)

Visual guide for Volume 1. Much of this is shared across both volumes; Vol 2 has its own style guide that narrows to the Brotherhood / theorem / fall palettes. Where rules apply to both, the rule is "SERIES" — where Vol 1 narrows it, the rule is "VOL 1".

## Overall aesthetic (SERIES)
Painterly realism, serious graphic novel register. Same visual DNA as *Cogito* and *Relativity*. Not cartoonish, not a children's book. Realistic proportions, adult faces, mature compositions.

**Always include in prompts:** "NOT a children's book. Serious mature graphic novel, realistic proportions. Painterly realism."

## Volume 1 palette: "warm, sunlit, eastern seeker"

Vol 1 is the warm volume. It lives in Mediterranean sun, Egyptian ochre, Babylonian star-indigo. It ends at golden-hour Croton. No ash, no grey dawn, no fire — those are Vol 2.

**Three sub-palettes across Vol 1:**

### Samos — amber coast (pages 1–4)
Gold and amber; pale Aegean blue; white-walled limestone villages; cypress green. Warm but clear. The forge (page 2) pushes toward red-orange from coals. Pherecydes's terrace (page 3) is olive-tree-dappled sun.

### Egypt — ochre and lapis (pages 5–7)
Hot ochre sand; warm red-brown sandstone; deep lapis sky; bone-white linen. Interiors have painted columns (red, ochre, blue) in shadowed depth. The Persian invasion page (page 7) lets a slash of smoke and sword-iron into the palette without fully tipping into Vol 2's darkness.

### Babylon — cobalt and star (pages 8–10)
Deep cobalt night skies; star-white points; warm torchlight amber on foreground figures; brick-red ziggurat silhouettes. Clay tablets are a warm grey. This is Vol 1's coolest palette.

### Return and Croton — homecoming gold (pages 11–17)
Back to amber Aegean for Samos (pages 11–13). Sea-spray cobalt for the crossing (pages 14–15). Ending on golden-hour Croton white-and-ivory (pages 16–17) — the destination.

## Format and layout (SERIES)
- **Aspect ratio:** 2:3 vertical (portrait), matches Descartes and Einstein
- **Panels:** 2–4 panels per page typically
- **Gutters:** thin, parchment-ivory (not black)
- **Captions:** small cream caption boxes, serif typography, top or bottom of panels. Narrator voice is omniscient and quiet.
- **Speech bubbles:** classical, clean white with serif text. Max 15 words per bubble.
- **Chalk-style labels:** used sparingly in Vol 1 (only for the hammer-ratios on page 2 and the rope-stretchers' triangle on page 6). Chalk-style labels in ALL CAPS, bold, hand-drawn feel.

## The math must READ (VOL 1 — lighter than Vol 2)

Vol 1 has two math-text pages. Both must render exactly.

- **Page 2 (The Hammers):** render the numerals "12 · 9 · 8 · 6" as chalk-style notation beside Pythagoras's wax tablet. These are the weights of the four hammers — the ratios 12:6 (octave), 12:8 (fifth), 12:9 (fourth). Do NOT add musical notation or symbols.
- **Page 6 (The Rope-Stretchers):** render the rope with 12 knots visible at regular intervals, arranged as a 3-4-5 triangle. Small chalk-style labels: "3", "4", "5" on the three sides. No equations, no "a²+b²=c²" — that is Vol 2's reveal.

No hand-waving. These diagrams are part of the reason the book exists.

## Character consistency (SERIES)
- Age-specific character references. In Vol 1, Pythagoras appears at **~10 (boy)**, **~20 (young man)**, and **~40 (mature-young, newly returned and then departing)**. The full-mature and elder Pythagoras are Vol 2.
- Always pass reference images into every page generation.
- When drift occurs, compose using two refs: the age-specific one for face shape, and a feature-anchor ref.
- **Face lock for Pythagoras (all ages):** thick straight dark brows + broad high forehead + aquiline strong nose. Repeat these in every prompt. When the model produces a generic handsome Greek face, regenerate composing with two refs.

## Pythagoras's appearance by age in Vol 1

- **Boy (~10, pages 1–2):** olive skin, tanned; dark brown tousled shoulder-length hair; thick straight brows; serious curious expression; cream wool short tunic (exomis); barefoot or leather sandals. Height and proportions of a real 10-year-old — NOT a chibi or cartoon child.
- **Teen (~14, page 3):** still boyish, hair slightly longer, still clean-shaven.
- **Young man (~20, page 4, and pages 5–6 shortly after):** short dark beard forming but sparse; shoulder-length dark hair; stronger but still wiry build; dark himation over cream tunic for travel; wooden walking staff.
- **Mid-to-late twenties (pages 7–10):** fuller beard, slightly weathered from travel, still dark-haired. Continues in cream and dark travel cloth.
- **Mature-young (~40, pages 11–17):** full dark beard with first threads of grey; shoulder-length dark hair greying at the temples; ivory himation over ivory chiton; upright, teacherly posture. This is the face that carries into Vol 2's theorem pages — same ref.

## Incidental characters' look
- **Pherecydes (page 3):** old Samian, ~70, long white beard, white hair, weathered face, sharp eyes, grey/ochre himation, seated with a papyrus scroll
- **Egyptian priest / rope-stretcher (page 6):** Egyptian man ~40, dark brown skin, shaved head, clean-shaven, white linen kilt, broad gold-and-lapis collar, bronze armbands, kohl around eyes
- **Babylonian Magus (pages 8–10):** older man ~60, lighter skin than the Egyptian, long grey-black beard, tall conical hat (blue or white, sometimes star-embroidered), long robes in deep blue and ochre
- **Polycrates (page 3 only):** distant figure on a palace balcony, purple robes, no facial specifics needed
- **The blacksmith (page 2):** muscular middle-aged man, leather apron, sooty face, one panel

## Settings rules (VOL 1)
- **Samos:** cypress and olive, NOT palm. White limestone cliffs. Blue-green Aegean.
- **Egypt:** sandstone, lapis-blue sky, painted temple columns, pyramids in distance. No camels in foreground (cliché).
- **Babylon:** ziggurat silhouettes, flat roofs, deep night sky, cuneiform tablets, bronze astronomical instruments. No minarets (Islamic, anachronistic).
- **Croton:** white-walled Ionic-order coastal Greek city, olive groves, Ionian Sea, golden hour. Terracotta accents but NOT the full red-roofed Roman city look.

## What to avoid (SERIES)
- Cartoon children's book aesthetics (big eyes, round features, bright primaries)
- Modern manga speed lines and chibis
- Cape-and-cowl superhero musculature
- Comic-sans or any casual font for captions
- Cluttered panel borders (keep gutters thin and quiet)
- Togas (Roman, wrong era and culture)
- Medieval pointed beards
- Minarets or domed mosques (wrong period for Babylon)
- Palm trees on Samos

## Text to render verbatim vs described (SERIES)
If specific text must appear, give the model the exact string. Never describe text conceptually on a math page.

- "12 · 9 · 8 · 6" (page 2) — render exactly
- "3", "4", "5" labels on the rope (page 6) — render exactly
- Samos, Egypt, Babylon, Croton — acceptable to render as lower-third place labels if useful
- Greek or cuneiform script on tablets (pages 8–10) — render as decorative script, does not need to be literally correct

## Prompt length discipline (SERIES)
2000-char limit on the MCP tools. Trim style boilerplate once the model has learned it. Keep character lock + exact text + panel layout + "NOT children's book" instruction.

## Reader-theme
Dark theme (same as Cogito and Relativity). Page-flipping with keyboard nav. Mobile-friendly. 5-question quiz at the end. Same CSS/JS DNA as the existing biographical readers.

## Landing-page card (for later)
Two separate cards in the landing `index.html`: one for Vol 1 (*The Seeker*), one for Vol 2 (*The Brotherhood*). Each with its own cover thumbnail and description. Match the format of the `house-of-atreus-vol1` and `house-of-atreus-vol2` cards.
