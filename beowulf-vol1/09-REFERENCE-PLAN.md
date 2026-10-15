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

**Register name:** Northern Saga (story) + Vellum Chronicle (Mode 4 pages).

**Register, verbatim in every generative sheet prompt:**

> **Northern Saga.** A painted northern saga in the tradition of the great
> book illustrators of a century ago: opaque oil on toned canvas board with
> visible, confident brushwork, a warm peat-brown underpainting showing
> through, thick impasto in the highlights, and strong simple shapes that read
> from across a room. Earth, sea and timber: peat brown, slate grey, sea grey,
> pine green, raw umber, oxide red, bone white, iron grey, and hearth-gold.
> Light like a stage: inside, the gold and red of hearth-fire and torchlight
> with real cast shadows and smoke under the rafters; outside, cold silver
> moonlight, sea fog, and flat grey northern daylight. One deep sea-blue is
> reserved for one character only, the hero Beowulf — bright on the young man,
> faded on the old; nothing else in the world is that blue. Materials painted
> with weight: riveted mail rings, rough undyed wool, grey fur, carved and
> tarred oak, gold shingles, wet black rock, peat water, reeds, iron, leather,
> amber beads, twisted gold, salt spray. Faces painted with character and
> weather, never pretty. Not smooth prestige-oil realism. No glossy
> concept-art surfaces, no airbrushed skin, no photographic rendering, no
> anime proportions, no children's-book softness, no plastic 3D render, no
> fantasy-game armour, no horned helmets, no glowing magic effects except where
> named. No blood, no wounds, no gore. No signature, monogram, artist's mark,
> or watermark in any corner.

Every character sheet closes with the anti-collision clause, verbatim:

> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.

**No sheet carries lettering of any kind** — no name plates, no labels, no
runes, no inscriptions on swords, shields, rings, or stone, no writing on
banners or walls. Labelled sheets teach the page model to letter the art.

**The Chronicle register** (the six Mode 4 pages, one at each chapter break) is
not a cast register. It is carried by one plate, `set-chronicle`, and by each
page's prompt: warm ivory vellum, a ruled margin, iron-gall brown ink, ink and
watercolour wash, and one illuminated initial frame in the Insular style — red
and lapis **interlace knotwork** with a touch of gold. No story character ever
appears in it.

## Anchoring (sequels)

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| — | first book; no cross-volume parent | — |
| 02 beowulf-old | 01 beowulf-young, attached as the in-book identity parent | the same man fifty years on: white hair still tied at the nape, a short close-trimmed white beard, weight, lines, pouched eyes; the crooked nose, left-brow notch, cleft chin, pale blue eyes, and enormous hands unchanged |

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
that need them. **Boards are critic-only rasters and never generation inputs** —
their file names carry `board`, `adversarial`, `silhouette` or `live-pair` so
the tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 01 | `01-beowulf-young` — mail and the deep sea-blue cloak, bronze brooch, boar helmet carried; view (d) the night of Grendel: unarmed, tunic only | character | after script gate | after script gate | new |
| 02 | `02-beowulf-old` — the same man at seventy: white hair tied back, short white beard, faded blue cloak, gold neck-ring; view (d) armed for the dragon: boar helmet on, iron shield, Naegling | character (state) | after script gate | after script gate | `01-beowulf-young` |
| 03 | `03-hrothgar` — crimson robe, grey fur mantle, gold circlet, waist-length white beard, carved staff; view (d) grieving in his high seat | character | after script gate | after script gate | new |
| 04 | `04-wealhtheow` — forest-green gown, oval gold brooches and amber, auburn braids under a white veil, the great gold cup; view (d) offering the twisted gold neck-ring | character | after script gate | after script gate | new |
| 05 | `05-unferth` — black and silver, pointed black beard, Hrunting at the hip; view (d) on his low stool at the king's feet | character | after script gate | after script gate | new |
| 06 | `06-grendel` — the full gaunt hairless form in even light; view (d) half in shadow at the edge of firelight | character | after script gate | after script gate | new |
| 07 | `07-grendels-mother` — weed hair, long wolf jaw, blue-black hide; view (d) rearing with the bone-handled knife | character | after script gate | after script gate | new |
| 08 | `08-wiglaf` — too-big mail, russet, iron cap, the yellow linden shield; view (d) the heir with the gold ring and the boar helmet | character | after script gate | after script gate | new |
| 09 | `09-dragon` — serpent body, short legs, ragged wings, ember-seamed bronze-black scales; view (d) in flight breathing fire | character | after script gate | after script gate | new |
| 10 | `10-old-friend` — Hrothgar's oldest friend (unnamed, no balloon; pp 2, 4, 22, 24): old bald warrior with a grey braided beard; view (d) half-rising from a bench at night, sword half-drawn | character | after script gate | after script gate | new |
| — | `board-heads` — all nine sheets, crop-and-place of each sheet's view (a) | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — all nine, full length | board | — | — | from approved sheets |
| — | `adversarial-beowulf-young-old` — CONTINUITY board: the same man at nineteen and seventy, full length and costume-free head pairs, grayscale pass; must read as one man | board | — | — | `01-beowulf-young` `02-beowulf-old` |
| — | `adversarial-hrothgar-beowulf-old` — the two old kings, full length and costume-free head pairs, grayscale pass | board | — | — | `03-hrothgar` `02-beowulf-old` |
| — | `adversarial-beowulf-young-wiglaf` — the young giant and the slight boy, full length and head pairs, grayscale pass | board | — | — | `01-beowulf-young` `08-wiglaf` |
| — | `adversarial-grendel-mother` — the two water-monsters, full length and head pairs, grayscale pass | board | — | — | `06-grendel` `07-grendels-mother` |
| — | `adversarial-wealhtheow-hrothgar` — the queen and the old king, full length and costume-free head pairs, strict profiles, grayscale pass (added at reference gate round 1) | board | — | — | `04-wealhtheow` `03-hrothgar` |
| — | `live-pair-beowulf-old-wiglaf` — unlettered, page scale: the old king and the boy side by side on the headland | board | — | — | `02-beowulf-old` `08-wiglaf` |
| — | `set-chronicle` — the Chronicle register: an empty ruled vellum page with an empty interlace-knotwork initial frame; an unlettered ink-and-wash map of the North Sea lands | set | after script gate | after script gate | — |
| — | `set-fen-moor` — black fen pools, reeds, strip mist, rising moon; the hall's lit doorway far off | set | after script gate | after script gate | — |
| — | `set-heorot-exterior` — the long gold-shingled hall with dragon-head gable ends on its rise above the moor | set | after script gate | after script gate | — |
| — | `set-heorot-interior` — the long hearth, benches, high seat, shields, iron-banded doors, by firelight and by cold grey day; nothing hung under the gable | set | after script gate | after script gate | — |
| — | `set-geat-harbour-ship` — the Geats' harbour of turf-roofed houses and beached ships; Beowulf's ship under its striped sail | set | after script gate | after script gate | — |
| — | `set-white-cliffs` — Denmark's white cliffs and the landing beach under a grey-green sea | set | after script gate | after script gate | — |
| — | `set-mere` — the black lake in a cleft of grey rock, fog, dripping trees, waterfall | set | after script gate | after script gate | — |
| — | `set-mere-hall` — the green-black depths; the air-filled giant-work cave hall with the pale fire and the giant's sword on the wall | set | after script gate | after script gate | — |
| — | `set-geat-hall` — Beowulf's hall on the Geats' coast fifty years on; the same hall burned to black timbers | set | after script gate | after script gate | — |
| — | `set-geat-forge` — the stone forge shed at night, coals and anvil | set | after script gate | after script gate | — |
| — | `set-barrow` — the grassy headland over the sea and the ancient mound with its stone doorway and steaming stream | set | after script gate | after script gate | — |
| — | `set-hoard` — the stone chamber heaped with gold, cups, armour, and the glowing golden banner | set | after script gate | after script gate | — |
| — | ~~`obj-swords`~~ — retired 2026-10-13: the overloaded five-study plate could not hold scale and state continuity; human-sword locks live on `01-beowulf-young`, `05-unferth`, and `02-beowulf-old`, while the giant sword is split below | object | — | — | — |
| — | `obj-giant-sword-whole` — the whole giant sword alone, resolved from its approved cave-wall state for the fight | object | after script gate | after script gate | `set-mere-hall` |
| — | `obj-giant-sword-hilt` — the same giant sword after the blade melts: golden hilt only, no blade fragment | object | after script gate | after script gate | `obj-giant-sword-whole` |
| — | `obj-claw` — Grendel's claw as a hung object: long dark scaled arm, hooked claws, no blood, shoulder end in shadow | object | after script gate | after script gate | — |
| — | `obj-shields-ring-cup` — the iron shield, Wiglaf's yellow linden shield, the twisted gold neck-ring, Wealhtheow's great gold cup, the golden hoard cup, the boar-crested helmet | object | after script gate | after script gate | — |

