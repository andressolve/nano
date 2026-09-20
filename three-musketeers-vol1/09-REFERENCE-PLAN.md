# Reference Plan — approved as a system

**Nothing generates a page until every character visibly on that page has an
approved permanent lock.** Not just-in-time. Locks live in `refs/approved/` and
get there only through `tools/refs.py promote` with an independent critic
report. A sheet in `refs/candidates/` is not a lock.

## Canvas and register — for every sheet

Reference sheets are **1536 × 1024 landscape**; story pages are portrait. This
is not an inconsistency: four views across a wide canvas is what a lock needs.

**Register, verbatim in every generative sheet prompt:**

> **Lantern and Steel.** Brush-and-ink line on warm laid paper with opaque,
> matte gouache washes: lamp-black line, raw umber and yellow ochre, Prussian
> blue for the Musketeers, vermilion for the Cardinal, lead white for lace and
> collars, a little gold. Seventeenth-century France lit like a lantern film:
> candle and lantern light indoors with real cast shadows and real depth,
> rain-grey and river-grey outdoors, dust and dawn on the road. Visible brush
> line, visible paper grain, gouache drying chalky at the edge of a wash;
> wool, leather, wet stone, steel, and wax. Not smooth prestige-oil realism.
> No glossy concept-art surfaces, no airbrushed skin, no engraved
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

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
named. **Boards are critic-only rasters and never generation inputs** — their
file names carry `board`, `adversarial`, `silhouette` or `live-pair` so the
tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 01 | `01-dartagnan` — ochre doublet, grey hat, the long sword; view (d) mud to the waist, hat in hand | character | 1 | p 1 | new |
| 02 | `02-athos` — blue cassock, black doublet, hands on pommel; view (d) left arm in the black sling | character | 8 | p 8 | new |
| 03 | `03-porthos` — blue cassock over crimson, gold baldric, red triple plume; view (d) from behind, cloak off, the plain leather back of the baldric | character | 9 | p 9 | new |
| 04 | `04-aramis` — blue cassock over dove grey, lace collar, book at belt; view (d) back to a rail, lace handkerchief wound round the sword hand | character | 10 | p 10 | new |
| 05 | `05-constance` — grey dress, white apron with a small gold crown, white cap, keys, basket; view (d) apron off, white collar, at the ball | character | 17 | p 17 | new |
| 06 | `06-cardinal` — red robe and skullcap, seated, the grey cat on his lap; view (d) standing, turned, one hand holding a folded letter | character | 22 | p 22 | new |
| 07 | `07-rochefort` — all black, red feather, the scar; view (d) soaked, hatless, right arm held against the chest | character | 3 | p 3 | new |
| 08 | `08-buckingham` — white satin slashed with gold, lace collar, pearls, blue sash; view (d) one glove off, holding it | character | 36 | p 36 | new |
| — | `board-heads` — all eight, same light, same angle | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — all eight, full length | board | — | — | from approved sheets |
| — | `adversarial-athos-rochefort` — same panel, same light, both three-quarter and profile, grayscale pass | board | — | — | `02-athos` `07-rochefort` |
| — | `adversarial-aramis-buckingham` — same panel, both fair men, three-quarter and profile | board | — | — | `04-aramis` `08-buckingham` |
| — | `adversarial-dartagnan-aramis` — the two young men side by side, grayscale pass | board | — | — | `01-dartagnan` `04-aramis` |
| — | `adversarial-athos-cardinal` — the two grave bearded men, costume-free crops, shared reaction, grayscale | board | — | — | `02-athos` `06-cardinal` |
| — | `live-pair-athos-rochefort` — unlettered, page scale, the p 12 staging: Athos under the tree, Rochefort at the gap in the wall | board | — | — | `02-athos` `07-rochefort` `01-dartagnan` |
| — | `set-road` — a white road between ochre hills, poplars; a night road under a big sky; the hill above the sea | set | 1 | p 1 | — |
| — | `set-meung-yard` — the inn yard, well, trough, stable door, the first-floor window | set | 3 | p 3 | — |
| — | `set-paris` — roofs, the river, a bridge with houses; a narrow street; the Musketeers' arched gate | set | 6 | p 6 | — |
| — | `set-carmelite-field` — the meadow, the yellow wall, the tree, the trough, the gap in the wall | set | 12 | p 12 | — |
| — | `set-house` — the street door at night with the lantern bracket, the steep stair, the attic with its window and nail | set | 17 | p 17 | — |
| — | `set-cardinal-study` — red hangings, black desk, one candle, no window | set | 22 | p 22 | — |
| — | `set-athos-room` — whitewash, one chair, one table, the sword on the wall | set | 25 | p 25 | — |
| — | `set-chantilly-inn` — a bright inn room, long table, noon light | set | 28 | p 28 | — |
| — | `set-beauvais-bridge` — a stone bridge at dusk, the river, the rail | set | 29 | p 29 | — |
| — | `set-amiens-inn` — the yard at evening; the cellar door and steps into barrels | set | 31 | p 31 | — |
| — | `set-calais-quay` — stone quay, barrier, gangplank, grey sea, gulls | set | 33 | p 33 | — |
| — | ~~`set-buckingham-palace`~~ — retired 2026-09-07 after six candidates: four locations plus a counted continuity object overloaded one canvas; architecture split into `set-buckingham-water-stair`, `set-buckingham-bedchamber`, and `set-buckingham-workroom`, while the casket lock lives on `obj-casket-pouch-ring` | — | — | — | — |
| — | `set-buckingham-water-stair` — the white river front, marble water stair, and river of masts | set | 36 | p 36 | — |
| — | `set-buckingham-bedchamber` — the white-and-gold bedroom and hall of mirrors; the bedside table stays clear for the separately locked casket | set | 37 | p 37 | — |
| — | `set-buckingham-workroom` — the pale jeweler's bench, loupe, tongs, and one small fire | set | 39 | p 39 | — |
| — | `set-louvre` — the ballroom with dais and gallery; the back stair and service door | set | 41 | p 41 | — |
| — | `obj-horse` — the yellow horse, old, calm, buttercup-yellow, saddled and bare | object | 1 | p 1 | — |
| — | `obj-letters-pass` — the father's letter sealed in red wax and the same letter with the seal broken; the Queen's small letter in blue wax with a crown; the pass, one line | object | 2 | p 2 | — |
| — | `obj-casket-pouch-ring` — the velvet casket open with twelve slots, ten filled, two empty; the same with twelve; the small leather pouch with two studs; the Queen's ring | object | 22 | p 22 | — |

