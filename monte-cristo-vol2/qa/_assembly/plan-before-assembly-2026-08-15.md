# PRODUCTION PLAN — The Count of Monte Cristo, Volume II

**48 portrait pages. Paris, 1838.**

This document is the deliverable. It is written to be executed by someone who
has **not** read the other project documents, has **not** read Dumas, and does
not have the `monte` skill. Everything needed is copied in here, not referenced.

---

# 1 · How to use this plan

## What this book is

Volume II of a series. Volume I shipped at 55 pages and is the register anchor
and the identity authority; it lives at
`/Users/andresrodriguez/Documents/nano/monte-cristo-expanded/`.

Volume II is one story: **the Count of Monte Cristo destroys Fernand Mondego,
Comte de Morcerf**, and finds out what it costs. It is a book about appetite. The
Count is not serene, not above it, and not the hero — he is a man enjoying
himself, and the volume is honest about that without ever letting a character say
so.

Danglars and Villefort are set up and left standing. They belong to later
volumes. Nothing in this book resolves them.

## Who does what

| Role | May | May never |
|---|---|---|
| **Builder** | generate one candidate, self-audit, derive proofs, submit to the critic, prepare the next prompt | approve, promote, write to `pages/`, reroll on taste |
| **Critic** | read, transcribe, judge, return a verdict | edit, regenerate, promote, propose prompt wording |
| **Production lead** | release a page, promote bytes, hold a batch, redesign a page at the v4 ceiling | generate, or approve their own generation |

Run the critic as a **genuinely separate agent**. A critic simulated inside the
builder's context approves its own work.

## Standing rules

1. **The executor may not redesign a page.** A page that cannot be built as
   specified stops and goes back to the plan owner. Do not invent a fix.
2. **Start at page 1.** Never anywhere else.
3. **There are no prototypes.** Every generated page is a production candidate
   with a direct path into the finished book.
4. **One page in flight at a time.** While the critic reviews page N, prepare the
   page N+1 prompt and nothing else.
5. **No page generates until every character visible on it has an approved lock**
   in `refs/approved/`.
6. **If text will not survive the transcription test, restage or split the page.
   Never shrink the type.** An extra page is cheap. No page budget outranks this.

---

# 2 · Preflight

## Tool requirements

The image tool must be able to:

1. take **multiple reference images per call** (this plan uses up to 6);
2. run at **high input fidelity**;
3. emit **1024 × 1536 natively**.

If the available tool cannot take reference images, **stop and say so.** The
continuity mechanism of this book is attaching approved references and the
promoted previous page as *image inputs*. Prose descriptions are not a
substitute — a run that silently degrades to prose-locking drifts in identity
and register while its ledger still records that inputs were resolved.

**GPT Image 2 processes input images at high fidelity automatically. Do not add
an `input_fidelity` parameter.**

## Known-good invocations

- **Claude Code MCP** — `mcp__openai-image-2__edit_image`, `imagePaths` (1–16).
  Bills the OpenAI API.
- **Codex CLI** — `~/.codex/skills/imagegen/scripts/image_gen.py edit --image A
  --image B`. Bills the OpenAI API.
- **Codex in-app** — bills the ChatGPT subscription.

## Billing decision

> **RECORDED AT THE FORK — see the note at the head of §2 in the delivered copy.**
> The repository default in `AGENTS.md` is the **Codex in-app subscription
> path**. API billing requires explicit approval in the conversation where the
> run happens. This plan does not leave the decision open; whichever path was
> chosen is written here before execution begins.

## Format lock

- Story pages: **1024 × 1536, 2:3 portrait, RGB PNG.** Never landscape, never
  square, never mixed.
- Reference sheets: **1536 × 1024, 3:2 landscape.** This is deliberate and
  inherited; do not "fix" it.
- Proofs: **600 × 900 desktop** (binding) and **768 × 1152 tablet** (secondary).
- Lettering is **baked natively into the flattened page.** No HTML, SVG or CSS
  layer may repair a page.
- Every delivered page is one finished flattened image.

---

# 3 · The craft floor

