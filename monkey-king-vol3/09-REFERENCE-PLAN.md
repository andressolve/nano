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

**No sheet carries lettering of any kind** — no name plates, no labels, no
glyphs on the bones, the gate, the pagoda, or the banner. Labelled sheets teach
the page model to letter the art. The one inscription the story needs, WHITE
BONE LADY cut into the skull's brow (pp 15–16), is lettered on the page from
the script's exact string; its plate `obj-bones` locks the skull, the heap and
a smooth flat carved band across the brow where the page letters it, and
carries no letters itself (the plate brief's no-lettering line is hard-coded
in `tools/refbrief.py`, and a misspelt inscription on a lock would be copied
onto every page).

**No blood anywhere** — not on the fallen disguises, the bones, the meat, the
horse's foreleg, the dragon, or any weapon. A wound is a clean dark line.

**Volume palette shift** (`05-SETTINGS-AND-OBJECTS.md`): White Tiger Ridge is
drained to chalk-white, bone and ash with hazy azurite valleys, the afternoon
going long and amber; its only warm round accent is the peaches. Flower-Fruit
Mountain is Volume I's wet malachite and white water with an orange western
evening. The pine wood is black-green; the pagoda is gold outside and black
stone inside, with one shaft of cold moonlight on the cage. The road west at
the end is clean early green and far azurite.

## Anchoring (sequels)

Parent anchors live in `refs/parents/`, copied byte-identical from
`../monkey-king-vol2/refs/approved/` (`10-wukong`, `02-sanzang`, `05-dragon`,
`06-white-horse`, `07-bajie`, `08-wujing`, and `03-guanyin` for the
critic-only comparison board) and from `../monkey-king-vol1/refs/approved/`
(`v1-09-wukong-tempered`, `v1-set-peak`, `v1-set-cave`). `tools/refbrief.py`
resolves every anchor name in the manifest's last column under
`refs/approved/`; a parent anchor is therefore written `../parents/<file>` and
resolves to `refs/parents/<file>.png`. A parent anchor is never attached to a
page — only the approved sheet built from it is.

**Why every returning character gets a fresh continuity sheet.** The page tools
accept inputs only from `refs/approved/` (`tools/verify.py`), the reference
driver locks a sheet only through a fresh critic verdict on a generated
candidate, and no tool promotes a parent file as-is. Each parent sheet also
carries a view (d) that is wrong for this book: Volume II's `10-wukong` (d) is
the released state with no band (the band is on every page here); `08-wujing`
wears the nine skulls (gone, and blocking); `02-sanzang` (d) leads the bay
horse (gone). So each returning character is re-locked from its parent with
views (a)–(c) copied and a new view (d) for the state this book needs. A
continuity pass, never a redesign. Returning sheets keep their Volume II
numbers; new sheets number from 11.

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| 10 wukong | `refs/parents/10-wukong.png` (the banded pilgrim, the whole locked identity, ears included) and `refs/parents/v1-09-wukong-tempered.png` (the gold eyes with the thin red ring) | **none** — views (a)–(c) are Volume II's banded pilgrim unchanged; view (d) at home with the crown of flowers and leaves sitting over the band. Ears copied from the attached sheet as they are; never reshaped, never "rounded" |
| 02 sanzang | `refs/parents/02-sanzang.png` | **none** — views (a)–(c) unchanged; view (d) saying the words |
| 07 bajie | `refs/parents/07-bajie.png` | **none** — view (d) flying on his small lumpy sagging cloud |
| 08 wujing | `refs/parents/08-wujing.png` | **the skulls are gone** — the same face, build and costume with no necklace, no cord, no skull anywhere; habitual gesture becomes a hand closed at the bare chest where they hung; view (d) bound with rope, head bowed |
| 06 white-horse | `refs/parents/06-white-horse.png` | **none** — view (d) the wounded right foreleg, hoof lifted |
| 05 dragon | `refs/parents/05-dragon.png` | **none** — view (d) recoiling in the air with the clean dark cut on the right foreleg |
| set-flower-fruit | `refs/parents/v1-set-peak.png`, `refs/parents/v1-set-cave.png` | five hundred years on: the same peak, waterfall and cave; the Volume I red banner now a faded pink rag on the old flagpole |
| adversarial-bone-lady-guanyin | `refs/parents/03-guanyin.png` | critic-only comparison: Guanyin is named once and never drawn in this book; the reader remembers "the lady in white" |

