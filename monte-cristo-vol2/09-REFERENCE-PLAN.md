# Reference Plan — 23 sheets, approved as a system

**Nothing generates a page until every character visibly on that page has an
approved permanent lock.** Not just-in-time. A prior run of this method replaced
the up-front reference system with a just-in-time one and finished with an empty
`refs/approved/` and 26 pages on disk.

Locks live in `refs/approved/`. A sheet in `refs/` that has not been promoted to
`refs/approved/` is not a lock and may not be attached to a page prompt.

---

## Canvas and register — for every sheet on this list

**1536 × 1024, 3:2 landscape, RGB PNG.** Reference sheets are landscape; the
story pages are portrait 1024 × 1536. **This is not an inconsistency and must
not be "fixed."** It is inherited from Volume I, where landscape sheets fed
landscape pages; here the sheet stays landscape because four views across a wide
canvas is what a lock needs, and the page-level format lock is enforced
separately in the page prompts.

Register, verbatim in every **generative** sheet prompt — **Velvet Cinema**, from
`monte-cristo/01-STYLE-GUIDE.md`:

> Mature historical graphic-novel realism painted in layered matte gouache and
> opaque watercolor over sparse charcoal and ink construction. Broad visible
> brushstrokes, simplified interlocking color shapes, bold shadow masses,
> selective hard edges at faces and hands, tactile cloth, stone, wood, paper,
> wax and metal, expressive anatomically credible faces, cinematic blocking
> without photographic lens effects.
>
> **Not** smooth prestige-oil realism. No glossy game-concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no oil-painting pastiche, no
> anime proportions, no children's-book softness, no generic grimdark.

Every character sheet closes with the anti-collision clause, verbatim:

> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.

**No sheet carries lettering of any kind** — no name plates, no labels, no
captions. Labelled sheets teach the page model to letter the art.

Sheets 10, 11 and 23 are deterministic transport artifacts, not generative
image calls. They may crop, normalize, silhouette or place already approved
pixels only as specified below. They may not repaint, invent, relight or alter
character identity, setting design or object design.

---

## Anchoring — the Volume I inheritance

Volume I shipped. Its approved references are the identity authority and the
returning cast must be **recognisably the same people**, aged forward. Each
anchor below is attached as an image input to its sheet generation; the sheet is
an ageing pass, not a redesign.

| Sheet | Anchor | Ageing job |
|---|---|---|
| 01 the Count | `monte-cristo-expanded/refs/02-count-v2.png` | 1829 → 1838, **+9 years** |
| 02 Mercédès | `monte-cristo-expanded/refs/07-mercedes-1838-v2.png` | **none** — already 1838; wardrobe only |
| 03 Fernand | `monte-cristo-expanded/refs/05-fernand-1815-v2.png` | 1815 → 1838, **+23 years.** The volume's largest ageing job |
| 06 Danglars | `monte-cristo/refs/11-danglars-1815.png` | 1815 → 1838, **+23 years** |
| 08 Villefort | `monte-cristo-expanded/refs/01-villefort-1815-v2.png` | 1815 → 1838, **+23 years** |

**Edmond's cross-volume invariant** (`01-STYLE-GUIDE.md`) is binding on sheet 01
and on every page he is on. It survives age, weight, hair and costume:

> deep-set black-brown eyes · strong straight brow · long clean nose · high
> cheekbones · a slight asymmetry at the left corner of the mouth · a poised
> right hand that becomes still before a decision · the habit of occupying a
> doorway before entering a room.

Albert, Haydée and Beauchamp are **new**. They have no anchor and are designed
here — which is exactly why their collision lanes are the tightest in the book.

---

## Sheet manifest

Character sheets 01–09 gate pages. Boards 10–16 and 22 gate nothing but are
required inputs to the reference critic. Setting and object plates 17–21 are
generation inputs to the pages named. Sheet 23 is a deterministic page-input
carrier used only to keep Page 33 within the in-app five-reference limit.

