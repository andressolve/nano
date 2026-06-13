# 02 — CHARACTERS

All appearance is INFERRED (no portrait of young Gauss exists). Locks describe the
VISUAL only — never the name. Re-Read each ref PNG before using it in a page prompt.

Ref generation: 1536×1024 landscape, neutral warm-toned plain background, portrait +
partial full body, neutral expression, "no text, no labels." Style/register/anti-drift
blocks prepended to every ref prompt.

---

## Gauss — four age phases

### ref_gauss_child.png (~7, poor schoolboy) — pages 2, 3, 4
LOCK: A boy of about seven. Fair, slightly unkempt sandy-blond hair, broad forehead, wide-set clear blue eyes, round determined face, fair skin. Sturdy not delicate, a little thin. Wears a coarse undyed linen shirt, plain brown wool waistcoat, simple breeches, gray woolen stockings, rough leather shoes. No wig. A laborer's son who is too watchful for his age. Realistic child anatomy. NOT cute, NOT mascot proportions, NOT oversized eyes.

### ref_gauss_youth.png (~15, Collegium, newly patronized) — pages 5, 6
LOCK: A youth of about fifteen. Sandy-blond hair grown a little longer and tied back in a short queue, broad forehead, clear blue eyes, fuller serious face, fair skin, sturdy build. Now in modest but respectable student dress: a dark blue-gray woolen frock coat, buff waistcoat, plain white linen stock at the throat, breeches, buckled shoes. The careful look of a poor boy given a chance he means to keep. No powder.

### ref_gauss_student.png (~18–19, Göttingen student) — pages 7, 8, 9, 10, 11
LOCK: A young man of about eighteen or nineteen. Sandy-blond hair, natural, short and side-swept (no wig, no powder, 1790s fashion), broad forehead, intense blue eyes with a slightly heavy-lidded inward look, fair skin, sturdy medium build. Dark charcoal coat with a high collar, white cravat, plain waistcoat. Often carrying a notebook or slate. An intense, absorbed, watchful expression. Serious mature proportions.

### ref_gauss_young_man.png (~24, post-Disquisitiones) — pages 12, 13, 14, 15, 16, 17
LOCK: A young man of about twenty-four. Sandy-blond hair short and side-swept in early-1800s Empire style, broad forehead, calm confident blue eyes, fair skin, sturdy build, clean-shaven. A well-cut dark coat, high white linen stock/cravat, dark waistcoat — a young gentleman-scholar, no longer poor. Composed, self-possessed, quietly certain.

---

## ref_dorothea.png — Gauss's mother — pages 1, 2, 5
LOCK: A working-class German woman, late 30s to 40s, plain and strong-featured, fair weathered skin, light hair drawn back under a simple white linen cap, a coarse dark dress with a plain apron and a kerchief at the shoulders. Reddened hands from labor. A direct, intelligent, fiercely tender gaze. The face of a maid-turned-mother who cannot read but misses nothing. Realistic, not idealized.

## ref_father.png — Gauss's father (optional; prose-described on P2) — page 2
LOCK: A poor German laborer, 40s, broad and worn, short brown hair, weathered ruddy face, calloused hands, plain coarse working clothes — undyed shirt, leather jerkin, heavy breeches. A tired, practical, unsmiling man, not unkind but hard-pressed. (Single appearance — may be carried by prose if ref budget is tight.)

## ref_duke.png — Carl Wilhelm Ferdinand, Duke of Brunswick — page 5
LOCK: A German aristocrat of the 1790s, around sixty, dignified, gray hair powdered and dressed, lean intelligent lined face, fine dark blue military-cut coat with gold braid and a sash, white stock, an order/medal at the breast. The bearing of an enlightened prince — measured, curious, benevolent. Period-accurate, NOT a costume; a real man of rank.

## ref_buttner.png — J. G. Büttner, schoolmaster — page 3
LOCK: A German village schoolmaster of the 1780s, 50s, stout, balding with gray side hair, stern florid face, small spectacles, a dark threadbare coat and white stock, holding a switch/cane. The look of a man who rules a crowded poor classroom by fear and is about to be astonished. Period-accurate.

## ref_bartels.png — Johann Martin Bartels, teaching assistant — pages 3, 4
LOCK: A young man of about eighteen to twenty (the schoolmaster's young assistant), slim, eager, kind, brown hair tied back, plain dark coat and white stock, ink-stained fingers, carrying books. An intelligent encouraging face — the first person to take the boy seriously. Period-accurate, NOT a child.

## ref_heyne.png — Christian Gottlob Heyne, classicist — pages 7, 8
LOCK: A distinguished German scholar of the 1790s, around sixty-five, refined and eloquent, thin silver hair, fine intelligent ascetic face, small round spectacles, a scholar's dark gown over a coat and white stock, surrounded by classical books and a marble bust. The embodiment of the life of WORDS — learned, persuasive, the path Gauss almost took. Dignified, warm-eyed.

(Kästner — the dull math professor — appears once on P7 and is carried by prose:
"a heavyset elderly professor, powdered wig, bored half-lidded eyes, a dusty math
text" — no ref.)

---

## ref_heptadecagon.png — the 17-gon construction (object) — pages 9, 10, 17
A clean geometric construction drawing on warm ivory paper / pale slate: a regular
seventeen-sided polygon inscribed in a circle, drawn in dark ink with faint compass
arcs and straightedge lines still visible, a few compass-point pricks, a pair of
brass dividers (compass) and a straightedge resting beside it. Precise, elegant,
hand-drawn-by-a-genius feel. NOT a printed diagram — a working construction. Plain
background. (Used as a locked prop across the hinge and closing pages.)

---

## Composite plate needed
- **composite_p3_classroom.png** — Gauss child + Büttner + Bartels, for the summation page (3 named characters). Build by local PIL stitch of the three validated refs (preferred) or edit_image anchored on Büttner. Pass as single imagePath for P3.

## Multi-character strategy per page
- P3 (3 chars): composite plate.
- P5 (Gauss youth + Duke, +Dorothea background): lock the Duke's face (most distinctive — powdered aristocrat), describe Gauss youth in prose with strong continuity (queue, blue-gray frock coat).
- P7/P8 (Gauss student + Heyne): lock Heyne (distinctive — spectacles, silver hair, gown), describe Gauss student in prose.
- All other pages: single locked character via edit_image.