**Generation order:** `01-beowulf-young` (he is on more pages than anyone and every other face is built against his); then `02-beowulf-old`, generated from the approved young sheet as its identity parent; then `03-hrothgar`, the old king the old hero must never be read as; then `08-wiglaf`, the boy built against young Beowulf's breadth; then `05-unferth` and `04-wealhtheow`; then the monsters `06-grendel`, `07-grendels-mother`, and `09-dragon`; then boards (head and silhouette boards are crop-and-place from approved pixels, not generations); then the continuity, adversarial, and live-pair boards; then plates in story order.

## States needed, enumerated from the ledger

*Pages are assigned after the script gate. The states below come from
`04-CHARACTER-LEDGER.md` and `05-SETTINGS-AND-OBJECTS.md`; the script may add
none without a new sheet view.*

| Character | State | Pages |
|---|---|---|
| Beowulf (young) | mail, deep sea-blue cloak with bronze brooch, plain sword; no neck-ring | assigned after script gate |
| Beowulf (young) | unarmed, tunic only, no mail, cloak, or helmet — the night of Grendel | assigned after script gate |
| Beowulf (young) | mail and sea-blue cloak with Wealhtheow's twisted gold neck-ring, from the victory feast on | assigned after script gate |
| Beowulf (young) | boar-crested helmet on (rare) | assigned after script gate |
| Beowulf (old) | old mail, faded blue cloak, gold neck-ring, no helmet | assigned after script gate |
| Beowulf (old) | armed for the dragon: boar helmet, iron shield, Naegling | assigned after script gate |
| Beowulf (old) | dying: helmet set down, eyes closed, no wound drawn | assigned after script gate |
| Hrothgar | crimson robe, fur mantle, circlet, staff; standing or in the high seat | assigned after script gate |
| Hrothgar | grieving, seated | assigned after script gate |
| Wealhtheow | carrying the great gold cup | assigned after script gate |
| Wealhtheow | giving the twisted gold neck-ring | assigned after script gate |
| Unferth | seated on the low stool at the king's feet | assigned after script gate |
| Unferth | standing, offering Hrunting | assigned after script gate |
| Grendel | always half in shadow on pages; never whole and fully lit | assigned after script gate |
| Grendel's mother | crouched in the dark; rearing in her hall | assigned after script gate |
| Wiglaf | iron cap, too-big mail, yellow linden shield | assigned after script gate |
| Wiglaf | shield burned away, behind Beowulf's iron shield | assigned after script gate |
| Wiglaf | the heir: gold neck-ring and boar helmet | assigned after script gate |
| Dragon | asleep coiled on the hoard | assigned after script gate |
| Dragon | awake, in flight, breathing fire | assigned after script gate |

## Nearest lookalikes and what carries the separation

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 Beowulf young | 08 Wiglaf; 05 Unferth | huge, broad, tawny-gold hair tied back, broad face, cleft chin, crooked nose vs. slight, dark curly hair, narrow freckled face; vs. lean, black close-cut hair, pointed black beard |
| 01 / 02 Beowulf | each other | must MATCH: flattened mid-bridge nose break, bold white left-brow notch scar, cleft chin, pale blue eyes, tied-back hair, enormous hands, the gold ring; age carried by white hair, short white beard, weight, lines |
| 02 Beowulf old | 03 Hrothgar | massive and heavy vs. very thin; short close-trimmed white beard vs. waist-length flowing beard; hair tied back vs. loose under a gold circlet; mail and faded blue vs. crimson robe and fur |
| 03 Hrothgar | 02 Beowulf old; 04 Wealhtheow | as above, inverted; and see 04 |
| 04 Wealhtheow | 03 Hrothgar (thumbnail silhouette: two tall robed figures at the high seat) | middle-aged long oval face, firm mouth, level dark brows, upright strong shoulders, two heavy auburn braids under a white veil vs. elderly long narrow face, sunken cheeks, stoop, loose white hair and waist-length white beard under a gold circlet; forest green vs. crimson; never blue, never blonde |
| 05 Unferth | 08 Wiglaf; 01 Beowulf young | pointed black beard, sneer, black and silver vs. beardless curly-haired boy; vs. huge tawny clean-shaven giant |
| 06 Grendel | 07 Grendel's mother; 09 dragon | bald, gaunt, ribbed, grey-green, ember eyes, short heavy-browed skull vs. weed-haired, heavier, blue-black, long wolf jaw, green eyes; vs. winged serpent |
| 07 Grendel's mother | 06 Grendel | as above, inverted |
| 08 Wiglaf | 01 Beowulf young; 05 Unferth | as above, inverted; the yellow shield |
| 09 Dragon | 06 Grendel | serpent with wings vs. man-shape |

## Separation system — from the ledger

Identity hierarchy, in order of priority: **1.** face shape and apparent age ·
**2.** hair and facial-hair mass · **3.** body silhouette and habitual posture ·
**4.** costume value pattern · **5.** colour accent, prop, repeated gesture.
Costume and colour may reinforce a character; they may never be the only cues.

The humans are spread on purpose: a young giant, an old thin king, a queen, a
lean dark sneerer, a slight boy — and the young giant grown old. The three
monsters are separated by shape before colour: Grendel a gaunt bald
man-shape, his mother a long-jawed weed-haired water-wolf, the dragon a
serpent with wings.

**Reserved design space** — no background or unnamed figure may inherit a
complete identity stack:

- huge young clean-shaven man with tawny hair tied back, blue cloak → Beowulf (young)
- huge old man with short white beard, white hair tied back, gold neck-ring → Beowulf (old)
- thin old man with waist-length white beard and gold circlet → Hrothgar
- tall woman in green with auburn braids and a gold cup → Wealhtheow
- lean dark man with a pointed black beard in black and silver → Unferth
- slight dark-curly-haired boy with a yellow shield → Wiglaf

