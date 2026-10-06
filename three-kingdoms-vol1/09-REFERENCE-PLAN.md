# Reference Plan — approved as a system

**Nothing generates a page until every character visibly on that page has an
approved permanent lock.** Not just-in-time. Locks live in `refs/approved/` and
get there only through `tools/refs.py promote` with an independent critic
report. A sheet in `refs/candidates/` is not a lock.

## Canvas and register — for every sheet

Reference sheets are **1536 × 1024 landscape**; story pages are portrait. This
is not an inconsistency: four views across a wide canvas is what a lock needs.

**Register, verbatim in every generative sheet prompt:**

> **Lacquer and Dust.** Bold, wet brush-and-ink line on warm, toothed
> mulberry paper, with flat matte washes of earth and mineral pigment:
> lamp-black ink, raw umber, loess yellow-ochre and dust grey for the land;
> and, laid flat and strong where people and banners carry them, cinnabar
> vermilion, malachite green, indigo, imperial purple, ivory, and the dull
> bronze and iron of armor. Late-Han China lit like a war film: hard white
> noon and long dust, smoke-orange firelight, brazier light in lacquered
> halls with real cast shadows and real depth, cold blue dawn. Visible brush
> line, visible paper tooth, ink and wash pooling at the edges of a stroke;
> lamellar iron, lacquered leather, hemp, silk, horsehair, rammed earth, grey
> tile, steel. Not smooth prestige-oil realism. No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no anime
> proportions, no children's-book softness, no plastic 3D render, no
> blue-green landscape-scroll prettiness, no gold leaf.

Every character sheet closes with the anti-collision clause, verbatim:

> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.

**No sheet carries lettering of any kind** — no name plates, no labels, no
calligraphy, no seal stamps. Labelled sheets teach the page model to letter
the art.

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
| 01 | `01-liu-bei` — iron lamellar over a white robe, white cloak, two swords crossed at his back; view (d) the faded hemp robe and straw sandals of the market | character | 2 | p 2 | new |
| 02 | `02-guan-yu` — dark green robe over dark lamellar, green headscarf, the Green Dragon blade; view (d) the tavern state: green robe and headscarf, no armor, no glaive, beard loose to the belt | character | 4 | p 4 | new |
| 03 | `03-zhang-fei` — black lamellar, black cloak, the serpent spear; view (d) the butcher's leather apron, sleeves rolled | character | 3 | p 3 | new |
| 04 | `04-cao-cao` — dark indigo lacquered armor, black cloak; view (d) indigo court robe and small black official's cap | character | 12 | p 12 | new |
| 05 | `05-dong-zhuo` — dark purple and gold brocade robes, gold-ornamented cap, food in hand; view (d) gilded armor straining over the belly, helmet crooked | character | 13 | p 13 | new |
| 06 | `06-lu-bu` — gold-and-bronze armor, vermilion cloak and war-robe, two long pheasant plumes, the halberd; view (d) before Dong Zhuo's gift: dark bronze armor, same plumes and vermilion | character | 18 | p 18 | new |
| 07 | `07-yuan-shao` — ivory and pale-gold silk court robes, tall black lacquered hat; view (d) gilded scale armor under an ivory cloak, hatless | character | 17 | p 17 | new |
| 08 | `08-uncle` — brown and russet farmer's cotton, straw hat on his back; view (d) riding a grey donkey with a wine jar and a basket of fruit | character | 25 | p 25 | new |
| — | `board-heads` — all eight, crop-and-place of each sheet's view (a); a pixel-identity check, not an expression-neutral one (that is `adversarial-heads-neutral-1` and `-2`) | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — all eight, full length | board | — | — | from approved sheets |
| — | `adversarial-liu-bei-cao-cao` — same light, three-quarter and profile, costume-free crops, grayscale pass | board | — | — | `01-liu-bei` `04-cao-cao` |
| — | `adversarial-guan-yu-lu-bu` — the two giants, full length side by side and costume-free head pairs, grayscale pass | board | — | — | `02-guan-yu` `06-lu-bu` |
| — | `adversarial-dong-zhuo-yuan-shao` — the two great lords, head pairs, grayscale pass | board | — | — | `05-dong-zhuo` `07-yuan-shao` |
| — | `adversarial-zhang-fei-dong-zhuo` — the two heavy men, full length and head pairs, grayscale pass | board | — | — | `03-zhang-fei` `05-dong-zhuo` |
| — | `adversarial-yuan-shao-uncle` — the two older bearded men, full length and costume-free head pairs, grayscale pass | board | — | — | `07-yuan-shao` `08-uncle` |
| — | `adversarial-liu-bei-yuan-shao` — the two lords of the brothers' humiliation, full length and costume-free head pairs, grayscale pass | board | — | — | `01-liu-bei` `07-yuan-shao` |
| — | `adversarial-heads-neutral-1` — Liu Bei, Guan Yu, Zhang Fei, Cao Cao: one angle, one light, closed-mouth resting faces (the expression-neutral companion to the crop board) | board | — | — | `01-liu-bei` `02-guan-yu` `03-zhang-fei` `04-cao-cao` |
| — | `adversarial-heads-neutral-2` — Dong Zhuo, Lü Bu, Yuan Shao, Uncle: one angle, one light, closed-mouth resting faces | board | — | — | `05-dong-zhuo` `06-lu-bu` `07-yuan-shao` `08-uncle` |
| — | `live-pair-liu-bei-cao-cao` — unlettered, page scale, the p 47 staging: the two seated side by side by a fire at dusk, Cao Cao leaning in with a cup | board | — | — | `01-liu-bei` `04-cao-cao` |
| — | `set-zhuo-market` — the dusty market street under a grey tile gate, the wall with a blank pale notice, the sandal stall; the low-beamed tavern interior | set | 2 | p 2 | — |
| — | `set-peach-garden` — Zhang Fei's rammed-earth farm courtyard at night with a fire; the walled peach garden in full blossom at morning; the same garden in green leaf | set | 5 | p 5 | — |
| — | `set-ridge-valley` — a bare ridge above a dust-yellow plain; the narrow valley between two scrubby hills | set | 8 | p 8 | — |
| — | `set-grass-plain` — a plain of tall dry grass with a rebel tent camp at night; the same plain burning; black stubble and smoke at grey dawn | set | 10 | p 10 | — |
| — | `set-imperial-camp` — a hillside of trampled imperial banners; a general's tent with flaps and guards' posts | set | 13 | p 13 | — |
| — | `set-palace` — the capital's grey roofs and the palace on its high platform with the long white stair; the throne hall of red lacquer columns, black floor, braziers, and the vast gold throne | set | 16 | p 16 | — |
| — | `set-banquet-stable` — the banquet hall with low tables and lamps; a palace stable at night lit by one lantern | set | 18 | p 18 | — |
| — | `set-bedchamber` — the imperial bedchamber with silk curtains and a wide couch, and a round bronze mirror on a stand facing the couch | set | 21 | p 21 | — |
| — | `set-farmhouse-road` — a modest farm gate and courtyard at dusk; a small kitchen at grey dawn; the road between willows and yellow fields | set | 25 | p 25 | — |
| — | `set-coalition-camp` — the mountain valley of tents and many-coloured banners with the fortress gate filling the pass at its head; the brothers' small tent by a fire at the camp's edge | set | 30 | p 30 | — |
| — | `set-great-tent` — the long table of the lords inside a great tent, with the entrance flap open onto the plain | set | 31 | p 31 | — |
| — | `set-hulao-gate` — the fortress gate from the plain: massive gate tower, studded doors, walls climbing the slopes; the battlements at night with purple banners | set | 34 | p 34 | — |
| — | `obj-weapons` — the Green Dragon crescent blade, the serpent spear, Liu Bei's two matching straight swords in their crossed back-scabbards, Lü Bu's crescent-bladed halberd | object | 7 | p 7 | — |
| — | `obj-red-hare` — Red Hare, the huge blood-red horse with a darker mane, saddled and bare | object | 19 | p 19 | — |
| — | `obj-small-things` — the Seven-Star dagger in and out of its scabbard; the bronze tiger seal of command; a plain cup of steaming wine; the champion's dented plumed helmet; a bundle of straw sandals | object | 20 | p 20 | — |

