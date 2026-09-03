# Reference Plan — approved as a system

**Nothing generates a page until every character visibly on that page has an
approved permanent lock.** Not just-in-time. Locks live in `refs/approved/` and
get there only through `tools/refs.py promote` with an independent critic
report. A sheet in `refs/candidates/` is not a lock.

## Canvas and register — for every sheet

Reference sheets are **1536 × 1024 landscape**; story pages are portrait. This
is not an inconsistency: four views across a wide canvas is what a lock needs.

**Register, verbatim in every generative sheet prompt:**

> **Mineral Ink.** Brush-and-ink line on toothed paper, with flat washes of
> mineral pigment: malachite green, azurite blue, cinnabar red, shell white,
> and gold leaf laid flat. The Chinese blue-green landscape tradition lit like
> a film, with real cast shadows and real depth. Visible ink line, visible
> paper tooth, pigment pooling at the edges of a wash. Not smooth prestige-oil
> realism. No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no anime proportions, no children's-book softness, no
> plastic 3D render.

Every character sheet closes with the anti-collision clause, verbatim:

> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.

**No sheet carries lettering of any kind** — no name plates, no labels.
Labelled sheets teach the page model to letter the art.

## Anchoring (sequels)

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| — | first book; no parent | — |

Within this book, sheet 09 (Wukong, furnace-tempered) is anchored on the
approved sheet 01 as an image input: same face, same armor, scorched, eyes
changed. A state pass, not a redesign.

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
named. **Boards are critic-only rasters and never generation inputs** — their
file names carry `board`, `adversarial`, `silhouette` or `live-pair` so the
tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 01 | `01-wukong` — Great Sage armor default; view (d) stone-born, leaf kilt | character | 1 | p1 | new |
| 02 | `02-old-ma` | character | 2 | p2 | new |
| 03 | `03-subhuti` | character | 8 | p8 | new |
| 04 | `04-laozi` | character | 19 | p19 | new |
| 05 | `05-jade-emperor` | character | 19 | p19 | new |
| 06 | `06-ao-guang` | character | 16 | p16 | `06-ao-guang` (continuity anchor) |
| 07 | `07-erlang` — with lance and hound in view (b) and (d) | character | 35 | p35 | new |
| 08 | `08-buddha` | character | 43 | p43 | `08-buddha` (gate revision: attach the approved sheet and change only the hand and the crown) |
| 09 | `09-wukong-tempered` — scorched armor, gold eyes with red ring | character (state) | 41 | p41 | `01-wukong` |
| — | `board-heads` — all eight, same light, same angle | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — all eight, full length | board | — | — | from approved sheets |
| — | `adversarial-subhuti-laozi` — same panel, same light, both three-quarter and profile | board | — | — | `03-subhuti` `04-laozi` |
| — | `adversarial-wukong-old-ma` — same panel, both monkeys, grayscale pass | board | — | — | `01-wukong` `02-old-ma` |
| — | `adversarial-emperor-laozi` — throne step, both robed | board | — | — | `04-laozi` `05-jade-emperor` |
| — | `live-pair-wukong-old-ma` — unlettered, page scale, the p14 staging | board | — | — | `01-wukong` `02-old-ma` |
| — | `set-peak` — Flower-Fruit peak, split stone, waterfall | set | 1 | p1 | — |
| — | `set-cave` — Water Curtain Cave interior, bridge, stone house | set | 4 | p4 | — |
| — | `set-courtyard` — the Master's courtyard, pine, cave mouth, round door | set | 8 | p8 | — |
| — | `set-sea-palace` — Ao Guang's hall and treasury, pillar glow | set | 15 | p15 | — |
| — | `set-south-gate` — the gate on cloud, tower guards | set | 21 | p21 | — |
| — | `set-hall-of-jade` — throne, steps, pillars, water floor | set | 19 | p19 | — |
| — | `set-stables` — white wood, cloud roof, desk | set | 22 | p22 | — |
| — | `set-peach-garden` — three terraces, three blossoms | set | 29 | p29 | — |
| — | `set-laboratory` — black iron, cinnabar, the furnace | set | 33 | p33 | — |
| — | `set-edge-of-world` — white nothing, five pillars | set | 44 | p44 | — |
| — | `set-five-elements` — the hand-mountain beside the peak, cleft, seal | set | 46 | p46 | — |
| — | ~~`obj-staff`~~ — retired 2026-09-02 after six candidates: the staff's lock is the staff in hand on `01-wukong` and `09-wukong-tempered` and the needle behind the ear on `01-wukong` views (a) and (c); page prompts cite those sheets | — | — | — | — |
| — | `obj-banner-seal-peach` — the banner whole, the gold paper seal, the head-sized peach | object | 25 | p25 | — |
| — | `obj-gourds-ring` — exactly five gourds, the iron ring | object | 33 | p33 | — |
| — | ~~`obj-staff-banner-gourds`~~ — retired 2026-09-02 after six candidates: six objects on one canvas thrashed; split into the three plates above | — | — | — | — |