Every other sheet is **new** and has no parent anchor.

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
named. **Boards are critic-only rasters and never generation inputs** — their
file names carry `board`, `adversarial`, `silhouette` or `live-pair` so the
tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 10 | `10-wukong` — continuity: the banded pilgrim of Volume II in views (a)–(c); view (d) at home, the flower crown over the band | character | 1 | p1 | `../parents/10-wukong` `../parents/v1-09-wukong-tempered` |
| 02 | `02-sanzang` — continuity: saffron robe, red kasaya, ringed staff, hat on his back; view (d) saying the words | character | 1 | p1 | `../parents/02-sanzang` |
| 07 | `07-bajie` — continuity: pig head, belly, black tunic, rake; view (d) flying on his lumpy cloud | character | 1 | p1 | `../parents/07-bajie` |
| 08 | `08-wujing` — continuity WITHOUT the skulls: gaunt slate ogre, red beard, crescent spade; view (d) bound with rope, head bowed | character | 1 | p1 | `../parents/08-wujing` |
| 06 | `06-white-horse` — continuity: the Third Prince as a horse, saddled; view (d) the wounded right foreleg, hoof lifted | character | 1 | p1 | `../parents/06-white-horse` |
| 05 | `05-dragon` — continuity: the slim white serpent dragon; view (d) recoiling with the clean cut on the right foreleg | character (state) | 30 | p30 | `../parents/05-dragon` |
| 11 | `11-bone-lady` — the White Bone Lady, true shape: skull face, loose black hair, ash-gray and violet burial silk; view (d) the mist escaping | character | 2 | p2 | new |
| 12 | `12-bone-girl` — disguise one: the girl, peach-pink jacket, single plait with a red string, lidded basket, green pinpoints in the eyes; view (d) as Wukong sees her | character (state) | 4 | p4 | `11-bone-lady` |
| 13 | `13-bone-old-woman` — disguise two: the old woman, white bun, dark brown padded jacket, bamboo cane, green pinpoints; view (d) as Wukong sees her | character (state) | 9 | p9 | `11-bone-lady` |
| 14 | `14-bone-old-man` — disguise three: the old man, bald with white fringe and long wispy white beard, gray lay-pilgrim gown, brown prayer beads, green pinpoints; view (d) as Wukong sees him | character (state) | 13 | p13 | `11-bone-lady` |
| 15 | `15-yellow-robe` — huge indigo-faced demon, tusks, black topknot, mustard-ochre robe with silver stars over black armour, scimitar; view (d) the star-light through the cracks | character | 24 | p24 | new |
| 16 | `16-sanzang-tiger` — the monk as a tiger: lean orange tiger, the torn red kasaya with the gold grid knotted at the throat, the monk's dark almond eyes, sitting upright with paws together | character (state) | 28 | p28 | `02-sanzang` |
| 09 | `09-monkeys` — ensemble lock: five young brown bare monkeys of Flower-Fruit Mountain, individually repeatable; no clothing, no gold | character | 20 | p20 | new |
| — | `board-heads` — all faces, same light, same angle | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — assembled automatically by the driver's crop-and-place step; NOT the silhouette test (method/07: it carried scenery fragments twice); the gate judges silhouettes on the two generated boards below and treats this one as superseded | board | — | — | crop-and-place from approved sheets |
| — | `adversarial-silhouettes-a` — Wukong, Sanzang, Bajie, Wujing, the Yellow Robe: isolated full bodies, a solid binary silhouette row and a matched grayscale row | board | — | — | `10-wukong` `02-sanzang` `07-bajie` `08-wujing` `15-yellow-robe` |
| — | `adversarial-silhouettes-b` — Sanzang, the White Bone Lady, the girl, the old woman, the old man: isolated full bodies, a solid binary silhouette row and a matched grayscale row | board | — | — | `02-sanzang` `11-bone-lady` `12-bone-girl` `13-bone-old-woman` `14-bone-old-man` |
| — | `adversarial-wujing-yellow-robe` — the highest-risk pair: both blue-skinned monsters side by side, color and grayscale, heads and profiles | board | — | — | `08-wujing` `15-yellow-robe` |
| — | `adversarial-sanzang-yellow-robe` — the two yellows: the monk and the demon at true relative scale, color and grayscale | board | — | — | `02-sanzang` `15-yellow-robe` |
| — | `adversarial-bone-lady-guanyin` — the bone lady against the remembered lady in white, same light, three-quarter and profile, then grayscale | board | — | — | `11-bone-lady` `../parents/03-guanyin` |
| — | `adversarial-disguises` — the girl, the old woman and the old man side by side, with the monk at the end of the row: three different people, and the old pilgrim never the monk | board | — | — | `12-bone-girl` `13-bone-old-woman` `14-bone-old-man` `02-sanzang` |
| — | `live-pair-wukong-sanzang` — unlettered, page scale, the p13 staging: Wukong asks first, the monk says no | board | — | — | `10-wukong` `02-sanzang` |
| — | `set-ridge` — White Tiger Ridge: chalk-white rock, bleached grass, dead pines, the pale road, the crag with its cave-mouth; midday and long amber afternoon | set | 1 | p1 | — |
| — | `set-flower-fruit` — Volume I's peak and Water Curtain Cave five hundred years on; the faded pink banner rag; orange western evening | set | 19 | p19 | `../parents/v1-set-peak` `../parents/v1-set-cave` |
| — | `set-pagoda-exterior` — black-green pine wood, the tall tiered gold-roofed pagoda, the black-iron gate, the stony stream | set | 23 | p23 | — |
| — | `set-pagoda-hall` — the black stone hall: iron lamps, the stone bed heaped with furs, the thick black pillar, the empty iron cage in a shaft of moonlight | set | 24 | p24 | — |
| — | `set-road-west` — a long road west through green hills into far blue mountains, clean early light | set | 23 | p23 | — |
| — | `obj-basket` — the girl's round lidded bamboo basket: closed; open on rice and noodles; open on pale grubs and green frogs | object | 4 | p4 | — |
| — | `obj-bones` — a neat heap of clean white bones, the skull on top, a smooth carved band across its brow | object | 15 | p15 | — |
| — | `obj-cage-meat` — the iron cage taller than a man, door shut, one plain untouched joint of meat on a bone on its floor | object | 29 | p29 | — |

**Generation order:** `10-wukong` (everyone collides with him, and he is on nearly every page); then the highest-risk lane, `08-wujing` and `15-yellow-robe`; then `02-sanzang`, and `16-sanzang-tiger` from the approved 02; then `11-bone-lady`, and from it `12-bone-girl`, `13-bone-old-woman` and `14-bone-old-man`; then `07-bajie`; then `06-white-horse`, and `05-dragon` from the approved 06; then `09-monkeys`; then boards (the head and silhouette crop-and-place boards are assembled from approved pixels by the driver, not generated); then the generated silhouette boards, the adversarial boards and the live pair; then plates in page order.

## States needed, enumerated from the architecture

| Character | State | Pages |
|---|---|---|
| Wukong | pilgrim, banded: hemp robe, mended left shoulder, tiger-skin kilt below, bare feet, the gold band; needle behind the right ear or the staff | 1–19, 35–48 |
| Wukong | at home: the same, with a crown of flowers and leaves sitting over the band, the band showing beneath | 21, 35–37 |
| Wukong | the sight: the red rings flaring (an effect on the face of sheet 10, drawn from words; the true shape showing through is locked as view (d) of 12, 13, 14) | 5, 9, 14, 36, 42 |
| Wukong | the three copies: identical to sheet 10 (prompt-only) | 18 |
| Sanzang | walking with the ringed staff, hat on his back; riding the white horse; saying the words; kneeling | 1–25, 45–48 |
| Sanzang | the tiger: torn red kasaya knotted at the throat, dark almond eyes, sitting upright paws together; turning his face from the meat | 28–29, 44–45 |
| Bajie | with the luggage pole; whining; asleep; fleeing; flying on his lumpy cloud; confessing | 1–48 |
| Wujing | no skulls; at the monk's back with the pole end; fighting; bound with rope at the pillar; cut free | 1–28, 44–48 |
| Third Prince | horse form, saddled | 1–30 |
| Third Prince | dragon form; cut across the right foreleg | 30–31 |
| Third Prince | horse form, wounded right foreleg, hoof lifted; lying in the stream | 32–33, 44–48 |
| White Bone Lady | true shape on her crag; the mist escaping a fallen disguise | 2, 4–6, 10, 15 |
| White Bone Lady | the girl with the basket; seen through | 4–6 |
| White Bone Lady | the old woman with the cane; seen through | 9–10 |
| White Bone Lady | the old man with the beads; seen through | 13–15 |
| Yellow Robe | asleep on the stone bed; laughing; fighting; the water spell; the star light through the cracks; rising as a star | 24–31, 40–43 |
| Monkeys | pouring out of the cave; crowding the throne; one tugging at the robe; dragging the pig in | 20–22, 35, 38 |

## Nearest lookalikes and what carries the separation

Carried from `04-CHARACTER-LEDGER.md`; the sheet prompt for each names its
lookalike and the differentiators that must survive grayscale and thumbnail.

