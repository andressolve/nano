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
glyphs on the seal, the tablet, the painting, or the milestone. Labelled
sheets teach the page model to letter the art.

**Volume palette shift** (`05-SETTINGS-AND-OBJECTS.md`): the road adds ochre,
dust and autumn rust to Volume I's malachite and azurite. The back house is
indigo black with one lantern; the Flowing Sand River is sand-gold and pale
gray with no green and no blue.

## Anchoring (sequels)

Parent anchors live in `refs/parents/`, copied byte-identical from
`../monkey-king-vol1/refs/approved/`. They are attached as image inputs to the
sheet that continues them. `tools/refbrief.py` resolves every anchor name in
the manifest's last column under `refs/approved/`; a parent anchor is
therefore written `../parents/<file>` and resolves to
`refs/parents/<file>.png`. A parent anchor is never attached to a page — only
the approved sheet built from it is.

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| 01 wukong | `refs/parents/09-wukong-tempered.png` (face, gold eyes with the red ring) and `refs/parents/01-wukong.png` (body, tail, posture, staff) | **none** — five hundred years under a mountain change nothing in the face; new costume only (the monk's hemp robe), and view (d) the released state, Volume I's armor gone dull and ragged |
| 04 ao-guang | `refs/parents/06-ao-guang.png` | **none** — continuity pass; view (d) pouring tea |
| set-five-elements | `refs/parents/set-five-elements.png` | spring instead of snow; second view the ridges split open |
| set-sea-palace | `refs/parents/set-sea-palace.png` | the same hall; the treasury's pillar is gone, its socket empty; the painted screen behind the throne |

Every other sheet is **new** and has no anchor.

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
named. **Boards are critic-only rasters and never generation inputs** — their
file names carry `board`, `adversarial`, `silhouette` or `live-pair` so the
tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| — | ~~`01-wukong`~~ — retired 2026-10-15 after six candidates (ears and crown never converged uncapped; v6 failed only on the ear apex in two views); Wukong locks through `10-wukong` | — | — | — | — |
| 02 | `02-sanzang` — saffron robe, red kasaya, ringed staff; view (d) leading the plain bay horse | character | 4 | p4 | new |
| 03 | `03-guanyin` — white hood-veil, willow, vase, on a small cloud | character | 2 | p2 | new |
| 04 | `04-ao-guang` — seated, coral throne; view (d) pouring tea | character | 14 | p14 | `../parents/06-ao-guang` |
| 05 | `05-dragon` — the Third Prince, slim white serpent dragon | character | 24 | p24 | new |
| 06 | `06-white-horse` — the Third Prince as a horse, saddled | character (state) | 28 | p28 | `05-dragon` |
| 07 | `07-bajie` — pig head, belly, black tunic, rake; view (d) with the luggage pole | character | 32 | p32 | new |
| 08 | `08-wujing` — gaunt slate ogre, red beard, nine skulls, crescent spade | character | 41 | p41 | new |
| 09 | `09-old-gao` — small stooped farmer, indigo, lantern | character | 30 | p30 | new |
| 10 | `10-wukong` — primary Wukong lock: pilgrim robe with the thin gold band, views (a)–(c); view (d) released, in the rags of Volume I's armor, no band. Pages 9–19 draw him from this sheet with the band named absent | character | 1 | p1 | `../parents/09-wukong-tempered` `../parents/01-wukong` |
| 12 | `12-wukong-bride` — Wukong in the bride's shape: the Gao daughter's face and green jacket, the gold band at her hairline; and the half-changed state | character (state) | 31 | p31 | `10-wukong` `11-gao-daughter` |
| 11 | `11-gao-daughter` — scenery with a sheet: pale green jacket, two hair loops; no balloons | character | 31 | p31 | new |
| 13 | `13-robbers` — ensemble lock: six ordinary beardless men in rough brown and gray with cloth head-wraps, each individually repeatable, the leader with the chopper | character | 11 | p11 | new |
| — | `board-heads` — all faces, same light, same angle | board | — | — | crop-and-place from approved sheets |
| — | ~~`board-silhouette-grayscale`~~ — superseded 2026-10-15 at the whole-cast gate (crop-and-place kept scenery and mixed thresholds); replaced by the two generated silhouette boards below | — | — | — | — |
| — | `adversarial-silhouettes-a` — Wukong, Sanzang, Guanyin, Old Gao, the Gao daughter: isolated full bodies, solid binary silhouettes and matched grayscale | board | — | — | `10-wukong` `02-sanzang` `03-guanyin` `09-old-gao` `11-gao-daughter` |
| — | `adversarial-silhouettes-b` — Bajie, Wujing, Ao Guang, the dragon, the white horse: isolated full bodies, solid binary silhouettes and matched grayscale | board | — | — | `07-bajie` `08-wujing` `04-ao-guang` `05-dragon` `06-white-horse` |
| — | `adversarial-sanzang-old-gao` — costume-free heads and profiles, reactions, grayscale thumbnails | board | — | — | `02-sanzang` `09-old-gao` |
| — | `adversarial-sanzang-guanyin` — same panel, same light, three-quarter and profile, then grayscale | board | — | — | `02-sanzang` `03-guanyin` |
| — | `adversarial-dragon-ao-guang` — both dragons in one frame | board | — | — | `04-ao-guang` `05-dragon` |
| — | `adversarial-bajie-wujing` — both monsters side by side, color and grayscale | board | — | — | `07-bajie` `08-wujing` |
| — | `live-pair-wukong-sanzang` — unlettered, page scale, the p9 staging | board | — | — | `10-wukong` `02-sanzang` |
| — | `set-five-elements` — the hand-mountain in spring, cleft, seal; second view split open | set | 1 | p1 | `../parents/set-five-elements` |
| — | `set-border-road` — dry valley road west, scrub pine, boulders, white milestone | set | 4 | p4 | — |
| — | `set-sea-palace` — Ao Guang's hall, the painted screen, the empty socket | set | 14 | p14 | `../parents/set-sea-palace` |
| — | `set-south-sea` — jade sea, rocky island, still bamboo | set | 22 | p22 | — |
| — | `set-eagle-grief` — gorge, deep green stream, undercut bank | set | 24 | p24 | — |
| — | `set-gao-farmhouse` — barred gate and courtyard at dusk; the front room with lamps and noodles | set | 30 | p30 | — |
| — | `set-back-house` — the small room at night, curtained bed, window, door locked from outside | set | 31 | p31 | — |
| — | `set-sand-river` — the sand-coloured river, reeds, the blank stone tablet; far bank willows | set | 39 | p39 | — |
| — | `obj-cap-band` — the plain cloth cap with the gold band inside; the band alone | object | 16 | p16 | — |
| — | `obj-painting` — the ink painting: bridge, old man, falling shoe, boy | object | 15 | p15 | — |
| — | ~~`obj-skulls-raft`~~ — retired 2026-10-16: the overloaded two-state plate repeatedly lost the exact count; the open cord lock lives on `08-wujing`, while the story-critical raft continues below | object | — | — | — |
| — | `obj-nine-skull-raft` — exactly nine skulls laid as a low raft of light | object | 46 | p46 | `08-wujing` |

**Generation order:** `10-wukong` (everyone collides with him, and he is on
every page; `01-wukong` is retired, see the manifest); then the highest-risk
lane, `02-sanzang` and `03-guanyin`; then `11-gao-daughter` and
`12-wukong-bride` from the approved 10 and 11; then `07-bajie` and
`08-wujing`; then `05-dragon` and `06-white-horse` from the approved 05; then
`04-ao-guang` and `09-old-gao`; then boards (head and silhouette boards are
crop-and-place from approved pixels, not generations); then adversarial and
live-pair boards; then plates in page order.

## States needed, enumerated from the script

| Character | State | Pages |
|---|---|---|
| Wukong | face in the rock, moss-matted (prompt-only: the face of sheet 01, framed by stone) | 1–6 |
| Wukong | released: dull green-gold armor in rags over the red tunic, tiger-skin kilt, no cap, matted fur | 7–9 |
| Wukong | pilgrim: hemp robe, mended left shoulder, tiger-skin kilt below, bare feet; needle behind right ear or staff | 9–19 |
| Wukong | pilgrim, banded: as above with the thin gold band on the brow | 18–48 (cap over the band pp 18–19) |
| Wukong | as the bride: the Gao daughter's face and jacket, the gold band at the hairline | 31–34 |
| Sanzang | walking with the ringed staff, straw hat on his back; seated; riding | 4–47 |
| Guanyin | on her cloud | 2–3, 16, 22 |
| Ao Guang | seated; pouring tea | 14–15 |
| Third Prince | dragon form | 24–28 |
| Third Prince | horse form, saddled | 28–48 |
| Bajie | courting (red sash); fleeing; kneeling; with luggage pole | 32–48 |
| Wujing | with skulls; kneeling; skulls off, carrying the pole end | 41–48 |
| Old Gao | at the gate with lantern; indoors | 30, 36 |

## Nearest lookalikes and what carries the separation

Carried from `04-CHARACTER-LEDGER.md`; the sheet prompt for each names its
lookalike and the differentiators that must survive grayscale and thumbnail.

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 Wukong | 07 Bajie (both beasts in clothes) | small wiry gold monkey vs huge round pink-gray pig; short muzzle vs long snout and floppy ears; hemp robe vs black tunic |
| 02 Sanzang | 03 Guanyin; 09 Old Gao | bare shaven dome vs white hood-veil; young man vs woman with red dot and red mouth; saffron and red vs white; on the ground vs on a cloud; ringed staff vs willow and vase. Vs Old Gao: 25 vs 65, fully shaven vs bald with fringe and knot, smooth vs moustache, upright vs stooped, saffron vs indigo |
| 03 Guanyin | 02 Sanzang | as above, inverted |
| 04 Ao Guang | 05 dragon | robed lord vs serpent; long horse-like head with fin beard vs short young face, no beard; branching antlers vs two short spikes; blue-green vs white; gold vs sea-green eyes |
| 05 / 06 Third Prince | 04 Ao Guang; the bay horse | as above; white horse with pale-blue mane and sea-green eyes vs plain bay |
| 07 Bajie | 08 Wujing; 01 Wukong | pig head vs ogre face; round vs gaunt; pink-gray vs slate; black bristle vs wild red; black tunic vs sand-brown; rake vs crescent spade; no necklace vs nine skulls |
| 08 Wujing | 07 Bajie | as above, inverted |
| 09 Old Gao | 02 Sanzang | as above |
| 11 Gao daughter | 12 Wukong as the bride | the band at the hairline is the only difference, by design; the daughter never wears gold |
| 12 Wukong as the bride | 11 Gao daughter | the always-visible finger-width gold brow band at the hairline is the sole pre-change separator; otherwise an exact identity match — no drift of hair, pose, face, or jacket from sheet 11 |
| Sanzang's bay horse (02, view d) | 06 white horse | brown bay coat, black mane and tail, dark eyes, a plain working saddle vs white coat, pale-blue mane and tail, sea-green eyes, dark-red brass-fitted saddle |
| 13 robbers | 02 Sanzang; 09 Old Gao | cloth head-wraps over hair, beardless, rough brown/gray, cudgels and a chopper vs a bare shaven monk in saffron and red; vs a bald old farmer with fringe, knot, and long moustache in indigo |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast. The Gao daughter (pp 31, 36–37) has a sheet and no balloons.
  The monk's bay horse (pp 4–24) is locked as view (d) of `02-sanzang`.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`). The young monkey on p 1 is brown, bare and
  young. The six robbers are locked as an ensemble on `13-robbers`; any other
  human on the road is a faceless traveller at a distance.
  Sea-floor servants are shrimp and crab. Villagers are shut indoors.
- Reserved stacks beyond the eight principals (mirrored in the ledger): paired
  hair loops + young round face + pale-green jacket + no gold → the Gao
  daughter; that stack + the thin gold brow band → Wukong as the bride; white
  fine-boned horse + pale-blue mane and tail + sea-green eyes + dark-red
  brass-fitted saddle → the Third Prince; bay coat + black mane and tail + the
  first horse's saddle and bridle → Sanzang's first horse (pp 4–24 only);
  cloth head-wrap + rough brown/gray + cudgel or chopper → the six robbers.
- A rejected sheet never becomes a lock and never becomes an input.
- The gold band is a thin flush plain band, the same gold as the staff's caps,
  never a crown, never jeweled, never wider than a finger.
- The staff's lock is the staff in hand and the needle behind the right ear on
  `01-wukong`, as in Volume I. The monk's ringed staff never reads as it.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas: **(a)** three-
quarter head and shoulders, neutral expression, even light; **(b)** full-length
standing figure, default costume, habitual posture; **(c)** strict profile, same
light; **(d)** the one state the script actually needs.

## 01 — WUKONG *(retired 2026-10-15; kept as the record of six candidates' lessons; see `10-wukong`)*

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the two approved Volume I sheets: the face and
the gold eyes with the thin red ring come from the tempered sheet; the body,
tail, posture and staff from the other. This is the same monkey, five hundred
years later, in new clothes.

Sun Wukong, the Monkey King, is unmistakably a monkey, not a man. His face is
short and heart-shaped, with a pale hairless muzzle and pale cheek field, a
wide mouth, a low brow, and large round gold eyes set wide, each iris circled
by one thin red ring of fire. Use the bare head in the fourth view on the
attached Volume I body sheet, the young monkey in the leaf kilt standing on
the split stone, as the anchor for face and ear proportions: two
rounded, soft-edged, cupped macaque ears sit at the sides of the head at eye
level, never pointed or elf-like. The cap is gone. Around the short
heart-shaped pale face, lock one pronounced swept-back crown and rear ruff of
separated golden fur tufts, longest behind the ears. This is monkey fur
continuous with the cheek ruff, not human hair. Use the identical face, round
ear geometry, and swept golden-fur silhouette in all four views.

His body is small and wiry, a head shorter than any human, with long arms and
a long tail fully visible in every full-body view. His posture is always
active and asymmetrical: one foot raised, a crouch, or a forward pitch, never
both feet planted in a square upright stance. His habitual gesture is a flat
hand shading his eyes to look into the distance. At rest he looks ready to
laugh.

In views (a), (b), and (c), he wears a plain undyed hemp travelling robe to
the knee, cord belt, sleeves rolled to the elbow, and one neat mended patch at
the left shoulder, over the tiger-skin kilt; his feet are bare. He has no cap,
gold brow band, or armor. When the full staff is absent, show one tiny straight
red-lacquer-and-gold needle tucked flat into the fur just behind his right
ear, close and parallel to the skull, with one capped tip showing just beyond
the rear ruff as a clear single red-and-gold tick. It must read as the stored
staff, not as part of the ear or a horn. Never add a second needle or any other
head ornament.
The full staff is a straight constant-diameter red-lacquered iron cylinder,
taller than Wukong, with blunt gold end caps and tight flush gold bands only
beside the caps; it has no mid-shaft collar, ring, taper, point, blade, ringed
head, or rake teeth.

View (a): three-quarter head and shoulders from his right side in even light;
show the swept golden-fur ruff, the small lateral round ear, both gold eyes with
their thin red iris rings, and the single red-and-gold needle tip behind the
right ear.
View (b): full length in the pilgrim robe, holding the full staff, one foot on
a low stone and the other hand shading his eyes; show the left-shoulder patch
and the entire long tail.
View (c): full-length strict right-side ninety-degree profile, facing left;
keep the short muzzle, swept golden-fur ruff, small round right ear, and single
projecting needle tip exact. Put one foot on a low stone, pitch the
torso slightly forward, and show the entire tail.
View (d): just released after five hundred years under the mountain, arms
flung wide and laughing. Keep exactly the same face, ears, and swept ruff,
but break the ruff and limb fur into dusty matted clumps with sparse muted moss
embedded at the surface; the fur remains unmistakably golden-tawny beneath the
dirt. He wears the old gold scale armor of Volume I gone dull green and broken
into hanging rags over a faded red tunic and the tiger-skin kilt. No cap and no
gold brow band.

Wukong must remain distinct from Bajie at page scale and in grayscale: small,
wiry, golden, short-muzzled, round-eared, swept-furred, long-tailed, active,
and light-robed, never huge, round, pink-gray, long-snouted, floppy-eared,
slow, or dressed in a black tunic. Never give Wukong a human face, gray or
silver fur, a stooped back, a monk's shaven head, saffron robe, red kasaya,
tall or pointed ears, or a smooth human coiffure or long hanging hair.

Model form with broad visible brush-and-ink contours and flat mineral-pigment
washes that pool on toothed paper. Do not use parallel or crossed hatch marks
on fur, cloth, armor, stone, or shadow.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — SANZANG

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Tang Sanzang, a young monk of about twenty-five. Slender, upright, of middle
height. A long oval face, smooth and beardless; a high round fully shaven
head with no hair and no topknot; straight dark brows; calm dark almond eyes;
a straight nose; a small closed mouth; fair skin. Stands straight with his
weight even. Habitual gesture: palms pressed together under his chin.
Expression at rest: polite, a little anxious, determined.

Costume: a saffron-yellow travelling robe to the ankles, under a red kasaya
with a gold-thread grid draped over the left shoulder; straw sandals; a broad
round straw hat hanging on his back by its cord. The monk's staff: a dark
wooden staff as tall as he is, topped with a pewter loop carrying six small
rings. A cloth bundle on his shoulder in view (b).

Views: (a) three-quarter head and shoulders, palms together under the chin;
(b) full length walking with the ringed staff and the bundle; (c) strict
profile showing the round shaven skull and the hat on his back; (d) full
length leading a plain bay horse (brown, black mane and tail, a dark red
saddle with brass fittings) by the bridle, his eyes wide, frightened, still
walking.

Sanzang must never be confused with Guanyin: his bare shaven head against
her white hood-veil; a young man's plain face against a woman's face with a
red dot between the brows; saffron and red against pure white; sandals on the
ground against a cloud; a ringed staff against a willow sprig and vase. He
must never be confused with Old Gao: young, upright, fully shaven and smooth
against old, stooped, a gray fringe and a long gray moustache. No beard, no
hair, no halo, no crown, no weapon.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — GUANYIN

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Guanyin, the Bodhisattva of mercy: a tall serene woman who looks about
forty. A long oval face, high smooth brow, long-lidded downcast eyes, arched
fine brows, a small red mouth, a small red dot between the brows, pale skin.
Black hair dressed high and covered by a long white hood-veil that falls to
her shoulders and down her back, with a small gold crown bearing a tiny
seated figure at the front of the hood. Long-limbed and very still.
Habitual gesture: a willow sprig held lightly, lifted, in her right hand; a
small white porcelain vase in her left. Expression: warm, exact, unhurried.

Costume: flowing white robes and the white veil; a gold-and-jade necklace;
nothing else coloured. She stands on a small white cloud in every full view;
her feet never touch the ground.

Views: (a) three-quarter head and shoulders, willow lifted; (b) full length
standing on a small cloud; (c) strict profile, the line of the veil and the
crown; (d) seated on the cloud, bending forward and down as if handing
something to a person below, both hands forward.

Guanyin must never be confused with Sanzang: a white hood-veil and crown
against a bare shaven head; a woman's face with a red dot and red mouth
against a young man's plain face; pure white against saffron and red; a cloud
against the ground; a willow and vase against a ringed staff. No shaven head,
no saffron, no kasaya, no staff, no hat, no halo disk.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — AO GUANG

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground. No lettering, labels, watermarks,
panel rules, view boxes, or enclosing border. Attach the approved Volume I
sheet: this is the same Dragon King, unchanged.

Ao Guang, the old and vast Dragon King of the Eastern Sea, is a dragon in the
shape of a lord. A long horse-like dragon head, a scaled blue-green face, a
heavy brow, large round golden eyes each with one centered vertical slit
pupil. Two branching antlers. Two long white whiskers that float as if
underwater. A beard of overlapping blue-green fin plates under the jaw. A
human-shaped body, enormous: seated on a coral throne he reads as about twice
the height of a standing man. Habitual gesture: fingers drumming on the
throne's arm. Expression: grand, weary, very polite up to the edge of panic.

Costume: deep sea-green robes patterned with waves, a coral crown, one pearl at
the throat.

Views: (a) three-quarter head and shoulders; (b) full length seated on the
coral throne, fingers drumming; (c) strict profile; (d) seated, leaning
forward, pouring tea with great care from a tiny white teapot into a tiny cup,
his eyes wide with polite alarm.

Ao Guang must never be confused with his son the white dragon: a robed lord
with a human body against a slim serpent; a long horse-like head with a fin
beard against a short young beardless face; branching antlers against two
short spikes; blue-green scales and gold eyes against white scales and
sea-green eyes. Never a human face, never ordinary-man scale.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — THE WHITE DRAGON

A character reference sheet, 1536 × 1024 landscape, four views of the same
creature on one plain warm-paper ground, no lettering of any kind, no labels.

The Third Prince, a young dragon. A slim serpentine dragon, white as river
foam, long and lithe; a short narrow young dragon face with no beard and no
fins at the jaw; two small short unbranched pale-gold horn spikes, never
antlers; large round sea-green eyes; a pale-blue mane running the length of
the spine; four small clawed legs; a tapering tail. No robes, no crown, no
human body. Expression at rest: quick, ashamed, eager.

Views: (a) three-quarter head and neck, the sea-green eyes and the two short
horns clear; (b) the full length of the body in one long S-curve, as if
swimming through the air; (c) strict profile of the head; (d) bursting up out
of water in a column of white foam, jaws wide.

The white dragon must never be confused with Ao Guang: no antlers, no
whiskers, no fin beard, no blue-green scales, no gold eyes, no robes, no human
body. It is a slim white serpent with sea-green eyes and a pale-blue mane.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — THE WHITE HORSE (state sheet, anchored on approved 05)

A character reference sheet, 1536 × 1024 landscape, four views of the same
animal on one plain warm-paper ground, no lettering of any kind, no labels.
Attach the approved white dragon sheet: this is the same creature, turned
into a horse. The eyes and the pale-blue mane carry the identity.

A slim, fine-boned white horse, white as river foam, with a pale-blue mane and
a pale-blue tail, and the dragon's large round sea-green eyes. It wears a
dark red leather saddle with brass fittings and a plain bridle. Calm,
watchful, never rearing.

Views: (a) three-quarter head and neck, the sea-green eye clear; (b) full
length standing, saddled; (c) strict profile; (d) standing in shallow water,
looking back over its shoulder at the water.

The white horse must never be confused with the monk's first horse, a plain
bay with a black mane. It is never brown, never dappled, never with dark eyes.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — BAJIE

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Zhu Bajie, a pig-headed man, big and round, about thirty-five. A pig's head: a
long snout with a wide pink-gray nose disc, two small lower tusks, enormous
floppy ears hanging to his jaw, small black eyes, bristly black hair on a
pink-gray hide. A huge round belly, short thick legs, broad sloping shoulders;
a head taller than a man and twice as wide. Slouches with his belly forward.
Habitual gesture: patting his belly, or fanning himself with one ear.
Expression at rest: hopeful, greedy, a little hurt.

Costume: a black cotton tunic open over the belly, a blue sash, black
trousers. His weapon: a nine-toothed iron rake on a long wooden shaft.

Views: (a) three-quarter head and shoulders, one ear lifted; (b) full length
with the rake on his shoulder, belly forward; (c) strict profile showing the
long snout and the hanging ear; (d) trudging with a bamboo carrying pole over
his shoulder, two cloth bundles hanging from it, mouth open, complaining.

Bajie must never be confused with Wujing the river ogre: a pig's head with
floppy ears against a gaunt ogre face; round and soft against bony and long;
pink-gray against slate blue-gray; black bristle against wild red hair and
beard; a black tunic against sand-brown; a rake against a crescent spade; no
necklace. Never fur, never a monkey's muzzle, never gold.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — WUJING

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Sha Wujing, a river ogre who looks about forty-five. He is a head taller than a
big man but only half as wide: tall and gaunt, bony and long-limbed, with long
arms and a forward hunch from the shoulders. His slate blue-gray face is long
and hollow-cheeked, with deep-set round red-brown eyes under a heavy brow, a
short broad flat nose with a wide bridge and level blunt end, and a wide grim
mouth. One strong hollow plane defines each cheek and one clean edge defines
each lower lid, giving him a hard-lived face in its forties rather than an
elderly face. Wild bristling red hair and a wild red beard frame the face.
Expression at rest: grim, ashamed, honest. Habitual gesture: one hand closed
over one skull as if counting.

He wears a dark sand-brown sleeveless tunic, a dry river-reed sash in tan,
ochre and muted brown, and has bare arms and feet. Clear below the beard, a
shallow open cord lies across the upper chest with exactly nine separate,
clean, pale fist-sized skulls: four on each side and one at the center, with a
visible gap between neighbours. His weapon is a long staff with a flat
crescent-moon blade at one end and a small spade at the other.

Views: (a) three-quarter head and shoulders, one hand closed around one skull;
(b) full length, hunched forward, holding the crescent spade with both hands
away from his chest so all nine skulls are unobstructed and countable in their
four-one-four arrangement; (c) strict profile showing the long face, heavy
brow, short broad blunt nose, beard mass and shoulder hunch; (d) kneeling in
shallow water, head bowed in shame, both hands resting open on his knees, the
cord of exactly nine skulls still around his neck in the same four-one-four
arrangement as view (b), every skull separately countable, none hidden by
the beard or the water. (The lifting-off on page 45 is drawn from the
object plate.)

Wujing must never be confused with Bajie the pig: a gaunt ogre face against a
pig's head and floppy ears; bony against round; slate blue-gray against
pink-gray; wild red hair and beard against black bristle; sand-brown against
black; a crescent spade against a rake. Never a long projecting or down-hooked
nose, dense age wrinkles, a dragon's face, scales, antlers, green costume
accents, or blood. The skulls are drawn as nine; under the ledger's art tolerance, a spaced cord of eight to ten reads as nine and passes.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 09 — OLD GAO

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Old Gao, a farmer of about sixty-five. A small stooped old man, thin and
wiry, shorter than a young man. A round wrinkled sun-browned face, bald on
top with a fringe of gray hair at the sides and back tied in a small gray
knot at the back of the head, a thin gray moustache that hangs past his chin,
and a wisp of gray chin beard; anxious narrow eyes. Habitual gesture:
wringing his hands, or holding a paper lantern up high. Expression at rest:
worried and aggrieved.

Costume: a faded indigo farmer's jacket and trousers, a cloth belt, cloth
shoes.

Views: (a) three-quarter head and shoulders, wringing his hands; (b) full
length, stooped, holding up a lit paper lantern; (c) strict profile showing
the gray knot and the hanging moustache; (d) peering through the crack of a
barred wooden gate with the lantern.

Old Gao must never be confused with Sanzang the monk: old, stooped, a gray
fringe and knot and a long gray moustache against young, upright, fully
shaven and smooth; faded indigo against saffron and red. No robes, no
kasaya.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 10 — WUKONG

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the two approved Volume I sheets: the face and
the gold eyes with the thin red ring come from the tempered sheet; the body,
tail, posture, staff, and the bare uncapped head from the other sheet's fourth
view, the young monkey in the leaf kilt standing on the split stone. This is
the same monkey, five hundred years later, in new clothes, without the cap he
always wore in Volume I.

Sun Wukong, the Monkey King, is unmistakably a monkey, not a man. His face is
short and heart-shaped, with a pale hairless muzzle and pale cheek field, a
wide mouth, a low brow, and large round gold eyes set wide, each iris circled
by one thin red ring of fire. His ears are two small upright monkey ears at the sides of the head, cupped,
their rims rounded or turning through a soft peak, the top at or a little above
the brow line, the same in every view; never long, never narrow and
sharp-tipped like an elf's or a fox's, never floppy.
Around the pale face, one swept-back crown and rear ruff of separated golden
fur tufts, longest behind the ears, continuous with the cheek ruff; monkey
fur, not human hair.

Across his brow, in views (a), (b) and (c), a thin plain gold band, just above
the eyes and below the fur of the crown, flush to the fur, no wider than a
finger, the same gold as the staff's end caps, no jewels, no pattern, never a
crown shape. It sits in front of the ears and never touches or covers them.

His body is small and wiry, a head shorter than any human, with long arms and
a long tail fully visible in every full-body view. His posture is always
active and asymmetrical: one foot raised, a crouch, or a forward pitch, never
both feet planted. His habitual gesture is a flat hand shading his eyes to
look into the distance. At rest he looks ready to laugh.

In views (a), (b), and (c), he wears a plain undyed hemp travelling robe to
the knee, cord belt, sleeves rolled to the elbow, and one neat mended patch at
the left shoulder, over the tiger-skin kilt; his feet are bare; no cap, no
armor. When the full staff is absent, one tiny straight red-lacquer-and-gold
needle lies flat in the fur just behind his right ear, parallel to the skull,
one capped tip showing as a single small red-and-gold tick; it never reads as
part of the ear or as a horn. The full staff is a straight constant-diameter
red-lacquered iron cylinder, taller than Wukong, with blunt gold end caps and
tight flush gold bands only beside the caps; no mid-shaft collar, ring,
taper, point, blade, ringed head, or rake teeth.

View (a): three-quarter head and shoulders from his right side in even light:
the gold band, the rounded cupped right ear, both gold eyes with their red
rings, the swept golden ruff, the needle tick.
View (b): full length in the pilgrim robe, holding the full staff, one foot on
a low stone, the other hand shading his eyes; the left-shoulder patch and the
entire tail; remove the needle completely from this view.
View (c): strict ninety-degree right-side profile, facing left, one foot on a
low stone, torso pitched forward, the whole tail; the band circling the skull
in front of a rounded cupped ear. Add one tiny straight red-lacquer-and-gold
needle behind that ear, lying flat and parallel to the skull, with only one
capped tip visible as a single small tick; do not enlarge it, duplicate it, or
let it merge with the ear silhouette. Because this is a strict right-side
profile, the left-shoulder patch must be hidden rather than repeated on the
near sleeve. Remove the patch from view (c) and keep the single neat patch only
on Wukong's left shoulder in the views where that shoulder is visible.
View (d): just released after five hundred years under the mountain, arms flung
wide, laughing, with NO band and no robe: the same face and the same rounded
cupped ears, the fur matted with dust and sparse moss but still golden-tawny,
wearing the old gold scale armor of Volume I gone dull green and broken into
hanging rags over a faded red tunic and the tiger-skin kilt. No cap.

Wukong must remain distinct from Bajie at page scale and in grayscale: small,
wiry, golden, short-muzzled, round-eared, long-tailed, active, and light-robed,
never huge, round, pink-gray, long-snouted, floppy-eared, slow, or in a black
tunic. Never a human face, gray or silver fur, a stooped back, a monk's shaven
head, saffron robe, or red kasaya; never long, sharp-tipped, elf-like or floppy ears.

Model form with broad visible brush-and-ink contours and flat mineral-pigment
washes that pool on toothed paper. No parallel or crossed hatch marks.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 11 — THE GAO DAUGHTER

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels.

Old Gao's youngest daughter, a young village woman of about eighteen. A round
gentle face, straight dark brows, dark eyes, a small mouth, light-brown skin;
black hair parted in the middle and dressed in two neat loops above the ears.
Slight, of small height. Habitual gesture: hands folded at her waist.
Expression at rest: tired and relieved.

Costume: a pale green cotton jacket with a high collar over a long darker
green skirt, cloth shoes. No jewelry, no gold anywhere.

Views: (a) three-quarter head and shoulders; (b) full length, hands folded;
(c) strict profile showing the two hair loops; (d) running forward, arms out,
toward someone off the sheet.

She must never be confused with Guanyin: no veil, no crown, no white, no red
dot, no cloud. She never wears gold.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 12 — WUKONG AS THE BRIDE (state sheet, anchored on approved 10 and 11)

A character reference sheet, 1536 × 1024 landscape, four views on one plain
warm-paper ground, no lettering of any kind, no labels. Attach the approved
Wukong sheet and the approved sheet of the young woman.

Views (a)–(c) are the young woman from the attached sheet, exactly her face,
hair loops and pale green jacket, with one thing wrong: the same thin plain
gold band that Wukong wears sits at her hairline, just above the brow. (a)
three-quarter head and shoulders; (b) sitting primly on the edge of a bed,
hands folded; (c) strict profile. View (d) the change half made: from the
right shoulder down still the young woman's green jacket, but the head turning
round fully into the monkey's face from the Wukong sheet, gold eyes with the
red ring, grinning, rounded cupped ears, swept golden ruff, the gold band on
his brow, a long golden tail slipping out from under the jacket.
Redraw the band in all four views as the same finger-width, smooth, featureless
gold strip from approved 10-wukong, flush at the brow/hairline, with no
medallions, engraving, beading, or crown-like shaping. Preserve the Gao
Daughter's face and hair unchanged beneath it.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 13 — THE SIX ROBBERS (ensemble lock)

A character reference sheet, 1536 × 1024 landscape, on one plain warm-paper
ground, no lettering of any kind, no labels, no borders. Six ordinary road
robbers standing in one row, full length, evenly spaced, each a different,
individually repeatable man: all human, all beardless and clean-shaven, faces
of ordinary working men aged twenty to forty, rough knee-length jackets and
trousers in brown, gray, and dull ochre, each head wrapped in a plain cloth
head-wrap of a different dull colour, cloth shoes. From left: the leader,
tallest, broad, a long scar-free square jaw, a dark-gray head-wrap, holding a
broad chopper; a thin wiry man with a hooked nose, brown wrap, a cudgel; a
heavy round-faced man, ochre wrap, a cudgel; a young narrow-faced man, gray
wrap, a short staff; a stocky man with heavy brows, brown-striped wrap, a
cudgel; a lanky man with a long face, faded blue-gray wrap, a cudgel. Below the
row, the same six as small heads in three-quarter view, in the same order.
No monk, no shaven head, no long moustache, no robes, no gold, no saffron,
no indigo farmer's jacket.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board prompts (critic-only rasters, generated from the attached approved sheets)

- **adversarial-sanzang-guanyin.** The monk and the woman from the attached sheets in one frame under the same flat even light, both in three-quarter view on the left half of the canvas and both in strict profile on the right half, side by side at the same distance, plain warm-paper ground, no props in hand, no cloud, no lettering. Then the identical pair repeated small in pure grayscale along the bottom edge. Each face must be exactly the face on its sheet.
- **adversarial-dragon-ao-guang.** The vast robed Dragon King seated on his coral throne on the left and the slim white serpent dragon coiled on the right, heads at the same height, same flat light, three-quarter view, plain warm-paper ground, and the same pair small in grayscale along the bottom edge. No lettering. Each face must be exactly the face on its sheet. Redraw the white dragon with the approved short, narrow young head: shorten the muzzle, enlarge the visible eye into a large round sea-green eye, retain exactly two short unbranched gold horn-spikes, and remove the hard cheek/jaw projections so the jaw remains smooth with no beard or fin silhouette. Remove that quadruped from the board. If a thumbnail repeat is required for the adversarial test, replace it with the locked white dragon silhouette only: a long white serpentine body, pale-blue dorsal mane, four small clawed legs, two short horn-spikes, and no packs, saddle, horse torso, or horse stance. Do not introduce a third intermediate form. Replace it with a miniature repeat of the locked Ao Guang silhouette: enormous human-bodied dragon lord seated on a coral throne, branching antlers and long whiskers readable, with no standing or travelling pose. The thumbnail pair must repeat the same two identities tested by the large figures.
- **adversarial-bajie-wujing.** The pig-headed man and the river ogre from the attached sheets standing side by side at the same distance under the same flat even light, each holding his own weapon, in color on the left half of the canvas and the identical pair in pure grayscale on the right half, plain warm-paper ground, no lettering. Each face must be exactly the face on its sheet.
- **live-pair-wukong-sanzang.** A single unlettered story-scale image: by a small campfire at dusk beside a dirt road, the young monk from one attached sheet sewing a tear at the left shoulder of a plain hemp robe that the gold monkey from the other attached sheet is wearing, the monkey holding his arms stiffly out to the sides, not knowing what to do with his hands. No band, no cap. No balloons, no captions, no text of any kind. Each face must be exactly the face on its sheet.
- **adversarial-silhouettes-a.** The five figures from the attached sheets — the gold monkey in his hemp robe, the young shaven monk, the woman in white standing on her small cloud, the stooped old farmer, the young village woman — isolated full bodies, each complete from head to feet (tail, hands, staff, cloud included), standing at one common scale on one uniform plain light ground, no scenery touching any figure. Top row: the five as true solid black binary silhouettes. Bottom row: the same five, same poses, in matched pure grayscale. No lettering. Each figure exactly as on its sheet.
- **adversarial-silhouettes-b.** The five figures from the attached sheets — the pig-headed man with his rake, the gaunt river ogre with his crescent spade and nine skulls, the vast robed Dragon King seated on a plain block, the slim white serpent dragon coiled upright, the white horse standing — isolated full bodies, complete in outline, at one common scale on one uniform plain light ground, no scenery touching any figure. Top row: true solid black binary silhouettes. Bottom row: the same five in matched pure grayscale. No lettering. Each figure exactly as on its sheet. Redesign both Wujing figures with one shallow open cord carrying exactly nine separate fist-sized skulls—four on each side and one centered—with clear gaps between neighbours and the cord fully clear below the beard. Preserve the present long hollow-cheeked face, heavy brow, gaunt long-limbed build, forward hunch, and crescent-spade silhouette. Redraw the white dragon in both the upper silhouette and lower rendering with the approved juvenile lock: shorten the eye-to-nose span by roughly one quarter, enlarge and round the eye socket, remove the long facial whiskers and any chin-beard mass, and expose exactly two short, smooth, unbranched backward-raked horns as clean silhouette notches. Keep Ao Guang's long horse-like face, fin beard, whiskers, and branching coral antlers unchanged so the ledger's head-level separation survives a costume-free profile crop.
- **adversarial-sanzang-old-gao.** The young monk and the old farmer from the attached sheets, costume-free head-and-shoulders crops (bare shoulders, no robe or jacket) side by side at equal scale and the same flat even light: on the left half both in three-quarter view, then both in strict profile; on the right half both again with reactive expressions (the monk frightened, eyes wide; the farmer anxious, mouth open); along the bottom edge the same four heads small, in pure grayscale. Plain warm-paper ground, no lettering. Each face exactly as on its sheet.

## Setting plates and the object plates

Each plate is 1536 × 1024 landscape, architecture and palette only, **no
figures, no lettering**. Register paragraph verbatim. One line each:

- **set-five-elements.** Attach the approved Volume I plate: the same bare mountain of five ridges like the fingers of a hand pressed into the earth, the same deep face-sized cleft at the base of the central ridge, the same thin vertical gold paper strip flat on the summit rock with no glyphs, and across a strip of sea the green Flower-Fruit peak. Now in spring: fresh grass and moss on the lower slopes only, blossom on a few trees on the far shore, blue sky. Two unframed vignettes on one continuous warm-paper ground: the left the spring mountain whole; the right the same mountain split open down the middle with rock and dust in the air, the cleft gone, the gold strip blowing away.
- **set-border-road.** A dirt road running west through a long dry valley toward far mountains, scrub pines, boulders, dust, low ochre hills on both sides, wide pale sky; beside the road, a single plain white stone milestone about waist height, its face blank with no carving. Ochre and malachite, morning light.
- **set-sea-palace.** Attach the approved Volume I plate: the same hall of crystal and coral, shell-white columns, sand floor lit from above, fish in the hall, the coral throne. At the back, the treasury doorway now holds only an empty round socket in the floor, no pillar, no red glow. Behind the throne, a tall folding screen of plain pale silk. Redesign the screen field to contain a scale-readable monochrome ink composition with three unmistakable structural beats—an old man on a stone bridge, a detached shoe visibly falling, and a boy reaching toward it. Keep the painting entirely ink-only, with no colored pigment, glyphs, labels, or other lettering, and retain the screen directly behind the throne as the hall's only flat pictorial element. Azurite and crystal, no green.
- **set-south-sea.** One compact rocky island in open pale-jade sea, with every secondary landmass and mountain silhouette removed and the distant horizon dissolving into morning mist. One compact, clearly bounded shell-white cloud hovering in unobstructed negative space above the island, visibly separate from the bamboo trunks and canopy. Remove all gold and yellow illumination and use diffuse cool morning light: pale-jade water, shell-white mist and cloud, silver-gray rock, with the dense perfectly still bamboo as the sole visual accent.
- **set-eagle-grief.** A deep narrow gorge of gray cliffs, a fast clear stream of deep green water with white foam over rocks, an undercut bank with a dark hollow beneath it at the waterline, a stony path along the top of the near bank. Cold blue-green, white foam, shadowed light.
- **set-gao-farmhouse.** Two unframed vignettes on one warm-paper ground: on the left, a farmhouse gate in an earthen wall at dusk, a heavy wooden bar across the doors, gray tile roofs, terraced fields behind; on the right, the front room inside, a square table laid with bowls of noodles, two oil lamps lit, plain wooden chairs, paper windows. Warm dusk gold outside, lamplight inside. Remove the plaque and every glyph-like stroke from the lintel; replace that area with one continuous strip of bare, unmarked dark timber while preserving the heavy horizontal gate bar as the location's primary marker. No signboard, inscription, seal, label, watermark, or decorative mark resembling writing may remain. Gate round 4: no round wall plaque or hanging, no calligraphy-like or glyph-like marks anywhere; the front-room walls are uninterrupted unmarked plaster with no ornament of any kind.
- **set-back-house.** One high three-quarter architectural cutaway viewed from the Gao courtyard at night. The small back room is enclosed by an intact gray-tile roof with exposed rafters beneath it and no opening to the sky; inside are a curtained bed, a wooden chest, and a paper window. The narrow plank door is shut. On its courtyard-facing outer surface, one cool blackened-iron hasp crosses from the door leaf to a staple fixed in the outer jamb, with exactly one heavy padlock closed through the staple; the whole engaged assembly is plainly visible from the courtyard. The room, furnishings, and hardware are indigo-black, blue-black, and near-neutral night values. One compact warm lantern glow at the paper window is the only warm hue and the only light source. This is the intact pre-p34 state.
- **set-sand-river.** A river so wide the far side is a thin line, the colour of sand, flat, heavy and still like mud, no waves, no boats; gray reed beds along the near bank; in the foreground a tall upright stone tablet with a smooth blank face, no carving and no marks; on a distant far bank, a faint line of willows. Sand-gold and pale gray, no green and no blue, flat late light.
- **obj-cap-band.** Replace the entire mountain, water, pine, and red-tree setting with one uninterrupted plain warm-paper ground. Keep only the two isolated objects with clear negative space between them. Reduce the vertical wall of both the free band and the band inside the cap to approximately half its present height, making both instances one identical finger-width, featureless sheet-gold strip with a light thin edge. Preserve the closed circle, but remove the current collar/cuff mass so the geometry matches the flush band on approved 10-wukong and 12-wukong-bride at thumbnail, in grayscale, and in strict side view. Replace the cap's current high, faceted, rock-like dome with a low pliable skullcap of thin undyed cream cotton: collapse the crown to less than half the present dome height, remove the stone-like angular planes and crack marks, and replace the thick rigid rim with one thin folded cloth brim. The underside must remain clearly visible. Seat the reduced band continuously and flush against the inside face of that thin folded brim, following the same oval without a visible gap. Its primary construction marker must read as a narrow strip sewn into soft cloth, not a separate rigid hoop resting inside a hard cavity. No lettering.
- **obj-painting.** A borderless painted image with no cord, rollers, end caps, rectangular mount edge, or blank exterior wall; let the ink scene run cleanly to the plate edges. Contain the single high arched stone bridge over a stream, the old man in a robe leaning over the parapet above, the detached airborne cloth shoe falling through the air, and the boy on the bank below reaching up with two raised arms entirely inside the plate. Render the image inside the plate solely in black ink and gray washes, with every colored pigment and gold fleck removed, and with value contrast preserving the high arched bridge, the old man's leaning posture, the detached airborne shoe, and the boy's two raised arms at thumbnail scale. Delete the pavilion, colored mountain panorama, framing pines, and red-leaved trees; retain only the single high arched stone bridge over a stream and the three required action markers: old man above, detached shoe falling, boy below reaching. No seals, no inscription, no lettering of any kind.
- **obj-skulls-raft.** Retired 2026-10-16: the open nine-skull cord is locked on `08-wujing`; the transformed state continues as `obj-nine-skull-raft`.
- **obj-nine-skull-raft.** One borderless, unlettered landscape object plate on uninterrupted warm paper, showing one object only: a low circular raft made from nine pale, clean, fist-sized human skulls (ledger art tolerance: eight to ten reads as nine) locked on the attached `08-wujing` sheet. Place the nine complete skulls at equal 40-degree intervals around a smaller thin disk of tightly interwoven charcoal-brown and pale-gray river reeds. Every full cranium, face, and jaw sits wholly outside the bindings on a dry perimeter, mutually separated and individually countable at thumbnail; no overlap, crop, structural occlusion, or water crosses a skull. One broad continuous pale-gold elliptical band immediately encircles the raft over a small localized patch of sand-gold and pale-gray water. Flat late illumination; pale bone, neutral dark reeds, warm paper, sand-gold, pale gray, and that single pale-gold light accent only. No thick poles, timber framework, cross-braces, extra skulls, skull-like forms, green, blue, blood, figures, scenery, horizon, sun, additional light rings, vignette border, labels, watermark, or lettering.