**Collision matrix** (the boards above exist for these pairs):

| Pair | Risk | Carried by |
|---|---|---|
| Young Beowulf / old Beowulf | must **match** | flattened mid-bridge nose break, bold white left-brow notch, cleft chin, pale blue eyes, tied-back hair, the ring — continuity board, not separation |
| Hrothgar / old Beowulf | high | thin vs massive; waist-length flowing beard vs short trimmed; loose hair and circlet vs tied hair and helmet; crimson robe vs mail |
| Young Beowulf / Wiglaf | medium | broad, tawny, clean jaw with cleft vs slight, dark curly, narrow face, freckles |
| Unferth / Wiglaf | low | black pointed beard, sneer vs beardless boy with curls |
| Grendel / Grendel's mother | high | bald, gaunt, grey-green, ember eyes vs weed-haired, heavy, blue-black, long wolf jaw, green eyes |
| Grendel / dragon | low | man-shape vs serpent with wings |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast. Beowulf is one character with two locked states; the young
  and old sheets never share a page.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- Unnamed and background figures may never carry a complete reserved identity
  stack. Background Danes and Geats are men of middle age in brown, grey, rust
  and undyed wool, with brown, grey or dark-blond hair and full beards; no
  clean-shaven giants, no blue cloaks, no waist-length white beards, no black
  pointed beards, no women in green with gold cups. Hrothgar's oldest friend is
  an unnamed old warrior with a grey braided beard and a bald head; he must
  never resemble Hrothgar. The coast-guard, the herald, the companions, the
  thief, and the eleven men are scenery: unnamed, unlocked, no balloons.
- **Deep sea-blue is reserved for Beowulf.** No banner, sail, shield, hanging,
  cloak, or garment on any other figure or any plate carries it. Grendel's
  mother's hide is blue-black like wet slate, never a clear blue.
- **The monsters never speak and are never gory.** No blood, wound, body, or
  eating is drawn anywhere. Grendel is always partly in shadow on pages; his
  sheet shows his full form clearly so the pages can hide it consistently.
- A rejected sheet never becomes a lock and never becomes an input.
- **Plates are attached for one item or state, never copied as a group.** King
  Arthur's plates were copied literally into pages. `obj-shields-ring-cup` is
  a multi-state reference: a page prompt attaching it names the one item and
  state it needs, and no page ever shows the whole set. The human swords live
  on their approved character sheets. The giant's sword appears whole only on
  its cave wall and in the swing; after the blade melts only the golden hilt
  exists, carried by its own anchored plate. Naegling is never in the Danish
  half; Beowulf's plain sword is never in the old half.
- **Grendel's claw is its own object plate.** `set-heorot-interior` is drawn
  with the gable bare so it can serve before and after the claw is hung; a
  page with the claw attaches `obj-claw` as well.
- **The twisted gold neck-ring** is absent from the young sheet's default
  views (he receives it at the victory feast) and present on every old-state
  view. Its single locked form is on `obj-shields-ring-cup`.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas, left to right:
**(a)** three-quarter head and shoulders, neutral expression, even light;
**(b)** full-length standing figure, default costume, habitual posture;
**(c)** strict profile, same light; **(d)** the one state the script actually
needs.

## 01 — BEOWULF (YOUNG)

A 1536 × 1024 landscape character reference sheet with four views of the same
nineteen-year-old man, arranged left to right on a plain warm peat-toned
canvas ground. Flat even reference light. No scenery, words, labels, runes,
frames, or borders between views.

Beowulf is exceptionally tall, with very wide shoulders, a narrow waist, long
arms and legs, and enormous hands. He is rangy and still growing, not thick in
the neck, chest, arms, forearms, or thighs, and never compact or
bodybuilder-like. His habitual posture is chest forward and chin up.

His permanent face lock is simple and identical in every view: a broad open
face, wide cheekbones, a square chin with a deep central cleft, pale blue eyes,
and a completely clean-shaven jaw. His broad compact nose has one obvious old
break: a flattened angular bump at mid-bridge, with the lower bridge set
slightly toward his right. His thick straight brows are tawny; at the outer
third of his left eyebrow, one bold narrow white scar removes a complete
vertical strip of brow hair and extends just beyond the brow above and below.
There are no other scars or facial scratches. His long thick tawny-gold hair
is pulled straight back and tied at the nape with a leather thong, with loose
strands at the temples. His fair skin is wind-reddened.

Views (a), (b), and (c) share one costume: a knee-length riveted mail shirt
over a dark brown wool tunic, a deep sea-blue wool cloak pinned at the right
shoulder with a round bronze brooch, a leather belt, leather boots, and
cross-gartered legs. A plain sheathed sword hangs at his left hip, with an
iron-grey blade, plain iron cross-guard, leather grip, and brass-capped pommel.
He has no neck-ring, and the helmet is never worn.

View (a): a large three-quarter head-and-shoulders portrait, turned so his
left eyebrow is fully visible. The flattened break in the nose bridge, the
complete white gap through the left brow, and the cleft chin are unmistakable.
He wears a cocky half-grin beginning at one corner of his mouth.

View (b): full length from the front, showing the long-limbed silhouette,
narrow waist, enormous hands, and wide shoulders. One hand rests on the sword
hilt. The other carries at hip level a rounded iron helmet with hinged
cheek-guards and one small bronze boar standing on its crest. No horns.

View (c): a strict ninety-degree left profile facing screen left, showing the
same broad compact nose with the flattened angular mid-bridge bump, the same
complete white gap through the exposed left eyebrow, the square cleft chin,
and the tied nape hair.

View (d): full length from the front on the night of Grendel, in only the dark
brown knee-length wool tunic, plain belt, boots, and cross-gartered legs. No
mail, cloak, brooch, sword, scabbard, helmet, or neck-ring. Both enormous
empty hands are fully visible, open and ready at his sides. His feet are
planted, his body is completely still, and his expression is deadly serious.

He must never resemble Wiglaf, who is slight with a narrow freckled face and
short dark curls, or Unferth, who is lean with close-cut black hair and a
pointed black beard. Never beard or stubble, dark hair, a second facial scar,
a hooked or long nose, a bulging physique, a horned helmet, or a serene or
modest manner.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — BEOWULF (OLD)

A 1536 × 1024 landscape character reference sheet with four views of one man
of about seventy, left to right, on a plain warm peat-toned canvas ground. No
words, labels, borders between views, or scenery.

The attached approved sheet shows this same man at nineteen. This sheet is the
same man fifty years on — an ageing pass, not a redesign. Keep from the
attached sheet, exactly: the broad face and wide cheekbones; the crooked,
badly set nose bent the same way; the short white notch scar through the left
eyebrow; the square cleft chin; the pale blue eyes; the long hair pulled back
and tied at the nape with a leather thong; the enormous hands.

Restore the young nose as the unchanged primary marker in all four views.
Shorten the old face's nasal bridge and forward projection; remove the long,
downturned profile silhouette; reproduce the young sheet's broad compact nose
with the same flattened angular break at mid-bridge and the same lower-bridge
offset toward his right. The strict profile must preserve that compact broken
silhouette rather than become aquiline.

Make the left-brow notch structural and repeatable. At the outer third of the
left eyebrow, remove one complete narrow vertical strip of brow hair, leave a
clean white gap, and extend the scar just beyond the brow above and below.
Carry the identical notch through every view, especially the large head crop
and strict left-side profile, at a width that remains visible at thumbnail
size.