| # | Sheet | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|
| 01 | The Count, 1838 | P1 | **P1** | Vol I 02 |
| 02 | Mercédès, 1838 | P11 | **P7** (silent, distant) · **P11** speaking | Vol I 07 |
| 03 | Fernand, 1838 | P8 | **P8** | Vol I 05 |
| 04 | Albert | P7 | **P7** | new |
| 05 | Haydée, 27 | P2 | **P2** | new |
| 06 | Danglars, 1838 | P9 | **P9** | Vol I 11 |
| 07 | Beauchamp | P27 | **P27** | new |
| 08 | Villefort, 1838 | P9 | **P9** | Vol I 01 |
| 09 | Janina 1822 board — Haydée at eleven, and her mother | P20 | **P20** | sheet 05 |
| 10 | Neutral head board — all eight principals | — | — | 01–08 |
| 11 | Grayscale silhouette board — all eight | — | — | 01–08 |
| 12 | Adversarial — Albert / the Count · **highest risk** | — | — | 01, 04 |
| 13 | Adversarial — Albert / Beauchamp · **high risk** | — | — | 04, 07 |
| 14 | Adversarial — Fernand / the Count | — | — | 01, 03 |
| 15 | Adversarial — Haydée / Mercédès | — | — | 02, 05 |
| 16 | Adversarial — Danglars / Villefort | — | — | 06, 08 |
| 17 | Setting — the Count's house, 30 Champs-Élysées | — | P1 | new |
| 18 | Setting — the Morcerf house and the general's staircase | — | P6 | new |
| 19 | Setting — the Chamber of Peers | — | P30 | new |
| 20 | Setting — Janina, and the market at Constantinople | — | P19 | new |
| 21 | Key objects board | — | P8 | new |
| 22 | Live-pair proof, unlettered — Albert and the Count | — | — | 01, 04 |
| 23 | Page 33 Chamber + objects carrier, unlettered | P33 | **P33** | 19, 21 |

**Generation order:** 01 → 03 → 04 → 05 → 07 → 02 → 06 → 08 → 09, then boards
10–16, then 22, then plates 17–21, then deterministic carrier 23. The Count
first because everything collides with him; Fernand, Albert, Haydée and
Beauchamp early because they carry the four risky lanes; Villefort and Danglars
last of the faces because they are the cheapest to redraw. Sheet 23 is built
only after sheets 19 and 21 are approved.

---

## Standing rules

- **Any character on two or more pages gets a sheet.** Prose locks are banned
  for recurring cast.
- **Absent lookalikes are critic-only rasters.** Never attach a lookalike to a
  generation as a negative example — the model draws what it is shown. Sheets
  12–16 exist for the critic's eye, not the builder's prompt.
- **Young Edmond from Volume I is reserved and unused.** Loose raven curls, open
  white shirt, red-brown sash: that identity stack does not appear anywhere in
  this volume, on any figure, background included.
- Unnamed and background figures may never carry a complete identity stack. The
  six reserved stacks are listed in `04-CHARACTER-LEDGER.md`.

---

# Part 1 — Character sheets

Each sheet is four views on one landscape canvas: **(a)** three-quarter head and
shoulders, neutral expression, even light; **(b)** full-length standing figure,
default costume, habitual posture; **(c)** strict profile, same light; **(d)**
the one state the script actually demands, named per sheet. No other views. No
turnaround grids, no expression sheets, no props not listed.

---

## Sheet 01 — THE COUNT OF MONTE CRISTO, 1838

**Attach:** `monte-cristo-expanded/refs/02-count-v2.png`
**Output:** `refs/01-count-1838.png`
**Blocks:** every page. Generate first.

> Create one flattened character reference sheet at exactly **1536 × 1024, 3:2
> landscape, RGB PNG**, four views of **one single man** on a plain neutral
> warm-grey ground. No text, no labels, no name plates, no borders.
>
> `[REGISTER BLOCK]`
>
> The attached reference is this same man nine years younger. **Age him forward
> nine years to forty-two.** Preserve exactly: deep-set black-brown eyes, strong
> straight brow, long clean nose, high cheekbones, hollow temples, cultivated
> pallor, and a slight asymmetry at the left corner of the mouth. He is
> **clean-shaven**, with a swept-back black wave carrying the first grey at the
> temples. Tall, columnar, unnaturally still. At forty-two he is slightly
> fuller in the face than the attached reference — the starvation now reads as
> discipline rather than damage. Do not thin him further and do not soften him.
>
> **Costume: unrelieved black**, 1838 Paris evening dress — black tailcoat,
> black waistcoat, black stock, white shirt-linen only at the throat and cuff.
> He is the only unbroken black vertical in any room.
>
> Four views, left to right:
> 1. Three-quarter head and shoulders, neutral expression, even light.
> 2. Full-length standing figure, arms at rest, the columnar stillness.
> 3. Strict profile, same light.
> 4. **The poised right hand** — hand and forearm only, larger, the hand gone
>    still in the instant before a decision. No face in this view.
>
> He must never be confused with a heavy-set moustached soldier of forty-six, a
> narrow pale rigid magistrate of fifty-three, or **a young man of twenty-two
> with chestnut hair and a pale waistcoat.** Differentiators that must survive
> grayscale and thumbnail: clean-shaven face, full swept-back black wave,
> pallor, columnar slimness, unrelieved black value.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 02 — MERCÉDÈS, COMTESSE DE MORCERF, 42