**Generation order:** `01-dartagnan` (he is on every page, and every young
man collides with him); then the risky lanes, `02-athos` and `07-rochefort`,
then `04-aramis` and `08-buckingham`; then `03-porthos`, `05-constance`,
`06-cardinal`; then boards (head and silhouette boards are crop-and-place
from approved pixels, not generations); then adversarial and live-pair
boards; then plates in page order.

## States needed, enumerated from the script

| Character | State | Pages |
|---|---|---|
| d'Artagnan | default: ochre doublet, grey hat, long sword, no cloak | 1–32 |
| d'Artagnan | mud to the waist, hat in hand, same clothes | 33–46 |
| d'Artagnan | shirt sleeves, no doublet, at the window and in the rain | 19–21 |
| d'Artagnan | ring on his hand | 46–49 |
| Athos | left arm in the black sling | 8–16 |
| Athos | default, no sling | 18–49 |
| Porthos | cloak off, baldric back seen (once) | 9 |
| Porthos | second hat crammed on top of his own | 47 |
| Aramis | handkerchief wound round the hand | 29–30, 47 |
| Aramis | limping (posture, not costume) | 47 |
| Constance | default, apron with crown, cap, keys, basket | 17–27 |
| Constance | apron off, white collar | 41–46 |
| Cardinal | seated, cat on lap | 22, 49 |
| Cardinal | seated in the ballroom chair, no cat; standing and turned p 45 | 42–45 |
| Rochefort | default, black, red feather, hat | 3–34 |
| Rochefort | hatless, soaked, right arm held to the chest | 35 |
| Rochefort | right arm in a white sling | 42–46 |
| Buckingham | one state; glove off from p 37 | 36–39 |

## Nearest lookalikes and what carries the separation

Carried from `04-CHARACTER-LEDGER.md`; the sheet prompt for each names its
lookalike and the differentiators that must survive grayscale and thumbnail.