Fifty years have changed the rest. His long hair is now white, still pulled
back and tied at the nape. A short, full, close-trimmed white beard, trimmed
close enough that the cleft of the chin still shows in the beard line —
never long, never flowing. The pale blue eyes are now pouched and deep-set;
deep lines run from nose to mouth; the forehead is weathered and spotted.
Restore the square cleft chin through the beard. Keep the beard short, full,
white, and close-trimmed, but contour it tightly over the centre of the chin so
the chin's central cleft is visible both in the facial geometry and in the
beard line. Do not let the beard produce the present continuous rounded chin
mass in either the head crop or profile.
He is still the biggest man in any room, but heavy now, thick through the
chest and neck, the shoulders a little rounded. Enormous old hands. Keep this
exact aged face, crooked nose, notched brow, cleft chin, short white beard,
and tied-back white hair in every view.

In views (a), (b), and (c) he wears an old, good coat of mail, a faded blue
wool cloak — the deep sea-blue gone soft and greyed with years — pinned at the
right shoulder with the same round bronze brooch, and at his neck a twisted
gold neck-ring: a thick torc of twisted gold rods with plain flat ends meeting
at the throat. No crown, no circlet. No helmet on his head.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, showing the crooked nose, the notch through the left brow, the pale
pouched eyes, the short white beard over the cleft chin, and the gold ring.
Expression tired, dry, the old grin faintly there. Correct the reaction lock in
view (a). Relax the downward pull of the inner brows, soften the tense lower
lids, and lift one mouth corner into a restrained but plainly readable old
grin. Keep the repaired nose, brow notch, and chin cleft fixed; the expression
must still read as a dry old grin after thumbnail reduction rather than as
stern neutrality.

View (b): full length from the front. Correct the habitual gesture in view
(b). Replace the clenched cloak-gripping fist with one enormous relaxed hand
whose thumb visibly contacts and rubs the twisted gold neck-ring while the
other fingers rest naturally below it. Retain the planted, wall-like stance
and make the shoulders slightly rounded rather than squarely military.

View (c): a true ninety-degree profile facing screen left, in the same light,
showing his left side: the crooked nose, the notched left brow, the short
white beard, and the white hair tied at the nape.

View (d): the same old man armed for the dragon, full length: the
boar-crested iron helmet on his head — a rounded iron cap with hinged
cheek-guards and a small bronze boar on the crest, no horns — the cheek-guards
framing the white beard so the crooked nose and pale eyes still read; on his
left arm a plain, dark, entirely iron round shield whose only structural
features are the simple rim and central iron boss, with no radial panels,
decorative rings, or ornamental stud pattern; in his right hand Naegling
drawn, a long old grey sword with a silver-banded grip. The gold neck-ring at
his throat, the faded blue cloak behind.

He must never be confused with Hrothgar: Beowulf is massive and heavy, with a
short close-trimmed white beard and white hair tied back, in mail; Hrothgar is
very thin, with a waist-length flowing white beard and loose hair under a gold
circlet, in a crimson robe. Never a long beard, never a crown, never frail.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — HROTHGAR

A 1536 × 1024 landscape character reference sheet with four views of one old
man of about seventy, left to right, on a plain warm peat-toned canvas ground.
No words, labels, borders between views, or scenery.

King Hrothgar is tall, very thin, long-boned, and slightly stooped. A long,
narrow face with high cheekbones and sunken cheeks; deep-set grey eyes, kind
and tired; a long straight nose. A very long, flowing white beard reaching to
his waist, and long thin white hair hanging loose to his shoulders under a
plain gold circlet. Long thin hands with heavy gold rings. Keep this exact
long narrow face, waist-length flowing beard, loose white hair, and circlet in
every view.

In views (a), (b), and (c) he wears a long dark crimson wool robe with a
gold-woven border at hem and cuffs, and a grey fur mantle over his shoulders.
No mail, no weapon.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, showing the long narrow face, sunken cheeks, deep-set grey eyes, the
gold circlet, and the flowing beard. Expression warm and sad.

View (b): full length from the front, slightly stooped, leaning on a tall
plain carved wooden staff in one hand, the other long hand reaching out
toward the viewer.

View (c): a true ninety-degree profile in the same light, showing the long
straight nose, the sunken cheek, and the long white beard falling to the
waist.

View (d): the same old man grieving, seated deep in a plain high-backed carved
wooden chair, head bowed, one long hand over his eyes, the beard spilling
over the crimson robe.

He must never be confused with old Beowulf: Hrothgar is very thin and
long-faced, with a waist-length flowing white beard and loose hair under a
circlet; Beowulf is massive, with a short trimmed white beard and his hair
tied back. Never a short beard, never bulk, never mail, never a horned helmet.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — WEALHTHEOW

A 1536 × 1024 landscape character reference sheet with four views of one
woman of about forty, left to right, on a plain warm peat-toned canvas ground.
No words, labels, borders between views, or scenery.

Queen Wealhtheow is tall, upright, and strong-shouldered. A long oval face; a
strong straight nose; level dark brows; steady hazel eyes; a firm mouth that
rarely smiles. Dark auburn hair in two heavy braids wound with gold thread,
under a fine white linen veil held by a narrow gold band. Perfectly straight
posture. Keep this exact long oval face, level brows, auburn braids, and veil
in every view.

In views (a), (b), and (c) she wears a long forest-green wool gown under a
long apron-dress, with two oval gold brooches at the shoulders joined by
strings of amber beads. No crown.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression grave and composed.

View (b): full length from the front, perfectly upright, carrying a great gold
cup high in both hands: a wide, deep, footed gold cup with two small handles
and a band of knotwork around the bowl.

View (c): a true ninety-degree profile in the same light, showing the strong
straight nose, the level brow, and a heavy auburn braid down her back under
the veil.

View (d): the same woman full length, holding out in both open hands a twisted
gold neck-ring — a thick torc of twisted gold rods with plain flat ends —
offering it, her face grave and searching.

She is the only woman in the book. Never blue, never blonde, never a crown
like Hrothgar's, never a fragile pose.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — UNFERTH

A 1536 × 1024 landscape character reference sheet with four views of one man
of about thirty-five, left to right, on a plain warm peat-toned canvas ground.
No words, labels, borders between views, or scenery.

Unferth is lean, wiry, of medium height, and narrow-shouldered. A narrow,
sharp, hollow-cheeked face; a thin, high-bridged nose; heavy-lidded dark eyes
under arched black brows; a thin mouth that sneers on one side. Black hair cut
close to the head, and a short black beard trimmed to a sharp point at the
chin. Olive skin. Keep this exact narrow hollow-cheeked face, arched brows,
close-cut black hair, and pointed black beard in every view.

In views (a), (b), and (c) he wears a black wool tunic with a
silver-embroidered collar, a black cloak, and a silver arm-ring on his upper
arm. At his hip, sheathed, the sword Hrunting, its hilt wrapped in bright
silver wire.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression mocking, the one-sided sneer.

View (b): full length from the front, weight back on one hip, arms folded,
chin tilted, amused.

View (c): a true ninety-degree profile in the same light, showing the
high-bridged nose, the hollow cheek, and the pointed beard.

View (d): the same man seated on a low three-legged wooden stool, one knee up,
an elbow resting on it, leaning back, one hand lifted mid-remark.