**Attach:** `monte-cristo-expanded/refs/07-mercedes-1838-v2.png`
**Output:** `refs/02-mercedes-1838.png`
**Blocks:** P11 onward. (She is visible but distant and silent on P7; that panel
may generate on this sheet or be held until it is approved — hold it.)

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> The attached reference is this same woman in the correct year and needs **no
> ageing at all.** Preserve exactly: decisive dark eyes, straight nose, lean
> mature cheeks, **visible lower-lid and temple lines**, restrained grey threads
> at the temple, dark hair sculpted into a formal 1838 Paris coiffure, still
> upright carriage. She is **forty-two and visibly forty-two.**
>
> **Do not youth-wash her.** A beautiful but smoothed face is a defect. The
> lower-lid lines, the temple lines and the grey are load-bearing and must be
> present in every view.
>
> Four views:
> 1. Three-quarter head and shoulders, neutral, even light.
> 2. Full-length standing, **burgundy-black vertical evening gown**, formal, the
>    upright carriage.
> 3. Strict profile, same light.
> 4. **Travelling black** — full-length, a plain dark travelling dress and
>    outdoor cloak, no jewellery, hair simpler. This is how she comes to a house
>    at night alone and how she leaves Paris.
>
> She must never be confused with a woman of twenty-seven with long unbound
> black hair and crimson-and-gold eastern embroidery. Differentiators that must
> survive grayscale and thumbnail: age, sculpted formal hairline, fitted French
> silhouette, restrained dark palette.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 03 — FERNAND MONDEGO, COMTE DE MORCERF, 46

**Attach:** `monte-cristo-expanded/refs/05-fernand-1815-v2.png`
**Output:** `refs/03-fernand-1838.png`
**Blocks:** P8 onward. **The volume's largest ageing job — expect revisions.**

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> The attached reference is this same man at twenty-three. **Age him forward
> twenty-three years to forty-six.** Preserve exactly: broad square jaw, heavy
> black brows set low and close, deep-set close dark eyes, weathered ruddy-olive
> Catalan skin coarser than any other face in this book.
>
> Add, as the primary marker of the intervening years: a **heavy iron-and-black
> military moustache**, grown after the attached reference was made; black hair
> **receding at the temples** and gone iron-grey at the sides; a thickened neck
> and a heavy upright soldier's build. He has spent twenty-three years
> constructing a person who could not have done what he did, and the
> construction shows — he is a man wearing his own evidence.
>
> Four views:
> 1. Three-quarter head and shoulders, neutral, even light.
> 2. Full-length standing, **general's evening dress with a chest of
>    decorations** — orders, ribbons, wax-red seals and old gold, worn and
>    polished and displayed.
> 3. Strict profile, same light.
> 4. **The same man in his shirtsleeves in an unlit room, coat off**,
>    decorations gone, holding a flat case. Same face, same build, everything
>    else stripped.
>
> The moustache and the receding hairline are load-bearing and must be present
> in all four views. He must never be confused with a clean-shaven pallid
> columnar man of forty-two in unrelieved black. Differentiators that must
> survive grayscale and thumbnail: moustache mass, hairline, thickened build,
> weathered skin value.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 04 — ALBERT DE MORCERF, 22 · NEW · highest collision risk

