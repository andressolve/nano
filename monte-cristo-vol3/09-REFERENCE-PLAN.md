# Reference Plan — approved as a system

**Nothing generates a page until every character visibly on that page has an
approved permanent lock.** Not just-in-time. Locks live in `refs/approved/` and
get there only through `tools/refs.py promote` with an independent critic
report. A sheet in `refs/candidates/` is not a lock.

*Page numbers are deliberately absent from this file. The script is still at
its gate; page assignments are added after it clears, from the approved
`08-FULL-SCRIPT.md` and `05-SETTINGS-AND-OBJECTS.md`, never before.*

## Canvas and register — for every sheet

Reference sheets are **1536 × 1024 landscape**; story pages are portrait. This
is not an inconsistency: four views across a wide canvas is what a lock needs.

**Register name:** Velvet Cinema, inherited verbatim from Volume II
(`~/Documents/nano/monte-cristo-vol2/09-REFERENCE-PLAN.md`).

**Register, verbatim in every generative sheet prompt:**

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
captions, no inscriptions on tombs, desks, cases, clocks, or walls, no
lettering on a court bench, no monogram on a box or case. Labelled sheets
teach the page model to letter the art.

**Volume palette shift** (`05-SETTINGS-AND-OBJECTS.md`): Villefort's house is
cold — grey-blue walls, white marble, frost light, the colour of a closed
file. The Count's house is black and gold. Auteuil is night-blue and lantern.
The court is dark oak and red.

## Anchoring (sequels)

Parent anchors live in `refs/parents/`, copied byte-identical from the parent
volumes. They are attached as image inputs to the sheet that continues them.
`tools/refbrief.py` resolves every anchor name in the manifest's last column
under `refs/approved/`; a parent anchor is therefore written
`../parents/<file>` and resolves to `refs/parents/<file>.png`. A parent anchor
is never attached to a page — only the approved sheet built from it is.

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| 01 count | `refs/parents/01-count-1838.png` (Volume II approved sheet) | **none** — the same autumn as Volume II's last page; an identity-and-costume continuity pass, not a redesign |
| 02 villefort | `refs/parents/08-villefort-1838.png` (Volume II approved sheet) | **none** — continuity pass; adds the court state as view (d) |
| 07 noirtier | `refs/parents/09-leclere-noirtier.png` (Volume I sheet) | **+23 years**, 53 → 76. The anchor shows TWO men: Noirtier is the one with the cavalry moustache and the forest-green Empire coat (the right half of the sheet). The other man — bald crown, grey side-whiskers, red coat — is never drawn |
| 08 haydee | `refs/parents/05-haydee.png` (Volume II approved sheet) | **none** — continuity pass; adds the bedside night state as view (d) |
| set-count-study, set-count-bedroom | `refs/parents/17-set-count-house.png` (Volume II approved plate) | none — the same house; the parent plate is three studies of the drawing room, and each new plate draws ONE continuous view of a different room in that house's architecture and palette |

Valentine, Maximilien, Madame de Villefort, Benedetto, and Villefort's son are
**new** and have no anchor. Volume I's Renée and Pierre Morrel sheets are
likeness notes for the ledger only, never attached inputs.

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
that need them. **Boards are critic-only rasters and never generation inputs** —
their file names carry `board`, `adversarial`, `silhouette` or `live-pair` so
the tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 01 | `01-count` — the Count, 42: unrelieved black evening dress, swept-back black wave with first grey; view (d) outdoors at night in the long black cloak | character | after script gate | after script gate | `../parents/01-count-1838` |
| 02 | `02-villefort` — the King's Attorney, 53: rigid black frock coat to a high white stock, iron-grey hard side part; view (d) the court state, black magistrate's robe, white bands, black cylindrical cap | character | after script gate | after script gate | `../parents/08-villefort-1838` |
| 03 | `03-benedetto` — "Prince Andrea Cavalcanti", 21: bottle-green velvet coat, cream embroidered waistcoat, diamond pin; view (d) the prisoner's grey smock | character | after script gate | after script gate | new |
| 04 | `04-maximilien` — captain of Spahis, 28: dark blue tunic with gold frogging, soldier's moustache; view (d) civilian plain brown coat | character | after script gate | after script gate | new |
| 05 | `05-valentine` — Villefort's daughter, 19: dove-grey and white, pale-blue ribbon, light-chestnut low knot; view (d) asleep in a white nightdress, hair loose on a pillow | character | after script gate | after script gate | new |
| 06 | `06-heloise` — Madame de Villefort, 33: amethyst-violet silk, honey-gold high coils and ringlets; view (d) the crystal vial half-hidden in her hand, violet reticule | character | after script gate | after script gate | new |
| 07 | `07-noirtier` — Villefort's father, 76: white mane and moustache, faded forest-green Empire coat, seated always in a wheeled armchair; view (d) the eyes — open fierce stare and the long blink | character | after script gate | after script gate | `../parents/09-leclere-noirtier` |
| 08 | `08-haydee` — Haydée, 27: crimson-and-gold Epirote dress, unbound black hair or one braid; view (d) seated at a bedside at night, sleeves pushed back, watchful | character | after script gate | after script gate | `../parents/05-haydee` |
| 09 | `09-villefort-son` — Villefort's son, about eight (UNNAMED, no balloons): dark violet velvet skeleton suit, white collar, honey-gold curly mop; view (d) his hands holding the tin hussar; nearest lookalike his mother, Madame de Villefort (lineage), then Villefort (no adult-face transfer) | character | after script gate | after script gate | new |
| — | `board-heads` — all nine sheets, crop-and-place of each sheet's view (a) | board | — | — | crop-and-place from approved sheets |
| — | ~~`board-silhouette-grayscale`~~ — retired 2026-10-14: the deterministic quarter-crop caught fragments of neighbouring views on these sheets (gate round 1); replaced by the two generated silhouette boards below | — | — | — | — |
| — | `adversarial-silhouettes-men` — the five men as flat black full-length silhouettes on one floor line | board | — | — | `01-count` `02-villefort` `03-benedetto` `04-maximilien` `07-noirtier` |
| — | `adversarial-silhouettes-women-boy` — the three women and the boy as flat black full-length silhouettes on one floor line | board | — | — | `05-valentine` `06-heloise` `08-haydee` `09-villefort-son` |
| — | `adversarial-haydee-valentine` — low but documented: the two young women | board | — | — | `08-haydee` `05-valentine` |
| — | `adversarial-count-villefort` — HIGHEST risk: both clean-shaven, both in black; full length and costume-free head pairs, grayscale pass | board | — | — | `01-count` `02-villefort` |
| — | `adversarial-valentine-heloise` — high: two fair women in one house; full length and costume-free head pairs, grayscale pass | board | — | — | `05-valentine` `06-heloise` |
| — | `adversarial-benedetto-maximilien` — high: the only young men; full length and costume-free head pairs, grayscale pass | board | — | — | `03-benedetto` `04-maximilien` |
| — | `adversarial-benedetto-villefort` — medium, deliberate kinship: father and buried son, 31 years apart; must read as two different people | board | — | — | `03-benedetto` `02-villefort` |
| — | `adversarial-noirtier-villefort` — medium, father and son: the old man in his chair and the magistrate beside it | board | — | — | `07-noirtier` `02-villefort` |
| — | `live-pair-count-villefort` — unlettered, page scale: the Count and Villefort in the same frame in Villefort's drawing room, the Count partly in silhouette | board | — | — | `01-count` `02-villefort` |
| — | `set-auteuil-garden` — the walled garden at Auteuil at night: the one old plane tree, bare undisturbed earth under it, lantern light | set | after script gate | after script gate | — |
| — | `set-auteuil-dining-room` — the long candlelit dining room at Auteuil, glass doors onto the night garden | set | after script gate | after script gate | — |
| — | `set-villefort-drawing-room` — the cold grey-blue drawing room, white marble chimneypiece, and through open double doors the straight white marble stair with its iron rail | set | after script gate | after script gate | — |
| — | `set-noirtier-room` — dark green walls, Empire clock, framed eagle, the wheeled armchair by the window, the lemon-water carafe and glass | set | after script gate | after script gate | — |
| — | `set-valentine-room` — white and dove-grey, narrow white-curtained bed, the glass of water and carafe, the tall wardrobe closed against the party wall; no hidden door | set | after script gate | after script gate | — |
| — | `set-garden-gate` — the tall iron gate in the high ivy-covered wall at the bottom of Villefort's garden, the lane beyond | set | after script gate | after script gate | — |
| — | `set-morrel-house` — the warm modest apartment, fire and books, the small red silk purse under a glass dome | set | after script gate | after script gate | — |
| — | `set-assize-court` — the Assize court empty: dark oak, the raised bench with the red of the judges' seats, the dock, the gallery, tall grey windows | set | after script gate | after script gate | — |
| — | `set-pere-lachaise-vault` — the Villefort family vault in rain: white stone, black wet trees, the iron door shut | set | after script gate | after script gate | — |
| — | `set-count-study` — the Count's study in his house on the Champs-Élysées, black and gold, continuous with the Volume II plate | set | after script gate | after script gate | `../parents/17-set-count-house` |
| — | `set-count-bedroom` — the upstairs room in the Count's house where a girl will sleep, the bed empty, one candle | set | after script gate | after script gate | `../parents/17-set-count-house` |
| — | `obj-vial` — the Count's vial alone: one small cut-crystal flask of red liquid, gold stopper | object | after script gate | after script gate | — |
| — | `obj-tin-hussar` — the boy's tin hussar alone: a toy soldier on a rearing horse, red and gold | object | after script gate | after script gate | — |
| — | `obj-pistol-case` — the Morrel pistol case alone, closed: dark wood, brass corners | object | after script gate | after script gate | — |
| — | `obj-pastille-box` — the Count's draught alone: a small gold box, lid open, one white pastille | object | after script gate | after script gate | — |

