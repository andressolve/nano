# Reference Plan — approved as a system

**Nothing generates a page until every character visibly on that page has an
approved permanent lock.** Not just-in-time. Locks live in `refs/approved/` and
get there only through `tools/refs.py promote` with an independent critic
report. A sheet in `refs/candidates/` is not a lock.

## Canvas and register — for every sheet

Reference sheets are **1536 × 1024 landscape**; story pages are portrait. This
is not an inconsistency: four views across a wide canvas is what a lock needs.

**Register, verbatim in every generative sheet prompt:**

> **Greenwood Romance.** Golden-age adventure illustration in oil, in the
> tradition of the great book illustrators of a century ago: opaque oil paint
> on canvas board with visible, confident brushwork, a warm raw-umber
> underpainting showing through, thick impasto in the highlights, and strong
> simple shapes that read from across a room. Earth and forest: raw umber,
> burnt sienna, yellow ochre, oxide red, sap green, oak brown, iron grey,
> bone white, snow-light blue, and deep Prussian-blue nights; one deep
> ultramarine reserved for the young king. Light like a stage: low winter sun,
> torchlight and firelight with real cast shadows, moonlight in silver and
> blue, white mist. Materials painted with weight: riveted mail rings, quilted
> linen, rough wool, oak beams, wet grey stone, iron, leather, horsehair,
> snow, still water. Faces painted with character and weather, never pretty.
> Not smooth prestige-oil realism. No glossy concept-art surfaces, no
> airbrushed skin, no photographic rendering, no anime proportions, no
> children's-book softness, no plastic 3D render, no fantasy-game armour,
> no glowing magic effects except where named. No signature, monogram,
> artist's mark, or watermark in any corner.

Every character sheet closes with the anti-collision clause, verbatim:

> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.

**No sheet carries lettering of any kind** — no name plates, no labels, no
inscriptions on the stone, no writing on banners or the table. Labelled sheets
teach the page model to letter the art.

**The Chronicle register** (pages 7, 19, 27, 36, 50, 59) is not a cast
register. It is carried by one plate, `set-chronicle`, and by each page's
prompt: warm ivory vellum, ruled margins, iron-gall brown ink, ink-and-wash
watercolour, one red-and-lapis illuminated initial with a touch of gold. No
story character ever appears in it.

## Anchoring (sequels)

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| — | first book; no parent | — |

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
named. **Boards are critic-only rasters and never generation inputs** — their
file names carry `board`, `adversarial`, `silhouette` or `live-pair` so the
tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 01 | `01-arthur` — mail and the deep-blue surcoat; view (d) the farm boy in a patched brown wool tunic | character | 3 | p 3 | new |
| 02 | `02-merlin` — dark grey-green hooded robe, rope belt, the crooked staff; view (d) hood up, carrying a lantern and a swaddled bundle | character | 1 | p 1 | new |
| 03 | `03-ector` — russet tunic over an old mail shirt; view (d) kneeling in a brown travelling cloak | character | 4 | p 4 | new |
| 04 | `04-kay` — new mail and black-and-yellow surcoat; view (d) the steward's black tunic with a yellow border, no mail | character | 4 | p 4 | new |
| 05 | `05-lot` — bearskin cloak over scaled mail, gold torc, iron crown, red braids; view (d) mounted battle state: iron helmet, sword raised | character | 8 | p 8 | new |
| 06 | `06-pellinore` — dented black armour, faded green surcoat with a white boar, huge sword planted; view (d) the flat-topped great helm on, shield up | character | 39 | p 39 | new |
| 07 | `07-lady-of-the-lake` — white samite gown, silver circlet, wet black hair; view (d) standing on the surface of still water | character | 45 | p 45 | new |
| 08 | `08-uther` — gaunt dying king; view (d) lying in the great bed under the red-dragon coverlet | character | 2 | p 2 | new |
| — | `board-heads` — all eight, crop-and-place of each sheet's view (a) | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — all eight, full length | board | — | — | from approved sheets |
| — | `adversarial-merlin-pellinore` — the two old bearded men, full length and costume-free head pairs, grayscale pass | board | — | — | `02-merlin` `06-pellinore` |
| — | `adversarial-merlin-ector` — the two old men, full length and head pairs, grayscale pass | board | — | — | `02-merlin` `03-ector` |
| — | `adversarial-ector-pellinore` — the two grey-haired knights, full length and head pairs, grayscale pass | board | — | — | `03-ector` `06-pellinore` |
| — | `adversarial-arthur-kay` — the brothers, full length and head pairs, grayscale pass | board | — | — | `01-arthur` `04-kay` |
| — | `adversarial-lot-pellinore` — the two big kings in armour, full length and head pairs, grayscale pass | board | — | — | `05-lot` `06-pellinore` |
| — | `live-pair-arthur-kay` — unlettered, page scale, the p 16 staging: the brothers gripping forearms in a snowy churchyard | board | — | — | `01-arthur` `04-kay` |
| — | `set-chronicle` — the Chronicle register: an empty ruled vellum page with an empty illuminated-initial frame; an unlettered ink-and-wash map of Britain; an ink-and-watercolour study of a sword on vellum | set | 7 | p 7 | — |
| — | `set-cliff-chamber` — the sea-cliff castle and switchback path in a night storm; the dark stone chamber with the great bed and brazier | set | 1 | p 1 | — |
| — | `set-ector-farm` — the muddy farmyard with stable and open forge shed; the forge shed at night, coals glowing | set | 3 | p 3 | — |
| — | `set-london` — the old Roman wall of grey stone with red brick bands and a great gate, roofs and towers inside; a narrow empty snowy street with a locked inn door | set | 6 | p 6 | — |
| — | `set-churchyard-stone` — the snowy churchyard before a squat stone church with the great block, iron anvil, and sword; the cold candlelit church interior | set | 8 | p 8 | — |
| — | `set-tournament` — the snowy tournament field, striped tents, wooden stands, banners | set | 9 | p 9 | — |
| — | `set-great-hall-london` — the long feasting hall with high table, torches, and great doors | set | 23 | p 23 | — |
| — | `set-bedegraine` — the forest valley at dawn with mist on a stream; the same valley at grey noon, empty, strewn with dropped shields and broken spears | set | 28 | p 28 | — |
| — | `set-camelot` — the pale castle on a green hill above a river; the high timber-roofed hall with great hearth and long table | set | 35 | p 35 | — |
| — | `set-forest-fountain` — moonlit oak forest road; the clearing with the stone fountain, pool, battered green-and-white pavilion, and shield hung on an oak | set | 38 | p 38 | — |
| — | `set-lake` — the wide misty lake with reeds, a small wooden boat at the shore, pale far hills | set | 44 | p 44 | — |
| — | `obj-swords` — the sword from the stone whole and broken in two; Excalibur drawn and in its dark-red scabbard | object | 8 | p 8 | — |
| — | `obj-round-table` — the great round oak table ringed with tall chairs, one chair with no gold before it | object | 53 | p 53 | — |