**Attach:** `refs/approved/01-count-1838.png` **as a same-sheet contrast only**
if the tool supports it without copying the face; otherwise generate standalone
and rely on sheet 12 for the adversarial check.
**Output:** `refs/04-albert.png`
**Blocks:** P7 onward.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> A **new** character, designed here: a French gentleman of **twenty-two** in
> 1838 Paris. He is the son of a self-made general and the volume's brightest
> figure.
>
> Structure: his mother's wide-set direct eyes and mouth; his father's jaw,
> **softened and un-weathered**; **chestnut-brown hair — never raven black, never
> black** — worn short with a neat side part in the 1838 fashion; fair-olive skin
> several values **lighter** than any other man in this book; slim, upright,
> unmarked by any work; clean-shaven with no side whiskers. His default
> expression is **open, mobile and quick to smile** — he is the only face in the
> volume that is not guarding something.
>
> **Costume: the volume's brightest values** — a pale cream or dove waistcoat, a
> coloured neckcloth, a dark coat that is nevertheless lighter and less absolute
> than unrelieved black.
>
> Four views:
> 1. Three-quarter head and shoulders, **the open quick-to-smile default**.
> 2. Full-length standing, evening dress with the pale waistcoat.
> 3. Strict profile, same light.
> 4. **Bareheaded at dawn in an overcoat, hat in hand, face closed** — the same
>    young man with all the brightness gone out of the expression. Costume value
>    stays light; only the face changes.
>
> **He must never read as a young version of the black-clad count, and never as
> a sandy-haired stooped young journalist in small oval spectacles.**
> Differentiators that must survive grayscale and thumbnail: hair colour
> (chestnut, not black, not sandy), skin value (light), costume value (bright),
> age (twenty-two), expression default (open), and **no spectacles ever**.
>
> He must never carry loose raven curls, an open white shirt, or a red-brown
> sash. That identity stack belongs to another book and is reserved.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 05 — HAYDÉE, 27 · NEW

**Attach:** none.
**Output:** `refs/05-haydee.png`
**Blocks:** P2 onward.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> A **new** character: a woman of **twenty-seven**, born in Epirus, living in
> Paris in 1838 and not remotely Parisian. She was eleven years old at Janina in
> 1822 and the volume's dates are checkable.
>
> Structure: long unbound black hair, or one heavy braid over the shoulder;
> large wide-set very dark eyes; straight brows; olive-gold skin; small straight
> nose; full mouth; slight build; direct unornamented stillness. She looks at
> people straight and does not arrange her face.
>
> **Costume: Epirote** — deep crimson and gold embroidery on a loose vertical
> silhouette, a long open coat over a straight underdress, no corsetry.
> **Never a French 1838 waist, never a French coiffure, never a bonnet.**
>
> Four views:
> 1. Three-quarter head and shoulders, neutral, even light.
> 2. Full-length standing, the crimson-and-gold Epirote dress, the loose
>    vertical silhouette.
> 3. Strict profile, same light.
> 4. **Full-length in the same dress, formally composed, holding nothing, about
>    to walk into a room of three hundred men.** Same costume; the difference is
>    entirely carriage.
>
> She must never be confused with a French comtesse of forty-two with a sculpted
> formal coiffure and a fitted burgundy-black gown. **Fourteen years separate
> them and the faces must show it.** Differentiators that must survive grayscale
> and thumbnail: age, unbound hairline, loose vertical silhouette, crimson-gold
> palette.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 06 — BARON DANGLARS, 55

**Attach:** `monte-cristo/refs/11-danglars-1815.png`
**Output:** `refs/06-danglars-1838.png`
**Blocks:** P9, P24, P25.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> The attached reference is this same man at thirty-two. **Age him forward
> twenty-three years to fifty-five**, and let the years read as money and
> comfort rather than hardship.
>
> Structure: heavy fleshy face; small shrewd close-set eyes; thin mouth; high
> colour in the cheeks; thinning sandy-grey hair combed across; **full side
> whiskers and no moustache**; short and thickening. **Expensive clothes that fit
> badly** — a banker's dark coat and a costly waistcoat straining, rings on the
> fingers, a heavy watch chain.
>
> Four views:
> 1. Three-quarter head and shoulders, neutral, even light.
> 2. Full-length standing, the badly-fitting expensive clothes.
> 3. Strict profile, same light — the side whiskers read hardest here.
> 4. **Seated at a writing desk, pen in hand, leaning over paper**, the ringed
>    hand and the thick wrist prominent.
>
> He must never be confused with a tall narrow pale rigid magistrate, or with a
> heavy moustached upright soldier. Differentiators that must survive grayscale
> and thumbnail: fleshy face shape, side whiskers with no moustache, short
> thickening build, high colour.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 07 — BEAUCHAMP, 28 · NEW · high collision risk