He must never be confused with Wiglaf (a beardless boy with dark curls) or
young Beowulf (huge, tawny-haired, clean-shaven). Never fair or long hair,
never a long beard, never bulk.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — GRENDEL

A 1536 × 1024 landscape character reference sheet with four views of one
monster, left to right, on a plain warm peat-toned canvas ground. No words,
labels, borders between views, or scenery. In views (a), (b), and (c) his whole
form is fully visible and clearly lit in flat even light, so every proportion
can be read; only view (d) hides him.

Grendel is a man-shape twice the height of a man and wrong in every
proportion: gaunt and stooped, a narrow chest with every rib showing, arms so
long the knuckles nearly drag, enormous hands ending in huge hooked black
claws. Completely hairless. A long skull with a heavy ridge of brow, deep
sockets with eyes that glow like coals, a wide lipless mouth. Hide the
grey-green of wet stone, scaled on the arms and shoulders; his lower body is
covered in the same coarse, dark, scaled hide, smooth and creature-like, not a
naked man. Both arms whole. Keep this exact long hairless skull, brow ridge,
ember eyes, lipless mouth, rib-cage, and long arms in every view.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, showing the long bald skull, the brow ridge, the coal-glow eyes in deep
sockets, and the wide lipless mouth, closed.

View (b): full length from the front, hunched, head low and thrust forward,
the long arms hanging so the knuckles almost touch the ground, claws curled.

View (c): a true ninety-degree profile in the same light, showing the long
skull, the jutting brow, the hunched spine, and the reach of the arm.

View (d): the same creature at the edge of darkness: lit from one side by warm
firelight, the other half of his body lost in black shadow, the ember eyes
burning, one long arm reaching forward, hooked claws spread, the canvas
ground still plain behind him.

He must never be confused with his mother (long wolf jaw, weed-like hair,
green eyes, blue-black hide). Never hair, never wings, never a comic or
pitiable face. No blood, no gore, no victims, no torn limb.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — GRENDEL'S MOTHER

A 1536 × 1024 landscape character reference sheet with four views of one
monster, left to right, on a plain pale stone-grey canvas ground. No words,
labels, borders between views, or scenery. In every view her whole form is
clearly visible and lit.

Grendel's mother is larger and heavier than her son, powerful through the
shoulders. A long wolfish jaw full of teeth; a flat nose; pale eyes that shine
green like a fish's in the dark. A mass of long, matted black-green hair like
river-weed hanging to her waist. Dark blue-black hide like wet slate, never a
clear or bright blue, wet-shining, paler underneath; webbed, clawed hands.
Her body is a creature's, covered in hide, never a human woman's. Keep this
exact long wolf jaw, flat nose, green eyes, and weed hair in every view.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, showing the long jaw, the flat nose, the green eyes, and the weed hair
hanging around the face. Mouth closed.

View (b): full length from the front, low and crouched, webbed claws spread on
the ground, the weed hair hanging.

View (c): a true ninety-degree profile in the same light, showing the long
wolf jaw, the flat nose, and the hair down her back.

View (d): the same creature rearing up to her full height out of the crouch,
the wet weed hair swinging, jaws parted, one webbed clawed hand gripping a long
knife with a plain iron blade and a bone handle.

She must never be confused with Grendel (bald, gaunt, grey-green, ember eyes).
Never a human woman's face, never a bald head. No blood, no gore.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — WIGLAF

A 1536 × 1024 landscape character reference sheet with four views of one boy
of seventeen, left to right, on a plain warm peat-toned canvas ground. No
words, labels, borders between views, or scenery.

Wiglaf is slight and lanky, still growing, narrow-shouldered. A narrow face
with a long straight nose; big dark brown eyes; dark brows that lift when he
is worried; a wide mouth; beardless. Short, thick, dark-brown curly hair.
Light olive skin with freckles across the nose. He stands too straight when
he is frightened. Keep this exact narrow freckled face, dark curly hair, big
dark eyes, and slight build in every view.

In views (a), (b), and (c) he wears a mail shirt too big for him — his
father's — hanging past his knees with the sleeves too long, over a russet
wool tunic; an old short sword sheathed at his hip.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, bareheaded so the curls read. Expression earnest and worried.

View (b): full length from the front, standing too straight, a plain iron
cap-helmet with no crest on his head, gripping the rim of a round yellow
linden-wood shield with both hands.

View (c): a true ninety-degree profile in the same light, bareheaded, showing
the long straight nose, the beardless jaw, and the curls.

View (d): the same boy as the heir, full length: a thick twisted gold
neck-ring at his throat, holding a boar-crested iron helmet — a rounded iron
cap with hinged cheek-guards and a small bronze boar on the crest — against
his chest in both hands, no shield, standing straight and grave.

He must never be confused with young Beowulf (huge, broad, tawny hair tied
back, cleft chin) or Unferth (pointed black beard, sneer). Never fair or
straight hair, never a beard, never a broad jaw.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 09 — DRAGON

A 1536 × 1024 landscape character reference sheet with four views of one
dragon, left to right, on a plain pale warm-grey canvas ground. No words,
labels, borders between views, or scenery.

The dragon is a long serpent fifty feet from snout to tail, thick as an oak at
the chest, coiling; four short clawed legs set low under the body; great
ragged bat-like wings. A long armoured head with a ridge of backswept horns
and a jaw like a crocodile's; eyes like molten gold. Scales bronze and black,
with seams of ember glow between them; a crest of spines from skull to tail.
Keep this exact long serpent body, short legs, ragged wings, horned crocodile
head, and ember-seamed scales in every view.

View (a): a large three-quarter study of the head and neck in flat even
light, showing the backswept horns, the long crocodile jaw closed, and the
molten-gold eye.

View (b): the whole body from the side, coiled in a long S on the ground,
wings half raised, the four short legs gripping, the spined crest running
from skull to tail tip.

View (c): a true ninety-degree profile of the head and neck in the same light,
showing the length of the jaw and the line of horns.

View (d): the same dragon in flight, ragged wings fully spread, breathing a
river of fire forward from its open jaws, the ember seams between its scales
blazing brightest.

Never a friendly face, never four long legs like a lizard-horse, never a rider
or saddle, no human figure for scale.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 10 — HROTHGAR'S OLD FRIEND

A 1536 × 1024 landscape character reference sheet with four views of one old
man of about sixty-five, left to right, on a plain warm peat-toned canvas
ground. No words, labels, borders between views, or scenery.

He is an old Danish warrior, broad and solid, shorter than Hrothgar, thick
through the chest and shoulders, a little bow-legged. A broad, weathered,
deeply lined square face with a heavy brow, a flattened boxer's nose, small
crinkled grey-green eyes and a wide mouth made for laughing. **Completely
bald**, the scalp brown and freckled from the sun. **A long grey beard worn in
one thick braid** to mid-chest, bound with a plain bronze ring. Big scarred
hands. Keep this exact bald head, braided grey beard, square lined face and
solid build in every view.

In views (a), (b), and (c) he wears a dull brown wool tunic with a grey fur
collar over an old mail shirt, a plain leather belt, a long sword sheathed at
his hip.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, laughing with his whole face.

View (b): full length from the front, standing at ease with one big hand on
his sword hilt.

View (c): a true ninety-degree profile in the same light, showing the bald
crown, the flattened nose and the braided beard.

View (d): the same man at night in his tunic only, half-rising from a bench,
his sword half-drawn from its scabbard, his face alarmed and turned to the
right.