| Sheet | Never confused with | Carried by |
|---|---|---|
| 10 Wukong | 07 Bajie; 09 the monkeys | small wiry gold monkey vs huge round pink-gray pig; short muzzle vs long snout and floppy ears; hemp robe vs black tunic. Vs the monkeys: golden fur, the band, the robe, the swept golden ruff and the red-ringed gold eyes vs brown, bare, young, no ruff, dark eyes |
| 02 Sanzang | 15 Yellow Robe; 14 the old man | middle height vs half again as tall; bare shaven dome vs black topknot; fair, smooth, gentle vs indigo and tusked; saffron under red kasaya vs mustard-ochre over black armour; ringed staff vs scimitar. Vs the old man: twenty-five vs eighty, fully shaven and smooth vs bald with a white fringe and a long white beard, upright vs thin and bent, saffron and red vs plain gray, ringed staff vs brown beads |
| 16 Sanzang as tiger | any ordinary tiger | the torn red kasaya with the gold grid knotted at the throat; the monk's calm dark almond eyes, never tiger-yellow; upright sitting, paws together; never snarling |
| 07 Bajie | 08 Wujing; 10 Wukong | pig head vs ogre face; round vs gaunt; pink-gray vs slate; black bristle vs wild red; black tunic vs sand-brown; rake vs crescent spade |
| 08 Wujing | 15 Yellow Robe (highest); 07 Bajie | gaunt and hunched vs huge and planted; long hollow face vs wide square face with tusks; slate blue-gray vs deep indigo; wild red hair and red beard vs black topknot and short black beard; red-brown eyes vs pale silver; sand-brown sleeveless tunic vs mustard-ochre robe over black armour; crescent spade vs scimitar; no skulls |
| 15 Yellow Robe | 08 Wujing; 02 Sanzang | as above, inverted |
| 05 / 06 Third Prince | each other only (continuity) | the sea-green eyes and pale-blue mane carry both forms; the wound on the right foreleg in both |
| 11 White Bone Lady | Guanyin (memory, `03-guanyin`) | a white skull face vs a woman's face with a red dot; loose black hair, no hood vs a white hood-veil and gold crown; tattered ash-gray and faded violet silk vs pure white robes; floating trailing hem vs a cloud; bone hands vs willow and vase; no gold |
| 12 / 13 / 14 the disguises | each other; 02 Sanzang | young woman vs old woman vs old man; black plait with a red string vs white bun with a wooden pin vs bald with a white fringe and long white beard; peach-pink vs dark brown vs gray; basket vs cane vs prayer beads. The girl's peach-pink is never saffron; the old man's gray gown is never a monk's robe and he is never fully shaven |
| 09 the monkeys | 10 Wukong | brown, bare, young, no clothing, no band, no gold, no swept golden ruff |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast. The monkeys of Flower-Fruit Mountain (five pages) are locked
  as an ensemble on `09-monkeys` and have no balloons.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown. `03-guanyin` is
  attached only to the critic-only board `adversarial-bone-lady-guanyin`.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`). Every monkey but Wukong is brown, bare and
  young. No other monk, no other tiger, no other lady in gray and violet, and
  no figure in peach-pink, mustard-ochre, saffron, or the gold band appears.
  The reserved colours — Wukong's gold, the monk's saffron and red, the girl's
  peach-pink, the Yellow Robe's mustard-ochre — never land on an extra or on a
  plate (method/07, the reserved colour on an extra).
- Reserved stacks (mirrored in the ledger): golden fur + gold band + hemp robe
  → Wukong; shaven head + saffron robe + red kasaya + ringed staff → Sanzang;
  tiger + torn red kasaya with gold grid + dark almond eyes → Sanzang as the
  tiger; pig head + belly + black tunic + rake → Bajie; blue-gray skin + red
  beard + crescent spade → Wujing; white horse or white serpent + pale-blue
  mane + sea-green eyes → the Third Prince; white skull face + long black hair
  + ash-gray and violet burial silk → the White Bone Lady; peach-pink jacket +
  single plait with red string + lidded bamboo basket → the girl; white bun +
  brown padded jacket + bamboo cane → the old woman; white beard + gray pilgrim
  gown + brown prayer beads → the old man; indigo face + tusks + black topknot
  + mustard-ochre robe with silver stars + scimitar → the Yellow Robe.
- A rejected sheet never becomes a lock and never becomes an input.
- The gold band is a thin flush plain band, the same gold as the staff's caps,
  never a crown, never jeweled, never wider than a finger, never absent from
  Wukong. Under the flower crown it still shows.
- **Wujing carries no skulls.** A skull, a cord, or a necklace on Wujing is
  blocking on every sheet, board and page.
- **No counted object above five** is drawn on any sheet or plate (method/07).
  The peaches are four and never counted in text; the frogs in the basket are
  three; the monkeys' ensemble is five; the bones are a heap, never counted.
- **No blood, guts, or rotting flesh** on any sheet or plate. The fallen
  disguises are hollow dry skins drawn on the pages from words, face-down,
  never a face shown.
- The staff's lock is the staff in hand and the needle behind the right ear on
  `10-wukong`. The monk's ringed staff, Wujing's crescent spade, and the
  Yellow Robe's scimitar never read as it.
- Every sheet prompt names the positive lock and the nearest forbidden
  lookalike; every plate names the location it must never resemble.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas: **(a)** three-
quarter head and shoulders, neutral expression, even light; **(b)** full-length
standing figure, default costume, habitual posture; **(c)** strict profile, same
light; **(d)** the one state the script actually needs.

## 10 — WUKONG (continuity sheet, anchored on Volume II's approved 10 and Volume I's tempered sheet)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume II Wukong sheet and the
approved Volume I tempered sheet. This is the same monkey as the Volume II
sheet, some months later, unchanged: copy his face, his ears, his swept golden
ruff, his band, his hemp robe and his staff exactly as they are drawn there.
The gold eyes with the thin red ring are the ones on the tempered sheet. Do
not redesign, refine, or reshape anything; this is a continuity pass.

Sun Wukong, the Monkey King, is unmistakably a monkey, not a man. His face is
short and heart-shaped, with a pale hairless muzzle and pale cheek field, a
wide mouth, a low brow, and large round gold eyes set wide, each iris circled
by one thin red ring of fire. His ears are exactly the ears on the attached
Volume II sheet: two small upright monkey ears at the sides of the head,
cupped, the same in every view; never long, never narrow and sharp-tipped like
an elf's or a fox's, never floppy. Around the pale face, one swept-back crown
and rear ruff of separated golden fur tufts, longest behind the ears,
continuous with the cheek ruff; monkey fur, not human hair.

Across his brow, in all four views, a thin plain gold band, just above the eyes
and below the fur of the crown, flush to the fur, no wider than a finger, the
same gold as the staff's end caps, no jewels, no pattern, never a crown shape.
It sits in front of the ears and never touches or covers them.

His body is small and wiry, a head shorter than any human, with long arms and a
long tail fully visible in every full-body view. His posture is always active
and asymmetrical: one foot raised, a crouch, or a forward pitch, never both
feet planted. His habitual gesture is a flat hand shading his eyes to look into
the distance. At rest he looks ready to laugh.

He wears a plain undyed hemp travelling robe to the knee, cord belt, sleeves
rolled to the elbow, and one neat mended patch at the left shoulder, over the
tiger-skin kilt; his feet are bare; no cap, no armor. When the full staff is
absent, one tiny straight red-lacquer-and-gold needle lies flat in the fur just
behind his right ear, parallel to the skull, one capped tip showing as a single
small red-and-gold tick; it never reads as part of the ear or as a horn. The
full staff is a straight constant-diameter red-lacquered iron cylinder, taller
than Wukong, with blunt gold end caps and tight flush gold bands only beside
the caps; no mid-shaft collar, ring, taper, point, blade, ringed head, or rake
teeth.

View (a): three-quarter head and shoulders from his right side in even light:
the gold band, the right ear exactly as on the attached sheet, both gold eyes
with their red rings, the swept golden ruff, the needle tick.
View (b): full length in the pilgrim robe, holding the full staff, one foot on
a low stone, the other hand shading his eyes; the left-shoulder patch and the
entire tail; no needle in this view.
View (c): strict ninety-degree right-side profile, facing left, one foot on a
low stone, torso pitched forward, the whole tail; the band circling the skull
in front of the ear; one tiny needle tick behind that ear. The left-shoulder
patch is hidden in this view.
View (d): at home, sitting sideways on a rough stone seat with one foot drawn
up, grinning, the staff leaning beside him: the same robe, the same band, and
on top of the band a loose crown of fresh green leaves and small pink and white
flowers, sitting high on the fur so the gold band shows clearly beneath it all
the way round the brow.

Wukong must remain distinct from Bajie at page scale and in grayscale: small,
wiry, golden, short-muzzled, cupped-eared, long-tailed, active, and
light-robed, never huge, round, pink-gray, long-snouted, floppy-eared, slow, or
in a black tunic. He must remain distinct from the brown monkeys of his
mountain: golden fur, the band, the robe and the red-ringed gold eyes are his
alone. Never a human face, gray or silver fur, a stooped back, a monk's shaven
head, saffron robe, or red kasaya; never long, sharp-tipped, elf-like or floppy
ears; never without the band.

Model form with broad visible brush-and-ink contours and flat mineral-pigment
washes that pool on toothed paper. No parallel or crossed hatch marks.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — SANZANG (continuity sheet, anchored on Volume II's approved 02)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved Volume II sheet: this is the same young monk, unchanged.
Copy his face, head, robe, kasaya and staff exactly as they are drawn there.

Tang Sanzang, a young monk of about twenty-five. Slender, upright, of middle
height. A long oval face, smooth and beardless; a high round fully shaven head
with no hair and no topknot; straight dark brows; calm dark almond eyes; a
straight nose; a small closed mouth; fair skin. Stands straight with his weight
even. Habitual gesture: palms pressed together under his chin. Expression at
rest: polite, a little anxious, determined.

Costume: a saffron-yellow travelling robe to the ankles, under a red kasaya
with a gold-thread grid draped over the left shoulder; straw sandals; a broad
round straw hat hanging on his back by its cord. The monk's staff: a dark
wooden staff as tall as he is, topped with a pewter loop carrying six small
rings.

Views: (a) three-quarter head and shoulders, palms together under the chin;
(b) full length walking with the ringed staff; (c) strict profile showing the
round shaven skull and the hat on his back; (d) full length, standing, saying
the words: the staff leaning in the crook of his arm, palms pressed hard
together at his chest, eyes shut tight, lips moving, his whole face pained.

Sanzang must never be confused with the Yellow Robe demon: a slender man of
middle height against a huge broad demon; a bare shaven dome against a black
topknot; a fair, smooth, gentle face against an indigo face with tusks; a
saffron robe under a red kasaya against a mustard-ochre robe over black armour;
a ringed staff against a scimitar. He must never be confused with an old lay
pilgrim: young, upright, fully shaven and smooth, never a white beard, never a
fringe of hair, never prayer beads in place of the staff. No beard, no hair, no
halo, no crown, no weapon, never mustard-ochre.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — BAJIE (continuity sheet, anchored on Volume II's approved 07)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved Volume II sheet: this is the same pig, unchanged. Copy his
head, body, tunic and rake exactly as they are drawn there.

Zhu Bajie, a pig-headed man, big and round, about thirty-five. A pig's head: a
long snout with a wide pink-gray nose disc, two small lower tusks, enormous
floppy ears hanging to his jaw, small black eyes, bristly black hair on a
pink-gray hide. A huge round belly, short thick legs, broad sloping shoulders;
a head taller than a man and twice as wide. Slouches with his belly forward.
Habitual gesture: patting his belly, or fanning himself with one ear.
Expression at rest: hopeful, greedy, a little hurt.

Costume: a black cotton tunic open over the belly, a blue sash, black trousers.
His weapon: a nine-toothed iron rake on a long wooden shaft.

Views: (a) three-quarter head and shoulders, one ear lifted; (b) full length
with the rake on his shoulder, belly forward; (c) strict profile showing the
long snout and the hanging ear; (d) flying: sitting heavily on a small, lumpy,
gray-white cloud that sags under his weight, the rake held across his knees,
ears blown back, mouth open, clutching the cloud's edge, plainly hating it.

Bajie must never be confused with Wujing the river ogre: a pig's head with
floppy ears against a gaunt ogre face; round and soft against bony and long;
pink-gray against slate blue-gray; black bristle against wild red hair and
beard; a black tunic against sand-brown; a rake against a crescent spade.
Never fur, never a tail in frame, never a monkey's muzzle, never gold.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — WUJING (continuity sheet, anchored on Volume II's approved 08, the skulls removed)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Remove the entire landscape field and all scenic rocks, water, mountains, and
vegetation; place the same four isolated views on one uninterrupted plain
warm-paper ground, with at most neutral contact shadows beneath the full
figures.
Attach the approved Volume II sheet: this is the same river ogre, with one
change. His face, hair, beard, build, tunic, sash and crescent spade are
exactly as drawn there. **The necklace of skulls is gone**: no skulls, no
cord, no necklace, nothing hanging at his neck or chest in any view. His bare
upper chest above the tunic shows plainly where it used to hang.

Sha Wujing, a river ogre who looks about forty-five. He is a head taller than a
big man but only half as wide: tall and gaunt, bony and long-limbed, with long
arms and a forward hunch from the shoulders. His slate blue-gray face is long
and hollow-cheeked, with deep-set round red-brown eyes under a heavy brow, a
short broad flat nose with a wide bridge and level blunt end, and a wide grim
mouth. Wild bristling red hair and a wild red beard frame the face.
Redesign the nose in all four views by shortening its projection, broadening
the bridge and base, flattening the ridge, and terminating the profile in a
level blunt plane with no downward hook; keep the long face and heavy brow
unchanged.
Expression at rest: grim, ashamed, honest. Habitual gesture: one hand closed
at his bare chest where the skulls used to hang, as if counting.

He wears a dark sand-brown sleeveless tunic, a dry river-reed sash in tan,
ochre and muted brown, and has bare arms and feet. His weapon is a long staff
with a flat crescent-moon blade at one end and a small spade at the other.

Views: (a) three-quarter head and shoulders, one hand closed at his bare
chest; (b) full length, hunched forward, holding the crescent spade upright in
both hands; (c) strict profile showing the long face, heavy brow, short broad
blunt nose, beard mass and shoulder hunch; (d) sitting on the ground bound with
plain rope wound round his chest and arms, head bowed, eyes open and grim, the
spade gone; the rope is plain hemp, no wound, no blood.

Wujing must never be confused with the Yellow Robe demon: gaunt, bony and
hunched against huge, broad and planted; a long hollow-cheeked face against a
wide square face with tusks; slate blue-gray skin against deep indigo; wild red
hair and a red beard against a black topknot and short black beard; red-brown
eyes against pale silver; a sand-brown sleeveless tunic against a mustard-ochre
robe over black armour; a crescent spade against a scimitar. Never confused
with Bajie: no pig's head, ears or belly, no rake, no black clothes. Never a
skull anywhere on him, never a long or hooked nose, never scales or antlers,
never blood.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — THE WHITE HORSE (continuity sheet, anchored on Volume II's approved 06)

A character reference sheet, 1536 × 1024 landscape, four views of the same
animal on one uninterrupted warm-paper ground, with no lettering, labels,
frames, panels, scenery or ground line. Attach the approved Volume II sheet as
the identity anchor. This is the same young Third Prince: a slim, fine-boned
horse, white as river foam, with a long narrow equine head, large round
sea-green eyes, a flowing pale-blue mane and tail, and a calm watchful bearing.
He wears the monk's dark-red leather saddle with brass fittings and a plain
bridle.

Show (a) a neutral three-quarter head and neck with the sea-green eye clear;
(b) the full-length saddled horse standing with all four hooves planted; (c) a
strict full-body profile; and (d) the injured state from the horse's right side,
right flank toward the viewer and head facing left across the sheet, head low,
with only the nearer anatomical right foreleg lifted. View (d) carries no drawn
gash, line, ring, wrap or bandage: the right-side pose and lifted right hoof are
the reusable reference lock; the fresh gash and the last-page bandage are drawn
from words on their story pages.

Keep the coat white, the mane and tail pale blue, and the eyes sea green. Never
brown or dappled, never dark-eyed or dark-maned. No antlers, horns, human
features, rearing, blood, open flesh or dangling material.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — THE WHITE DRAGON (continuity sheet, anchored on Volume II's approved 05)

A character reference sheet, 1536 × 1024 landscape, with exactly four cleanly
separated views of the same young dragon on one uninterrupted warm-paper
field. No lettering, labels, frames, scenery, ground line, or props. Use the
attached Volume II `05-dragon` only for the white serpent body, sea-green eyes,
pale-blue mane, and youthful identity; the head lock below is definitive.

The Third Prince is a slim white serpentine dragon, long and lithe, with a
complete tapering tail and four small clawed legs. Give him a compact young
lizard head with a blunt wedge silhouette and almost no projecting muzzle.
One broad shield-shaped nasal scale fills the nose and carries a small slit
nostril on its side. The face also has large round sea-green eyes, two compact
straight unbranched pale-gold horn spikes, a short reptilian mouth, a clean
jaw with no beard or fins, and a pale-blue mane beginning at the crown and
running along the spine. He looks quick, brave, and a little frightened. He
wears no costume or tack.

Show (a) the three-quarter head and neck, (b) the complete dragon in one long
readable S-curve, (c) the strict-profile head, and (d) the complete dragon
recoiling in startled pain. In view (d), show his anatomical right side and
lift that right foreleg alone clear of the chest. Across the front of that
foreleg, midway between elbow and claws, place one bold charcoal-dark diagonal
slash, large enough to read at proof scale but ending inside the white limb.

Never draw a long horse-like rostrum, rounded fleshy muzzle, terminal horse
nostril, horse anatomy, hooves, or tack. Never draw a second wound mark, red,
blood, open flesh, bandage, wrap, ring, or dangling material. Never draw
antlers, whiskers, a fin beard, blue-green scales, gold eyes, robes, a crown,
or a human body.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 11 — THE WHITE BONE LADY (true shape)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

The White Bone Lady, an ancient demon: a tall, gaunt lady made of bone, taller
than a man, very thin. Her face is a smooth, clean white skull with a lady's
high cheekbones and a long narrow jaw; deep dark eye-hollows, and in each
hollow one small pinpoint of cold green light; no lips, the teeth showing in a
fixed polite smile; no nose but the skull's narrow opening. Long straight black
hair hangs loose from the crown of the white skull to her waist, with no hood,
no veil and no ornament. A long thin neck. Long white bone hands with fingers
long and thin as knitting needles. She is wrapped in layered, tattered burial
silks of ash-gray and faded violet that trail like smoke at the hem, so she
seems to float a little above the ground. Habitual gesture: one long bone
finger drawn slowly across her teeth. Expression: patient, hungry, amused.

Views: (a) three-quarter head and shoulders, one bone finger at her teeth, the
green pinpoints clear in both eye-hollows; (b) full length, floating just above
a low white rock, the silks trailing; (c) strict profile showing the long skull,
the long jaw and the black hair falling straight down her back; (d) her escape:
a thin cold white mist streaming sideways out of the frame from a low point
near the ground, and her skull face just visible inside the mist, stretched
thin, the green pinpoints the brightest thing in it; no body, no silks in this
view, nothing fallen shown.

The White Bone Lady must never be confused with the gentle Bodhisattva in
white whom the reader remembers: a white skull, never a woman's living face;
loose black hair, never a white hood-veil, never a crown; tattered ash-gray and
faded violet silk, never pure white robes; floating trailing silk, never a
cloud; bone hands, never a willow sprig or a vase; no gold anywhere, no red dot
between the brows. Never blood, guts, rotting flesh, or exposed organs: she is
clean dry bone. Never saffron, never red.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 12 — THE GIRL (disguise one, state sheet anchored on approved 11)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved sheet of the bone lady. Views (a), (b) and (c) are a wholly
living young woman with nothing of the skull in her face or hands — the only
trace of the bone lady is the two small pinpoints of cold green light in the
centres of her dark eyes. View (d) alone shows what lies under the face.

A pretty young village woman of about eighteen. A round soft face, rosy
cheeks, straight dark brows, dark eyes each with a faint pinpoint of cold green
at the centre, a small smiling mouth, light-brown skin. Black hair in one long
plait brought forward over her right shoulder, tied at the end with a short red
string. Slight, of small height. She smiles a great deal. Habitual gesture: the
basket held forward on her arm, as if offering it.

Costume: a peach-pink cotton jacket with a high collar, dark blue trousers,
cloth shoes. On her left arm a round lidded bamboo basket with a bamboo hoop
handle, the lid closed. No jewelry, no gold anywhere.

Views: (a) three-quarter head and shoulders, smiling, the green pinpoints
clear; (b) full length, holding the basket forward; (c) strict profile showing
the plait and the red string; (d) as the monkey sees her: the same girl in the
same pose as (a), and through her face and her hand on the basket a pale,
translucent ghost of the attached bone lady's skull face and long bone fingers
showing, like a figure seen through thin paper; her black hair, jacket and
basket unchanged.

The girl must never be confused with the monk: her jacket is peach-pink, never
saffron-yellow; no kasaya, no shaven head. She must never be confused with the
old woman or the old man: young, black-haired, plaited, peach-pink, carrying a
basket. Never gold, never white robes, never a veil, never blood.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 13 — THE OLD WOMAN (disguise two, state sheet anchored on approved 11)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one uninterrupted plain warm-paper ground, with no scenery, border,
lettering or labels. Attach the approved Bone Lady only as the shape reference
for the supernatural shadow in view (d), never as a separate figure.

The figure is a wholly living village woman of about eighty, small and shorter
than the girl, with a strongly bent back and rounded shoulders. Her face is
short and broad, almost round: wide full cheeks, a short lower face, a small
low rounded nose, a blunt rounded chin, deep wrinkles, a sorrowful brow and a
small toothless mouth. Keep this same compact face in both three-quarter views
and in strict profile. Her narrow dark eyes hold exactly one tiny cold-green
pinpoint at the centre of each eye. Her white hair is pulled into a tight bun
secured by one plain wooden pin. She weeps and pleads, leaning her weight on a
plain shoulder-high bamboo cane. When she wipes a tear, her bare fingers touch
her cheek.

Costume: a dark brown padded cotton jacket ending at the hips, darker brown
trousers and plain cloth shoes. No jewellery and no carried object except the
cane.

Views: (a) three-quarter head and shoulders, weeping, bare fingertips at one
cheek; (b) full length, bent over the cane; (c) strict profile, clearly showing
the short broad face, low rounded nose, blunt chin, bent back, tight bun and
wooden pin; (d) a second three-quarter head-and-shoulders view of the same
wholly living, opaque old woman as Wukong sees her. Immediately behind view
(d), place one flat, low-contrast pale-gray head-and-shoulders shadow. Its head
alone has the approved Bone Lady's long-jawed skull silhouette; its shoulders
simply echo the old woman's jacket. The shadow is a graphic sign, not another
body and not a transparent layer inside her face. Its eye hollows are unlit.
The only green on the entire sheet is the same two tiny pinpoints in the old
woman's living eyes. Exactly four depictions total; no separate Bone Lady,
skeletal body, bone hands or additional skull anywhere.

**Relock ruling (2026-10-16, after six candidates):** the lock for `13-bone-old-woman` is views (a)–(c), the living disguise. View (d), the reveal, is out of scope and is never a reference for any page: pages draw Wukong's view of the skull from `11-bone-lady` and words. A fifth figure or a reveal artifact confined to view (d) is nonblocking on this sheet.

Keep her unmistakable from the other disguises: elderly woman, short broad
wrinkled face, white bun, compact bent silhouette, dark-brown clothes and cane;
never the girl's black plait, peach jacket or basket, and never the old man's
bald head, beard, gray gown or prayer beads. Never gold, white robes, veil,
saffron, red kasaya, blood or a handkerchief. Never place a skull inside or
over her living face.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 14 — THE OLD MAN (disguise three, state sheet anchored on approved 11)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved sheet of the bone lady. Views (a), (b) and (c) are a wholly
living old man with nothing of the skull in his face or hands — the only trace
of the bone lady is the two small pinpoints of cold green light in the centres
of his eyes. View (d) alone shows what lies under the face.

A thin old man of about eighty, a little stooped, of middle height. A long,
lined, sun-browned face; a bald brown head with a ring of white hair at the
sides and back; a long wispy white beard falling to his chest and thin white
eyebrows; narrow dark eyes each with a faint pinpoint of cold green at the
centre; lips always moving in prayer. Habitual gesture: a string of brown
wooden prayer beads passing through both hands at his chest. Expression:
mild, murmuring, a little too eager.

Costume: a plain gray lay-pilgrim's gown to the shins with a darker gray sash,
cloth shoes, a cloth bundle on his back. No staff.

Views: (a) three-quarter head and shoulders, the beads at his chest, the green
pinpoints clear; (b) full length, stooped a little, the beads in both hands;
(c) strict profile showing the bald crown, the white fringe and the long beard;
(d) as the monkey sees him: reuse view (a)'s three-quarter pose; keep the
complete long, lined, sun-browned living face and both flesh hands visibly
present; align one pale, low-contrast translucent long-jawed skull ghost within
the face and translucent long bone-finger ghosts within the hands, as if seen
through thin paper; keep the bald crown, white fringe, long wispy beard, gown,
and brown beads unchanged over and around the overlay. No exposed or
replacement skull, no exposed or replacement skeletal hands.

The old man must never be confused with the young monk: eighty, never
twenty-five; a white fringe and a long white beard, never a fully shaven smooth
head and face; a plain gray gown, never saffron, never a red kasaya; prayer
beads, never a ringed staff. Never confused with the old woman or the girl: a
man, bald, bearded, gray, with beads. Never gold, never white robes, never
blood.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 15 — THE YELLOW ROBE

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views, and no scenery.

The Yellow Robe is a huge demon in his prime, half again as tall as a man and
broad as a door, with heavy shoulders, a thick neck and big hands. His deep
indigo-blue face is wide and square, with a heavy jaw, broad flat nose, thick
black brows, two short white tusks rising from the lower lip, and pale silver
eyes with no iris colour, like starlight. His long black hair is pulled into a
high topknot bound with black cord. His short square black beard is a compact
jaw-length block with a broad straight lower edge and squared corners, clearly
separate from the topknot hair. He stands upright with feet planted wide and
chin up. His expression is big, lazy, delighted and cruel.

He wears a long mustard-ochre robe over black lamellar armour, with one simple
small silver star motif repeated along the robe edges; any point count is
acceptable and is not an identity requirement. He has a wide black belt and
black boots. The only weapon anywhere on the sheet is one broad curved
scimitar. The blade remains silver, but the grip and pommel are black or dark
iron and the guard is black, dark iron, or at most a small dark-bronze piece;
no bright-gold surface may remain anywhere on the weapon.

Views: (a) three-quarter head and shoulders, laughing, with both tusks and the
silver eyes clear; (b) full length, feet planted wide, tossing the single
scimitar between his two open hands; (c) strict profile showing the high
topknot, one tusk, the heavy jaw and the compact square beard; (d) standing
with his head thrown back as thin cracks of pure silver light shine through
his indigo face and the seams of his robe, as if a star were inside him.

The Yellow Robe must never be confused with Wujing: huge, broad and planted,
never gaunt, bony or hunched; a wide square tusked face, never long and
hollow-cheeked; deep indigo skin, never slate blue-gray; a black topknot and
compact square black beard, never wild red hair or a long red beard; pale
silver eyes, never red-brown; mustard-ochre over black armour, never a
sand-brown sleeveless tunic; one scimitar, never a crescent spade. He must
never be confused with Sanzang: never saffron-yellow, never a red kasaya,
never a shaven head. Never gold eyes, bright-gold costume ornaments, white
robes, or blood on the blade.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 16 — SANZANG AS THE TIGER (state sheet, anchored on approved 02)

A character reference sheet, 1536 × 1024 landscape, four views of the same
animal on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved sheet of the young monk: this tiger is that monk under a
spell. Two things of the monk survive and carry the identity in every view:
his torn red kasaya, and his calm dark almond eyes.

A lean, long-legged tiger, orange with black stripes, thin from not eating, the
ribs faintly showing. The monk's red kasaya with its gold-thread grid, torn and
ragged, still hangs over the tiger's left shoulder and is knotted at its throat
— the only scrap of the monk left on him. The eyes are the monk's: calm dark
almond human-shaped eyes, dark brown, never a tiger's yellow, never slit
pupils. A tiger's muzzle and body otherwise, never a human face on a tiger's
body. Habitual posture: sitting upright on his haunches with his front paws
placed close together, the nearest a tiger can come to palms pressed together.
Expression: frightened, patient, gentle.

Views: (a) three-quarter head and shoulders, the dark almond eyes and the
kasaya knot at the throat clear; (b) full length sitting upright, front paws
together, the torn kasaya over the left shoulder; (c) strict profile, sitting
upright, the kasaya's gold grid visible on the shoulder; (d) lying down with
his head turned sharply away and lowered, eyes shut, refusing something off
the sheet.

The tiger must never be confused with any ordinary tiger: the torn red kasaya
and the monk's dark almond eyes are always visible. Never snarling, never
baring teeth at anyone, never eating, never bloody, never a human face, never
standing on his hind legs.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 09 — THE MONKEYS OF FLOWER-FRUIT MOUNTAIN (ensemble lock)

A character reference sheet, 1536 × 1024 landscape, on one uninterrupted
plain warm-paper ground, no lettering of any kind, no labels, no borders. No
mountain panorama, rock ledge, dense foliage, or secondary branches; retain
only the peach and one minimal low branch needed to carry the fourth monkey's
hanging posture. Five young monkeys of
Flower-Fruit Mountain standing and crouching in one row, full length, evenly
spaced, each individually repeatable: all brown, all bare, all young; ordinary
small macaques with short brown fur, pinkish-brown faces, small round dark
eyes, short muzzles, small ears, and tails. From left: a lanky young monkey on
all fours, mid-scramble; a plump one sitting with a peach in both hands; a tiny
one standing on its hind legs, one hand reaching up as if to tug at someone's
sleeve; a wiry, narrow-faced one hanging by one arm from a low branch; a
round-faced one crouched, mouth open, chattering. Below the row, the same five as small heads
in three-quarter view, in the same order. In both the fourth monkey's full-body
view and matching lower head, remove the backward-pointing crown wedge and
rear ruff, and replace them with a close, uniformly short brown fur cap that
follows the skull with a compact rounded rear contour. Preserve its narrow
face, small round dark eyes, wiry build, and one-arm hanging posture.

The monkeys must never be confused with the Monkey King: brown, never golden;
no swept golden ruff; dark eyes, never gold with a red ring; no clothing of any
kind, no robe, no kilt, no band, no gold anywhere, no crown, no staff.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board prompts (critic-only rasters, generated from the attached approved sheets)

- **adversarial-silhouettes-a.** The five figures from the attached sheets — the small gold monkey in his hemp robe with his staff, the young shaven monk with his ringed staff, the big pig-headed man with his rake, the gaunt river ogre with his crescent spade and no skulls, the huge indigo-faced demon with his scimitar — isolated full bodies, each complete from head to feet (tail, hands and weapons included), standing at one common true relative scale on one uniform plain light ground, no scenery, no shadow and nothing touching any figure. Top row: the five as true solid black binary silhouettes, filled solid with no interior white marks. Bottom row: the same five, same poses, in matched pure grayscale. No lettering. Each figure exactly as on its sheet. Redraw Wujing's head from the approved sheet: keep the face long and hollow-cheeked, deepen the round eyes beneath one heavy brow ridge, broaden and flatten the nose, and restore the full bristling hair mass and dense long beard silhouette. Preserve the gaunt stoop and crescent weapon exactly; do not solve this with costume or colour. Redraw the head from the approved sheet with a visibly wider square face and heavy jaw, a broad flat nose, thick brows, two short tusks rising clearly from the lower lip, a short square beard, and the high black topknot. Keep the chin-up posture and huge planted build. These face markers must remain readable in grayscale, strict profile, a reaction expression, and a thumbnail crop without armour, robe, or scimitar. Place the corrected Wujing and Yellow Robe in same-panel opposition at matched head scale, including a readable strict-profile comparison. Wujing must retain a long hollow face, heavy brow, broad flat nose, wild outward hair/beard mass, and gaunt forward stoop; the Yellow Robe must retain a wide square tusked face, short square beard, high topknot, thick neck, and planted posture. The separation must survive grayscale and thumbnail reduction without relying on weapon, costume, or skin hue.
- **adversarial-silhouettes-b.** The five figures from the attached sheets — the young shaven monk with his ringed staff, the tall bone lady floating in her trailing silks, the young girl with her basket, the bent old woman with her cane, the thin old man with his prayer beads — isolated full bodies, each complete from head to feet, at one common true relative scale on one uniform plain light ground, no scenery, no shadow and nothing touching any figure. Top row: true solid black binary silhouettes, filled solid with no interior white marks. Bottom row: the same five in matched pure grayscale. No lettering. Each figure exactly as on its sheet; the girl, the old woman and the old man show no ghost of the skull.
- **adversarial-wujing-yellow-robe.** The gaunt slate blue-gray river ogre with the red beard and no skulls, and the huge indigo-faced demon with the tusks and the black topknot, from the attached sheets, standing side by side at true relative scale under the same flat even light, each holding his own weapon, on a plain warm-paper ground: on the left half of the canvas both in full length in color, then both heads in strict profile; on the right half the identical arrangement in pure grayscale. No lettering. Each face must be exactly the face on its sheet.
- **adversarial-sanzang-yellow-robe.** The young shaven monk in saffron and red and the huge indigo-faced demon in mustard-ochre, from the attached sheets, standing side by side at true relative scale (the monk's head at the demon's chest) under the same flat even light, on a plain warm-paper ground: on the left half in color, three-quarter view full length; on the right half the same pair in pure grayscale, and below them both heads in strict profile in grayscale. No lettering. Each face must be exactly the face on its sheet.
- **adversarial-bone-lady-guanyin.** The tall bone lady with the white skull face and loose black hair in ash-gray and violet silk, and the serene woman in white with the hood-veil, from the attached sheets, in one frame under the same flat even light, both in three-quarter head and shoulders on the left half of the canvas and both in strict profile on the right half, side by side at the same distance, plain warm-paper ground, no props in hand, no cloud, no lettering. Then the identical pair repeated small in pure grayscale along the bottom edge. Each face must be exactly the face on its sheet.
- **adversarial-disguises.** Four figures from the attached sheets in one row at true relative scale under the same flat even light on a plain warm-paper ground: the young girl in peach-pink with her basket, the bent old woman in dark brown with her cane, the thin old man in gray with his prayer beads, and at the end of the row the young shaven monk in saffron and red with his ringed staff. Upper half: full length in color, with no ghost of the skull on any of them. Lower half: the same four heads in three-quarter view and the same four in strict profile, in pure grayscale. No lettering. Each face must be exactly the face on its sheet.
- **live-pair-wukong-sanzang.** A single unlettered story-scale image: late amber afternoon on a pale chalk-white ridge road, the small gold monkey from one attached sheet, the gold band on his brow, standing in front of the young monk from the other attached sheet with one hand held out flat toward him, asking, his face serious and not laughing; the monk, palms pressed together at his chest, shaking his head, frightened and firm. Remove the large woven backpack from Sanzang and restore the approved sheet's compact soft gray cloth pilgrim bundle, with an irregular fabric silhouette and no wicker weave, lid, hoop handle, or basket rim. No third figure. No balloons, no captions, no text of any kind. Each face must be exactly the face on its sheet.

## Setting plates and the object plates

Each plate is 1536 × 1024 landscape, architecture and palette only, **no
figures, no lettering**. Register paragraph verbatim. One line each:

- **set-ridge.** Two unframed vignettes on one continuous warm-paper ground, with their outer edges dissolving into that ground and no rule, gutter, frame, or panel boundary; retain the crag-and-cave-mouth silhouette as the primary marker in both light states. Left: a high dry ridge of chalk-white rock and bleached pale grass under hard flat midday light with short shadows, a narrow pale road running along the spine, a few twisted dead gray pines, wide hazy azurite valleys falling away on both sides; above the road, a tall tooth of white rock — the crag — with a dark cave-mouth at its top. Right: the same ridge road further along in long amber late-afternoon light, long shadows across the white rock, the crag small behind. Bone, ash, chalk and hazy blue; no green fields, no water, no buildings, no fruit, no figures, no gold. Never the ochre dust road of the earlier volume or a sand-coloured river plain.
- **set-flower-fruit.** Attach the two approved Volume I plates: the same green peak on the eastern coast and the same Water Curtain Cave. Two unframed vignettes on one continuous warm-paper ground. Left: the peak, wet malachite slopes and peach trees in leaf with a few blossoms, the split stone on the summit, and beside it an old wooden flagpole carrying one small ragged faded pale-pink banner rag stirring in the wind; beyond, an orange evening sky over far western hills. Right: the white waterfall falling across the mouth of the cave, and through it the cave behind with its rough stone seats and a stone throne; wet green, white water, warm light. The rag is faded pale pink, never bright red, never a full banner, no glyphs. No monkeys, no figures. Never the dry white ridge.
- **set-pagoda-exterior.** Redraw the two environmental views as a borderless plate: carry image content continuously to the meeting edge, with no pale strip, rule, frame, seam, or exposed-paper gutter between them. Left: a dark wood of tall black-green pines in deep shadow, and in a clearing a tall tiered pagoda of five to seven storeys whose curved roofs are plated with gold that gleams through the trees, at its base a heavy black-iron double gate, shut; a clear stony stream running past the clearing. The pagoda is a tall tiered tower of five to seven stacked storeys (any count in that range passes; the storey count is not a story object), each storey under its own unmistakable gold curved roof/eave tier, readable in thumbnail and grayscale. Make the gate, hinges, latch, and all gate fittings uniformly matte black iron; reserve every gold accent on the plate for the pagoda roofs. Right: the same stream at dawn at the edge of the wood, shallow clear water over pale stones, a low grassy bank, pine trunks behind. Shift that vignette to cool, pale dawn light; suppress the saturated orange-pink field and warm reflection, and keep the shallow water visibly cold blue-green and transparent over pale stones so the roof gold remains the plate's sole strong warm accent. Black-green, gold on the roofs only, cold clear water; no plaque, no signboard, no glyphs on the gate or the pagoda, no figures. Never a crystal sea palace, never a farmhouse.
- **set-pagoda-hall.** One great dark hall of black stone inside the pagoda, lit by a few small iron lamps with low warm flames: a wide stone bed heaped with dark furs on a low dais; one thick black stone pillar standing free in the hall; against the far wall an iron cage taller than a man, empty, its barred door shut; from a single high narrow window, one shaft of cold white moonlight falling across the floor onto the cage. Black, iron and deep shadow, the lamps the only warm points, the moonlight the only cold one; no gold inside, no meat, no bones, no ropes, no weapons, no glyphs, no figures. Never the sea palace's shell-white columns, never a farmhouse room.
- **set-road-west.** A long dirt road going west through rolling green hills toward far blue mountains, clean early-morning light from behind the viewer, long soft shadows across the road, a line of dark pines falling away at the left edge behind. Malachite and soft azurite, pale gold early light; no milestone, no buildings, no figures, no glyphs. Never the dry white ridge, never the ochre dust valley of the earlier volume.
- **obj-basket.** One borderless, unlettered object plate on uninterrupted warm paper with clear space between three views of the same round lidded bamboo basket with a bamboo hoop handle. Left: the basket closed, the lid on. Centre: the lid lifted and resting against it, the basket full of white rice and pale noodles. Right: the lid off and the same basket full of small pale cream-coloured grubs, drawn simply like grains of rice that have begun to wriggle, and two to four small bright green frogs sitting on top (any count in that range passes), one climbing out over the rim. Woven pale bamboo, white rice, green frogs; nothing rotting, no blood, no slime, no flies, no figures, no hands, no scenery.
- **obj-bones.** One borderless, unlettered object plate on one uninterrupted warm-paper ground: a neat, low, cohesive heap of clean, dry, white bones lying on only a small patch of pale road dust, shaped as one shallow compact oval directly beneath the inscription skull — nest the ribs inward, overlap or roughly align the long bones inside the mound, remove the foreground X, and pull every detached small bone back into the mound so no bone radiates or trails outward, not counted — with one complete white skull only, resting visibly on top at the mound's center, facing the viewer, its brow wide and smooth with one flat, clean, recessed rectangular band running straight across the frontal brow from temple to temple, the band blank and empty, ready to carry an inscription, with no paired wraparound grooves or raised cap-like strip; remove every secondary skull and cranium from the heap; and separately at the right, the same skull alone in three-quarter close-up, reading as a repeat close-up of that same skull, with the same wide, blank, recessed brow band clear across the brow, with no paired wraparound grooves or raised cap-like strip. Restrict the plate to clean bone white, ash shadow, pale road dust, and warm paper; no saturated teal or malachite landscape and no gold foliage. No lake, mountains, cliffs, living pines, foliage, clouds, or any other scenery; no letters, glyphs or marks of any kind in the band or anywhere else, no blood, no flesh, no hair, no cloth, no green light in the eye-hollows, no figures.
- **obj-cage-meat.** One borderless, unlettered isolated object plate on uninterrupted warm-paper ground: one iron cage taller than a man, square, of thick black-iron bars with a barred door, shut, standing on one compact black-stone floor footprint directly beneath the cage; on the cage floor inside, one plain cooked joint of meat on a single bone, brown and dry, whole and untouched, set on the bare stone; a single shaft of cold white moonlight falls through the bars onto the cage and meat as the sole strong light accent. The square cage, its shut barred door, and the single meat joint are the only depicted objects. Every bar, post, crosspiece, hinge, latch, and door plane reads predominantly matte black iron, never ochre or rust-gold; brown is restricted to the cooked meat and, at most, tiny subordinate oxidation freckles. No full-height black-stone walls or chamber architecture, no blood, no raw red flesh, no bones scattered, no animal, no figure, no straw, no scenery beyond the compact floor footprint.


**Relock ruling (2026-10-16, after six candidates):** the dragon locks as Volume II's approved `05-dragon` sheet, unchanged (it passed Volume II's sheet critic and whole-cast gate as this same character). No wound view is required on the sheet: the cut on the right foreleg (pp 31–32) is drawn from words, and `06-white-horse` carries the wound lock. Shared sea-green eyes, pale-blue mane and white value with the horse are the intended cross-form identity, not a collision; the dragon is separated from the horse by the serpent body, four small clawed legs, the two short horns and no tack.