**Attach:** none.
**Output:** `refs/07-beauchamp.png`
**Blocks:** P27, P29, P35.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> A **new** character: a Paris newspaper editor of **twenty-eight**. He is the
> only man in this book who works for a living and looks it.
>
> Structure: tall, thin, **slightly stooped**; **sandy-light brown hair, untidy**;
> **small oval spectacles — the primary marker, present in every view**; long
> face; ironic mouth; ink-stained fingers. Costume: plain dark practical clothes,
> unfashionable and slightly worn, a coat that has been rained on.
>
> Four views:
> 1. Three-quarter head and shoulders, neutral, **spectacles on**.
> 2. Full-length standing, the stoop, the worn dark coat.
> 3. Strict profile, same light, spectacles reading clearly against the temple.
> 4. **The same man in the same Paris coat under hard white southern sun**, a
>    notebook in one hand, absurd and out of place. Same clothes, different
>    light.
>
> **He and the young gentleman of twenty-two are the volume's only two young men
> and they appear together on four pages.** He must never be confused with a
> clean-featured young man in a pale waistcoat with neat chestnut hair and no
> spectacles. Differentiators that must survive grayscale and thumbnail: hair
> colour (sandy, not chestnut), **spectacles always**, costume value (plain dark
> and worn, not bright and pale), posture (stooped, not upright).
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 08 — GÉRARD DE VILLEFORT, 53

**Attach:** `monte-cristo-expanded/refs/01-villefort-1815-v2.png`
**Output:** `refs/08-villefort-1838.png`
**Blocks:** P9.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> The attached reference is this same man at thirty. **Age him forward
> twenty-three years to fifty-three.**
>
> Structure: long narrow inverted-triangle face; very high forehead; close-set
> grey-hazel eyes; thin brows; convex aquiline nose; pointed chin; cool pale
> skin; chestnut hair gone iron-grey, still in a hard side part; deep vertical
> lines beside the mouth; rigid high-necked black silhouette; clean-shaven.
>
> **He must carry no trace of the count's face.** No curls, no olive skin, no
> broad cheekbones, and above all **no asymmetry at the left corner of the
> mouth** — that mark belongs to another man and these two collided badly enough
> in Volume I to force a full redesign.
>
> Four views:
> 1. Three-quarter head and shoulders, neutral, even light.
> 2. Full-length standing, the rigid high-necked black silhouette.
> 3. Strict profile, same light — the inverted triangle reads hardest here.
> 4. **The right hand extended to shake**, hand and forearm only, larger. No
>    face in this view.
>
> He must never be confused with a fleshy short thickening banker with side
> whiskers, nor with a pallid columnar man in unrelieved black. Differentiators
> that must survive grayscale and thumbnail: inverted-triangle face, very high
> forehead, hard side part, rigidity.
>
> `[ANTI-COLLISION CLAUSE]`

---

## Sheet 09 — JANINA 1822 BOARD — Haydée at eleven, and her mother

**Attach:** `refs/approved/05-haydee.png`
**Output:** `refs/09-janina-1822.png`
**Blocks:** P20, P21.