| Sheet | Never confused with | Carried by |
|---|---|---|
| 01 d'Artagnan | 04 Aramis; 07 Rochefort | beardless vs moustached; black unruly hair vs blond curls; ochre with no cloak vs blue cassock. Beardless boy vs scarred man; ochre vs black; weight forward vs weight back |
| 02 Athos | 07 Rochefort; 06 Cardinal | pointed beard vs thin moustache only; no scar vs scar; tallest vs middle height; blue with white cross vs all black; stillness with hands on pommel vs chin up. Standing, thirty, dark vs seated, grey, red |
| 03 Porthos | none close; 08 Buckingham at a stretch | bulk; red-brown curls and waxed moustache; the baldric. Round ruddy face vs square handsome; blue and crimson vs white satin |
| 04 Aramis | 08 Buckingham; 01 d'Artagnan | slim vs broad; hair to the collar, fine vs past the shoulder, heavy; small moustache vs short beard; blue serge vs white satin and pearls. Blond vs black; moustache vs none |
| 05 Constance | the Queen (scenery) | grey and white, cap, apron vs white and silver, crown, seen only at a distance |
| 06 Cardinal | 02 Athos | seated, red, grey, cropped hair under a cap vs standing, blue, dark, hair to the shoulder |
| 07 Rochefort | 02 Athos | the scar; thin moustache, no beard; black, no cross; red feather; middle height |
| 08 Buckingham | 04 Aramis | as above, inverted; pearls and the blue sash |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`). The Cardinal's guards wear the red cassock
  with the white cross and plain steel morions or wide hats with no feather,
  faces generic and turned away; other Musketeers in the street wear the blue
  cassock with the white cross and are clean-shaven or full-bearded, never a
  pointed beard, never a red-brown waxed moustache, never blond curls;
  innkeepers and sailors are bareheaded and aproned; the court at the ball is
  gold and silver silk and no one in it wears red, ochre, or a black doublet;
  the Queen is white and silver with a small crown, seen from behind or at a
  distance, face never close; the King is a crowned figure seated on the dais,
  no face. No background man is beardless and black-haired in ochre. No
  background man has a scar.
- A rejected sheet never becomes a lock and never becomes an input.
- **Art notes carried from the script gate:** the twelve studs are drawn as
  one bright cluster in two rows on the Queen's left shoulder, never as a
  countable puzzle; the casket's ten-then-twelve is carried by two large empty
  velvet slots, not by counting stones. The father's letter must be
  recognisable on p 22 and p 44 from p 4: cream paper, red wax, then the same
  paper with the seal broken. The Queen's letter is small and blue-sealed and
  never confused with it.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas: **(a)** three-
quarter head and shoulders, neutral expression, even light; **(b)** full-length
standing figure, default costume, habitual posture; **(c)** strict profile, same
light; **(d)** the one state the script actually needs (age phase, disguise,
grief, travel clothes).

## 01 — D'ARTAGNAN

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

d'Artagnan, eighteen, from Gascony. A boy, not a man: long narrow face, sharp
chin, a long straight nose, dark brows, dark brown eyes set close and quick,
sun-brown skin. No beard and no moustache of any kind; the only clean-shaven
male face in the book. Black hair, thick and unruly, falling into his eyes,
cut roughly to the jaw. Lean, all elbows and knees, narrow shoulders. He never
stands still: weight forward on the balls of his feet, one hand on the hilt.
Habitual gesture: pushing his hair out of his eyes with the back of his sword
hand. Expression at rest: about to say something he should not.

Default costume, views (a), (b), (c): a doublet of faded, patched ochre-yellow
wool over a plain shirt, brown breeches, worn brown riding boots, a grey felt
hat with exactly one visibly snapped, short broken feather, and his father's
sword at his hip: an old long rapier with a plain swept steel hilt, visibly
too long for him. There must be no second plume. No cloak.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, large enough to lock the long narrow face, sharp chin, long straight nose,
close-set quick dark eyes, low dark brows, and the black hair falling into his
eyes. Clean-shaven, unmistakably.

View (b): full length, hat on, the body reading forward on the balls of the
feet: pitch the centre of gravity over the leading foot, lightly flex both
knees, raise the rear heel so only the ball of that foot is loaded, and remove
the settled one-leg, hip-cocked contrapposto. Keep the narrow shoulders and
one hand on the hilt, the sword's length against his leg showing it is too
long for him, the other hand pushing his hair back. At thumbnail, the result
must read as a boy already moving, not Aramis's weight-on-one-hip posture.

View (c): a true ninety-degree profile from hat to boots, same light, keeping
the long nose, sharp chin, narrow shoulders, and the sword's length.

Views (a)–(c) have no scenery and no props beyond the sword and hat, leaving
only the plain warm paper.

View (d): the same boy at the end of a two-day ride: the same clothes with
mud to the waist, the same grey felt hat in his hand carrying the identical
broken-feather silhouette with exactly one visibly snapped, short broken
feather and no second plume, hair wet and in his eyes, standing very straight
in a doorway of light.

d'Artagnan must never be confused with Aramis. Differentiators that must
survive grayscale and thumbnail: no moustache against Aramis's small neat
one; black rough hair against blond curls; ochre with no cloak against the
blue cassock; weight forward against weight on one hip. He must never be
confused with Rochefort: a beardless boy's face against a scarred man's; ochre
against black; a broken grey feather against a red one.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — ATHOS

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Athos, a Musketeer, thirty and looking older. Tall, straight as a post, the
tallest man in the book. Long pale face, high forehead, straight nose, grey
eyes, hooded and level, deep vertical lines beside the mouth. Dark brown hair
to the shoulder, straight, pushed back from the forehead; a short pointed
beard and a neat moustache, dark. Lean and broad-shouldered, no stomach.
Stands with both hands folded on the pommel of his sword, point on the
ground, and does not shift his weight. Habitual gesture: stillness.
Expression at rest: level, unamused, and not unkind.

Default costume, views (a), (b), (c): the Musketeer's blue cassock with the
white cross, worn open over a black doublet; black breeches and boots; a
black hat with one white plume; a plain steel-hilted sword.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, large enough to lock the long pale face, high forehead, hooded grey eyes,
the vertical lines by the mouth, the pointed dark beard and neat moustache,
and the shoulder-length hair pushed back.

View (b): full length, hat on, both hands folded on the pommel, point on the
ground, feet together, absolutely still.

View (c): a true ninety-degree profile from hat to boots, same light, keeping
the height, the straight back, the pointed beard, and the hands on the pommel.

Views (a)–(c) have no scenery and no props beyond the sword and hat.

View (d): the same man with his left arm in a plain black cloth sling, the
cassock worn over it, the right hand on the pommel, the face slightly whiter,
otherwise unchanged.

Athos must never be confused with Rochefort. Differentiators that must
survive grayscale and thumbnail: a short pointed beard against a thin
moustache with no beard; no scar against a scar from temple to mouth; a head
taller; the blue cassock with the white cross against all black; a white plume
against a red feather; stillness with hands on the pommel against weight back
and chin up. He must never be confused with the Cardinal: standing, thirty,
dark-haired, in blue, against seated, grey, in red.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — PORTHOS

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Porthos, a Musketeer, thirty-five. Enormous: the widest man in the book by
half, chest like a barrel, big hands, a head taller than a boy. Round ruddy
face, heavy jaw, small bright blue eyes, a big nose. Red-brown hair in thick
curls to the collar; a great red-brown moustache waxed out to points; no
beard. Stands chest out, fists on hips, feet planted wide. Habitual gesture:
one hand smoothing the front of his baldric. Expression at rest: delighted
with himself.

Default costume, views (a), (b), (c): the blue cassock with the white cross,
strained across the chest, over a doublet of crimson; a wide shoulder-baldric
heavily embroidered with gold across the front; a black hat with three red
ostrich plumes, the largest hat in the book; a heavy sword with a gilt hilt.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, large enough to lock the round ruddy face, heavy jaw, small bright eyes,
big nose, the waxed red-brown moustache, and the curls to the collar. No
beard.

View (b): full length, hat on, chest thrust out and feet planted wide, with
one fist remaining on the hip while the other large hand lies flat along the
embroidered front of the gold baldric in a clear smoothing action.

View (c): a true ninety-degree profile from plumes to boots, same light,
keeping the bulk, the barrel chest, the moustache points, and the plumes, with
both fists on hips as the default posture.

Views (a)–(c) have no scenery and no props beyond the sword and hat.

View (d): the same man seen from directly behind, cloak off, so that the back
of the baldric shows: plain buff leather with no gold at all, buckled across
the blue cassock.

Across views (b), (c), and (d), show exactly one heavy sword: one gilt hilt
entering one scabbard at one consistent hip attachment. Remove every
secondary hilt, dagger, free blade, and divergent extra scabbard form. The
single-sword silhouette must match from front, profile, and rear.

Porthos must never be confused with Buckingham. Differentiators that must
survive grayscale and thumbnail: red-brown curls to the collar against gold
curls past the shoulder; a waxed moustache with no beard against a short
beard; a round ruddy face against a square handsome one; blue and crimson wool
against white satin. He must never be confused with Athos: bulk against
leanness, red hair against dark, three red plumes against one white.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — ARAMIS

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Aramis, a Musketeer, twenty-four. Slim, of middle height, a hand shorter
than the tallest man in the book and half the width of the widest. Fine oval
face, smooth high forehead, small straight nose, large dark eyes with long
lashes, pale clear skin, a small mouth. Blond hair, fair and fine, curled to
the collar and always in order; a small neat blond moustache and a tiny tuft
under the lip; no beard. Stands with his weight on one hip. Habitual gesture:
two fingers touching the moustache before he speaks. Expression at rest:
polite, amused, and not telling you why.

Default costume, views (a), (b), (c): the blue cassock with the white cross,
immaculate, over a doublet of dove grey with a wide white lace collar; black
hat with one white plume; a slim sword with a silver hilt; a small
leather-bound book in a strap at his belt.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, large enough to lock the fine oval face, smooth forehead, large lashed
dark eyes, small mouth, the small neat blond moustache and lip tuft, and the
fair curls to the collar.

View (b): full length, hat on, weight on one hip, two fingers at the
moustache, the book visible at the belt.

View (c): a true ninety-degree profile from hat to boots, same light, keeping
the slim build, the small nose, the moustache, and the curls ending at the
collar.

Views (a)–(c) have no scenery and no props beyond the sword, hat, and book.

View (d): the same man with his back to a plain stone rail, sword out, a white
lace handkerchief with a small embroidered monogram wound round his sword
hand, hat on, calm, two fingers of the other hand at his moustache. The rail
is the only scenery on the sheet.

Aramis must never be confused with Buckingham. Differentiators that must
survive grayscale and thumbnail: slim against broad; fair fine curls ending at
the collar against heavy gold curls past the shoulder; a small moustache and
lip tuft against a short full beard; blue wool and a lace collar against
white satin, pearls, and a blue sash. He must never be confused with
d'Artagnan: blond against black, a moustache against none, a cassock against
an ochre doublet.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — CONSTANCE

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Constance, twenty, the Queen's dresser. Small and quick, a head shorter than
the boy. Round face, soft chin, short straight nose, wide-set hazel eyes, dark
brows, a scatter of freckles. Dark brown hair in curls, pinned up under a
white linen cap, with strands always escaping. Slight, straight-backed,
hands never idle. Habitual gesture: looking up, chin lifted, as if up a
stair. Expression at rest: practical, and about to say something true.

Default costume, views (a), (b), (c): a plain dress of dove grey with white
cuffs and a white apron whose bib carries one small embroidered gold crown;
a white linen cap; a ring of iron keys at her waist; a covered wicker basket
on her arm.

View (a): a true three-quarter head-and-shoulders study in even light, cap
on, large enough to lock the round face, soft chin, short nose, wide-set eyes,
freckles, and the escaping curls.

View (b): full length, cap on, basket on her arm, keys at her waist, chin
lifted as if looking up a stair.

View (c): a true ninety-degree profile from cap to hem, same light, keeping
the small straight-backed figure, the short nose, and the cap.

Views (a)–(c) have no scenery.

View (d): the same young woman in the same grey dress with the apron off and
a plain white collar in its place, cap on, no basket, both hands on a plain
wooden rail, looking down.

Constance must never be confused with the Queen, who is scenery: grey and
white and a linen cap against white and silver and a small crown; small,
freckled, and close against tall, distant, and never seen close.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — THE CARDINAL

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

The Cardinal, forty-five. A thin ascetic man: long narrow face, hollow
cheeks, high forehead, a thin high-bridged nose, pale grey hooded eyes that
do not blink, pale skin. Grey hair cropped close under the cap; a short
pointed grey beard and a thin grey moustache, both precise. Narrow-shouldered,
long-fingered. Seated whenever possible. Habitual gesture: one hand stroking a
grey cat on his lap. Expression at rest: calm, and already decided.

Default costume, views (a), (b), (c): a cardinal's robe and short cape of one
saturated vermilion red, a red skullcap, a small gold cross on a chain at the
chest. No sword, no hat with a feather.

View (a): a true three-quarter head-and-shoulders study in even light, cap
on, large enough to lock the long hollow-cheeked face, thin high-bridged nose,
pale hooded unblinking eyes, and the precise grey pointed beard and thin
moustache.

View (b): seated in a plain high-backed black chair, the robe falling to the
floor, a grey cat on his lap, one long hand on the cat. This is his default
full-length view; he does not stand for it.

View (c): a true ninety-degree profile, seated, same light, keeping the thin
nose, the cropped grey hair under the cap, and the pointed beard.

Views (a)–(c) have no scenery beyond the chair.

View (d): the same man standing, for once, turned half away as if toward a
door, one hand holding the already-opened folded cream letter, its fold torn
visibly through the sealing point and two clearly separate, jagged red wax
remnants remaining attached to opposite sides of the opened fold, with open
paper visible between them and no single circular seal shape, so the broken
state remains unmistakable at story-page scale and cannot seed an intact
sealed letter on later pages, the robe falling straight, no cat.

The Cardinal must never be confused with Athos. Differentiators that must
survive grayscale and thumbnail: grey against dark; cropped hair under a cap
against hair to the shoulder under a plumed hat; seated against standing; red
against blue; forty-five against thirty.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — ROCHEFORT

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

Rochefort, the man with the scar, forty. A dark man of middle height: square
hard face, heavy black brows, black eyes, strong jaw, sallow skin, and a pale
scar running from the left temple down across the cheekbone to the corner of
the mouth, visible in every view. Black hair, straight, to the collar; a thin
black moustache; no beard. Compact and muscular. Stands with his weight back
and his chin up. Habitual gesture: a laugh through the nose. Expression at
rest: amused at someone else's expense.

Default costume, views (a), (b), (c): black from hat to boot: a black doublet,
a black cloak, black breeches and boots, a black hat with a single red
feather, a plain black-hilted sword. Never a cassock, never a cross.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, turned so that his anatomical LEFT cheek faces the viewer and the scar is
fully visible, large enough to lock the square face, heavy black brows, thin
moustache with no beard, and the scar from temple to mouth. The scar exists on
his anatomical left side only; his right cheek is unmarked, and any view that
shows the right cheek shows no scar.

View (b): full length, hat on, weight back, chin up, one hand on the hilt,
the red feather clearly the only colour on him.

View (c): a true ninety-degree profile of his anatomical LEFT side, nose
pointing toward the viewer's right, from hat to boots, same light, the scar
running across the visible left cheek, the thin moustache, no beard.

Views (a)–(c) have no scenery.

View (d): the same man hatless and soaked through, hair flat, standing on
a stone step turned to show his left cheek, his right elbow visibly bent and
his right forearm pinned diagonally across the upper chest, with his left hand
supporting the right forearm or wrist and his right fist closed, the scar on
the left cheek and the thin moustache unchanged.

Rochefort must never be confused with Athos. Differentiators that must
survive grayscale and thumbnail: a thin moustache with no beard against a
short pointed beard; a scar against none; middle height against the tallest
man in the book; all black with a red feather against a blue cassock with a
white cross and a white plume; weight back and chin up against stillness
with hands on the pommel.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 08 — THE DUKE OF BUCKINGHAM

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views.

The Duke of Buckingham, thirty-five. A broad-shouldered man in his prime, as
tall as the tallest man in the book: a handsome square-jawed face, straight
nose, blue eyes, high colour, a wide mouth. Golden hair in long loose curls
past the shoulder; a short golden beard and a full moustache. Athletic, moves
fast. Habitual gesture: pulling off one glove. Expression at rest: warm, and
about to decide something.

Default costume, views (a), (b), (c): a doublet and breeches of white satin
slashed with gold, a wide collar of white lace, a rope of pearls, a sash of
blue silk across the chest, white stockings, shoes with gold rosettes. No
cloak, no cassock, no hat.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the square jaw, straight nose, wide mouth, the short golden
beard and full moustache, and the heavy gold curls past the shoulder.

View (b): full length, one foot forward as if coming down a stair, the pearls
and sash fully visible.

View (c): a true ninety-degree profile, same light, keeping the height, the
breadth, the beard, and the length of the curls.

Views (a)–(c) have no scenery.

View (d): the same man with one glove pulled off and held in his fist, the
bare hand flat on a small table, face lowered, colour gone from his cheeks.

Buckingham must never be confused with Aramis. Differentiators that must
survive grayscale and thumbnail: broad against slim; heavy gold curls past
the shoulder against fine fair curls to the collar; a short full beard
against a small moustache; white satin, pearls, and a sash against blue wool.
He must never be confused with Porthos: gold against red-brown, a beard
against a waxed moustache, satin against cassock.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

---

## Board prompts (critic-only rasters, generated from the two attached approved sheets)

`board-heads` and `board-silhouette-grayscale` are crop-and-place from
approved pixels (`tools/boards.py`), never generated.

- **adversarial-athos-rochefort.** One unframed 1536 × 1024 landscape reference board on a plain warm laid-paper ground, under flat even light, with no lettering, labels, rules, or props in hand. On the left third, show the two men from the attached approved sheets full length, side by side on one floor line and at one scale: Athos is one bare head taller, upright and still in his blue cassock with white cross and single white plume; Rochefort stands compactly with weight back and chin raised, dressed entirely in black with one red feather. On the right two-thirds, arrange four matched costume-free head pairs in a clean two-by-two field with open paper between them, every crop ending at the jaw and upper neck: a neutral three-quarter pair; the same pair sharing an open-mouth alarm; strict left-cheek profiles with every nose pointing screen right; and strict right-cheek profiles with every nose pointing screen left, this last pair rendered in pure grayscale. Keep the faces identical to the approved sheets in every view: Athos has a long pale narrow face, high forehead, hooded level grey eyes, straight nose, neat moustache, and short pointed dark beard; Rochefort has a shorter square hard face, heavy black brows, strong jaw, thin black moustache, and no beard. Rochefort's single pale scar is anatomically fixed from his left temple across the left cheekbone to the left corner of his mouth: show the continuous scar in the left-cheek profile and whenever that left facial plane is exposed, and show an entirely unmarked right cheek in the right-cheek profile. The scar never changes sides. Preserve Athos's longer beard-pointed lower face against Rochefort's broader bare chin through the reaction, profiles, and grayscale reduction.
- **adversarial-aramis-buckingham.** 1536 × 1024 landscape, plain warm-paper ground, no lettering, no borders. Four matched tests on one scale, the two fair men from the attached sheets in each: a costume-free neutral three-quarter face pair; a costume-free strict-profile pair; a costume-free shared-reaction pair, both with the same clenched-jaw anger; and a pure-grayscale repeat of the shared reaction. Costume-free means crops ending at the jaw and upper neck with no lace, pearls, sash, collar, or cassock visible. Each face must be exactly the face on its sheet: Aramis's short oval face, tapered chin, high fine brows, small upturned moustache and lip tuft, fine curls to the collar; Buckingham's square jaw, short full beard, wide mouth, heavy gold curls past the shoulder.
- **adversarial-dartagnan-aramis.** 1536 × 1024 landscape, plain warm-paper ground, no lettering, no borders. The two young men from the attached sheets, hats off, at identical scale and angle in four quadrants: neutral three-quarter pair in colour; strict-profile pair in colour; the pair sharing one strong open-mouth alarm reaction; and the neutral pair repeated in pure grayscale. Crops end at the jaw and upper neck with no cassock or collar. Each face must be exactly the face on its sheet: d'Artagnan's long projecting nose, sharp narrow chin, close-set eyes, jagged black fringe, bare upper lip; Aramis's shorter nose, tapered oval chin, high fine brows, blond hairline, small upturned moustache and lip tuft.
- **adversarial-athos-cardinal.** 1536 × 1024 landscape, plain warm-paper ground, no lettering, no borders. Four matched tests at one scale under identical flat light, the two men from the attached sheets in each: a costume-free neutral three-quarter face pair; a costume-free strict-profile pair; a costume-free shared-reaction pair, both with the same clenched-jaw anger; and a pure-grayscale repeat of the shared reaction. Costume-free means crops ending at the jaw and upper neck with no hat, skullcap, plume, collar, cassock, or red robe visible. Each face must be exactly the face on its sheet: Athos thirty, long pale face filled at the cheek, hooded grey eyes, dark hair to the shoulder, short pointed dark beard; the Cardinal forty-five, hollow cheeks, thin high-bridged nose, pale unblinking eyes, cropped grey hair, precise short grey beard.
- **live-pair-athos-rochefort.** A single unlettered story-scale image on the 1536 × 1024 landscape canvas, the scene composed as a wide tableau at page scale: the meadow behind a high wall of yellow stone at noon, one big tree, a stone trough by the wall. Athos and Rochefort are alone, standing on the same ground plane. The tall Musketeer from one attached sheet stands under the tree on the right, narrow, vertical, and motionless with both hands centered on the pommel of his grounded sword. The man in black from the other attached sheet stands at a gap in the wall on the left, compact, weight back, red feather, chin raised, hand on hilt. Athos is exactly one full head taller than Rochefort: do not scale their hats or feathers to manufacture the gap; the top of Athos's bare skull must sit one head-height above Rochefort's. No balloons, no captions, no text of any kind. Each face must be exactly the face on its sheet.
- **set-road.** Regenerate it as one unframed 1536 x 1024 landscape canvas: carry the warm laid-paper ground cleanly to every edge, remove all perimeter edging, and let each view feather organically into the common paper instead of meeting at straight horizontal or vertical divisions. Three views on one ground: a white road between ochre hills with a line of poplars under a hot morning sky, warm light from behind the viewer; the same kind of empty road at night under a large sky; a road cresting a long hill at dawn with an open grey sea horizon beyond. Remove the milestone completely from every view; the daytime view must be carried only by the white road, ochre hills, and poplar line, the night view by the empty road and large sky, and the dawn view by the hill road and sea horizon. Remove the harbor, buildings, vessels, and masts; beyond the empty hill road, show open sea and dawn only, reserving all quay and shipping markers for `set-calais-quay`. Dust, ochre, and dawn; no figures, no horses.
- **set-meung-yard.** A low inn yard of packed dirt: a stone well, a stone trough, a stable door standing open on straw, and a first-floor window with shutters open above the yard; hard afternoon shadows. Keep the first-floor shutters visibly open in every view. Replace the lower-right view with the same yard in the afternoon under the same hard directional light as the upper view, from a lower yard-level angle aimed upward: retain the well, trough, and stable door as grounding landmarks, but enlarge and isolate the open first-floor window in the upper third, making it the dominant high-contrast marker above the yard, with its hard cast shadow pointing down into the playable yard space; one stall remains empty. Remove the lit wall lantern and all night-blue illumination. This primary-marker hierarchy must survive grayscale and thumbnail reduction. No figures. Remove the horse completely and leave that stall as dark, empty architecture; preserve the explicitly required empty stall in the adjoining bay without adding any animal or human silhouette elsewhere. Remove the rule and redesign the transition as unmarked negative space on the common warm laid-paper ground, with both yard views feathering organically into that ground and no straight frame, panel edge, or separator.
- **set-paris.** Three views: Paris from the last hill, grey-blue slate roofs stacked to the horizon, a brown river, stone bridges with houses built on them, chimney smoke, and one narrow church spire, overcast light; a narrow street of tall leaning houses, mud, a corner; a great arched carriage door in a stone wall, standing open on a courtyard, seen from the step. No figures. Remove every perimeter line and straight horizontal or vertical separator. Carry the common warm laid-paper ground cleanly to all four canvas edges, and let the panorama, narrow street, and gate vignette feather organically into that ground through unmarked negative space. Remove that lantern completely and relight the entire narrow-street view with the same cool overcast daylight as the Paris panorama, preserving only the tall leaning houses, mud, and corner as its primary markers. Replace that dome with a lower irregular run of grey-blue slate roofs, chimney smoke, and one narrow church spire; retain the house-lined stone bridge and brown river as the panorama's dominant location markers. Remove every human silhouette from that vignette and reconstruct the vacated areas as uninterrupted muddy ruts, puddled cobbles, and cool overcast street depth. Keep the tall leaning houses, mud, and corner as the only primary markers; do not replace the figures with cloaks, carts, animals, or any other recurring prop.
- **set-carmelite-field.** A meadow of long grass behind a high wall of yellow stone, one big tree, a stone horse trough against the wall, and a gap in the wall; flat bright noon light. Then the same field at early morning with dew. No figures. Regenerate the plate as one unframed 1536 x 1024 landscape canvas: carry the common warm laid-paper ground cleanly to all four edges, eliminate the horizontal rule and every perimeter edge, and let the two field views feather organically into unmarked negative space. Preserve the trough as the repeated primary marker in both views, in the same relationship against the yellow wall and to the left of the wall gap. Redesign the wall in both views as a continuous barrier at least 2.5 times the visible height of the trough, built from at least seven clearly readable stone courses; make the opening a full-height break through that barrier, keep the trough directly against the wall immediately left of the opening, and preserve this same wall–trough–gap geometry in the noon and early-morning views.
- **set-house.** One unframed 1536 x 1024 landscape plate on a shared warm laid-paper ground, with three separate architectural vignettes whose irregular outer edges feather into open negative space and form no straight divider: at left, a narrow street door at night in rain, blue-black except for one warm lantern on a bracket beside the door, with one puddle and one cart; at centre, the signature steep wooden stair seen from the bottom, with warm light and one candle at the top; at right, the warm attic with structural floor, plaster, and beams, containing only one street-facing window, one narrow bed, one bare table, one candle, and exactly one bare hand-forged iron nail high in a beam. The nail is isolated against clear negative space and has a small solid head with a short straight shank projecting horizontally from the beam, unmistakable at thumbnail scale; it has no curve, hook, ring, eye, cord, or attached object. No other furniture, books, cups, stools, boxes, chests, trunks, portable props, figures, lettering, labels, borders, or panel rules.
- **set-cardinal-study.** A red room and nothing else: red hangings, a black desk with a single candle, maps, one plain high-backed black chair, no window and no daylight of any kind. Red and black only. No figures, no cat. Remove the lantern, its candle, and its glow completely; reconstruct that portion of the desk as uninterrupted black wood, and retain the existing bare desk candle as the room's only flame and only local light source. Remove the ornament, stem, and tassel completely; reconstruct continuous unbroken red hanging behind it so that the room's primary-marker hierarchy is red hangings, black desk, one bare candle, maps, and one plain high-backed black chair—nothing else. Re-render the entire plate in the locked **Lantern and Steel** register: visible brush-and-ink line over a warm laid-paper ground, opaque matte gouache washes, visible paper grain, and chalky drying edges. Remove the current photographic/3D surface rendering, glossy candle sheen, lens-like light falloff, and texture-map realism. Preserve the required primary-marker structure exactly—continuous red hangings, one plain high-backed black chair, one black desk, maps, and one bare candle as the only flame and local light source—with no added object, figure, lettering, border, window, or daylight.
- **set-athos-room.** A bare whitewashed room: one wooden chair, one table, one narrow bed, and a single sword hung on the wall; grey window light. No figures. Remove both the lit tabletop lantern and the lit candle, including every amber glow, flame reflection, and warm cast shadow they create. Relight the whole room exclusively with diffuse grey daylight entering through the single window at left, with cool neutral shadows and no secondary flame or local light source. This is also required to keep Athos's room from collapsing into the warm, candlelit attic identity specified for `set-house`. Remove the tankard, dish, candleholder, lantern, and every other loose tabletop item; reconstruct the table as one completely empty rough wooden surface and do not replace the removed objects. Preserve exactly one wooden chair, one table, one narrow bed, and one wall-hung sword as the room's readable inventory. Replace the blue cover with worn undyed grey-brown bedding no more saturated than the whitewashed walls and timber, and keep the single wall-hung sword as the sole high-contrast accent. At thumbnail and in grayscale, the sword must remain the first isolated object read after the room silhouette, not the table light or bedcover. Redesign the entire plate as line-led brush-and-ink architecture on visibly warm laid paper, with raw-umber and restrained grey gouache washes, visible grain, and chalky wash edges; eliminate photographic surface rendering and smooth prestige-oil/3D realism while retaining grey window light and real cast depth. Replace the broad, double-edged cruciform sword and round pommel with the same narrow-bladed seventeenth-century rapier carried by approved Athos: a slender blade, compact swept metal hilt, straight grip, and matching pommel proportions. Keep that single rapier hanging on the wall in the present state so it can leave the wall for Athos's hand on p. 26 without creating a second weapon identity.
- **set-chantilly-inn.** A bright inn room at noon: a long table with cups and bread, a hearth, a door to the yard; hard sunlight through small windows. No figures.
- **set-beauvais-bridge.** A stone bridge over a brown river at dusk, a low parapet rail, a line of stones dragged across the road at the far end, picks leaning on them, the first star. No figures.
- **set-amiens-inn.** Two views: an inn yard at evening with a well and lanterns being lit; a cellar door standing open at the top of stone steps going down into a dark full of barrels. No figures.
- **set-calais-quay.** One unframed 1536 x 1024 landscape setting plate in the locked **Lantern and Steel** register: brush-and-ink line, matte gouache, visible warm laid-paper grain. A low wet stone quay reaches into a wind-beaten grey harbour under diffuse grey morning light, with one working boat alongside, ropes, rigging, gulls, sea spray, and open grey water. Compose the quay from its landward approach toward the boat. Beside the foot of the gangplank, place one simple waist-high hinged timber swing gate across the walking route, its rail perpendicular to the waterline and its opening aligned with the route onto the boat; keep open staging space on both sides of the gate for the sergeant, traveller, and hand-held pass on the finished page. Every face of the gate is uninterrupted bare timber. The plate's dominant marker is one continuous wet gangplank, pale-edged against the grey, running in a strong diagonal from the open quay stones down to the boat. No notice, paper, placard, signboard, writing, glyphs, marks, fence along the water, lantern, flame, figures, lettering, border, or watermark.
- **set-buckingham-palace.** *Retired; see the manifest. Its architecture is split across `set-buckingham-water-stair`, `set-buckingham-bedchamber`, and `set-buckingham-workroom`; the counted casket is locked separately on `obj-casket-pouch-ring`.*
- **set-buckingham-water-stair.** One unframed 1536 x 1024 landscape view on warm laid paper: Buckingham's white palace front above a luminous river-grey river crowded with masts, with a broad marble stair descending unmistakably to the water. Use high-key, directionless white illumination with restrained gold accents; preserve depth through brush-and-ink contour, marble joints, overlapping pale planes, and the river silhouette, with no cast-shadow shapes or dark tonal masses. No figures, portable objects, lettering, labels, borders, or watermark.
- **set-buckingham-bedchamber.** One unframed 1536 x 1024 landscape plate on warm laid paper, with two irregular architectural vignettes feathered into open negative space and no straight seam, rule, frame, or rectangular division. Use the same high-key, directionless white illumination in both views; preserve depth through brush-and-ink contour, mirror edges, overlapping pale planes, and restrained gold accents, with no cast-shadow shapes or dark tonal masses. First: Buckingham's white-and-gold bedroom with one bed, unmistakable tall mirror panels, and exactly one small white-and-gold bedside table. Keep that tabletop completely bare so the separately locked `obj-casket-pouch-ring` can supply the scripted ten-then-twelve state on the pages; every other table and console is also bare, and no portable bedroom object appears. Second: a wide hall of mirrors whose primary marker is a repeated rhythm of full-height mirrors in white-and-gold wall bays, clearly distinct from the intimate bedroom. No figures, lettering, labels, borders, or watermark.
- **set-buckingham-workroom.** One unframed 1536 x 1024 landscape view on warm laid paper: Buckingham's jeweler's workroom in white, cream, and very light umber, with one pale bench, pale recess, pale bench fronts, and pale under-bench planes. Use high-key, directionless white illumination; carry depth only through brush-and-ink contour and overlapping pale planes, with no black mass or cast-shadow pool. Remove the hanging lantern and every flame or glowing wick except the one small, shallow fire on the bench; keep that bench fire as the sole concentrated dark-warm accent without adding a cast-shadow pool. Replace it with a compact, shallow circular loupe in a thin metal housing, rotated to side-three-quarter so a transparent lens opening is unmistakable; give it no vertical wall, cavity, crown, brim, cup, or hat silhouette, and place it immediately beside the tongs for scale. Redesign it as exactly one pair of compact pivoted tongs with two opposed gripping jaws and short handles; remove or simplify any secondary bench or rack tools whose paired jaws could read as additional tongs, leaving the remaining tools faint and subordinate. No figures, casket, lettering, labels, borders, or watermark.
- **set-louvre.** Two views: a hall of gold and a thousand candles seen from a gallery above, a dais at the far end with two thrones and a court's worth of empty polished floor, long doors along one side; a torchlit service door at the back of the palace with a stone stair going up into light, copper pans and steam implying the kitchens. No figures. Redesign the plate as one unframed 1536 × 1024 landscape canvas on a common warm laid-paper ground: remove the full-width horizontal band and every straight separator, then feather the irregular lower edge of the ballroom and upper edge of the service-stair vignette into open negative space without allowing either scene to form a rectangular frame. Remove every human form from the wall art and reconstruct those bays as nonfigurative dark painted fields or plain shadowed architectural panels within the existing gold mouldings; preserve the hall's primary-marker hierarchy of gallery overlook, empty polished floor, distant two-throne dais, long side doors, and candlelight, with no replacement portrait, statue, silhouette, or heraldic personage. Replace the entire ballroom pavement with continuous polished wooden floorboards whose reflections preserve the long approach to the dais; retain stone only in the separate service-stair vignette. Redesign the ballroom architecture so an elevated gallery with a visible supporting edge or arcade is plainly readable above one side of the hall, while retaining the dais at the far end and the run of long doors along one side.
- **obj-horse.** One old buttercup-yellow gelding, calm, on one plain ground. Redesign the plate as four distinct views of the same old gelding: retain a large three-quarter head study, retain a strict full-length ninety-degree side profile with the established saddle and bridle, replace only the lower-left view with a full-length bare three-quarter view rotated approximately 35 degrees toward the viewer: show both sides of the chest and barrel, separate all four legs in depth, keep the heavy calm weight evenly grounded, and preserve the same modest withers, long slightly downturned head, pale mane and tail, and buttercup-yellow coat. Keep this replacement completely free of saddle, blanket, bridle, reins, stirrups, and all other tack, and add a bare rear view. Preserve the same long, slightly downturned head, modest withers, heavy calm posture, pale mane and tail, and unmistakable buttercup-yellow coat in all four views. Remove the trough, masonry, water pump, wet paving, and all other scenery from the object plate. Make both bare views read as the horse's late re-entry state through the tack-free silhouette itself; the page may supply the Carmelite-field trough separately from its setting lock. The only yellow animal in the book; never cream, palomino, dun, or chestnut. No figures, no lettering.
- **obj-letters-pass.** On a plain ground, four discrete paper objects: the father's long cream fold with red wax in sealed and visibly broken states; the Queen's smaller folded letter with a blue crowned seal; and a long, narrow pass, unfolded once, with no wax seal, materially slimmer than the father's letter and larger than the Queen's letter. Its one-line construction must be carried by a single broad horizontal ink rule with no legible glyphs, preserving the plate's absolute no-lettering requirement while giving the pass a primary marker that survives thumbnail reduction and re-entry after absence. Every exposed paper surface is completely free of handwriting, signatures, pseudo-letters, glyphs, captions, labels, and watermarks. Redesign the father's sealed letter as a distinctly long horizontal tri-fold packet with a plain, unmarked red seal, and carry that same long tri-fold geometry into its opened/broken-seal state; retain the Queen's letter as a compact near-square packet whose blue seal alone carries the crisp crown impression. The two sealed states must remain distinguishable by packet proportion and seal design with all color removed. No other objects.
- **obj-casket-pouch-ring.** On a pale white field under even, diffuse, shadowless white-and-gold palace light, with gold hardware as the restrained accent and no cast shadows beneath the caskets, pouch, ring, or studs, the casket in two state views, plus the pouch and ring only: a small velvet-lined casket standing open, one grid of exactly twelve large slots in two rows of six, exactly ten occupied and exactly two adjacent slots visibly empty; beside it a second, separately readable open-casket view using the identical casket, identical twelve-slot grid, and identical orientation, but with all twelve slots filled; beside them a small drawstring leather pouch with its mouth turned toward the viewer and exactly two studs visibly nested at or partly emerging from the mouth, with no detached studs outside the pouch; a gold ring with one dark stone. Redesign every occupied slot and both pouch-mouth pieces as the same compact, bright, clearly faceted diamond jewel in a restrained gold mount, with no enamel field and no fleur-de-lis device. Preserve the exact state geometry already achieved: in the first casket, ten occupied slots and the two adjacent lower-right slots empty; in the second, those identical ten positions unchanged and the two lower-right positions filled; at the pouch mouth, exactly two matching diamond studs and none outside. Remove every ground-plane cast shadow and reconstruct one uninterrupted pale white field beneath all four object groups; retain depth only through brush-and-ink contour, internal velvet value, overlap, and restrained gold hardware highlights. Exactly ten studs in the first casket view, exactly twelve in the second casket view, and exactly two at the pouch mouth, counted. Preserve the two oversized empty slots as the primary marker of the first state; do not ask the page model or reader to infer the second state from the two pouch studs. No other objects.