**Generation order:** `01-count` first (every face in the book collides with him, and Villefort collided with him badly in Volume I); then `02-villefort`, built against the approved Count; then `03-benedetto`, who carries Villefort's long face and nose deliberately and must be built against him; then `04-maximilien`, the other young man, built against Benedetto; then `05-valentine` and `06-heloise`, the two fair women of one house, in that order; then `07-noirtier`, aged forward from his Volume I anchor; then `08-haydee`, a continuity pass on her approved Volume II sheet; then `09-villefort-son`, the unnamed boy; then boards (head and silhouette boards are crop-and-place from approved pixels, not generations); then the adversarial and live-pair boards; then plates in story order, object plates last.

## States needed, enumerated from the ledger

*Pages are assigned after the script gate. The states below come from
`04-CHARACTER-LEDGER.md` and `05-SETTINGS-AND-OBJECTS.md`; the script may add
none without a new sheet view.*

| Character | State | Carried by | Pages |
|---|---|---|---|
| The Count | unrelieved black evening dress, white linen at throat and cuff only | views (a)–(c) | assigned after script gate |
| The Count | outdoors: the long black cloak over the black dress, bareheaded | view (d) | assigned after script gate |
| The Count | the vial in his hand, stopper in | `obj-vial` + words | assigned after script gate |
| Villefort | rigid black frock coat, high white stock | views (a)–(c) | assigned after script gate |
| Villefort | court: black magistrate's robe, white bands, black cylindrical cap | view (d) | assigned after script gate |
| Villefort | last state: shirtsleeves, collar torn open, hair fallen across the brow, earth on his hands | words on the page, from views (a)–(c) | assigned after script gate |
| Benedetto | prince: bottle-green velvet coat, cream embroidered waistcoat, diamond pin, gloves | views (a)–(c) | assigned after script gate |
| Benedetto | prisoner: grey prison smock, the same grin | view (d) | assigned after script gate |
| Benedetto | cellar: stained mustard-brown jacket, grey neckerchief, coarse grey shirt — never a white open shirt | words on the page, from the face of views (a)/(c) | assigned after script gate |
| Maximilien | Spahi captain: dark blue tunic, gold frogging, short scarlet-lined dark cloak outdoors | views (a)–(c) | assigned after script gate |
| Maximilien | civilian: plain brown coat | view (d) | assigned after script gate |
| Maximilien | the pistol case in his hands | `obj-pistol-case` + words | assigned after script gate |
| Valentine | dove-grey and white, pale-blue ribbon, low knot | views (a)–(c) | assigned after script gate |
| Valentine | white nightdress, hair loose on a pillow, asleep or "dead" | view (d) | assigned after script gate |
| Madame de Villefort | amethyst-violet silk, lace, gold locket | views (a)–(c) | assigned after script gate |
| Madame de Villefort | the vial half-hidden in her hand, the violet reticule | view (d) | assigned after script gate |
| Madame de Villefort | fallen on the white stair, eyes closed, with dignity | words on the page | assigned after script gate |
| Noirtier | seated in the wheeled armchair, hands still on the tartan rug | views (a)–(c) | assigned after script gate |
| Noirtier | yes = one long blink; the open fierce stare | view (d) | assigned after script gate |
| Haydée | crimson-and-gold Epirote dress, loose vertical silhouette | views (a)–(c) | assigned after script gate |
| Haydée | seated at a bedside at night, sleeves pushed back, watchful | view (d) | assigned after script gate |
| Villefort's son | violet velvet skeleton suit, white collar, the tin hussar in hand | views (a)–(c) | assigned after script gate |
| Villefort's son | his hands holding the tin hussar | view (d) | assigned after script gate |
| Villefort's son | asleep on his mother's lap; in the Count's arms | words on the page | assigned after script gate |