The only page in the volume that needs a child, and the only two figures who
belong to 1822. Haydée's mother appears as a distant shape on P20 and as a face
and a hand on P21; she is a locked figure on two pages and therefore gets a
reference rather than a prose lock. **Restraint is mandatory on P21** — the
subject is a child watching her mother sold and then dying, and the image is a
face and a hand let go of. This sheet must not make either figure a spectacle.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Two figures on one sheet, Epirus 1822, under hard high Mediterranean light —
> white limestone, cypress black, Ionian blue, sun-bleached ochre. This is a
> different world from Paris and must not look like it.
>
> **Figure A — a girl of eleven.** The attached reference is the same person
> sixteen years later; this is her as a child. Preserve the large wide-set very
> dark eyes, straight brows, olive-gold skin, small straight nose. Long unbound
> black hair. Plain Epirote child's dress, undyed linen and one band of dark
> embroidery — **not** the crimson and gold of her adult sheet. Slight, direct,
> unsmiling.
>
> **Figure B — her mother, mid-thirties.** The same bones, fifteen years on and
> exhausted: dark eyes, olive-gold skin, black hair covered by a plain dark
> headcloth. Plain travelling clothes, no ornament, no jewellery. **Fully
> clothed, unbound, unrestrained. No chains, no bare skin, no display.** She is
> a woman at the end of a long journey, drawn with dignity.
>
> Four views:
> 1. The girl — three-quarter head and shoulders, neutral, even light.
> 2. The girl — full-length standing, the plain child's dress.
> 3. The mother — three-quarter head and shoulders, neutral, even light.
> 4. **Two hands, an adult's and a child's, at the moment of coming apart** —
>    hands and wrists only, no faces, no crowd, no context.
>
> No crowd, no market, no onlookers, no leering, no spectacle of any kind on
> this sheet.
>
> `[ANTI-COLLISION CLAUSE]`

---

# Part 2 — Cast boards

Boards exist for the **reference critic**, not for the builder. Sheets 10–16 and
22 are never attached to a page prompt.

## Sheet 10 — Neutral head board, all eight principals

**Source:** sheets 01–08, all approved. No image-generation call.
**Output:** `refs/10-head-board.png`

Build deterministically at exactly **1536 × 1024, 3:2 landscape, RGB PNG**.
Extract the approved three-quarter head-and-shoulders view from each source
sheet, crop without repainting, normalize the eight crops to one consistent
head scale, and place them in a single even row on one plain neutral ground.
Do not generate, relight, retouch, interpolate facial features or add costume
below the collar beyond what the source crop contains. No text, labels, dividers
or borders.

Left to right, source order is fixed: 01 Count · 02 Mercédès · 03 Fernand · 04
Albert · 05 Haydée · 06 Danglars · 07 Beauchamp · 08 Villefort. Save a manifest
beside the QA evidence recording every source path, source SHA-256, crop box,
scale and placement. Every face must remain identifiable as a distinct
individual at thumbnail scale with no costume cue available.

## Sheet 11 — Grayscale silhouette board

**Source:** sheets 01–08, all approved. No image-generation call.
**Output:** `refs/11-silhouette-board.png`

Build deterministically at exactly **1536 × 1024, 3:2 landscape, RGB PNG**.
Extract the approved full-length standing view from each source sheet, isolate
only that figure from its plain ground, normalize all eight figures to one
consistent floor and body-height scale, convert every isolated figure to the
same flat dark silhouette, and place them in a single even row on a light
neutral ground. The silhouette has no interior detail and no colour. Do not
generate, redraw, reshape, invent or pose-correct any figure. No text, labels,
dividers or borders.

Left to right, source order is fixed: 01 Count · 02 Mercédès · 03 Fernand · 04
Albert · 05 Haydée · 06 Danglars · 07 Beauchamp · 08 Villefort. Save a manifest
beside the QA evidence recording every source path, source SHA-256, extraction
method, crop box, scale and placement. This board exists to prove that build,
height, posture and costume mass separate the cast with all face and colour
information removed. Any two silhouettes that could be swapped are a defect.

## Sheets 12–16 — Adversarial boards

Each is the same construction: **two figures, same panel, same light, in direct
opposition, at page scale rather than portrait scale.** Not a comparison chart —
a staged pair, the way the reader will actually meet them.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Two figures standing in one interior, facing each other in three-quarter view,
> **the same distance from the viewer, the same light, both faces visible**. No
> text and no labels. Render at the scale a story panel would use, not at
> portrait-study scale.

| # | Pair | Risk | The differentiators the board must prove |
|---|---|---|---|
| 12 | Albert / the Count | **highest** | hair colour · skin value · costume value · age · expression default |
| 13 | Albert / Beauchamp | **high** | spectacles · hair colour · costume value · posture |
| 14 | Fernand / the Count | medium | moustache · hairline · build · pallor |
| 15 | Haydée / Mercédès | medium | age · hairline · silhouette · palette |
| 16 | Danglars / Villefort | medium | face shape · build · whiskers · colour |

