# The Boy Who Watched Birds — Style Guide

Visual register, palette, lettering, and the verbatim blocks that go into every page prompt.

## Register — paste verbatim into every prompt

> Oil-painting realism. NOT a comic. NO halftones, NO cel shading, NO ink linework. Painted brushwork, cinematic lighting, muted period palette. Renaissance and early-modern oil-portrait sensibility — the visual language of Verrocchio, Ghirlandaio, and the early Leonardo himself, then translated into landscape graphic-novel pages.

## Anti-drift directive — paste verbatim into every prompt

> NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting, cinematic composition.

## Audience-standard line — paste verbatim where useful

> First-time reader. Captions must be self-contained. No info-withholding. No jigsaw narration.

## Palette by act

The volume has three visual acts. Each act has a dominant warm/cool register that the prompt should specify.

### Act 1 — Vinci and Florence (Pages 1–6)
- **Time:** 1452 to ~1481.
- **Palette:** sun-warmed Tuscan hills, terracotta, olive green, raw umber, bone white, warm shadow. Verrocchio's workshop adds amber lamplight and pigment-stone gray.
- **Light:** Italian afternoon, diffused window light, glints on bronze tools.
- **Mood:** discovery, apprenticeship, the boy still looking up at adults.

### Act 2 — Milan, the court (Pages 7–18)
- **Time:** 1482 to early 1498.
- **Palette:** cooler. Sforza-court blue-gray stone, deep red velvet, cold silver, candle gold. The refectory of Santa Maria delle Grazie is white plaster, walnut tables, north light. Notebook pages are linen-cream with iron-gall ink shading toward sepia.
- **Light:** indoor candlelight and clerestory light. Cooler than Act 1.
- **Mood:** mastery, ambition, accumulation.

### Act 3 — The fall (Pages 19–22)
- **Time:** August 1499 to December 1499.
- **Palette:** ash, cold blue shadow, bronze still warm but dying, late-autumn ochre. The clay horse model in dust. The Last Supper wall already showing the first ghost-flakes.
- **Light:** late-day, low, going. End-of-something light.
- **Mood:** loss without melodrama; what survives is the notebook in the saddlebag.

## Lettering — the Honda formula, applied here

All narration lives **inside the image** as caption boxes. Reader UI does not duplicate the captions in HTML.

### Caption-box style — verbatim phrase per caption

> Off-white parchment box, dark serif text, readable.

For Act 2 Milan-court formality, optionally:

> Cream parchment plaque, hand-set serif type, readable, ink-on-paper.

For the primary-source letter page (P7) and notebook page (P9):

> Period typography. Render text exactly as quoted. Ink-on-cream paper.

### Speech-bubble style

Round, off-white, dark serif text. Tail explicitly anchored to the speaker. Keep dialogue **under 15 words** even on gpt-image-2.

### Lettering preamble per prompt

Open the lettering section of every prompt with:

> LETTERING — verbatim, render exactly:

Then list each text element with its position (`top caption band`, `lower-left caption box`, `speech bubble — TAIL POINTS TO LEFT FIGURE`, etc.) and the **exact quoted string** in quotation marks.

### Lettering restrictions block — paste at end of every prompt

> All words spelled correctly. Do not duplicate text. Do not invent extra captions. NO modern logos, NO watermarks, NO spurious signage. Render only the LETTERING listed above.

## Mirror-writing pages

For the notebook hero page (P9) and any page where Leonardo's hand is visible writing:

- Mirror writing should appear as **legible text reversed left-to-right**, with letters individually mirrored. The visible passage should be a real Leonardo phrase from the dossier (or a directly relatable observational note).
- For the closing-as-invention page (P22), captions over a notebook-page background can render as mirror writing where the script calls for it; non-mirror captions still appear in normal off-white boxes.

If text rendering of mirror writing fails, fall back: render the page as a normal cream notebook page with **handwritten cursive serif** text in iron-gall ink color, not mirrored, and note the choice in the production log.

## Rendered artifacts policy (primary-source pages)

When rendering a letter, manuscript page, or printed broadsheet as the visual subject (P7 letter to Sforza; P9 notebook; P22 closing), specify the artifact as a **physical object** in the scene:

- The letter sits on a desk, slightly tilted, candle to one side, sealed letter beside it.
- The notebook page is held open in Leonardo's hand or laid on a table; corners visible; ink stains and smudges welcome.
- The closing notebook page can fill the frame as the entire image — the page IS the panel.

## Anti-patterns — do not do these

- No bracketed lock-list prompt format (`[1] "INSCRIPTION..."`). Use natural prose.
- No full-width date strips. Render dates inside off-white caption boxes.
- No modern English alongside the Italian quote unless the script explicitly says to (translation in subtitle).
- No over-rendered halos, gold leaf, or ecclesiastical kitsch — these are oil portraits, not icons.
- No anachronistic facial features (Leonardo at 14 should not have a 19th-century novel-illustration face). Reference Quattrocento Florentine portraits — long noses, neat hair, restrained expression.

## Cover register

Painted oil portrait of Leonardo at ~45, in Milan, three-quarter view, half-shadowed in the manner of his own *Lady with an Ermine*. Behind him, slightly out of focus: the great clay horse model in the courtyard; on a table beside him, an open notebook with a sketch of bird wings and mirror-script. Title typography: hand-painted serif, period feel, large at top.