## Nearest lookalikes and what carries the separation

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 Count | 02 Villefort; 03 Benedetto; 04 Maximilien | swept-back black wave, high cheekbones, hollow temples, pallor, left-mouth asymmetry, loose columnar black vs. iron-grey hard side part, narrow inverted triangle, high forehead, rigid high white stock; vs. young chestnut wave, lounging grin, coloured velvet; vs. moustache, sun-brown skin, blue uniform |
| 02 Villefort | 01 Count; 07 Noirtier; 03 Benedetto | as above, inverted; vs. broad leonine face, white mane and moustache, the armchair; vs. 31 years, chestnut hair, lounging grin (they share the long face and the nose on purpose) |
| 03 Benedetto | 04 Maximilien; 02 Villefort; 01 Count | clean-shaven narrow long face, pale skin, chestnut swept wave, crooked grin higher on the right, slim lounging build vs. moustache, sun-brown square face, cropped dark hair, broad upright build; vs. grey hair, age, rigidity; vs. black, pallor, stillness |
| 04 Maximilien | 03 Benedetto; 01 Count | as above, inverted; the moustache is the primary marker |
| 05 Valentine | 06 Madame de Villefort; 08 Haydée | 19, heart-shaped face, wide-set grey-blue eyes, light-chestnut centre-parted low knot, dove-grey vs. 33, long oval face, pale-green heavy-lidded eyes, honey-gold high coils and ringlets, violet; vs. olive-gold skin, black unbound hair, crimson |
| 06 Madame de Villefort | 05 Valentine; 08 Haydée | as above, inverted |
| 07 Noirtier | 02 Villefort | broad leonine face, white mane swept back, white cavalry moustache, the wheeled armchair vs. narrow inverted triangle, grey side part, clean-shaven, standing rigid |
| 08 Haydée | 05 Valentine; 06 Madame de Villefort | black unbound hair or one braid, olive-gold skin, very dark eyes, crimson-gold loose vertical dress vs. fair skin, light chestnut or honey-gold hair, French waists in dove-grey or violet |
| 09 Villefort's son | 06 Madame de Villefort (lineage, primary); 02 Villefort (secondary) | he inherits her pale-green eyes, honey-gold hair and violet palette on purpose; separated by his round child skull, eight-year-old scale, short soft curly mop, wide white collar and solemn child posture vs. her long oval adult face, high coils with temple ringlets and rounded figure; never Villefort's adult face |

## Separation system — from the ledger

Identity hierarchy, inherited from Volumes I and II, in order of priority:
**1.** face shape and apparent age · **2.** hair and facial-hair mass ·
**3.** body silhouette and habitual posture · **4.** costume value pattern ·
**5.** colour accent, prop, repeated gesture. Costume and colour may reinforce
a character; they may never be the only cues.

**Reserved design space** — no background or unnamed figure may inherit a
complete identity stack:

- unrelieved black columnar dress with swept-back black hair and pallor → the Count
- rigid black frock coat with high white stock and iron-grey hard side part on a narrow face → Villefort
- dark blue tunic with gold frogging and a dark moustache on a young man → Maximilien
- bottle-green velvet with a diamond pin on a young chestnut-haired man → Benedetto
- amethyst-violet silk with honey-gold coils → Madame de Villefort
- dove-grey and white with a pale-blue ribbon on a young fair woman → Valentine
- forest-green Empire coat, white mane and moustache, in a wheeled armchair → Noirtier
- crimson-and-gold Epirote embroidery with unbound black hair → Haydée
- loose raven curls, open white shirt, red-brown sash → young Edmond, Volume I. Reserved and unused.

**Collision matrix** (the boards above exist for these pairs):

| Pair | Risk | Carried by |
|---|---|---|
| The Count / Villefort | **highest** | hair (black swept wave vs iron-grey hard side part), face (high cheekbones and hollow temples vs narrow inverted triangle and high forehead), age (42 vs 53), collar (loose black stock vs rigid high white stock), posture (columnar stillness vs rigid stiffness) |
| Valentine / Madame de Villefort | **high** | age (19 vs 33), hair (simple light-chestnut low knot vs honey-gold high coils and ringlets), face (heart-shaped vs long oval), eyes (grey-blue vs pale-green heavy-lidded), costume (dove-grey vs violet) |
| Benedetto / Maximilien | **high** | moustache (never vs always), skin (pale vs sun-brown), build (slim lounging vs broad upright), costume (bottle-green velvet or grey smock vs blue-and-gold), face (long narrow vs square) |
| Benedetto / Villefort | medium — deliberate kinship | age, hair colour (chestnut vs iron-grey), posture (lounging vs rigid), expression (crooked grin vs cold) |
| Noirtier / Villefort | medium — father and son | face (broad leonine vs narrow), hair (white mane and moustache vs grey side part, clean-shaven), the armchair |
| Haydée / Valentine | low | skin, hair colour, costume |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast. Villefort's son is unnamed and has no balloons, and has a
  full sheet because he recurs.
- Absent lookalikes are critic-only. **Never attach a lookalike to a
  generation as a negative example** — the model draws what it is shown. Every
  character prompt below names its nearest lookalikes in words only. Boards
  attach both sheets because a board is never a page input.
- Unnamed and background figures may never carry a complete reserved identity
  stack. **Extras on any page with the Count wear brown, grey, buff, dark green
  or navy, never unrelieved black.** Court officials in black robes appear only
  behind Villefort on the court pages, never at the Count's height or with his
  hair. Judges wear red; Villefort's robe is black, never red.
- **Reserved colours never appear on unrelated things in plates:** no
  crimson-and-gold embroidered textile (Haydée), no amethyst-violet silk or
  drapery (Madame de Villefort and her son), no bottle-green velvet (Benedetto),
  no blue-and-gold braid (Maximilien), no garment of any kind left lying on
  furniture. Forest green belongs to Noirtier's own room and coat only.
- **Plates carry only a permitted state** (method/07, the plate that carries a
  forbidden state). `set-auteuil-garden` shows bare, undisturbed earth under the
  tree — never a hole, mound, spade, or box; the dug-open hole is drawn from
  words. `set-valentine-room` shows the wardrobe closed against an unbroken wall
  — never a hidden door, seam, or opening; the door through the wall is drawn
  from words on the pages that need it. `set-pere-lachaise-vault` shows the iron
  door shut and no light inside. The glass by Valentine's bed holds clear water,
  never red drops.
- **One vial, always.** `obj-vial` shows exactly one flask; the vial appears on
  `06-heloise` view (d) and nowhere else on any sheet. The draught is a white
  pastille in a gold box, never the red vial.
- **Every plate here is a single continuous view**, so that no page ever
  attaches a multi-study plate; a page attaches at most one setting plate
  (method/07, the montage from multi-view plates). The Count's house anchor is
  itself a three-study plate: the two Count's-house plates are told to draw ONE
  view and never to copy its panel layout.
- **No figures, no lettering, no signature on any plate.** Tombs carry no
  names or dates; the court carries no inscription; the case and the box carry
  no monogram.
- A rejected sheet never becomes a lock and never becomes an input.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas, left to right:
**(a)** three-quarter head and shoulders, neutral expression, even light;
**(b)** full-length standing figure, default costume, habitual posture;
**(c)** strict profile, same light; **(d)** the one state the script actually
needs.

## 01 — THE COUNT OF MONTE CRISTO

A 1536 × 1024 landscape character reference sheet with four views of one
single man of forty-two, arranged left to right on a plain neutral warm-grey
ground. Flat even reference light. No scenery, words, labels, name plates,
frames, or borders between views.

The attached approved sheet is this same man, drawn this same autumn. This
sheet is an identity-and-costume continuity pass, not a redesign and not an
ageing: keep the attached face exactly. Deep-set black-brown eyes; a strong
straight brow; a long clean nose; high cheekbones; hollow temples; cultivated
pallor; a slight asymmetry at the left corner of the mouth; clean-shaven. A
full swept-back black wave with the first grey at the temples. Tall, slim,
columnar, unnaturally still. Keep this exact face, hairline, and pallor in
every view.