**Generation order:** `01-wukong` (everyone collides with him, and he is on
every page); then the risky lanes, `02-old-ma` and `03-subhuti` / `04-laozi`;
then `05-jade-emperor`, `08-buddha`; then the cheapest faces, `06-ao-guang`,
`07-erlang`; then `09-wukong-tempered` from the approved 01; then boards
(head and silhouette boards are crop-and-place from approved pixels, not
generations); then adversarial and live-pair boards; then plates in page
order.

## States needed, enumerated from the script

| Character | State | Pages |
|---|---|---|
| Wukong | stone-born: bare, leaf kilt, no ornament | 1–17 |
| Wukong | Great Sage: gold scale armor, red tunic, tiger-skin kilt, black cloud-boots, plumed cap; staff or needle behind ear | 18–40 |
| Wukong | tempered: state above, scorched, plumes singed at tips, gold eyes with a thin red ring | 41–47 |
| Wukong | in chains, ring on head (p38), ring off (p39) | 38–39 |
| Old Ma | one state: shawl, stick. Snow on the shawl, p47 | 2–47 |
| Subhuti | one state | 8–13 |
| Laozi | default: indigo, gourd, scroll or basket in hand | 19–43 |
| Laozi | no smile, no dabbing: pp 34, 38, 39, 42 (expression, not costume) | 34–42 |
| Jade Emperor | seated default; standing p27; pressed to the throne p42 | 19–45 |
| Ao Guang | seated; off the throne p17 | 16–18 |
| Erlang | armored with lance; hound at heel; hawk/cormorant/crane forms p36 are scenery shapes, not a sheet state | 35–39 |
| Buddha | seated, one hand open; the hand alone at page scale p43–45 | 43–46 |

## Nearest lookalikes and what carries the separation

