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

This is Volume I's register, carried word for word (`00-VOLUME-MANDATE.md`,
parent authorities). In each character block below, the line
`*(register paragraph, verbatim)*` is replaced with exactly this paragraph by
`tools/refbrief.py`; plate and board briefs get it appended by the same tool.

Every character sheet closes with the anti-collision clause, verbatim:

> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.

**No sheet carries lettering of any kind** — no name plates, no labels, no
writing on the Cardinal's paper or the commission, no words on the bottle's
tag, no sign on the inn. Labelled sheets teach the page model to letter the
art. The two texts the story needs on paper — the Cardinal's pardon read
aloud on p 29, and the bottle's tag read aloud on p 19 — are lettered on the
page from the script's exact strings, or spoken; their plate locks blank
paper (a misspelt word on a lock would be copied onto every page).

**No blood, no drawn wound, no brand on any sheet or plate.** The lily on
Milady's shoulder is a page instruction from words on p 13 only; it never
appears on her sheet, in any view, as skin mark or ornament (see her block and
the standing rules). Constance's death is staged on the pages from words; no
sheet carries it.

**Volume palette** (`05-SETTINGS-AND-OBJECTS.md`): Volume I's, unchanged, with
one addition. Musketeer blue and the Cardinal's red still own the book; the
boy's ochre-yellow belongs to him and his horse; **Milady's plum** — deep
violet silk with silver — appears nowhere she is not. Three locations must
look like different worlds: Milady's salon (gold candlelight and plum, too
beautiful), the camp at La Rochelle (dun earth, smoke, grey sea), and the
river (black, white water, one lantern).

## Anchoring (sequels)

Parent anchors live in `refs/parents/`, copied byte-identical from
`../three-musketeers-vol1/refs/approved/`: the seven returning characters
(`01-dartagnan`, `02-athos`, `03-porthos`, `04-aramis`, `05-constance`,
`06-cardinal`, `07-rochefort`) and seven plates (`set-paris`, `set-house`,
`set-carmelite-field`, `set-cardinal-study`, `set-athos-room`, `obj-horse`,
`obj-casket-pouch-ring`). `tools/refbrief.py` resolves every anchor name in the
manifest's last column under `refs/approved/`; a parent anchor is therefore
written `../parents/<file>` and resolves to `refs/parents/<file>.png`. A
parent file is never attached to a page — only the approved lock built from it
(or relocked as it) is.

**Why every returning character gets a fresh continuity sheet.** The page
tools accept inputs only from `refs/approved/` (`tools/verify.py`), and each
Volume I sheet carries a view (d) that is wrong for this book: Athos's (d) is
the black sling (none in this volume), Rochefort's (d) is the soaked man with
the arm pinned across his chest (no injury here), d'Artagnan's (d) is the mud
of the Calais ride (this book needs the blue cassock), Porthos's (d) is the
back of the baldric, Aramis's (d) is the handkerchief round the sword hand,
the Cardinal's (d) holds Volume I's broken-sealed letter, and Constance's (d)
leans on a rail. So each returning character is re-locked from its parent
with views (a)–(c) copied unchanged and a new view (d) for the state this book
needs. **A continuity pass, never a redesign.** Returning sheets keep their
Volume I numbers; the one new sheet is `08-milady` (Volume I's 08 was
Buckingham, who does not return).

**Why the seven inherited plates are relocked, not regenerated.** They passed
Volume I's plate critics and whole-cast gate as these same places and objects,
and none of them changes in this book. Each is relocked as its approved parent,
unchanged, the way Monkey King Volume III relocked its dragon: a fresh
reference critic judges the parent file under the relock scope below, and
`refs.py promote --as` locks it. Regeneration is the fallback only if that
critic returns REVISE (the plate's prompt bullet then generates from the
attached parent).

| Sheet | Parent anchor | Ageing job |
|---|---|---|
| 01 dartagnan | `refs/parents/01-dartagnan.png` | **none** — a few months later, the same boy: views (a)–(c) Volume I's ochre doublet, grey hat with the broken feather, the too-long sword, unchanged; the Queen's ring now shown small on his right hand; new view (d) in the Musketeer's blue cassock with the white cross over the same ochre doublet (pp 56–57) |
| 02 athos | `refs/parents/02-athos.png` | **none** — views (a)–(c) unchanged; **no sling** anywhere; new view (d) hatless and soaked, one hand held out open (the river, pp 48–49) |
| 03 porthos | `refs/parents/03-porthos.png` | **none** — views (a)–(c) unchanged; new view (d) with the breakfast basket (the bastion, pp 27–33) |
| 04 aramis | `refs/parents/04-aramis.png` | **none** — views (a)–(c) unchanged; new view (d) hatless, kneeling, the small book open (Béthune, p 43) |
| 05 constance | `refs/parents/05-constance.png` | **none** — views (a)–(c) Volume I's apron with the small gold crown, keys and cap (pp 7–8), unchanged; new view (d) the Béthune state: the same grey dress, no apron, no keys, a white collar, the white cap, a straw garden basket (pp 36–42) |
| 06 cardinal | `refs/parents/06-cardinal.png` | **none** — views (a)–(c) unchanged, seated, the grey cat; new view (d) seated in a plain dark travelling cloak thrown over the red, hood down (the Red Dovecote, pp 22–23); the horse state (p 34) is drawn from words |
| 07 rochefort | `refs/parents/07-rochefort.png` | **none** — views (a)–(c) unchanged, the scar on the left only; **no sling, no injured arm**; new view (d) bareheaded, hat in hand, left cheek to the viewer (pp 4, 53) |
| 08 milady | — | **new**; no parent |
| set-paris, set-house, set-carmelite-field, set-cardinal-study, set-athos-room, obj-horse, obj-casket-pouch-ring | `refs/parents/<same name>.png` | **relock as the approved parent, unchanged** (see Relocks) |

## Sheet manifest

Character sheets gate pages. Boards gate nothing but are required inputs to the
reference critic. Setting and object plates are generation inputs to the pages
named. **Boards are critic-only rasters and never generation inputs** — their
file names carry `board`, `adversarial`, `silhouette` or `live-pair` so the
tools can refuse them.