In views (a), (b), and (c) he wears unrelieved black 1838 Paris evening dress,
as on the attached sheet: black tailcoat, black waistcoat, black stock, white
shirt-linen only at the throat and cuff. He is the only unbroken black
vertical in any room. He carries nothing.

Remove every brown, gold, bronze, and patterned mark from all garments and
from the cloak; render the tailcoat, waistcoat, stock, trousers, gloves, and
cloak as solid matte near-black shapes, with white confined to the throat and
cuffs, so the full figure reads as one unbroken black vertical in colour,
grayscale, and thumbnail.

View (a): a large three-quarter head-and-shoulders portrait in flat even light,
neutral expression, the left mouth corner's slight asymmetry legible, the
deep-set eyes level and amused.

View (b): full length from the front, arms at rest, the columnar stillness,
the right hand gone still at his side as if before a decision.

View (c): a strict ninety-degree profile in the same light, showing the long
clean nose, the strong brow, the hollow temple, and the swept-back wave.

View (d): the same man outdoors at night, full length: a long black cloak
falling straight from the shoulders over the black evening dress, bareheaded,
the swept-back black wave and the pale face the only light values, the right
hand lifted to chest height and perfectly still, empty. The ground stays plain.

He must never be confused with Villefort, a narrow pale rigid magistrate of
fifty-three with an iron-grey hard side part, a very high forehead, and a
rigid high white stock; with Benedetto, a lounging young man of twenty-one
with a glossy chestnut wave and a crooked grin in coloured velvet; or with
Maximilien, a broad sun-browned young cavalry officer with a dark moustache
in blue and gold. Never grey hair beyond the temples, never a side part,
never a moustache or beard, never colour in his dress, never loose raven
curls, an open white shirt, or a red sash.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — GÉRARD DE VILLEFORT

A 1536 × 1024 landscape character reference sheet with four views of one man
of fifty-three, left to right, on a plain neutral warm-grey ground. Flat even
reference light. No scenery, words, labels, frames, or borders between views.

The attached approved sheet is this same man, drawn this same autumn. This
sheet is an identity-and-costume continuity pass, not a redesign and not an
ageing: keep the attached face exactly. A long narrow inverted-triangle face;
a very high forehead; close-set grey-hazel eyes; thin brows; a convex aquiline
nose; a pointed chin; cool pale skin; chestnut hair gone iron-grey, combed flat
with a hard side part; deep vertical lines beside the mouth; clean-shaven.
Rigid, upright, high-necked. Keep this exact face, hairline, and side part in
every view.

In views (a), (b), and (c) he wears a rigid black frock coat buttoned high to
a stiff high white stock — black, but broken by the white stock and his grey
hair; never the loose columnar line of an evening tailcoat.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, cold and composed, mouth closed in a straight line.

View (b): full length from the front, rigid and upright, heels together, one
hand at his side and one resting flat against the front of the coat.

View (c): a strict ninety-degree profile in the same light — the inverted
triangle reads hardest here: the high forehead, the aquiline nose, the
pointed chin, the high white stock.

View (d): the same man in court, full length: a long black magistrate's robe
with wide sleeves, two white bands at the throat, and a black cylindrical cap
on his head, the grey side part showing beneath it; standing rigid, one hand
raised with the forefinger pointing forward, arguing. The robe is black,
never red.

He must carry no trace of the Count's face: no black hair, no swept-back wave,
no high cheekbones, no hollow temples, no olive skin, and above all no
asymmetry at the left corner of the mouth. He must never be confused with
Noirtier, his father, a gaunt broad-faced old man with a white mane and a
white cavalry moustache in a wheeled armchair; nor with Benedetto, who shares
his long face and nose but is twenty-one, smooth, chestnut-haired, and always
grinning. Never a moustache, never a soft or warm expression, never a loose
collar in the default views.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — BENEDETTO, called PRINCE ANDREA CAVALCANTI

A 1536 × 1024 landscape character reference sheet with four views of one young
man of twenty-one, left to right, on a plain neutral warm-grey ground. Flat
even reference light. No scenery, words, labels, frames, or borders between
views.

Benedetto is slim and loose-limbed, and he leans on everything; his habitual
posture is weight on one hip, one shoulder dropped. A long narrow face and a
convex aquiline nose, young and smooth; grey-hazel eyes, lazy and
heavy-lidded; a quick crooked grin that rises higher on the right side; a
clean-shaven chin with short side-whiskers to the jaw angle. Glossy dark
chestnut hair worn long, in a fashionable swept wave over the brow. Pale skin.
Keep this exact long face, crooked grin, chestnut wave, and lounging carriage
in every view.

In views (a), (b), and (c) he is dressed as a prince: a bottle-green velvet
tailcoat, an embroidered cream silk waistcoat, a white cravat with a single
diamond pin, pale gloves.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, the crooked grin higher on the right, the heavy-lidded eyes amused.

View (b): full length from the front, lounging: weight on one hip, one
shoulder dropped, one gloved hand on his hip, the other loose.

View (c): a strict ninety-degree profile in the same light, showing the
aquiline nose, the smooth young jaw, the side-whisker, and the swept chestnut
wave.

View (d): the same young man as a prisoner, full length: a coarse grey prison
smock belted with cord, grey trousers, hair unkempt but still long and
chestnut, the same crooked grin, leaning back with his arms folded.

He must never be confused with Maximilien Morrel, a broad upright sun-browned
officer with a square face, cropped dark hair, and a dark moustache in blue
and gold; with Villefort, a rigid grey-haired man of fifty-three; or with the
Count, still and pale in unrelieved black. Never a moustache, never sun-brown
skin, never black clothes, never grey hair, never rigid posture, never loose
raven curls, an open white shirt, or a red sash.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — MAXIMILIEN MORREL

A 1536 × 1024 landscape character reference sheet with four views of one man
of twenty-eight, left to right, on a plain neutral warm-grey ground. Flat even
reference light. No scenery, words, labels, frames, or borders between views.

Maximilien Morrel is broad-shouldered with an upright cavalry carriage, and
quick to laugh. A square open face with a strong straight jaw; frank brown
eyes under level dark brows; a straight nose; sun-browned skin from Africa,
the warmest skin of any man in the book. Short dark-brown hair cropped close,
not curled. A neat dark-brown soldier's moustache — his primary marker,
present in every view. Keep this exact square face, moustache, cropped hair,
and sun-brown skin in every view.

In views (a), (b), and (c) he wears the uniform of a captain of Spahis: a
dark blue tunic with gold braid frogging across the chest, dark trousers,
boots; no sash.

Remove the unlisted sabre completely from uniform views (b) and (c): no hilt,
guard, tassel, scabbard, or suspension straps. Leave a plain belt, keep view
(b)'s hand resting on that belt, and preserve the same broad shoulders and
upright cavalry posture.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, frank and warm, on the edge of a laugh.

View (b): full length from the front, upright, shoulders square, one hand
resting on his belt, a short dark cloak lined in scarlet thrown back from one
shoulder.

View (c): a strict ninety-degree profile in the same light, showing the
square jaw, the straight nose, the moustache, and the cropped hair.