Copied in full. This is the part of the method that gets dropped first.

## The three page modes

**Dramatic** — a scene between people, carried by balloons. 45–80 words
typical; ~105 only where large protected balloon lanes were reserved before the
faces were placed. 33 of the 48 pages.

**Illustrated prose** — a narrative field over one dominant image or a
continuous-time sequence. 50–120 words, 140 exceptional. Compose the prose field
*first*, then the art around it. 8 of the 48 pages.

**Spectacle or silence** — text under 15% of visual attention. One short line may
anchor scale or identity. 7 of the 48 pages.

**A book of nothing but dramatic pages fails.** Prose and spectacle pages buy the
dramatic pages their room. No movement in this volume runs more than five
dramatic pages without a prose or spectacle page, which is why pages **6, 13, 39
and 43 cannot be cut for budget.**

## Page architecture — blocking at every page gate

- **Exactly one dominant panel, occupying 45–70% of the page.** Declared in the
  prompt. The model will not infer hierarchy from a list of equal-sounding
  panels.
- **Panel shares sum to 100.**
- **At most two locations per page.** Only three pages carry two: **6, 25, 28.**
- **Exactly one dominant turn** — one thing changed, statable in one sentence.
- **The declared mode must be the mode rendered.**

## The numeric typography law

Inherited unchanged from Volume I
(`monte-cristo-expanded/06-PORTRAIT-TYPOGRAPHY-SYSTEM.md`). This volume relaxes
nothing.

| Property | Value |
|---|---|
| Canvas | **1024 × 1536 portrait** |
| Outer safe margin | **64 px** all sides |
| Minimum panel gutter | **24 px** |
| No essential text below | **72 px** from the bottom edge |
| Speech lettering height | **44–50 px** |
| Short-reply lettering | **48–54 px** where space allows |
| **Minimum approved lettering height** | **40 px — HARD FLOOR** |
| Balloon width | **240–390 px** |
| Maximum words per balloon | **~24** |
| Prose field lettering | **36–42 px** |
| Prose line length | **38–52 characters** including spaces |
| Prose paragraph | **2–5 lines** |
| Prose fields per page | **one or two**, never scattered |
| Prose field width | **78–88% of canvas** |
| Prose internal padding | **≥42 px** |

**Below 40 px is blocking. Between 40 and 54 px, do not measure and do not
reject.** A 43 px line that reads well is fine even though the target says 44.
Measuring against targets above the floor is the tolerance-exercise failure mode
that drove one Volume I page to v77 across 143 candidates.

**Three visible text levels only:** narrative prose · speech · small sound or
object label. Production titles, page titles, scene titles, speaker names and
editorial labels never appear in finished art.

**Banned letterforms:** condensed comic-display; modern geometric UI fonts;
cursive body text; all-capital prose; faux-aged or distressed forms; tiny
handwritten documents carrying essential facts; **the thin old-style italic serif
that a failed run of this method rendered at 27 px.**

Balloons are **warm ivory, never pure digital white**, with a restrained
charcoal-brown painted outline. Captions are matte parchment rectangles, tail-free,
integrated into calm image areas, never over busy art or faces.

## The register — Velvet Cinema

From `monte-cristo/01-STYLE-GUIDE.md`, binding on every page and every sheet:

> Mature historical graphic-novel realism painted in **layered matte gouache and
> opaque watercolor over sparse charcoal and ink construction.** Broad visible
> brushstrokes, simplified interlocking color shapes, bold shadow masses,
> selective hard edges at faces, hands and decisive objects, tactile cloth,
> stone, wood, paper, wax, metal and water, expressive anatomically credible
> faces, cinematic blocking without photographic lens effects.

**The register's enemy, named in every prompt: smooth prestige-oil realism.**
Also banned: glossy game-concept-art surfaces, airbrushed skin, dense engraved
cross-hatching, oil-painting pastiche, anime proportions, children's-book
softness, generic grimdark, steampunk decoration.

## The world palettes