| # | Sheet | Kind | Blocks pages from | First appearance | Anchor |
|---|---|---|---|---|---|
| 08 | `08-milady` — new: tall, very pale, ice-blue eyes, pale ash-gold ringlets far past the shoulder, deep plum silk with silver lace, the dark-stoned ring on her left hand; view (d) the Béthune widow, dark grey dress, black veil pushed back | character | 4 | p 4 | new |
| 01 | `01-dartagnan` — continuity: ochre doublet, grey hat with the broken feather, the long sword, the small ring on his right hand; view (d) the blue Musketeer cassock with the white cross over the ochre doublet | character | 1 | p 1 | `../parents/01-dartagnan` |
| 02 | `02-athos` — continuity: blue cassock over black, white plume, hands on the pommel, no sling; view (d) hatless and soaked, one hand held out open | character | 1 | p 1 | `../parents/02-athos` |
| 07 | `07-rochefort` — continuity: all black, red feather, the scar on the left cheek only, no sling; view (d) bareheaded, hat in hand, left cheek toward us | character | 4 | p 4 | `../parents/07-rochefort` |
| 04 | `04-aramis` — continuity: blue cassock over dove grey, lace collar, book at the belt; view (d) hatless, kneeling, the small book open | character | 1 | p 1 | `../parents/04-aramis` |
| 05 | `05-constance` — continuity: dove-grey dress, apron with the small gold crown, cap, keys, basket; view (d) the Béthune state, no apron, white collar, white cap, straw basket | character | 7 | p 7 | `../parents/05-constance` |
| 03 | `03-porthos` — continuity: blue cassock over crimson, gold baldric, red plumes; view (d) with the big lidded breakfast basket | character | 1 | p 1 | `../parents/03-porthos` |
| 06 | `06-cardinal` — continuity: red robe and skullcap, seated, the grey cat; view (d) seated in a plain dark travelling cloak over the red, hood down | character | 4 | p 4 | `../parents/06-cardinal` |
| — | `board-heads` — all eight faces, same light, same angle | board | — | — | crop-and-place from approved sheets |
| — | `board-silhouette-grayscale` — assembled automatically by the driver's crop-and-place step; NOT the silhouette test (method/07: it carried fragments of neighbouring views twice); the gate judges silhouettes on the two generated boards below and treats this one as superseded | board | — | — | crop-and-place from approved sheets |
| — | `adversarial-silhouettes-a` — d'Artagnan, Athos, Porthos, Aramis, Rochefort: isolated full bodies, a solid binary silhouette row and a matched grayscale row | board | — | — | `01-dartagnan` `02-athos` `03-porthos` `04-aramis` `07-rochefort` |
| — | `adversarial-silhouettes-b` — Milady, Constance, Aramis, the Cardinal, Athos: isolated full bodies, a solid binary silhouette row and a matched grayscale row | board | — | — | `08-milady` `05-constance` `04-aramis` `06-cardinal` `02-athos` |
| — | `adversarial-athos-rochefort` — the highest-risk pair: full length together, costume-free heads, profiles both sides, both hatless, grayscale | board | — | — | `02-athos` `07-rochefort` |
| — | `adversarial-milady-aramis` — the two fair heads: costume-free crops, profiles, shared reaction, Aramis hatless, grayscale; the river-landing full-length pair | board | — | — | `08-milady` `04-aramis` |
| — | `adversarial-milady-constance` — the only two women, in their Béthune states, at true relative scale; heads three-quarter and profile; grayscale | board | — | — | `08-milady` `05-constance` |
| — | `adversarial-dartagnan-aramis` — the two young men, costume-free heads and grayscale, then both in blue cassocks full length (pp 56–57) | board | — | — | `01-dartagnan` `04-aramis` |
| — | `adversarial-athos-cardinal` — the two grave bearded men: costume-free crops, shared reaction, grayscale; Athos against the Cardinal in his dark travelling cloak | board | — | — | `02-athos` `06-cardinal` |
| — | `live-pair-milady-constance` — unlettered, page scale, the p 36 staging: the kind widow holding both of Constance's hands on the cloister bench | board | — | — | `08-milady` `05-constance` |
| — | `obj-horse` — RELOCK of Volume I's approved plate, unchanged: the old buttercup-yellow gelding, saddled and bare | object | 1 | p 1 | `../parents/obj-horse` |
| — | `set-paris` — RELOCK of Volume I's approved plate, unchanged: roofs, river and house-lined bridge; the narrow street; the arched gate | set | 1 | p 1 | `../parents/set-paris` |
| — | `set-house` — RELOCK of Volume I's approved plate, unchanged: the street door with the lantern bracket, the steep stair, the attic | set | 2 | p 2 | `../parents/set-house` |
| — | `obj-casket-pouch-ring` — RELOCK of Volume I's approved plate, unchanged; critic continuity reference for the Queen's ring only, never a page input (the casket and studs do not exist in this book) | object | — | — | `../parents/obj-casket-pouch-ring` |
| — | `set-carmelite-field` — RELOCK of Volume I's approved plate, unchanged: the long grass, the yellow wall, the tree, the trough | set | 3 | p 3 | `../parents/set-carmelite-field` |
| — | `set-cardinal-study` — RELOCK of Volume I's approved plate, unchanged: red hangings, black desk, one candle, no window | set | 4 | p 4 | `../parents/set-cardinal-study` |
| — | `obj-milady-carriage` — the black closed coach with plum curtains drawn, no horses, no arms on the door | object | 5 | p 5 | — |
| — | `set-milady-square` — the tall pale stone house on a paved square: the front door up its steps, the tall first-floor windows | set | 9 | p 9 | — |
| — | `set-milady-salon` — the gold salon: plum hangings, gilt mirror, harpsichord, the tall window, and the half-drawn plum curtain on the small cabinet | set | 9 | p 9 | — |
| — | `set-tavern` — the Paris tavern: one table with four chairs, dark beams, lamplight, a window on the street | set | 10 | p 10 | — |
| — | `set-athos-room` — RELOCK of Volume I's approved plate, unchanged: whitewash, one chair, one table, one bed, the sword on the wall | set | 15 | p 15 | `../parents/set-athos-room` |
| — | `set-camp` — the camp before La Rochelle: tents, the trench ring, dun ground, smoke, and the walled city on its harbour with the grey sea beyond | set | 18 | p 18 | — |
| — | `obj-poison-ring-and-bottle` — Milady's ring closed and open; the dark green bottle with a blank paper tag; one jug and two plain glasses | object | 19 | p 19 | — |
| — | `set-dovecote-common-room` — the Red Dovecote below: low brown smoky room, big hearth, the broken iron stovepipe up through the ceiling, the dark stair to a door | set | 22 | p 22 | — |
| — | `set-dovecote-upper-room` — the room above: a small plank room, one table, one candle, two chairs, the stovepipe coming up through the floor, a dark window | set | 22 | p 22 | — |
| — | `obj-cardinals-paper` — the pardon, one cream sheet folded in three with no seal; the commission, a larger flat sheet with one red wax seal; both blank | object | 22 | p 22 | — |
| — | `set-north-road` — a long straight road through flat country, a line of poplars, a post inn, rain coming in | set | 25 | p 25 | — |
| — | `set-bastion` — inside the ruined fort Saint-Gervais: broken walls of stone and earth, rubble, a fallen block, a bare pike, the tall cracked wall leaning outward, standing; the city walls beyond | set | 26 | p 26 | — |
| — | `set-bethune-cloister` — the small cloister of pale stone: a square rose garden round a well, low round arches, a stone bench and a bare small table | set | 36 | p 36 | — |
| — | `set-bethune-gate` — the convent from the road: the plain arched front gate in a pale wall, the one upstairs window over the road, the long straight road with poplars | set | 39 | p 39 | — |
| — | `set-ferry-night` — the flooded ferry landing at night: black timbers, the rope across the river, the flat raft moored with one lantern on a short post, the white line of the weir | set | 45 | p 45 | — |
| — | `set-ferry-dawn` — the same landing at grey dawn: brown calm water, the cut rope hanging slack, no raft, no lantern | set | 51 | p 51 | `set-ferry-night` |

**Generation order:** first the seven inherited plates are relocked as their approved parents (see Relocks — a critic and a promotion each, no generation; do this before `tools/refrun.py --all`, which skips any sheet already locked). Then `08-milady` (new, and two of her three collisions are high: Aramis and Constance); then `01-dartagnan` (on every page; the blue-cassock state is new); then the highest-risk lane, `02-athos` and `07-rochefort`; then `04-aramis`; then `05-constance`; then `03-porthos`; then `06-cardinal`; then boards (the head and silhouette crop-and-place boards are assembled from approved pixels by the driver, not generated); then the two generated silhouette boards, the adversarial boards and the live pair; then the new plates in page order (the order of the manifest above), `set-ferry-dawn` after the approved `set-ferry-night` it is anchored on.

## Relocks — the seven inherited plates

Each inherited plate is relocked **as its approved Volume I parent, unchanged**,
by the procedure Monkey King Volume III used for its dragon:

1. `cp refs/parents/<name>.png refs/candidates/<name>-parent.png` (byte
   copy; the driver's version count ignores a `-parent` file).
2. Write `qa/references/<name>/critic-brief-parent-relock.md` from the
   refbrief critic template with the candidate path set to
   `refs/candidates/<name>-parent.png`, and this Stage 2 line: *"RELOCK SCOPE:
   this candidate is Volume I's approved plate, re-judged for Volume II. Judge
   only whether it locks this location or object as `05-SETTINGS-AND-OBJECTS.md`
   and this plan describe it for this volume, with no figures, no lettering, and
   no consequential object in a state this book forbids on every page that will
   attach it (the per-plate cautions below are page instructions, not plate
   defects)."*
3. A fresh `reference-critic` writes `qa/references/<name>/critic-parent-relock.md`.
4. On `VERDICT: APPROVED`: `python3 tools/refs.py three-musketeers-vol2 promote
   refs/candidates/<name>-parent.png --as <name>.png --report
   qa/references/<name>/critic-parent-relock.md`.
5. On `VERDICT: REVISE`: the plate generates through `tools/refrun.py` from its
   prompt bullet below with the parent attached; the relock file is not a
   candidate and does not count toward the ceiling.

Per-plate cautions (each is written into the packet of every page that
attaches the plate, as the forbidden-state rule requires):

- **set-paris** — overcast on the plate; the summer pages (1, 5–6) take hazy
  warm light from words. Attach one study only and name it (the house-lined
  bridge for p 1; the narrow street for pp 5–6 and 57; the arched gate for
  p 52, evening, from words).
- **set-house** — the street lantern is lit on the plate. On p 56 the bracket
  is dark and empty until the boy lights it: the page says so and names the
  study (the street door). Attach one study only: the attic for pp 2 and 56,
  the stair or street door for pp 7–8.
- **set-carmelite-field** — noon and early-morning studies; p 3 is late
  afternoon, from words. Name the noon study.
- **set-cardinal-study** — no cat on the plate; the cat comes from
  `06-cardinal`. The study has no window: p 57's window is the Cardinal's at
  a street, drawn from words, never this plate.
- **set-athos-room** — grey daylight, no flame on the plate. Pp 15–17 are night
  with one candle and a glass on the table, from words. The sword hangs on the
  wall (pp 15–16); on p 17 Athos takes it down.
- **obj-horse** — unchanged; the only yellow animal in the book.
- **obj-casket-pouch-ring** — **never attached to any page**: it carries the
  casket and the studs, which do not exist in this book. It is locked only so
  the critics can hold the Queen's ring (gold, one round faceted black stone in
  a raised claw setting, on the boy's right hand, drawn on `01-dartagnan`)
  apart from Milady's ring (`obj-poison-ring-and-bottle`).

## States needed, enumerated from the script

| Character | State | Pages |
|---|---|---|
| d'Artagnan | default: faded patched ochre doublet, grey hat with the broken feather, the long sword, the small ring on his right hand, no cloak | 1–55 |
| d'Artagnan | shirt sleeves at the attic window, night | 2 |
| d'Artagnan | on the yellow horse, flat out, hat flying | 5, 18, 35, 41, 45 |
| d'Artagnan | hay in his hair | 15 |
| d'Artagnan | mud and rain, hatless; chest-deep in the river gripping Athos's belt | 41–51 |
| d'Artagnan | muddy, hat in hand, before the Cardinal | 53 |
| d'Artagnan | the blue cassock with the white cross over the same ochre doublet, the same grey hat (view (d)) | 56–57 |
| Athos | default: blue cassock over black, black hat with one white plume, hands on the pommel; no sling | 1, 3, 10–11, 15–35, 41–47, 52, 55, 57 |
| Athos | hat in hand; seated on a camp stool; hat off at Béthune | 24; 26; 42–44 |
| Athos | hatless, soaked to the chest, one hand held out open (view (d)) | 48–49, 51 |
| Athos | the young count of his story: drawn small, from behind, black and silver on a grey horse (words; no lock) | 16 |
| Porthos | default: blue cassock over crimson, gold baldric, the red plumes; eating | 1, 3, 10–11, 17, 19–20, 21–23, 25–35, 41–51, 55, 57 |
| Porthos | with the big lidded breakfast basket (view (d)); shoulder to the wall; arms up on the ruin | 27–28, 33; 31; 32 |
| Porthos | hat crushed in his two hands | 43 |
| Aramis | default: blue cassock over dove grey, lace collar, book at the belt | 1, 3, 10–11, 17, 19–35, 41–51, 55, 57 |
| Aramis | tying the lace handkerchief to the pike (words) | 33 |
| Aramis | hatless, kneeling, the small book open (view (d)) | 43 |
| Constance | Volume I's default: dove grey, apron with the small gold crown, white cap, keys | 7 |
| Constance | brown wool travelling cloak over the default | 8 |
| Constance | the Béthune state: the same grey dress, no apron, no keys, white collar, white cap, straw garden basket (view (d)) | 36–44 |
| Constance | dying, eyes closed, head on his shoulder; laid on the bench (posture, words) | 42–44 |
| The Cardinal | seated, red, the grey cat; the hand stops on p 54 | 4, 53–54 |
| The Cardinal | a cloaked rider on the heath, a flash of red (words) | 21 |
| The Cardinal | seated in a plain dark travelling cloak over the red, hood down (view (d)); down the stair hood up | 22–23 |
| The Cardinal | on a grey horse, the red cape under a dark cloak (words) | 34 |
| The Cardinal | at a window above a street, one hand on the grey cat on the sill (words) | 57 |
| Rochefort | default: all black, red feather, scar on the left cheek only | 4–5, 12–14, 34–35, 38, 52–53 |
| Rochefort | bareheaded, hat in hand (view (d)) | 4, 53 |
| Rochefort | on a black horse (words) | 34, 35, 38 |
| Milady | default: deep plum silk gown, silver lace collar, slashed sleeves, the ring on her left hand | 4, 6, 9, 12–14 |
| Milady | the torn left sleeve and the lily (p 13 only, words; never on the sheet) | 13 |
| Milady | slate-grey hooded travelling cloak over the plum, hood back (words) | 22–24, 46–49 |
| Milady | the Béthune widow: dark grey dress, black veil pushed back, ringlets bound up (view (d)) | 36–37, 40 |
| Milady | the slate-grey cloak over the widow's dress (words) | 38–39 |
| Milady | with a knife at the rope; kneeling on the raft beside the lantern (words) | 46–49 |

## Nearest lookalikes and what carries the separation

Carried from `04-CHARACTER-LEDGER.md`; the sheet prompt for each names its
lookalike and the differentiators that must survive grayscale and thumbnail.
Lookalikes are named in prompts as words only — **a lookalike's sheet is never
attached to another character's generation; boards are critic-only.**

| Sheet | Never confused with | Carried by |
|---|---|---|
| 08 Milady | 04 Aramis (high); 05 Constance (high) | Vs Aramis: a woman's heart-shaped face with a small pointed chin and no facial hair vs an oval face with a small moustache and lip tuft; pale ice-blue eyes vs large dark eyes; pale ash-gold ringlets far past the shoulder vs fine blond curls ending at the collar; bareheaded vs a black hat with a white plume; plum silk gown vs blue cassock. Vs Constance: a head taller; pale ash-gold ringlets vs dark brown curls under a white cap; heart-shaped, very pale, no freckles vs round, freckled; dark charcoal widow's grey and a black veil vs light dove grey with a white collar and cap; ice-blue vs hazel |
| 01 d'Artagnan | 04 Aramis (high on pp 56–57, both in blue); 07 Rochefort | no facial hair vs a small neat moustache and lip tuft; black rough hair in the eyes vs blond curls in order; grey hat with a broken feather vs black hat with a white plume; weight forward vs weight on one hip; the ochre doublet showing at the chest and sleeves under his cassock. Vs Rochefort: beardless boy vs scarred man; ochre vs black |
| 02 Athos | 07 Rochefort (highest); 06 the Cardinal | short pointed dark beard vs thin moustache only; no scar vs the left-cheek scar; a head taller; blue cassock with the white cross vs all black; white plume vs red feather; stillness with hands on the pommel vs weight back, chin up. Vs the Cardinal: thirty vs forty-five; dark hair to the shoulder vs grey hair cropped under a skullcap; standing in blue vs seated in red |
| 07 Rochefort | 02 Athos | as above, inverted; bareheaded he keeps straight black collar-length hair, a square jaw, the thin moustache with no beard and the scar on the left only |
| 04 Aramis | 08 Milady; 01 d'Artagnan | as above, inverted; hatless he shows fine blond curls ending at the collar, the small moustache and lip tuft |
| 05 Constance | 08 Milady | as above, inverted; never taller than the boy |
| 03 Porthos | none close | bulk, the red-brown waxed moustache, the gold baldric, the red plumes |
| 06 the Cardinal | 02 Athos; 07 Rochefort when cloaked (p 34) | grey precise pointed beard, hollow cheeks, red skullcap, seated; under the travelling cloak the red always shows at the throat, cuffs and hem, and the cloak is dark brown-grey, never black like Rochefort's |

## Standing rules

- Any character on two or more pages gets a sheet. Prose locks are banned for
  recurring cast. Eight locks; everyone else is scenery.
- Absent lookalikes are critic-only. Never attach a lookalike to a generation
  as a negative example — the model draws what it is shown.
- **A returning character is a continuity pass on its parent.** Views (a)–(c)
  copy the attached Volume I sheet; only view (d) is new. A face, hair mass,
  beard or build that has drifted from the parent is a blocking finding even if
  it is handsome.
- **The costume that reverts to the sheet** (method/07). d'Artagnan's blue
  cassock lives only in his view (d): every packet for pp 1–55 says he wears
  the first three views' costume only, never the cassock; every packet for pp
  56–57 says he wears only the fourth view's costume. Constance's Béthune state
  (pp 36–44) and Milady's widow state (pp 36–37, 40) carry the same sentence;
  separation lines name the current colours, never the default ones.
- Unnamed and background figures may never carry a complete reserved identity
  stack (`04-CHARACTER-LEDGER.md`): beardless youth + black hair in the eyes +
  ochre → d'Artagnan; tall + dark pointed beard + blue cassock → Athos; huge +
  red moustache + gold baldric + red plumes → Porthos; slim + blond curls +
  small moustache + blue cassock → Aramis; grey dress + white cap + small and
  freckled → Constance; red robe + grey beard + cat + chair → the Cardinal;
  black clothes + scar + red feather → Rochefort; pale-gold ringlets + ice-blue
  eyes + plum silk + dark-stoned ring → Milady.
- **Reserved colours never land on an extra or a plate** (method/07, the
  reserved colour on an extra). Plum belongs to Milady and her carriage's
  curtains and her salon's hangings, nowhere else. The Cardinal's red robe is
  his alone; his guards wear the red cassock with the white cross, faces turned
  away. Ochre-yellow is the boy's and his horse's. The nuns are black and white;
  the army buff and steel; the Rochelais dun and black.
- **Two rings, never confused.** The Queen's ring: on d'Artagnan's right hand,
  small, gold, one round faceted black stone in a raised claw setting (Volume
  I's `obj-casket-pouch-ring`). Milady's ring: on her left hand, gold, a flat
  square violet-black stone in a box bezel that opens on a hinge. Neither is
  ever drawn on the other's hand.
- **The lily is never on a sheet or plate.** No fleur-de-lis shape anywhere on
  Milady's sheet, on her gown, lace, ribbon, ring or skin, and on no plate. Her
  sheet shows both shoulders covered and both sleeves whole. The brand is a
  page instruction on p 13 alone.
- **No counted object above five** on any sheet or plate (method/07), and **no
  number written into an uncounted ornament**: Milady's forward ringlets are
  "two or three", never counted; Porthos's plumes are Volume I's mass of red
  plumes as the parent shows them; the camp's tents, the bastion's stones and
  embrasures, the convent's arches and roses, the inn's beams are never
  numbered. Counts that are the story: one ring, one bottle, one jug, exactly
  two glasses, exactly four chairs at the tavern table, one lantern at the
  ferry, one candle in the room above the Dovecote.
- **No lettering on paper.** The pardon and the commission are blank; the
  bottle's tag is blank; the Dovecote's sign (p 21, words) is a painted red
  dove, never a word.
- **No blood, no drawn wound, no brand** on any sheet, board, or plate.
- A rejected sheet never becomes a lock and never becomes an input.
- Every sheet prompt names the positive lock and the nearest forbidden
  lookalike; every plate names the location it must never resemble.

---

# Sheet prompts

Each character sheet is four views on one landscape canvas: **(a)** three-
quarter head and shoulders, neutral expression, even light; **(b)** full-length
standing figure, default costume, habitual posture; **(c)** strict profile, same
light; **(d)** the one state the script actually needs.

## 08 — MILADY (new)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views, no scenery.

Milady, Lady de Winter, twenty-eight and looking younger: an English widow in
Paris whom nobody suspects. Tall for a woman — as tall as a lean young man of
eighteen — slender, very straight, with a long neck. A heart-shaped face with
high fine cheekbones, a small pointed chin, a short straight nose, and a full
mouth that smiles a moment before the eyes do. Large pale ice-blue eyes under
fine dark-gold brows. Very pale skin, no freckles. Her hair is pale ash-gold,
almost silver-gold, in long loose ringlets falling well past the shoulders to
the middle of the back, with two or three ringlets brought forward over her
right shoulder (any small number passes; they are not counted), and one narrow
dark ribbon in the hair. She is always bareheaded. Habitual gesture: turning
the ring on her left hand with her left thumb. Expression at rest: warm,
amused, attentive, as if you were the only person in the room.

Redesign the skull so the widest point is at the high cheekbones and the jaw
tapers continuously from those cheekbones to a visibly small pointed chin in
every view; keep the nose short and straight. Remove every discrete brown facial
speck in all four views while retaining very pale skin, high cheekbones, fine
dark-gold brows, and pale ice-blue eyes. Shift all hair in views (a)–(d) to a
uniformly cooler, lighter silver-ash gold whose grayscale value remains
distinctly light; retain the long loose ringlet silhouette through mid-back in
views (a)–(c), the narrow dark ribbon, and the dark-gold brows. Remove the crown
braid and all long hanging curls in the widow state; move the entire pale
ash-gold hair mass down and bind it at the nape beneath the pushed-back veil,
leaving only a few short pale strands at the temples. Preserve the same
corrected heart-shaped face and pointed chin so the disguise remains
unmistakably Milady. Replace the bow in views (a)–(c) with one narrow dark ribbon
tied unobtrusively into the long ringlets; do not add any other hair ornament or
jewellery.

Default costume, views (a), (b), (c): a gown of deep plum-violet silk with a
square neckline and a wide falling collar of silver lace that lies over both
shoulders; long sleeves slashed with silver; the skirt to the floor. On the
fourth finger of her left hand, a gold ring set with one flat square
violet-black stone in a raised box bezel, as if the stone were a small lid. No
other jewellery, no fan, no gloves, no hat.

View (a): a true three-quarter head-and-shoulders study in even light, large
enough to lock the heart-shaped face, the small pointed chin, the pale
ice-blue eyes under fine dark-gold brows, the full mouth beginning to smile,
and the pale ash-gold ringlets falling forward over the right shoulder.

View (b): full length, standing very straight, chin a little raised, the left
hand at her waist with the thumb on the ring, the right hand relaxed at her
side, the plum gown falling to the floor and the ringlets down her back.

View (c): a true ninety-degree profile from head to hem, same light, keeping
the long neck, the short straight nose, the small pointed chin, and the long
ringlets falling straight down her back.

Views (a)–(c) have no scenery and no props beyond the ring.

View (d): the same woman as a widow hiding in a convent: a plain high-necked
dress of dark charcoal grey, much darker than dove grey, with long plain
sleeves and no collar of any colour; a black veil pushed back from her head
and falling behind her shoulders; the pale ash-gold ringlets bound up at the
nape under the veil, a few pale strands at the temples; the same gold ring on
her left hand; hands folded at the waist; the same warm smile. No apron, no
white cap, no white collar, no basket.

In every view both shoulders are covered and both sleeves are whole. There is
no mark, brand, emblem or lily shape anywhere on the sheet — not on her skin,
not in the lace, the ribbon, the ring, or the gown.

Milady must never be confused with Aramis, the slim fair Musketeer.
Differentiators that must survive grayscale and thumbnail: a woman's
heart-shaped face with a small pointed chin and no facial hair against an oval
face with a small moustache and a tuft under the lip; pale ice-blue eyes
against large dark eyes; pale ash-gold ringlets far past the shoulder against
fine curls ending at the collar; bareheaded against a black hat with a white
plume; plum silk against a blue cassock. She must never be confused with
Constance: a head taller; pale ash-gold ringlets against dark brown curls under
a white cap; a pale heart-shaped face against a round freckled one; dark
charcoal and a black veil against light dove grey with a white collar and cap;
ice-blue eyes against hazel. Never blue, never red, never ochre; never the
dove-grey dress and white cap; never black hair or dark eyes; never short hair;
never a man's hat; never blood.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 01 — D'ARTAGNAN (continuity sheet, anchored on Volume I's approved 01)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume I sheet: this is the same
boy a few months later, unchanged. Copy his face, his hair, his build, his
ochre doublet, his grey hat with the broken feather and his father's sword in
views (a), (b) and (c) exactly as they are drawn there. Do not redesign,
refine, age or reshape anything; this is a continuity pass. Replace the
attached sheet's fourth view (the muddy figure in a doorway) entirely with the
new view (d) below.

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
too long for him. No cloak. On his right hand, small, a gold ring with one
round dark stone (the ring is small; where the hand is hidden it may be
unseen).

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, large enough to lock the long narrow face, sharp chin, long straight nose,
close-set quick dark eyes, low dark brows, and the black hair falling into his
eyes. Clean-shaven, unmistakably.

View (b): full length, hat on, the body reading forward on the balls of the
feet, one hand on the hilt, the other pushing his hair back, the sword's
length against his leg showing it is too long for him.

View (c): a true ninety-degree profile from hat to boots, same light, keeping
the long nose, sharp chin, narrow shoulders, and the sword's length.

Views (a)–(c) have no scenery and no props beyond the sword, hat and ring.

View (d): the same boy, full length, in the Musketeer's blue cassock for the
first time: the knee-length sleeveless Prussian-blue cape-mantle of the King's
Musketeers with a pale silver-grey border and a white cross on each front
panel, worn open over the same faded ochre doublet, so the ochre shows clearly
at the chest and sleeves; the cassock a little too big in the shoulders; the
same grey hat with the same single broken feather and no second plume; the
same too-long sword; the ring on his right hand. Standing straighter than
usual, chin up, trying not to grin. Still beardless, the black hair still in
his eyes.

d'Artagnan must never be confused with Aramis, especially when both wear the
blue. Differentiators that must survive grayscale and thumbnail: no moustache
against Aramis's small neat one and lip tuft; black rough hair falling into the
eyes against fair curls kept in order; a grey hat with a broken feather against
a black hat with a white plume; weight forward against weight on one hip; the
ochre doublet under his cassock against dove grey and a lace collar. He must
never be confused with Rochefort: a beardless boy's face against a scarred
man's; ochre against black; a broken grey feather against a red one. Never a
beard or moustache, never blond hair, never black clothes, never a scar, never
broad shoulders.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 02 — ATHOS (continuity sheet, anchored on Volume I's approved 02, no sling)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground. Use the attached approved Volume I
sheet as the identity anchor: Athos is the same man a few months later, with
the same face, proportions, hair, beard, costume and sword. No lettering,
labels, borders or scenery. No sling in any view; both arms are whole and free.

Athos is a thirty-year-old Musketeer who looks older. He is the tallest man in
the book, tall and lean with broad shoulders, no stomach, and a rigid upright
posture. His face is long and pale, with a high forehead, straight nose, level
hooded grey eyes, deep vertical lines beside the mouth, a neat dark moustache
and a short pointed dark beard. His dark-brown hair is straight, reaches his
shoulders, and is pushed cleanly back from the forehead. His resting expression
is level, unamused and not unkind. Stillness is his identifying gesture.

In views (a)–(c), he wears the Musketeer's blue cassock with the white cross,
open over a black doublet, with black breeches and boots, a black hat with one
white plume, and a plain steel-hilted sword.

View (a): a large three-quarter head-and-shoulders study in even light, hat on,
clearly showing the high forehead, long face, hooded eyes, mouth lines,
straight pushed-back shoulder-length hair, moustache and pointed beard.

View (b): full length, hat on, feet together, straight as a post. Both hands
are folded on the sword pommel with the point resting on the ground. His weight
does not shift.

View (c): a true ninety-degree full-length profile in the same light, hat on,
showing the long face, high forehead, pointed beard, straight back, great
height and both hands resting on the pommel.

View (d): full length in his river state, hatless and drenched from head
through chest. His straight dark hair forms heavy wet clumps pressed flat to
the temples, skull and neck. The blue cassock is saturated and markedly darker
across the chest; its collar has collapsed with water and the cassock and black
doublet hang heavy and cling to the torso in wet vertical folds. This soaked
state must be unmistakable in grayscale and at thumbnail size. The sword stays
at his hip. He remains upright and controlled, extending his right arm straight
forward with the hand open, palm up, offering it; his face is quiet and grave,
not pleading. The ground stays plain and dry-looking: no river, bank, puddle,
splash, rain or suspended droplets.

Identity separations: Athos is a head taller than Rochefort, with a pointed
beard, no scar, shoulder-length hair, a blue-and-white cassock, a white plume
and a still vertical posture; Rochefort has only a thin moustache, a left-cheek
scar, collar-length hair, black clothes, a red feather, weight back and chin
up. Athos is thirty, dark-haired, broad-shouldered and standing; the Cardinal
is older, grey, narrow and seated. Athos never has a scar, sling, stomach, red
hair, fair hair or book.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 07 — ROCHEFORT (continuity sheet, anchored on Volume I's approved 07, no injury)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume I sheet as an identity,
palette, and costume continuity reference: this is the same man a few months
later. The binding face, hair, build, and scar construction below takes
priority. He is uninjured, with two free, whole arms: no sling and no arm held
to the chest.

Rochefort, forty, is a compact middle-height fighting man, taller than
d'Artagnan and a head shorter than Athos. Give him broad shoulders, chest,
forearms, and thighs, but keep him far narrower than Porthos; his full-length
proportions must read compact rather than tall or long-legged. His default
stance is unmistakably weight-back, chest open, and chin raised, amused at
someone else's expense.

His skull is short, broad, square, and hard: a short lower facial third,
nearly parallel jaw sides, and a broad flat chin. He has sallow skin, heavy
black brows, black eyes, and a moustache reduced to one thin black line. The skin below his lower
lip and across his chin is clean: no beard, goatee, lip tuft, or stubble mark.
His straight black hair ends in one blunt line at the collar, with no wave,
curl, feathered end, or lock below the collar, including when bareheaded.

He has one pale scar on his anatomical LEFT side, continuous from the left
temple across the left cheekbone to the left corner of the mouth. In every
left-side view below, his nose points screen-right and the scarred left plane
faces the viewer. His anatomical right cheek is completely unmarked, with no
scar or scar-like mark in any view. Keep the scar's path and endpoints
identical in all four studies.

His costume is an unbroken black value mass: black doublet, cloak, breeches,
boots, and hat; one plain black-hilted sword. Every button, cloak clasp, buckle,
belt fitting, sword guard, and other piece of hardware is blackened steel or
neutral near-black. Recolour all of that hardware to matte near-black blackened
steel in every view; retain no gold or bright-metal highlight. A single red
feather in the hat is the only colour accent. Never a cassock, cross, bright
metal fitting, blue garment, white plume, red robe, or extra prop.

View (a): a large head-and-shoulders left three-quarter study in even light,
hat on, nose pointing screen-right, scarred left cheek fully exposed. Make the
short square skull, broad flat chin, thin moustache, clean chin, and blunt
collar-length hair unmistakable.

View (b): full length in the default costume, body mostly frontal, head in the
same left three-quarter direction with the nose pointing screen-right. Weight
back, chin up, one hand on the sword hilt. The compact muscular proportions,
black silhouette, and single red feather must read at thumbnail size.

View (c): full length in a strict ninety-degree anatomical-left profile, nose
pointing screen-right. Show the scar as one continuous line from left temple
across cheekbone to mouth corner, with the short square skull, broad flat chin,
thin moustache, compact build, and straight collar-length hair unchanged.

View (d): full length and bareheaded. Redesign view (d) so Rochefort turns
toward sheet-left and exposes his anatomical left cheek to the viewer; place the
single scar only from the left temple across the left cheekbone to the left
corner of the mouth, and leave the anatomical right cheek completely clean. His
right hand holds the black hat with its red feather at his side; his left hand
rests on the sword hilt. Both arms are free and whole; the black cloak hangs
straight; the blunt collar-length hair is fully visible.

Views (a)–(d) contain no scenery. Rochefort must remain unmistakable from
Athos in grayscale, at thumbnail size, and in a costume-free face crop:
Rochefort is shorter and compact, with a short square face, broad flat chin,
thin moustache only, collar-length hair, left-cheek scar, weight-back pose,
and black value mass; Athos is a head taller and still, with a long pale face,
pointed beard, shoulder-length hair, blue-and-white value mass, and hands on
the pommel.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 04 — ARAMIS (continuity sheet, anchored on Volume I's approved 04)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume I sheet: this is the same
man a few months later, unchanged. Copy his face, his fair hair, his small
moustache and lip tuft, his build, cassock, collar, hat, sword and book in
views (a), (b) and (c) exactly as they are drawn there. This is a continuity
pass. Replace the attached sheet's fourth view (the rail and the handkerchief)
entirely with the new view (d) below.

Aramis, a Musketeer, twenty-four. Slim, of middle height, a hand shorter than
the tallest man in the book and half the width of the widest. Fine oval face,
smooth high forehead, small straight nose, large dark eyes with long lashes,
pale clear skin, a small mouth. Blond hair, fair and fine, curled to the collar
and always in order, never longer; a small neat blond moustache and a tiny
tuft under the lip; no beard. Stands with his weight on one hip. Habitual
gesture: two fingers touching the moustache before he speaks. Expression at
rest: polite, amused, and not telling you why.

Redraw the same face in all four views with a materially shorter nasal bridge
and reduced forward projection, preserving a straight contour; the strict
profile must read as a small short nose rather than a long pointed one.

Default costume, views (a), (b), (c): the blue cassock with the white cross,
immaculate, over a doublet of dove grey with a wide white lace collar; black
hat with one white plume; a slim sword with a silver hilt; a small
leather-bound book in a strap at his belt.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, the fine oval face, smooth forehead, large lashed dark eyes, small mouth,
the small neat blond moustache and lip tuft, the fair curls ending at the
collar.

View (b): full length, hat on, weight on one hip, two fingers at the
moustache, the book visible at the belt.

View (c): a true ninety-degree profile from hat to boots, same light, keeping
the slim build, the small nose, the moustache, and the curls ending at the
collar.

Views (a)–(c) have no scenery and no props beyond the sword, hat, and book.

View (d): the same man kneeling on one knee, bareheaded, the hat not shown,
head bowed, the small leather-bound book open in both hands, reading a prayer
quietly; the fine blond curls ending at the collar fully visible from above,
the small moustache and lip tuft unchanged; immaculate even here.

Aramis must never be confused with Milady. Differentiators that must survive
grayscale and thumbnail: an oval face with a small neat moustache and a tuft
under the lip against a heart-shaped woman's face with none; large dark eyes
against pale ice-blue; fine blond curls ending at the collar against pale
ash-gold ringlets far past the shoulder; a black hat with a white plume
against a bare head; a blue cassock against plum silk. He must never be
confused with d'Artagnan: blond against black, a moustache against none, his
cassock over dove grey against the boy's ochre. Never a beard, never dark
hair, never hair past the collar, never plum, never dishevelled.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 05 — CONSTANCE (continuity sheet, anchored on Volume I's approved 05)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume I sheet: this is the same
young woman a few months later, unchanged. Copy her face, freckles, curls,
cap, dress, apron with the small gold crown, keys and basket in views (a), (b)
and (c) exactly as they are drawn there. This is a continuity pass. Replace
the attached sheet's fourth view (the woman at the wooden rail) entirely with
the new view (d) below; no rail anywhere on the sheet.

Constance, twenty, the Queen's dresser. Small and quick, a head shorter than
the boy. Round face, soft chin, short straight nose, wide-set hazel eyes, dark
brows, a scatter of freckles. Dark brown hair in curls, pinned up under a
white linen cap, with strands always escaping. Slight, straight-backed,
hands never idle. Habitual gesture: looking up, chin lifted, as if up a stair
or along a road. Expression at rest: practical, and about to say something
true.

Default costume, views (a), (b), (c): a plain dress of dove grey with white
cuffs and a white apron whose bib carries one small embroidered gold crown;
a white linen cap; a ring of iron keys at her waist; a covered wicker basket
on her arm.

View (a): a true three-quarter head-and-shoulders study in even light, cap
on, the round face, soft chin, short nose, wide-set eyes, freckles, and the
escaping curls.

View (b): full length, cap on, basket on her arm, keys at her waist, chin
lifted as if looking up a stair.

View (c): a true ninety-degree profile from cap to hem, same light, keeping
the small straight-backed figure, the short nose, and the cap.

Views (a)–(c) have no scenery.

View (d): the same young woman full length at the convent: the same light
dove-grey dress with white cuffs, no apron, no crown, no keys, a plain white
collar at the neck, the same white linen cap with curls escaping, a shallow
open straw garden basket on her arm; standing straight, chin lifted, looking
up and away as if watching a road from a window, the beginning of a smile.

Constance must never be confused with Milady. Differentiators that must
survive grayscale and thumbnail: small, a head shorter; dark brown curls under
a white cap against pale ash-gold ringlets; a round freckled face against a
pale heart-shaped one; light dove grey with a white collar against dark
charcoal and a black veil; hazel eyes against ice-blue. Never finery, jewels,
plum, silk, or pale-gold hair; never taller than the boy; never a veil.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 03 — PORTHOS (continuity sheet, anchored on Volume I's approved 03)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume I sheet: this is the same
man a few months later, unchanged. Copy his face, moustache, curls, bulk,
cassock, crimson doublet, gold baldric, plumed hat and single heavy sword in
views (a), (b) and (c) exactly as they are drawn there. This is a continuity
pass. Replace the attached sheet's fourth view (the back of the baldric)
entirely with the new view (d) below.

Porthos, a Musketeer, thirty-five. Enormous: the widest man in the book by
half, chest like a barrel, big hands, a head taller than the boy. Round ruddy
face, heavy jaw, small bright blue eyes, a big nose. Red-brown hair in thick
curls to the collar; a great red-brown moustache waxed out to points; no
beard. Stands chest out, fists on hips, feet planted wide. Habitual gesture:
one hand smoothing the front of his baldric. Expression at rest: delighted
with himself.

Default costume, views (a), (b), (c): the blue cassock with the white cross,
strained across the chest, over a doublet of crimson; a wide shoulder-baldric
heavily embroidered with gold across the front; a black hat with the great
mass of red ostrich plumes drawn on the attached sheet, the largest hat in the
book; exactly one heavy sword with a gilt hilt.

View (a): a true three-quarter head-and-shoulders study in even light, hat
on, the round ruddy face, heavy jaw, small bright eyes, big nose, the waxed
red-brown moustache, and the curls to the collar. No beard.

View (b): full length, hat on, chest thrust out and feet planted wide, one
fist on the hip, the other hand flat on the gold baldric.

View (c): a true ninety-degree profile from plumes to boots, same light,
keeping the bulk, the barrel chest, the moustache points, and the plumes,
both fists on hips.

Views (a)–(c) have no scenery and no props beyond the sword and hat.

View (d): the same man full length, striding forward, hat on, with a big
lidded wicker hamper hooked over his left forearm, as wide as his chest, and
a cooked chicken leg in his right hand, mouth open in a laugh. The one heavy
sword at his hip.

Porthos must never be confused with Athos: bulk against leanness, red-brown
hair against dark, the red plumes against one white, loud against still. Never
a beard, never lean or still, never without the baldric, never anything neat.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## 06 — THE CARDINAL (continuity sheet, anchored on Volume I's approved 06)

A character reference sheet, 1536 × 1024 landscape, four views of the same
figure on one plain warm-paper ground, no lettering of any kind, no labels, no
borders between views. Attach the approved Volume I sheet: this is the same
man a few months later, unchanged. Copy his face, beard, cropped grey hair,
skullcap, red robe and cape, gold cross, the black chair and the grey cat in
views (a), (b) and (c) exactly as they are drawn there. This is a continuity
pass. Replace the attached sheet's fourth view (standing with the opened
letter) entirely with the new view (d) below; no letter, paper or seal
anywhere on the sheet.

The Cardinal, forty-five. A thin ascetic man: long narrow face, hollow
cheeks, high forehead, a thin high-bridged nose, pale grey hooded eyes that
do not blink, pale skin. Grey hair cropped close under the cap; a short
pointed grey beard and a thin grey moustache, both precise. Narrow-shouldered,
long-fingered. Seated whenever possible. Habitual gesture: one hand stroking a
grey cat on his lap; the hand never stops. Expression at rest: calm, and
already decided.

Default costume, views (a), (b), (c): a cardinal's robe and short cape of one
saturated vermilion red, a red skullcap, a small gold cross on a chain at the
chest. No sword, no hat with a feather.

View (a): a true three-quarter head-and-shoulders study in even light, cap
on, the long hollow-cheeked face, thin high-bridged nose, pale hooded
unblinking eyes, and the precise grey pointed beard and thin moustache.

View (b): seated in a plain high-backed black chair, the robe falling to the
floor, a grey cat on his lap, one long hand on the cat. This is his default
full-length view; he does not stand for it.

View (c): a true ninety-degree profile, seated, same light, keeping the thin
nose, the cropped grey hair under the cap, and the pointed beard.

Views (a)–(c) have no scenery beyond the chair.

View (d): the same man seated on a plain wooden chair, full length, in
secret: a plain dark brown-grey travelling cloak thrown over the red robe and
fastened at the throat, its hood down on his shoulders, so that the saturated
red shows clearly at the throat, at both cuffs and in a strip down the front
to the hem; the red skullcap on; no cat; his long hands folded on one knee;
the same calm face. The cloak is plain wool, dark brown-grey, never black.

The Cardinal must never be confused with Athos. Differentiators that must
survive grayscale and thumbnail: grey against dark; cropped hair under a cap
against hair to the shoulder under a plumed hat; seated against standing; red
against blue; forty-five against thirty. Under the travelling cloak he must
never be confused with Rochefort: a grey precise beard and hollow cheeks
against a thin black moustache, a square jaw and a scar; the red always
showing against all black; a red skullcap against a hat with a red feather.
Never black clothes, never a scar, never a sword, never a raised hand.

*(register paragraph, verbatim)*

Their faces must remain structurally distinct even in profile, reduced scale,
grayscale, partial hair, and travel clothes.

## Board prompts (critic-only rasters, generated from the attached approved sheets)

`board-heads` and `board-silhouette-grayscale` are crop-and-place from
approved pixels (`tools/boards.py`), never generated; the silhouette test is
the two generated boards below.

- **adversarial-silhouettes-a.** The five men from the attached sheets — the lean beardless boy in ochre with his grey hat and too-long sword, the tall still Musketeer with the pointed dark beard and white plume, the huge Musketeer with the red plumes and gold baldric, the slim fair Musketeer with the white plume, and the compact man in black with the red feather — isolated full bodies in their default costumes (each sheet's view (b)), each complete from hat to boots with sword included, standing at one common true relative scale on one shared floor line on one uniform plain light ground, no scenery, no shadow and nothing touching any figure. Top row: the five as true solid black binary silhouettes, filled solid with no interior white marks. Bottom row: the same five, same poses, in matched pure grayscale. No lettering. Each figure exactly as on its sheet; Athos's anatomical crown is one complete head-height above Rochefort's anatomical crown in both the black silhouettes and the rendered figures. Do not obtain the difference through hat or feather height: keep Athos tall, vertically still, and hands-folded, while Rochefort remains middle-height, wiry, chin-up, and hip-cocked. The huge one half again as wide as anyone, the boy the smallest.
- **adversarial-silhouettes-b.** The six figures from the attached sheets — the tall pale-haired woman in the plum gown, the small young woman in grey with the white cap, the slim fair Musketeer with the white plume, the thin man in the red robe seated in his black chair with the grey cat, the tall still Musketeer with the pointed dark beard, and the man in black with the red feather — isolated full bodies in their default costumes (each sheet's view (b)), each complete from head to feet, at one common true relative scale on one shared floor line on one uniform plain light ground, no scenery, no shadow and nothing touching any figure. Keep Athos and Rochefort adjacent at equal scale. Top row: true solid black binary silhouettes, filled solid with no interior white marks. Bottom row: the same six in matched pure grayscale. Add matched strict 90-degree profile head pairs for Milady and Constance, Milady and Aramis, Athos and the Cardinal, and Athos and Rochefort; within every pair, show both heads at identical head height and in the same strict 90-degree orientation, retaining the approved face structures and primary markers rather than relying on costume or pose. Select Rochefort's left-cheek profile so the left-cheek scar is visible. No lettering. Each figure exactly as on its sheet; the woman in plum a full head taller than the young woman in grey, her long ringlets readable in the silhouette against the Musketeer's hat and collar-length curls. Athos is one head taller than Rochefort, with a full short pointed beard, one white plume and both hands folded on the pommel; narrow his torso and jaw, lengthen his face, restore the long straight nose and short pointed full beard, and keep his habitual still posture with both hands folded on the sword pommel. Rochefort has a clean chin, thin upturned moustache, one red feather, hand on hip and chin raised. Rebuild Rochefort on this board with black wavy hair falling past the collar to the shoulder tops, heavy black brows, a hard middle-length face with high cheekbones and an angular jaw, sallow olive skin, and one thin black upturned moustache over a completely clean chin. Remove the pale-blond ringlets, fine oval jaw, blond moustache, and any Aramis-like lip tuft. Keep him a head shorter than Athos with chin raised and one hand on his hip. When the left facial plane is exposed, preserve the single scar from left temple across cheekbone toward the mouth; keep the strict right-cheek profile clean. The revised Athos/Rochefort opposition must remain legible from face shape, beard state, height, and posture after colour, feather, cloak, and cassock are removed. For Constance, shorten the lower face, round and widen the cheeks, reduce the nose projection, restore visible freckles, and retain the dark curls under the plain white cap as her primary head marker. For Milady, shorten the nose projection and lower face, taper the jaw into the approved small chin, and preserve the high cheekbones and pale ash-gold ringlets extending far past the shoulders.
- **adversarial-athos-rochefort.** One unframed landscape board on a plain warm laid-paper ground, under flat even light, no props in hand. On the left third, the two men from the attached sheets full length, side by side on one floor line at one scale: the tall Musketeer one bare head taller, upright and still in his blue cassock with the white cross and white plume; the man in black compact, weight back, chin raised, one red feather. Rebuild the paired full-length view with both soles on the same baseline and make Athos's crown exactly one Athos-head height above Rochefort's crown; achieve this through body stature, not vertical placement, hat, hair, or cape. Preserve Athos's upright folded-hands posture and Rochefort's hand-on-hip, chin-up posture. On the right two-thirds, four matched costume-free head pairs in a clean two-by-two field with open paper between them, every crop ending at the jaw and upper neck, both men bareheaded: a neutral three-quarter pair; the same pair sharing one open-mouth alarm; strict left-cheek profiles with every nose pointing screen right; strict right-cheek profiles with every nose pointing screen left, this last pair in pure grayscale. Athos keeps the long pale narrow face, high forehead, hooded grey eyes, neat moustache, short pointed dark beard and long straight hair to the shoulder; Rochefort keeps the shorter square hard face, heavy black brows, strong jaw, thin black moustache, no beard, straight black hair ending at the collar. Rochefort's single pale scar is fixed from his left temple across the left cheekbone to the left corner of his mouth: continuous in the left-cheek profile, and his right cheek entirely unmarked in the right-cheek profile. Each face must be exactly the face on its sheet.
- **adversarial-milady-aramis.** One unframed landscape board on a plain warm laid-paper ground, under flat even light. On the left third, the two from the attached sheets full length, side by side on one floor line at true relative scale, as if on a river landing at night but drawn on plain paper: the tall pale woman in the plum gown, bareheaded, the ringlets down her back; the slim fair Musketeer in his blue cassock with his hat on. On the right two-thirds, four matched costume-free head pairs in a two-by-two field, crops ending at the jaw and upper neck, both bareheaded (the Musketeer's head as in his sheet's view (d)): a neutral three-quarter pair; a strict-profile pair; the pair sharing one cold, unsmiling stare; and the neutral pair repeated in pure grayscale. Milady keeps the heart-shaped face, small pointed chin, no facial hair, pale ice-blue eyes, pale ash-gold ringlets falling far past the jaw; Aramis keeps the oval face, the small neat blond moustache and lip tuft, the large dark eyes, the fine blond curls ending at the collar. Each face must be exactly the face on its sheet.
- **adversarial-milady-constance.** One unframed landscape board on a plain warm laid-paper ground, under flat even soft grey light. On the left half, the two women from the attached sheets full length, side by side on one floor line at true relative scale, each in her sheet's view (d) costume: the tall pale woman in the dark charcoal widow's dress with the black veil pushed back, a full head taller; the small young woman in the light dove-grey dress with the white collar, the white cap and the straw basket. On the right half, matched head pairs: a three-quarter pair in colour, a strict-profile pair in colour, and both pairs repeated below in pure grayscale. Milady keeps the heart-shaped pale face, ice-blue eyes and pale ash-gold hair bound up under the veil; Constance keeps the round freckled face, hazel eyes and dark brown curls escaping the cap. Each face must be exactly the face on its sheet.
- **adversarial-dartagnan-aramis.** One unframed landscape board on a plain warm laid-paper ground, under flat even light. Upper half: the two young men from the attached sheets, hats off, at identical scale and angle, crops ending at the jaw and upper neck with no cassock or collar: a neutral three-quarter pair in colour; a strict-profile pair in colour; the pair sharing one strong open-mouth alarm; the neutral pair repeated in pure grayscale. Lower half: both full length side by side at true relative scale, BOTH in the blue Musketeer cassock with the white cross — the boy exactly as his sheet's view (d), the cassock over his ochre doublet, his grey hat with the broken feather; the fair Musketeer exactly as his sheet's view (b) — once in colour and once in pure grayscale. d'Artagnan keeps the long projecting nose, sharp narrow chin, close-set eyes, the black hair falling into his eyes, a bare upper lip, weight forward; Aramis keeps the shorter nose, tapered oval chin, fine blond curls, the small moustache and lip tuft, weight on one hip. Each face must be exactly the face on its sheet.
- **adversarial-athos-cardinal.** One unframed landscape board on a plain warm laid-paper ground. Four matched tests at one scale under identical flat light, the two men from the attached sheets in each: a costume-free neutral three-quarter face pair; a costume-free strict-profile pair; a costume-free shared-reaction pair, both with the same clenched-jaw anger; a pure-grayscale repeat of the shared reaction. Costume-free means crops ending at the jaw and upper neck with no hat, skullcap, plume, collar, cassock, cloak, or red robe visible. Then, small along the bottom edge, the two full length at true scale: the tall Musketeer standing in blue, and the thin man seated in his view (d) dark brown-grey travelling cloak with the red showing at the throat, cuffs and hem. Athos keeps the long pale face filled at the cheek, hooded grey eyes, dark hair to the shoulder, short pointed dark beard; the Cardinal keeps the hollow cheeks, thin high-bridged nose, pale unblinking eyes, cropped grey hair, precise short grey beard. Each face must be exactly the face on its sheet.
- **live-pair-milady-constance.** A single unlettered story-scale image on the landscape canvas, composed as a wide quiet tableau at page scale: a small cloister of pale stone in soft grey northern light, a square garden of roses round a stone well, low round arches behind. On a stone bench in the cloister walk, the two women from the attached sheets sit side by side, turned toward each other, each in her sheet's view (d) costume: the tall pale widow in dark charcoal with the black veil pushed back, holding both of the young woman's hands in hers, smiling warmly; the small young woman in dove grey with the white collar and white cap, her straw basket beside her on the bench, looking up at the widow, glad. The widow's gold ring with its square dark stone visible on her left hand. No third figure. No balloons, no captions, no text of any kind. Each face must be exactly the face on its sheet; the widow is a full head taller even seated.
- **Note on all boards.** Critic-only rasters: never a page input, never a builder input for a sheet or plate, never shown to a page builder. The whole-cast gate judges the collision pairs on them. This note is not a prompt.

## Setting plates and the object plates

Each plate is 1536 × 1024 landscape, architecture and palette only, **no
figures, no lettering**. The register paragraph is appended by
`tools/refbrief.py`. A plate is **one study on one ground** unless its bullet
names its studies; a page that attaches a multi-study plate names the one study
it uses and says "one single continuous scene, never several panels" (method/07,
the montage from multi-view plates). The seven RELOCK bullets are the fallback
prompts if a relock critic returns REVISE; they are not generated otherwise.

- **obj-horse.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged: the same old buttercup-yellow gelding in the same four views, saddled and bare, with the same long slightly downturned head, modest withers, heavy calm posture, pale mane and tail, on one plain ground. No scenery, no figures, no lettering. The only yellow animal in the book; never cream, palomino, dun, or chestnut.
- **set-paris.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged: Paris from the last hill with grey-blue slate roofs, the brown river and the stone bridges with houses on them; the narrow street of tall leaning houses, mud and a corner; the great arched carriage door in a stone wall open on a courtyard — three vignettes feathered into one warm laid-paper ground with no rules or frames. No figures, no lanterns, no signboards.
- **set-house.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged: the narrow street door at night in rain with one warm lantern on a bracket beside it; the steep wooden stair seen from the bottom with one candle at the top; the attic with one street-facing window, one narrow bed, one bare table, one candle and one bare iron nail high in a beam — three vignettes feathered into one warm laid-paper ground. No figures.
- **obj-casket-pouch-ring.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged, object for object and count for count, on its pale field. This plate is never a page input in Volume II.
- **set-carmelite-field.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged: the meadow of long grass behind the high yellow stone wall, the big tree, the stone trough against the wall left of the full-height gap, at noon and at early morning, feathered into one warm laid-paper ground. No figures.
- **set-cardinal-study.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged: red hangings, a black desk with one bare candle as the only flame, maps, one plain high-backed black chair, no window and no daylight. Red and black only. No figures, no cat.
- **obj-milady-carriage.** One closed town carriage of the 1620s, alone on a plain warm-paper ground, in one clear three-quarter view from the front left: a black lacquered box body on four tall black-spoked wheels, a high empty coachman's box, a door with a plain black panel and no coat of arms, no crest, no device, no monogram; in its windows, curtains of deep plum silk drawn shut. Black, plum, a little dull silver at the handles; no horses, no shafts in use, no driver, no luggage, no lantern, no figures, no scenery, no lettering. It must never resemble the plain brown coach that takes Constance away, the Cardinal's red, or a gilded royal coach.
- **set-milady-square.** One single study: a tall, handsome town house of pale cream stone on the corner of a wide paved square in Paris, evening light warm and golden low across the stones. A broad front door of dark polished wood at the top of a short flight of stone steps, with a fanlight and dull silver fittings; above it, a row of tall first-floor windows with small iron balconies, the nearest one open and plum silk curtains stirring inside it, warm candlelight within; a high slate roof. The square in front is clean and wide, empty, with a stone kerb and a gutter. Gold light, pale stone, plum at the windows. No figures, no footman, no carriage, no hay cart, no signboard, no lettering. Never the narrow muddy streets of the boy's quarter or the Louvre.
- **set-milady-salon.** One single study, one continuous interior seen from the doorway: a grand salon in gold candlelight, walls hung with deep plum silk in tall panels framed in gilt moulding, one large gilt-framed mirror over a marble fireplace, a harpsichord with its lid open, a curved sofa upholstered in plum and a single gilt chair facing it, a few tall candlesticks lit; on the right wall, one tall window onto the square with heavy plum curtains looped back; at the back, a wide archway closed by a heavy plum curtain drawn halfway, and through the gap a small dim cabinet with a small writing table and one candle on it. Too beautiful, slightly too much. Line-led brush-and-ink drawing over warm laid paper with matte gouache, visible grain and chalky wash edges; no photographic surface, no glossy sheen. No portable objects on any table: no knife, no glasses, no papers, no flowers. No figures, no portraits with faces, no lettering. Never the Louvre's ballroom or Buckingham's white and gold; never red hangings like the Cardinal's study.
- **set-tavern.** One single study: a low Paris tavern room at evening, plastered walls and dark heavy beams, warm lamplight, a small leaded window onto the street; in the foreground one rough wooden table with exactly four plain wooden chairs round it, the table bare but for one candle; the rest of the room dim, with benches along the walls and a counter with casks at the back. Warm brown, amber and umber. Redraw the same room and preserve its composition and counts, but make the primary graphic structure explicit lamp-black brush-and-ink contours on every major beam, chair, table, window, counter, and cask; leave visible warm laid-paper grain across the plaster and quieter shadow fields; and replace the blended modeling with discrete matte raw-umber, yellow-ochre, and amber gouache washes whose drying edges remain visibly chalky. Do not add, remove, or rearrange the four chairs, foreground table, single table candle, street window, wall benches, counter, or rear casks. No figures, no hearth with a stovepipe, no signboard, no lettering. Never Athos's bare whitewashed room, never the Red Dovecote's low smoky common room, never an inn yard.
- **set-athos-room.** RELOCK fallback. Attach the approved Volume I plate and reproduce it unchanged: a bare whitewashed room in grey window light from a single window, one wooden chair, one empty table, one narrow bed with undyed grey-brown bedding, and one narrow-bladed rapier hanging on the wall; no flame, no loose objects. No figures.
- **set-camp.** One single study, seen from a low rise inside the King's lines: in the foreground and middle ground, rows of grey-white canvas tents among wet dun earth, cooking smoke drifting, a few cannon behind earth banks, plain pale pennants on poles with no devices; beyond, a deep zigzag trench line and earthworks ringing the land, then open, broken, cratered ground; on the skyline, the walled city of La Rochelle on its harbour — grey stone walls and towers, roofs and a church tower behind them — and the grey sea beyond with no ships. Wind, salt light, dun, smoke-grey and sea-grey. The ruined fort is NOT on this plate. No figures, no horses, no lettering, no flags with crosses or arms. Never Paris, never the green north road.
- **obj-poison-ring-and-bottle.** One borderless object plate on one uninterrupted warm-paper ground, four object studies with clear space between them, each a separate reference never copied as a group. Left: Milady's ring, closed — a gold ring set with one flat square violet-black stone in a raised box bezel, seen in three-quarter view. Second: the same ring, open — the square stone lifted on a tiny hinge like a lid, and in the small hollow beneath, a few grey grains; never a skull, never a death's-head, never a label. Third: one dark green glass wine bottle, corked, with a small blank paper tag tied round its neck with string; the tag completely blank. Right: one plain brown earthenware jug and exactly two plain clear drinking glasses, empty, side by side. No hands, no table, no scenery, no figures, no lettering or marks on any surface. The ring must never resemble the Queen's ring: no round faceted stone, no claw setting.
- **set-dovecote-common-room.** One single study, one continuous interior: the low common room of a lonely country inn at night, brown and smoky, a big stone hearth with a fire burning, one rough table with two benches, rush-strewn floor, smoke-blackened ceiling beams; against the side wall a small black iron stove whose black iron stovepipe runs straight up the wall and through a ragged hole in the plank ceiling into the room above, with one joint in the pipe visibly broken open at about a standing man's ear height; in the far corner, a steep dark wooden stair going up to a closed door at the top with a thin line of candlelight under it. Brown, umber and firelight below; one thin warm line above. Preserve the current continuous-room composition, object counts, stair-and-door placement, and broken-pipe state, but redraw the hearth, table, two benches, stove, stovepipe, stair, and upper door with explicit lamp-black brush contours; replace continuous blended texture and specular modeling with restrained raw-umber, yellow-ochre, and fire-orange matte gouache shapes, leaving visible warm laid-paper grain and chalky drying edges throughout the plaster, beams, floor, and shadows. No figures, no dice, no cups, no signboard, no lettering. Never the Paris tavern with its window on the street, never Athos's whitewash.
- **set-dovecote-upper-room.** One single study, one continuous interior: a small low room under the roof of a country inn at night, rough plank walls and floor, one small dark window looking onto an empty blue-black night heath and distant low horizon, with no neighbouring roof mass, tower, or lit windows, one plain wooden table with exactly one candle burning on it and two plain wooden chairs facing each other across it; the black iron stovepipe coming up through the floor beside the table and remaining the dominant vertical marker, with one unmistakably broken or disconnected open joint within the upper room and a visible open mouth or gap large enough to read at thumbnail, never represented as another closed collar or seam; a plain door. Keep the window itself dark so the one candle remains the room's sole light accent: deep brown shadow, warm wax light on the table. Line-led brush-and-ink drawing over warm laid paper with matte gouache, no photographic surface. No paper, pen, ink or seal on the table, no figures, no lettering. Never the Cardinal's red study, never the attic in Paris.
- **obj-cardinals-paper.** One borderless object plate on one uninterrupted warm-paper ground, two object studies with clear space between them, each a separate reference never copied as a group. Left: the pardon — one sheet of cream paper folded in three into a long narrow packet, no seal, no ribbon, its outer face plain. Right: the commission — one larger sheet of heavier cream paper lying flat, with one round red wax seal pressed at the foot of the sheet, centred, plain and unmarked, and an empty margin above it. Every paper surface completely blank: no handwriting, no signatures, no pseudo-letters, no glyphs, no lines, no watermarks. The two must stay distinguishable without colour by size and shape: the narrow folded packet with no seal against the large flat sheet with the seal. No hands, no desk, no pen, no figures, no lettering.
- **set-north-road.** One single study: a long straight dirt road running away to the horizon across flat country under a low grey sky, a line of tall poplars along one side bending in the wind, wet fields, and close by the road a low post inn of stone with a stable yard and a hitching rail; a curtain of rain coming in across the fields from one side. Grey, green-grey, wet earth brown. Redraw those two areas as uninterrupted mud, puddle, grass, and marsh texture, with every letterform, initial, monogram, signature, logo, and watermark removed. Preserve the current road, poplar line, inn massing, storm front, palette, and figure-free composition; the corrected plate must contain no glyph-like mark anywhere on the canvas. No figures, no horses, no milestone, no signboard, no lettering. Never the white southern road of the earlier volume, never the camp.
- **set-bastion.** One single study, inside the ruined fort of Saint-Gervais in bright smoky morning light: broken walls of grey stone and packed earth, gun embrasures, rubble and fallen blocks, one large flat fallen block of stone lying like a low table in the open floor, one bare pike standing upright in the earth with nothing on it; on the side toward the enemy, a tall cracked stone wall standing alone and leaning outward over a rough slope, a long crack running down it, plainly about to fall; through the gaps, the slope falling away toward the grey walls of the city in the distance. Stone grey, earth dun, white smoke. The tall wall is standing. No figures, no basket, no tablecloth, no food, no flag, no ladders, no lettering. Never the camp's tents, never the Paris streets.
- **set-bethune-cloister.** One single study: a small, quiet convent cloister of pale cream stone in soft grey northern light — a square garden of rose bushes in flower, red and pink, round a small stone well with a wooden cover in the centre, a gravel path; on all four sides a covered walk behind low round-arched arcades; in the walk in the foreground, a plain stone bench and beside it one small bare wooden table; across the garden, one deeper arch leading toward the convent's front gate. Pale stone, green leaves, rose red, soft grey light. Line-led brush-and-ink drawing over warm laid paper with matte gouache, no photographic surface. No figures, no nuns, no jug, no glasses, no basket on the bench, no statues with faces, no lettering. Never the Louvre, never Milady's gold salon, never a ruin.
- **set-bethune-gate.** One single study, seen from the road: a small convent of pale cream stone standing alone beside a long straight road across flat country in morning light; a high plain wall along the road with one arched wooden double gate in it, standing shut; above the wall, the convent's front with one upstairs window looking straight up the road, its shutters open; a small bell-cote on the roof; the road running away straight to the horizon past a line of poplars. Pale stone, grey-green fields, soft light. Rebuild the convent front as a narrow bay immediately behind the road wall and rotate its facade so its single upstairs window, with shutters open, is centered on and visibly looks straight down the road to the horizon. Keep that window unobstructed and allow no competing upper window. Replace the entire portal surround with one unadorned round stone arch flush in the pale wall, retaining only the shut wooden double leaves and simple iron hardware. Remove the pediment, finials, gate-mounted crosses or crests, and every carved glyph-like mark; keep the small roof bell-cote as the sole ecclesiastical silhouette marker. Re-light the plate with diffuse soft grey northern morning light under a pale overcast sky; shift the convent to pale cream stone, the flat fields to muted grey-green, and the road to cool earth with low-contrast shadows. Remove the cypress masses and replace them with restrained northern deciduous planting, while preserving the specified single line of poplars receding along the road. No figures, no horses, no carriage, no signboard, no lettering. Never a castle, never the Paris gate.
- **set-ferry-night.** One single study: a flooded river at night in a storm, lit by one flash of lightning. A ferry landing of black wet timbers jutting into the swollen water; a heavy rope running from a thick post on the landing out across the river into the rain, the far bank lost; tied to the landing on that rope, one flat ferry raft of heavy planks with low rails, and on a short post at the raft's corner one iron lantern, lit — the only warm light in the picture; downstream, a long white roaring line of a weir across the river. Black water, white foam and rain, one warm point. There is no other lantern anywhere. No figures, no horses, no carriage, no boat but the raft, no lettering. Never the calm Paris river.
- **set-ferry-dawn.** Attach the approved `set-ferry-night` plate: this is the same landing, the same timbers, post and river, at grey dawn after the storm, one single study. The river high, brown and calm. Redesign the plate by removing the raft in full, including its deck, rails, posts, reflection, and any mooring connection; retain the landing's black timber structure, and make the cut ferry rope the primary state marker by showing its severed end hanging visibly slack at the landing, with no rope spanning the river and no lantern anywhere. This primary marker must read immediately at thumbnail size. Replace the gold and peach illumination with diffuse cool grey first light over low grey cloud, retaining brown calm water without a warm reflective band. Reduce the weir to a low, distant, quiet pale line with no prominent vertical fall or bright foaming foreground edge. Wet grass on the bank. Brown, grey, quiet. No figures, no horses, no lettering. Never night, never rain.
- **End of plate prompts.** Nothing after this line is a prompt.