View (d): the same man as a civilian, full length: a plain brown coat, a buff
waistcoat, a dark stock, no braid, no uniform; standing straight, hands at his
sides, his face grave.

He must never be confused with Benedetto, a slim lounging pale young man with
a clean-shaven long narrow face and a glossy chestnut wave in coloured
velvet; or with the Count, pale, still, and in unrelieved black. Never
clean-shaven, never long or curled hair, never pale skin, never black, never
loose raven curls, an open white shirt, or a red sash.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — VALENTINE DE VILLEFORT

A 1536 × 1024 landscape character reference sheet with four views of one young
woman of nineteen, left to right, on a plain neutral warm-grey ground. Flat
even reference light. No scenery, words, labels, frames, or borders between
views.

Valentine is slight, quick, and upright, and nineteen and looks it. A
heart-shaped face, wide and soft at the cheekbones, narrowing to a small
rounded chin; wide-set grey-blue eyes; fine straight light brows; a small
straight nose; pale fair skin, the palest face in the book. Light chestnut
hair with a gold cast, parted in the centre and worn simply in a low knot at
the nape, with a few loose strands at the temples — no ringlets, no high
coils. Keep this exact heart-shaped face, grey-blue eyes, and simple low knot
in every view.

In views (a), (b), and (c) she wears a plain dove-grey and white day dress,
long sleeves, a narrow pale-blue ribbon at the throat — the plainest dress in
her house. No jewellery.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, gentle and direct, a small dry smile.

View (b): full length from the front, upright, hands lightly clasped in front.

View (c): a strict ninety-degree profile in the same light, showing the small
straight nose, the rounded chin, and the low knot at the nape.

View (d): the same young woman lying asleep and perfectly still, seen from
slightly above: head, shoulders, and upper body on a plain white pillow, in a
plain white long-sleeved nightdress, her light chestnut hair loose and spread
on the pillow, eyes closed, face calm, hands folded on a white sheet. No bed
frame, no room, the ground stays plain.

She must never be confused with Madame de Villefort, a woman of thirty-three
with a long oval face, pale-green heavy-lidded eyes, and honey-gold hair
dressed high in coils with long ringlets, in amethyst-violet silk; or with
Haydée, olive-gold with black unbound hair in crimson. Never honey-gold,
never ringlets or high coils, never violet, never crimson, never jewellery.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — HÉLOÏSE, MADAME DE VILLEFORT

A 1536 × 1024 landscape character reference sheet with four views of one woman
of thirty-three, left to right, on a plain neutral warm-grey ground. Flat even
reference light. No scenery, words, labels, frames, or borders between views.

Madame de Villefort is of medium height with a soft rounded figure. A long
oval face with a high rounded forehead and soft full cheeks; pale-green,
heavy-lidded eyes; fine arched brows; a small rosebud mouth, always half
smiling; pink-white skin. Honey-gold hair dressed high in coils, with long
ringlets falling at both temples — the most elaborate hair in the book. Keep
this exact long oval face, heavy-lidded pale-green eyes, rosebud half-smile,
and honey-gold coils and ringlets in every view.

In views (a), (b), and (c) she wears an amethyst-violet silk gown with lace at
the wrists and a small gold locket on a fine chain.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, sweet and attentive, the half-smile.

View (b): full length from the front, soft and composed, one hand lowered
and curved at her side as if resting on a small child's head; a small violet
silk reticule hangs from the other wrist.

View (c): a strict ninety-degree profile in the same light, showing the high
rounded forehead, the small mouth, the coils, and a temple ringlet.

View (d): the same woman, three-quarter length, the violet reticule open at
her wrist and one hand half-closed against it, holding — half hidden in her
palm — one small cut-crystal flask of deep red liquid with a gold stopper.
Exactly one flask. Her eyes are lowered to it, her mouth still half smiling.

She must never be confused with Valentine, a girl of nineteen with a
heart-shaped face, wide-set grey-blue eyes, and a simple light-chestnut low
knot, in dove-grey; or with Haydée, black-haired and olive-gold in crimson.
Never a heart-shaped face, never a low knot, never dove-grey, never crimson,
never a second flask.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — NOIRTIER DE VILLEFORT

A 1536 × 1024 landscape character reference sheet with four views of one old
man of seventy-six, left to right, on a plain neutral warm-grey ground. Flat
even reference light. No scenery, words, labels, frames, or borders between
views.

The attached sheet shows two men. **Noirtier is the one with the cavalry
moustache and the forest-green Empire coat** (the right half of the attached
sheet). The other man — bald crown, grey side-whiskers, red coat — is a
different person and is never drawn on this sheet. This sheet is Noirtier
twenty-three years later — an ageing pass, not a redesign. Keep from the
attached sheet: the broad leonine face, the heavy brow, the deep-set dark
eyes, the strong nose, the cavalry moustache, the hair swept back from the
forehead, and the forest-green Empire coat with its high dark collar.

Twenty-three years and a stroke have changed the rest. His long swept-back
hair is now pure white, a mane to the collar. Heavy white brows; a full white
cavalry moustache. The broad face has gone gaunt, the cheeks sunken. He is
paralysed: the body is utterly still, the head upright, the hands motionless
on a rug — and the deep-set dark eyes are fierce and glittering, the only
living thing in him. Keep this exact white mane, white moustache, broad gaunt
face, and fierce eyes in every view.

In views (a), (b), and (c) he wears the same forest-green Empire coat of 1815,
faded and too large for him now, over a dark waistcoat and a dark stock, and
he sits in a high-backed wheeled armchair: a tall upholstered back, wooden
arms, two large spoked wheels at the sides. A dark tartan rug covers his
knees. He never stands.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, the head upright against the high chair back, the face still, the eyes
alive and fixed on the viewer.

View (b): full length, seated in the wheeled armchair seen from the front at a
slight angle, the whole chair and wheels visible, the rug over his knees, both
hands lying motionless on it.

View (c): a strict ninety-degree profile of the head and shoulders in the
same light, showing the heavy brow, the strong nose, the white moustache, the
sunken cheek, and the white mane swept back.

View (d): two close studies of the same face from brow to moustache, one above
the other: above, the eyes wide open in a fierce, glittering stare; below,
the identical face with the eyes closed in one long, deliberate blink. Nothing
else in the face moves.

He must never be confused with Villefort, his son: a narrow inverted-triangle
face, iron-grey hair in a hard side part, clean-shaven, standing rigid in
black. Never standing, never a gesture, never an open mouth, never frail or
pitiable, never grey-black hair, never the other man on the attached sheet.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — HAYDÉE

A 1536 × 1024 landscape character reference sheet with four views of one woman
of twenty-seven, left to right, on a plain neutral warm-grey ground. Flat even
reference light. No scenery, words, labels, frames, or borders between views.

The attached approved sheet is this same woman, drawn this same autumn. This
sheet is an identity-and-costume continuity pass, not a redesign and not an
ageing: keep the attached face exactly. Long unbound black hair, or one heavy
braid over the shoulder; large wide-set very dark eyes; straight brows;
olive-gold skin; a small straight nose; a full mouth; a slight build; direct,
unornamented stillness. She looks at people straight and does not arrange her
face. Keep this exact face and hair in every view.