**Sheet 12 is the one that decides the volume.** The two men appear together on
P7, P10, P36 and P43; if a reader ever wonders whether the young man is the
Count's younger self, the book has failed at its most-read moment. The board
must show them shoulder to shoulder in the same light with nothing but their own
faces separating them.

## Sheet 22 — Live-pair proof, unlettered

**Attach:** sheets 01 and 04.
**Output:** `refs/22-live-pair-proof.png`

> One **unlettered** story panel at 1024 × 1536 portrait — the only portrait item
> in this plan — staging the highest-risk pair as the book will actually stage
> them: a warm crowded entrance hall lit from behind, the young man in a pale
> waistcoat coming down two steps with his hand already out, the older man in
> unrelieved black in the foreground and partly in silhouette. **No balloons, no
> captions, no lettering of any kind.**
>
> This proof exists to answer one question before any page is generated: **at
> real page scale, with one of the two men in silhouette, can a cold reader tell
> them apart?** If not, the sheets are wrong, not the page.

---

# Part 3 — Setting and object plates

Unlike the character sheets, these are **generation inputs** to the pages named,
attached alongside the character sheets. They exist because the volume's rooms
are arguments and a room that drifts breaks the argument.

Only four locations get a plate. The other six appear once or twice, carry no
identity risk, and are prose-locked in `05-SETTINGS-AND-OBJECTS.md`.

## Sheet 17 — The Count's house, 30 Champs-Élysées

**Used on:** P1–6, P14–15, P17–18, P20, P22–23, P26, P29, P37–40, P44–46 — **the
most-seen interior in the book, sixteen pages.**

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Three views of one interior, no figures anywhere.
>
> Palette: lacquer black, ivory, cold grey daylight, unpolished new gold. The
> room is **enormous, correct, and deliberately underfurnished** — a stage set
> for a man who does not live anywhere. **No family objects, no clutter, no
> warmth, no portraits, no books left open.** Tall uncurtained windows with the
> city in them.
>
> 1. The whole drawing room from the door, empty, cold grey daylight.
> 2. The same room at night by one lamp: a low black table, a decanter and one
>    glass, the tall windows black.
> 3. The window itself from inside, close: the city beyond it at night, and
>    **three lit roofs** distinguishable at middle distance. They are the only
>    warm thing in the room and they are other people's houses.

## Sheet 18 — The Morcerf house and the general's staircase

**Used on:** P6–13, P16, P26, P28, P41, P47.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Three views of one interior, no figures anywhere.
>
> Palette: burgundy, polished walnut, wax red, old gold, dense candle amber. The
> exact opposite of a cold correct house — this one is **overstuffed with
> purchased legitimacy**: too many portraits, too much gilt, warm and crowded and
> trying too hard.
>
> 1. The entrance hall and the foot of the staircase, lit for a party.
> 2. **The general's staircase**, full height, from below — a staircase built for
>    a man who was not born to one. This is the volume's most repeated structure
>    and must be the same staircase every time.
> 3. The same staircase **unlit and empty**, and beyond it a bedroom with the
>    wardrobes standing open and emptied.

## Sheet 19 — The Chamber of Peers

**Used on:** P30–34.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Three views, no figures anywhere.
>
> Palette: crimson benches, heavy gold, dark oak, cold high daylight from above.
> **The volume's largest room, designed as a mechanism** — tiered, symmetrical,
> and built to process a man.
>
> 1. The **exterior**: the front steps of the building from a side street, and
>    the narrow public stair at its flank. The building must be recognisable from
>    outside so that the interior reads as the same building.
> 2. The interior from the floor: the bar where a man stands, the tiers rising
>    away, the door at the back of the hall.
> 3. The interior from the **public gallery above**, looking down the length of
>    the hall at the floor — the view of a man who is at the killing and not in
>    the room.

## Sheet 20 — Janina, and the market at Constantinople

**Used on:** P19–21, P29.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Three views, no figures anywhere. **This must not look like Paris.** White
> limestone, cypress black, Ionian blue, sun-bleached ochre. High hard
> Mediterranean light where Paris is candlelit; horizontal where Paris is
> vertical. **This is the only place in the volume with a sky in it.**
>
> 1. The white lake fortress under hard high light, a shut gate in its wall.
> 2. A stone pavilion by water, a lamp burning inside it, night.
> 3. A dusty market square under heat-glare — bleached white, indigo shadow,
>    **empty of people.** No crowd, no platform, no spectacle.