**Generation order:** `01-arthur` (he is on more pages than anyone and is the
book's eye); then `02-merlin`, whom three other old men must be built against;
then `06-pellinore` and `03-ector`, the other two old men; then `04-kay`,
`05-lot`, `07-lady-of-the-lake`, `08-uther`; then boards (head and silhouette
boards are crop-and-place from approved pixels, not generations); then
adversarial and live-pair boards; then plates in page order.

## States needed, enumerated from the script

*Page numbers follow the approved script (round 10, 59 pages) and `05-SETTINGS-AND-OBJECTS.md`.*

| Character | State | Pages |
|---|---|---|
| Arthur | patched brown wool tunic, squire's belt, no armour | 3–20 |
| Arthur | deep-blue surcoat (over mail), thin gold crown | 22–26 |
| Arthur | mail, blue surcoat, helmet on or off, the sword from the stone | 28–34, 38–43 |
| Arthur | mail and blue surcoat, Excalibur in the red scabbard | 44–49 |
| Arthur | blue surcoat at court, no crown (Excalibur at his hip from p 51) | 35, 37, 51–58 |
| Merlin | hood up, carrying the lantern and the bundle | 1 |
| Merlin | hood back, staff | 2, 8, 20, 22–26, 34, 41–49, 52–53, 57–58 |
| Ector | russet tunic over old mail; brown travelling cloak on the road and in London | 4–6, 9, 12–17, 23 |
| Ector | at court in russet | 54, 56, 58 |
| Kay | new mail, black-and-yellow surcoat | 4, 6, 8–17, 23–26, 29–34 |
| Kay | steward's black with a yellow border | 37, 49, 51–57 |
| Lot | bearskin, scaled mail, gold torc, iron crown | 8, 20, 23–24, 55 |
| Lot | mounted for battle, helmet | 29, 32 |
| Pellinore | dented black armour, faded green surcoat, no helm | 39, 41–42, 48, 53–57 |
| Pellinore | great helm on, jousting and fighting | 39–40 |
| Lady of the Lake | white samite, on the water | 45–46 (her arm 44, 46) |
| Uther | in bed under the red-dragon coverlet | 2 |

## Nearest lookalikes and what carries the separation

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 Arthur | 04 Kay | blond, oval, soft-jawed boy, freckles, wide grey-green eyes vs. black-haired, sharp-cheeked young man with a thin moustache; blue vs. black-and-yellow |
| 02 Merlin | 06 Pellinore; 03 Ector; 08 Uther | very thin and stooped vs. enormous; long *forked* white beard and wild white hair vs. short square grey beard and cropped hair; vs. bald, round, clean-shaven; vs. moustache only, in bed |
| 03 Ector | 06 Pellinore; 02 Merlin | short, barrel-bodied, bald, round clean-shaven face vs. huge, cropped grey hair, square beard; vs. tall thin bearded |
| 04 Kay | 01 Arthur | as above, inverted |
| 05 Lot | 06 Pellinore | copper-red braided beard, gold torc, black bearskin vs. iron-grey square beard, faded green, dented black armour |
| 06 Pellinore | 02 Merlin; 03 Ector; 05 Lot | as above, inverted; the biggest man in the book |
| 07 Lady | — | the only woman with a name; white, black hair, stillness |
| 08 Uther | 02 Merlin | grey moustache, no beard, gaunt, red dragon |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast. Uther is on one page and still gets a sheet: he shares it
  with Merlin and must not be read as him.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`). Background lords and knights are
  middle-aged, brown- or dark-haired with short beards, in muted surcoats
  (brown, rust, grey, dull green, dull red); never blond boys, never a forked
  white beard, never red braids, never a bald clean-shaven old man, never
  black-and-yellow, never deep blue. Townspeople are in browns and greys.
  The churchmen at the crowning are in white, faces small. The minstrel is a
  young dark-haired man. The wounded smith is a young dark-haired man in a
  leather apron. No background woman wears white.
- A rejected sheet never becomes a lock and never becomes an input.
- **Two swords, never confused.** The sword from the stone is plain: long,
  dull iron-grey blade, dark iron cross-guard, round iron pommel, a worn
  leather grip. It breaks on p 40; Arthur holds the two halves on pp 41–43;
  Kay takes them on p 49; it is never seen whole again. Excalibur is held up by
  the arm on p 44, taken on p 46, and Arthur's from p 47: longer and bright,
  with a gold-wired grip and a single green stone in the centre of its
  cross-guard, worn in a dark-red leather scabbard chased in gold. The scabbard
  first appears on p 44, is buckled on first on p 47, and is on Arthur's hip
  on every armed page from p 48.
- **Merlin's magic is never a glow.** The only magical light in the book is
  the sword's flare on p 21 and its blaze on p 32. Merlin's sleep spell on
  p 41 is a gesture and a falling giant.
- **The Round Table** is proposed on p 52, built on p 53, carries its gold
  names on pp 54–58, and has exactly one unmarked chair on pp 54 and 57–58.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas, left to right:
**(a)** three-quarter head and shoulders, neutral expression, even light;
**(b)** full-length standing figure, default costume, habitual posture;
**(c)** strict profile, same light; **(d)** the one state the script actually
needs.

## 01 — ARTHUR

A 1536 × 1024 landscape character reference sheet with four views of one
fifteen-year-old boy, left to right, on a plain warm-umber-toned canvas
ground. No words, labels, borders between views, or scenery.

Arthur is a boy, not yet a man: slight and long-limbed, still growing into
big hands and feet, narrow shoulders. An oval face with a soft, rounded jaw
and no trace of beard; a dusting of freckles across a short straight nose;
wide-set grey-green eyes under straight dark-blond brows; a wide, expressive
mouth. Thick straw-blond hair, roughly cut and uneven, falling over his
forehead and the tops of his ears. Fair skin reddened at the cheeks by
weather. He leans slightly forward, eager. Keep this exact face, jaw, freckles,
eye set, and hair mass in every view.

In views (a), (b), and (c) he wears a knee-length coat of riveted mail with a
plain deep-ultramarine-blue surcoat over it, belted, slightly too big in the
shoulders; brown leather boots; no helmet; no crown. A plain long sword with a
dark iron cross-guard and a round iron pommel hangs sheathed at his left hip.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, showing the soft jaw, freckles, grey-green eyes, and the blond hair over
the brow. Expression open and earnest.

View (b): full length from the front, weight forward on the balls of his
feet, one hand on the sword hilt, the other pushing his hair back with the
heel of the hand.

View (c): a true ninety-degree profile in the same light, keeping the short
straight nose, the rounded unbearded jaw, and the hair falling over the ear.

View (d): the same boy as a farm squire, full length: a patched, undyed
brown wool tunic to mid-thigh, a squire's plain leather belt, brown hose,
muddy boots, sleeves pushed up, holding a polishing rag.

He must never be confused with Kay: Arthur is blond, round-jawed, freckled,
and beardless; Kay is black-haired, sharp-cheeked, older, with a thin
moustache.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — MERLIN

A 1536 × 1024 landscape character reference sheet with four views of one very
old man, left to right, on a plain warm-umber-toned canvas ground. No words,
labels, borders between views, or scenery.

Merlin is very old, tall, and very thin, stooped from the shoulders, with a
long neck. A long, narrow, deeply lined face; a great hooked nose; deep-set,
bright black eyes under wild, tufted white brows; hollow cheeks. A long,
narrow white beard that divides into two points at the chest — clearly forked.
Wild white hair standing away from his head in all directions. Big-knuckled,
long-fingered hands. Keep this exact face, nose, forked beard, and hair in
every view.

In views (a), (b), and (c) he wears a plain hooded robe of very dark
grey-green wool, frayed at the hem, the hood down on his shoulders, a rope
belt, and a single silver ring with a green stone on his right hand. He leans
on a crooked, knotted wooden staff taller than himself. No pointed hat, no
stars, no symbols, no glowing anything.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light, showing the hooked nose, deep-set eyes, and the fork of the beard.
Expression dry and amused.

View (b): full length from the front, stooped, leaning on the staff, the
other hand raised, with the index and middle fingers both clearly extended
together in the same pointing direction, and the ring and little fingers
folded.

View (c): a true ninety-degree profile in the same light, showing the great
hooked nose and the long forked beard against the narrow chest, leaning on
the same crooked, knotted wooden staff used in view (b), extending from the
ground to clearly above Merlin's crown. Do not retain a short walking stick
or cane.

View (d): the same man full length with the hood pulled up so his face is in
shadow, walking, a small lantern hanging from the top of his staff, and a
small swaddled bundle held against his chest under his cloak.

He must never be confused with Pellinore (huge, cropped grey hair, short
square beard), Ector (short, bald, clean-shaven), or Uther (grey moustache, no
beard). No wizard's hat.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — ECTOR

A 1536 × 1024 landscape character reference sheet with four views of one man
of about fifty-five, left to right, on a plain warm-umber-toned canvas ground.
No words, labels, borders between views, or scenery.

Sir Ector is a country knight: short and broad, barrel-bodied, thick-necked,
with thick forearms. A big round head, bald on top, with a fringe of short
grey hair around the sides and back; a round, ruddy, completely clean-shaven
face with heavy jowls; small kind brown eyes under bushy grey brows; a broken,
flattened nose. He plants his feet wide. Keep this exact round bald head,
clean-shaven jowled face, and broken nose in every view.

In views (a), (b), and (c) he wears a worn russet-red wool tunic to the knee
over an old, dark mail shirt whose sleeves show at the wrists, a broad leather
belt, and brown boots.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression warm and gruff.

View (b): full length from the front, feet wide, both thumbs hooked in his
belt.

View (c): a true ninety-degree profile in the same light, showing the round
bald crown, the broken nose, and the heavy clean-shaven jaw.

View (d): the same man down on one knee, head bowed, wearing a heavy brown
wool travelling cloak over the russet tunic.

He must never be confused with Pellinore (huge, cropped grey hair, square
beard) or Merlin (tall, thin, long forked beard). Ector has no beard at all.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — KAY

A 1536 × 1024 landscape character reference sheet with four views of one man
of nineteen, left to right, on a plain warm-umber-toned canvas ground. No
words, labels, borders between views, or scenery.

Sir Kay is tall, lean, and hard-edged, a young man. A narrow face with high,
sharp cheekbones and a pointed chin; a thin straight nose; narrow dark eyes,
quick and sardonic; a thin mouth with a half-smile lifting one corner. Short,
straight, neat black hair. A thin, new black moustache and nothing else.
Olive skin. Chin up, weight on one hip, arms folded. Keep this exact narrow
face, cheekbones, eyes, and moustache in every view.

In views (a), (b), and (c) he wears brand-new bright mail and a surcoat
quartered black and yellow, belted, with a sword at his hip and new boots.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression amused and superior.

View (b): full length from the front, weight on one hip, arms folded.

View (c): a true ninety-degree profile in the same light, showing the thin
straight nose, sharp cheekbone, and pointed chin.

View (d): the same young man as the king's steward, full length: a long black
wool tunic with a yellow border at hem and cuffs, a ring of keys at the belt,
no mail, no sword.

He must never be confused with Arthur: Kay is black-haired, sharp, older, with
a moustache; Arthur is a blond, round-faced, freckled, beardless boy.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — LOT

A 1536 × 1024 landscape character reference sheet with four views of one man
of about forty, left to right, on a plain warm-umber-toned canvas ground. No
words, labels, borders between views, or scenery.

King Lot of Orkney is big and heavy-shouldered, a powerful man going thick at
the waist. A broad, square, weathered face; a strong flat nose; pale blue
eyes, hooded and contemptuous, under a heavy brow. Long copper-red hair to the
shoulders and a long copper-red beard plaited into two thick braids, each
bound with iron rings. Head back, looking down his nose. Keep this exact
square face, pale eyes, and the two red braids in every view.

In views (a), (b), and (c) he wears a heavy black bearskin cloak over a coat of
dark iron scale mail, a thick twisted gold torc around his neck, and a plain
iron crown. A broadsword at his hip.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression mocking.

View (b): full length from the front, head back, laughing with his whole
chest, one hand on his sword hilt.

View (c): a true ninety-degree profile in the same light, showing the flat
nose, the heavy brow, and a braid hanging down the chest.

View (d): the same man ready for battle, visibly mounted, keeping his big
heavy-shouldered, thick-waisted build and head-back posture readable in the
saddle: a round iron helmet with a nose-guard over the red hair, copper-red
braids hanging below it, the bearskin cloak thrown back, broadsword raised.
The rider and mount must read together at thumbnail scale.

He must never be confused with Pellinore: red braids, gold torc, and black fur
against iron-grey cropped hair, square grey beard, and faded green.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — PELLINORE

A 1536 × 1024 landscape character reference sheet with four views of one man
of about fifty, left to right, on a plain warm-umber-toned canvas ground. No
words, labels, borders between views, or scenery.

King Pellinore is enormous, the tallest and widest man in the story, built
like a bear. A long, heavy, horse-like face with a big lantern jaw; a pale
scar across the left cheek; small grey eyes; a nose broken more than once.
Iron-grey hair cropped close to the skull. A short, thick, square-cut
iron-grey beard. Very still. Keep this exact long heavy face, scar, cropped
hair, and square beard in every view.

In views (a), (b), and (c) he wears old, dented, black-painted plate-and-mail
armour, worn at the edges, under a faded green surcoat with a white boar on
the chest, and stands with both hands resting on the pommel of a huge sword
planted point-down in front of him. No helmet.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression grave and patient.

View (b): full length from the front, both hands on the planted sword,
feet apart, enormous.

View (c): a true ninety-degree profile in the same light, showing the long
lantern jaw, broken nose, and square beard.

View (d): the same man in full armour with a flat-topped iron great helm
covering his head, a narrow eye-slit, a battered green-and-white shield on his
arm, the huge sword raised.

He must never be confused with Merlin (thin, stooped, long forked white beard,
wild hair), Ector (short, bald, clean-shaven), or Lot (red braids, gold torc,
black fur). Pellinore is no villain: grave, not cruel.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — LADY OF THE LAKE

A 1536 × 1024 landscape character reference sheet with four views of one
woman, left to right, on a plain cool-grey-toned canvas ground. No words,
labels, borders between views, or scenery.

The Lady of the Lake is tall, upright, and perfectly still, ageless. A long
pale oval face with a high forehead; calm grey eyes; a straight narrow nose;
a closed, unsmiling mouth. Very long, straight, black hair, wet and heavy,
falling to her knees. Pale skin with a faint cool tint. Hands folded in front
of her. Keep this exact face and hair in every view.

In views (a), (b), and (c) she wears a plain long gown of white samite, heavy
and faintly shimmering, wet and darker at the hem, long sleeves, and a thin
silver circlet on her brow. Bare feet. No other jewellery.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression calm and unreadable.

View (b): full length from the front, upright, hands folded.

View (c): a true ninety-degree profile in the same light, showing the high
forehead, straight nose, and the long black hair down her back.

View (d): the same woman full length, standing on the surface of still grey
water as if on a floor, rings of ripple spreading from her bare feet, white
mist around her.

No other woman in the book wears white.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — UTHER

A 1536 × 1024 landscape character reference sheet with four views of one old
man of about sixty who is dying, left to right, on a plain warm-umber-toned
canvas ground. No words, labels, borders between views, or scenery.

King Uther is gaunt and hollow-cheeked, the bones of his face showing. Sunken
dark eyes; a high-bridged straight nose; a long drooping grey moustache that
hangs past his chin, and no beard at all — the chin and jaw are bare. Long,
thin, straight grey hair. Keep this exact gaunt face, moustache without beard,
and long thin hair in every view.

In views (a), (b), and (c) he wears a long dark-red wool nightrobe with a
gold border and a red-gold dragon brooch at the shoulder.

View (a): a large three-quarter head-and-shoulders portrait in flat even
light. Expression exhausted, urgent.

View (b): full length, standing with difficulty, one hand on a bedpost.

View (c): a true ninety-degree profile in the same light, showing the
high-bridged nose and the moustache hanging past the bare chin.

View (d): the same man lying in a great carved bed, propped on pillows, his
grey hair spread on them, under a heavy red-and-gold coverlet embroidered with
a large red dragon, one hand reaching out.

He must never be confused with Merlin: Uther has a moustache and no beard;
Merlin has a long forked white beard and wild hair.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board prompts (critic-only rasters, generated from the two attached approved sheets)

- **adversarial-merlin-pellinore.** One unframed 1536 × 1024 landscape reference board on a plain warm-umber-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two men from the attached approved sheets full length, side by side on one floor line at one scale: Merlin very tall, very thin, and stooped in his dark grey-green robe; Pellinore enormous and broad in dented black armour and faded green. On the right two-thirds, four matched costume-free head pairs in a clean two-by-two field with open ground between them, every crop ending at the jaw and upper neck with the full length of each beard: a neutral three-quarter pair with closed mouths; the same pair in a shared reaction of anger; strict profiles with both noses pointing screen right; the same profiles in pure grayscale. Merlin keeps his long narrow lined face, great hooked nose, deep-set black eyes, wild white hair, and long white beard forked into two points; Pellinore keeps his long heavy lantern-jawed face, cheek scar, small grey eyes, broken nose, cropped iron-grey hair, and short square-cut grey beard.
- **adversarial-merlin-ector.** One unframed 1536 × 1024 landscape reference board on a plain warm-umber-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two men full length side by side on one floor line at one scale: Merlin very tall, thin, stooped, in his robe; Ector short, broad, barrel-bodied, in his russet tunic, thumbs in his belt. On the right two-thirds, four matched costume-free head pairs, crops ending at the jaw and upper neck with the full beard: neutral three-quarter with closed mouths; the same pair laughing; strict profiles screen right; the same profiles in pure grayscale. Merlin's long narrow face, hooked nose, wild white hair, forked white beard; Ector's big round bald head with a grey fringe, round ruddy jowled clean-shaven face, broken flat nose, bushy grey brows.
- **adversarial-ector-pellinore.** One unframed 1536 × 1024 landscape reference board on a plain warm-umber-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two men full length side by side at one scale: Ector short and barrel-bodied in russet; Pellinore a head and a half taller and far broader in dented black armour and faded green. On the right two-thirds, four matched costume-free head pairs, crops ending at the jaw: neutral three-quarter with closed mouths; the same pair grieving; strict profiles screen right; the same profiles in pure grayscale. Ector bald on top, round face, clean-shaven jowls; Pellinore cropped grey hair, long lantern-jawed face, cheek scar, square grey beard.
- **adversarial-arthur-kay.** One unframed 1536 × 1024 landscape reference board on a plain warm-umber-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two young men full length side by side on one floor line at one scale: Arthur slighter and shorter in mail and deep-blue surcoat; Kay taller and lean in mail and black-and-yellow, arms folded. On the right two-thirds, four matched costume-free head pairs, crops ending at the jaw and upper neck: neutral three-quarter with closed mouths; the same pair shouting; strict profiles screen right; the same profiles in pure grayscale. Arthur's oval soft-jawed beardless boy's face, freckles, wide-set grey-green eyes, thick uneven straw-blond hair over the brow; Kay's narrow face, high sharp cheekbones, pointed chin, narrow dark eyes, thin black moustache, short neat black hair.
- **adversarial-lot-pellinore.** One unframed 1536 × 1024 landscape reference board on a plain warm-umber-toned canvas ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two kings full length side by side at one scale: Lot big and heavy in black bearskin, scale mail, gold torc, iron crown; Pellinore taller and broader still in dented black armour and faded green with a white boar. On the right two-thirds, four matched head pairs with crowns and helmets removed, crops ending at the jaw with the full beard: neutral three-quarter with closed mouths; the same pair sneering; strict profiles screen right; the same profiles in pure grayscale. Lot's broad square face, flat nose, hooded pale eyes, long copper-red hair and beard in two iron-ringed braids; Pellinore's long lantern-jawed face, scar, cropped grey hair, short square grey beard.
- **live-pair-arthur-kay.** One unframed 1536 × 1024 landscape board, unlettered, at story-page scale, in the register: a snowy churchyard in pale winter light. Arthur, from the attached sheet, in his patched brown farm tunic, standing left, gripping Kay's forearm in a knight's grip; Kay, from the attached sheet, in mail and black-and-yellow, standing right, gripping back, red in the face, half-smiling. Their faces three-quarter, each large enough to read at reduced size. No other figures in the foreground. Regenerate the board with a completely clean full-bleed lower-right edge and no letters, glyphs, signature, watermark, caption, label, or border anywhere; preserve Arthur's short freckled round face and shaggy light hair, Kay's long sharp moustached face and compact black hair, and the present opposed three-quarter staging.

## Plate prompts (generation inputs to the pages named)

- **set-chronicle.** One 1536 × 1024 landscape plate showing the Chronicle register, three studies feathering into one continuous warm ivory vellum ground with no rules, boxes, or borders between them: a page of an old manuscript chronicle on warm ivory vellum, with a ruled brown ink margin, faint ruled lines, and in its upper left corner an empty square frame for an illuminated initial painted in vermilion red and lapis blue with a touch of raised gold leaf and vine tendrils, the frame left empty, the page otherwise blank; a hand-drawn map of the island of Britain in iron-gall brown ink with soft watercolour washes of green for hills and pale blue for the sea, straight thin red lines for roads, a wall drawn across the north, a few small ships with square sails off the east coast, no words or letters anywhere on it; and a study of one unsheathed sword only: the sword from the stone, with a long dull iron-grey blade, straight dark-iron cross-guard, worn brown leather grip, and round iron pommel, with no scabbard, belt, buckle, oak sprig, or rock. Render the sword study in fine iron-gall brown line, hatching, and restrained transparent wash so it belongs to the Chronicle register rather than reading as a third full-colour weapon lock. This plate replaces the oil register: it is pen, brown ink, and transparent watercolour wash on vellum, with fine hatching. No figures, no lettering, no letters inside the initial frame, no pseudo-writing.
- **set-cliff-chamber.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with open space between them and no dividing rule: a black stone castle high on a sea cliff at night in a storm, one window lit, slanting rain, white waves bursting on the rocks below, a narrow switchback path cut into the cliff face; and a dark stone royal bedchamber lit by one bronze brazier, a great carved bed with heavy red-and-gold hangings and a red-and-gold coverlet embroidered with a large red dragon, shadows crowding the room. No figures, no lettering.
- **set-ector-farm.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: a small manor farm in late autumn, a timber-and-stone house, a muddy yard with puddles and straw, a stable door, a wooden mounting block, a wattle gate, and an open-fronted forge shed with a glowing fire, an anvil block, and tools; and the same forge shed at night, the fire burned down to red coals, an anvil block and a sack of grain beside it, warm light on the timber walls. No figures, no animals, no lettering.
- **set-london.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: an enormous old city wall of grey squared stone with horizontal bands of thin red Roman brick, crumbling in places, a great arched gate, and behind it a crowd of steep medieval roofs, smoke, church towers, and plain banners in muted rust, ochre, dull green, and iron grey (no blue banners or blue cloth anywhere; deep blue is reserved for one character), all in falling snow under a white sky; and a narrow empty snowy street of timber-framed houses with every shutter closed, a heavy locked oak inn door with iron studs and no sign, and at the end of the street the square tower of a stone church over the roofs. No figures, no animals, no lettering, no inn sign.
- **set-churchyard-stone.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: a snowy churchyard in pale winter light before a squat, old stone church with a round-arched door, snow on low gravestones, and in the middle a great rough block of grey stone as high as a man's waist with a black iron anvil on top and a long plain sword with a dark iron cross-guard and round pommel driven down through the anvil into the stone, the front face of the stone carved smooth and left completely blank; and the cold interior of the same church at night, round stone arches, a plain wooden bench, a single candle, a high window letting in snow-light. No figures, no lettering anywhere, no carved letters on the stone.
- **set-tournament.** One unframed 1536 × 1024 landscape setting plate, one view: a bright snowy tournament field outside a lower, clearly Roman grey-stone city wall articulated by unmistakable horizontal red-brick bands, with medieval roofs visibly abutting or built against that wall, ringed with striped round tents in weathered rust-and-cream, dull green-and-cream, and ochre-and-cream (no blue anywhere on the plate; deep blue is reserved for one character), long wooden spectators' stands hung with plain cloths in muted oak brown, weathered rust, dull ochre, and dull green, a wooden barrier down the middle of the field, plain unlettered banners on tall poles in the same muted colours, trodden snow, a low winter sun. No figures, no horses, no lettering, no emblems.
- **set-great-hall-london.** One unframed 1536 × 1024 landscape setting plate, one view: a long stone feasting hall at night lit by torches in iron brackets, long trestle tables with benches running down both sides, a raised high table across the far end with a tall carved chair in the middle, a great pair of oak doors at the near end standing open, painted beams overhead, rushes on the floor. No figures, no lettering, no heraldry, and no signature, monogram, or mark of any kind on the floor, threshold, or in any corner. Remove every large isolated tree/tree-of-life device from the side hangings and far-wall tapestry. Replace those fields with low-contrast, unfigured woven cloth in dull green, oak brown, and muted ochre; any retained beam decoration must remain a continuous non-emblematic vine border rather than an isolated badge. Remove that fireplace opening and continue the far wall and dais in plain stone and oak. Keep London identified by the long stone nave, painted beams, paired side tables, raised high table, open near-end oak doors, rush floor, and iron-bracket torchlight; do not introduce another central architectural fire feature.
- **set-bedegraine.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: a forest valley at dawn, frost on the grass, two long open slopes facing each other across a shallow stream with white mist lying along it, dark forest on the ridges, a low gold sun behind the near slope; and the same valley at noon under a grey sky with the mist gone, the near slope strewn with dropped round and kite shields, broken spears, a torn plain banner lying in the stream, crows on the far ridge. No figures, no horses, no bodies, no blood, no lettering.
- **set-camelot.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: a castle of pale cream stone with round towers on a green hill above a winding river, a road climbing to its gate, plain banners flying, spring light; and the interior of its great hall: a high timber roof with dark oak beams, tall arched windows, a great stone hearth with a round iron-bound shield hanging above it, torches, and a long rectangular oak table with benches down the middle of the floor and a carved chair at its head. Remove every deep-blue/ultramarine pennant and hanging from both views. Repaint the exterior pennants and interior wall hangings in muted oak brown, weathered rust, iron grey, or dull ochre, with no blue large enough to read at thumbnail scale. Deep ultramarine must remain exclusive to Arthur. No figures, no lettering, no heraldic devices.
- **set-forest-fountain.** One unframed 1536 × 1024 landscape setting plate, two studies feathering into one continuous ground with no dividing rule: an old oak forest at night in cool silver-blue moonlight, a pale road winding between huge trunks; and a clearing in that forest with a plain, battered medieval stone fountain with a nonfigurative central spout spilling into a round pool that holds the moon's reflection, a battered round pavilion of faded green-and-white striped cloth readable by moonlight rather than by a second warm focal source, and the same single large kite-shaped shield locked on `06-pellinore` hanging from a low oak branch: battered faded green field, white boar device, and no alternate heraldry or shield geometry. The moon's reflection in the fountain pool is the brightest and only dramatic accent. No campfire, orange cast light, or warm interior lamp. Remove all carved human, bearded, or beast faces. No figures, no horses, no lettering.
- **set-lake.** One unframed 1536 × 1024 landscape setting plate, one view: a very wide lake, still as glass, under thick white mist, tall reeds in the foreground, a small plain wooden rowing boat drawn up at the pebbled shore, far hills faded to silver-grey. The colours are cold silver, grey, and white only. Repaint every warm foreground mass into a tightly cold range: reeds in desaturated charcoal-grey, boat in weathered silver-grey, and shore and rocks in blue-grey and neutral grey. Preserve the boat's plain construction and the existing reed/boat silhouettes, but remove all readable brown, ochre, yellow, rust, and olive colour groups, including at thumbnail scale. Remove the circular disk as a readable object and replace it with diffuse white cloud light of nearly uniform value, leaving the future white-silk arm as the only localized dramatic accent in lake scenes. No figures, no hand or arm in the water, no sword, no lettering.
- **obj-swords.** One unframed 1536 × 1024 landscape object plate on a plain warm-umber-toned canvas ground, four items at one scale with open ground between them, no hands, no figures, no lettering: the sword from the stone, whole — a long plain sword with a dull iron-grey blade, a straight dark iron cross-guard, a worn brown leather grip, and a round iron pommel; the same sword snapped in two, the hilt with a short jagged stub of blade and the long broken half lying beside it; Excalibur drawn — a longer sword with a bright polished blade, a grip wound with gold wire, and a single green stone set in the centre of its cross-guard; and Excalibur's scabbard — dark red leather chased with fine gold work, with its belt.
- **obj-round-table.** One unframed 1536 × 1024 landscape object plate, two studies feathering into one continuous dark earth-toned ground with no border, frame, gutter, or light seam: seen from high above in a great timber hall, an enormous round table of pale oak with a wide plain rim, ringed with about twenty-four tall carved oak chairs, every chair the same height; retain a gold dash at every chair station but one; at exactly one chair station, leave a clean bare pale-oak interval at least one neighboring dash wide; and align that same bare station with one chair visibly isolated by a narrow shaft of moonlight in the floor-level study; flank it with visible gold-marked neighboring stations so the absence reads immediately at thumbnail and after long re-entry; and the same table at night from floor level, moonlight from high windows lying across it. Replace the central roundel with uninterrupted pale-oak boards and replace every rug and hanging with unfigured, low-contrast earth-colour fields. The wide plain oak rim, short gold dashes, and one bare station must be the plate's only recurring graphic markers. No figures, no lettering, no legible names, no pseudo-writing.