| Location | Palette | Accent that does the work |
|---|---|---|
| The Count's house | lacquer black, ivory, cold grey daylight, unpolished new gold; **deliberately underfurnished** | the three lit roofs outside the window — other people's houses |
| The Morcerf house | burgundy, polished walnut, wax red, old gold, dense candle amber; **overstuffed with purchased legitimacy** | wax red — seals, ribbons, the decorations on Fernand's chest |
| Janina, 1822 & 1838 | white limestone, cypress black, Ionian blue, sun-bleached ochre, fire. **Horizontal where Paris is vertical; the only sky in the volume** | fire |
| The slave market | dust, bleached white, heat-glare, indigo shadow | restraint — a face and a hand let go of |
| Danglars' study | bottle green baize, brass, ledger calf, gaslight, coin-yellow | brass — everything that counts, weighs or locks |
| The newspaper office | ink black, newsprint grey, tallow, bare board | the only unluxurious room in Paris in this book |
| The Chamber of Peers | crimson benches, heavy gold, dark oak, cold high daylight from above | Haydée's crimson-and-gold dress, which rhymes with the benches |
| The Bois, dawn | pale grey-green, mist, wet black trunks, thin gold at the horizon | air — the one place the world breathes |
| The street at night | lacquer black, wet cobble, gas-yellow | the departing carriage lamp — the last warm thing, leaving |
| The Opera foyer | gilt, mirrors, gaslight, massed pale silk and black coats | the Count as the one unbroken black vertical in a moving crowd |

---

# 4 · The reference plan

Full sheet prompts are in `09-REFERENCE-PLAN.md`. This section carries what the
page executor needs.

## The approved locks

Page prompts attach files from `refs/approved/` **only**.

| File | Who | Notes |
|---|---|---|
| `refs/approved/01-count-1838.png` | The Count, 42 | unrelieved black, clean-shaven, swept-back black wave with first grey, columnar |
| `refs/approved/02-mercedes-1838.png` | Mercédès, 42 | **visibly forty-two** — temple and lower-lid lines, restrained grey. Views: evening gown; travelling black |
| `refs/approved/03-fernand-1838.png` | Fernand, 46 | heavy iron-black military moustache, receding temples, thickened build, chest of decorations. Views: decorations; shirtsleeves |
| `refs/approved/04-albert.png` | Albert, 22 | chestnut hair, fair-olive skin, pale waistcoat, open face. Views: default; bareheaded at dawn |
| `refs/approved/05-haydee.png` | Haydée, 27 | unbound black hair, olive-gold, crimson-and-gold Epirote, loose vertical silhouette |
| `refs/approved/06-danglars-1838.png` | Danglars, 55 | fleshy, side whiskers **no moustache**, short and thickening, expensive clothes fitting badly |
| `refs/approved/07-beauchamp.png` | Beauchamp, 28 | **small oval spectacles always**, untidy sandy hair, stooped, plain worn dark clothes |
| `refs/approved/08-villefort-1838.png` | Villefort, 53 | long narrow inverted triangle, very high forehead, iron-grey hard side part, rigid |
| `refs/approved/09-janina-1822.png` | Haydée at 11, and her mother | 1822 only |
| `refs/approved/17-set-count-house.png` | The Count's house | 3 views |
| `refs/approved/18-set-morcerf-house.png` | The Morcerf house and staircase | 3 views |
| `refs/approved/19-set-chamber.png` | The Chamber of Peers | exterior, floor, gallery |
| `refs/approved/20-set-janina.png` | Janina and the market | 3 views |
| `refs/approved/21-objects.png` | Key objects | glass, decanter, sealed document, case, decorations, newspaper |

Sheets **10, 11, 12–16 and 22** are cast boards and the live-pair proof. They are
**critic-only** and are never attached to a page prompt.

## The gate that blocks page generation

Nothing generates until the reference critic returns an unconditional APPROVED
on the whole cast **as a system** and the sheets are promoted to
`refs/approved/` with SHA-256 verification. Blocking criteria are in
`09-REFERENCE-PLAN.md`; the two that matter most are **Albert must never read as
a young version of the Count**, and **Mercédès must never be youth-washed.**

---

# 5 · Page prompts

