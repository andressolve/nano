Builder brief — adversarial-heads-neutral-1 — candidate v1 — three-kingdoms-vol1

You are a reference-sheet builder. You generate exactly one candidate from the prompt below, write it to disk, write a non-gating audit, and stop. You never judge whether the sheet is good, never regenerate on your own opinion, never promote, and never open any other file in this book.

GENERATION. Codex in-app image generation on the ChatGPT subscription only. No API key, no image CLI, no separately billed path. One call. Size 1536 × 1024.
IMAGE INPUTS (attach exactly these, nothing else):
  books/three-kingdoms-vol1/refs/approved/01-liu-bei.png
  books/three-kingdoms-vol1/refs/approved/02-guan-yu.png
  books/three-kingdoms-vol1/refs/approved/03-zhang-fei.png
  books/three-kingdoms-vol1/refs/approved/04-cao-cao.png

PROMPT — issue this text exactly, nothing added, nothing removed:

----- BEGIN PROMPT -----
A critic-only comparison board, 1536 × 1024 landscape, built from the attached approved reference sheets. No lettering of any kind, no labels, no borders.

One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering, labels, rules, or props. Four costume-free heads from the four attached approved sheets in one even row at one head scale, each a true three-quarter view turned the same way, each with a closed mouth and a calm resting expression, crops ending at the upper neck with the full crown, both ears where visible, the whole jaw, and the full length of any beard shown, open paper between them: Liu Bei (broad compact oval, bare rounded chin, thin moustache, long heavy earlobes, sad almond eyes); Guan Yu (deep red face, upturned phoenix eyes, silkworm brows, long smooth black beard to the bottom edge, headscarf removed, hair only); Zhang Fei (square leopard head, round bulging eyes, bristling short whiskers all round jaw and cheeks, mouth closed); Cao Cao (narrow angular face, sharp cheekbones, narrow glittering eyes, slightly hooked nose, neat moustache and short pointed goatee). Faces identical to the sheets.

Their faces must remain structurally distinct even in profile, reduced scale, grayscale, partial hair, and travel clothes.

Lacquer and Dust. Bold, wet brush-and-ink line on warm, toothed mulberry paper, with flat matte washes of earth and mineral pigment: lamp-black ink, raw umber, loess yellow-ochre and dust grey for the land; and, laid flat and strong where people and banners carry them, cinnabar vermilion, malachite green, indigo, imperial purple, ivory, and the dull bronze and iron of armor. Late-Han China lit like a war film: hard white noon and long dust, smoke-orange firelight, brazier light in lacquered halls with real cast shadows and real depth, cold blue dawn. Visible brush line, visible paper tooth, ink and wash pooling at the edges of a stroke; lamellar iron, lacquered leather, hemp, silk, horsehair, rammed earth, grey tile, steel. Not smooth prestige-oil realism. No glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no anime proportions, no children's-book softness, no plastic 3D render, no blue-green landscape-scroll prettiness, no gold leaf.

Their faces must remain structurally distinct even in profile, reduced scale, grayscale, partial hair, and travel clothes.
----- END PROMPT -----

SAVE. Write the returned PNG byte for byte to books/three-kingdoms-vol1/refs/candidates/adversarial-heads-neutral-1-v1.png. Write the prompt text above, exactly as issued, to books/three-kingdoms-vol1/refs/candidates/adversarial-heads-neutral-1-v1.md.

AUDIT (a report, not a verdict). Write books/three-kingdoms-vol1/refs/candidates/adversarial-heads-neutral-1-v1.audit.md with: the file's pixel size as a script reports it (must be 1536 × 1024); whether all four views are present (three-quarter head, full length, strict profile, the named state) — for a plate, whether any figure appears; for a board, whether both attached characters appear and read as the same faces as their sheets; whether any lettering, label, watermark, or border appears; anything else you noticed. Then stop.

SUBMIT RULE. The candidate is submitted as it is, even if your audit says it failed. The only regeneration allowed without a critic verdict is for a failed generation — wrong dimensions, a corrupt or truncated file, an empty or refused result — and in that case delete the bad file and regenerate the same version once. Never regenerate because you dislike the drawing.

Reply with: the output path, its SHA-256, and the audit path. Nothing else.
