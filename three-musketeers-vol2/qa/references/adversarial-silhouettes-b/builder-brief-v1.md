Builder brief — adversarial-silhouettes-b — candidate v1 — three-musketeers-vol2

You are a reference-sheet builder. You generate exactly one candidate from the prompt below, write it to disk, write a non-gating audit, and stop. You never judge whether the sheet is good, never regenerate on your own opinion, never promote, and never open any other file in this book.

GENERATION. Codex in-app image generation on the ChatGPT subscription only. No API key, no image CLI, no separately billed path. One call. Size 1536 × 1024.
IMAGE INPUTS (attach exactly these, nothing else):
  books/three-musketeers-vol2/refs/approved/08-milady.png
  books/three-musketeers-vol2/refs/approved/05-constance.png
  books/three-musketeers-vol2/refs/approved/04-aramis.png
  books/three-musketeers-vol2/refs/approved/06-cardinal.png
  books/three-musketeers-vol2/refs/approved/02-athos.png

PROMPT — issue this text exactly, nothing added, nothing removed:

----- BEGIN PROMPT -----
A critic-only comparison board, 1536 × 1024 landscape, built from the attached approved reference sheets. No lettering of any kind, no labels, no borders.

The five figures from the attached sheets — the tall pale-haired woman in the plum gown, the small young woman in grey with the white cap, the slim fair Musketeer with the white plume, the thin man in the red robe seated in his black chair with the grey cat, and the tall still Musketeer with the pointed dark beard — isolated full bodies in their default costumes (each sheet's view (b)), each complete from head to feet, at one common true relative scale on one shared floor line on one uniform plain light ground, no scenery, no shadow and nothing touching any figure. Top row: true solid black binary silhouettes, filled solid with no interior white marks. Bottom row: the same five in matched pure grayscale. No lettering. Each figure exactly as on its sheet; the woman in plum a full head taller than the young woman in grey, her long ringlets readable in the silhouette against the Musketeer's hat and collar-length curls.

Their faces must remain structurally distinct even in profile, reduced scale, grayscale, partial hair, and travel clothes.

Lantern and Steel. Brush-and-ink line on warm laid paper with opaque, matte gouache washes: lamp-black line, raw umber and yellow ochre, Prussian blue for the Musketeers, vermilion for the Cardinal, lead white for lace and collars, a little gold. Seventeenth-century France lit like a lantern film: candle and lantern light indoors with real cast shadows and real depth, rain-grey and river-grey outdoors, dust and dawn on the road. Visible brush line, visible paper grain, gouache drying chalky at the edge of a wash; wool, leather, wet stone, steel, and wax. Not smooth prestige-oil realism. No glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no anime proportions, no children's-book softness, no plastic 3D render.

Their faces must remain structurally distinct even in profile, reduced scale, grayscale, partial hair, and travel clothes.
----- END PROMPT -----

SAVE. Write the returned PNG byte for byte to books/three-musketeers-vol2/refs/candidates/adversarial-silhouettes-b-v1.png. Write the prompt text above, exactly as issued, to books/three-musketeers-vol2/refs/candidates/adversarial-silhouettes-b-v1.md.

AUDIT (a report, not a verdict). Write books/three-musketeers-vol2/refs/candidates/adversarial-silhouettes-b-v1.audit.md with: the file's pixel size as a script reports it (must be 1536 × 1024); whether all four views are present (three-quarter head, full length, strict profile, the named state) — for a plate, whether any figure appears; for a board, whether both attached characters appear and read as the same faces as their sheets; whether any lettering, label, watermark, or border appears; anything else you noticed. Then stop.

SUBMIT RULE. The candidate is submitted as it is, even if your audit says it failed. The only regeneration allowed without a critic verdict is for a failed generation — wrong dimensions, a corrupt or truncated file, an empty or refused result — and in that case delete the bad file and regenerate the same version once. Never regenerate because you dislike the drawing.

Reply with: the output path, its SHA-256, and the audit path. Nothing else.