One complete prompt per page. Use verbatim. Copy to
`qa/production/page-NN/prompts/page-NN-v1.md` **before** generating.

Where a prompt says to attach the promoted previous page, attach
`pages/page-[NN-1].png` as an image input. That is the continuity mechanism and
prose is not a substitute for it.

---

## PAGE 1 — *illustrated prose*

**Turn:** nine years have passed; the Count is in Paris with all three men inside
one window frame.
**Dominant:** the dark room, the window, the three roofs — 65%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-01/candidates/page-01-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 1
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism, continuous with Volume I: layered matte
> gouache and opaque watercolor over sparse charcoal and ink construction, broad
> visible brushstrokes, bold shadow masses, tactile plaster, glass, cold stone,
> lacquered wood and night air, selective hard edges only at the figure and the
> window frame. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness.
>
> Palette: **lacquer black, ivory, cold grey-blue night, unpolished new gold**,
> and — only outside the glass — warm lamp-yellow in distant windows. The
> interior is the coldest thing on the page.
>
> **Predecessor:** there is no image predecessor; this is page 1. No prior state
> carries in. **Do not show** any woman, any second figure, any servant, any
> crowd. One human being on this page and no other.
>
> **Character lock.** One supplied canonical reference binds the only visible
> figure. **The Count, 42:** tall, columnar, unnaturally still, clean-shaven,
> swept-back black hair with the first grey at the temples, cultivated pallor,
> **unrelieved black 1838 evening dress**. On this page he is seen **from behind
> and small in the frame** — his identity is carried by silhouette, not by face.
> Render the silhouette so that it is unmistakably a tall slim man in unbroken
> black with a swept-back dark head, and give no other figure that silhouette
> anywhere on the page.
>
> ### Panel 1 — **DOMINANT, roughly 65% of the page**, upper two-thirds
>
> Interior, from behind. An **enormous unlit room with almost nothing in it** —
> no clutter, no portraits, no family objects, no warmth, a room a rich man
> furnished without meaning to live in it. One **tall uncurtained window**. The
> man in black stands at the glass, small in the frame, back to us. Beyond him,
> Paris at night — and **three roofs close enough to count**, each with a lit
> window or two, at middle distance.
>
> One matte parchment prose field, **upper third of this panel, set against the
> dark blank wall — never over the window and never over the figure.** Cold-ivory
> parchment. Exactly this text, in two paragraphs:
>
> `Nine years after a shipowner in Marseille walked down to the harbour and found a ship he had lost sitting at anchor, a stranger bought the house at number thirty, Champs-Élysées.`
>
> `He paid in gold, he paid at once, and he furnished it the way a man furnishes a room he does not mean to live in. Within a month Paris had decided he was the most interesting person in France. Nobody could say where the money came from. Nobody asked twice.`
>
> ### Panel 2 — roughly 35% of the page, a **wide horizontal band across the bottom**
>
> The **three roofs alone**, no figure, no interior, no window frame — a wide
> night cityscape strip at rooftop level. Left: a roof with a **copper gutter**.
> Centre: a roof with a **flagpole**. Right: a roof with **every window lit**.
> The three must be visually distinguishable from one another at a glance and
> must be redrawable as the same three roofs on later pages.
>
> One matte parchment prose field in this band, in a calm dark area of sky,
> exactly this text, in two paragraphs:
>
> `From that window he could see three roofs.`
>
> `He had chosen the house for that.`
>
> **Lettering:** all **4** text blocks exactly once, with exact spelling, order,
> punctuation, capitalization, apostrophes and accents. This page has **no speech
> balloons and no speaking characters.** Prose fields: **36–42 px** lettering on
> the 1024 × 1536 canvas, never below **40 px** for any character; **38–52
> characters per line**; field width **78–88% of canvas**; internal padding **≥42
> px**; left-aligned with a calm ragged right edge; upright mixed-case literary
> serif. **No italics, no all-caps prose, no condensed display faces.** No
> quotation marks, no speaker labels, no page number, no title, no pseudo-text,
> no signature. Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** an empty cold enormous room → one man at the glass
> → three roofs he can count → he bought the house for the view. The three roofs
> established here are the same three roofs on page 2 and the same roof he looks
> up at on page 48.
>
> No second figure, no face, no furniture beyond the barest minimum, no fire in
> the grate, no identity collision, duplicated person or hand, fused fingers,
> illegible text, crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — binds the figure's silhouette, build and
>    costume.
> 2. `refs/approved/17-set-count-house.png` — binds the room, the window, and the
>    three roofs.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 2 — *dramatic*