In views (a), (b), and (c) she wears the Epirote dress of the attached sheet:
a long open coat of deep crimson with gold embroidery over a straight pale
underdress, a loose vertical silhouette, never a French waist, never a French
coiffure, never a bonnet.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, direct and level, unsmiling.

View (b): full length from the front, standing straight, hands at her sides,
the loose vertical silhouette.

View (c): a strict ninety-degree profile in the same light, showing the small
straight nose, the full mouth, and the heavy braid down her back.

View (d): the same woman at night, seated on a plain wooden chair as if beside
a sickbed, leaning forward, forearms on her knees, the crimson coat's sleeves
pushed back from her wrists, her braid over one shoulder, her eyes wide awake
and watchful, turned to one side. A single warm candle glow from off frame
lights one side of her; no bed, no room, the ground stays plain.

She must never be confused with Valentine, pale and fair with light chestnut
hair in dove-grey; or with Madame de Villefort, with honey-gold coils and
ringlets in violet silk. Never fair hair, never pale skin, never a French
waist, never violet or dove-grey.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 09 — VILLEFORT'S SON (unnamed)

A 1536 × 1024 landscape character reference sheet with four views of one small
boy of about eight, left to right, on a plain neutral warm-grey ground. Flat
even reference light. No scenery, words, labels, frames, or borders between
views.

This boy is unnamed and never speaks; he is Villefort's young son. He is small
for eight. A round child's face with his mother's pale-green eyes and her
honey-gold hair in a soft curly mop; pink-white skin; a solemn, watchful
face that breaks into delight. Keep this exact round face, pale-green eyes,
and honey-gold curly mop in every view.

In views (a), (b), and (c) he wears a dark violet velvet skeleton suit — a
short jacket buttoned onto high-waisted trousers — with a wide white collar.
In his right hand he always holds a tin hussar: a toy soldier in a red and
gold uniform on a rearing horse, painted tin, small enough to fit his fist.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, solemn and watchful.

View (b): full length from the front, standing straight, the tin hussar held
in his right hand at his chest.

View (c): a strict ninety-degree profile in the same light, showing the round
cheek, the small nose, and the curly mop.

View (d): a larger close study of his two small hands holding the tin hussar
up to be seen: the red-and-gold rider on the rearing horse, the paint chipped
at the edges, the violet velvet cuffs at his wrists. No face in
this view.

He must never resemble any adult: never an adult face, never Villefort's long
narrow face or grey hair, never black clothes. Never a different toy, never a
sword or weapon of his own.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board, plate, and object prompts

Boards are critic-only rasters generated from the attached approved sheets.
Plates are generation inputs: architecture, palette, light and objects only,
unlettered and without figures, each one single continuous view. Every plate
prompt carries the reserved-colour and no-signature clauses. The bullets run
to the end of this file; nothing follows them.