Carried from `04-CHARACTER-LEDGER.md`; the sheet prompt for each names its
lookalike and the differentiators that must survive grayscale and thumbnail.

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 Wukong | 02 Old Ma; 07 Erlang in armor | gold vs gray fur; smooth vs lined muzzle; mid-leap vs stooped; round amber vs half-lidded pale eyes. Muzzle vs human face; back-curving plume pair vs single standing plume |
| 02 Old Ma | 01 Wukong | as above, inverted |
| 03 Subhuti | 04 Laozi; 08 Buddha | long face vs round; topknot vs bald crown; pointed beard vs square; lean vs stout; whisk vs gourd; pale gray-blue vs indigo. Beard vs none; man-scale vs giant |
| 04 Laozi | 03 Subhuti; 05 Jade Emperor | as above; white square beard vs black three-point; bald vs beaded crown; standing vs seated |
| 05 Jade Emperor | 04 Laozi | black beard, crown, prime of life, seated |
| 06 Ao Guang | none | dragon head, antlers, whiskers; nothing else in the cast is not a face |
| 07 Erlang | 01 Wukong in armor | human face, third eye, silver vs gold armor, single standing plume |
| 08 Buddha | 03 Subhuti | no beard, broad face, curled dome, giant, saffron |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`). Brown monkeys are bare and young; students
  are shaved and beardless; soldiers wear faceplates; guards in the sea are
  shrimp and crab.
- A rejected sheet never becomes a lock and never becomes an input.
- **Art note carried from the script gate (p44):** the letters Wukong scratches
  into the pillar read red because the needle-staff leaves cinnabar where it
  cuts, the way it glows dull red in the sea. The object plate shows the staff
  at needle size with a red tip.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas: **(a)** three-
quarter head and shoulders, neutral expression, even light; **(b)** full-length
standing figure, default costume, habitual posture; **(c)** strict profile, same
light; **(d)** the one state the script actually needs (age phase, disguise,
grief, travel clothes).

## 01 — WUKONG

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Sun Wukong, the Monkey King. A monkey, not a man: short heart-shaped face, a
pale hairless muzzle and pale cheek patches against golden-tawny fur, a wide
mouth, large round amber eyes set wide, a low brow, small ears standing out
from the skull, a golden ruff of fur around the head that is fur and not hair.
Small and wiry, long arms, a long tail always in frame. He never stands
square: one foot up on something, or crouched, or mid-leap. Habitual gesture:
a flat hand shading his eyes to look far away. Expression at rest: about to
laugh.

Default costume, views (a), (b), (c): golden scale armor over a red tunic, a
tiger-skin kilt, black cloud-boots, and a cap with two long pheasant plumes
curving back over his head. A red-lacquered iron staff with gold bands at each
end, taller than he is, in his hand in view (b).

View (a): a true three-quarter head-and-shoulders study in even light,
expression at rest and about to laugh, large enough to lock the short
heart-shaped face, low brow, wide-set round amber eyes, wide mouth, small
projecting ears, golden ruff, pale muzzle and cheek patches, and needle behind
the ear. The brow and face lock are unobscured; the habitual shading gesture is
kept in the full-body view (b).

View (b): a full-length armored view with the habitual flat hand shading his
eyes, reposed in a clean crouch or mid-leap so the small, wiry, never-square
posture reads without an invented support.

View (c): a true ninety-degree armored profile from brow through boots,
preserving the short forward muzzle, low brow, projecting ear, circular golden
ruff, visible needle, small wiry build, long arm, long tail, non-square stance,
and two separately readable back-curving plumes. This profile establishes the
body silhouette as well as the face.

Views (a)–(c) have no mountain scenery and no rock supports, leaving only the
plain warm paper.

View (d): the same monkey before the armor: bare, a kilt of leaves, no
ornament, no needle, one foot up on a split stone. This split stone is the only
rock support on the sheet.

Wukong must never be confused with Old Ma, the elder monkey. Differentiators
that must survive grayscale and thumbnail: gold fur against her gray, a smooth
muzzle against her white lined one, an upright leaping body against her stoop,
round bright eyes against her half-lidded pale ones. He must never be confused
with Erlang: a monkey's muzzle, never a human face; two back-curving plumes,
never one standing plume; gold armor, never silver.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — OLD MA

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Old Ma, elder of the monkeys. A monkey, unmistakably very old. Long narrow
face, the muzzle gone white, silver-gray fur thinning at the crown, white
tufted brows, pale half-lidded eyes, deep lines at the mouth. Small and
stooped, walking bent over a peach-wood stick; when seated, knees up and arms
wrapped around them. Habitual gesture: one hand laid flat on top of a smaller
monkey's head (view (d) shows this, her hand on the head of a small brown
monkey drawn only as a shape, no face detail). Costume: a faded red shawl over
the head and shoulders, nothing else.

Views: (a) three-quarter head and shoulders, level and dry; (b) full length,
stooped over the stick; (c) strict profile; (d) seated on a rock, knees up,
hand on the small monkey's head, the shawl dusted with snow.

Old Ma must never be confused with Wukong. Differentiators that must survive
grayscale and thumbnail: gray fur against his gold, a long white lined muzzle
against his short smooth one, a stoop and a stick against a leap, half-lidded
pale eyes against round bright ones, a shawl against armor. She has no human
trait.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — SUBHUTI

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Subhuti, the Master. A lean old man, tall and straight as a post. Long narrow
face, high forehead, hooded eyes, a thin high-bridged nose, a long white beard
falling in one narrow point to mid-chest, white hair drawn up into a topknot
with a plain wooden pin. Thin body, no stomach. Stands with his hands folded
inside his sleeves. Habitual gesture: a white horsetail whisk held low, about
to be flicked once. Expression: level; every look is a test. Costume: a robe
of one pale gray-blue value, no pattern, no gold, no ornament.

Views: (a) three-quarter head and shoulders; (b) full length, hands in
sleeves, whisk under one arm; (c) strict profile showing the beard's single
point and the topknot; (d) the whisk raised for the flick, the face unchanged.

Subhuti must never be confused with Laozi. Differentiators that must survive
grayscale and thumbnail: a long face against a round one, a topknot against a
bald crown, a beard in one long point against a short square beard, a lean
straight body against a stout forward-leaning one, stillness against fuss, a
whisk against a gourd, a pale plain robe against a dark sashed one. He must
never be confused with the Buddha: he has a beard and a topknot and is the
size of a man.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — LAOZI

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Laozi, counselor and alchemist to the Jade Emperor. A round old man: round
face, round cheeks, small bright eyes, a bald shining crown with white hair
only at the sides and back, a short square white beard, a round belly. Short,
quick on his feet, standing with his weight forward and both hands busy.
Habitual gesture: dabbing his brow with his sleeve. Expression at rest: warm,
worried, one step ahead. Costume: deep indigo robes with a gold sash, a dried
gourd on a cord at his hip.

Redraw the same beard in all four views as a short, jaw-width white block
ending no more than two finger-widths below the chin, with vertical sides and
a blunt horizontal lower edge; no central taper, point, or dangling profile
tuft.

Replace them with one unmistakable dried bottle gourd on one cord at the same
hip, with the same two-lobed silhouette, scale, and attachment in every view
where the hip is visible. No second vessel may remain to propagate as a
recurring costume prop.

Views: (a) three-quarter head and shoulders, dabbing; (b) full length, weight
forward, a gold scroll in one hand; (c) strict profile showing the bald crown
and square beard; (d) the same man with the smile gone and the sleeve down,
holding a dull iron ring the size of a bracelet.

Close the tooth-showing mouth into a small closed worried half-smile and raise
the inner ends of the short white brows slightly while keeping the small
bright eyes alert; retain view (d) as the fully unsmiling reaction state.

Laozi must never be confused with Subhuti. Differentiators that must survive
grayscale and thumbnail: a round face against a long one, a bald crown against
a topknot, a short square beard against a long pointed one, a belly against a
straight lean line, motion against stillness, a gourd against a whisk, dark
indigo against pale gray-blue. He must never be confused with the Jade
Emperor: white beard, bare head, standing, old.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — THE JADE EMPEROR

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

The Jade Emperor, ruler of Heaven. A broad-faced man in his prime, about
fifty: heavy jaw, full cheeks, black brows, black eyes, a black beard trimmed
into three points, black hair hidden under the crown. Heavy build, seated
whenever possible, hands on his knees. Habitual gesture: two fingers pressed
to his temple. Expression: a man who ends conversations. Costume: robes of
yellow-gold with dragon roundels; a flat-topped jade crown with strings of
beads hanging before his face.

Views: (a) three-quarter head and shoulders, beads parted enough to read the
face; (b) full length, seated on a plain block, hands on knees; (c) strict
profile, the beads and the beard's three points; (d) on his feet, beads
swinging, one hand up.

The Jade Emperor must never be confused with Laozi. Differentiators that must
survive grayscale and thumbnail: a black beard against a white one, a crown
against a bald crown, the prime of life against old age, seated against
standing, yellow against indigo. His is the only black beard in the cast.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — AO GUANG

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground. No lettering, labels, watermarks,
panel rules, view boxes, or enclosing border.

Ao Guang, the old and vast Dragon King of the Eastern Sea, is a dragon in the
shape of a lord. Give him a long horse-like dragon head, a scaled blue-green
face, a heavy brow, and large round golden eyes, each with one centered
vertical slit pupil. Two branching antlers crown the head. Two long white
whiskers float as if underwater and are the only filament-like facial hair.
His beard is a continuous mass of overlapping blue-green fin plates rooted
along the underside of the jaw and converging beneath the chin, never a
hanging goatee.

His human-shaped body is enormous and lordly. Seated on a coral throne, he
reads as about twice the height of a standing man and visibly larger than any
ordinary person; this is a page-readable scale impression, not an exact
drafting ratio. One hand lies over a clear horizontal throne arm in mid-drum,
with some fingertips touching and another visibly lifted so the fingers read
as beating a rhythm rather than gripping. He does not rise until alarm drives
him from the throne. His expression is grand, weary, and very polite up to the
edge of panic.

Costume: deep sea-green robes patterned with waves, a coral crown, and one
pearl at the throat. Keep the robe value pattern, crown silhouette, and pearl
consistent in every view.

Views: (a) three-quarter head and shoulders, clearly showing the round eye,
slit pupil, antlers, whiskers, and fin beard; (b) full length seated on the
coral throne with the drumming hand, beside a neutral bald featureless adult
human silhouette on the same ground plane whose head-to-foot height reads as
roughly half of Ao Guang's seated antler-tip-to-foot height; (c) strict
profile, preserving the projecting horse-like muzzle, antlers, round eye,
whiskers, and fin plates; (d) standing in alarm, with the same face and round
eye widened and the whiskers held straight out.

Ao Guang has no lookalike in the cast. His projecting dragon head, antlers,
whiskers, fin beard, vast body, and coral-throne silhouette must remain
unmistakable at page scale, in profile, in grayscale, and after a long
absence. Never give him a human face or an ordinary-man scale.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — ERLANG

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Erlang, champion of Heaven. A young man, human, about twenty-five, handsome
and sharp: a long jaw, high cheekbones, a straight nose, level dark brows, and
a third eye set vertically in the center of his forehead, open and alert.
Black hair in a high topknot under a small silver helmet with one red plume
standing straight up. Tall, athletic, standing square with his weight even.
Habitual gesture: the third eye narrowing while the other two stay still.
Expression: amused, direct, sporting. Costume: silver-white armor over a dark
tunic, a yellow-gold sash. A three-pointed double-edged lance held upright.
A lean gray hound at his heel.

Views: (a) three-quarter head and shoulders, all three eyes open; (b) full
length with the lance upright and the hound sitting at his heel. Redraw view
(c) at the same true ninety-degree angle with a shallow but unmistakable
forward projection and eyelid seam centered above the normal brow, aligned to
the third eye's placement in view (a). Preserve the long jaw, high cheekbone,
straight nose, and single upright plume. Redraw view (d) with both ordinary
eyes equally open, aligned on one level axis, and holding the same forward
gaze; narrow only the vertical third eye to a clearly thinner vertical
aperture. Carry the laugh through the open mouth, lifted cheeks, and
nasolabial folds without changing either ordinary eyelid.

Erlang must never be confused with Wukong in armor. Differentiators that must
survive grayscale and thumbnail: a human face against a monkey's muzzle, skin
against fur, a third eye, one standing plume against two back-curving plumes,
silver armor against gold. He has no beard.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — THE BUDDHA

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Rebuild all four views on one uninterrupted plain warm-paper field; remove
every vertical and horizontal dividing edge, architectural frame, and scenic
compartment so no view is boxed or bordered.

The Buddha. A serene giant, seated, larger than any room he is in. Broad
smooth face, half-closed eyes, a small smile, long earlobes, golden skin, a
bare head of tight dark curls rising to a small dome at the crown. Broad
round shoulders, one hand always visible and open. He does not gesture.
Costume: a plain saffron robe over one shoulder, no ornament.
Remove the gold disk completely. Carry tight dark curls continuously from the
hairline over the entire cranium. Redesign all three crowns to the same low
hemispherical dome: one curl-row high (approximately 10–15% of skull height)
above the surrounding cranium, broadest at its base, with no conical taper.
Carry the same tight dark curl size continuously from hairline through dome
and preserve that dome height and outline in three-quarter, front, and profile.
No halo, smooth gold cap, crown, or other head ornament may remain.

Views: (a) three-quarter head and shoulders; (b) full length seated, one hand
open palm-up on his knee, a small human-sized figure drawn only as a
silhouette on the floor before him for scale; (c) strict profile, the curled
dome and the long earlobe; (d) the open hand alone, palm up, filling the
view, the fingers slightly curled.
Redesign the full-length pose by rotating the forearm inward and lowering it
until the heel and ulnar edge of the palm rest on the near knee, palm up, with
a neutral wrist and the elbow tucked beside the torso; remove all forward or
downward reach and keep both shoulders level. Keep the torso motionless. Do
not change the isolated hand view. The isolated hand view may retain its
slightly curled palm-up fingers.

The Buddha must never be confused with Subhuti. Differentiators that must
survive grayscale and thumbnail: no beard against a long beard, a broad round
face against a long narrow one, a curled dome against a topknot, a giant
against a man, saffron against gray-blue. He never stands. He never frowns.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

Gate revision, the only two changes from the attached approved sheet:
(1) in the full-length seated view, rotate the forearm inward and lower it
until the heel and outer edge of the palm rest on the near knee, palm up,
wrist neutral, elbow tucked beside the torso, both shoulders level, with no
forward or downward reach; leave the isolated hand view unchanged. (2) On
the three head-bearing views, carry one continuous curl size from the
hairline over the cranium and reduce the crown rise to one curl-row, about a
tenth of the skull's height, one low hemispherical outline broadest at its
base with no taper, identical in three-quarter, front, and strict profile;
no halo, cap, crown, or smooth gold patch.

## 09 — WUKONG, TEMPERED (state sheet, anchored on approved 01)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved `01-wukong` sheet; this is the same monkey, same face,
same armor, after forty-nine days in a furnace.

Everything in sheet 01 holds: heart-shaped face, pale muzzle, golden fur,
wide mouth, small ears, golden ruff, wiry body, long tail, plumed cap, gold
scale armor, tiger-skin kilt, cloud-boots, the red staff. What has changed:
the armor is scorched and smoke-darkened at every edge, the plumes are singed
to black at their tips, and the eyes are gold, with a thin red ring of fire
around each iris. The scorch is on the armor and the plumes, never on the
face. The face reads as the same character at thumbnail; only the eyes are
new.

Views: (a) three-quarter head and shoulders, the gold eyes plain; (b) full
length mid-leap with the staff, chains falling off him in pieces; (c) strict
profile; (d) only the face and eyes, close, the red ring visible.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board prompts (critic-only rasters, generated from the two attached approved sheets)

- **adversarial-subhuti-laozi.** The two old men from the attached sheets in one frame, standing side by side at the same distance under the same flat even light, both in three-quarter view on the left half of the canvas and both in strict profile on the right half, plain warm-paper ground, no costume emphasized, no props in hand, no lettering. Each face must be exactly the face on its sheet.
- **adversarial-wukong-old-ma.** The two monkeys from the attached sheets in one frame, standing side by side at the same distance under the same flat even light, in color on the left half of the canvas and the identical pair rendered in pure grayscale on the right half, plain warm-paper ground, no lettering. Each face must be exactly the face on its sheet. Replace both the color and grayscale right-hand figures with Old Ma's approved identity: lengthen and narrow the face and muzzle; make the muzzle white; change all golden fur to silver-gray with a visibly thinning crown; add white tufted brows, pale half-lidded eyes, and deep mouth lines; reduce and stoop the build over a peach-wood stick; and replace the leaf skirt with her faded red shawl and nothing else. These locks must remain legible in a costume-free face crop and at thumbnail size. Rebuild the opposing view with the approved Wukong face unchanged on the left and a strict Old Ma profile on the right: Wukong's muzzle stays short, blunt, and lifted beneath a wide round amber eye, while Old Ma's muzzle must project longer and lower beneath a pale half-lidded eye, with a receding crown, white brow tuft, lined mouth, and white chin hair defining the silhouette. Repeat that exact pair without facial drift in grayscale.
- **adversarial-emperor-laozi.** The two men from the attached sheets on the steps of a plain throne dais, the seated one one step above the standing one, same flat even light, three-quarter view, plain ground, no lettering. Each face must be exactly the face on its sheet. Redesign that figure to retain Laozi's long bald crown with white hair only at the rear and sides, broad round cheeks and bulbous nose, short square white beard with no black mustache or pointed extension, and stout barrel build with dropped shoulders. Remove the square imperial crown and black hairline entirely. These markers must remain plainly visible in the strict profile and at thumbnail size so that the pair reads as crowned, black-bearded Emperor versus bald, white-bearded Laozi in grayscale.
- **live-pair-wukong-old-ma.** A single unlettered story-scale image: on a bare stone mountain peak beside a split boulder, the old gray monkey from one attached sheet lays her hand flat on the head of the young gold monkey from the other, who has just stepped off a small cloud and is in his stone-born state exactly as in view (d) of his sheet: bare, a kilt of leaves, long tail, no armor, cap, plumes, boots, staff, needle, or ornament, his short lifted muzzle and bright round eyes clear beneath her hand; a crowd of small brown monkeys, faceless, on the slopes behind. Warm morning light. No balloons, no captions, no text of any kind. Each face must be exactly the face on its sheet.

## Setting plates and the object plate

Each plate is 1536 × 1024 landscape, architecture and palette only, **no
figures, no lettering**. Register paragraph verbatim. One line each:

- **set-peak.** Flower-Fruit Mountain's bare stone summit with the split
  boulder, light in the split; the waterfall off the cliff to one side; fruit
  trees down the flanks; the eastern sea; malachite and mist, warm morning.
- **set-cave.** The Water Curtain Cave from inside: the waterfall as a silver
  wall on the left, an iron bridge over the pool, a dry stone house cut into
  the mountain with stone beds, bowls, stools, a hearth. Blue-green water
  light, warm firelight inside. Replace every freestanding brown wooden stool
  or bench with a monolithic stool cut from the same gray cave stone as the
  beds and platforms. Remove all wood color, grain, thin timber legs, and
  joinery so the furnishings read as the ancient stone beds, stone bowls, and
  stone stools required by the location lock. Remove the metallic gold-leaf
  patches scattered across the ceiling and right-hand vault. Rebuild those
  surfaces as charcoal stone with malachite and azurite mineral washes under
  cool blue-green water light; confine the only warm color to the
  orange-cinnabar fire and its short local spill inside the hearth, leaving
  the silver falling-water wall as the location's restrained accent. Rebuild
  the complete crossing as visibly forged dark iron: a thin iron deck or
  trussed span, iron uprights and rails, and exposed iron connections, with no
  stone-block parapet or carved stone balusters. Stone may remain only at the
  abutments or footings. The bridge's dark metal silhouette must remain
  unmistakable against the gray stone platforms at thumbnail size and in
  grayscale.
- **set-courtyard.** White gravel raked in lines, one pine, a cave mouth in a
  gray cliff, a bell, and a small round door in the cliff, shut. Pale, cool,
  dawn. Remove every metallic-gold streak and ochre-gold patch from the cliff
  and sky. Rebuild the cliff as cool shell gray with restrained desaturated
  azurite and malachite shadow washes, retain the white raked gravel, and keep
  the dawn illumination pale and cool; no gold leaf may remain in this
  non-Heaven location. Rebuild the shut round back door as an unornamented,
  desaturated blue-gray or weathered gray slab set flush into the cliff. Remove
  the cinnabar-red field and gold trim/fitting; retain one clean circular
  outline, a closed central seam, and at most one small plain dark pull so the
  required primary marker survives grayscale and thumbnail without borrowing
  the monkey/Heaven color codes. Reduce the bell silhouette to less than half
  the round door's diameter and hang it from a plain side bracket beside the
  cave mouth rather than in the center of the cave opening. Lift the entire
  visible cave interior by two clear value steps to a cool mid-dark
  shell-gray/azurite wash, with legible interior rock planes rather than a
  single dark mass. At the same time, give the round door one continuous
  desaturated blue-gray value that is one step darker than the immediately
  surrounding cliff and preserve a clean circular edge, closed central seam,
  and single small dark pull. The door, not the cave void or bell, must become
  the strongest compact accent when the plate is reduced to thumbnail size
  and converted to grayscale.
- **set-sea-palace.** Ao Guang's hall: crystal and coral, columns of white
  shell, a sand floor lit from above, fish in the hall, a coral throne; a
  treasury doorway at the back with a dull red glow. Azurite and crystal, no
  green. Rebuild the rear treasury opening around one unmistakable red-iron
  pillar: a single straight cylindrical vertical with parallel sides, an
  unbroken shaft, and a clean narrow silhouette extending from the treasury
  floor upward. Make that shaft glow dull cinnabar red with only a short local
  spill, and remove the branching warm cluster behind it. The pillar must
  remain the dominant narrow upright in the rear opening at thumbnail size and
  in grayscale. Rebuild every coral mass and the throne surround in cool
  shell-white, desaturated blue-violet, or azurite; neutralize the columns and
  floor to cool shell-white and pale sand under blue overhead light; remove the
  gold/ochre tracery. Reserve all cinnabar warmth for the single dull-red pillar
  and its short treasury spill so the primary marker remains unique on re-entry
  after a long absence.
- **set-south-gate.** A gate the size of a city, gold on white cloud, doors
  open, tower-sized armored guards with faceplates on either side, palaces
  rising behind. Gold leaf and cloud-white, noon. Redesign the plate by
  removing both humanoid bodies, faces, armor, helmets, swords, and plinth
  figures entirely; preserve the required monumental flanking-guard idea as
  two unoccupied, matching gatehouse towers integrated into the left and right
  architecture, while keeping the central gate visibly open. Redesign the
  atmospheric field as shell-white and cloud-white banks with pale-gold edges,
  reducing blue-green to only faint cool shadow traces; light both tower faces
  and the lintel in the same high-key, everywhere-noon value range. Preserve
  the fully open central portal as the primary marker and the single deepest
  spatial value, with the gold-leaf gate against white cloud remaining the
  dominant thumbnail read.
- **set-hall-of-jade.** A hall the size of a valley: a throne at the top of a
  flight of steps, jade-green pillars, a floor like still water. Pale gold and
  jade. A second view with long tables laid for a banquet. Remove the rule
  entirely and rebuild both views as separate unframed studies that vignette
  into one continuous warm-paper ground; no hard line, box edge, panel frame,
  or contrasting gutter may remain anywhere between them. Repaint every red
  side pillar jade-green and reduce the blue wall bands to pale, desaturated
  jade shadow; keep pale gold on the throne axis and step nosings. Lower the
  lantern poles and tabletop clutter below the top of the stair flight,
  preserve a fully uninterrupted central aisle, and increase the value
  separation of each step edge so the throne's steps are the single dominant
  compact marker in both views at thumbnail and after a long absence.
- **set-stables.** A long stable of white wood under a cloud roof, stalls down
  its length, a small desk with a ledger by the door, a nail for a cap. Warm
  hay light. Rebuild both visible pages as completely blank unmarked paper:
  remove every glyph, stroke, ruled line, numeral, and pseudo-text mark while
  preserving the ledger's open-book silhouette on the intact desk. Rebuild the
  entire overhead roof plane as one continuous shell-white cloud canopy with a
  clearly lobed cloud edge and restrained pale-gold rim light; remove the dark
  teal ceramic tiles and hard tiled eave silhouette. Keep the exposed
  supporting rafters and stall fronts white wood so the thumbnail reads
  unmistakably as white stables under a cloud roof, with the intact desk
  remaining the compact primary marker by the door. Remove every horse form
  from every bay, including all heads, ears, eyes, backs, legs, and tack.
  Rebuild the openings as empty stall interiors: uninterrupted deep warm-gray
  shadow behind the white vertical slats, with loose hay confined to the stall
  floors. Preserve the current camera, intact desk, blank open ledger, cap nail,
  continuous lobed cloud canopy, white rafters, and warm hay light.
- **set-peach-garden.** Three terraces of peach trees on a hill in Heaven,
  three colors of blossom, fruit the size of a head, one huge tree at the top.
  Pink, green, gold, late afternoon.
- **set-laboratory.** A round room of black iron and cinnabar red, shelves of
  gourds and jars, a bronze furnace taller than a man with a lid like a temple
  roof, firelight only. Replace every blue-green floor plane and reflection
  with matte black-iron plates or charcoal-black stone reflecting only
  amber-orange furnace light; retain the cinnabar walls and bronze furnace,
  and introduce no blue, teal, or green pigment anywhere in the room. Rebuild
  one clearly highest, continuous shelf as the primary marker, place exactly
  five individually countable dried bottle gourds on that shelf with no other
  vessel on its tier, and preserve enough empty wall around that shelf that the
  same shelf will read unmistakably when empty. Other tiers may retain
  subordinate jars and gourds.
- **set-edge-of-world.** A flat white nothing, no horizon, five pale pink
  pillars rising into white and tapering out of sight. Rebuild the field with
  exactly five independently readable pale-pink shafts, spaced so all five
  remain countable at thumbnail and in grayscale; every shaft must emerge
  directly from the white field, continue without interruption, and narrow by
  visibly converging sides until it passes beyond the top edge. Remove every
  stair, rail, post, finial, plinth, base ring, carved panel, ledge, and floor
  joint. Rebuild the entire ground and sky as one uninterrupted shell-white
  field with no horizon, plane break, texture cue, or architectural support;
  the five pale-pink shafts must be the only forms in the image. Remove all
  gold, brown, gray, blue-gray, and black pigment and eliminate every cast
  shadow. Light the plate as a diffuse, shadowless white field, retaining only
  restrained pale pink within the five shafts so the later page-specific red
  writing can remain the sole accent without being pre-empted by the reference
  plate.
- **set-five-elements.** The coast beside Flower-Fruit Mountain: a bare
  mountain of five ridges like fingers pressed into the earth, a cleft at its
  base, a gold paper seal on its summit; the green peak with its split stone
  and a red banner across the water. One view in summer, one under snow.
  Redesign the sheet as two unframed landscape vignettes on one continuous
  warm-paper ground, with open or feathered space separating the states and no
  ruled, full-width, or edge-to-edge dividing line. Remove every tree, shrub,
  and green groundcover from the five-ridge hand-mountain in both states;
  retain exposed stone in the first state and snow directly on exposed stone
  in the last-page state. Recompose both states to include a separately
  readable Flower-Fruit peak beside the new five-ridge mass, preserving
  Flower-Fruit's bare summit split stone and waterfall so returning readers can
  identify the old location after the long absence. Cut one deep, dark,
  face-sized cleft into the base of the central ridge, with enough open rock
  around it to stage Wukong there on the page; keep the reference plate itself
  figure-free. Remove both red bands completely from both states; no bridge,
  ribbon, banner, causeway, or red wake may cross the water on this plate.
  Replace it with one thin, vertical gold-leaf paper strip visibly affixed flat
  to the summit rock, narrow enough to read as paper rather than architecture
  and with no legible glyphs on the reference plate.
- **obj-staff.** *Retired; see the manifest. The staff and needle are locked on the Wukong sheets.*
- **obj-banner-seal-peach.** On plain warm paper, three isolated objects with clear space between them: a cinnabar-red cloth banner, whole and unfaded, held out in a wind-filled flying shape with one continuous unbroken outer hem and no writing, no support pole visible; a paper-thin vertical strip of gold-leaf paper at least four times taller than wide, flat, glyph-free, with one shallow edge bow or turned lower corner so its primary silhouette reads as curled paper at thumbnail and in grayscale, with no visible side thickness or heavy block-like shadow; and a peach the size of a monkey's head with one clear cleft. No lettering. Remove every mountain, shoreline, water, mist, cast scenic wash, and gray cast-shadow wash extending outside the gold seal and peach silhouettes; place the same three objects on one uninterrupted plain warm-paper ground, completely around all three objects, with every red, gold, peach, and gray pigment mark confined inside the objects' outer contours.
- **obj-gourds-ring.** On plain warm paper, two isolated objects: exactly five dried bottle gourds, each with a pinched neck and a round bulb, laid side by side with their contours not touching so the count of five reads at thumbnail; and one dull iron ring the size of a bracelet, plain, unornamented. Nothing else. No lettering.