**Turn:** he names his order of operations — the banker first, because the banker
is easy.
**Dominant:** the Count at the window, back to the room — 55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-02/candidates/page-02-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 2
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile glass, plaster, porcelain and
> lacquered wood, selective hard edges at faces and hands. **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey-blue night**, warm lamp-yellow only
> outside the glass, and **one restrained note of deep crimson and gold** on the
> seated woman — the only colour in the room.
>
> **Predecessor: attach the promoted page 1.** Same room, same window, same
> three roofs, same night, moments later. What carries: the room's emptiness and
> cold, the man's position at the glass, the exact arrangement of the three
> roofs.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with first grey at the temples, deep-set black-brown eyes, strong straight
> brow, long clean nose, high cheekbones, **a slight asymmetry at the left corner
> of the mouth**, cultivated pallor, **unrelieved black evening dress**.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set
> very dark eyes, straight brows, small straight nose, full mouth, slight build,
> direct unornamented stillness, **crimson-and-gold Epirote dress with a loose
> vertical silhouette — never a French 1838 waist and never a French coiffure.**
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — **DOMINANT, roughly 55% of the page**, top
>
> The Count at the window, **back to the room**, one hand flat on the glass, the
> night city and the three roofs beyond him. Far behind him in the dark of the
> enormous room, **Haydée seated**, small, with a cup she is not drinking from.
> She is silent in this panel and receives no balloon.
>
> One warm-ivory balloon, **upper left, over the dark wall**, short tail to the
> Count's head, exactly:
>
> `The copper gutter is the banker. The slate roof with the flagpole is the King's Attorney.`
>
> ### Panel 2 — roughly 15%, left of a three-panel lower tier
>
> Close: **his hand flat on the glass**, and through the glass the third house,
> every window burning. No face.
>
> One warm-ivory balloon, upper area of the panel, tail running off-panel toward
> the figure above, exactly:
>
> `And that one entertains. Every night, all season. He is very anxious to be liked.`
>
> ### Panel 3 — roughly 15%, centre of the lower tier
>
> **Haydée**, head and shoulders, watching **him** and not the window. Direct,
> unsmiling, entirely still.
>
> One warm-ivory balloon, tail to her mouth, exactly:
>
> `Which one first?`
>
> ### Panel 4 — roughly 15%, right of the lower tier
>
> The Count **three-quarters, turned into the room now**, lit from outside so the
> light comes off the window onto one side of his face. **Pleasure in the face —
> not calm, not serenity.** A man reading a menu. The slight asymmetry at the
> left corner of the mouth is doing work here.
>
> One warm-ivory balloon, tail to his mouth, exactly:
>
> `The banker. A man who lives on credit comes apart in one season, and quietly.`
>
> **Lettering:** all **4** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering
> **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**; balloons
> **240–390 px** wide; warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps.** Tails touch only the Count's and Haydée's mouths exactly as
> assigned; the Count owns three balloons and Haydée owns one. No captions on this
> page. No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** three roofs named as three men → the third one
> characterised with contempt → she asks the operational question → he answers
> with relish and picks the easy one first. The pleasure on his face in panel 4 is
> the engine of the whole book and must be visible.
>
> No third figure, no servant, no crowd, no fire, no clutter entering the room, no
> identity collision, duplicated person or hand, fused fingers, illegible text,
> crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the room, the window, the three
>    roofs.
> 4. `pages/page-01.png` — promoted previous page; binds room, window and roof
>    arrangement.
>
> All other character sheets are **prohibited generation inputs** for this page.

---