## Sheet 21 — Key objects

**Used on:** P8, P11, P12, P15, P18, P22–26, P30, P32–33, P40, P42–45, P47.

> `[CANVAS BLOCK]` · `[REGISTER BLOCK]`
>
> Seven objects on a plain neutral ground, no figures, no hands, no text, **no
> legible writing on any document.**
>
> 1. A tall wine glass, full, standing untouched — and beside it the same glass,
>    empty.
> 2. A cut-glass decanter.
> 3. A **large folded document with a broken red wax seal**, old, handled. The
>    handwriting on it must be present as marks and **not legible** — no story
>    logic ever depends on reading it.
> 4. A flat travelling case sized to hold that document.
> 5. **A chest of military decorations** — orders, ribbons, wax-red seals and old
>    gold — laid out flat.
> 6. A folded 1838 Paris newspaper, cheap paper, dense grey columns, **the type
>    rendered as texture and not as readable words.**
> 7. **A flat rosewood duelling-pistol case, open**, with a pair of long
>    single-shot percussion pistols in fitted green baize, and the same case
>    closed. It is carried on P40, P42–44 and stands shut on P47; it must be the
>    same case in all of them, so it is locked here rather than described in
>    prose on five separate pages.

## Sheet 23 — Page 33 Chamber + objects carrier, unlettered

**Source:** approved sheets 19 and 21. No image-generation call.
**Used on:** P33 only.
**Output:** `refs/23-page-33-chamber-objects-carrier.png`

Build deterministically at exactly **1536 × 1024, 3:2 landscape, RGB PNG**.
Place an exact, aspect-preserving reduction of approved sheet 19 in the left
half and an exact, aspect-preserving reduction of approved sheet 21 in the right
half, separated only by a narrow neutral gutter. Use direct pixel resampling and
placement only. Do not generate, repaint, crop away any source view, add visual
content, or add text, labels, dividers or borders. Save a manifest beside the QA
evidence recording both source paths, both source SHA-256 values, the resampling
method, scales and placements.

This carrier is a reference-transport artifact, not a redesign or merged scene.
It contains no character identity. Page 33 attaches it in place of the two
separate setting/object inputs so that Haydée, Fernand, the Count, this carrier
and promoted Page 32 total exactly five references.

---

# The reference gate

Run before any page generates. The critic is independent and read-only.

**Blocking:**

1. **Any two of the eight principals confusable at thumbnail scale** on sheet 10
   or sheet 11.
2. **Albert reading as a young version of the Count** on sheet 12 or sheet 22 —
   the volume's single highest risk.
3. **Albert and Beauchamp confusable** on sheet 13.
4. Mercédès **youth-washed** — smoothed face, missing temple or lower-lid lines,
   missing grey. Named a blocking defect in Volume I's ledger and inherited
   verbatim.
5. Any returning character **not recognisably the same person** as their Volume I
   anchor.
6. Fernand **without the moustache or without the receding hairline** in any
   view.
7. Beauchamp **without spectacles** in any view.
8. Haydée in **French dress, a French coiffure, or a fitted waist**.
9. **Any lettering on any sheet.**
10. Register drift — smooth prestige-oil realism, airbrushed skin, glossy
    concept-art surfaces.
11. Any figure carrying a **reserved identity stack** it does not own,
    especially young Edmond's.
12. Wrong canvas: anything not 1536 × 1024 landscape, except sheet 22.

**Nonblocking:** costume detail accuracy, period-correct tailoring minutiae,
background finish on a plain-ground sheet, exact pose within a named view,
anything that does not change who the reader thinks a person is.

**Promotion.** On an unconditional APPROVED only: copy bytes into
`refs/approved/`, verify SHA-256, record in the ledger. **The production lead
alone promotes.** A sheet that returns REVISE is regenerated whole from its
anchor — never patched, and never fed its own rejected candidate as an input.
A deterministic artifact that returns REVISE is rebuilt in full from its
approved sources and recorded method; it is never manually patched.

**v4 ceiling applies to generative sheets too.** If a generative sheet is still returning REVISE at
v4, the lock itself is wrong: change the structural description in
`04-CHARACTER-LEDGER.md`, and re-run the collision matrix on the change before
regenerating.