**Generation order:** `01-liu-bei` (he is on more pages than anyone, and the
book's hardest pair runs through him); then `04-cao-cao`, the other half of
that pair; then the giants, `02-guan-yu` and `06-lu-bu`; then the lords,
`05-dong-zhuo` and `07-yuan-shao`; then `03-zhang-fei` and `08-uncle`; then
boards (head and silhouette boards are crop-and-place from approved pixels,
not generations); then adversarial and live-pair boards; then plates in page
order.

## States needed, enumerated from the script

| Character | State | Pages |
|---|---|---|
| Liu Bei | hemp robe, cloth cap, straw sandals (the market) | 2–7, 28–29 |
| Liu Bei | iron lamellar over white robe, white cloak, white headband or cap, two swords crossed at his back, straw sandals in the stirrups | 8–15, 30–49 |
| Liu Bei | the two swords drawn, one in each hand | 43–45 |
| Guan Yu | green robe and headscarf, no armor (the tavern, the oath) | 4–6 |
| Guan Yu | green robe over dark lamellar, the Green Dragon blade | 7–15, 29–49 |
| Zhang Fei | butcher's leather apron over a dark tunic | 3–6 |
| Zhang Fei | black lamellar, black cloak, the serpent spear, a black horse | 7–15, 29–49 |
| Cao Cao | dark indigo lacquered armor, black cloak | 12, 24, 28, 30–49 |
| Cao Cao | indigo court robe, small black cap, the jeweled dagger in his sleeve | 18, 20–23 |
| Cao Cao | dusty, hollow-eyed, on the run, the court robe travel-stained | 24–27 |
| Dong Zhuo | gilded armor straining, helmet crooked (the field) | 13–14 |
| Dong Zhuo | purple and gold robes, gold cap (the capital, the wall) | 15–24, 37 |
| Lü Bu | dark bronze armor, vermilion war-robe, plumes, halberd | 18–19 |
| Lü Bu | gold-and-bronze armor, vermilion cloak, plumes, halberd, on Red Hare | 20–49 |
| Yuan Shao | ivory and gold silk, tall black hat | 17, 30–35 |
| Yuan Shao | gilded scale armor, ivory cloak, hat on; then hatless and muddy | 39–40, 43 |
| Uncle | brown farmer's cotton; on a grey donkey with a jar | 25, 27 |

## Nearest lookalikes and what carries the separation

Carried from `04-CHARACTER-LEDGER.md`; the sheet prompt for each names its
lookalike and the differentiators that must survive grayscale and thumbnail.

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 Liu Bei | 04 Cao Cao; 07 Yuan Shao | tall vs short; broad compact oval face vs narrow angular; sad almond eyes vs narrow glittering; long earlobes; clean rounded chin vs pointed goatee; white vs indigo. Young vs forty-five; moustache-only clean chin vs long three-strand beard; cloth cap vs tall black hat |
| 02 Guan Yu | 06 Lü Bu | red face vs pale; beard to the belt vs clean-shaven; massive vs lean; green headscarf vs pheasant plumes; green vs vermilion |
| 03 Zhang Fei | 05 Dong Zhuo | young hard bulk vs old soft fat; round bulging eyes and bristling cheek whiskers vs small sunk eyes and a drooping thin moustache; black armor vs purple silk |
| 04 Cao Cao | 01 Liu Bei | as above, inverted; short, quick, chin forward, one eyebrow up |
| 05 Dong Zhuo | 07 Yuan Shao; 03 Zhang Fei | obese vs thin; jowls vs long narrow face; gold cap vs tall black hat; purple vs ivory |
| 06 Lü Bu | 02 Guan Yu | as above, inverted; the only beardless grown warrior |
| 07 Yuan Shao | 05 Dong Zhuo; 08 Uncle | thin, tall-hatted, three-strand black beard vs obese; vs bald, white-bearded, bent, in brown cotton |
| 08 Uncle | 07 Yuan Shao | as above, inverted |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`). Yellow Turbans wear yellow headbands over
  plain brown and grey; never a red face, never a long beard, never
  pheasant plumes. Coalition lords other than Yuan Shao wear dull bronze and
  brown, are never in close-up, never wear ivory, purple, indigo, green,
  vermilion, or a tall black hat. Dong Zhuo's soldiers wear dull iron under
  purple banners. The boy emperor is a small figure in imperial yellow robes
  on a vast throne. The deposed emperor is a young man in yellow robes, seen
  once. The old lord behind whom Lü Bu stands is in grey, white-haired, face
  never close. The champion at the gate is a dark rider in a plumed helmet
  seen only at a distance. The farmhouse family is an old woman and a young
  man in brown, seen once alive in a doorway. No background man has a red
  face, long earlobes, or two long pheasant plumes.
- A rejected sheet never becomes a lock and never becomes an input.
- **Art notes carried from the script gate:** Liu Bei's swords stay sheathed
  at his back until p 43; Cao Cao's separate hill on p 39 must be a clear,
  readable placement apart from the gold banner; on p 47 Liu Bei refuses the
  cup in panel 1 and is holding it in panel 4; on p 26 the young man holds a
  knife, the whetstone is in the kitchen; the oath on p 6 is spoken by Liu Bei
  for all three.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas: **(a)** three-
quarter head and shoulders, neutral expression, even light; **(b)** full-length
standing figure, default costume, habitual posture; **(c)** strict profile, same
light; **(d)** the one state the script actually needs.

## 01 — LIU BEI

A 1536 × 1024 landscape character reference sheet with four views of one
twenty-eight-year-old man on a plain warm-paper ground. No words, labels,
seals, borders, or scenery.

Liu Bei is a poor sandal-seller who carries himself like a prince. He is tall
and slim, with a long neck and narrow, sloping shoulders. His face is a broad,
compact oval: high clear brow, full cheeks, full lower jaw, and a short,
bluntly rounded chin. His pale skin is smooth. Gentle, slightly downturned
almond eyes look sad even when he smiles. A straight medium nose and small
mouth sit above a thin, neat black moustache. The skin beneath his lower lip
and across his rounded chin and jaw is completely clean-shaven. His unusually
long, heavy earlobes hang almost to the jaw line. Black hair is tied in a
plain topknot. Keep this exact head, jaw, clean chin, eye shape, and ear length
in every view.

In views (a), (b), and (c), he wears plain dark iron lamellar over a white
robe with modest, unbulky sleeves, a white cloak, a plain white cloth headband,
and straw sandals. Two matching straight swords remain sheathed in plain black
scabbards crossed high on his back, with both hilts above his shoulders.

View (a): a large three-quarter head-and-shoulders portrait in flat even light,
showing both the broad rounded lower face and the full length of the near
earlobe. His expression is courteous and restrained, with private ambition in
the eyes.

View (b): full length from the front, upright and slim, head only slightly
bowed, hands folded low inside the sleeves below the belt. The narrow shoulders,
long neck, dark armored core, white outer cloth, crossed sword hilts, and straw
sandals make one clear silhouette.

View (c): a strict ninety-degree head-and-shoulders profile in the same flat
light. Show the high brow, straight nose, short rounded chin, bare jaw, thin
moustache, and long heavy earlobe without changing their proportions.

View (d): the same man full length as a market sandal-seller, standing nearly
upright in a small courteous bow. He wears a faded undyed hemp robe patched at
the elbows, a plain dark cloth cap, and straw sandals. A bamboo pole rests over
one shoulder with bundles of straw sandals hanging from it. No armor or swords.
Keep the tall slim torso, narrow shoulders, broad compact face, clean rounded
chin, downturned eyes, and long earlobes identical to the other views.

At thumbnail size Liu Bei is the tall, slim man with the broad gentle face,
long earlobes, clean rounded chin, and white outer clothing. Cao Cao is short
and compact, narrow-faced, sharp-eyed, indigo-clad, and has a pointed goatee.
Yuan Shao is older and wears a long three-strand beard and tall black hat.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — GUAN YU

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Guan Yu, about thirty, a fugitive and a giant: the tallest of the three
brothers by a head, with massive shoulders, a long torso, and a still,
upright bearing; he never hurries. A deep red, date-coloured face, the colour
of the skin itself and not a flush: the only red face in the book. Long
narrow phoenix eyes that tilt upward at the outer corners, usually
half-lidded. Heavy, straight, dark brows like silkworms. A long straight nose.
A long, glossy black beard that falls in a single smooth sheet to his belt,
joined by a long moustache. Hair under a dark green cloth headscarf. Habitual
gesture: stroking the beard downward with one hand. Expression at rest:
proud, grave, final.

Default costume, views (a), (b), (c): a dark green robe worn over dark iron
lamellar armor, the green headscarf, dark boots; in his right hand the Green
Dragon blade: a long-handled glaive with a broad crescent blade and a
dragon worked at its base, butt on the ground, taller than he is.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the deep red face, the upturned phoenix eyes, the silkworm
brows, and the single sheet of black beard.

View (b): full length, standing very straight, the glaive upright beside him,
the other hand stroking the beard downward.

View (c): a true ninety-degree profile from headscarf to boots, same light,
keeping the red face, the long straight nose, the beard to the belt, and the
height.

Views (a)–(c) have no scenery and no props beyond the glaive.

Remove the secondary weapon and its tasselled fitting from every view. Keep a
plain belt closure and the Green Dragon Crescent Blade as Guan Yu's only
weapon/prop.

View (d): the same man as he first walks into the tavern, before he has any
armor: the dark green robe belted plainly over trousers, the green headscarf,
no lamellar, no glaive in hand; the long black beard loose and falling in its
single smooth sheet to his belt; standing very straight, one hand stroking the
beard downward. The beard is never bagged, tied, or shortened in any view.

Guan Yu must never be confused with Lü Bu. Differentiators that must survive
grayscale and thumbnail: a deep red face against a pale one; a beard to the
belt against a clean-shaven face; massive and long-torsoed against lean and
long-legged; a green headscarf against two long pheasant plumes; green
against vermilion.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — ZHANG FEI

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Zhang Fei, about twenty-five, a butcher. A broad, square, heavy head like a
leopard's; round bulging eyes with white showing all around the iris; thick,
wild eyebrows; a wide flat nose; a big mouth, usually open. Short, black,
bristling whiskers that stand out all around his jaw and cheeks like a
tiger's, and a short spiky moustache: never long, never smooth. Dark,
sun-tanned, ruddy-brown skin. Black hair pulled up roughly, strands escaping.
Short and enormously broad: a barrel chest, a thick neck, arms like hams, a
head shorter than Guan Yu and twice Liu Bei's width. All of it hard muscle,
young. Posture: fists on hips, chest out, or leaning forward ready to
charge. Habitual gesture: head thrown back to laugh or roar. Expression at
rest: delighted and dangerous.

Default costume, views (a), (b), (c): black iron lamellar armor, a black
cloak, black boots; in his hand the serpent spear: a very long spear with a
wavy, snake-shaped blade, much longer than he is tall.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the square head, the round bulging eyes, the wild brows, and
the bristling whiskers all round the jaw and cheeks.

View (b): full length, fists on hips, chest out, feet planted wide, the
serpent spear leaning against his shoulder.

View (c): a true ninety-degree profile from topknot to boots, same light,
keeping the bristling whiskers, the thick neck, the barrel chest, and the
short height.

Views (a)–(c) have no scenery and no props beyond the spear.

View (d): the same man as a market butcher: a heavy leather apron over a dark
tunic, sleeves rolled above the elbows, no armor, no spear; arms folded,
grinning.

Zhang Fei must never be confused with Dong Zhuo. Differentiators that must
survive grayscale and thumbnail: a young man's hard muscle against an old
man's soft fat; round bulging eyes against small eyes sunk in fat; bristling
whiskers all round the jaw and cheeks against a thin drooping moustache;
black armor against purple silk. He must never be confused with Guan Yu:
short and broad against towering; bristling short whiskers against a long
smooth beard; ruddy-brown against deep red.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — CAO CAO

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Cao Cao, about thirty, an imperial officer. Short: a head shorter than Liu
Bei, compact and quick. A narrow, angular face with sharp cheekbones and a
pointed chin. Narrow, slanted, glittering eyes under thin arched brows, one
brow often raised; the eyes are always amused. A slightly hooked nose. A
neatly trimmed black moustache and a short, pointed, precise black goatee.
Black hair in a tight topknot. Posture: weight on one hip, head tilted, chin
forward. Habitual gesture: a cup held in one hand, or one finger raised as he
makes a point. Expression at rest: amused, measuring.

Default costume, views (a), (b), (c): dark indigo lacquered lamellar armor,
a black cloak, a black topknot cover, black boots, a plain sword at his hip.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the narrow angular face, the sharp cheekbones, the narrow
glittering eyes with one brow raised, the hooked nose, and the pointed goatee.

View (b): full length, weight on one hip, head tilted, chin forward, a small
wine cup held in one hand.

View (c): a true ninety-degree profile from topknot to boots, same light,
keeping the pointed chin and goatee, the hooked nose, and the short height.

Views (a)–(c) have no scenery and no props beyond the cup and the sword.

View (d): the same man at court: a dark indigo official's robe with wide
sleeves and a small black official's cap, bowing low with folded hands, and
just showing at the edge of one sleeve the jeweled hilt of a short dagger.

Cao Cao must never be confused with Liu Bei. Differentiators that must
survive grayscale and thumbnail: short and compact against tall and slim; a
narrow angular face against a soft oval one; narrow glittering eyes against
sad almond eyes; ordinary earlobes against long heavy ones; a pointed goatee
against a moustache over a bare, rounded chin; indigo against white.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — DONG ZHUO

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Dong Zhuo, about fifty-five, a general who has taken an empire. Obese: a huge
round belly, heavy jowls, a thick neck that merges with his chin, small eyes
sunk in fat under heavy lids, a fleshy nose, a wet, greedy mouth. A thin,
drooping black-and-grey moustache and a few strands of greying beard. Black
and grey hair under a tall cap ornamented with gold. Posture: leaning back,
reclining, swaying when he stands. Habitual gesture: food in one hand, a
drumstick, a fig, a cup. Expression at rest: mocking.

Default costume, views (a), (b), (c): robes of dark imperial purple and gold
brocade, heavy rings on his fingers, the gold-ornamented cap.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the jowls, the sunk small eyes, the fleshy nose, the drooping
thin moustache, and the gold cap.

View (b): full length, leaning back on his heels with his belly forward, a
roast drumstick in one ringed hand.

View (c): a true ninety-degree profile from cap to slippers, same light,
keeping the jowls merging into the neck and the great belly.

Views (a)–(c) have no scenery and no props beyond the food.

View (d): the same man in the field: gilded scale armor straining over the
belly, a gilded helmet knocked crooked, red-faced from exertion, panting.

Dong Zhuo must never be confused with Yuan Shao. Differentiators that must
survive grayscale and thumbnail: obese against thin; heavy jowls against a
long narrow face; a drooping thin moustache against a combed three-strand
beard; a gold cap against a tall black lacquered hat; purple against ivory.
He must never be confused with Zhang Fei: old soft fat against young hard
muscle; sunk small eyes against round bulging ones.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — LÜ BU

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Lü Bu, about thirty, the greatest warrior alive. As tall as a giant, but
long-legged and lean. Handsome and clean-shaven: the only beardless grown
warrior in the book. A long face, high cheekbones, a strong straight jaw, a
pale complexion, thin lips set in a half-smile. Cold, wide-set eyes under
straight brows. Two very long pheasant tail-feathers rise from his gold
headdress and curve back high over his head, so his silhouette is the
tallest in any crowd. Across all four views, both brows are straight,
near-horizontal bars over the same wide-set eyes, with no steep diagonal,
pinch down at the nose, or inward V; preserve the long face, high cheekbones,
clean straight jaw, and thin half-smile. Posture: easy and loose, the halberd rested across one
shoulder, looking down at people. Habitual gesture: a lazy turn of the
halberd; a laugh. Expression at rest: bored, superior.

Default costume, views (a), (b), (c): gold-and-bronze armor with a
beast-face belt plate, a vermilion war-robe and vermilion cloak, the gold
headdress with the two long pheasant plumes; the sky-piercer halberd, a long
halberd with a crescent side-blade.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the long handsome beardless face, the high cheekbones, the
cold wide-set eyes, the thin half-smile, and the base of the plumes.

View (b): full length, standing loose, the halberd across his shoulder, the
two plumes rising and curving back high above the head.

View (c): a true ninety-degree profile from plume-tips to boots, same light,
keeping the clean-shaven jaw and the full curve of the plumes.

Views (a)–(c) have no scenery and no props beyond the halberd.

View (d): the same man before Dong Zhuo bought him: every armor plate and
fitting revalued to dark bronze with no gold, including the chest beast and
belt plate; retain the same vermilion war-robe, the same two long pheasant
plumes, the halberd, the frontal still posture, and all locked facial
structure, standing behind an unseen shoulder and looking straight at the
viewer.

Lü Bu must never be confused with Guan Yu. Differentiators that must survive
grayscale and thumbnail: a pale face against a deep red one; clean-shaven
against a beard to the belt; lean and long-legged against massive; two long
pheasant plumes against a green headscarf; vermilion against green.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — YUAN SHAO

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Yuan Shao, about forty-five, the greatest lord in the empire. Tall, thin, and
stiff-backed. A long, narrow, refined face with a high forehead, a long thin
nose, and a small mouth turned down; hooded eyes looking down that nose. A
long, thin, carefully combed black beard in three strands, one at the chin
and one at each corner of the mouth, reaching his chest, streaked with first
grey. A tall black lacquered official's hat with a flat board on top.
Posture: chin up, shoulders back, hands behind his back or on his sword hilt.
Habitual gesture: smoothing one strand of his beard between two fingers.
Expression at rest: disdain.

Default costume, views (a), (b), (c): ivory and pale-gold silk court robes
with embroidered borders, the tall black lacquered hat, a sword with a gold
hilt.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the long narrow face, the high forehead, the hooded eyes, the
three strands of beard, and the tall hat.

View (b): full length, chin up, one hand smoothing a strand of beard, the
other on the gold sword hilt.

View (c): a true ninety-degree profile from hat-board to slippers, same
light, keeping the long thin nose, the three strands, and the stiff back.

Views (a)–(c) have no scenery and no props beyond the sword.

View (d): the same man in battle, hatless: gilded scale armor under an ivory
cloak, his topknot loose, mud on one side, the three-strand beard
disordered, gripping reins that are not shown.

Yuan Shao must never be confused with Dong Zhuo. Differentiators that must
survive grayscale and thumbnail: thin against obese; a long narrow face
against heavy jowls; a combed three-strand beard against a drooping thin
moustache; a tall black hat against a gold cap; ivory against purple. He must
never be confused with the old farmer: forty-five against sixty-five; a black
three-strand beard against a sparse white one; silk against brown cotton.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — UNCLE

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

An old farmer, about sixty-five, kind and fussy. Thin, small, a little bent.
A round, deeply lined face with crow's feet from smiling and cheeks like
apples. Nearly bald, with a thin white topknot; a sparse white beard and
white eyebrows; one missing tooth in a wide smile. Posture: leaning forward,
arms open. Habitual gesture: both hands spread wide in welcome. Expression at
rest: delighted to see you.

Default costume, views (a), (b), (c): brown and russet farmer's cotton, a
plain sash, cloth shoes, a straw hat hanging on his back by its cord.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the round lined face, the crow's feet, the white topknot, the
sparse white beard, and the gap-toothed smile.

View (b): full length, a little bent, both arms spread wide in welcome.

View (c): a true ninety-degree profile, same light, keeping the bent back,
the white topknot, and the sparse beard.

Views (a)–(c) have no scenery and no props beyond the hat.

View (d): the same old man riding a small grey donkey, a full clay wine jar
under one arm and a basket of fruit on the donkey's back, waving.

He must never be confused with Yuan Shao: bald, white-bearded, small, and
bent in brown cotton against tall, black-bearded, stiff-backed, and
tall-hatted in silk. He must never be confused with Dong Zhuo: thin against
obese.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board prompts (critic-only rasters, generated from the two attached approved sheets)

- **adversarial-liu-bei-cao-cao.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, under flat even light, with no lettering, labels, rules, or props in hand. On the left third, the two men from the attached approved sheets full length, side by side on one floor line and at one scale: Liu Bei a head taller, slim, hands folded in his sleeves, in white; Cao Cao short and compact, weight on one hip, chin forward, in indigo. On the right two-thirds, four matched costume-free head pairs in a clean two-by-two field with open paper between them, every crop ending at the jaw and upper neck: a neutral three-quarter pair; the same pair sharing a sudden laugh; strict profiles with both noses pointing screen right; and the same strict profiles rendered in pure grayscale. Keep the faces identical to the approved sheets in every view: Liu Bei's broad compact oval face, sad downturned almond eyes, long heavy earlobes, thin moustache, clean rounded chin, and bare cheeks and jaw; Cao Cao's narrow angular face, sharp cheekbones, narrow glittering eyes, slightly hooked nose, neat moustache and short pointed goatee, ordinary earlobes.
- **adversarial-guan-yu-lu-bu.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering or labels. On the left third, the two warriors full length side by side on one floor line at one scale, each holding his polearm upright: Guan Yu massive and long-torsoed in green with the beard to his belt; Lü Bu as tall but lean and long-legged in vermilion and gold with the two long pheasant plumes. On the right two-thirds, four costume-free head pairs (headscarf and headdress removed, hair only), crops ending at the jaw: neutral three-quarter; the same pair shouting; strict profiles screen right; the same profiles in pure grayscale. Guan Yu's deep red face, upturned phoenix eyes, silkworm brows and long smooth black beard; Lü Bu's pale clean-shaven long face, high cheekbones, cold wide-set eyes, thin lips.
- **adversarial-dong-zhuo-yuan-shao.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering or labels. On the left third, the two lords full length side by side at one scale: Dong Zhuo obese and leaning back in purple and gold; Yuan Shao tall, thin, and stiff in ivory with the tall black hat. On the right two-thirds, four hat-free head pairs, crops ending at the jaw: neutral three-quarter; the same pair sneering; strict profiles screen right; the same profiles in pure grayscale. Dong Zhuo's heavy jowls, small sunk eyes, fleshy nose, drooping thin moustache; Yuan Shao's long narrow face, high forehead, long thin nose, combed three-strand black beard.
- **adversarial-zhang-fei-dong-zhuo.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering or labels. On the left third, the two heavy men full length side by side at one scale: Zhang Fei short, young, barrel-chested and hard, fists on hips, in black; Dong Zhuo old, obese and soft, leaning back, in purple. On the right two-thirds, four costume-free head pairs, crops ending at the jaw: neutral three-quarter; the same pair laughing; strict profiles screen right; the same profiles in pure grayscale. Zhang Fei's square head, round bulging eyes, wild brows, bristling whiskers all round the jaw and cheeks; Dong Zhuo's jowls, sunk small eyes, drooping thin moustache, greying.
- **adversarial-yuan-shao-uncle.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two men from the attached approved sheets full length, side by side on one floor line at one scale: Yuan Shao tall, thin, and stiff-backed in ivory and gold with the tall black lacquered hat; the old farmer small and a little bent in brown cotton. On the right two-thirds, four matched costume-free head pairs (hats and headwear removed, hair only), crops ending at the jaw and upper neck: a neutral three-quarter pair with closed mouths; the same pair in a shared reaction of surprise; strict profiles with both noses pointing screen right; the same profiles in pure grayscale. Yuan Shao keeps his long narrow high-foreheaded skull, hooded eyes, long thin nose, small down-turned mouth, and three distinct combed black beard strands streaked with first grey; the farmer keeps his short round deeply lined skull, apple cheeks, crow's feet, nearly bald head with a thin white topknot, sparse white beard and brows, and the missing tooth when the mouth opens. No donkey, no basket, no silk, no hat in the head pairs.
- **adversarial-liu-bei-yuan-shao.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering, labels, rules, or props in hand. On the left third, the two men full length side by side on one floor line at one scale: Liu Bei tall and slim in iron lamellar and white cloak, hands folded low; Yuan Shao tall, thin, and stiff-backed in ivory and gold with the tall black hat. On the right two-thirds, four matched costume-free head pairs (headband and hat removed, hair only), crops ending at the jaw and upper neck: a neutral three-quarter pair with closed mouths; the same pair in a shared reaction of anger; strict profiles with both noses pointing screen right; the same profiles in pure grayscale. Liu Bei keeps his broad compact oval face, full untapered lower jaw and short bluntly rounded bare chin, sad downturned almond eyes, unusually long heavy earlobes, and thin moustache only; Yuan Shao keeps his long narrow face, high forehead, hooded eyes, long thin nose, and three distinct combed black beard strands. No swords, no white or ivory cloth in the head pairs.
- **adversarial-heads-neutral-1.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering, labels, rules, or props. Four costume-free heads from the four attached approved sheets in one even row at one head scale, each a true three-quarter view turned the same way, each with a closed mouth and a calm resting expression, crops ending at the upper neck with the full crown, both ears where visible, the whole jaw, and the full length of any beard shown, open paper between them: Liu Bei (broad compact oval, bare rounded chin, thin moustache, long heavy earlobes, sad almond eyes); Guan Yu (deep red face, upturned phoenix eyes, silkworm brows, long smooth black beard to the bottom edge, headscarf removed, hair only); Zhang Fei (square leopard head, round bulging eyes, bristling short whiskers all round jaw and cheeks, mouth closed); Cao Cao (narrow angular face, sharp cheekbones, narrow glittering eyes, slightly hooked nose, neat moustache and short pointed goatee). Faces identical to the sheets.
- **adversarial-heads-neutral-2.** One unframed 1536 × 1024 landscape reference board on a plain warm mulberry-paper ground, flat even light, no lettering, labels, rules, or props. Two matched costume-free head pairs in pure grayscale, each head a true 90-degree profile with a closed mouth and a calm resting expression, crops ending at the upper neck with the full crown, the whole jaw, and the full length of any beard shown, open paper between them. Dong Zhuo and Yuan Shao appear at the same scale and in direct opposition so their profile silhouettes can be compared without costume or colour: preserve Dong Zhuo's short round cranium, projecting jowl, and sparse drooping moustache against Yuan Shao's long narrow facial plane, straighter nose-to-chin line, and three clearly separated beard strands. Yuan Shao and the old farmer appear at the same scale and in direct opposition so their profile silhouettes can be compared without costume or colour: preserve Yuan Shao's full black hairline and long three-strand beard against the old farmer's bald crown, low wispy white side hair, shortened age-collapsed jaw, and sparse white beard. Faces identical to the sheets.
- **live-pair-liu-bei-cao-cao.** One unframed 1536 × 1024 landscape board, unlettered, at story-page scale, in the register: dusk at the edge of an army camp, a small fire. Liu Bei, from the attached sheet, seated left in his armor and white cloak, looking down at a small wine cup held in both hands; Cao Cao, from the attached sheet, seated right and leaning in close, smiling, his own cup raised, his narrow eyes catching the firelight. Their faces three-quarter, each large enough to read at reduced size. No other figures in the foreground.

## Plate prompts (generation inputs to the pages named)

- **set-zhuo-market.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, two views feathering into the common paper with no borders: an unoccupied, dusty market street of a north-China county town under a grey tile gatehouse, stalls and baskets, a rammed-earth wall in shade with a small stall hung with straw sandals beside it and a single pale blank paper notice pasted on the wall with no writing on it; and the empty low-beamed interior of a country tavern, benches, a big clay wine jar, lamplight. A setting plate must contain no figures. Structurally redesign the street as an unoccupied environment: remove every human and animal/cart silhouette from foreground through the gate, rebuild the exposed road, stalls, and distant architecture behind them, and retain the grey-tile gate, empty dusty street, blank pale notice, sandal stall, and empty tavern interior. Do not replace the figures with smaller silhouettes or staffage. No lettering anywhere.
- **set-peach-garden.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, three views feathering together: a rammed-earth farm courtyard at night with a small fire and a bare foreground table, pale blossoming treetops showing over the wall behind; a walled garden of old peach trees in full pink-and-white bloom at morning, petals falling through slanting light, a small low table under the largest tree with incense smoking and three cups; the same old-tree and walled-garden architecture months later with green leaves only—no blossom, falling petals, or visible fruit. The only soft colour in the book. No figures, no lettering. No jug, cup, bowl, steaming drink, or transport vessel anywhere else in the plate.
- **set-ridge-valley.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, two views: from a bare ridge, a dust-yellow plain stretching to the horizon under hard noon; and a narrow valley running toward the viewer between two scrubby hills, clear enough that a reader sees where riders could come down from either side. No figures, no lettering.
- **set-grass-plain.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, with the three states as unframed panoramic vignettes on one continuous warm-paper sheet, with irregular brush-faded edges and open paper separating the studies; no rule, strip, box, or edge-to-edge rectangular frame may divide them: a plain of tall dry grass at night with a rebel camp of plain tents and watchfires in the middle; the same plain burning, flames twice the height of a man, black smoke, orange light, with a clearly repeated family of tall, wind-stretched, unlettered black-and-indigo field banners, with indigo cloth planes visibly distinct from their lamp-black poles and edging and with their silhouettes isolated directly against the orange fire, free of emblems, characters, seals, and labels; the same plain at grey dawn, black stubble and drifting smoke. No figures, no lettering.
- **set-imperial-camp.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, two views: a hillside of trampled red imperial banners and broken spears in late-afternoon light with long shadows; and a general's large field tent of heavy cloth with its front flaps tied back, guard posts on either side. No figures, no lettering on banners.
- **set-palace.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, two views: the capital seen from above, grey tile roofs and wide avenues, the palace on a high stone platform with a long, steep white stair; and the throne hall inside: red lacquer columns, a polished black floor, smoking bronze braziers, and at the far end on a dais a vast gold throne built for a grown emperor. No figures, no lettering, no inscribed boards. Remove every human figure from both views and reconstruct the vacated areas as uninterrupted paving, stair, wall, roof, tree, or floor. Preserve the set's primary marker as a completely empty axial complex: grey roofs and walls framing the high platform and long white stair above; red lacquer columns, black reflective floor, braziers, and the vast gold throne below. Do not replace the figures with guards, courtiers, statues, banners shaped like people, or any other humanoid silhouette. Remove every plaque-shaped or character-like mark in both views and reconstruct each vacated area as uninterrupted painted beam, lintel, wall, or door; retain the vast gold throne itself as the interior primary marker without any inscription. Recompose the two studies as unframed vignettes on one continuous warm mulberry-paper ground: eliminate the horizontal rule/gutter and feather the lower edge of the exterior and upper edge of the hall irregularly into shared open paper, while preserving the exterior's empty axial high platform and long white stair and the interior's empty red-column/black-floor/brazier/gold-throne axis.
- **set-banquet-stable.** One 1536 × 1024 landscape plate on warm mulberry paper. Redesign the plate as two unframed vignettes on one continuous warm-paper ground, separated by a broad blank-paper gutter; remove the black inter-panel rule and do not enclose either vignette with a frame. The banquet vignette is a palace banquet hall with rows of low lacquered tables laden with dishes, lamps, red columns, and hanging purple textiles. Redesign those textiles as solid dark-purple cloth with non-glyph geometric edge bands only: remove every discrete vertical stroke cluster that can resolve as a written character at full size, thumbnail size, or in grayscale. The stable vignette is a palace stable at night. Remove the polearm completely. Keep the stable's primary markers to the single amber lantern, stall doors, hay, and visually subordinate tack; reserve every crescent or long-bladed polearm silhouette for the approved Lü Bu/Guan Yu weapon references. No figures, no horses, no lettering.
- **set-bedchamber.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, one view: the emperor's bedchamber, heavy silk curtains, a great bed, a wide low couch, and in the corner a round polished bronze mirror on a carved stand facing the couch, clearly reflective. Brazier light. No figures, no lettering. Rebuild the complete room in bold brush-and-ink contours and matte ink-and-wash on visibly warm mulberry paper; remove the mirror-like floor gloss and photoreal material modeling while retaining the dark lacquer-red, black, and restrained gold palette, brazier-lit cast shadows, and the same bed/couch/mirror spatial hierarchy. Replace the mirror with a true circular polished bronze disc on a carved freestanding stand, and rotate its reflective plane unambiguously toward the wide low couch. Keep the circle and its couch-facing reflection legible at thumbnail size and in grayscale.
- **set-farmhouse-road.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, three views: a modest farm gate and small courtyard among yellow fields at dusk; a small farm kitchen at grey dawn, a plain wooden table, a cleaver, a whetstone, a hearth; and a country road between willows and yellow fields in morning light. No figures, no other animals, no lettering. Redesign the plate as a borderless three-view montage: extend the top courtyard image and both lower images fully to their shared edges, replacing both white gutters with edge-to-edge painterly joins while preserving the same three views and their current relative scale. Redesign the lower-left view so one tied pig lies lengthwise across the central foreground table as the dominant primary marker. Keep the cleaver and whetstone present but subordinate and clearly separate from the animal; add no person and preserve the grey-dawn exterior light. Redesign the lower-right view so one plain earthenware wine jar is clearly visible tipped and rolling on the road's central track, large enough to read at thumbnail, with the willows and yellow fields remaining the environmental frame. Do not add the uncle, donkey, fruit basket, or any other figure to this view. Redesign the tree and wall vegetation in muted raw umber, loess ochre, and dust grey, leaving only restrained dusk warmth in the sky; the gate opening and rammed-earth courtyard should carry the silhouette.
- **set-coalition-camp.** One unframed 1536 × 1024 landscape setting plate on warm mulberry paper, composed as two separate environmental studies with irregular brush-faded edges and broad open paper between them; no box, inset, panel rule, border, or dividing strip. The larger daylight study is a high oblique valley-wide view of a temporarily empty coalition camp: dense rows of unoccupied neutral-loess canvas tents extend to the far end, divided by broad empty packed-earth lanes and dotted with unmanned wagons, crates, low palisade fences, cold cooking hearths, and rising smoke columns. Many tall banners of varied plain colours and shapes show the eighteen factions; every cloth face is blank. Directly above the largest neutral-loess command tent, one very tall pole carries an unmistakable wind-stretched matte-gold banner with a free cloth edge, wholly separate from the tent roof and the only gold command accent. At the valley's head, a vast grey fortress gate fills the pass between two mountains, its walls climbing both slopes and small plain purple banners flying from its towers. The smaller study is the camp edge at dusk: one small plain tent beside a low campfire, split logs, and modest camp furniture, with no faction standard. The entire plate is an unoccupied environment: no people, troops, walkers, guards, sentries, crowds, animals, statues, or human-shaped silhouettes anywhere. No lettering, labels, emblems, seals, pictograms, glyph-like strokes, or watermarks.
- **set-great-tent.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, one view: inside a great command tent, a long table running away from the viewer with seats on either side and one raised seat at the head under Yuan Shao's great unlettered gold command banner, restrained with ivory rather than vermilion, daylight through canvas, and at the near end the entrance flap tied open onto a dusty plain with a distant grey fortress wall. Do not introduce an imperial dragon, seal, or written device. No figures, no lettering. Remove every black glyph from both narrow standards flanking the command end and replace the marked areas with blank cloth or a simple non-symbolic woven border; no letters, calligraphy, seals, or pseudo-writing may remain anywhere on the plate. Remove every human body, face, helmeted head, and human silhouette from the canvas. Preserve the empty guard posts, spear racks, chairs, and entrance architecture as environmental structure only; do not replace the guards with alternate people. Retain the long red-edged table and rank-ordered chairs, but clear the full central tabletop of the campaign map, loose and tied scrolls, brushes, ink pieces, and bronze desk vessels. Leave a broad, mostly bare dark tabletop with an unobstructed head-of-table area so the separately governed hot-wine cup and champion's helmet can be introduced only in their scripted states.
- **set-hulao-gate.** One unframed 1536 × 1024 landscape plate on warm mulberry paper, two views: Hulao Gate from the plain in hard daylight, a massive gate tower over great iron-studded wooden doors, thick grey walls running up the mountain slopes on either side, purple banners along the battlements, a dusty plain in front where armies could meet; and the battlements at night, crenellations, purple banners, a heap of cushions, the moon, and far below the campfires of a great army filling the valley. No figures, no lettering. Structurally redesign the gate-front primary marker as a completely blank dark-lacquer panel with no glyphs, pseudo-glyphs, seals, stamps, monograms, or emblematic marks; keep all purple banners free of character-like marks as well. Remove every human and horse silhouette. Carry the army's scale only with unoccupied tents, cooking fires, smoke columns, banner poles, palisade lines, and distant points of fire; no body-shaped marks may remain at full resolution or thumbnail size. Retain the loose heap of cushions as the sole foreground prop and remove the chest, rug, and rolled carpet-like bundles so the reference cannot propagate a false recurring object state. Structurally redesign the night-view primary-marker composition by removing the brazier, its stand, and its foreground flame, then reconstructing that vacated area as uninterrupted cold-moonlit battlement stone and shadow. Keep the loose cushion heap as the only foreground prop; keep all other fire only as distant points in the army camp below.
- **obj-weapons.** One unframed 1536 × 1024 landscape object plate on warm mulberry paper, four weapons laid out at one scale with open paper between them: the Green Dragon blade, a long-handled glaive with a broad crescent blade and a dragon worked at its base; the serpent spear, a very long spear with a wavy, snake-shaped blade; two matching plain straight swords in black scabbards, crossed as they would be worn on a back, with a strap; and a long halberd with a spear point and a crescent side-blade. No hands, no figures, no lettering.
- **obj-red-hare.** One unframed 1536 × 1024 landscape object plate on uninterrupted open warm mulberry paper, two views of the same horse at one scale: Red Hare, a huge, powerful horse the colour of blood with a darker red-black mane and tail, saddled with bronze-and-vermilion tack, standing; and the same horse bare, rearing. Remove every field banner and pole, palisade, fortification, smoke plume, hill, dust cloud, and ground plane behind and between the horses, reconstructing those areas as plain paper. Add no replacement scenery, faction accent, rider, lettering, border, or third state.
- **obj-small-things.** One unframed 1536 × 1024 landscape object plate on warm mulberry paper, items at a readable scale with open paper between them: a short dagger with seven coloured jewels set in a row down its hilt, shown sheathed and drawn; a small bronze seal of command in the shape of a crouching tiger; a plain bronze wine cup with steam rising from it; a dented iron helmet with a dark plume; and a bundle of woven straw sandals tied on a cord. No hands, no lettering, no characters or seal marks.