He must never be confused with Hrothgar (very tall and thin, long narrow face,
waist-length loose flowing white beard, loose white hair, gold circlet) or old
Beowulf (huge, white hair tied back, short close-trimmed white beard). Never a
crown, never hair on his head, never a loose or white beard, never blue.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board, plate, and object prompts

Boards are critic-only rasters generated from the attached approved sheets.
Plates are generation inputs: architecture, palette, light and objects only,
unlettered and without figures. Every plate prompt carries the blue-reserve
and no-signature clauses. The bullets run to the end of this file; nothing
follows them.

- **adversarial-beowulf-young-old.** One unframed 1536 × 1024 landscape reference board on a plain warm peat-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. This is a CONTINUITY board: it proves sameness, not difference. The two figures are one man, Beowulf, at nineteen and at seventy, from the two attached approved sheets, and they must read at once as the same person. On the left third, both full length side by side on one floor line at one scale: the young man rangy and broad in mail and the deep sea-blue cloak; the old man heavier and slightly rounded in old mail, the faded blue cloak, and the twisted gold neck-ring. On the right two-thirds, four matched costume-free head pairs in a clean two-by-two field with open ground between them, every crop ending at the jaw and upper neck: a neutral three-quarter pair with closed mouths; the same pair grinning; strict profiles with both noses pointing screen left, showing the left side; the same profiles in pure grayscale. In every pair keep identical: the broad face and wide cheekbones, the crooked nose bent the same way, the white notch scar through the left eyebrow, the square cleft chin, the pale blue eyes, and the hair pulled back and tied at the nape. The only differences are age: the old man's white hair, short close-trimmed white beard with the cleft still showing, pouched eyes, deep lines, and heavier neck.
- **adversarial-hrothgar-beowulf-old.** One unframed 1536 × 1024 landscape reference board on a plain warm peat-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two old men from the attached approved sheets full length, side by side on one floor line at one scale: Hrothgar tall, very thin, and stooped in his crimson robe and grey fur mantle, gold circlet on loose white hair; old Beowulf massive and heavy in old mail, faded blue cloak, and gold neck-ring. On the right two-thirds, four matched costume-free head pairs, circlet removed, every crop ending at the jaw and upper neck with the full length of each beard shown: a neutral three-quarter pair with closed mouths; the same pair in shared grief; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Hrothgar keeps his long narrow face, sunken cheeks, deep-set grey eyes, long straight nose, loose thin white hair, and very long flowing white beard to the waist; Beowulf keeps his broad face, crooked nose, notch scar through the left brow, pale blue pouched eyes, short close-trimmed white beard over the cleft chin, and white hair tied at the nape.
- **adversarial-beowulf-young-wiglaf.** One unframed 1536 × 1024 landscape reference board on a plain warm peat-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two young men from the attached approved sheets full length, side by side on one floor line at one scale: Beowulf very tall and broad in mail and the deep sea-blue cloak; Wiglaf a head shorter, slight and lanky, in his too-big mail and russet, bareheaded, no shield. On the right two-thirds, four matched costume-free head pairs, every crop ending at the jaw and upper neck: a neutral three-quarter pair with closed mouths; the same pair afraid; strict profiles with both noses pointing screen left; the same profiles in pure grayscale. Beowulf keeps his broad face, wide cheekbones, crooked nose, notched left brow, square cleft chin, pale blue eyes, and long tawny-gold hair tied back; Wiglaf keeps his narrow face, long straight nose, big dark brown eyes, freckles, beardless narrow jaw, and short thick dark-brown curls.
- **adversarial-grendel-mother.** One unframed 1536 × 1024 landscape reference board on a plain pale stone-grey canvas ground, flat even light, both creatures fully lit with no shadow hiding either, no lettering, labels, rules, or props in hand. On the left third, the two monsters from the attached approved sheets full length, side by side on one floor line at one scale: Grendel gaunt, stooped, ribbed, and hairless, grey-green, long arms almost to the ground; his mother larger and heavier, powerful through the shoulders, blue-black hide like wet slate, weed hair to her waist. On the right two-thirds, four matched head pairs, every crop ending at the jaw and upper neck: a neutral three-quarter pair with closed mouths; the same pair snarling, with no blood; strict profiles with both snouts pointing screen left; the same profiles in pure grayscale. Grendel keeps his long bald skull, heavy brow ridge, deep sockets with coal-glow eyes, and wide lipless mouth; his mother keeps her long wolfish jaw, flat nose, green fish-shine eyes, and the mass of matted black-green weed hair. No gore.
- **adversarial-wealhtheow-hrothgar.** One unframed 1536 × 1024 landscape reference board on a plain pale stone-grey canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the queen and the old king from the attached approved sheets full length, side by side on one floor line at one scale: Wealhtheow tall and perfectly upright, strong-shouldered, in her long forest-green gown with oval gold brooches and amber; Hrothgar tall, very thin and stooped, in his crimson robe and grey fur mantle, leaning on his carved staff. On the right two-thirds, four matched head pairs, every crop ending at the jaw and upper neck, no veil, circlet, or costume visible in the crops: a neutral three-quarter pair; the same pair grieving; strict profiles both facing screen left; the same profiles in pure grayscale. Wealhtheow keeps her middle-aged long oval face, strong straight nose, level dark brows, steady hazel eyes, firm mouth, and two heavy auburn braids; Hrothgar keeps his elderly long narrow face, high cheekbones, sunken cheeks, deep-set grey eyes, long straight nose, thin loose white hair, and the waist-length flowing white beard. Deep sea-blue is reserved for one character and appears nowhere. No signature, monogram, artist's mark, or watermark in any corner.
- **live-pair-beowulf-old-wiglaf.** One unframed 1536 × 1024 landscape board, unlettered, at story-page scale, in the register: a high grassy headland over a grey sea at dusk, smoke drifting from somewhere off frame. Old Beowulf, from the attached sheet, stands left in old mail, the faded blue cloak, the gold neck-ring, and the boar-crested helmet, a plain dark round shield whose entire face reads as forged iron, with no wood grain or plank seams, retaining only an iron boss and iron rim consistent with that all-metal construction, on his arm; Wiglaf, from the attached sheet, stands right beside him in his too-big mail and plain iron cap, gripping the rim of his yellow linden shield with both hands, looking up at the old man. Their faces three-quarter, each large enough to read at reduced size: Beowulf's crooked nose, short white beard, and pale eyes; Wiglaf's narrow freckled face and dark curls under the cap. No other figures, no dragon. A completely clean full-bleed edge on every side and no letters, glyphs, signature, watermark, caption, label, or border anywhere.
- **set-chronicle.** One 1536 × 1024 landscape plate showing the Chronicle register, two studies feathering into one continuous warm ivory vellum ground with no rules, boxes, or borders between them: a page of an old manuscript chronicle on warm ivory vellum, with a ruled brown-ink margin, faint ruled lines, and in its upper left corner an empty square frame for an illuminated initial in the Insular Northern style — dense red and lapis-blue interlace knotwork, ribbons over and under each other, with a touch of raised gold leaf at the corners — the frame left empty, the page otherwise blank; and a hand-drawn map of the North Sea lands in iron-gall brown ink with soft watercolour washes, green for land and pale grey-green for the sea: the peninsula of Jutland and the Danish islands, the southern coast of what is now Sweden across the water, the open sea between, a few small ships with striped square sails, and no words, letters, or labels anywhere on it. This plate replaces the painted saga register described below: it is pen, iron-gall brown ink, and transparent watercolour wash on vellum, with fine hatching. The lapis of the initial is the only blue, and it is manuscript pigment, not the reserved character blue. No figures, no lettering, no letters inside the initial frame, no pseudo-writing. No signature, monogram, artist's mark, or watermark in any corner.
- **set-fen-moor.** One unframed 1536 × 1024 landscape setting plate, one view: a wide fen and moor at night under a rising moon, black pools of still water among reeds and tussock grass, mist lying in long low strips across the ground, dead stumps, and on a far hill at the very horizon a cold, near-black timber hall silhouette with every window, seam, and secondary aperture unlit and one clearly readable open doorway as the single compact gold accent on the far hill. Repaint every warm foreground and middle-ground passage into cold slate, silver, or blue-grey values while preserving the doorway as the sole compact gold mark; no ochre, rust, russet, or warm peat-brown may remain anywhere in the terrain. Everything else is cold slate, silver, and blue-grey moonlight with no saturated blue object. Deep sea-blue is reserved for one character; no blue banners, cloaks, or hangings on scenery. No figures, no creatures, no lettering. No signature, monogram, artist's mark, or watermark in any corner. The distant hall shows exactly one lit opening — one compact gold doorway — and every other window, gable and aperture of the hall is dark and cold; no second warm light anywhere on the page.
- **set-heorot-exterior.** One unframed 1536 × 1024 landscape setting plate, one view: the greatest hall in the world on a low rise above open Danish moorland in cold silver moonlight — a long, high timber hall with a gold-shingled roof, paired curling dragon-head gables, carved door-posts, great double doors bound with iron, smoke rising from the roof-hole, and a worn path climbing to the doors. Redesign the entire ground and horizon as peat-brown earth, low heath and reeds, and mist in strips, with no visible sea, harbour, coastal village, or mountain-walled inlet. Keep the exterior timber and moor in slate, sea-grey, peat-brown, and raw umber, and confine warm hearth-gold to a small glow through the hall openings. No freestanding door braziers. Deep sea-blue is reserved for one character; no blue banners, cloaks, or hangings on scenery. No figures, no animals, no lettering, no runes. No signature, monogram, artist's mark, or watermark in any corner.
- **set-heorot-interior.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: the interior of the great hall at night by firelight — a long stone-lined hearth down the middle of the floor with a bright fire, carved timber pillars holding a high dark roof, smoke under the rafters, long benches along both walls with round shields in muted red, ochre, and undyed wood and clearly readable, long iron-headed spears secured on racks above and among the existing shield rhythm, a raised high seat of carved wood at the far end, and at the near end great double doors bound with iron bands; and the same hall by cold grey day after a raid, with the same spear arrangement repeated as part of the same hall design, the hearth cold and grey, a bench overturned, bare stone floor and sparse straw continuous with the surrounding ground, pale light through the open doors. Replace the entire exterior vista beyond the doors with the primary location marker: low, treeless moor in cold flat grey daylight, with no visible surf, beach, sea inlet, or coastal cliffs. Keep the iron-banded double doors and the hall geometry unchanged. Rebuild the surface treatment around a visible warm peat-brown underpainting, broad confident brush shapes in the beams and paving, and restrained impasto confined to hearth, torch, and reflected-gold highlights; remove lens-like microtexture and photographic edge/detail treatment while retaining the current long-hearth silhouette and warm-fire/cold-day value opposition. Show no loose cup, goblet, tankard, horn, or other portable vessel in either state. The gable beam above the doors is bare in both studies: nothing hangs there. Deep sea-blue is reserved for one character; no blue banners, cloaks, shields, or hangings on scenery. No figures, no bodies, no blood, no lettering, no runes. Remove both corner marks completely and repaint those exact areas as uninterrupted floor/timber texture, leaving no signature, monogram, watermark, glyph, label, or border anywhere on the plate.
- **set-geat-harbour-ship.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: the Geats' harbour on a grey northern morning — a curve of shingle beach, low turf-roofed houses with smoke, long ships drawn up on the stones, a grey-green sea; and Beowulf's ship under sail on that grey-green sea — a long, low, clinker-built ship of overlapping oak planks, a high curled prow and stern, a row of oars, and a single square sail striped in oxide red and undyed cream. Rebuild the entire sky, sea reflections, roof highlights, and shore highlights in cold slate-grey, sea-grey, and bone-white under a continuous overcast; remove the radiant sun opening and every gold-lit cloud or water passage so the light is broad, cold, and directionless. Reduce the sail's value and saturation contrast while retaining its oxide-red and undyed-cream stripes, and shift the sailing ship's framing so its forward high curled prow is isolated against pale open sea or sky and becomes the strongest compact silhouette and highest local contrast on the plate. Deep sea-blue is reserved for one character; no blue sails, banners, cloaks, or shields on scenery. No figures, no lettering, no emblems on the sail. No signature, monogram, artist's mark, or watermark in any corner.
- **set-white-cliffs.** One unframed 1536 × 1024 landscape setting plate, one view: Denmark's coast from the sea — tall white chalk cliffs shining under a pale sky, green turf on their tops, a narrow shingle landing beach at their foot, a path climbing a gap in the cliffs, the grey-green sea breaking white on the stones in the foreground. Deep sea-blue is reserved for one character; no blue banners, cloaks, or sails on scenery. No figures, no ships, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-mere.** One unframed 1536 × 1024 landscape setting plate, one view: a black lake in a narrow cleft of grey rock, its water perfectly dark and still, fog lying on the surface, gnarled trees leaning out over the water from the cliffs with roots hanging and dripping, a thin waterfall falling into the far end, and a few small water-snakes coiled on the wet rocks at the edge. Cold grey, black, and dark pine green; no warm light at all. Deep sea-blue is reserved for one character; no blue objects on scenery. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-mere-hall.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: murky green-black depths under the lake, faint light from far above, weed drifting, rock walls falling away; and the air-filled cave-hall beneath the water — a great dry chamber of old rough-hewn giant-work stone arches far too big for men, lit by a strange pale fire burning white-green in a stone basin on the floor, old weapons and dark shields hung on the walls, and among them, alone on the wall, one enormous ancient sword far too long for a man, whole, its blade grey and pitted, its hilt of gold. The sword hangs on the wall; nothing else is near it. Deep sea-blue is reserved for one character; no blue objects on scenery. No figures, no creatures, no bodies, no lettering, no runes. No signature, monogram, artist's mark, or watermark in any corner.
- **set-geat-hall.** One unframed 1536 × 1024 landscape setting plate, two spatially discontinuous state studies without a dividing border, using the same camera angle and matching the foundation footprint, ridge length, doorway position, wall-post spacing, and both gable-end terminals exactly. Do not connect the two states with one continuous shoreline, harbour, or village panorama. Beowulf's hall on the Geats' coast fifty years on — smaller and sturdier than the great Danish hall, built of heavy dark timber with a turf-and-shingle roof and a plain carved gable. Make its primary silhouette compact and low-slung: lower the ridge and front gable by roughly one third relative to the footprint, shorten the visible wall run to a few stout bays, thicken the wall and corner posts, and simplify the front carving to restrained structural timberwork rather than a towering ornamental facade. Preserve those exact compact proportions in the burned state. In the burned state remove the roof and walls but leave the corresponding foundation and charred post stumps in those same positions. Remove all open orange flames from the ruined hall and nearby buildings; render a cold blackened frame with small smouldering wisps and one broad grey smoke drift passing over a sparse distant village. The ruined state must read as aftermath, not a second hall burning concurrently beside the intact one. Crop both studies around the hall so the building and its matched footprint occupy the majority of each state; retain only a narrow strip of grey-green sea and a few distant turf roofs as coastal context, and remove the foreground docks and all boats. Deep sea-blue is reserved for one character; no blue banners, cloaks, or hangings on scenery. No figures, no bodies, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-geat-forge.** One unframed 1536 × 1024 landscape setting plate, one view: a low stone forge shed at night, its front open, a bed of glowing orange coals in the hearth with bellows beside it, a heavy iron anvil on a block, hammers and tongs on the wall, a water trough, the coal-glow throwing warm light across rough stone and the dark beyond. Nothing lies on the anvil. Deep sea-blue is reserved for one character; no blue objects on scenery. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **set-barrow.** One unframed 1536 × 1024 landscape setting plate, one view. On a high, exposed headland above a grey sea, an ancient low grave mound of earth and turf rises against a cold overcast dusk. A doorway of two massive neutral-grey standing stones and one heavy stone lintel opens in the mound as a deep, unlit neutral-black void. A small dark-grey stream issues from that doorway and runs down the slope. Compact plumes of pale steam rise at the threshold and along the stream's first descent; the steam is the only light value and the unmistakable location marker. Hold the sky, horizon, sea, surf, and liquid water to cold mid-value slate-grey and sea-grey, clearly darker than the steam. Render the turf in dark pine and olive, exposed earth and dead grass in peat-brown and raw umber, and all stone and lichen in neutral greys. The entire exterior is cold and lightless: no sunset colour, orange, gold, peach, yellow ochre, ember glow, flame, or warm reflection. Deep sea-blue is reserved for one character; no blue object appears in the scenery. No figures, creatures, hoard objects, letters, runes, signature, monogram, artist's mark, watermark, frame, or border.
- **set-hoard.** One unframed 1536 × 1024 landscape setting plate, one view: the stone chamber inside the barrow, its walls of great rough slabs, heaped with treasure — drifts of gold coins, gold cups and dishes, old helmets and mail, rusted swords and arm-rings — and standing above the heap on a pole, a golden banner woven of gold threads that glows softly in the dark, the only light in the chamber. Deep sea-blue is reserved for one character; no blue objects on scenery. No figures, no creatures, no bones, no lettering, no runes. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-swords.** Retired 2026-10-13: human swords remain locked on their approved character sheets; the story-critical giant sword continues as `obj-giant-sword-whole` and `obj-giant-sword-hilt`.
- **obj-giant-sword-whole.** One unframed 1536 × 1024 landscape object plate on a plain warm peat-toned canvas ground, showing one weapon only: resolve the same enormous ancient giant sword seen on the wall in the attached approved cave-hall sheet as a clean full-length study for its fight scene. Lay it horizontally with the entire tip, blade, guard, grip, and pommel visible and generous open ground around it. The sword is far too long and heavy for an ordinary man: a very broad, thick, pitted iron-grey blade and a massive gold hilt. Lock the hilt clearly for its later state: a three-lobed gold pommel; a thick braided grip between two gold collars; and a broad, shallow down-curved gold guard with round terminals, one circular medallion near each end, and small carved figure scenes that are images only, never letters or runes. No second weapon, hands, figures, scabbard, lettering, label, inscription, or rune. Deep sea-blue is reserved for one character; no blue on any object. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-giant-sword-hilt.** One unframed 1536 × 1024 landscape object plate on a plain warm peat-toned canvas ground, showing one object only: the exact same giant sword from the attached approved whole-sword sheet after its blade has melted away. Show the golden hilt alone, large and fully visible, matching its identity parent exactly: the same three-lobed pommel silhouette, grip length and diameter, braid pitch, two collars, guard width, thickness and shallow down-curve, round terminals, paired circular medallions, and carved figure-scene placement. Remove that projection completely and redesign the blade-side centre of the guard as one clean, continuous unbroken edge, with uninterrupted peat ground immediately beyond it; retain the crescent guard, paired circular terminal medallions, braided grip, two collars, and three-lobed pommel unchanged. The final plate must contain no blade, blade stub, shard, remnant, glow, or dripping metal. No hand, figure, second object, scabbard, lettering, label, inscription, or rune. Deep sea-blue is reserved for one character; no blue on any object. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-claw.** One unframed 1536 × 1024 landscape object plate, one view: Grendel's claw hung high under the dark timber gable of a hall, above great iron-banded doors, seen from below by firelight — a monster's limb, a long dark grey-green scaled arm ending in an enormous hand with hooked black claws, hanging by a rope from the gable beam, its shoulder end lost in deep shadow so no torn end is seen. No blood, no torn flesh, no wound, no dripping. Deep sea-blue is reserved for one character; no blue objects on scenery. No figures, no lettering. No signature, monogram, artist's mark, or watermark in any corner.
- **obj-shields-ring-cup.** One unframed 1536 × 1024 landscape object plate on a plain warm peat-toned canvas ground, six objects at one scale with open ground between them, no hands, no figures, no lettering. This is a MULTI-STATE reference: each object is a separate study, never shown together in a story. Put all six studies at one shared physical scale. Keep the shields and helmet at their present sizes, uniformly reduce the torc until its outside diameter is no wider than the helmet across the cheek-guards, retain the thick twisted rods and plain flat ends, and reposition it with open ground around it. Keep both shield diameters fixed and uniformly reduce the entire cup, including handles and foot, until its handle-to-handle width is approximately 50% of either shield's outside diameter; retain the wide deep bowl, two small plain upper-side loop handles, single knotwork band, and foot without changing their proportions. Keep each shield as the dominant form, and keep the hoard goblet smaller again at roughly one quarter of a shield diameter. Do not independently enlarge the torc or cups to fill their cells. Redesign the iron shield as one plain, continuous, dark forged-iron disc. Remove every radial seam, wedge-shaped panel division, crack that reads as a plank or plate joint, decorative concentric treatment, and ornamental face rivet. Retain only a simple iron rim and one central iron boss, matching the primary shield marker already locked on `02-beowulf-old`. Remove the black wolf device from Wiglaf's shield completely. Rebuild it to match the approved 08 sheet as a plain yellow-ochre, visibly vertical-planked round linden shield with one central dark iron boss and a simple dark rim; retain only wear, plank grain, and small construction fasteners, with no heraldic animal or other face-wide motif. The twisted gold neck-ring — a thick torc of twisted gold rods with plain flat ends; Wealhtheow's great gold cup — a wide, deep, footed gold cup with two small plain loop handles attached close to the upper sides of the bowl and a single knotwork band. Remove both animal heads and their projecting necks while retaining the wide deep footed bowl and the single knotwork band. This must match the simple handled cup already carried on the approved 04 sheet. The golden cup from the hoard — smaller and taller, a gold goblet set with red garnets, plainly a different cup; and the boar-crested helmet — a rounded iron cap with hinged cheek-guards and a small bronze boar standing on its crest, no horns. Deep sea-blue is reserved for one character; no blue on any object. No inscriptions or runes. No signature, monogram, artist's mark, or watermark in any corner.