- **adversarial-count-villefort.** One unframed 1536 × 1024 landscape reference board on a plain neutral warm-grey ground, flat even light, no lettering, labels, rules, or props in hand. This is the HIGHEST-risk pair in the book: two clean-shaven men in black. On the left third, the two men from the attached approved sheets full length, side by side on one floor line at one scale: the Count tall, slim, and columnar in unrelieved black evening dress with a black stock, white linen only at throat and cuff; Villefort rigid and upright in his black frock coat buttoned to a stiff high white stock. On the right two-thirds, four matched costume-free head pairs in a clean two-by-two field with open ground between them, every crop ending at the jaw and upper neck, no collar or stock visible: a neutral three-quarter pair with closed mouths; the same pair in a cold half-smile; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. The Count keeps his full swept-back black wave with first grey at the temples, deep-set black-brown eyes, strong straight brow, long clean nose, high cheekbones, hollow temples, pallor, and the slight asymmetry at the left corner of the mouth; Villefort keeps his long narrow inverted-triangle face, very high forehead, iron-grey hair combed flat in a hard side part, close-set grey-hazel eyes, thin brows, convex aquiline nose, pointed chin, and deep vertical lines beside a straight mouth with no asymmetry. No signature, monogram, artist's mark, or watermark in any corner.
- **adversarial-valentine-heloise.** One unframed 1536 × 1024 landscape reference board on a plain neutral warm-grey ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two women from the attached approved sheets full length, side by side on one floor line at one scale: Valentine, nineteen, slight and upright in plain dove-grey and white with a pale-blue ribbon; Madame de Villefort, thirty-three, soft and rounded in amethyst-violet silk, no reticule, no flask. On the right two-thirds, four matched head pairs, every crop ending at the jaw and upper neck, no ribbon, locket, or costume visible: a neutral three-quarter pair with closed mouths; the same pair smiling; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Valentine keeps her heart-shaped face narrowing to a small rounded chin, wide-set grey-blue eyes, fine straight light brows, pale fair skin, and light chestnut hair centre-parted in a simple low knot; Madame de Villefort keeps her long oval face with a high rounded forehead and soft full cheeks, pale-green heavy-lidded eyes, fine arched brows, rosebud mouth, and honey-gold hair dressed high in coils with long temple ringlets. Fourteen years separate them and the faces must show it. No signature, monogram, artist's mark, or watermark in any corner.
- **adversarial-benedetto-maximilien.** One unframed 1536 × 1024 landscape reference board on a plain neutral warm-grey ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two young men from the attached approved sheets full length, side by side on one floor line at one scale: Benedetto slim and lounging, weight on one hip, in the bottle-green velvet coat and cream waistcoat; Maximilien broad and upright in the dark blue Spahi tunic with gold frogging. On the right two-thirds, four matched costume-free head pairs, every crop ending at the jaw and upper neck: a neutral three-quarter pair with closed mouths; the same pair laughing; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Benedetto keeps his long narrow face, convex aquiline nose, heavy-lidded grey-hazel eyes, crooked grin higher on the right, pale skin, clean-shaven chin with short side-whiskers, and long glossy chestnut swept wave; Maximilien keeps his square open face, strong straight jaw, frank brown eyes under level dark brows, sun-browned skin, short cropped dark-brown hair, and the neat dark soldier's moustache. No signature, monogram, artist's mark, or watermark in any corner.
- **adversarial-benedetto-villefort.** One unframed 1536 × 1024 landscape reference board on a plain neutral warm-grey ground, flat even light, no lettering, labels, rules, or props in hand. This pair is father and son, thirty-one years apart: they share the long narrow face and the convex aquiline nose on purpose, and must still read at once as two different people. On the left third, the two men from the attached approved sheets full length, side by side on one floor line at one scale: Benedetto slim and lounging in the grey prison smock, arms folded; Villefort rigid in the black frock coat and high white stock. On the right two-thirds, exactly four matched costume-free head pairs stacked top to bottom, every crop ending at the jaw and upper neck: FIRST, a neutral three-quarter pair with BOTH mouths closed and Benedetto NOT smiling — his grin fully suppressed, lips together, the bones alone carrying the difference; SECOND, Benedetto grinning beside Villefort cold; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Benedetto keeps his young smooth skin, heavy-lidded lazy eyes, crooked grin higher on the right, short side-whiskers, and long glossy chestnut swept wave; Villefort keeps his very high forehead, iron-grey hard side part, close-set eyes, pointed chin, deep vertical lines beside the mouth, and fifty-three years. No signature, monogram, artist's mark, or watermark in any corner.
- **adversarial-silhouettes-men.** One unframed 1536 × 1024 landscape critic board on a plain clean white ground, no lettering, labels, rules, numbers, signature or watermark. Exactly five complete full-length figures, one from each attached approved sheet's full-length view, standing side by side on one common floor line at one comparative scale, in any left-to-right order (order carries no identity information): the Count, Villefort, Benedetto, Maximilien, Noirtier (seated in his high-backed wheeled armchair). Approved v1 was made opaque and solid-filled deterministically (gate round 2). Render every figure as a single flat solid black silhouette — no interior detail, no grey, no shading, no ground shadow — only the outer contour: hair mass, hat-free head, shoulders, costume outline, posture. Generous white space between figures; no figure overlaps another; nothing else on the board.
- **adversarial-silhouettes-women-boy.** One unframed 1536 × 1024 landscape critic board on a plain clean white ground, no lettering, labels, rules, numbers, signature or watermark. Exactly four complete full-length figures, one from each attached approved sheet's full-length view, standing side by side on one common floor line at one comparative scale (the boy is a child of eight, much shorter), in this order left to right: Valentine, Madame de Villefort, Haydée, the boy. Approved v1 was made solid-filled deterministically (gate round 2). Render every figure as a single flat solid black silhouette — no interior detail, no grey, no shading, no ground shadow — only the outer contour: hair mass and coiffure, dress silhouette, posture. Generous white space between figures; no figure overlaps another; nothing else on the board.
- **adversarial-haydee-valentine.** One unframed 1536 × 1024 landscape reference board on a plain neutral warm-grey ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two women from the attached approved sheets full length, side by side on one floor line at one scale: Haydée in her crimson-and-gold Epirote coat over a straight underdress, black braid over the shoulder, loose vertical carriage; Valentine in dove-grey and white with the pale-blue ribbon, slight and upright. On the right two-thirds, exactly four matched costume-free head pairs stacked top to bottom, every crop ending at the jaw and upper neck: a neutral three-quarter pair; a reaction pair (both startled, mouths slightly open); strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Haydée keeps her long direct face, olive-gold skin, large wide-set very dark eyes, straight brows and black hair; Valentine keeps her heart-shaped face narrowing to a small rounded chin, pale fair skin, wide-set grey-blue eyes and light-chestnut hair in a low knot. No signature, monogram, artist's mark, or watermark in any corner.
- **adversarial-noirtier-villefort.** One unframed 1536 × 1024 landscape reference board on a plain neutral warm-grey ground, flat even light, no lettering, labels, rules, or props in hand. Father and son. On the left half, the two men from the attached approved sheets full length at one scale: Noirtier seated in his high-backed wheeled armchair, the dark tartan rug over his knees, in the faded forest-green Empire coat; Villefort standing rigid beside the chair in the black frock coat and high white stock. On the right half, three matched costume-free head pairs at one height, every crop ending at the jaw and upper neck: a neutral three-quarter pair; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Noirtier keeps his broad gaunt leonine face, heavy white brows, deep-set fierce dark eyes, long white mane swept back, and full white cavalry moustache; Villefort keeps his long narrow inverted-triangle face, very high forehead, iron-grey hard side part, aquiline nose, pointed chin, and clean-shaven upper lip. No signature, monogram, artist's mark, or watermark in any corner.
- **live-pair-count-villefort.** One unframed 1536 × 1024 landscape board, unlettered, at story-page scale, in the register: a cold grey-blue panelled drawing room with a white marble chimneypiece by grey winter daylight. The Count, from the attached sheet, stands left by a tall window in unrelieved black evening dress, partly in silhouette against the pale window light, his face turned three-quarter toward the other man, the pale face, swept-back black wave, and high cheekbones still readable; Villefort, from the attached sheet, stands right in even light, rigid in his black frock coat and high white stock, facing him three-quarter. The two men stand at the same distance from the viewer, about two paces apart, each face large enough to read at reduced size: the Count's hollow temples and the asymmetry at the left corner of his mouth; Villefort's very high forehead, iron-grey hard side part, and pointed chin. No other figures. No balloons, captions, letters, glyphs, signature, watermark, label, or border anywhere; a completely clean full-bleed edge on every side.
- **set-auteuil-garden.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the walled garden of an old shuttered country house in the village of Auteuil at night. High old stone walls on three sides, a gravel walk, overgrown flower beds gone to seed, and in the centre one old plane tree with a wide pale mottled trunk and bare spreading branches. The ground under the tree is bare, flat, undisturbed earth — no hole, no mound, no turned soil, no spade, no box, nothing marked or buried. Night-blue everywhere; one iron lantern hanging on a bracket on the house wall at the edge of the frame throws a pool of warm gold across the gravel and onto the bare earth under the tree — the only warm light. Reserved colours stay off this plate: no crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no garment or cloak lying anywhere. No figures, no animals, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-auteuil-dining-room.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the long dining room of the old house at Auteuil at night, seen from one end. A long table with a white cloth laid with empty places, two tall silver candelabra lit, high-backed chairs, old panelled walls in faded cream and grey; along the far long wall a row of tall glass doors opening onto the garden, the night beyond them deep blue, and through the central doors the pale trunk of one old plane tree just visible in the dark. Warm candle gold inside, night-blue outside. No portraits or paintings of people. Reserved colours stay off this plate: no crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no garment or cloak lying anywhere. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-villefort-drawing-room.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the drawing room of the King's Attorney's house in the Faubourg Saint-Honoré, seen from a far corner by cold grey winter daylight. Grey-blue panelled walls, a white marble chimneypiece with a cold grate, a cold crystal chandelier, polished floor, straight-backed chairs set in exact order; and through a pair of tall double doors standing open in the side wall, the stair hall beyond, where a straight white marble stair with a plain black iron rail rises to the upper floor — the white stair is the brightest form on the plate. Rerender it as one rectilinear straight run: square-edged parallel treads, a straight flight, and a straight plain iron rail, with no bowed starter steps, curved landing, or turn. Preserve the stair as the plate's single brightest and most dominant light form. Order, polish, no warmth: the colour of a closed file. Redesign the value and colour hierarchy so the stair beyond the open double doors is the single brightest and most dominant light form; lower the exterior window to cold mid-grey daylight, cool/desaturate the floor and furniture, and reduce the gold fittings to near-neutral subdued metal so the room reads as “the colour of a closed file.” Remove every closed rectangular box/case and loose book from the central table, foreground desk, and right-side furniture; leave those surfaces bare rather than substituting another portable prop. Remove the clock, both mantel candelabra, and both console urns completely; leave the mantel and console surfaces bare, without replacement props. Keep the room's marker stack limited to the grey-blue panelling, white marble chimneypiece and cold grate, cold crystal chandelier, ordered straight-backed chairs, and the open double doors framing the straight white stair. No portraits or paintings of people, no flowers. Reserved colours stay off this plate: no crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no garment lying anywhere, no object on the stair. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-noirtier-room.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: an old man's ground-floor room kept as it was in 1815. Dark forest-green walls; an Empire mantel clock of gilt bronze with a plain blank dial and no numerals; a framed eagle — an embroidered Napoleonic eagle under glass, no letters; shelves of old leather-bound books with blank spines; by a tall window with grey daylight, an empty high-backed wheeled armchair — a tall upholstered back, wooden arms, two large spoked wheels — with a dark tartan rug folded over its seat; beside it a small round table with a glass carafe of pale lemon-water and one full glass, upright. Forest green is the accent of this room. No portraits or paintings of people. No crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-valentine-room.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: a young woman's bedroom on the upper floor of the same cold house, at night by cold frost light from the window. White and dove-grey walls; a narrow bed with white curtains drawn back, the white covers smooth and empty; beside it a small night table with a glass carafe of clear water and one full glass of clear water that catches the brightest isolated glint in the room. No visible bedside candle and no broad gold wash. Against the side wall a tall plain wardrobe of pale painted wood, its doors shut. The wall around and beside the wardrobe is continuous and unbroken: no hidden door, no seam, no crack, no gap, no opening, no light leaking from behind it. Remove the large tied bundle of dried herbs, bow, and hanging stems completely and leave that wall bare, without replacing them with another prop or decoration. Rerender the same room as a plainly painted plate: reduce the walls, bed, curtains, wardrobe, and floor to large interlocking dove-grey, cold grey-blue, and chalk-white shapes; make broad dry matte brushstrokes visible across every surface; consolidate the present soft gradients into two or three decisive shadow masses; reserve hard edges for the bed, closed wardrobe, and water glass/carafe only; remove photographic lens realism and polished 3-D surface rendering. Remove both trunks, the ornate box, the books, and the vase; simplify the left foreground to an unadorned partial writing table and plain chair, or crop them out; keep the room's primary marker stack limited to the narrow white-curtained bed, one night table with one clear glass and one clear-water carafe, and the tall closed wardrobe flush against an unbroken party wall. No portraits or paintings of people. Reserved colours stay off this plate: no crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no garment lying anywhere, no red drops in the water. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-garden-gate.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the bottom of a Paris town-house garden at dusk, seen from inside the garden. A high old stone wall thick with dark green ivy; set in it a tall wrought-iron gate of plain black vertical bars, shut; through the bars, a narrow cobbled lane beyond and a blank wall opposite. A gravel path leads up to the gate between bare shrubs. Ivy green against black iron is the accent; cold blue-grey dusk. No crimson-and-gold, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid. No figures, no lettering, no sign or number on the gate or wall. No signature, monogram, artist's mark, or watermark in any corner.
- **set-morrel-house.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the one warm house in the book — a modest Paris apartment on the rue Meslay at evening. Wood floors and plain wood panelling, a small fire burning in a simple fireplace, shelves of worn books, two worn armchairs, lamplight. Remove the bust entirely and fill its footprint with worn books whose spines are blank and unlettered; leave no portrait, bust, statuette, or other human-shaped ornament anywhere on the plate. Remove the box entirely and leave that part of the table clear; do not replace it with any closed rectangular case, casket, or brass-cornered container. On a small side table, a small red silk purse lying under a clear glass dome — the red purse is the accent and the brightest colour on the plate. Warm amber and brown throughout. Replace the landmark with a low 1838 Paris roofline of slate roofs and chimney pots only, with no dominant dome, basilica, or modern landmark. No portraits or paintings of people. No crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no uniform or coat lying anywhere, no pistol case. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-assize-court.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the Assize court of the Palais de Justice in Paris, empty, by grey winter daylight. Dark oak panelling and benches; at the far end a raised bench with a row of empty high-backed judges' seats upholstered in deep red, with red hangings behind them — the red of the bench is the accent; to one side a plain oak desk for the prosecutor; on the other side the prisoner's dock, a box with a heavy oak rail, empty; above, a public gallery of packed wooden benches, empty; tall windows of grey light. No painting, statue, crucifix, coat of arms, or inscription anywhere; no papers with writing. No black robe or garment lying anywhere, no crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-pere-lachaise-vault.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels: the cemetery of Père-Lachaise in heavy rain at a grey dusk. In the centre, a family vault like a small temple of white stone, wet and shining, with a shallow pediment, two short columns, and a heavy black iron door, shut, no light inside it. Black wet trees, other grey tombs and stone crosses behind, a muddy path. The white of the stone in rain is the accent. Every stone surface is blank: no names, dates, initials, inscriptions, or carved letters anywhere. No lantern. No crimson-and-gold, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-count-study.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels. The attached approved plate shows the drawing room of the same house in three separate studies; take only its architecture, palette, and light — lacquer black, ivory panelling, unpolished new gold, tall uncurtained windows — and never copy its panel layout. Draw the Count's study in that house at night: a large black lacquered desk with gold mounts, bare except for one lamp; a black leather chair; tall uncurtained windows black with the night city; black-and-ivory panelling with thin gold mouldings; one lamp's gold light on black. Enormous, correct, and deliberately underfurnished: no family objects, no clutter, no portraits, no books left open, no papers with writing. No crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no cloak or garment lying anywhere. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-count-bedroom.** One unframed 1536 × 1024 landscape setting plate, one single continuous view, never panels. The attached approved plate shows the drawing room of the same house in three separate studies; take only its architecture, palette, and light — lacquer black, ivory panelling, unpolished new gold — and never copy its panel layout. Draw an upstairs bedroom in that house at night: a bed with plain white sheets and pillows, the covers turned back, the bed empty; a plain wooden chair set beside it; a small black night table with one lit candle, the only light; ivory panelling with thin gold mouldings; a tall window with its curtain drawn. Quiet and still. No crimson-and-gold embroidered textile, no amethyst-violet, no bottle-green velvet, no blue-and-gold braid, no garment lying anywhere, no glass or vial on the table. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-vial.** One unframed 1536 × 1024 landscape object plate on a plain neutral warm-grey ground, showing one object only, large in the centre with generous open ground around it: a small cut-crystal flask, the height of a finger, its faceted body filled two-thirds with clear deep red liquid, closed with a small gold stopper, standing upright. Exactly one flask: no second vial, no reflection or shadow that reads as a second flask, no glass, no hand, no label, no box. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-tin-hussar.** One unframed 1536 × 1024 landscape object plate on a plain neutral warm-grey ground, showing one object only, large in the centre with generous open ground around it: a child's painted tin toy soldier, a hussar in a red jacket with gold frogging and a tall black shako, riding a rearing horse on a small flat oval base, the paint a little chipped at the edges, small enough to fit a child's fist. Exactly one toy: no other soldiers, no box, no hand. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-pistol-case.** One unframed 1536 × 1024 landscape object plate on a plain neutral warm-grey ground, showing one object only, large in the centre with generous open ground around it: a closed duelling-pistol case of dark polished wood, a flat rectangular box with brass corner pieces and a small plain brass keyhole plate, the lid shut. No pistols visible, no engraving, no monogram, no nameplate, no hand. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-pastille-box.** One unframed 1536 × 1024 landscape object plate on a plain neutral warm-grey ground, showing one object only, large in the centre with generous open ground around it: a small round gold box with a hinged lid standing open, plain polished gold with no engraving, holding one small white pastille. Exactly one pastille, white; no red anywhere, no vial, no glass, no hand. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
