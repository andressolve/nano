# PRODUCTION PLAN — The Count of Monte Cristo, Volume II

**49 portrait pages. Paris, 1838.**

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
| **Builder** | generate one completed candidate, record a non-gating audit, derive proofs, submit every completed candidate to the critic, prepare the next prompt | approve, promote, write to `pages/`, gate its own work, reroll without a critic verdict except for a failed generation |
| **Critic** | read, transcribe, judge, return a verdict | edit, regenerate, promote, propose prompt wording |
| **Production lead** | release a page, promote bytes, hold a batch, bring a v4 ceiling and split proposal to the owner | generate, approve their own generation, autonomously redesign after v4, modify the page contract or full script |

Run the critic as a **genuinely separate agent**. A critic simulated inside the
builder's context approves its own work.

## Standing rules

1. **The builder may not redesign or gate a page.** Every completed candidate is
   audited, proofed and submitted to the independent critic. The audit records
   findings; it is not a verdict.
2. **Start at page 1.** Never anywhere else.
3. **There are no prototypes.** Every generated page is a production candidate
   with a direct path into the finished book.
4. **One page in flight at a time.** While the critic reviews page N, prepare the
   page N+1 prompt and nothing else.
5. **No page generates until every character visible on it has an approved lock**
   in `refs/approved/`.
6. **If text will not survive the transcription test, restage or split the page.
   Never shrink the type.** An extra page is cheap. No page budget outranks this.
7. **Only a failed generation may be regenerated without a critic verdict:**
   wrong canvas, corrupt/truncated output, or gross anatomical breakage. Every
   other page judgment belongs to the critic.
8. **A v4 ceiling stops the run and comes to the owner.** The earlier autonomous
   redesign authorization is revoked. Do not generate v5, redesign, split, or
   change page count without owner direction. **The count is total generations
   of the page from v1 and never resets** — a redesign, restaging or new panel
   plan does not start a new count. The fourth image ever generated for a page
   is v4 whatever it is called.
9. **If a page resists three independent critic rounds, propose a split before
   adding a sixth panel.**
10. **Never modify `07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`.** They are
    owner-controlled story authorities. Model-compensation numbers belong only
    in the generation prompt.
11. **Neither lettering size nor panel share is a gate.** Both stay in every page
    prompt as construction targets; neither is ever measured against a rendered
    page. Reading is proved by transcription, hierarchy by eye.
12. **Work from `qa/_plan/page-NN.md`, never from this master file, and start a
    fresh session at every page boundary.** The per-page file carries identical
    law plus that one page's prompt and appendix at roughly an eighth the size,
    and `assemble.py` emits it in the same pass that builds this file, so the two
    cannot drift. Restarting costs nothing — the ledger, the critic reports, the
    promoted bytes and `RUN-LOG.md` hold every piece of state the run needs. See
    §6, *Instantiating the two agents*, for the measurement behind this rule.

---

# 2 · Preflight

## Tool requirements

The image tool must be able to:

1. take **multiple reference images per call** (this amended plan uses no more
   than 5 in any one in-app call);
2. run at **high input fidelity**;
3. emit **1024 × 1536 natively**.

If the available tool cannot take reference images, **stop and say so.** The
continuity mechanism of this book is attaching approved references and the
promoted previous page as *image inputs*. Prose descriptions are not a
substitute — a run that silently degrades to prose-locking drifts in identity
and register while its ledger still records that inputs were resolved.

**GPT Image 2 processes input images at high fidelity automatically. Do not add
an `input_fidelity` parameter.**

### Authorized five-reference transport amendment — 2026-08-15

The subscription-backed Codex in-app image tool rejected a six-image call with
the exact pre-generation error `referenced_image_paths must contain at most 5
paths`. No candidate was generated. The owner authorized this narrow transport
amendment:

- Sheets 10 and 11 are deterministic, unlettered QA boards assembled only from
  the approved pixels of sheets 01–08. They are critic-only and are never page
  inputs.
- Sheet 23 is a deterministic, unlettered carrier containing only approved
  setting sheet 19 and approved object sheet 21. Page 33 attaches the carrier
  instead of those two separate plates, leaving its three character locks and
  promoted previous page separate for a total of five inputs.
- These operations may crop, normalize, silhouette, resample and place pixels
  exactly as specified in `09-REFERENCE-PLAN.md`; they may not generate,
  repaint, invent or redesign content.

All generative work remains in-app and subscription-backed. This amendment does
not authorize the OpenAI API, prose substitution, page redesign or any
additional composite reference.

## Known-good invocations

- **Claude Code MCP** — `mcp__openai-image-2__edit_image`, `imagePaths` (1–16).
  Bills the OpenAI API.
- **Codex CLI** — `~/.codex/skills/imagegen/scripts/image_gen.py edit --image A
  --image B`. Bills the OpenAI API.
- **Codex in-app** — bills the ChatGPT subscription.

## Billing decision

> **DECIDED: Codex in-app, billed to the ChatGPT subscription.** This is the
> repository default in `AGENTS.md` and it is what the owner chose at the fork on
> 2026-08-15.
>
> **The OpenAI API path is not approved for this run.** Do not use
> `mcp__openai-image-2__edit_image` and do not use
> `~/.codex/skills/imagegen/scripts/image_gen.py`; both bill the API. If you find
> yourself unable to execute in-app, **stop and ask the owner** rather than
> falling back to an API call — the fallback is a billing decision, not a
> technical one.
>
> This constrains nothing else in the plan. Every reference manifest, canvas size
> and proof derivation below is identical on either path.

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
faces were placed. 34 of the 49 pages.

**Illustrated prose** — a narrative field over one dominant image or a
continuous-time sequence. 50–120 words, 140 exceptional. Compose the prose field
*first*, then the art around it. 8 of the 49 pages.

**Spectacle or silence** — text under 15% of visual attention. One short line may
anchor scale or identity. 7 of the 49 pages.

**A book of nothing but dramatic pages fails.** Prose and spectacle pages buy the
dramatic pages their room. No movement in this volume runs more than five
dramatic pages without a prose or spectacle page, which is why pages **6, 13, 39
and 43 cannot be cut for budget.**

## Page architecture — blocking at every page gate

- **Exactly one unmistakable dominant panel** — one panel that owns the page at
  a glance and carries its turn. **This is judged by eye and never measured.**
  The **45–70% construction target** stays in every page prompt, because the
  model will not infer hierarchy from a list of equal-sounding panels — but it is
  a builder instruction only. **Owner instruction, 2026-08-16: dominant share is
  not a gate at any level.** Critics do not measure, estimate or compute panel
  area, and a REVISE resting on a share value is void. This is the same
  correction already made for lettering height, made for the same reason.
- **Panel shares sum to 100** as declared in the prompt. A construction check on
  the prompt, never a measurement of the rendered page.
- **At most two locations per page.** Only three pages carry two: **6, 25, 28.**
- **Exactly one dominant turn** — one thing changed, statable in one sentence.
- **The declared mode must be the mode rendered.**

## Numeric typography construction targets

Inherited from Volume I
(`monte-cristo-expanded/06-PORTRAIT-TYPOGRAPHY-SYSTEM.md`). These remain useful
instructions for the builder; they are not critic gates.

| Property | Value |
|---|---|
| Canvas | **1024 × 1536 portrait** |
| Outer safe margin | **64 px** all sides |
| Minimum panel gutter | **24 px** |
| No essential text below | **72 px** from the bottom edge |
| Speech lettering height | **44–50 px** |
| Short-reply lettering | **48–54 px** where space allows |
| **Minimum lettering height** | **40 px** — a builder target, never measured at the gate |
| Balloon width | **240–390 px** |
| Maximum words per balloon | **~24** |
| Prose field lettering | **36–42 px** |
| Prose line length | **38–52 characters** including spaces |
| Prose paragraph | **2–5 lines** |
| Prose fields per page | **one or two**, never scattered |
| Prose field width | **78–88% of canvas** |
| Prose internal padding | **≥42 px** |

**Owner override, 2026-08-15: NO SWEATING ABOUT TEXT SIZE. Every number in this
table is a construction instruction for the builder. None of them is a gate.**
They belong in every page prompt, and they are what produces correct type. They
are never checked against a rendered page.

**Never measure lettering, at any size** — not glyph extent, x-height, cap
height or line pitch, not on the 1024 × 1536 source and not on the proof. The
**transcription test is the entire text gate**: a string that reads off the
600 × 900 proof is big enough, and a string that does not read is blocking
whatever it measures. A REVISE that cites lettering size while its own
transcription succeeded is void.

This is not a relaxation for convenience. Measuring type against these targets is
the tolerance-exercise failure mode that drove one Volume I page to v77 across
143 candidates, and it took this volume's page 1 to a v4 ceiling across four
reports that each stated the text was fully readable.

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
| `refs/approved/21-objects.png` | Key objects | glass, decanter, sealed document, case, decorations, newspaper, duelling-pistol case |
| `refs/approved/23-page-33-chamber-objects-carrier.png` | Page 33 transport carrier | deterministic, unlettered combination of approved sheets 19 and 21; no character identity |

Sheets **10, 11, 12–16 and 22** are cast boards and the live-pair proof. They are
**critic-only** and are never attached to a page prompt. Sheets 10 and 11 are
deterministic QA boards. Sheet 23 is not critic-only: it is the authorized
deterministic five-reference transport carrier attached only to Page 33.

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
> up at on page 49.
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

---

## PAGE 3 — *dramatic*

**Turn:** Haydée refuses his order of operations and puts Janina — in Greece — on
the table.
**Dominant:** Haydée full-figure, refusing, his stopping hand failing — 56%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-03/candidates/page-03-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 3
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile porcelain, cold glass, lacquered
> wood, plaster and candle-smoke, selective hard edges only at faces, hands and
> the cup. **Not smooth prestige-oil realism.** No glossy concept-art surfaces,
> no airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey-blue night, unpolished new gold**,
> warm lamp-yellow only outside the glass, and **one restrained note of deep
> crimson and gold** on the standing woman — the only colour in the room. The
> interior stays the coldest thing on the page.
>
> **Predecessor: attach the promoted page 2.** Same enormous underfurnished room,
> same tall uncurtained window, same three lit roofs beyond it, same night,
> seconds later. What carries in: the room's emptiness and cold, the low black
> table, **the cup she was not drinking from** — on this page she sets it down and
> it stays down — and both figures in exactly the clothes of page 2. **Do not
> show** any servant, any third figure, any crowd, any child, any other woman, any
> fire in the grate, any clutter arriving in the room. Two human beings on this
> page and no others.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **The Count, 42:** tall, columnar, habitually still; clean-shaven; swept-back
> black wave with the first grey at the temples; deep-set black-brown eyes; strong
> straight brow; long clean nose; high cheekbones; hollow temples; **a slight
> asymmetry at the left corner of the mouth**; cultivated pallor; **unrelieved
> black 1838 evening dress**, the only unbroken black vertical in the room.
> **Haydée, 27:** olive-gold skin; **long unbound black hair** or one heavy braid;
> large wide-set very dark eyes; straight brows; small straight nose; full mouth;
> slight build; direct unornamented stillness — she looks at people straight and
> does not arrange her face; **crimson-and-gold Epirote dress, loose vertical
> silhouette, no corsetry — never a French 1838 waist, never a French coiffure,
> never a bonnet.**
>
> **Collision prohibition.** Haydée must never read as a French comtesse of
> forty-two with a sculpted formal coiffure and a fitted burgundy-black gown; she
> is twenty-seven, unbound-haired, and loose-silhouetted. The Count must never
> carry a heavy military moustache, a receding hairline, a thickened soldier's
> build, or a young man's chestnut hair and pale waistcoat.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on all four panels:** Haydée holds the **left** of
> every panel she is in; the Count holds the **right**. Every balloon sits on its
> owner's side.
>
> ### Panel 1 — roughly 20% of the page, a wide horizontal band across the top
>
> Haydée at the left of the band, **setting the porcelain cup down** on the low
> black table and rising to her feet in one motion. She does not come closer to
> him. At the right of the band, the Count at the glass, half in silhouette,
> **not yet turned** — he has not registered the interruption.
>
> One warm-ivory balloon, upper left over the dark blank wall, tail to her mouth,
> exactly:
>
> `Then take him apart in the spring.`
>
> ### Panel 2 — roughly 12%, a wide horizontal band directly below
>
> The Count occupying the **right third** of the band, half-turned from the
> window, caught mid-pleasure and interrupted; the rest of the band is empty dark
> room. **Annoyance, not menace** — a man enjoying himself who has been stopped.
>
> One warm-ivory balloon, right of the band over dark wall, tail to his mouth,
> exactly:
>
> `You are not listening to me.`
>
> ### Panel 3 — roughly 12%, a wide horizontal band directly below that
>
> Haydée standing at the **left third** of the band, level, unhurried, entirely
> still. The Count is out of this panel or reduced to a dark edge at the extreme
> right.
>
> One **wide flat** warm-ivory balloon occupying the left two-thirds of the band,
> set in **two or three lines**, tail to her mouth, exactly:
>
> `I listened. You said the banker was simple. You did not say he was first.`
>
> ### Panel 4 — **DOMINANT, roughly 56% of the page**, the whole lower half
>
> **Haydée full-figure, small in the frame and absolutely still**, standing
> centre-left against the enormous dark room — the emptiness around her is the
> point and must be given room. In the **near foreground at the right edge**, out
> of focus and much larger, **the Count's poised right hand slightly raised**
> together with the dark out-of-focus edge of his shoulder — the gesture that
> stops other people, not working. His face is not visible in this panel.
>
> Three warm-ivory balloons. **The Count's is the highest element in the panel and
> is read first:** place `Haydée.` at the top right, small, with a short tail
> running into the dark beside his out-of-focus shoulder at the right edge — the
> tail must **not** touch or point at the raised hand. Her two balloons then drop
> down the left side, the first above the second. Exact strings, in this reading
> order:
>
> `Haydée.`
>
> `In Greece, in a lake town called Janina, they carried my father's head through the streets on a pike. I was eleven.`
>
> `The man who sold him is at dinner tonight, three streets from this room. And you want to begin with a bank.`
>
> **Lettering:** all **6** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization, apostrophes and accents — including the
> accent in **Haydée**. Balloon lettering **44–50 px** on the 1024 × 1536 canvas,
> **never below 40 px** for any character; balloons **240–390 px** wide, except
> the two long strings in panels 3 and 4, which run **wide and flat** across their
> reserved lanes rather than tall — **if a string will not set at 44 px inside its
> lane, widen the balloon and reduce the figure's scale; never reduce the
> lettering.** Warm ivory fill, never pure digital white, with a restrained
> charcoal-brown painted outline; upright mixed-case. **No italics, no condensed
> display faces, no all-caps.** **Haydée owns four balloons; the Count owns two**
> (panel 2, and `Haydée.` in panel 4). No captions and no prose fields on this
> page. No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** she sets the cup down → he is interrupted
> mid-appetite → she refuses his order of operations → she names Janina, Greece
> and the pike in a Paris drawing room → his stopping hand does not stop her. The
> cup is set down in panel 1 and is never picked up again on this page.
>
> **Page-specific prohibitions:** **do not depict the head, the pike, the streets
> of Janina, any flashback inset, any memory vignette, or any blood.** That
> atrocity is spoken, never shown, on this page. No sky, no daylight, no second
> room, no servant, no crowd. Standing prohibitions: no identity collision, no
> duplicated person, hand or object, no fused fingers, no illegible text, no crop
> sheet, no outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the room, the window, the three
>    roofs.
> 4. `pages/page-02.png` — promoted previous page; binds room, window, roof
>    arrangement, costumes and hour.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 4 — *dramatic*

**Turn:** she names the real reason he left Morcerf for later — Mercédès.
**Dominant:** two faces in three-quarter opposition, the accusation landing —
55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-04/candidates/page-04-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 4
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile plaster, cold glass, lacquered wood
> and candle-smoke, selective hard edges only at the two faces and at the door
> frame. **Not smooth prestige-oil realism.** No glossy concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey-blue night, unpolished new gold**,
> with **one restrained note of deep crimson and gold** on the woman. Candle amber
> is admitted only as a small close warmth on the two faces in the dominant panel;
> the room stays cold.
>
> **Predecessor: attach the promoted page 3.** Same room, same night, continuous —
> this page begins in the second after page 3 ends. What carries in: both
> costumes unchanged, the cup left standing on the low black table, the window and
> the three roofs in the same arrangement, the same candle level. **Do not show**
> any servant, any third figure, any crowd, Fernand, Albert, Mercédès, or any
> woman other than Haydée. Two human beings on this page and no others.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **The Count, 42:** tall, columnar, habitually still; clean-shaven; swept-back
> black wave with the first grey at the temples; deep-set black-brown eyes; strong
> straight brow; long clean nose; high cheekbones; **a slight asymmetry at the
> left corner of the mouth**; cultivated pallor; **unrelieved black 1838 evening
> dress**.
> **Haydée, 27:** olive-gold skin; **long unbound black hair** or one heavy braid;
> large wide-set very dark eyes; straight brows; small straight nose; full mouth;
> slight build; direct unornamented stillness; **crimson-and-gold Epirote dress,
> loose vertical silhouette — never a French 1838 waist, never a French
> coiffure.**
>
> **Collision prohibition.** Haydée must never read as a sculpted-coiffure French
> comtesse of forty-two in a fitted burgundy-black gown — that woman is a
> different character in this book and does not appear on this page. The Count
> must never carry a military moustache, a receding hairline, a thickened build,
> or chestnut hair and a pale waistcoat.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on all four panels:** Haydée holds the **left**,
> the Count holds the **right**, and every balloon sits on its owner's side.
>
> ### Panel 1 — roughly 20%, upper left, sharing the top tier with panel 2
>
> The Count, **recovering**: reasonable, courteous, the voice he uses on Paris.
> Half-length, at the right of this panel, the raised hand now lowered. Haydée is
> present only as a dark still edge at the left margin of the panel; **she is
> silent here and receives no balloon and no tail fragment.**
>
> One warm-ivory balloon, upper right of the panel, tail to his mouth, exactly:
>
> `The Morcerf house is difficult. There are more people in it.`
>
> ### Panel 2 — roughly 15%, upper right, completing the top tier
>
> Haydée, head and shoulders, **unmoved** — not angry, not pleading, simply not
> moving. She is at the left of this panel and looks across the gutter toward the
> Count's panel.
>
> One warm-ivory balloon, upper left of the panel, tail to her mouth, exactly:
>
> `There is one more person in it.`
>
> ### Panel 3 — **DOMINANT, roughly 55% of the page**, a wide band across the
> middle and lower-middle
>
> **Two faces, near, in three-quarter opposition.** Haydée at the left facing
> right, **level**; the Count at the right facing left, **not level** — the
> composure is coming apart in small increments across the panel. Nothing else in
> frame but dark room and one candle. Reserve the upper-left and lower-right of
> this panel as balloon lanes before placing the faces.
>
> Four warm-ivory balloons. Her three drop down the left side, each below the
> last; his single reply sits at the **lower right**, beneath the lowest of hers.
> Exact strings, in this reading order:
>
> `I have lived in your house four years and you have never once said her name to me.`
>
> `You say Mondego. You say the banker, the attorney.`
>
> `You say the woman.`
>
> `That is enough.`
>
> **The third string renders as plain upright mixed-case lettering with no
> emphasis of any kind** — no italics, no bold, no asterisks, no underline, no
> enlargement, no quotation marks. The weight of the line is carried by her face
> and by the Count's, not by the letterforms.
>
> ### Panel 4 — roughly 10%, a shallow wide band across the bottom
>
> Haydée at the door at the **left**, one hand on the frame, **not looking back**,
> already half through. The room and the Count are small, dark and out of focus
> to the right.
>
> One **single-line** wide low warm-ivory balloon spanning the left three-quarters
> of the band, tail to her mouth, exactly:
>
> `I am not the one who is afraid of a house.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px** for any character;
> balloons **240–390 px** wide, except the long strings in panels 3 and 4, which
> run **wide and flat** across their reserved lanes — **if a string will not set
> at 44 px inside its lane, widen the balloon; never reduce the lettering.** Warm
> ivory fill with a restrained charcoal-brown painted outline; upright mixed-case.
> **No italics, no condensed display faces, no all-caps.** **Haydée owns five
> balloons; the Count owns two.** No captions and no prose fields. No quotation
> marks, speaker labels, page numbers, titles or pseudo-text. Comfortably readable
> when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** he answers the Janina charge with logistics → she
> corrects the count of people in the house → she names the four years and the
> name he has never said → he shuts her down instead of denying it → she leaves
> before he can cover it. **The woman being discussed is never shown, named, or
> depicted anywhere on this page.**
>
> **Page-specific prohibitions:** no portrait, miniature, locket, silhouette,
> memory inset or vignette of the woman under discussion; no flashback; no
> Marseille; no daylight; no sky. Standing prohibitions: no identity collision, no
> duplicated person, hand or object, no fused fingers, no illegible text, no crop
> sheet, no outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the room, the window, the door.
> 4. `pages/page-03.png` — promoted previous page; binds room, costumes, candle
>    level and hour.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 5 — *dramatic*

**Turn:** he concedes, names Mondego as Morcerf, and says out loud that he will
enjoy it.
**Dominant:** the Count turning fully into the room, aimed — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-05/candidates/page-05-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 5
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile plaster, cold glass, wax, guttering
> tallow and lacquered wood, selective hard edges at the face, the flat hand and
> the door frame. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness.
>
> Palette: **lacquer black, ivory, cold grey-blue night, unpolished new gold**,
> **one restrained note of deep crimson and gold** on the woman, and — new on this
> page — **lower, redder candle amber**, because the candles have burned down. The
> shadow masses are deeper than on page 4 and the window is colder.
>
> **Predecessor: attach the promoted page 4.** Same room, same night, **later**.
> What carries in: both costumes unchanged, the cup still standing where she left
> it, the window and the three roofs in the same arrangement. **The one visible
> change is time: the candles are lower and the room is darker.** Haydée left the
> room at the end of page 4 and **is absent from panel 1 entirely**; she returns
> in the doorway in panel 2. **Do not show** any servant, any third figure, any
> crowd, Fernand, Albert, Mercédès, or any woman other than Haydée.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **The Count, 42:** tall, columnar; clean-shaven; swept-back black wave with the
> first grey at the temples; deep-set black-brown eyes; strong straight brow; long
> clean nose; high cheekbones; hollow temples; **a slight asymmetry at the left
> corner of the mouth**; cultivated pallor; **unrelieved black 1838 evening
> dress**.
> **Haydée, 27:** olive-gold skin; **long unbound black hair** or one heavy braid;
> large wide-set very dark eyes; straight brows; small straight nose; full mouth;
> slight build; direct unornamented stillness; **crimson-and-gold Epirote dress,
> loose vertical silhouette — never a French 1838 waist, never a French
> coiffure.**
>
> **Collision prohibition.** Haydée must never read as a French comtesse of
> forty-two with a sculpted coiffure and a fitted burgundy-black gown. The Count
> must never carry a military moustache, a receding hairline, a thickened
> soldier's build, or a young man's chestnut hair and pale waistcoat.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule:** Haydée holds the **left**, the Count the **right**, in
> every panel where both appear. **Reserve the balloon lanes on this page before
> placing any figure** — this page carries more speech than any page before it.
>
> ### Panel 1 — roughly 12%, upper left, a tall narrow panel sharing the top tier
> with panel 2
>
> **Silent panel — no balloon, no caption, no tail fragment.** The Count alone at
> the tall window, seen from behind and slightly below, the night city beyond.
> **The poised right hand has gone flat on the sill** — the one thing this panel
> exists to show; render the flat hand hard-edged and clearly readable at small
> scale.
>
> ### Panel 2 — roughly 18%, upper right, completing the top tier
>
> Haydée standing in the **doorway at the left of this panel — she came back**,
> and has not come further into the room. The Count at the right, turned partly
> toward her, still against the window. Both are at half-length or smaller; the
> upper two-thirds of this panel is a **reserved balloon lane** and the figures
> occupy the lower third.
>
> Two warm-ivory balloons. His is the **highest element in the panel** and is read
> first: a wide flat balloon in the upper right of the panel, set in three or four
> lines, tail to his mouth. Hers sits **below and to the left**, small, tail to her
> mouth. Exact strings, in this reading order:
>
> `When I found you and bought you back, I told you I would give you everything he took. I meant the money.`
>
> `I know what you meant.`
>
> ### Panel 3 — **DOMINANT, roughly 50% of the page**, a wide band across the
> middle
>
> **The Count turning fully into the room for the first time on the page** —
> three-quarter to nearly frontal, the window behind him now, low candlelight up
> one side of the face. **The appetite is back in the face and it is worse than
> before, because now it is aimed:** pleasure, appetite, a man who has been given
> permission. **Not serenity, not calm, not a smirk** — the slight asymmetry at
> the left corner of the mouth is doing the work. Haydée stands small and dark at
> the left edge, listening, **silent in this panel and receiving no balloon.**
> Reserve the left and upper-right of the panel as balloon lanes.
>
> Three warm-ivory balloons, all his, stacked so the reading path runs downward
> without crossing back. Exact strings, in this order:
>
> `I knew him when he mended nets. He could not write his own name; another man wrote it for him.`
>
> `He went east to Greece a fisherman's son, and came home a general.`
>
> `Paris calls him the Comte de Morcerf now, and nobody has ever asked him what he did there.`
>
> ### Panel 4 — roughly 20%, a wide band across the bottom
>
> The two of them at last in the same frame at the same distance: Haydée at the
> left, now a step inside the room; the Count at the right, still lit from the
> low candles. He is enjoying being corrected, which is its own kind of appetite.
>
> Three warm-ivory balloons. His first runs **wide and flat across the top of the
> band**; hers sits **lower left**; his last sits **lower right**. Exact strings,
> in this reading order:
>
> `You are right, and I am going to enjoy being told so more than I should. Morcerf first.`
>
> `How will you get into his house?`
>
> `I won't. He'll ask me.`
>
> **Lettering:** all **8** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px** for any character;
> balloons **240–390 px** wide for the short replies, and **wide and flat** across
> their reserved lanes for the four long strings — **this page's text load is at
> the ceiling: if a string will not set at 44 px, widen the balloon and shrink the
> figures; never reduce the lettering, and never let a balloon cross a panel
> border.** Warm ivory fill with a restrained charcoal-brown painted outline;
> upright mixed-case. **No italics, no condensed display faces, no all-caps.**
> **The Count owns six balloons; Haydée owns two** (panel 2 and panel 4). Panel 1
> and panel 3 contain **no** balloon belonging to Haydée. No captions and no prose
> fields. No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** the stopping hand lies flat and defeated on the sill
> → she comes back → he admits what he promised her and what he meant by it → he
> tells her who Mondego was before he was a Comte → he concedes the order of
> operations out loud and enjoys conceding → he says the enemy will invite him in.
> The flat hand in panel 1 is the same right hand that was raised and failing on
> page 3.
>
> **Page-specific prohibitions:** no Greece, no nets, no boats, no flashback, no
> memory inset, no Marseille, no daylight, no sky; **no wine glass and no decanter
> on this page** — the glass motif does not begin until page 8. Standing
> prohibitions: no identity collision, no duplicated person, hand or object, no
> fused fingers, no illegible text, no crop sheet, no outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the room, the window, the door.
> 4. `pages/page-04.png` — promoted previous page; binds room, costumes and
>    arrangement. **Time has advanced: the candles are lower than on that page.**
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 6 — *spectacle*

**Turn:** the invitation arrives — his enemy has asked him to dinner.
**Dominant:** the Morcerf house lit for a party — 65%.
**Locations:** 2 — the Count's hall, and the street outside the Morcerf house.
**Panels:** 3.
**Output:** `qa/production/page-06/candidates/page-06-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 6
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile engraved card stock, kid leather,
> wet stone, carriage lacquer, window glass and candle amber, selective hard
> edges at the card, the gloved hand and the lit doorway. **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> engraved cross-hatching, no children's-book softness.
>
> Palette moves across the page and the movement is the point. Panel 1 is **the
> Count's house**: lacquer black, ivory, cold grey, unpolished new gold, no
> warmth. Panels 2 and 3 are **the Morcerf house and its street**: burgundy,
> polished walnut, wax red, old gold and **dense candle amber pouring out of every
> window**, against wet black cobble. The cold page becomes the warm page and then
> ends in the dark at the end of the street.
>
> **Predecessor:** **do not attach page 5.** Page 5 ends in the black drawing room
> and this page opens in the hall and then crosses the city; it is not a visual
> predecessor and attaching it will drag the drawing-room window into the wrong
> panel. What carries in from page 5 by description only: the Count's unrelieved
> black, and the fact that he predicted this. **Do not show** Haydée, Fernand,
> Albert, Mercédès, Danglars, Villefort, or any legible face anywhere on this
> page. **No face appears on this page at all** — this is a page of a hand, a
> house and a carriage.
>
> **Character lock.** One supplied canonical reference binds the only human
> presence: **the Count, 42** — seen **only** as a gloved right hand and a black
> sleeve in panel 1, and as a black sleeve at a carriage window in panel 3.
> Identity is carried entirely by the **unrelieved black cloth, the long clean
> hand, and the stillness of the arm**. Give no other figure black cloth of that
> absolute value anywhere on the page, and do not render his face, hair or
> silhouette in any panel.
>
> ### Panel 1 — roughly 20%, a wide horizontal band across the top
>
> **Location one: the Count's hall.** A **gloved hand holding an engraved card at
> arm's length**, as if the card were slightly distasteful and entirely expected.
> The card is **large in frame**, held at a slight angle, cream, thick, plate-sunk.
> Behind it, only lacquer black and cold grey — no furniture, no servant, no
> door, no face, no second hand.
>
> The card carries **one legible line, rendered as an engraved object and not as a
> speech balloon**, centred on the card in upright engraved capitals, exactly:
>
> `LE COMTE DE MORCERF`
>
> This is the single permitted use of capitals on the page, and it is an object
> label, not prose. Any other marks on the card are illegible engraved texture
> only — **no address, no date, no second legible line, no signature.**
>
> ### Panel 2 — **DOMINANT, roughly 65% of the page**, the whole middle of the page
>
> **Location two: the Morcerf house at night, from the street.** **Every window
> lit.** Carriages stacked to the corner, horses steaming, footmen as small dark
> unfaced shapes. Through the open double doors, deep in the picture, **the
> general's staircase blazing** — the same staircase as the supplied setting
> plate, and it must be redrawable as the same staircase on later pages. Warm,
> crowded, gilt, **trying very hard.** The house is showing off and the painting
> should let it.
>
> One matte parchment caption rectangle, **upper left, tail-free**, set into a
> calm dark area of night sky or roofline — **never over a lit window and never
> over the doors** — warm cream parchment, exactly one word:
>
> `Thursday.`
>
> ### Panel 3 — roughly 15%, a wide horizontal band across the bottom
>
> **The same street, the far dark end of it.** A closed carriage stopped in the
> black, well away from the lights, lamp low. **A black sleeve resting at the open
> carriage window** — no face, no eyes, no reflected features in the glass. The
> lit house is a distant warm smear at the far end of the band, small enough that
> the reader understands the distance is deliberate.
>
> One warm-ivory balloon, sitting just above the carriage window, with a short
> tail ending in the **open dark inside the carriage window** beside the sleeve —
> the tail must not touch the sleeve and must not point at the lamp or the
> carriage body. It is the only balloon on the page. Exactly:
>
> `Four days he lasted. I thought he would manage a week.`
>
> **Lettering:** exactly **3** text elements on this page — **one** engraved
> object line, **one** caption, **one** balloon — each rendered exactly once with
> exact spelling, punctuation and capitalization. The engraved card line: upright
> engraved capitals, **not less than 56 px** tall on the 1024 × 1536 canvas,
> centred on the card, high contrast against the cream stock. The caption: matte
> parchment rectangle, lettering **40–42 px**, never below **40 px**, internal
> padding **≥42 px**, upright mixed-case literary serif, no tail. The balloon:
> lettering **44–50 px**, never below **40 px**, **240–390 px** wide, warm ivory
> fill with a restrained charcoal-brown painted outline, upright mixed-case. **No
> italics, no condensed display faces, no all-caps prose** — the card is engraving,
> not prose. No quotation marks, speaker labels, page numbers, titles or
> pseudo-text; no shop signs, no street names, no carriage lettering, no legible
> writing anywhere else on the page. Comfortably readable when the page is reduced
> to 600 × 900.
>
> **Continuity and meaning:** the card arrives in the cold house → the warm house
> is lit for a party on the named night → the man who was invited is sitting in
> the dark at the end of the street, counting how long it took. The staircase seen
> through the doors here is the staircase he climbs on page 8; the house is the
> house he enters on page 7.
>
> **Page-specific prohibitions:** **no faces anywhere, no crowd rendered in
> detail, no interior of the carriage, no reflection of a face in glass, no
> Haydée.** No third location — this page carries exactly two and no more. Only
> panel 1 is the Count's house; panels 2 and 3 are one continuous street. Standing
> prohibitions: no identity collision, no duplicated person, hand or object, no
> fused fingers, no illegible essential text, no crop sheet, no outer decorative
> frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — binds the black sleeve, the glove and the
>    hand.
> 2. `refs/approved/17-set-count-house.png` — binds the palette and materials of
>    the Count's hall in panel 1.
> 3. `refs/approved/18-set-morcerf-house.png` — binds the Morcerf house, the open
>    doors and **the general's staircase seen through them**.
>
> The engraved card is **not** on the object board and is designed here: a thick
> cream plate-sunk 1838 Paris card. All other character sheets are **prohibited
> generation inputs** for this page.

---

## PAGE 7 — *dramatic*

**Turn:** Albert opens the door and is immediately, disarmingly kind.
**Dominant:** Albert in the doorway, lit from behind by the whole burning house —
55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-07/candidates/page-07-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 7
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile wool broadcloth, silk, gilt plaster,
> polished walnut and candle amber, selective hard edges at faces and hands.
> **Not smooth prestige-oil realism.** No glossy concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **the Morcerf house** — burgundy, polished walnut, wax red, old gold,
> **dense candle amber**, overstuffed with purchased legitimacy: too many
> portraits, too much gilt. Against all of it, **one unbroken black vertical**:
> the Count. The page is the warmest so far in the volume and he does not warm up
> in it.
>
> **Predecessor: attach the promoted page 6.** Same night, same house, minutes
> later — he has come up the street and gone in. What carries in: the house's
> light level and colour, the doorway and the staircase beyond it, the Count's
> unrelieved black and his outdoor coat, and the fact that it is April and he
> walked. **Do not show** Haydée, Fernand, Danglars, Villefort, or any second
> young man. The woman in burgundy-black appears **only** in panel 4, distant,
> small and silent.
>
> **Character locks.** The 3 supplied canonical character references bind the
> named visible characters.
> **Albert de Morcerf, 22:** wide-set direct eyes and mouth; a jaw softened and
> un-weathered; **chestnut-brown hair — never raven black, never sandy** — worn
> short with a neat side part; **fair-olive skin several values lighter than the
> Count's**; slim, upright, unmarked by work; clean-shaven, no side whiskers;
> **open, mobile, quick-to-smile expression — he is the only face in the volume
> not guarding something**; **the volume's brightest costume values**: pale cream
> waistcoat, coloured neckcloth, a dark coat that is nevertheless lighter and less
> absolute than black.
> **The Count, 42:** twenty years older and reads it — tall, columnar, still;
> clean-shaven; **swept-back black hair with the first grey at the temples**;
> deep-set black-brown eyes; hollow temples; **cultivated pallor**; **a slight
> asymmetry at the left corner of the mouth**; **unrelieved black**, the darkest
> value on the page; **default expression closed and assessing, never open.**
> **Mercédès, Comtesse de Morcerf, 42 and visibly forty-two** (panel 4 only,
> distant and silent): lean mature cheeks, decisive dark eyes, **visible lower-lid
> and temple lines**, **restrained grey threading the dark hair**, hair sculpted
> into a formal 1838 coiffure, upright carriage, **burgundy-black vertical evening
> gown**. **Do not youth-wash her even at this distance** — a smoothed young face
> here is a blocking defect.
>
> **Collision prohibition — the highest risk in the volume.** Albert must never
> read as a young version of the Count. Separate them on all five axes in every
> panel where both appear: **hair colour** (chestnut brown vs black with grey at
> the temples), **skin value** (fair-olive and light vs cultivated pallor over a
> darker, colder value structure), **costume value** (pale waistcoat and lighter
> coat vs unrelieved black), **age** (twenty-two vs forty-two, and the twenty
> years must be visible in the eye sockets, jaw and neck), and **default
> expression** (open and mobile vs closed and assessing). Neither man may carry
> loose raven curls, an open white shirt, or a red-brown sash — that identity
> stack is reserved and does not appear in this volume. Mercédès must never read
> as a woman of twenty-seven with long unbound black hair and crimson-and-gold
> eastern embroidery.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule:** Albert holds the **left**, the Count the **right**, in
> every panel where both appear, and every balloon sits on its owner's side.
>
> ### Panel 1 — **DOMINANT, roughly 55% of the page**, the whole upper half
>
> **Albert in the doorway at the left, lit hard from behind by the whole burning
> house** — a rim of candle amber all down one side of him, the staircase and the
> crowd blazing behind. He is **coming down two steps with his hand already out**,
> mid-stride, warm, quick, delighted, talking before he has arrived. In the
> **near foreground at the right**, larger and darker, **the Count in
> silhouette** — the back and shoulder of an unbroken black vertical, his face
> turned away or only edge-lit, **not yet a portrait**. The contrast of a lit young
> man against a black shape is the image of the page.
>
> One warm-ivory balloon, upper left over the dark doorframe, tail to Albert's
> mouth, **wide and flat**, exactly:
>
> `You're the Count of Monte Cristo. Don't say anything yet — I want to have guessed.`
>
> ### Panel 2 — roughly 18%, lower left, a tall panel sharing the third tier with
> panel 3
>
> Both men now at the same distance and in the same light for the first time:
> **Albert left, chestnut and pale-waistcoated; the Count right, black and
> clean-shaven with grey at the temples.** Half-length. This is the panel where a
> reader decides they are two different men, so both faces must be fully visible
> and fully lit. Reserve the upper two-thirds of the panel as a balloon lane.
>
> Three warm-ivory balloons. The Count's short line is the **highest**, at the
> right; Albert's two follow, down the left. Exact strings, in this reading order:
>
> `You have guessed.`
>
> `Albert de Morcerf. The general's son.`
>
> `He's been asking after you for a month and pretending he hasn't, so please look impressed.`
>
> ### Panel 3 — roughly 15%, lower right, completing the tier
>
> **Albert taking the Count's cloak himself**, off-hand and unselfconscious,
> lifting it out of a waiting servant's arms because he wants to — the servant is
> a **faceless dark shape at the edge, silent, receiving no balloon.** Albert at
> the left with the black cloak across his arm; the Count's black sleeve and
> shoulder at the right.
>
> One warm-ivory balloon, upper left, tail to Albert's mouth, exactly:
>
> `You walked. In that coat, in April. You'll want the fire.`
>
> ### Panel 4 — roughly 12%, a wide horizontal band across the bottom
>
> **Silent panel — no balloons, no caption, no tail fragments.** Over Albert's
> shoulder from behind, deep into the crowded drawing room: colour, movement,
> **forty people**, gilt and candle amber, all of it in motion and none of it
> individuated — and, at the far side of the room, **one woman in burgundy-black
> who has stopped moving.** She is small, distant, upright, and the only still
> figure in the band; the crowd blurs around her. Her face is legible enough to
> read as **a woman in her early forties**, not enough to read as a portrait.
> **She is silent and receives no balloon.**
>
> **Lettering:** all **5** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes — including the em dash in
> Albert's first line. Balloon lettering **44–50 px** on the 1024 × 1536 canvas,
> **never below 40 px** for any character; balloons **240–390 px** wide, except
> Albert's two long strings, which run **wide and flat** across their reserved
> lanes — **panel 2 is at its text ceiling: if a string will not set at 44 px
> inside the reserved lane, widen the balloon and reduce the figures; never reduce
> the lettering.** Warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps.** **Albert owns four balloons; the Count owns one.** Panel 4 carries no
> text of any kind. No captions or prose fields on this page. No quotation marks,
> speaker labels, page numbers, titles or pseudo-text. Comfortably readable when
> the page is reduced to 600 × 900.
>
> **Continuity and meaning:** the door opens on a lit young man → he guesses the
> famous stranger and is delighted with himself → he names himself as the
> general's son → he takes the coat with his own hands → and behind all that
> warmth, across the room, someone has seen the black figure and stopped. The
> woman in panel 4 is the same woman who offers him apricots on page 11.
>
> **Page-specific prohibitions:** Fernand does not appear on this page — **no
> moustached decorated officer anywhere, including in the crowd.** No Haydée, no
> crimson-and-gold eastern dress in the crowd, no second young man in spectacles,
> no legible portrait faces on the walls, no daylight, no street. Standing
> prohibitions: no identity collision, no duplicated person, hand or object, no
> fused fingers, no illegible text, no crop sheet, no outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/04-albert.png` — Albert.
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/02-mercedes-1838.png` — the distant silent woman in panel 4.
> 4. `refs/approved/18-set-morcerf-house.png` — the entrance hall, the doorway and
>    the staircase beyond.
> 5. `pages/page-06.png` — promoted previous page; binds the house, its light
>    level and the hour.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 8 — *dramatic*

**Turn:** the Count makes Fernand say *Greece* out loud, and leaves the toast
undrunk.
**Dominant:** the general's staircase, two men climbing it side by side — 62%.
**Locations:** 1. **Panels:** 9.
**Output:** `qa/production/page-08/candidates/page-08-v14.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 8
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile gilt, polished walnut, marble, wool,
> ribbon silk, enamel, cut glass and candle amber, selective hard edges at the two
> faces, the hand on the banister and the two glasses. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **the Morcerf house** — burgundy, polished walnut, old gold, dense
> candle amber, and **wax red doing the accent work: the ribbons, seals and
> enamels of the decorations across the older man's chest.** The Count remains the
> only unbroken black vertical in the frame.
>
> **Predecessor: attach the promoted page 7.** Same night, same house, minutes
> later; **his cloak is gone — Albert took it on page 7** — and he is in
> unrelieved black evening dress with no outdoor coat. What carries in: the
> house's light level and colour, the staircase seen through the doors on page 6
> and behind Albert on page 7, and the crowd noise implied off-panel. **Do not
> show** Albert, Haydée, Mercédès, Danglars or Villefort anywhere on this page.
> Two named men only; any other figure is a small faceless dark shape at the
> margin.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw; heavy black brows
> set low and close; deep-set close dark eyes; **weathered ruddy-olive Catalan
> skin, coarser in texture and warmer in value than any other face on this page**;
> **heavy iron-and-black military moustache**; black hair **receding at the
> temples** and iron-grey at the sides; thick neck; heavy upright soldier's build;
> general's evening dress with **a chest of decorations — orders, ribbons, wax-red
> seals and old gold, polished and displayed.**
> **The Count, 42:** tall, columnar, **taller than Fernand and much slimmer**;
> **clean-shaven**; swept-back black wave with the first grey at the temples;
> deep-set black-brown eyes; long clean nose; high cheekbones; hollow temples;
> **cultivated pallor, several values cooler and paler than Fernand's skin**; **a
> slight asymmetry at the left corner of the mouth**; **unrelieved black, no
> decoration, no ribbon, no order, nothing on the chest at all.**
>
> **Collision prohibition.** The Count must never carry Fernand's heavy moustache,
> receding hairline, thickened build or weathered skin; Fernand must never appear
> clean-shaven, pallid, slim or columnar, and must never lose the moustache or the
> receding temples in any panel, including the tight panels and the profile
> panels. **The decorations belong to Fernand alone and never appear on the black
> figure.**
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Nine-panel asymmetric-mosaic rule, binding on every panel: do not make
> horizontal strips and do not equalize panel heights.** Panel 1 is one huge
> upper-left rectangle, exactly 75% of page width and 82% of page height. Panels
> 2, 3, 4, 5 and 6 stack in the narrow 25%-wide right column beside it. Panels
> 7, 8 and 9 occupy the remaining 18%-tall bottom row. **Fernand holds the left and
> the Count holds the right.**
> Every right-column panel has exactly one visible speaker and one balloon:
> Fernand, Count, Fernand, Count, Fernand. The question and answer are isolated:
> Panel 5 shows only the Count with only his question; Panel 6 shows only Fernand
> with only his answer. Never put `In Spain?` and `In Greece.` in the same panel.
> Panel 7 is a large silent glass
> action. The Count's two final replies occupy separate side-by-side
> one-speaker panels, one balloon each.
>
> ### Panel 1 — **DOMINANT, the huge upper-left 75% wide × 82% tall rectangle, about 62% of the page**
>
> **Hard geometry:** this rectangle begins at the top-left page corner, its right
> separator stands at approximately source x=768 of 1024, and its bottom
> separator stands at approximately source y=1260 of 1536. It is visibly more
> than seven times the area of any other panel. Do not turn it into a full-width
> horizontal strip; do not compress it below 45% of the page.
>
> **Two men climbing the general's staircase side by side**, seen from below and
> close behind so the staircase towers — the same wide gilt staircase as the
> supplied setting plate and as page 6. **Crop every wall plane completely out
> of the image.** The frame contains only the burgundy runner and rising stair
> treads, both wooden balustrades, ceiling shadow, candle glow, and the two live
> men; no framed picture, wall portrait, painted person, sculpted person, display
> case, wall-mounted order, ribbon or decoration is visible anywhere. The two
> men are large in frame and the runner/steps fill the background. **Fernand at
> the left, one step ahead and
> enjoying being ahead**, half-turned to talk, chest of decorations catching the
> candlelight, hand out on the rail. **The Count at the right, one step lower,
> black, taller even a step down, unhurried, entirely composed.** No party guests
> and no other human image or figure appear in this panel.
>
> Two warm-ivory balloons: Fernand's upper left, tail to his mouth; the Count's
> lower right, tail to his mouth. Exact strings, in this reading order:
>
> `A month in Paris, and everyone has had you at their table but me.`
>
> `I wanted to see the house first. I walked past it four times.`
>
> ### Panel 2 — top of the narrow right column, about 25% wide × 12% tall
>
> **Fernand alone**, half-turned back, flattered and not sure why. Moustache and
> receding temple unmistakable. The Count is absent. Exactly one warm-ivory
> balloon with one short tail visibly terminating at Fernand's mouth, exactly:
>
> `Four times. Why?`
>
> ### Panel 3 — below it in the right column, about 25% wide × 30% tall
>
> **The Count alone**, clean-shaven face and mouth visible above his long clean
> poised hand on the gilt banister. Fernand is absent. Exactly one wide vertical
> warm-ivory balloon with one tail visibly terminating at the Count's mouth,
> exactly:
>
> `I like to know what a man built before I take his hand. You have a general's staircase.`
>
> ### Panel 4 — below it in the right column, about 25% wide × 10% tall
>
> **Fernand alone**, upright, decorations visible on his live chest. The Count is
> absent. Exactly one warm-ivory balloon with one tail visibly terminating at
> Fernand's mouth, exactly:
>
> `I earned it.`
>
> ### Panel 5 — below it in the right column, about 25% wide × 15% tall
>
> **The Count alone**, head and shoulders, straight on and evenly
> lit. Nothing on his face — not amusement, menace or sympathy. Fernand is not
> visible and owns no balloon in this panel.
>
> Exactly one small warm-ivory balloon, tail visibly terminating at
> the Count's mouth, exactly:
>
> `In Spain?`
>
> ### Panel 6 — bottom of the narrow right column, about 25% wide × 15% tall
>
> **Fernand alone**, head and shoulders, moustache and receding
> temple unmistakable, the answer leaving him before he understands the trap.
> The Count is not visible and owns no balloon in this panel.
>
> Exactly one small warm-ivory balloon, tail visibly terminating at
> Fernand's mouth, exactly:
>
> `In Greece.`
>
> ### Panel 7 — left 62% of the bottom row, about 62% wide × 18% tall
>
> **The volume's primary motif begins here and must be physically
> unmistakable.** This bottom-left rectangle begins near y=1260. At the left,
> Fernand's thick ringed fingertips enter from the top edge and suspend a
> deliberately miniature full glass: the complete glass from rim to foot occupies
> no more than 15% of the panel height and ends within the upper 25% of the panel.
> The entire lower 75% beneath its foot is uninterrupted empty black space,
> visibly at least three complete glass-heights. The raised glass is a small prop,
> never a large foreground hero object.
> There is no marble,
> table edge or supporting surface anywhere under Fernand's glass. At the right,
> a small marble corner occupies only the lower-right quarter and the Count's long pale hand is **pressing the foot
> of a separate identical full glass onto that marble**. One glass is aloft over
> empty space; the other visibly touches stone. Neither is near a mouth. **This
> panel is silent: no balloon, caption, tail fragment or text of any kind.**
>
> ### Panel 8 — middle 14% of the bottom row, about 14% wide × 18% tall
>
> **The Count alone**, face and mouth clearly visible, the flat
> answer immediately after his full glass touches stone. Fernand is not visible
> and owns no balloon here.
>
> Exactly one warm-ivory balloon with one short tail visibly
> terminating at the Count's mouth, exactly:
>
> `Of course. Greece.`
>
> ### Panel 9 — right 24% of the bottom row, about 24% wide × 18% tall
>
> **The Count alone**, face and mouth clearly visible, already
> turning the knife into courtesy. Fernand is not visible and owns no balloon
> here.
>
> Exactly one warm-ivory balloon with one short tail visibly
> terminating at the Count's mouth, exactly:
>
> `Forgive me. I am a stranger here and I get your wars wrong.`
>
> **Lettering:** all **9** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px** for any character; the
> short replies (`Four times. Why?`, `I earned it.`, `In Spain?`, `In Greece.`)
> may take the **48–54 px** short-reply size where space allows; balloons **240–390
> px** wide, except the two long strings in panels 3 and 9, which run **wide and
> flat** across their bands — **if a string will not set at 44 px inside its band,
> widen the balloon; never reduce the lettering, and never let a balloon cross a
> panel border.** Warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps.** **The Count owns five balloons; Fernand owns four.** No captions and
> no prose fields. No quotation marks, speaker labels, page numbers, titles or
> pseudo-text; **no legible engraving on the decorations and no legible lettering
> anywhere in the room.** Comfortably readable when the page is reduced to 600 ×
> 900.
>
> **Continuity and meaning:** the host climbs his own staircase one step ahead →
> the guest says he walked past the house four times → the guest admires what the
> host built and the host claims to have earned it → one flat question makes the
> host say **Greece** out loud → the guest apologises charmingly and sets the full
> glass down. Nobody in the house notices the glass. **The glass is full when it
> touches the marble and it stays full** — this is the first of the volume's three
> refusals and it is never explained in words.
>
> **Page-specific prohibitions:** the Count must not drink, sip, raise the glass
> to his mouth, or hold an emptied glass; no toast clinking the two glasses
> together; no wine spilled; no Greece, no flashback, no memory inset, no map, no
> military portrait of any kind, legible or not; no painted military figure; no
> wall display of orders, ribbons or decorations; no Albert; no woman in
> burgundy-black.
> Standing prohibitions: no identity collision, no duplicated person, hand or
> object — **the two glasses in panel 7 are two different glasses in two different
> vertical planes: Fernand's aloft over empty black space, the Count's touching
> marble** — no fused fingers, no illegible text, no crop sheet, no outer
> decorative frame.
>
> ## Reference images
> 1. `refs/approved/03-fernand-1838.png` — Fernand, the moustache, the receding
>    temples, the decorations.
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/18-set-morcerf-house.png` — **the general's staircase**, which
>    must be the same staircase as page 6 and as later pages.
> 4. `refs/approved/21-objects.png` — the wine glass, full, and the decorations.
> 5. `pages/page-07.png` — promoted previous page; binds the house, the hour and
>    the Count's dress without the cloak.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 9 — *dramatic*

**Turn:** Danglars and Villefort each take his hand, and Villefort feels
something he cannot name.
**Dominant:** the held handshake, Villefort's face very close — 45%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-09/candidates/page-09-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 9
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile broadcloth, starched linen, gold
> watch-chain, ring metal, gilt and candle amber, selective hard edges at the
> faces and — above everything else on this page — **at the hands.** **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> engraved cross-hatching, no children's-book softness.
>
> Palette: **the Morcerf drawing room** — burgundy, polished walnut, wax red, old
> gold, dense candle amber, crowded and overwarm; the Count remains the only
> unbroken black vertical. Villefort's black is **high-necked, rigid and colder**
> than the room but is not the absolute black of the Count's evening dress.
>
> **Predecessor: attach the promoted page 8.** Same night, same house, the same
> hour, one room on from the staircase. What carries in: the light level, the
> palette, the Count's unrelieved black without cloak, and the crowd as warm
> blurred light. **Do not show** Fernand, Albert, Mercédès or Haydée on this page.
> Three named men only; every other figure is a small faceless dark shape at the
> margin, and none of them receives a balloon.
>
> **Character locks.** The 3 supplied canonical character references bind the
> named visible characters.
> **Baron Danglars, 55:** heavy fleshy face; small shrewd close-set eyes; thin
> mouth; high colour in the cheeks; thinning sandy-grey hair combed across;
> **full side whiskers and NO moustache**; **short and thickening**; expensive
> clothes fitting badly; rings on the fingers; heavy watch chain.
> **Gérard de Villefort, 53:** **long narrow inverted-triangle face**; very high
> forehead; close-set grey-hazel eyes; thin brows; convex aquiline nose; pointed
> chin; **cool pale skin**; chestnut hair gone iron-grey in a hard side part; deep
> vertical lines; **rigid high-necked black silhouette**; clean-shaven.
> **The Count, 42:** tall, columnar, still; clean-shaven; swept-back black wave
> with the first grey at the temples; deep-set black-brown eyes; strong straight
> brow; long clean nose; high cheekbones; **a slight asymmetry at the left corner
> of the mouth**; cultivated pallor; **unrelieved black 1838 evening dress.**
>
> **Collision prohibition.** Danglars must never be given Villefort's narrow pale
> rigidity, and Villefort must never be given Danglars' fleshy face, side whiskers
> or thickening build — **side whiskers with no moustache belong to Danglars alone
> and Villefort is clean-shaven with none.** Neither man may take the Count's
> columnar height, swept-back wave or left-mouth asymmetry; the Count may never
> take Villefort's inverted-triangle face or Danglars' bulk, and never a
> moustache or side whiskers of any kind.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on every panel:** **the Count holds the right of
> every panel; whoever he is speaking to holds the left**, and every balloon sits
> on its owner's side. This is the same convention as pages 8 and 10–12.
>
> ### Panel 1 — roughly 20%, upper left, sharing the top tier with panel 2
>
> **Danglars at the left, hand already out, mouth already going** — short,
> thickening, ringed, side-whiskered, no moustache, a costly waistcoat straining.
> The Count at the right, taller, black, receiving him with courtesy and no
> warmth. Half-length.
>
> Two warm-ivory balloons: Danglars' upper left, the Count's lower right, each
> tail to its owner's mouth. Exact strings, in this reading order:
>
> `Danglars. Baron. You'll have heard the name at your bank.`
>
> `I have. You hold six millions of mine.`
>
> ### Panel 2 — roughly 12%, upper right, completing the top tier
>
> Danglars close, **delighted, both hands now** — one of the Count's hands taken
> in two of his, rings and thick wrists prominent. The Count is present as a black
> sleeve and a fraction of jaw at the right; **he is silent in this panel and
> receives no balloon.**
>
> One warm-ivory balloon, upper left, tail to Danglars' mouth, exactly:
>
> `Then we are old friends and neither of us knew it.`
>
> ### Panel 3 — roughly 15%, a wide band across the middle
>
> **Villefort at the left — narrow, pale, rigid in high-necked black — offering
> his hand as though signing something**, the arm straight, the wrist formal, no
> pleasure in it. The Count at the right, taking it. A different temperature from
> the two panels above and the painting should show it: less amber on these two,
> more cold shadow.
>
> Two warm-ivory balloons: Villefort's short line upper left; the Count's runs
> **wide and flat** at the right. Exact strings, in this reading order:
>
> `Villefort. Attorney-General.`
>
> `The King's Attorney. Then you would be the man who decides what is forgotten.`
>
> ### Panel 4 — **DOMINANT, roughly 45% of the page**, the whole lower-middle
>
> **The handshake, held.** Two hands joined in the near foreground, hard-edged and
> large — the pale long hand and the pale narrow one — and above them **Villefort's
> face very close to the picture plane at the left**, filling much of the panel:
> **a cold going through him that he cannot place and will not admit to.** Not
> fear, not recognition — a physical chill arriving in a man who does not believe
> in them. The Count's face at the right, calm, offering nothing, watching him
> have it. This panel is the page and must carry the page's turn.
>
> Two warm-ivory balloons: Villefort's at the upper left; the Count's below at the
> right, **wide and flat.** Exact strings, in this reading order:
>
> `I decide what is prosecuted.`
>
> `Yes. Forgive me. My French is excellent and my meaning is sometimes not.`
>
> ### Panel 5 — roughly 8%, a narrow band across the bottom
>
> **The hands still joined** — the same two hands, closer, cropped to hands and
> cuffs alone. **Villefort has not let go**, and the reader must be able to see
> that it is he who is holding on. No faces in this band.
>
> Two small warm-ivory balloons, Villefort's at the left, the Count's at the
> right, tails running off the top edge of the band toward the two unseen speakers
> above — neither tail may point at a hand or a cuff. Exact strings, in this
> reading order:
>
> `Have we met?`
>
> `No.`
>
> **Lettering:** all **9** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px** for any character; the
> short replies (`Villefort. Attorney-General.`, `Have we met?`, `No.`) may take
> the **48–54 px** short-reply size; balloons **240–390 px** wide, except the
> Count's two long strings in panels 3 and 4, which run **wide and flat** across
> their reserved lanes — **if a string will not set at 44 px, widen the balloon;
> never reduce the lettering.** Warm ivory fill with a restrained charcoal-brown
> painted outline; upright mixed-case. **No italics, no condensed display faces,
> no all-caps.** **The Count owns four balloons; Danglars owns two; Villefort owns
> three.** No captions and no prose fields. No quotation marks, speaker labels,
> page numbers, titles or pseudo-text. Comfortably readable when the page is
> reduced to 600 × 900.
>
> **Continuity and meaning:** the banker introduces himself by his own bank → the
> Count already owns six millions of him → the banker calls it friendship → the
> magistrate offers his hand like a signature → the Count says something with two
> meanings → the magistrate feels the cold and holds on → and asks. **Three
> handshakes in one page and not one of them knows what he is holding.** Hands are
> the moral instrument of this page: they are the hardest-edged, best-drawn thing
> in every panel.
>
> **Page-specific prohibitions:** no recognition on the Count's face — **he does
> not smile, does not narrow his eyes, and gives nothing away in panels 3 to 5**;
> no flashback, no memory inset, no Marseille, no prison, no document; **no
> moustache on any of the three named men**; no Fernand and no decorations in
> frame. Standing prohibitions: no identity collision, no duplicated person, hand
> or object — **the joined hands in panels 4 and 5 must read as exactly two hands,
> one each** — no fused fingers, no illegible text, no crop sheet, no outer
> decorative frame.
>
> ## Reference images
> 1. `refs/approved/06-danglars-1838.png` — Danglars.
> 2. `refs/approved/08-villefort-1838.png` — Villefort.
> 3. `refs/approved/01-count-1838.png` — the Count.
> 4. `refs/approved/18-set-morcerf-house.png` — the Morcerf house interior, its
>    palette and its gilt.
> 5. `pages/page-08.png` — promoted previous page; binds the house, the hour and
>    the Count's dress.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 10 — *dramatic*

**Turn:** Albert is proud of his father, out loud, to the man who came to destroy
him.
**Dominant:** Albert talking, the Count genuinely listening — 49%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-10/candidates/page-10-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 10
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile window glass, painted shutter, silk
> waistcoat, porcelain and candle amber, selective hard edges at the two faces and
> at the forgotten plate. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **the Morcerf house** — burgundy, polished walnut, old gold, dense
> candle amber — but this is a **window bay off the main room**, so the party's
> light and noise are behind them and there is a band of **cold night blue** in
> the window glass at their backs. Albert carries the page's brightest values; the
> Count is the black vertical against the cold glass.
>
> **Predecessor: attach the promoted page 9.** Same night, same house, a little
> later, one bay off the crowded drawing room. What carries in: the light level,
> the palette, the crowd as warm blurred light behind them, and the Count's
> unrelieved black. **Do not show** Fernand, Danglars, Villefort, Haydée or
> Mercédès on this page. Two named people only; the party behind them is warm
> blur with **no individuated faces.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **Albert de Morcerf, 22:** wide-set direct eyes and mouth; a jaw softened and
> un-weathered; **chestnut-brown hair — never raven black, never sandy** — short
> with a neat side part; **fair-olive skin several values lighter than the
> Count's**; slim, upright, unmarked by work; clean-shaven, no side whiskers;
> **open, mobile, quick-to-smile expression**; **pale cream waistcoat and coloured
> neckcloth — the brightest costume values on the page.**
> **The Count, 42:** tall, columnar, still; **clean-shaven**; **swept-back black
> hair with the first grey at the temples**; deep-set black-brown eyes; hollow
> temples; **cultivated pallor**; **a slight asymmetry at the left corner of the
> mouth**; **unrelieved black, the darkest value on the page**; twenty years older
> than the young man and it reads in the eye sockets, the jaw and the neck.
>
> **Collision prohibition — the highest risk in the volume, and this page is the
> longest the two of them are alone together.** Albert must never read as a young
> version of the Count. Separate them in **every panel** on all five axes: **hair
> colour** (chestnut vs black with grey at the temples), **skin value** (light
> fair-olive vs cold cultivated pallor), **costume value** (pale waistcoat and
> lighter coat vs unrelieved black), **age** (twenty-two vs forty-two), **default
> expression** (open and mobile vs closed and assessing). Neither may carry loose
> raven curls, an open white shirt or a red-brown sash — that identity stack is
> reserved and unused in this volume. Albert never wears spectacles.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on every panel:** **Albert holds the left, the
> Count holds the right**, and every balloon sits on its owner's side.
>
> ### Panel 1 — **DOMINANT, roughly 49% of the page**, the whole upper portion
>
> The window bay. **Albert at the left, animated, half-sitting on the window
> ledge with a plate he has forgotten he is holding**, tipped slightly, food
> untouched — talking with his hands, entirely at ease. **The Count at the right,
> standing, listening — genuinely listening, and that is the problem:** he is
> attentive, unguarded for a moment, leaning very slightly in. The cold night
> glass behind them, the party's warm blur behind that.
>
> One warm-ivory balloon, upper left over the dark window frame, **wide and
> flat**, tail to Albert's mouth, exactly:
>
> `He never talks about Greece. I've had to get it out of other people, in pieces, for twenty years.`
>
> ### Panel 2 — roughly 18%, a wide band below
>
> The two of them closer, half-length, same staging: Albert left, the Count right.
> Reserve the upper two-thirds of this band as a balloon lane and keep the figures
> low in the frame.
>
> Two warm-ivory balloons. The Count's is the **highest element in the band**, at
> the right; Albert's follows **below and to the left**. Exact strings, in this
> reading order:
>
> `What does he say when you ask him?`
>
> `That it was a long time ago and nobody came out of it clean.`
>
> ### Panel 3 — roughly 15%, a wide band below that
>
> **The Count, a beat late.** Close, at the right of the band: the smallest
> possible hesitation before he answers — the composure is intact and the timing
> is not. Albert at the left, waiting, still cheerful.
>
> Two warm-ivory balloons: the Count's at the right, upper; Albert's at the left,
> below. Exact strings, in this reading order:
>
> `That is an honest answer.`
>
> `He's an honest man. It's the only unfashionable thing about him.`
>
> ### Panel 4 — roughly 18%, a wide band across the bottom
>
> **Albert grinning, oblivious**, at the left, offering the invitation with his
> whole face. **The Count's face turned very slightly away at the right, and for
> this one panel there is nothing in it** — not appetite, not pleasure, not guilt;
> the expression has simply been removed, exactly as in the tight panel on page 8.
> The reader must be able to see that Albert cannot see it.
>
> Two warm-ivory balloons, both Albert's, at the left, the second below the first,
> each tail to his mouth. **The Count has no balloon in this panel and no tail
> fragment.** Exact strings, in this reading order:
>
> `Come back. Any evening you like, without the forty people.`
>
> `He's dull about Spain and wonderful about horses, and my mother will like you.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px** for any character;
> balloons **240–390 px** wide, except the long strings in panels 1, 2 and 4,
> which run **wide and flat** across their reserved lanes — **this page carries
> more words than any other page in this movement: reserve every balloon lane
> before placing the two figures, and if a string will not set at 44 px inside its
> lane, widen the balloon and reduce the figures; never reduce the lettering.**
> Warm ivory fill with a restrained charcoal-brown painted outline; upright
> mixed-case. **No italics, no condensed display faces, no all-caps.** **Albert
> owns five balloons; the Count owns two.** No captions and no prose fields. No
> quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** the boy volunteers Greece without being asked → the
> father's evasion is quoted honestly → the Count calls it an honest answer and is
> a beat late doing it → the boy says his father is an honest man → and invites
> the man who came to destroy him back to the house, and mentions his mother. The
> emptied face in panel 4 is the first crack in the appetite and it is never
> explained.
>
> **Page-specific prohibitions:** no Greece, no flashback, no memory inset, no
> military portrait, no map; **the Count does not smile in any panel on this
> page**; Albert does not stop smiling until the page ends; no food eaten by
> either man and **no wine glass in the Count's hand anywhere on this page**; no
> third named face. Standing prohibitions: no identity collision, no duplicated
> person, hand or object, no fused fingers, no illegible text, no crop sheet, no
> outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/04-albert.png` — Albert.
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/18-set-morcerf-house.png` — the Morcerf house, its palette and
>    its windows.
> 4. `pages/page-09.png` — promoted previous page; binds the house, the hour and
>    the Count's dress.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 11 — *dramatic*

**Turn:** Mercédès offers fruit from her own garden, he refuses, and she does not
lower the plate.
**Dominant:** the plate held level between them — 50%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-11/candidates/page-11-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 11
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile porcelain, damask linen, apricot skin,
> silk, polished walnut and candle amber, selective hard edges at the two faces,
> at her hands and at the plate. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **the Morcerf house** — burgundy, polished walnut, wax red, old gold,
> dense candle amber, the long table dressed and overloaded. Against it the
> Count's unrelieved black. **The apricots are the only fresh living colour in the
> volume so far** — warm ochre-gold with a red blush — and the painting should
> make them the most edible thing on the page.
>
> **Predecessor: attach the promoted page 10.** Same night, same house, a little
> later, at the long table in the drawing room. What carries in: the light level,
> the palette, the crowd as warm blurred light, the Count's unrelieved black.
> **Do not show** Fernand, Albert, Danglars, Villefort or Haydée on this page. Two
> named people only; other guests are small faceless dark shapes at the margin and
> none receives a balloon.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **Mercédès, Comtesse de Morcerf, 42 and visibly forty-two:** decisive dark eyes;
> straight nose; **lean mature cheeks**; **visible lower-lid lines and temple
> lines**; **restrained grey threading the dark hair**, which is sculpted into a
> formal 1838 Paris coiffure; still, upright carriage; **burgundy-black vertical
> evening gown.** **Do not youth-wash her. A beautiful but smoothed face is a
> blocking defect on this page** — she is forty-two, she has been forty-two for
> the whole volume, and the lines around the eye are load-bearing because this is
> the page on which she becomes certain.
> **The Count, 42:** tall, columnar, still; clean-shaven; swept-back black wave
> with the first grey at the temples; deep-set black-brown eyes; long clean nose;
> high cheekbones; hollow temples; **a slight asymmetry at the left corner of the
> mouth**; cultivated pallor; **unrelieved black 1838 evening dress.**
>
> **Collision prohibition.** Mercédès must never read as a woman of twenty-seven
> with **long unbound black hair and crimson-and-gold eastern embroidery** — that
> is a different character in this book and she is not in this house. Her hair is
> sculpted, her silhouette is a fitted French 1838 gown, and her age is visible.
> The Count must never carry a military moustache, a receding hairline, a
> thickened build, or a young man's chestnut hair and pale waistcoat.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on every panel:** **Mercédès holds the left, the
> Count holds the right**, and every balloon sits on its owner's side.
>
> ### Panel 1 — roughly 17%, a wide band across the top
>
> **Mercédès at the left with a plate of apricots, offering** — the plate already
> up, held in both hands or in one steady hand, the fruit lit. The Count at the
> right, half-length, courteous. Her face is the subject of the band: early
> forties, lean, still, the temple and lower-lid lines legible at this scale.
>
> Two warm-ivory balloons: hers upper left, his lower right, each tail to its
> owner's mouth. Exact strings, in this reading order:
>
> `You have eaten nothing all evening.`
>
> `I dined late.`
>
> ### Panel 2 — roughly 18%, a wide band below
>
> Mercédès closer, at the left, **not retreating** — she has answered a polite
> deflection by giving him more information than a hostess needs to give. The
> Count at the right, listening. Reserve the upper two-thirds of this band as a
> balloon lane and keep the figures low in the frame.
>
> Two warm-ivory balloons, **both hers**, at the left, the second below the first,
> each tail to her mouth. **The Count is silent in this panel and receives no
> balloon.** Exact strings, in this reading order:
>
> `These are from my own garden.`
>
> `There is a wall at the back of the house that holds the sun. I grew them myself.`
>
> ### Panel 3 — **DOMINANT, roughly 50% of the page**, the whole middle of the page
>
> **The plate between them, held out and not withdrawn.** The plate of apricots is
> in the near-middle of the frame, hard-edged and fully lit, level. Mercédès at
> the left, **her eyes on his face and not on the fruit** — the whole page turns
> on where she is looking. The Count at the right, refusing with perfect courtesy,
> **his hands not moving toward the plate at all.** Both faces large and fully
> visible; this is the second-longest look the two of them exchange in the volume.
>
> One warm-ivory balloon, at the right, tail to the Count's mouth, exactly:
>
> `You are very kind. I never eat fruit.`
>
> ### Panel 4 — roughly 8%, a narrow band below
>
> **The plate, still level.** Close on the plate and her hand alone — **her hand
> has not moved a millimetre**, no tremble, no lowering, the fruit still lit.
> Faces may be cropped out entirely, or her jaw and mouth kept at the left edge.
>
> One small warm-ivory balloon at the left, tail running toward her unseen or
> partly-seen mouth at the left edge — **the tail must not point at the plate, the
> fruit or the hand.** Exactly:
>
> `Never.`
>
> ### Panel 5 — roughly 7%, a narrow band across the bottom
>
> **Tight on the Count.** Head only, at the right. **He has just made a mistake
> and he knows it** — the smallest possible correction passing across a face that
> is otherwise perfectly controlled. Not panic, not guilt: a man who has heard his
> own answer.
>
> One small warm-ivory balloon at the right, tail to his mouth, exactly:
>
> `A habit from the east.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes — including the accents in
> **Mercédès** where any word carries them in the rendered strings (none of this
> page's strings contains an accented character; do not add one). Balloon
> lettering **44–50 px** on the 1024 × 1536 canvas, **never below 40 px** for any
> character; `Never.` and `I dined late.` may take the **48–54 px** short-reply
> size; balloons **240–390 px** wide, except her long string in panel 2, which runs
> **wide and flat** across its reserved lane — **if a string will not set at 44 px
> inside its lane, widen the balloon and reduce the figures; never reduce the
> lettering.** Warm ivory fill with a restrained charcoal-brown painted outline;
> upright mixed-case. **No italics, no condensed display faces, no all-caps.**
> **Mercédès owns four balloons; the Count owns three.** No captions and no prose
> fields. No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** she notices he has eaten nothing → he deflects → she
> tells him she grew the fruit herself, which is not a hostess's remark → he
> refuses **fruit as a category**, which is a strange thing to say → **she does not
> lower the plate**, and that unmoved hand is the page's real event → he invents a
> reason. **This is the second refusal of the volume's primary motif and the one
> that is noticed.** On page 8 nobody saw the full glass; here she sees, and the
> reader must understand she has become certain of something without being told
> what.
>
> **Page-specific prohibitions:** the Count does not touch the plate, does not
> take an apricot, does not hold one, does not set one down; **the plate is never
> lowered, withdrawn, tilted away or handed to a servant on this page**; no eating
> by anyone in frame; no flashback, no memory inset, no Marseille, no garden, no
> daylight, no sky, no Catalan village; no wine glass in his hand in any panel.
> Standing prohibitions: no identity collision, no duplicated person, hand or
> object, no fused fingers, no illegible text, no crop sheet, no outer decorative
> frame.
>
> ## Reference images
> 1. `refs/approved/02-mercedes-1838.png` — Mercédès, **forty-two, unsmoothed.**
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/18-set-morcerf-house.png` — the Morcerf drawing room and the
>    long table.
> 4. `refs/approved/21-objects.png` — binds the glassware and table objects of
>    this house; **the plate of apricots is not on the object board and is designed
>    here** — a shallow white-and-gilt porcelain plate of ripe apricots.
> 5. `pages/page-10.png` — promoted previous page; binds the house, the hour and
>    the Count's dress.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 12 — *dramatic*

**Turn:** she knows, and neither of them says so.
**Dominant:** two faces in profile opposition with the full glass between them —
60%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-12/candidates/page-12-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 12
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile cut glass, dark wine, damask, walnut,
> chair-back gilding and candle amber, selective hard edges at the two faces, at
> her knuckles and **at the full glass.** **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **the Morcerf house**, but quieter — burgundy, polished walnut, old
> gold, candle amber pulled back to a single close warmth on the two of them,
> because **the party has moved away from this corner** and the noise is now at
> the far side of the room. The Count is the unbroken black vertical; the wine in
> the glass is the one deep red note and it is never touched.
>
> **Predecessor: attach the promoted page 11.** Same night, same house, the same
> corner, continuous with page 11. What carries in: both costumes unchanged, the
> light level, the crowd now further off, and — most importantly — **the fact that
> he has just refused something of hers.** The plate of apricots is **gone from
> this page**: it has been set down off-frame and does not appear. **Do not show**
> Fernand, Albert, Danglars, Villefort or Haydée on this page. Two named people
> only; other guests are distant faceless shapes and none receives a balloon.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **Mercédès, Comtesse de Morcerf, 42 and visibly forty-two:** decisive dark eyes;
> straight nose; lean mature cheeks; **visible lower-lid lines and temple lines**;
> **restrained grey threading the dark hair**, sculpted into a formal 1838 Paris
> coiffure; still, upright carriage; **burgundy-black vertical evening gown.**
> **Do not youth-wash her — a smoothed face is a blocking defect on this page**,
> and the profile panel is where it usually happens: keep the lower-lid line, the
> temple line and the slight slackening under the jaw visible **in profile.**
> **The Count, 42:** tall, columnar, still; clean-shaven; swept-back black wave
> with the first grey at the temples; deep-set black-brown eyes; strong straight
> brow; long clean nose; high cheekbones; hollow temples; **a slight asymmetry at
> the left corner of the mouth**; cultivated pallor; **unrelieved black.**
>
> **Collision prohibition.** Mercédès must never read as a woman of twenty-seven
> with long unbound black hair and crimson-and-gold eastern embroidery. The Count
> must never carry a military moustache, a receding hairline, a thickened build,
> or chestnut hair and a pale waistcoat.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on every panel:** **Mercédès holds the left, the
> Count holds the right**, and every balloon sits on its owner's side. **Reserve
> every balloon lane on this page before placing the faces** — panels 2 and 3
> carry more speech than their area comfortably allows.
>
> ### Panel 1 — roughly 15%, upper left, sharing the top tier with panel 2
>
> The two of them a little apart from the noise, half-length: Mercédès left, the
> Count right, the crowd small and warm behind them. **On the table between them,
> in full view, an untouched glass of wine** — full to the same level as the glass
> he set down on page 8, standing where he left it, catching one hard highlight.
>
> Two warm-ivory balloons: hers upper left, his lower right. Exact strings, in
> this reading order:
>
> `My son likes you.`
>
> `He is easy to like back.`
>
> ### Panel 2 — roughly 12%, upper right, completing the top tier
>
> A closer beat: her face at the left, his at the right, the same corner. **She
> asks the question after a pause and the pause is visible** — her second balloon
> is a separate balloon from her first, and the gap between them is the beat. Keep
> the figures small and low; the upper two-thirds of this panel is a **reserved
> balloon lane.**
>
> Three warm-ivory balloons, set so the reading path runs cleanly down: hers at
> the upper left, hers again immediately below it on the same side, his at the
> lower right. All three sit within the panel and none crosses the panel border.
> Exact strings, in this reading order:
>
> `He has always been.`
>
> `Where were you born, Count?`
>
> `At sea. My father moved a great deal.`
>
> **The parenthetical beat between her two lines is staging, not text: no dash, no
> ellipsis, no bracket, no word renders between them.**
>
> ### Panel 3 — **DOMINANT, roughly 60% of the page**, the whole lower-middle
>
> **Two faces, close, in profile opposition** — Mercédès facing right, the Count
> facing left, both in near-strict profile, the same distance from the viewer, the
> same light. **The full glass sharp in the near foreground between them**, larger
> than either face's features, hard-edged, still full. Neither of them is going to
> say it: her profile is doing arithmetic, his is refusing to help her with it.
> The rest of the room falls away into dark burgundy.
>
> Four warm-ivory balloons. Hers stack down the left side; his sits at the right
> **below** the second of hers; her last drops **below his** on the left. The
> reading path runs left-down, left-down, right, left-down and never crosses
> backward. Exact strings, in this reading order:
>
> `I was born in a fishing village and never went further than Marseille until I was nineteen.`
>
> `Forgive me. For a moment you reminded me of somebody.`
>
> `I hope he was a friend of yours.`
>
> `He was.`
>
> ### Panel 4 — roughly 13%, a wide band across the bottom
>
> **Silent panel — no balloons, no caption, no tail fragments.** **Her hand on the
> back of a chair, knuckles white**, hard-edged and close at the left of the band —
> the only violence on the page is in that hand. Behind her, out of focus and
> walking away into the crowd, **the black vertical of him**, unmistakable by
> silhouette and unreadable as a face. **On the table, still in frame and still in
> focus, the glass — and it is still full.** All three elements must be legible in
> one look: the white knuckles, the departing black vertical, the full glass.
>
> **Lettering:** all **9** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px** for any character; `He
> was.` and `My son likes you.` may take the **48–54 px** short-reply size;
> balloons **240–390 px** wide, except her long strings in panels 2 and 3, which
> run **wide and flat** across their reserved lanes — **panel 2 is the tightest
> text lane on the page: if its three strings will not set at 44 px inside it,
> widen the balloons and shrink the figures to head-and-shoulder scale; never
> reduce the lettering and never let a balloon cross into panel 1.** Warm ivory
> fill with a restrained charcoal-brown painted outline; upright mixed-case. **No
> italics, no condensed display faces, no all-caps.** **Mercédès owns six
> balloons; the Count owns three.** Panel 4 carries no text of any kind. No
> captions and no prose fields. No quotation marks, speaker labels, page numbers,
> titles or pseudo-text. Comfortably readable when the page is reduced to 600 ×
> 900.
>
> **Continuity and meaning:** she opens with her son → she asks where he was born
> and he answers with nothing → she gives him her own origin, precisely, including
> Marseille and the age of nineteen → she apologises for a resemblance she has
> already stopped doubting → he declines to ask the name of her village → he walks
> away and her hand closes on the chair. **The full glass sits between them for
> the entire scene and is still full in the last panel after he has gone.** It is
> the same glass, at the same level, in panels 1, 3 and 4, and it is never lifted,
> sipped, moved, refilled or cleared.
>
> **Page-specific prohibitions:** **the Count never touches the glass on this
> page**; no servant clears it; no second glass appears in his hand; no plate of
> apricots; **no flashback, no memory inset, no young man in a white shirt, no
> Marseille, no harbour, no boat, no sea** — the resemblance she is describing is
> never depicted; no recognition scene, no gasp, no hand to the mouth, no tears.
> Standing prohibitions: no identity collision, no duplicated person, hand or
> object, no fused fingers, no illegible text, no crop sheet, no outer decorative
> frame.
>
> ## Reference images
> 1. `refs/approved/02-mercedes-1838.png` — Mercédès, **forty-two, unsmoothed, in
>    profile too.**
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/18-set-morcerf-house.png` — the Morcerf drawing room, its
>    corner, its table and chairs.
> 4. `refs/approved/21-objects.png` — **the tall wine glass, full and untouched.**
> 5. `pages/page-11.png` — promoted previous page; binds the corner, the hour, the
>    costumes and the glass.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 13 — *illustrated prose*

**Turn:** what she has known about her husband since 1815, and why she never said
it.
**Dominant:** Mercédès alone in front of a mirror — 65%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-13/candidates/page-13-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 13
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread. **This page is illustrated prose, not a dialogue page: it
> carries two matte parchment prose fields and no speech balloons at all.**
> Compose the two prose fields first and build the picture around them.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile silk, mirror glass, tortoiseshell,
> lacquer, cut crystal, wax and one candle flame, selective hard edges at her face
> in the glass and at her hands. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **the Morcerf house at its warmest and its emptiest** — burgundy,
> polished walnut, wax red, old gold, and **one candle** carrying the whole room.
> The room is crowded with beautiful things and none of them is doing her any
> good. Deep shadow occupies more than half the picture; the warmth is a trap, not
> a comfort.
>
> **Predecessor: attach the promoted page 12.** Same house, **very late** — hours
> after the party, the guests gone. What carries in and is load-bearing: **she is
> still in the same burgundy-black evening gown**, undisturbed, still dressed,
> still coiffed; the same face at the same age; the same night. **Do not show**
> the Count, Fernand, Albert, Haydée, Danglars, Villefort, a maid, a servant, a
> second woman, or any reflection of a second person in the mirror. **One human
> being on this page and no other, in the room or in the glass.**
>
> **Character lock.** One supplied canonical reference binds the only visible
> figure. **Mercédès, Comtesse de Morcerf, 42 and visibly forty-two:** decisive
> dark eyes; straight nose; lean mature cheeks; **visible lower-lid lines and
> temple lines**; **restrained grey threading the dark hair**, still sculpted into
> the formal 1838 coiffure she wore all evening; still, upright carriage;
> **burgundy-black vertical evening gown.** **Do not youth-wash her. This page is
> the one most likely to fail on it** — a woman alone at a mirror by candlelight
> is exactly where the smoothing happens, and a smoothed face here is a blocking
> defect. The age must be legible **both in the room and in the mirror**, and both
> must be the same woman at the same age.
>
> She must never read as a woman of twenty-seven with long unbound black hair and
> crimson-and-gold eastern embroidery. Her faces — the real one and the reflected
> one — must remain structurally distinct from every other face in this book even
> in profile, reduced scale, grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — **DOMINANT, roughly 65% of the page**, the upper two-thirds
>
> **Mercédès alone in front of a mirror, still in the gown, not undressing, not
> moving.** Seated or standing at a dressing table, hands at rest, **one candle**
> the only light. She is not looking at her own face for vanity and she is not
> crying: she is doing arithmetic and has just finished it. The mirror shows her
> face; the room around the mirror is **warm, burgundy, and crowded with beautiful
> things** — silver, crystal, ribbon, gilt, a jewel case — all of it worth money
> and none of it any use.
>
> One matte **warm cream** parchment prose field, placed in the **calm dark
> burgundy wall area beside the mirror** — **never over her face, never over the
> mirror glass, never over the crowded table of objects.** Width **78–88% of the
> canvas**, internal padding **≥42 px**, left-aligned with a calm ragged right
> edge. Exactly this text, set as **three paragraphs** — the break before `But in
> the winter` is a line-length accommodation and **changes not one character of
> the text**:
>
> `Mercédès de Morcerf had known about her husband since she was nineteen years old.`
>
> `Not the details. She had never had the details, and she had been careful for twenty-three years not to come into possession of any.`
>
> `But in the winter Edmond was taken, her cousin Fernand could not stay in a room where the name was spoken — and when word came that the prisoner had died in the fortress, Fernand wept before anyone else in Marseille had heard it.`
>
> ### Panel 2 — roughly 35% of the page, a wide band across the bottom
>
> **Her hands in her lap, seen in the mirror, holding nothing.** The reflection is
> the subject: the hands, the lap of the burgundy-black gown, the edge of the
> mirror frame, and — at the top edge of the reflection — the lower part of her
> face, unmoving. Empty open hands, palms slack, **no ring turned, no handkerchief,
> no letter, no fruit, no glass.** The candle is lower in this band than in panel
> 1 and the shadow has grown.
>
> One matte warm cream parchment prose field in a calm dark area of this band,
> **never over the hands and never over the reflected face.** Exactly this text,
> in two paragraphs:
>
> `She married him anyway. She had a son by him and made a house with him and was, for a time, something very near to happy.`
>
> `Tonight a man had refused to eat her fruit.`
>
> **Lettering:** all **5** prose paragraphs exactly once, in this order, with
> exact spelling, punctuation, capitalization, apostrophes and accents —
> **including the accents in `Mercédès` and the em dash in the third paragraph.**
> This page has **no speech balloons and no speaking characters**; do not add one.
> Prose lettering **36–42 px** on the 1024 × 1536 canvas, **never below 40 px for
> any character**; **38–52 characters per line**; field width **78–88% of canvas**;
> internal padding **≥42 px**; upright mixed-case literary serif, left-aligned.
> **No italics, no all-caps prose, no condensed display faces, no cursive.** No
> quotation marks, no speaker labels, no page number, no title, no date, no
> pseudo-text, no signature, and **no legible writing on any object in the room.**
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** the woman who spent the evening being a hostess is
> alone, still dressed, not moving → what she has known since she was nineteen →
> what she was careful never to learn → the one piece of evidence she could never
> unsee, which is a man weeping too early → she married him anyway, and made a
> life → and tonight a stranger refused her fruit. **The refusal on page 11 is the
> last line of this page and the reader must connect the two without help.**
>
> **Page-specific prohibitions:** **no flashback, no memory inset, no vignette of
> Marseille, of a young man, of a fortress, of a wedding, or of Fernand weeping** —
> every past event on this page exists only in the prose. No apricots and no plate
> in the room. No tears on her face, no hand to the mouth, no collapse, no
> theatrical grief: she is **still**. No second reflection, no doubled figure, no
> reflection that differs from the woman in the room. Standing prohibitions: no
> identity collision, no duplicated person, hand or object, no fused fingers, no
> illegible text, no crop sheet, no outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/02-mercedes-1838.png` — Mercédès, **forty-two, unsmoothed, in
>    the same gown she wore all evening.**
> 2. `refs/approved/18-set-morcerf-house.png` — binds the Morcerf house palette,
>    its walnut, gilt and burgundy; **the dressing room is not a view on that plate
>    and is designed here as a small warm over-furnished private room in the same
>    house.**
> 3. `pages/page-12.png` — promoted previous page; binds her face, her gown, her
>    coiffure and the hour.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 14 — *dramatic*

**Turn:** Haydée asks whether the wife knew him, and he lies to her for the first
time.
**Dominant:** Haydée looking at him steadily; his back turned to her — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-14/candidates/page-14-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 14
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile plaster, cold window glass, lacquered
> wood, spent candle wax and the first grey light, selective hard edges at the two
> faces and at the window frame. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **the Count's house** — lacquer black, ivory, unpolished new gold, and
> **near-dawn**: the cold grey-blue of the window has begun to go pale and thin at
> the bottom edge, the city lights outside are guttering out, and the three roofs
> are barely warm now. **One restrained note of deep crimson and gold** on Haydée
> — still the only colour in the room. The candles inside are dead or nearly dead;
> the light is coming from outside for the first time in the volume.
>
> **Predecessor: do not attach page 13.** Page 13 is a warm burgundy room in
> another house and is not a visual predecessor to this cold black one; attaching
> it will drag the wrong palette and the wrong woman into the frame. What carries
> in by description only: **the Count is still in the unrelieved black evening
> dress he wore all night at the Morcerf house**, slightly less immaculate than he
> was at the door — he has come straight home. **Haydée is still dressed from the
> evening, in the crimson-and-gold Epirote dress, because she has waited up and
> has not been to bed.** **Do not show** Mercédès, Fernand, Albert, Danglars,
> Villefort, any servant or any crowd. Two human beings on this page and no
> others.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **The Count, 42:** tall, columnar, still; clean-shaven; swept-back black wave
> with the first grey at the temples; deep-set black-brown eyes; strong straight
> brow; long clean nose; high cheekbones; hollow temples; **a slight asymmetry at
> the left corner of the mouth**; cultivated pallor; **unrelieved black 1838
> evening dress.**
> **Haydée, 27:** olive-gold skin; **long unbound black hair** or one heavy braid;
> large wide-set very dark eyes; straight brows; small straight nose; full mouth;
> slight build; **direct, unornamented stillness — she looks at people straight
> and does not arrange her face**; **crimson-and-gold Epirote dress, loose vertical
> silhouette — never a French 1838 waist, never a French coiffure, never a
> bonnet.**
>
> **Collision prohibition.** Haydée must never read as a French comtesse of
> forty-two with a sculpted formal coiffure and a fitted burgundy-black gown —
> that woman was in the previous page and must not follow the reader into this
> room. Haydée is twenty-seven, unbound-haired, loose-silhouetted, olive-gold. The
> Count must never carry a military moustache, a receding hairline, a thickened
> build, or a young man's chestnut hair and pale waistcoat.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Page staging rule, binding on every panel:** **Haydée holds the left, the
> Count holds the right**, and every balloon sits on its owner's side — including
> in panel 4, where his back is turned and his balloon still sits on the right.
>
> ### Panel 1 — roughly 17%, upper left, sharing the top tier with panel 2
>
> **Haydée in a doorway at the left, awake, still dressed, having waited up** —
> standing, not leaning, no blanket, no shawl, no candle in her hand; the
> stillness of someone who has been standing there a while. The Count at the right
> of the panel, just in from the street, black, still wearing the evening.
>
> Two warm-ivory balloons: hers upper left, his lower right, each tail to its
> owner's mouth. Exact strings, in this reading order:
>
> `Was he everything you wanted?`
>
> `More. He has a staircase.`
>
> ### Panel 2 — roughly 15%, upper right, completing the top tier
>
> Closer on both: her face at the left, his at the right. **He is still pleased —
> the appetite from the staircase is still on him** — and her question changes the
> temperature of the panel without changing anything on his face.
>
> Two warm-ivory balloons: hers upper left, his lower right. Exact strings, in
> this reading order:
>
> `And the wife?`
>
> `She was there.`
>
> ### Panel 3 — roughly 18%, a wide band across the middle
>
> **Haydée, not letting it go.** She is at the left of the band, level, entirely
> still, looking straight at him; the Count at the right, beginning to move away
> toward the window. Keep both figures low and small in the band: **the upper two
> thirds of this band is a reserved balloon lane.**
>
> Two warm-ivory balloons: hers at the upper left; his runs **wide and flat**
> across the right and below, set in two or three lines. Exact strings, in this
> reading order:
>
> `That is not what I asked you.`
>
> `She poured wine and asked me where I was born. She is a woman who runs a house.`
>
> ### Panel 4 — **DOMINANT, roughly 50% of the page**, the whole lower half
>
> **Haydée at the left, looking at him steadily** — full-length or three-quarter,
> face fully visible, absolutely still, the crimson and gold the only colour in a
> black room. **The Count at the right has turned back to the window, and the turn
> is the answer**: three-quarter back to us and fully back to her, the pale
> near-dawn window in front of him, the three roofs beyond, his face hidden or
> reduced to a rim of profile. The distance between them across the empty room is
> the subject and must be large.
>
> Two warm-ivory balloons: hers at the upper left, tail to her mouth; his at the
> lower right, tail to the hidden side of his head — **the tail must clearly reach
> him and must not point at the window, at the roofs, or at empty room.** Exact
> strings, in this reading order:
>
> `You have never lied to me before.`
>
> `Go to bed, Haydée.`
>
> **Lettering:** all **8** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization, apostrophes and accents — including the
> accent in **Haydée**. Balloon lettering **44–50 px** on the 1024 × 1536 canvas,
> **never below 40 px** for any character; `And the wife?`, `She was there.` and
> `Go to bed, Haydée.` may take the **48–54 px** short-reply size; balloons
> **240–390 px** wide, except his long string in panel 3, which runs **wide and
> flat** across its reserved lane — **if it will not set at 44 px inside that
> lane, widen the balloon and shrink the figures; never reduce the lettering.**
> Warm ivory fill with a restrained charcoal-brown painted outline; upright
> mixed-case. **No italics, no condensed display faces, no all-caps.** **Haydée
> owns four balloons; the Count owns four.** No captions and no prose fields. No
> quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** she has waited up → he is still full of the evening
> and answers about the staircase → she asks about the wife and he gives her three
> words → she refuses the three words → he answers with an inventory of a hostess,
> which is true and is not an answer → she names it as a lie → and he ends the
> conversation with his back to her. **The turn to the window is the lie**; the
> reader must be able to see that she can see it. He is at the same window as
> pages 1, 2 and 5, and the three roofs are the same three roofs.
>
> **Page-specific prohibitions:** no Mercédès anywhere — **no memory inset, no
> flashback, no imagined face, no burgundy-black gown, no apricots and no plate on
> this page**; no wine glass in the Count's hand; no anger from Haydée, no raised
> voice, no tears, no touching between them at any point; no daylight beyond the
> first thin grey at the bottom of the window; no sky in the room. Standing
> prohibitions: no identity collision, no duplicated person, hand or object, no
> fused fingers, no illegible text, no crop sheet, no outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the black room, the tall window, the
>    three roofs, the doorway.
>
> **No promoted previous page is attached to this page** — page 13 is a different
> house and a different palette. All other character sheets are **prohibited
> generation inputs** for this page.

---

---

## PAGE 15 — *illustrated prose*

**Turn:** his account of the evening — appetite intact, and one part he will not
go over.
**Dominant:** the empty black drawing room — 70%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-15/candidates/page-15-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 15
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile plaster, bare parquet, cold window
> glass, lacquered wood and unpolished new gold, selective hard edges only at the
> chair, the glass and the far figure. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey daylight, unpolished new gold.**
> Morning, and the light is flat, colourless and northern. There is no candle, no
> fire and no warm source anywhere on this page — the one red note in the whole
> image is the wine standing in the glass in the lower band.
>
> **Predecessor: attach the promoted page 14.** Same house, same black room and
> the same enormous drawing room beyond it, hours later: page 14 was near dawn
> and this is full morning. What carries: the room's emptiness, its scale, its
> cold, the same tall uncurtained windows. **Do not show** Haydée, Mercédès,
> Fernand, Albert, any servant, any visitor, any second figure of any kind. **At
> most one human being appears on this page and he is small and far away.**
>
> **Character lock.** One supplied canonical reference binds the only figure.
> **The Count, 42:** tall, columnar, unnaturally still, clean-shaven, swept-back
> black hair with the first grey at the temples, cultivated pallor, **unrelieved
> black**. On this page he is **one small black shape at the far end of the room,
> seen at a distance and not in close-up** — his identity is carried by
> silhouette alone: a tall slim unbroken black vertical with a swept-back dark
> head. He must never be given a heavy moustache, a thickened soldier's build,
> chestnut hair, or a pale waistcoat. No other figure anywhere on the page may
> carry that black columnar silhouette.
>
> ### Panel 1 — **DOMINANT, roughly 70% of the page**, the whole upper two-thirds
>
> The enormous drawing room in cold grey morning daylight, seen down its full
> length from the doorway. **Entirely empty: correct, huge, unlived-in.** Not one
> family object — no portraits, no books, no flowers, no clutter, no rug worth
> the name, nothing anyone has chosen for pleasure. **One single chair**, placed
> where nobody would place a chair to sit in company. Tall uncurtained windows
> down one wall with flat grey sky in them. The Count is a **small black shape at
> the far end**, standing, no bigger than a thumb-length in the frame, facing
> away.
>
> One matte **cold-ivory** parchment prose field, **upper third of the panel,
> laid against the large blank wall above the windows — never over a window,
> never over the chair, never over the figure.** Exactly this text, in two
> paragraphs:
>
> `He had wanted to remember every part of the evening and he did. The weight of Mondego's hand. The four seconds Villefort had held on. Danglars saying old friends to a man he had helped bury.`
>
> `He went over it three times before the candles were out, and each time it was better than the last, and that, he told himself, is the appetite of a man who has been patient and is owed it.`
>
> The words **old friends** are set in the same upright mixed-case letterform as
> the rest of the paragraph. **No italics, no quotation marks, no asterisks, no
> emphasis of any kind on those two words.**
>
> ### Panel 2 — roughly 30% of the page, a wide horizontal band across the bottom
>
> Close and low: **the single chair, and beside it on the bare floor a tall glass
> of red wine, full to the level it was poured at, untouched.** The light of a
> risen sun has **moved**: one long hard shadow runs from the glass far across
> empty parquet, and a second, older, fainter light-stain lies at a different
> angle beside it, so that the reader understands the glass has stood there for
> hours. Nobody is in this panel. No hand, no figure, no decanter being poured.
> The wine is **at the poured level, with a clean unmarked rim** — nobody has
> drunk from it.
>
> One matte cold-ivory parchment prose field in the calm dark floor area of this
> band, exactly this text, in two paragraphs:
>
> `There was one part of the evening he did not go over.`
>
> `He noticed that he was not going over it, and he went on not going over it.`
>
> **Lettering:** all **4** paragraphs, exactly once each, in this order, with
> exact spelling, punctuation and capitalization. This page has **no speech
> balloons and no speaking characters.** Prose fields: **36–42 px** lettering on
> the 1024 × 1536 canvas, **never below 40 px for any character**; **38–52
> characters per line**; field width **78–88% of canvas**; internal padding **≥42
> px**; two fields on this page and no more; left-aligned with a calm ragged
> right edge; upright mixed-case literary serif. **No italics, no all-caps prose,
> no condensed display faces, no cursive.** No quotation marks, no speaker
> labels, no page number, no title, no pseudo-text, no signature, no writing on
> any surface in the room. Comfortably readable when the page is reduced to 600 ×
> 900.
>
> **Continuity and meaning:** a huge empty correct room in flat morning light →
> one man too far away to read → a chair nobody sits in → a full glass nobody
> drank, with the light moved across it. The glass is the volume's running motif
> and its state here is the point: **this is his own house, there is no enemy to
> perform for, and he still did not drink it.** He refused a glass under
> Fernand's roof on page 8 and fruit from Mercédès' garden on page 11; here the
> habit has nobody to aim at.
>
> No second figure, no face in close-up, no servant, no fire, no candle, no
> clutter, no portrait, no lettering on the walls, no identity collision,
> duplicated person, duplicated glass, duplicated chair, fused fingers, illegible
> text, crop sheet, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — binds the distant figure's silhouette,
>    build and unrelieved black costume.
> 2. `refs/approved/17-set-count-house.png` — binds the drawing room, its
>    emptiness, the windows and the palette.
> 3. `refs/approved/21-objects.png` — binds the tall wine glass, standing full and
>    untouched.
> 4. `pages/page-14.png` — promoted previous page; binds the room and its cold.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 16 — *dramatic*

**Turn:** Mercédès does not warn her husband. She warns nobody.
**Dominant:** Mercédès below him on the stairs — 60%.
**Locations:** 1. **Panels:** 3.
**Output:** `qa/production/page-16/candidates/page-16-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 16
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile polished walnut, gilt frames, waxed
> banister, heavy silk and guttering candle wax, selective hard edges at the two
> faces and at the handrail. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **burgundy, polished walnut, wax red, old gold, dense candle amber** —
> a house overstuffed with purchased legitimacy, too many portraits and too much
> gilt, warm and crowded and trying too hard. The candles are low and the amber
> is going out of the hall.
>
> **Predecessor:** the immediately preceding page 15 is a different house on a
> different morning and is **not** a visual predecessor — **do not attach page
> 15.** **Attach the promoted page 13 instead.** This page steps back to the night
> of the party, at the other end of Paris, in the same hours as pages 8 to 13.
> What carries from page 13: Mercédès in **the same evening gown she wore all
> evening**, the same dressed hair, the same house, the same dying candle amber.
> Fernand is in the same evening dress he wore on pages 8 to 12, **coat open now**,
> the decorations still on his chest. **Do not show** the Count, Haydée, Albert,
> Danglars, Villefort, Beauchamp, any guest, or any servant. **Two people on this
> page and no others** — the house is empty of company and that is the point.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, heavy black brows
> set low and close, deep-set close dark eyes, weathered ruddy-olive skin coarser
> than any other face in this volume, **heavy iron-and-black military moustache**,
> black hair **receding at the temples** and iron-grey at the sides, thick neck,
> heavy upright soldier's build, evening dress with a **chest of wax-red and old-gold
> decorations**, coat open, expansive.
> **Mercédès, Comtesse de Morcerf, 42:** decisive wide-set eyes, straight nose,
> lean mature cheeks, **visibly forty-two — temple lines and lower-lid lines
> present and drawn, restrained grey threads at the temple**, dark hair sculpted
> into formal 1838 dress, burgundy-black vertical evening gown, still upright
> carriage. **A smoothed, youth-washed, beautiful blank face is a defect on this
> page.** She must never be given unbound black hair, gold embroidery, an Epirote
> silhouette, or a late-twenties face.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Fernand is always upper and on the right.
> Mercédès is always lower and on the left.** That relationship holds in all three
> panels and every balloon sits on its owner's side.
>
> ### Panel 1 — roughly 20% of the page, a wide band across the top
>
> The top of the general's staircase. **Fernand at the head of the stairs on the
> right**, coat open, one hand on the newel, expansive, pleased, looking down and
> away past the reader toward the hall below, where the **last carriage of the
> party is pulling out of the porte-cochère** — its lamp small and yellow and
> already leaving. **Mercédès on the left, three or four steps below him**, seen
> from the shoulders up, still, facing up the stairs.
>
> One matte **warm-cream** parchment caption rectangle, **upper left, laid over
> the dark panelling and never over a face or the banister**, tail-free, exactly:
>
> `That same night, at the other end of Paris — the last carriage of the party.`
>
> Then two warm-ivory balloons. Reserve both lanes **before** placing the figures.
> Fernand's balloon **upper right**, short tail to his mouth, exactly:
>
> `He'll come again. He said so himself.`
>
> Mercédès' balloon **lower left, below and left of his**, short tail to her mouth,
> exactly:
>
> `Did he.`
>
> ### Panel 2 — roughly 20% of the page, a wide band directly beneath
>
> Closer: **Fernand's head and shoulders on the right**, turning down toward her,
> the smile going; **Mercédès' head and shoulders on the left**, lower in the
> frame, not moving. Three balloons in strict descending order, each on its owner's
> side:
>
> `You didn't like him.`
>
> `I didn't say that.`
>
> `You went up at eleven.`
>
> The first and third are Fernand's and sit on the **right**, upper and lower. The
> second is Mercédès' and sits on the **left**, between them in height. The reading
> path descends steadily and never crosses back upward.
>
> ### Panel 3 — **DOMINANT, roughly 60% of the page**, the whole lower half
>
> The full height of the general's staircase, seen from the hall below and to one
> side, so the reader gets **the whole warm crowded hall in one image**: the gilt,
> the massed portraits of a family that is not his, the guttering candle amber, the
> polished walnut. **Fernand small and high at the top of the flight on the right,
> looking down.** **Mercédès below him on the stairs on the left,** one hand on the
> banister, looking up at her husband. Real distance between them, held on the
> staircase, rendered as a large quiet panel with a lot of empty air in it. This is
> a long beat and the panel's job is to make the reader feel it.
>
> Four warm-ivory balloons, in strict descending order down the panel, each on its
> owner's side:
>
> `I was tired.`
>
> `Fernand.`
>
> `What?`
>
> `Nothing. Put out the lamps.`
>
> The first, second and fourth are Mercédès' and sit on the **left**; the third is
> Fernand's and sits on the **right**, between the second and the fourth in height.
> Four short balloons, four short tails, no crossing tails, no ambiguity about who
> is holding the last line.
>
> **Lettering:** **1** caption and **9** balloon strings, exactly once each, in this
> order, with exact spelling, punctuation, capitalization, apostrophes and accents.
> Balloon lettering **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**;
> short replies such as `Did he.`, `Fernand.` and `What?` at **48–54 px**; balloon
> widths **240–390 px**; warm ivory fill, never pure digital white, with a
> restrained charcoal-brown painted outline; upright mixed-case. Caption lettering
> **36–42 px**, never below 40 px, on matte warm-cream parchment, tail-free, in a
> calm dark area. **No italics, no condensed display faces, no all-caps.** Fernand
> owns four balloons, Mercédès owns five. Tails touch only their two mouths, exactly
> as assigned. No quotation marks, speaker labels, page numbers, titles, dates in
> the art, or pseudo-text on the portraits. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** the last carriage leaves → he is delighted with his
> famous guest → she will not agree with him → he pushes at her silence → she says
> his name, and then does not say the thing after it. She had it in her mouth and
> swallowed it. **Nothing on this page may telegraph what she nearly said** — no
> significant glance at a portrait, no hand to the heart, no tear. Her face is
> closed and the panel is large so the reader has to sit in it.
>
> No third figure, no guest, no servant, no dog, no clock face with hands worth
> reading, no identity collision, duplicated person or hand, fused fingers,
> illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/03-fernand-1838.png` — Fernand, with the moustache, the
>    receding temples and the decorations.
> 2. `refs/approved/02-mercedes-1838.png` — Mercédès at forty-two, evening gown.
> 3. `refs/approved/18-set-morcerf-house.png` — binds the general's staircase, the
>    hall and the palette. **This is the same staircase as pages 6, 8 and 47.**
> 4. `pages/page-13.png` — promoted page from the same night; binds Mercédès' gown,
>    hair and the house's candle amber.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 17 — *dramatic*

**Turn:** offered a way out, he refuses it and chooses the pleasure out loud.
**Dominant:** the Count at the window, smiling — 45%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-17/candidates/page-17-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 17
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile heavy wool cloak, bare wood, cold
> glass and flat plaster, selective hard edges at the two faces, the hands and the
> cloak. **Not smooth prestige-oil realism.** No glossy concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey daylight, unpolished new gold**, with
> **one restrained note of deep crimson and gold** on Haydée — the only colour in
> the room. Flat morning light from tall uncurtained windows. No lamp, no candle,
> no fire: the night is over and nothing was lit to replace it.
>
> **Predecessor: attach the promoted page 15.** Same house, same morning, the same
> flat grey light. What carries: the room's emptiness and scale, the tall
> uncurtained windows, the cold. **The Count is in the same black evening clothes
> he wore to the party** — he has not been to bed and has not changed; the clothes
> are a night old and read as such. **Do not show** Mercédès, Fernand, Albert,
> Danglars, Villefort, Beauchamp, any servant, any visitor. **Two people on this
> page and no others** — this man has no valet, no steward and no household, and
> the emptiness of the room is an argument.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, deep-set black-brown eyes, strong straight
> brow, long clean nose, high cheekbones, **a slight asymmetry at the left corner
> of the mouth**, cultivated pallor, hollow temples, **unrelieved black**. Never a
> heavy moustache, never a thickened soldier's build, never chestnut hair or a pale
> waistcoat.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build, direct
> unornamented stillness, **crimson-and-gold Epirote dress with a loose vertical
> silhouette — never a French 1838 waist and never a sculpted French coiffure.**
> She is twenty-seven and must not be drawn as a woman in her forties.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Haydée holds the left of every panel she is in;
> the Count holds the right.** Every balloon sits on its owner's side.
>
> **Balloon lanes are reserved before the figures are placed, on this page above
> all others.** Panels 2 and 4 carry long speeches and the figures are staged
> around the lettering, not the reverse. If the strings named below cannot be set
> at 44–50 px inside their panels, **stop and return the page to the plan owner.
> Do not shrink the type and do not drop a word.**
>
> ### Panel 1 — roughly 13% of the page, a wide band across the top
>
> A doorway in the black room. **Haydée in the doorway on the left**, standing,
> **his heavy black cloak still over her arm from the night before**. **The Count
> on the right**, seated or standing at the far side of the frame, still in last
> night's clothes, unshaven only in the sense of being worn — he has not slept and
> the face shows it.
>
> Two warm-ivory balloons, both **wide and shallow rather than tall**, so this
> narrow band can hold them at full lettering height. Haydée's on the **left**,
> tail to her mouth, exactly:
>
> `You did not sleep.`
>
> The Count's on the **right**, tail to his mouth, exactly:
>
> `No.`
>
> ### Panel 2 — roughly 20% of the page, a wide band directly beneath
>
> Haydée has come into the room. **She puts the cloak down on a bare low table
> between them** — hands, cloak, table, and the two figures flanking it, left and
> right. Framed from the waist up and staged wide, with **the upper two-thirds of
> this band left clear as a protected lettering lane** and the cloak, the table and
> the two figures occupying the lower third.
>
> Three warm-ivory balloons, **all Haydée's**, all on the **left and centre-left**,
> in strict left-to-right, top-to-bottom reading order, tails to her mouth. The
> Count receives no balloon in this panel and is silent. Exactly, and split across
> the three balloons exactly as broken here:
>
> `If this is going to cost you something, say so now.`
>
> `Let me go to the newspapers with my father's name and my own face.`
>
> `You need never go into that house again.`
>
> The second and third balloons are **one continuous speech in two linked
> balloons** with a small connecting bridge between them, both tailed to the same
> mouth, so no reader can assign either to the Count.
>
> ### Panel 3 — roughly 12% of the page, a narrow band
>
> **The Count alone**, close, three-quarter, **no balloon, no caption, no sound —
> a silent panel.** He is considering it. Not amused, not dismissive: a man who has
> genuinely been offered a way out and is looking at it. The flinch lives here and
> it is entirely carried by the face.
>
> **This panel contains no text of any kind.**
>
> ### Panel 4 — **DOMINANT, roughly 45% of the page**, the large lower-middle block
>
> The Count at the tall window in flat morning light, **turned back into the room
> on the right of the frame**, and **for the first time in this volume he smiles
> with his whole face** — a wide, delighted, entirely un-serene smile that reaches
> the eyes, with the slight asymmetry at the left corner of the mouth doing its
> work. This is appetite, chosen in daylight, after a flinch, and it must be
> unmistakable and slightly frightening. Haydée stands small on the **left**,
> watching, silent in this panel and receiving no balloon. Grey city light behind
> the glass; the room around them stays empty.
>
> Three warm-ivory balloons, **all the Count's**, on the **right**, in strict
> descending order, tails to his mouth, exactly:
>
> `He held my hand on his own staircase and told me he earned it.`
>
> `No. I want to be in the room.`
>
> `I want to be at his table when it goes. And I want it to take a long time.`
>
> ### Panel 5 — roughly 10% of the page, a wide band across the bottom
>
> **Haydée on the left**, head and shoulders, watching him; **the Count on the
> right**, mostly turned away. She has got what she wanted and it has told her
> something she did not ask for, and her face carries that and nothing louder.
>
> Two warm-ivory balloons, **wide and shallow**, each on its owner's side, exactly:
>
> `Then you are not doing this for my father.`
>
> `No.`
>
> The first is Haydée's on the left, the second is the Count's on the right.
>
> **Lettering:** **10** balloon strings, exactly once each, in this order, with
> exact spelling, punctuation, capitalization, apostrophes and accents. **Two
> separate balloons on this page read `No.`** — one from the Count in panel 1 and
> one from the Count in panel 5 — and both must be present. Balloon lettering
> **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**; the short replies
> at **48–54 px**; balloon widths **240–390 px**, except in the narrow bands
> (panels 1 and 5) where a **wider, shallower balloon up to roughly 620 px across
> and two lines deep** is required so that the lettering height is never
> compromised — **the lettering height governs, the balloon shape yields**. Warm
> ivory fill, never pure digital white, restrained charcoal-brown painted outline,
> upright mixed-case. **No italics, no condensed display faces, no all-caps.** The
> Count owns six balloons, Haydée owns four. Panel 3 owns none. No captions on this
> page. No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** she finds him awake → she puts the cloak and the
> question on the table together → he actually considers the way out, in silence →
> he refuses it, smiling, and names the pleasure out loud → she hears whose revenge
> this is. The silent panel 3 is load-bearing: without a visible flinch, the smile
> in panel 4 is just villainy. **The smile must be the largest emotional event on
> the page and it must live in the dominant panel.**
>
> No third figure, no servant, no lamp, no candle, no fire, no clutter, no
> newspaper, no document on this page, no identity collision, duplicated person or
> hand, fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the black room, the doorway and the
>    tall windows.
> 4. `pages/page-15.png` — promoted previous page; binds the room, the morning light
>    and the emptiness.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 18 — *dramatic*

**Turn:** Haydée produces the proof she has been holding for four years.
**Dominant:** the document flat under the lamp — 55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-18/candidates/page-18-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 18
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile worn leather, heavy laid paper, dark
> red sealing wax, brass, black lacquered wood and lamp glass, selective hard
> edges at the document, the seal and the four hands. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, unpolished new gold**, one warm pool of oil-lamp
> light on the table and everything outside that pool going to black; **one
> restrained note of deep crimson and gold** on Haydée. **The red wax seal is the
> hottest colour on the page.**
>
> **Predecessor: attach the promoted page 17.** Same house, same two people. Time
> has moved to evening: the tall windows are black and **one small brass oil lamp
> with a glass chimney** is lit on a small bare table. What carries: the room's
> emptiness and scale, both characters' faces and builds. **The Count is now in
> fresh unrelieved black**, not the night-old clothes of page 17. **Do not show**
> Mercédès, Fernand, Albert, Danglars, Villefort, Beauchamp, any servant, any
> clerk, any third person. **Two people on this page and no others.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with first grey at the temples, deep-set black-brown eyes, strong straight brow,
> long clean nose, high cheekbones, **slight asymmetry at the left corner of the
> mouth**, cultivated pallor, **unrelieved black**. Never a heavy moustache, never
> a thickened soldier's build, never chestnut hair or a light waistcoat.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build, direct
> unornamented stillness, **crimson-and-gold Epirote dress, loose vertical
> silhouette — never a French 1838 waist, never a sculpted French coiffure, never a
> forty-year-old face.**
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Haydée sits on the left of the table, the Count
> on the right, in every panel.** Every balloon sits on its owner's side.
>
> ### Panel 1 — roughly 20% of the page, a wide band across the top
>
> A small bare table, two plain chairs, one lamp, and black on every side. **Haydée
> sitting down opposite him on the left**, deliberately — the movement of a person
> who has decided something — with **a flat worn leather travelling case held flat
> in both hands**. The Count on the right, watching her sit. The case is closed.
>
> One warm-ivory balloon, **wide and shallow**, on the **left** over the black
> ground, tail to Haydée's mouth, exactly:
>
> `You have kept me four years and asked me for nothing. I have had this for all four of them.`
>
> ### Panel 2 — roughly 15% of the page, a wide band directly beneath
>
> Two faces across the lamp, close. The case is now open on the table between them
> and a **large folded sheet of heavy paper** is out of it.
>
> Two warm-ivory balloons, each on its owner's side, the Count's first and on the
> **right**, Haydée's reply on the **left** and lower, exactly:
>
> `You never showed me.`
>
> `No. I thought you would take it.`
>
> ### Panel 3 — **DOMINANT, roughly 55% of the page**, the large lower-middle block
>
> Looking down onto the table from above and slightly to one side. **The document
> flat on the table between them under the lamp, very large in frame** — a heavy
> sheet of laid paper, unfolded, with an eastern script on the upper part, a
> French signature low on the right, and **a broken red wax seal**. **Both their
> hands are near it, at the edges of the frame, and neither is touching it.**
> Haydée's hands enter from the left, the Count's long pale hands from the right.
> Faces are out of frame or at the frame's top edge; **the document is the subject
> of this panel.**
>
> **The writing on the document renders as marks and not as legible words.** The
> eastern script, the signature and any figures are visible as ink texture,
> convincing at a glance and unreadable at any magnification. **No story logic on
> this page depends on reading it, and no readable French or Greek word may appear
> on it.** The red wax seal is intact enough to read as a seal and is the
> brightest thing in the image.
>
> Three warm-ivory balloons in strict descending order, in the black outside the
> lamp pool, never over the paper. The Count's is first and sits on the **right**;
> Haydée's two follow, both on the **left**, tails to her mouth, exactly:
>
> `He learned to write his name, then. For this.`
>
> `It is a receipt. He sold my mother and me in the market at Constantinople.`
>
> `He signed for the money the way a man signs for a horse.`
>
> ### Panel 4 — roughly 10% of the page, a wide band across the bottom
>
> **The Count's face over the lamp**, lit from below by it, on the **right** of the
> band; the top of Haydée's head and shoulder small at the left, silent, no balloon.
> This is the best thing that has ever happened to him and **he is trying not to let
> it show and not entirely succeeding** — the control is visible, and so is what it
> is controlling. Not serenity. Appetite, held down.
>
> One warm-ivory balloon, **wide and shallow**, on the **right**, tail to his mouth,
> exactly:
>
> `Tell me all of it. From the beginning.`
>
> **Lettering:** **7** balloon strings, exactly once each, in this order, with exact
> spelling, punctuation, capitalization, apostrophes and accents. Balloon lettering
> **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**; balloon widths
> **240–390 px**, except in the narrow top and bottom bands where a **wider,
> shallower balloon up to roughly 620 px across** is required so that lettering
> height is never compromised — **the lettering height governs, the balloon shape
> yields**. Warm ivory fill, never pure digital white, restrained charcoal-brown
> painted outline, upright mixed-case. **No italics, no condensed display faces, no
> all-caps.** Haydée owns four balloons, the Count owns three. No balloon and no
> tail crosses the document. No captions on this page. **The only writing rendered
> anywhere on this page is inside the seven balloons** — the document carries no
> legible words. No quotation marks, speaker labels, page numbers, titles or
> pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** she sits down opposite him with a case → she says she
> has held it for four years → the receipt lies between them and neither will touch
> it → he asks for the whole story, and cannot quite keep his face. This is the same
> document that both of them hold on page 22, that passes back into her hands on
> page 30 and that she carries through the door of the Chamber on page 32 — **draw
> it so it is redrawable: same size, same fold pattern, same broken red seal, same
> ink layout.**
>
> No third figure, no servant, no clerk, no fire, no clutter, no second document, no
> books, no identity collision, duplicated person, duplicated hand or duplicated
> document, fused fingers, illegible balloon text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the black room, the low table, the one
>    lamp, the black windows.
> 4. `refs/approved/21-objects.png` — binds the large folded document with the broken
>    red wax seal and the flat travelling case sized to hold it. **The handwriting on
>    it is marks, not words.**
> 5. `pages/page-17.png` — promoted previous page; binds the room and both faces.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 19 — *spectacle*

**Turn:** Janina, 1822 — the other world, and a shut gate with a French hand on
it.
**Dominant:** the white fortress under hard light — 70%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-19/candidates/page-19-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 19
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile sun-heated limestone, dust, dry
> cypress, iron strapwork, worn timber and open water, selective hard edges at the
> fortress wall, the gate and the lock. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness, no travel-poster prettiness.
>
> Palette: **white limestone, cypress black, Ionian blue, sun-bleached ochre**,
> under **hard high Mediterranean noon light** with short black shadows. **This
> page must not look like Paris and must not be mistaken for it.** Paris in this
> book is candlelit, interior, vertical and cold; **this is outdoors, horizontal,
> bleached, hot and open, and it is the only place in the volume with a sky in
> it.** The sky is a large, real, load-bearing part of the image.
>
> **Predecessor:** page 18 was a black interior in Paris by lamplight. **Do not
> attach page 18 and do not carry any part of its palette, light or architecture
> into this page.** The break between the two pages is the point: the reader must
> feel the world change on the turn. This page is a memory of Greece in 1822,
> sixteen years before the rest of the volume. **Do not show** the Count, Haydée,
> Mercédès, Fernand's face, Albert, Danglars, Villefort, Beauchamp, any Paris
> interior, any lamp, any candle, any gilt, any evening dress.
>
> **Character lock.** There are no locked named characters on this page and **no
> character reference sheet is attached.** One unnamed figure appears in panel 2:
> **a French officer of 1822, seen from behind only.** He is a back, a shoulder
> line, a plain dark 1820s French officer's coat and one bare hand. **No face, no
> profile, no eye, no moustache, no decorations, no medals, no identifying mark.**
> His identity is deliberately withheld on this page. He must not be given a heavy
> military moustache, a chest of orders, or any other feature that would let a
> reader name him here — the reader learns who he was two pages later and not
> before.
>
> ### Panel 1 — **DOMINANT, roughly 70% of the page**, the whole upper two-thirds
>
> A **white limestone lake-fortress** standing above a wide blue lake, seen from
> across the water in enormous hard noon light: long horizontal walls, a low round
> tower, black cypresses standing up against the white, sun-bleached ochre hills
> behind, and a great open sky above all of it. **Horizontal composition, wide,
> bright, outdoors, alive.** A handful of tiny figures on the wall for scale, too
> small to have faces. No fire, no smoke, no damage — this is Janina before
> anything happened to it.
>
> One matte **sun-bleached ochre** parchment caption rectangle, **upper left, laid
> against the plain sky and never over the fortress**, tail-free, exactly:
>
> `Janina. 1822.`
>
> ### Panel 2 — roughly 30% of the page, a wide low band across the bottom
>
> A wide low strip, close in: **the eastern gate of the fortress, shut** — heavy
> timber, iron straps, a black iron lock plate, white limestone jambs each side,
> in deep raking shadow with the glare of the square beyond it. **The back of a
> French officer stands in the shadow of the gate, one hand flat on the lock.** No
> face. The hand is the subject of the panel: bare, deliberate, resting on the
> lock of a gate that is closed.
>
> **No text of any kind in this panel.**
>
> **Lettering:** exactly **1** string on this page, once, with exact spelling,
> punctuation and capitalization: `Janina. 1822.` Caption lettering **36–42 px** on
> the 1024 × 1536 canvas, **never below 40 px**, on a matte sun-bleached ochre
> parchment rectangle, tail-free, in the calm sky area, internal padding **≥42 px**,
> upright mixed-case literary serif. **No italics, no all-caps prose, no condensed
> display faces.** This is a spectacle page and text occupies well under 15% of
> visual attention. **No speech balloons, no speaking characters, no second
> caption, no date anywhere else on the page, no signage, no inscription on the
> gate, no pseudo-text, no page number, no title.** Comfortably readable at 600 ×
> 900.
>
> **Continuity and meaning:** a white fortress in hard light, whole and alive → the
> one gate that matters, shut, with a foreign hand on the lock. This fortress is the
> same building that burns on page 20 and the same building Beauchamp walks up to,
> unburned and sixteen years older, on page 29 — **draw it so it is recognizable
> again: same wall line, same round tower, same lake, same cypresses.**
>
> No Paris, no interior, no lamp, no candle, no gilt, no snow, no rain, no northern
> light, no visible face, no crowd, no violence, no identity collision, duplicated
> figure or hand, fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/20-set-janina.png` — binds the white lake fortress, the shut
>    gate, the light and the palette.
>
> All character sheets without exception are **prohibited generation inputs** for
> this page.

---

## PAGE 20 — *illustrated prose*

**Turn:** the gate opened, the head carried through, the price paid — and his
hands flat on the Paris table.
**Dominant:** fire on the walls — 55%.
**Locations:** 1. **Panels:** 3.
**Output:** `qa/production/page-20/candidates/page-20-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 20
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile limestone, smoke, night water, brass,
> lamp glass and black lacquered wood, selective hard edges at the pavilion, the
> lamp and the two hands. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **white limestone going orange, cypress black, deep night blue, and
> fire** — fire is the accent and the only warm source in the Janina panels. In the
> Paris half of panel 3 the palette switches hard to **lacquer black, ivory and one
> small pool of lamp-yellow**.
>
> **Predecessor: attach the promoted page 19.** Same fortress, same lake, same
> world, now at night and burning. What carries: the wall line, the round tower,
> the cypresses, the lake. **Do not show** Fernand's face, Danglars, Villefort,
> Albert, Beauchamp, Mercédès, any Paris interior except in panel 3, any gore, any
> severed head, any body, any wound, any blood.
>
> **Character locks.** No face is legible anywhere on this page. Two locked figures
> appear as **small distant shapes only** — **Haydée's mother, mid-thirties, plain
> travelling clothes, black hair under a plain dark headcloth**, and **Haydée at
> eleven, a slight girl in a plain undyed Epirote child's dress with one band of
> dark embroidery** — both fully clothed, both drawn with dignity, both too small
> and too far for a face. **The Count, 42,** appears in the last panel **as two
> hands and two black cuffs only**: long, pale, strong hands, unrelieved black
> sleeves, no face, no head, no shoulders. No other figure on this page may carry a
> recognizable identity.
>
> ### Panel 1 — **DOMINANT, roughly 55% of the page**, the top
>
> **Fire on the fortress walls at night.** The same white limestone walls from page
> 19, seen from a distance across the dark lake, now lit orange from within, smoke
> going up into a black sky, the cypresses black against it. **Figures far off and
> very small on the walls and below them — no faces, no gore, no bodies, no
> weapons in close-up. The scale is the horror**: a large building full of fire and
> people the size of pinheads.
>
> One matte **sun-bleached ochre** parchment prose field, **upper left of this
> panel, laid against the plain black sky — never over the fire and never over the
> walls.** Exactly this text, in two paragraphs:
>
> `My father had four hundred men, a lake at his back, and a French officer he trusted with the eastern gate, because the French were professionals and had no quarrel of their own.`
>
> `The officer went out under a white flag to negotiate terms. He came back having agreed to them. The terms were four hundred thousand francs, and the gate was opened at two in the morning.`
>
> ### Panel 2 — roughly 25% of the page, a wide band beneath
>
> **Compose the prose field first and the art around it.** A wide band of night
> water and dark sky. **A small stone pavilion by the water with one lamp burning
> inside it**, low in the band, small and far, and **two shapes waiting in it — a
> woman and a child, seen as silhouettes against the lamp, no faces.** The rest of
> the band is calm dark water and sky, and the prose field sits in it.
>
> One matte sun-bleached ochre parchment prose field occupying the upper portion of
> this band, exactly this text, in two paragraphs:
>
> `They carried his head through the town at first light, so that the province would understand it was over.`
>
> `My mother and I were in the pavilion by the water where he had left us, waiting for the officer to come back for us. He did.`
>
> **Nothing carried through the town is depicted.** There is no procession, no
> head, no body, no crowd and no blood anywhere in this panel or on this page — the
> sentence carries it and the image does not.
>
> ### Panel 3 — roughly 20% of the page, a wide band across the bottom — **the
> match cut, held in one frame**
>
> **One single panel containing two places at once, divided by the composition and
> not by any border, gutter, line, split-screen device or panel edge.** There is no
> border between the two halves. The image is continuous and the two worlds meet in
> the middle of it.
>
> **Left, and far away:** the inside of the stone pavilion in Janina, **empty** —
> the woman and the child gone — and **a small brass oil lamp with a glass chimney
> knocked over on the floor and still burning**, its spilled flame running along the
> stone. Hot orange, white limestone, night blue.
>
> **Right, and much nearer to the reader:** **the same lamp — the identical brass
> oil lamp with the identical glass chimney, the same height, the same handle, the
> same shape — standing upright on the Count's low black lacquered table in Paris**,
> and on either side of it **his two long pale hands flat on the black wood**. Cold
> lacquer black, ivory, one pool of lamp-yellow. **He is listening. The hands are
> not relaxed: the fingers are spread and pressed down, and the tension in them is
> the only emotion visible in the frame.** No face, no head, no shoulders, no
> Haydée, no chair.
>
> **The cut must read as the same lamp in two places.** Render both lamps from a
> single design — the same object, once fallen and burning in Greece, once standing
> in Paris — and let that identity override any difference between the two attached
> setting plates. Nothing else in the frame is duplicated: **one pavilion, one
> table, exactly two lamps, exactly two hands.** The two palettes collide along the
> middle of the frame without blending into each other; the collision is the point.
>
> **No text of any kind in this panel.**
>
> **Lettering:** all **4** paragraphs, exactly once each, in this order, with exact
> spelling, punctuation and capitalization. This page has **no speech balloons and
> no speaking characters** — the words are Haydée's narration, set as narrative
> prose and not as speech. Prose fields: **36–42 px** lettering on the 1024 × 1536
> canvas, **never below 40 px for any character**; **38–52 characters per line**;
> field width **78–88% of canvas**; internal padding **≥42 px**; **two fields on
> this page and no more**; left-aligned with a calm ragged right edge; upright
> mixed-case literary serif. **No italics, no all-caps prose, no condensed display
> faces.** No quotation marks, no speaker labels, no page number, no title, no
> pseudo-text, no writing on any surface. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** the trusted officer opened the gate for money → the
> fortress burned and the Pasha's head was carried through the town → the woman and
> the child waited in the pavilion for the officer to come back, and he did → and
> the man being told all this, sixteen years later, has his hands flat on a table in
> Paris. **The last panel exists so that the Count is inside his own mechanism and
> not off-page while it runs.** The lamp on his table is the same lamp lit on pages
> 18 and 22 and again on page 26.
>
> No gore, no severed head, no body, no blood, no wound, no chains, no nudity, no
> leering crowd, no legible face, no Paris interior outside panel 3, no border or
> gutter inside panel 3, no identity collision, duplicated person, duplicated hand
> or third lamp, fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/20-set-janina.png` — binds the fortress, the lake and the stone
>    pavilion with its lamp.
> 2. `refs/approved/09-janina-1822.png` — binds the mother and the eleven-year-old
>    girl as distant silhouettes, clothed and dignified.
> 3. `refs/approved/17-set-count-house.png` — binds the Paris half of panel 3: the
>    low black lacquered table and the one lamp.
> 4. `refs/approved/01-count-1838.png` — binds the two hands and the black cuffs
>    only.
> 5. `pages/page-19.png` — promoted previous page; binds the fortress, the lake and
>    the Janina palette.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 21 — *spectacle*

**Turn:** the market. A mother sold, a child's hand let go of.
**Dominant:** two hands coming apart — 65%.
**Locations:** 1. **Panels:** 3.
**Output:** `qa/production/page-21/candidates/page-21-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 21
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile dust, whitewashed wall, dry timber,
> coarse linen, worn ledger calf, sealing wax and dulled coin metal, selective hard
> edges at the two hands and at the coins. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **dust, bleached white, heat-glare, indigo shadow.** Flat hammering
> midday heat. **The accent of this page is restraint**: nothing on it is dramatic
> lighting, nothing is spectacle, and the loudest thing in the image is a gap
> between two hands.
>
> **Predecessor: attach the promoted page 20**, whose first two panels bind this
> world's light and palette — hard southern sun, bleached stone, indigo shadow.
> **This is Constantinople, not Janina**: no lake, no lake-fortress, no cypress
> hills, no fire. **Do not show** the Count, Haydée as an adult, Mercédès, Fernand,
> Albert, Danglars, Villefort, Beauchamp, any Paris interior, any lamp, any candle,
> any gilt.
>
> **Restraint is mandatory and is a blocking condition on this page.** The subject
> is a child watching her mother sold, and then losing her. **This page contains no
> nudity, no partial nudity, no bare shoulders or backs, no chains, no ropes, no
> shackles, no cages, no platform, no auction block, no whip, no violence, no
> restraint of any kind, no person being handled or displayed, no leering, no
> jeering, no crowd looking at anybody, and no distress rendered for effect.**
> Everyone visible is fully and plainly clothed and is going about ordinary
> business. **The image is two hands and a ledger. It cannot be built any other
> way.** If any element of this page would require a person to be shown as
> merchandise, that element is omitted — the caption carries the fact and the
> picture does not.
>
> **Character locks.** No face appears anywhere on this page. Two locked figures
> are present **as hands only** — **the mother, mid-thirties**, and **Haydée at
> eleven**. Both are fully clothed to the wrist; the reference sheet binds the two
> hands and nothing else. No other identity may be read anywhere in the image.
>
> ### Panel 1 — roughly 20% of the page, a wide band across the top
>
> A wide public square in Constantinople, **seen from a considerable distance and
> slightly above**, under heat-glare: bleached white walls, dust in the air, deep
> indigo shade under awnings, a few dry trees. It is **crowded, ordinary and
> businesslike** — porters, bales, baskets, awnings, animals, men doing paperwork
> in the shade. The figures are far too small to have faces or to be looked at
> individually. **Nothing in this panel is a spectacle of cruelty. It is a place
> where things are bought, drawn as such, and its ordinariness is the point.**
>
> **No text in this panel.**
>
> ### Panel 2 — **DOMINANT, roughly 65% of the page**, the great central block
>
> **A child's hand and a woman's hand coming apart. That is the entire image.**
> Two hands and two wrists, very large in frame, filling the panel: the adult hand
> above and to the left, the child's hand below and to the right, fingers already
> separated, **the space between them opening** — a few inches of empty bleached
> air that is the subject of the panel and the subject of the page. Both wrists are
> covered by plain sleeves, both hands are unmarked, and **neither hand is being
> held, gripped, pulled or restrained by anyone else — there is no third hand in
> the frame.**
>
> **Nothing else is identifiable.** No faces, no bodies, no figures, no crowd, no
> platform, no chains, no background detail worth naming — only heat-glare, dust
> and indigo shadow behind the two hands, thrown out of focus by distance and light
> rather than by any photographic lens effect.
>
> **No text in this panel.**
>
> ### Panel 3 — roughly 15% of the page, a wide band across the bottom
>
> **Seen from directly above, straight down:** a plain wooden table in the shade,
> **an open ledger**, a **stick of dark red sealing wax and a finished red seal**,
> and **coins being counted into short stacks** by two pairs of hands at the frame's
> edges. Wrists and cuffs only, no faces, no bodies. Businesslike, unhurried,
> clerical.
>
> **The ledger's writing renders as marks and not as legible words** — ink texture
> only, unreadable at any magnification, no numbers a reader can total, no name a
> reader can read.
>
> One matte **sun-bleached ochre** parchment caption rectangle, tail-free, laid on
> the plain table surface in a calm empty area, never over the ledger, the seal or
> the coins, exactly:
>
> `My mother died in the afternoon. I was eleven.`
>
> **Lettering:** exactly **1** string on this page, once, with exact spelling,
> punctuation and capitalization. Caption lettering **36–42 px** on the 1024 × 1536
> canvas, **never below 40 px**, matte sun-bleached ochre parchment, tail-free,
> internal padding **≥42 px**, upright mixed-case literary serif, and **no essential
> text below 72 px from the bottom edge of the page**. **No italics, no all-caps
> prose, no condensed display faces.** This is a spectacle page and text occupies
> well under 15% of visual attention. **No speech balloons, no speaking characters,
> no second caption, no signage, no shop lettering, no legible writing in the
> ledger, no pseudo-text, no page number, no title.** Comfortably readable at 600 ×
> 900.
>
> **Continuity and meaning:** an ordinary square where things are bought → two hands
> letting go → a ledger, a seal and coins counted. The seal in panel 3 is the same
> dark red wax as the seal on the document Haydée put on the table on page 18, and
> the reader is meant to make that connection without being told. **The page must be
> devastating by omission, not by depiction.**
>
> No nudity, chains, restraint, violence, crowd reaction, visible face, named
> identity, lamp, candle, Paris interior, fire, lake, fortress, identity collision,
> duplicated hand, third hand, fused fingers, illegible caption text, crop sheet, or
> outer frame.
>
> ## Reference images
> 1. `refs/approved/09-janina-1822.png` — binds the adult hand and the child's hand
>    at the moment of coming apart, clothed and unrestrained.
> 2. `refs/approved/20-set-janina.png` — binds the dusty bleached market square, the
>    heat-glare and the indigo shadow.
> 3. `pages/page-20.png` — promoted previous page; binds the southern light and the
>    palette of this world.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 22 — *dramatic*

**Turn:** she refuses to hand the proof over as evidence and keeps the right to
speak it herself.
**Dominant:** both their hands on the document — 52%.
**Locations:** 1. **Panels:** 3.
**Output:** `qa/production/page-22/candidates/page-22-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 22
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile heavy laid paper, red sealing wax,
> brass, lamp glass, black lacquered wood and crimson embroidery, selective hard
> edges at the document, the seal, the hands and the two faces. **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> engraved cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, unpolished new gold**, one warm pool of oil-lamp
> light on the table with everything outside it going to black, and **one
> restrained note of deep crimson and gold** on Haydée. The red wax seal is the
> hottest colour on the page.
>
> **Predecessor: attach the promoted page 18.** This page is **continuous from page
> 18** — the same evening, the same small table, the same two chairs, the same
> single brass oil lamp, the same clothes on both people, and **the same document
> lying exactly where it was left**, same size, same fold pattern, same broken red
> wax seal, same ink layout. Pages 19 to 21 were Haydée's account and took no time
> in this room. **Do not show** Mercédès, Fernand, Albert, Danglars, Villefort,
> Beauchamp, any servant, any clerk, any Janina, any daylight. **Two people on this
> page and no others.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with first grey at the temples, deep-set black-brown eyes, strong straight brow,
> long clean nose, high cheekbones, **slight asymmetry at the left corner of the
> mouth**, cultivated pallor, **unrelieved black**. Never a heavy moustache, never a
> thickened soldier's build, never chestnut hair or a light waistcoat.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build, direct
> unornamented stillness, **crimson-and-gold Epirote dress, loose vertical
> silhouette — never a French 1838 waist, never a sculpted French coiffure, never a
> forty-year-old face.** She is twenty-seven and eleven years old in the memory
> three pages back; nothing here may age her into Mercédès.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Haydée holds the left of every panel, the Count
> the right**, exactly as on page 18. Every balloon sits on its owner's side.
>
> **Three panels only.** This page was split off a denser one precisely so that
> its dominant image can be large and its lettering can be set at full height.
> Reserve every balloon lane first and stage the two people into what is left. If
> the strings in panel 3 cannot be set at **44–50 px** inside the panel, **stop and
> return the page to the plan owner. Do not shrink the type, do not drop a word,
> and do not move a string to another panel.**
>
> ### Panel 1 — roughly 14% of the page, a narrow band across the top
>
> The lamp, the small table, the two of them back in the black room, framed wide and
> shallow. **The document still lying where it was.** **The Count's hand comes out
> over it from the right, flat, palm down, waiting** — not touching it.
>
> Two warm-ivory balloons, **wide and shallow**, each on its owner's side, the
> Count's on the **right** first, Haydée's reply on the **left**, exactly:
>
> `Give it to me.`
>
> `No.`
>
> ### Panel 2 — **DOMINANT, roughly 52% of the page**, the large central block
>
> Close on the table under the lamp: **Haydée's hands passing the document across to
> him — and holding the far edge, so that for one image both of them are holding
> it.** Four hands, one sheet of heavy paper, the broken red wax seal, the lamp. Her
> hands enter from the left, his from the right; the paper spans the space between
> them and is under tension, held at both ends. Both faces are in frame above the
> paper, small, looking at each other and not at it.
>
> **The writing on the document renders as marks and not as legible words** — ink
> texture only, unreadable at any magnification.
>
> Two warm-ivory balloons, **both Haydée's**, on the **left**, in descending order,
> tails to her mouth, never over the paper, exactly:
>
> `You will hold it.`
>
> `When it is read out in a room, I will be the one reading it.`
>
> ### Panel 3 — roughly 34% of the page, a wide block across the bottom
>
> **Two faces, level with each other and level with the frame**, close: Haydée on
> the **left**, the Count on the **right**, the lamp between and below them. **He is
> looking at her the way he looks at a problem he likes** — interested, amused,
> already working. Faces are pushed to the outer thirds of the block so that the
> centre and upper area of the panel are a clear lettering lane running its full
> width.
>
> Three warm-ivory balloons in strict descending order, each on its owner's side —
> Haydée's two on the **left**, the Count's reply on the **right** and lowest,
> exactly:
>
> `I have waited sixteen years.`
>
> `I will not stand at the back of a room while a Frenchman says my father's name for me.`
>
> `Then I shall have to build you a room to say it in.`
>
> **Lettering:** **7** balloon strings, exactly once each, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px**; the short reply `No.` at
> **48–54 px**; balloon widths **240–390 px**, except in panel 1's narrow band and
> for the long third string in panel 3, where a **wider, shallower balloon up to
> roughly 620 px across** is required so the lettering height is never compromised —
> **the lettering height governs, the balloon shape yields.** Warm ivory fill, never
> pure digital white, restrained charcoal-brown painted outline, upright mixed-case.
> **No italics, no condensed display faces, no all-caps.** Haydée owns five
> balloons, the Count owns two. No balloon and no tail crosses the document. No
> captions on this page. **The only writing rendered anywhere on this page is inside
> the seven balloons.** No quotation marks, speaker labels, page numbers, titles or
> pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** he asks for the receipt → she refuses to hand it over
> → for one image they are both holding it, which is the bargain → she keeps the
> right to say her father's name aloud in public, and he answers by promising her a
> room to say it in. **The both-hands-on-the-document image in the dominant panel is
> the page** — if it is not the largest and clearest thing here, the page has failed.
>
> No third figure, no servant, no clerk, no daylight, no window view, no second
> document, no fire, no clutter, no identity collision, duplicated person, duplicated
> hand or duplicated document, fused fingers, illegible text, crop sheet, or outer
> frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the black room, the small table and the
>    one lamp.
> 4. `refs/approved/21-objects.png` — binds the large folded document with the broken
>    red wax seal. **The handwriting on it is marks, not words.**
> 5. `pages/page-18.png` — the continuous predecessor scene; binds the table, the lamp,
>    the document's exact appearance and both characters' clothes.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 23 — *dramatic*

**Turn:** he names the room — and the mechanism that will walk Fernand into it.
**Dominant:** the Count with the document flat under the lamp, looking past it — 46%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-23/candidates/page-23-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 23
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile heavy laid paper, red sealing wax,
> brass, lamp glass, black lacquered wood and crimson embroidery, selective hard
> edges at the document, the seal, the hands and the two faces. **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> engraved cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, unpolished new gold**, one warm pool of oil-lamp
> light on the table with everything outside it going to black, and **one
> restrained note of deep crimson and gold** on Haydée. The red wax seal is the
> hottest colour on the page.
>
> **Predecessor: attach the promoted page 22.** This page is **continuous from page
> 22** — the same minute, the same table, the same lamp, the same two chairs, the
> same clothes, the same document. Nothing in the room has moved except the
> document, which is now **in the Count's hands** and no longer lying on the table.
> **Do not show** Mercédès, Fernand, Albert, Danglars, Villefort, Beauchamp, any
> servant, any clerk, any Janina, any daylight, any Chamber, any crowd. The room he
> is describing must **not** appear on this page — it is spoken, not shown. **Two
> people on this page and no others.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with first grey at the temples, deep-set black-brown eyes, strong straight brow,
> long clean nose, high cheekbones, **slight asymmetry at the left corner of the
> mouth**, cultivated pallor, **unrelieved black**. Never a heavy moustache, never a
> thickened soldier's build, never chestnut hair or a light waistcoat.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build, direct
> unornamented stillness, **crimson-and-gold Epirote dress, loose vertical
> silhouette — never a French 1838 waist, never a sculpted French coiffure, never a
> forty-year-old face.** She is twenty-seven and eleven years old in the memory
> three pages back; nothing here may age her into Mercédès.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Haydée holds the left of every panel, the Count
> the right**, exactly as on page 18. Every balloon sits on its owner's side.
>
> ### Panel 1 — roughly 14% of the page, a narrow band across the top
>
> Haydée on the **left**, close, **not letting go of the document** — her hand still
> on the near edge of it while it rests in his. Only her hand and face are needed.
> The right of the band is a clear lettering lane.
>
> One warm-ivory balloon on the **left**, tail to her mouth, exactly:
>
> `What room?`
>
> ### Panel 2 — **DOMINANT, roughly 46% of the page**, the large upper-middle block
>
> The Count with **the document held flat under the lamp, not reading it** — his
> eyes are past it and off into the middle distance, laying something out in his
> head. He is on the **right**, seated, the lamp lighting the paper from below and
> throwing his face upward into hard light and hard shadow. Haydée is on the
> **left**, in the near dark, watching him do it. **The document's writing renders
> as marks and not as legible words.** The figures occupy the lower two-thirds of
> the block; **the upper third is a reserved lettering lane running the full
> width.**
>
> Two warm-ivory balloons, **both the Count's**, on the **right**, in strict
> descending order, tails to his mouth, never crossing the document, exactly:
>
> `A public one. Three hundred men in it.`
>
> `And Mondego walking through the door on his own legs, because he demanded to be heard.`
>
> ### Panel 3 — roughly 20% of the page, a wide band beneath
>
> Haydée alone in frame, or nearly — **working it out and not liking how simple it
> is.** She is on the **left**, turned slightly toward him, the lamp edge-lighting
> one side of her face. Her figure sits in the left third; the centre and right of
> the band are a clear lettering lane.
>
> One warm-ivory balloon on the **left**, tail to her mouth, exactly:
>
> `How do you make a man demand that?`
>
> ### Panel 4 — roughly 20% of the page, a wide band across the bottom
>
> The Count, **pleased with it** — the small asymmetry at the left corner of his
> mouth doing the work, not a broad smile. He is on the **right**, the document
> lowered, the lamp under him. **This is appetite, not serenity: a man enjoying the
> shape of his own machine.** His figure sits in the right third; the left and
> centre of the band are a clear lettering lane.
>
> One warm-ivory balloon on the **right**, tail to his mouth, wide and shallow,
> exactly:
>
> `I don't. A stranger accuses him in print, and his vanity does the rest.`
>
> **Lettering:** **5** balloon strings, exactly once each, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px**; the short question `What
> room?` at **48–54 px**; balloon widths **240–390 px**, except for the two long
> strings in panels 2 and 4, where a **wider, shallower balloon up to roughly 620 px
> across** is required so the lettering height is never compromised — **the
> lettering height governs, the balloon shape yields.** Warm ivory fill, never pure
> digital white, restrained charcoal-brown painted outline, upright mixed-case. **No
> italics, no condensed display faces, no all-caps.** Haydée owns two balloons, the
> Count owns three. No balloon and no tail crosses the document. No captions on this
> page. **The only writing rendered anywhere on this page is inside the five
> balloons.** No quotation marks, speaker labels, page numbers, titles or
> pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** she asks what room → he describes a public one with
> three hundred men in it and Fernand walking in under his own power → she asks how
> you make a man demand that → and he answers with the mechanism: a stranger in
> print, and Fernand's vanity doing the rest. **Panel 2 is the page**, and its
> subject is a man who is not looking at the evidence in his hands because he is
> already looking at the room. **He must read hungry.** A serene, remote,
> above-it-all Count in panels 2 and 4 is a failed page.
>
> No third figure, no servant, no clerk, no daylight, no window view, no Chamber, no
> crowd, no newspaper, no second document, no fire, no clutter, no identity
> collision, duplicated person, duplicated hand or duplicated document, fused
> fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/17-set-count-house.png` — the black room, the small table and the
>    one lamp.
> 4. `refs/approved/21-objects.png` — binds the large folded document with the broken
>    red wax seal. **The handwriting on it is marks, not words.**
> 5. `pages/page-22.png` — promoted previous page, the same minute; binds the table,
>    the lamp, the document in his hands and both characters' clothes.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 24 — *dramatic*

**Turn:** the Count needles Danglars' vanity until Danglars decides, alone, to
write to Janina.
**Dominant:** Danglars writing; the Count behind him — 45%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-24/candidates/page-24-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 24
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile bottle-green baize, polished brass,
> ledger calf, cut glass, ink and gaslight, selective hard edges at the two faces,
> the letter-scale and the pen. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **bottle green baize, brass, ledger calf, gaslight, coin-yellow.**
> **Money rendered as furniture**, with mechanisms everywhere — a clock, a
> strongbox, a brass letter-scale, a wall of ledgers. **Brass is the accent: every
> object in the room that counts, weighs or locks.** The room is warm, hard and
> well-fed, and the Count's unrelieved black is the one thing in it that does not
> belong.
>
> **Predecessor:** page 23 was a black room in the Count's own house at night.
> **Do not attach page 23** — this is a different house on a different day and the
> palette must break. What carries: **the Count wears unrelieved black, as always.**
> **Do not show** Haydée, Mercédès, Fernand, Albert, Villefort, Beauchamp, any
> woman, any clerk, any servant. **Two people on this page and no others**, and the
> room's whole argument is that Danglars is comfortable in it.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters.
> **Baron Danglars, 55:** heavy fleshy face, small shrewd close-set eyes, thin
> mouth, high colour, thinning sandy-grey hair combed across, **full side whiskers
> and no moustache**, short and thickening, expensive clothes that fit badly, rings
> on the fingers. He must never be given a military moustache, an upright soldier's
> carriage, a chest of decorations, or a narrow pale rigid magistrate's face and
> high forehead.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with first grey at the temples, deep-set black-brown eyes, long clean nose, high
> cheekbones, **slight asymmetry at the left corner of the mouth**, cultivated
> pallor, **unrelieved black**. He is a head taller than Danglars and half his
> width, and that difference is visible in every panel they share.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Danglars holds the left of every panel, the
> Count the right.** Every balloon sits on its owner's side.
>
> ### Panel 1 — roughly 14% of the page, a wide band across the top
>
> Danglars **pouring** — a decanter and two glasses, expansive, mid-gesture, at
> home in his own room, on the **left**. The Count on the **right**, standing, not
> yet holding anything. Behind them the ledgers, the strongbox, the gaslight.
>
> Two warm-ivory balloons, **wide and shallow**, each on its owner's side. The
> Count's first, on the **right**; Danglars' reply on the **left**, exactly:
>
> `I am thinking of putting money behind Morcerf.`
>
> `The general? He's good for it.`
>
> ### Panel 2 — roughly 12% of the page, a narrow band beneath
>
> Closer: two heads, Danglars **left**, the Count **right**, the gaslight between
> them. Danglars is pleased to be consulted.
>
> Two warm-ivory balloons, **wide and shallow**, each on its owner's side, the
> Count's first on the **right**, exactly:
>
> `Is he? You would know. You have seen the ledgers.`
>
> `I've seen enough.`
>
> ### Panel 3 — roughly 17% of the page, a wide band beneath
>
> **The Count, pleasant and idle, on the right, looking at a polished brass
> letter-scale on the desk and not at Danglars** — turning its pan with one finger,
> entirely uninterested, the way a man handles an ornament while saying something
> he has planned. Danglars small on the **left**, watching him, beginning to be
> pricked. **Reserve the upper two-thirds of this band as a clear lettering lane**
> and stage both figures low in it.
>
> Two warm-ivory balloons, **both the Count's**, on the **right**, in descending
> order, tails to his mouth. Danglars is silent in this panel and receives no
> balloon. Exactly:
>
> `In Rome they would have written to wherever the money came from and made a nuisance of themselves for a month.`
>
> `Paris is a more trusting town.`
>
> ### Panel 4 — roughly 12% of the page, a narrow band beneath
>
> **Danglars' face**, close, on the **left**, pricked exactly where he was aimed
> at: not suspicious of the Count — offended on his own behalf. The Count's black
> shoulder at the **right** edge, face turned away.
>
> Two warm-ivory balloons, **wide and shallow**, each on its owner's side,
> Danglars' first on the **left**, exactly:
>
> `I am not a trusting man. The money came out of Greece.`
>
> `Then I suppose Greece would answer a letter.`
>
> ### Panel 5 — **DOMINANT, roughly 45% of the page**, the whole lower block
>
> **Danglars at his desk in the lit half of the room on the left, the pen already
> in the ink, writing** — bent over a fresh sheet, thoroughly pleased with himself,
> a man demonstrating his own prudence. Brass, baize, ledgers and gaslight around
> him. **The Count stands behind him in the dark half of the room on the right,
> turned toward the reader**, so that **the reader can see his face and Danglars
> cannot.** The face is doing exactly what it did at the window on page 2:
> **pleasure, appetite, a man watching a machine he built start up.** Not serenity.
>
> The letter is a **fresh clean sheet, unsealed, no broken seal, no red wax on it
> yet**, and **its writing renders as marks and not as legible words.**
>
> Three warm-ivory balloons in strict descending order, each on its owner's side —
> Danglars' two on the **left**, the Count's on the **right** and lowest, exactly:
>
> `I'll write it tonight, over my own name.`
>
> `Three weeks for an answer, and then we shall both know what the man is worth.`
>
> `You are very thorough, Baron.`
>
> **Lettering:** **11** balloon strings, exactly once each, in this order, with
> exact spelling, punctuation, capitalization and apostrophes. Balloon lettering
> **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**; short replies at
> **48–54 px**; balloon widths **240–390 px**, except in the narrow bands (panels 1,
> 2 and 4) where a **wider, shallower balloon up to roughly 620 px across and two
> lines deep** is required so the lettering height is never compromised — **the
> lettering height governs, the balloon shape yields.** Warm ivory fill, never pure
> digital white, restrained charcoal-brown painted outline, upright mixed-case. **No
> italics, no condensed display faces, no all-caps.** The Count owns six balloons,
> Danglars owns five. No captions on this page. **No legible writing anywhere in the
> room** — the ledger spines, the letter and any label are texture, not words. No
> quotation marks, speaker labels, page numbers, titles or pseudo-text. Comfortably
> readable at 600 × 900.
>
> **Reserve the balloon lanes before placing the figures.** Panels 3 and 4 carry
> more words than their height easily holds. If those strings cannot be set at
> **44–50 px** inside their panels, **stop and return the page to the plan owner. Do
> not shrink the type and do not drop a word.**
>
> **Continuity and meaning:** he offers Danglars the flattery of being consulted →
> Danglars claims to have seen the ledgers → the Count says, idly, that Paris is
> careless → Danglars' vanity supplies *Greece* by itself → and by the last panel
> Danglars is writing the letter, over his own name, believing it was his idea. **The
> Count never asks for the letter anywhere on this page and must never appear to.**
> This is the letter whose reply arrives on page 25 and reaches print on page 26.
>
> No third figure, no clerk on this page, no woman, no servant, no daylight, no
> Haydée's document, no broken red wax seal, no identity collision, duplicated person
> or hand, fused fingers, illegible balloon text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/06-danglars-1838.png` — Danglars, with side whiskers and no
>    moustache.
> 2. `refs/approved/01-count-1838.png` — the Count.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 25 — *dramatic*

**Turn:** the reply arrives and Danglars sells it to a newspaper without knowing
what it is.
**Dominant:** the letter crushed in his fist — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-25/candidates/page-25-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 25
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile bottle-green baize, polished brass,
> ledger calf, crumpled foreign paper and gaslight, selective hard edges at
> Danglars' face and at the crushed letter. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **bottle green baize, brass, ledger calf, gaslight, coin-yellow.** The
> same room as page 24, three weeks later. **The Count's black is absent from this
> page and the room is warmer for it** — this is the one scene in his mechanism that
> runs without him in the room.
>
> **Predecessor: attach the promoted page 24.** Same study, same desk, same
> ledgers, same strongbox, same brass letter-scale, same gaslight, same Danglars in
> the same kind of expensive badly fitting clothes. Three weeks have passed and
> nothing in the room has moved. **Do not show** the Count, Haydée, Mercédès,
> Fernand, Albert, Villefort, Beauchamp, or any woman. **Danglars and one anonymous
> clerk, and nobody else.**
>
> **Character locks.** One supplied canonical character reference binds the only
> named character.
> **Baron Danglars, 55:** heavy fleshy face, small shrewd close-set eyes, thin
> mouth, high colour, thinning sandy-grey hair combed across, **full side whiskers
> and no moustache**, short and thickening, expensive clothes that fit badly, rings.
> Never a military moustache, never an upright soldier's carriage, never a chest of
> decorations, never a narrow pale rigid face with a very high forehead.
>
> **The clerk is an anonymous figure and must stay anonymous.** A middle-aged man of
> about fifty in shabby brown, thin grey hair, no spectacles of any kind, plain
> collar, stooped over an inkstand and only half listening. **He must not be given
> small oval spectacles, untidy sandy hair, ink-stained fingers held up, chestnut
> hair, a pale waistcoat, youth, or an open mobile face** — he must not be
> confusable with either of the volume's two young men, and he is never seen in
> close-up. **His face is turned away or in shadow in every panel he appears in.**
>
> **Staging law for this page:** **Danglars holds the right of every panel; the
> clerk, where visible, is small and on the left.** Every balloon sits on Danglars'
> side. The clerk is silent on this entire page and receives no balloon and no tail
> fragment.
>
> ### Panel 1 — roughly 20% of the page, a wide band across the top
>
> **Danglars on his feet on the right, a foreign sheet held up at arm's length,
> reading it aloud** — chin up, enjoying being right. The clerk small on the
> **left**, half turned away at an inkstand, not really listening. The sheet is
> **visibly foreign**: different paper, different fold, a different hand from the
> letter he wrote on page 24, **and its writing renders as marks and not as legible
> words.**
>
> One warm-ivory balloon on the **right**, tail to Danglars' mouth, its lane
> reserved before the figures are placed, exactly — **including the single quotation
> marks at each end, which are part of the string because he is reading aloud**:
>
> `'The fortress of Janina was surrendered on the second of February, 1822, by the French officer Fernand Mondego, who was paid for it.'`
>
> ### Panel 2 — roughly 15% of the page, a wide band beneath
>
> **Danglars laughing, genuinely**, head back, on the **right** — a fat, delighted,
> entirely unmalicious laugh. The clerk is not in this panel.
>
> One warm-ivory balloon, **wide and shallow**, on the **right**, exactly:
>
> `He sold a castle.`
>
> ### Panel 3 — **DOMINANT, roughly 50% of the page**, the large lower-middle block
>
> **The letter crushed in his fist and held up**, large in frame, and his face
> behind and above it. **The face is the panel: not calculation — real, wounded
> indignation.** A man who has just found out that a friend of twenty-three years
> lied to him at his own table, and who is genuinely hurt, and who is entirely
> unaware that he himself put a man in a fortress in 1815. **He must not look
> cunning, scheming, or pleased here.** Gaslight hard on the crushed paper.
>
> One warm-ivory balloon on the **right**, tail to his mouth, exactly:
>
> `Twenty-three years at my table, telling me about Spain.`
>
> ### Panel 4 — roughly 15% of the page, a wide band across the bottom
>
> **The crushed letter, half smoothed out again, going into the clerk's hands** —
> two pairs of hands and a sheet of paper, Danglars' ringed hand on the **right**,
> the clerk's plain cuff on the **left**, the clerk's face turned away and in shadow.
>
> One warm-ivory balloon on the **right**, tail to Danglars' mouth, exactly:
>
> `Take it to the Impartial. Not from me — say it came from a friend of the house.`
>
> The word **Impartial** is set in the same upright mixed-case letterform as the rest
> of the balloon. **No italics, no underline, no quotation marks and no emphasis of
> any kind on it.**
>
> **Lettering:** **4** balloon strings, exactly once each, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. **The single quotation marks
> in the panel 1 string are part of that string and are rendered; no other quotation
> mark appears anywhere on this page.** Balloon lettering **44–50 px** on the 1024 ×
> 1536 canvas, **never below 40 px**; balloon widths **240–390 px**, except in the
> narrow bands where a **wider, shallower balloon up to roughly 620 px across** is
> required so the lettering height is never compromised — **the lettering height
> governs, the balloon shape yields.** Warm ivory fill, never pure digital white,
> restrained charcoal-brown painted outline, upright mixed-case. **No italics, no
> condensed display faces, no all-caps.** Danglars owns all four balloons; the clerk
> owns none and is silent. No captions on this page. **No legible writing on the
> foreign letter, on any ledger, or anywhere else in the room.** No speaker labels,
> page numbers, titles or pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** the answer he asked for has come → it says his friend
> sold a fortress → he laughs, and then he is genuinely wounded → and he hands it to
> a newspaper while hiding his own name. **The chain of paper must be visibly
> unbroken:** the clean sheet he wrote on page 24, this foreign reply, and the printed
> column on page 26 are one object becoming a public fact. **Danglars never connects
> any of this to himself, and nothing on this page may suggest that he does.**
>
> No Count, no black columnar figure, no woman, no third speaker, no legible document
> text, no identity collision, duplicated person or hand, fused fingers, illegible
> balloon text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/06-danglars-1838.png` — Danglars.
> 2. `pages/page-24.png` — promoted previous page; binds the study, the desk, the
>    brass, the gaslight and Danglars' clothes three weeks earlier.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 26 — *spectacle*

**Turn:** it is in print — read first by the man who caused it, then by the boy it
destroys.
**Dominant:** the opened paper and the paragraph — 65%.
**Locations:** 2. **Panels:** 3.
**Output:** `qa/production/page-26/candidates/page-26-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 26
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile cheap newsprint, black lacquered wood,
> lamp glass, porcelain, silver and starched linen, selective hard edges at the
> hands, the sheet of newsprint and the printed column. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> **This page carries two locations and the cut between them is the page.**
> Panels 1 and 2 are the Count's black room at dawn: **lacquer black, ivory, one
> small pool of lamp-yellow, and the first grey light in the tall windows.** Panel
> 3 is the Morcerf breakfast room an hour later: **burgundy, polished walnut, old
> gold, warm morning light, white linen.** The two palettes must be unmistakably
> different rooms in the same city on the same morning, and **the one object common
> to both is the same folded sheet of newsprint.**
>
> **Predecessor:** page 25 was Danglars' green-and-brass study. **Do not attach page
> 24** and do not carry its palette into this page. What carries is the object: the
> foreign letter Danglars sent to a newspaper has become **this printed edition**.
> **Do not show** Danglars, Haydée, Mercédès, Fernand, Villefort, Beauchamp, any
> clerk, any servant, or any crowd. **Two figures on this page, one per location,
> and they never share a panel.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters. **These two are the volume's highest collision risk and both
> appear on this page. All four separators are stated and all four must render.**
> **The Count, 42:** tall, columnar, clean-shaven, **swept-back black hair with the
> first grey at the temples**, deep-set black-brown eyes, long clean nose, high
> cheekbones, **slight asymmetry at the left corner of the mouth**, **cultivated
> pallor — the palest skin value in the volume**, **unrelieved black**, and forty-two
> years old with the lines of it. In panel 1 **the face is half out of frame** and
> the identity is carried by the hands, the black cuffs and the mouth.
> **Albert de Morcerf, 22:** **chestnut-brown hair — never raven black, never blue-
> black** — short with a neat side part; **fair-olive skin several values lighter
> than the Count's pallor is cold**; his mother's wide-set direct eyes and mouth on
> his father's jaw, softened and un-weathered; slim, upright, unmarked; **the
> volume's brightest costume values — a pale waistcoat and a coloured neckcloth,
> never unrelieved black**; clean-shaven, no side whiskers, no moustache. He is
> twenty-two and must read as twenty-two.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — roughly 20% of the page, a wide band across the top
>
> The Count's black room at dawn: **one small brass oil lamp with a glass chimney**
> still burning on the low black lacquered table, the tall windows going first grey.
> **The same edition, opened, held up in two long pale hands** — the black cuffs, the
> ivory paper, the black room. **He is not reading it; he has already read it.** His
> face is **half out of the top of the frame**: what the reader gets is the mouth and
> the jaw, and **the mouth is doing the thing it does — the slight asymmetry at the
> left corner pulled into open, unhidden pleasure.** Not serenity. This is a man
> enjoying his own work at six in the morning.
>
> One warm-ivory balloon, **wide and shallow**, in the black area to the right of the
> paper, tail to his mouth, never over the newsprint, exactly:
>
> `Nine hundred copies, and he has not had his breakfast yet.`
>
> ### Panel 2 — **DOMINANT, roughly 65% of the page**, the great central block
>
> **The paper opened flat and filling the entire frame**, seen from directly above at
> very close range, lying on black lacquered wood that shows only at the extreme
> edges. Cheap 1838 newsprint: soft grey paper, uneven inking, a hard fold crease
> running across it.
>
> **The sheet is rendered at extreme scale so that a single column is large enough to
> read comfortably.** One column — **the second column** — runs vertically and
> occupies **76–86% of the panel's width**; the columns on either side of it are cut
> off at the panel edges and render as **unreadable grey type texture with no
> discernible words**. **One short paragraph in that second column is fully legible
> and is the only readable text on the sheet.** Everything else on the page of
> newsprint — headings, rules, mastheads, adjoining paragraphs — is texture, not
> words.
>
> The legible paragraph is set as **newspaper type, not as a balloon and not on
> parchment**: dark ink on grey newsprint, upright mixed-case, justified as a printed
> column, exactly:
>
> `We are informed from Janina that the fortress was delivered to the enemy in 1822 by a French officer then in the Pasha's service, named FERNAND MONDEGO, and that he was paid for it. We are told this officer sits today in the Chamber of Peers.`
>
> **The two words FERNAND MONDEGO are capitalised exactly as written, and nothing
> else in the paragraph is capitalised beyond ordinary sentence case.** No masthead
> title, no headline, no dateline, no byline, no price, no other legible word appears
> anywhere on the sheet.
>
> ### Panel 3 — roughly 15% of the page, a wide band across the bottom
>
> **The Morcerf breakfast room an hour later** — burgundy, walnut, old gold, warm
> morning light, white linen. **A cup, a spoon and a tray pushed aside**, the meal
> abandoned. **Albert with the same paper flat on the table under both hands, reading
> it a second time**: chestnut hair, pale waistcoat, **still in the previous evening's
> clothes and not changed**, leaning over it on both arms. **The open face is closed
> for the first time in this volume** — not shouting, not weeping: shut. He is alone
> in the room.
>
> **No text in this panel.**
>
> **Lettering:** **2** strings on this page, exactly once each, in this order, with
> exact spelling, punctuation, capitalization and apostrophes: one speech balloon in
> panel 1 and one printed newspaper paragraph in panel 2. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px**; balloon width up to roughly
> **620 px** in that narrow band so the lettering height is never compromised — the
> lettering height governs, the balloon shape yields; warm ivory fill, restrained
> charcoal-brown painted outline, upright mixed-case. **The printed newspaper
> paragraph is the third text level and is lettered at 40–46 px, never below 40 px**,
> in an upright mixed-case printed serif, dark on grey. **No italics, no condensed
> display faces, no faux-aged or distressed letterforms, no cursive.** Every word of
> the printed paragraph must survive the transcription test at 600 × 900 — if it
> cannot be set that large in the column, **enlarge the sheet in frame further. Never
> shrink the type.** No quotation marks, speaker labels, page numbers, titles or
> pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** the man who caused it is holding the edition before the
> city is awake and enjoying it out loud → the paragraph itself, big enough that the
> reader reads exactly what Paris read → the boy at his breakfast reading it a second
> time. **The same physical newspaper appears in all three panels and must be the same
> object** — same fold, same crease, same column layout. Panel 1 rhymes deliberately
> with page 29's last panel, where the same lamp, the same two hands and another sheet
> of paper return.
>
> No second figure in any panel, no servant, no Danglars, no Fernand, no Mercédès, no
> crowd, no legible text on the sheet beyond the one paragraph, no headline, no
> masthead, no identity collision between the man in black and the young man in the
> pale waistcoat, duplicated person, duplicated hand or duplicated newspaper, fused
> fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count: hands, cuffs, mouth, pallor.
> 2. `refs/approved/04-albert.png` — Albert: chestnut hair, fair-olive skin, pale
>    waistcoat, twenty-two.
> 3. `refs/approved/17-set-count-house.png` — the black room, the low table, the one
>    lamp, the tall windows at dawn.
> 4. `refs/approved/18-set-morcerf-house.png` — the Morcerf house palette and the
>    breakfast room's warmth.
> 5. `refs/approved/21-objects.png` — binds the folded 1838 Paris newspaper: cheap
>    paper, dense grey columns, type as texture except where this page specifies
>    otherwise.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 27 — *dramatic*

**Turn:** offered a retraction, Albert refuses it and asks for the truth instead.
**Dominant:** Albert on his feet at the table — 46%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-27/candidates/page-27-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 27
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile bare deal board, printer's ink,
> newsprint, tallow, iron press furniture and worn wool, selective hard edges at
> the two faces, the spectacles and the hands on the table. **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> engraved cross-hatching, no children's-book softness.
>
> Palette: **ink black, newsprint grey, tallow, bare board.** **This is the only
> unluxurious room in Paris in this book** — no gilt, no burgundy, no polish, no
> candle amber, no lacquer. Cheap light from a high dirty window and one tallow
> dip, paper everywhere, a press and its furniture behind them. The room must read
> as poorer than every other room in the volume.
>
> **Predecessor: attach the promoted page 26.** Same morning, an hour or two later.
> What carries: **Albert is still in the previous evening's clothes, unchanged and
> now creased**, and he has not slept; **the same edition of the newspaper is on the
> table between them**, same fold, same crease. **Do not show** the Count, Haydée,
> Mercédès, Fernand, Danglars, Villefort, any woman, any servant. **Two people on
> this page and no others**; other printers may exist as far shapes at the back of
> the room only, with no faces and no balloons, or may be omitted entirely.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible characters. **These two are the volume's second-highest collision risk —
> the only two young men in the book — and all four separators are stated and all
> four must render.**
> **Albert de Morcerf, 22:** **chestnut-brown hair, never sandy and never raven
> black**, short with a neat side part; **no spectacles, ever**; fair-olive skin;
> **bright pale costume values — a pale waistcoat and a coloured neckcloth**, now
> creased from a night in them; **upright carriage**; his mother's wide-set direct
> eyes and mouth on his father's jaw, softened and un-weathered; clean-shaven, no
> side whiskers. Pale and furious and holding it in.
> **Beauchamp, 28:** tall, thin, **slightly stooped**; **untidy sandy-light brown
> hair, never chestnut**; **small oval spectacles — his primary identifying mark**;
> long face, ironic mouth, ink-stained fingers; **plain dark practical clothes,
> unfashionable and slightly worn — the dullest costume values on the page**. Calm
> throughout, and calm is not smugness.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for this page:** **Albert holds the left of every panel; Beauchamp
> holds the right.** Every balloon sits on its owner's side, and the difference in
> costume value between the left figure and the right figure is visible in every
> panel.
>
> ### Panel 1 — roughly 18% of the page, a wide band across the top
>
> A long bare press-room table, paper and proofs on it. **Albert on the left**,
> standing, pale and furious, still in last night's clothes. **Beauchamp on the
> right**, seated, stooped, spectacles on, ink on his fingers, entirely calm.
>
> Three warm-ivory balloons in strict descending order, each on its owner's side —
> Albert's on the **left**, Beauchamp's on the **right**, Albert's second on the
> **left** and lowest — exactly:
>
> `Beauchamp.`
>
> `I wondered which of us would knock first. Sit down before you say it.`
>
> `Retract it.`
>
> ### Panel 2 — roughly 18% of the page, a wide band beneath
>
> Closer across the table: two heads, Albert **left**, Beauchamp **right**, the
> newspaper flat on the board between them. **Reserve the upper two-thirds of this
> band as a clear lettering lane** and stage both figures low in it.
>
> Three warm-ivory balloons in strict descending order, each on its owner's side —
> Beauchamp's on the **right**, Albert's on the **left**, Beauchamp's second on the
> **right** and lowest — exactly:
>
> `I can't retract something I haven't checked.`
>
> `You printed it without checking it.`
>
> `I printed that a letter exists. It does. I have held it.`
>
> ### Panel 3 — roughly 18% of the page, a wide band beneath
>
> **Beauchamp taking his small oval spectacles off** — the only concession he makes
> on this page — holding them in his ink-stained fingers, looking up at Albert with
> the naked, slightly weaker eyes of a man who takes his glasses off to say something
> kind. He is on the **right**. **This is the one panel where his primary identifying
> mark is off his face: the untidy sandy hair, the stoop, and the plain dark worn
> clothes must carry the identification alone, and the spectacles must be visible in
> his hand.** Albert on the **left**, listening, not moving.
>
> Two warm-ivory balloons, **both Beauchamp's**, on the **right**, in descending
> order, tails to his mouth. Albert is silent in this panel and receives no balloon.
> Exactly:
>
> `I'll withdraw it. Tomorrow, front page, over my own name.`
>
> `Say the word and it's done and we never speak of it again.`
>
> ### Panel 4 — **DOMINANT, roughly 46% of the page**, the whole lower block
>
> **Albert on his feet, both hands flat on the table**, leaning on them, on the
> **left** and large in frame; Beauchamp still seated on the **right**, spectacles in
> his hand, looking up at him. **This is the longest beat of Albert's life and the
> panel is built to hold it**: the room around them cheap and grey, the newspaper
> under his hands, a lot of quiet air above the figures. He is not shouting. He is
> deciding, and then he decides.
>
> Five warm-ivory balloons in strict descending order, each on its owner's side —
> Albert's first three on the **left**, Beauchamp's on the **right**, Albert's last on
> the **left** and lowest — exactly:
>
> `No.`
>
> `A withdrawal is you saying you were careless. It isn't you saying he didn't do it.`
>
> `Go and find out.`
>
> `You may not like what I bring back.`
>
> `I'll like it better than a favour.`
>
> **Lettering:** **13** balloon strings, exactly once each, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering **44–50
> px** on the 1024 × 1536 canvas, **never below 40 px**; short strings such as
> `Beauchamp.`, `Retract it.`, `No.` and `Go and find out.` at **48–54 px**; balloon
> widths **240–390 px**, except in the narrow bands where a **wider, shallower
> balloon up to roughly 620 px across** is required so the lettering height is never
> compromised — **the lettering height governs, the balloon shape yields.** Warm ivory
> fill, never pure digital white, restrained charcoal-brown painted outline, upright
> mixed-case. **No italics, no condensed display faces, no all-caps.** Albert owns
> seven balloons, Beauchamp owns six. No captions on this page. **No legible printed
> words on the newspaper, the proofs, or anywhere in the room** — all of it is type
> texture. No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable at 600 × 900.
>
> **Reserve the balloon lanes before placing the figures.** Panels 2 and 3 carry more
> words than their height easily holds. If those strings cannot be set at **44–50 px**
> inside their panels, **stop and return the page to the plan owner. Do not shrink the
> type and do not drop a word.**
>
> **Continuity and meaning:** he comes to demand a retraction → Beauchamp will not
> retract what he has not checked, and says he has held the letter → Beauchamp offers,
> as a friend, to withdraw it over his own name and end it → and Albert refuses the way
> out and asks for the truth instead. **He had it in his hand and gave it back**, and
> the panel where he does it is the largest on the page. **Beauchamp is decent here and
> must look decent** — the offer is genuine, not a trap, and his decency is what kills
> Fernand three pages later.
>
> No third named figure, no woman, no gilt, no luxury, no warm amber, no identity
> collision between the young man in the pale waistcoat and the young man in the small
> oval spectacles, duplicated person or hand, fused fingers, illegible text, crop
> sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/04-albert.png` — Albert: chestnut hair, pale waistcoat, upright,
>    no spectacles.
> 2. `refs/approved/07-beauchamp.png` — Beauchamp: sandy untidy hair, small oval
>    spectacles, stooped, plain worn dark clothes.
> 3. `pages/page-26.png` — promoted previous page; binds Albert's unchanged clothes and
>    the same edition of the newspaper.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

---

## PAGE 28 — *dramatic*

**Turn:** Fernand demands his wife defend him and learns she has known since 1815.
**Dominant:** the full length of the room between them — 55%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-28/candidates/page-28-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 28
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile polished walnut, gilt frames, silk
> wall-covering, wax, carpet pile and crumpled newsprint, selective hard edges
> only at the two faces and at the newspaper in the man's fist. **Not smooth
> prestige-oil realism.** No glossy concept-art surfaces, no airbrushed skin, no
> engraved cross-hatching, no children's-book softness.
>
> Palette: **burgundy, polished walnut, wax red, old gold** — but lit by **flat
> grey daylight from tall windows, with no candle amber anywhere.** This is the
> overstuffed house of purchased legitimacy seen in daylight with the guests
> gone, and the daylight is showing it: too many portraits, too much gilt, dust
> in the light. Wax red does the accent work — the seals and ribbons on the desk.
>
> **Predecessor:** the previous page is a different room and a hard cut; **do not
> attach it and do not carry its ink-and-bare-board palette in.** What carries in
> is the object: **the same cheap grey 1838 Paris newspaper** that has been
> passing from hand to hand, now crushed in Fernand's fist. Daylight, guests
> gone, no party. **Do not show** Albert, Beauchamp, the Count, Haydée, Danglars,
> Villefort, any servant, any guest, or any crowd. **Two human beings on this
> page and no other.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, heavy black brows
> set low and close, deep-set close dark eyes, weathered ruddy-olive Catalan skin
> coarser than any other face in this book, **heavy iron-and-black military
> moustache**, black hair **receding at the temples** and iron-grey at the sides,
> thick neck, heavy upright soldier's build. Indoors at home in daylight: dark
> coat, **no decorations on his chest on this page.**
> **Mercédès, Comtesse de Morcerf, 42:** decisive dark eyes, straight nose, lean
> mature cheeks, **visible lower-lid lines and temple lines**, restrained grey
> threads at the temple, dark hair sculpted into a formal 1838 Paris coiffure,
> burgundy-black vertical day gown, still upright carriage. She is **forty-two
> and must be visibly forty-two — a smoothed, beautiful, youth-washed face is a
> defect on this page.**
>
> Fernand must never be given the clean-shaven pallor, full swept-back black wave
> or columnar slimness of the black-clad man of forty-two who is not on this page;
> the moustache and the receding hairline are load-bearing. Mercédès must never be
> given long unbound black hair, gold eastern embroidery, or a late-twenties face.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for the whole page: Fernand is on the LEFT in every panel and
> Mercédès is on the RIGHT in every panel.** They never swap sides. Every balloon
> sits on its own speaker's side of the panel. Do not rely on tails to carry
> attribution.
>
> ### Panel 1 — roughly 13% of the page, a **wide band across the top**
>
> The long drawing room end to end. **Fernand at the far left end**, the newspaper
> crushed in one fist at his side. **Mercédès at the far right end, standing**,
> hands empty, not moving. The whole furnished length of the room between them.
>
> Two warm-ivory balloons in the clear upper air of the band, each on its owner's
> side. Left, Fernand's:
>
> `You've read it.`
>
> Right, hers:
>
> `Yes.`
>
> ### Panel 2 — roughly 9%, a **narrow wide band** directly under panel 1
>
> Tighter: only the two heads, one at the extreme left edge and one at the extreme
> right edge, facing each other across the band, the room compressed between them.
>
> Two warm-ivory balloons, one on each side, in the empty centre air. Left, his:
>
> `And?`
>
> Right, hers:
>
> `And what, Fernand?`
>
> ### Panel 3 — roughly 18%, a **wide band**
>
> Fernand crossing half the room toward her, left to right, mid-stride, one arm
> out — **loud, because loud has always worked in this house.** She is at the right
> edge and has not moved. **Reserve the upper two-thirds of this band as a clear
> balloon lane before placing the figure**, and keep him low and small in the
> lower third so the lane stays empty.
>
> Two warm-ivory balloons, **both his, both in the left and centre of the lane**,
> the first above the second, exactly:
>
> `Say it's a lie. That's all I want.`
>
> `Say it out loud in this room and I'll carry it down to the Chamber in my mouth.`
>
> ### Panel 4 — **DOMINANT, roughly 55% of the page**, the large lower block
>
> The full length of the room between them, wide, deep and cold: **Fernand small
> at the left, Mercédès small at the right**, and everything purchased in the
> space between — the gilt, the ranked portraits, the desk with its **wax-red
> seals**. She has not moved and is not going to. **Fernand is silent in this
> panel and receives no balloon.** Keep the upper right quadrant of the panel as
> calm wall and empty air.
>
> Two warm-ivory balloons, **both hers, both stacked in the upper right**, exactly:
>
> `I have never asked you one question about anything you have ever done. Not once, in twenty-three years.`
>
> `Did you never wonder why?`
>
> ### Panel 5 — roughly 5%, a **very narrow strip across the very bottom**
>
> Fernand's face alone, cropped close, filling the strip — working it out. **No
> text of any kind in this strip.** No balloon, no caption, no sound word.
>
> **Lettering:** all **8** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes. Balloon lettering
> **44–50 px** on the 1024 × 1536 canvas, **never below 40 px** for any character;
> balloons **240–390 px** wide; warm ivory fill, never pure digital white, with a
> restrained charcoal-brown painted outline; upright mixed-case. **No italics, no
> condensed display faces, no all-caps.** **Fernand owns four balloons** (panels 1,
> 2, and both in panel 3) and **Mercédès owns four** (panels 1, 2, and both in
> panel 4). Every balloon sits on its owner's side of its panel. No captions and
> no prose fields on this page. No quotation marks, speaker labels, page numbers,
> titles or pseudo-text, and **no readable words on the newspaper in his fist** —
> its type is texture only. Comfortably readable when the page is reduced to
> 600 × 900.
>
> **Continuity and meaning:** she has read it → he asks and she will not perform →
> he crosses the room and demands the lie out loud → she answers with twenty-three
> years of deliberate silence → he understands what her silence was. The newspaper
> in his fist is the same edition read on page 26. The room is the same room the
> party filled on page 6, now empty and lit wrong.
>
> No third figure, no servant, no guest, no candle amber, no decorations on
> Fernand's chest, no crowd, no identity collision, duplicated person or hand,
> fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/03-fernand-1838.png` — Fernand.
> 2. `refs/approved/02-mercedes-1838.png` — Mercédès.
> 3. `refs/approved/18-set-morcerf-house.png` — the room, the walnut, the gilt,
>    the portraits.
> 4. `refs/approved/21-objects.png` — the folded 1838 newspaper, type as texture.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 29 — *illustrated prose*

**Turn:** Beauchamp verifies it — and the man who aimed him is holding the result.
**Dominant:** Beauchamp in a Janina street — 55%.
**Locations:** 2. **Panels:** 3.
**Output:** `qa/production/page-29/candidates/page-29-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 29
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile whitewashed limestone, dry dust,
> worn wool coat cloth, a paper notebook, an old hand's skin, and — in the last
> panel — lacquered wood, lamp brass and damp newsprint. Selective hard edges at
> faces, hands and the sheet of paper. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette, and it changes once on this page: panels 1 and 2 are **Janina, 1838 —
> white limestone, cypress black, Ionian blue, sun-bleached ochre, hard high
> southern sunlight, and a sky.** Horizontal, bleached, hot, open. **This must not
> look like Paris.** Panel 3 is **Paris — lacquer black, ivory, cold grey, one
> small warm lamp**, vertical, interior, airless. The collision of the two
> palettes on one page is the point and must be obvious at a glance.
>
> **Predecessor:** the previous page is a different room, a different country and
> a hard cut; **do not attach it.** What carries in is the register and the
> printed edition. This is Janina **sixteen years after the fire and unburned** —
> the same white limestone and the same hard light the reader saw burning
> earlier, now standing, quiet and ordinary. **No fire anywhere on this page.**
> **Do not show** Albert, Mercédès, Fernand, Haydée, Danglars, Villefort, any
> soldier, any woman, any crowd scene, and **no face at all in panel 3.**
>
> **Character locks.** One supplied canonical character reference binds the only
> named visible character.
> **Beauchamp, 28:** tall, thin, **slightly stooped**, **sandy-light brown untidy
> hair**, **small oval spectacles — present and clearly readable against the
> temple in every panel he appears in**, long face, ironic mouth, ink-stained
> fingers, **plain dark practical Paris coat, unfashionable and slightly worn** —
> absurd and out of place under a southern sun, and sweating in it. He must never
> be given neat chestnut hair, a pale bright waistcoat, an upright unmarked
> posture, or a face without spectacles; that belongs to the young gentleman of
> twenty-two who is not on this page.
>
> **The old man in panel 2 is unnamed and has no reference sheet.** Build him
> fresh: **a Greek man of about seventy**, weathered dark-brown skin, deep
> creases, white stubble, a plain undyed shirt and a worn dark sash, no
> spectacles, no uniform, no decorations. He must not resemble any other man in
> this book and must not carry any of these combinations: unrelieved black
> columnar evening dress with swept-back hair; a heavy iron-black military
> moustache with receding temples; small oval spectacles with untidy sandy hair;
> loose raven curls with an open white shirt and a red-brown sash.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — **DOMINANT, roughly 55% of the page**, the large upper block
>
> A street in Janina under hard white light: whitewashed limestone walls, black
> cypress, a strip of Ionian blue water or sky at the top, deep indigo shadow cut
> hard against the glare. **Beauchamp stands in the middle of it in his Paris
> coat with a notebook open in one hand**, plainly foreign and plainly
> uncomfortable. Three or four local men are in the street going about their own
> business and **none of them is looking at him** — no crowd, no confrontation, no
> hostility, just indifference. He is small enough in the frame that the town
> reads as a real place.
>
> One matte parchment prose field, **sun-bleached ochre**, placed **across the
> upper area of this panel against flat sunlit wall — never over a face, never
> over the notebook, never over the figure.** Exactly this text, in two
> paragraphs:
>
> `Beauchamp was in Janina eleven days and enjoyed none of them. He found the register of the surrender. He found the clerk who had counted the money out, and two men old enough to have stood on the walls, and every one of them told him the same thing.`
>
> `Not one of them had ever been asked before, because in sixteen years nobody had ever come.`
>
> ### Panel 2 — roughly 30%, a **wide band** beneath panel 1
>
> Very close: **the old man's face at the left, large**, and **his hand closed
> hard on the sleeve of Beauchamp's dark coat** in the lower centre. Beauchamp at
> the right, half-turned, caught. Same hard sunlight. This is the only moment in
> this part of the book where somebody wants something from Beauchamp, and the
> hand on the cloth must carry it.
>
> One matte parchment prose field, sun-bleached ochre, **narrow, along the top
> edge of this band against plain sunlit wall**, exactly:
>
> `On the last day one of them took hold of his sleeve and would not let go.`
>
> Then three warm-ivory balloons, **the old man's on the LEFT on his own side,
> Beauchamp's on the RIGHT on his**, in this reading order — old man's first, high
> left; Beauchamp's second, right; the old man's third, lower left:
>
> `What will you do with it?`
>
> `Print it.`
>
> `Has the officer got a son?`
>
> ### Panel 3 — roughly 15%, a **wide band across the bottom**
>
> Paris. **The Count's black room, one small lamp, everything else lacquer
> black.** In frame: **two long pale hands only, holding an opened printed
> newspaper instalment, still damp**, and the corner of a low black table with the
> lamp on it. **The face is entirely out of frame — do not show it.** No other
> figure. The composition deliberately rhymes an earlier page: the same lamp, the
> same two hands, the same paper.
>
> One warm-ivory balloon, upper area of the band in the black air away from the
> hands, short tail running down toward the out-of-frame head, exactly:
>
> `Eleven days, and he never once wondered who sent him.`
>
> The word **JANINA** may appear once as a headline on the newspaper as **coarse
> printed newspaper display type, part of the art**, no larger than the balloon
> lettering; **every other word on that sheet is grey texture and must not be
> legible.**
>
> **Lettering:** all **7** text blocks exactly once — **2 prose fields carrying 3
> paragraphs in total, and 4 balloons** — with exact spelling, order, punctuation, capitalization and
> apostrophes. Prose fields: **36–42 px** lettering, never below **40 px** for any
> character; **38–52 characters per line**; field width **78–88% of canvas**;
> internal padding **≥42 px**; left-aligned with a calm ragged right edge; upright
> mixed-case literary serif. Balloons: **44–50 px**, never below **40 px**,
> **240–390 px** wide, warm ivory with a restrained charcoal-brown painted
> outline, upright mixed-case. **No italics, no all-caps prose, no condensed
> display faces.** **The old man owns two balloons, Beauchamp owns one, and the
> unseen speaker in panel 3 owns one; Beauchamp speaks only once on this page.**
> No quotation marks, speaker labels, page numbers, titles, signatures or
> pseudo-text. Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** eleven days of honest work in a town nobody ever
> came to → an old man who wants to know what it will cost → he answers *print
> it* and does not answer the question about the son → and the result is already
> in the hands of the man who aimed him. The Janina of panels 1 and 2 is the same
> place the reader watched burn in 1822, standing and unburned; the black room of
> panel 3 is the same room, lamp and hands as page 26's first panel.
>
> No fire, no burning fortress, no soldiers, no weapons, no crowd, no face in
> panel 3, no Paris architecture in panels 1 and 2, no sky in panel 3, no identity
> collision, duplicated person or hand, fused fingers, illegible essential text,
> crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/07-beauchamp.png` — Beauchamp, the stoop, the spectacles, and
>    the same Paris coat under hard southern sun.
> 2. `refs/approved/20-set-janina.png` — Janina: white limestone, cypress, Ionian
>    blue, the hard light.
> 3. `refs/approved/17-set-count-house.png` — panel 3's black room, low table and
>    lamp.
> 4. `refs/approved/21-objects.png` — the newspaper, its type rendered as texture.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 30 — *dramatic*

**Turn:** the Count arms Haydée, sends her through the front door, and takes the public stair himself.
**Dominant:** the case passing back into her hands — 45%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-30/candidates/page-30-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 30
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile cut stone, carriage lacquer, buttoned
> leather, wool broadcloth, gold thread and old handled paper, selective hard
> edges at the two faces, the hands and the flat case. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **cold pale morning daylight on grey public stone**, lacquer black
> carriage and black coat, and **one deep crimson-and-gold note on the woman —
> the only colour on the page.** The building is heavy, symmetrical and official.
> This is the outside of the volume's largest room and it must be built so that
> the same building is recognisable from inside on the next page.
>
> **Predecessor:** the previous page is a different country and a hard cut; **do
> not attach it.** What carries in is the printed campaign — eight days of it —
> and **the flat leather case**, last seen in the Count's keeping. Morning, cold,
> dry, public street. **Do not show** Albert, Mercédès, Fernand, Beauchamp,
> Danglars, Villefort, the interior of the Chamber, any bench, any speaking crowd,
> or any woman other than Haydée.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, deep-set black-brown eyes, strong straight
> brow, long clean nose, high cheekbones, **a slight asymmetry at the left corner
> of the mouth**, cultivated pallor, **unrelieved black** — black coat, black
> stock, white linen only at throat and cuff. **He is enjoying this and it is on
> his face: not serene, not grave, not above it.**
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build, direct
> unornamented stillness, **crimson-and-gold Epirote embroidery on a loose
> vertical silhouette — never a French 1838 waist, never a French coiffure, never
> a bonnet.**
>
> Haydée must never be given a sculpted formal French coiffure, a fitted
> burgundy-black gown, or the face of a woman of forty-two; the comtesse she must
> not resemble is not on this page. The Count must never be given a heavy military
> moustache, receding temples or a thickened build.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — roughly 10% of the page, a **wide band across the top**
>
> Exterior, establishing, and it must do real work: **the Chamber of Peers seen
> down a narrow side street** — a heavy classical façade with **columns and a
> great flight of front steps**, small black-coated men going up them, and **a
> narrow secondary public stair at the flank of the building**, plainly a lesser
> entrance. **A stopped black carriage small in the near foreground with its
> blinds half down.** Cold morning light. No figures large enough to identify.
>
> One matte parchment caption rectangle, tail-free, **upper left, set against
> plain sky or plain stone — never over the building's detail and never over the
> carriage**, exactly:
>
> `Beauchamp printed for eight days. Then the Chamber of Peers agreed to hear the Comte de Morcerf.`
>
> ### Panel 2 — roughly 11%, a **wide band** under panel 1
>
> Interior of that same carriage, close and dim. **Haydée on the LEFT seat in
> crimson and gold. The Count on the RIGHT seat in black, the flat leather case
> lying across his knee.** Both seated, facing each other.
>
> Two warm-ivory balloons, each on its owner's side. Left, hers:
>
> `How long will they let him talk?`
>
> Right, his:
>
> `As long as he likes. That is what the room is for.`
>
> ### Panel 3 — **DOMINANT, roughly 45% of the page**, the large middle block
>
> Inside the carriage. **The flat leather case going across the space between
> them into her hands — and for this one image both of them are holding it at
> once**, his hands still on one edge, hers already closed on the other. Haydée
> LEFT, the Count RIGHT, as in panel 2. He is unhurried and enjoying the telling;
> she is the only person alive he can show this to. **Stage the two figures low
> and to the outside of the panel, with the case at the centre, and reserve the
> entire upper half of this panel as clear dim carriage interior for balloons
> before placing any face.**
>
> Five warm-ivory balloons. **Hers is first and sits on the LEFT. His four follow
> down the RIGHT side in a single reading column, top to bottom.** In this exact
> reading order:
>
> `They will not let me through that door.`
>
> `A petition went last night to the President of the Chamber, in your name.`
>
> `It was carried by a lawyer who has never heard of me.`
>
> `He read it at breakfast. He believes it was his own idea.`
>
> `You carry it in. Nobody carries it for you.`
>
> ### Panel 4 — roughly 22%, a **wide band**
>
> **Haydée's face very close**, filling the left two-thirds of the band. She has
> just understood something about him. **She is not frightened by it — she is
> interested.** A sliver of the Count at the right edge, mostly in shadow.
> **Reserve the right third and the top of this band as a clear balloon lane.**
>
> Four warm-ivory balloons, **hers on the LEFT, his on the RIGHT**, alternating in
> this exact reading order:
>
> `You could have put this in a newspaper in April.`
>
> `Yes.`
>
> `You waited so that he could stand up in front of three hundred men first.`
>
> `I waited so that he could think he had won.`
>
> ### Panel 5 — roughly 12%, a **wide low band across the bottom**
>
> Exterior again, **from behind, both figures small**: two people separating on
> the pavement outside the same building. **She is on the LEFT, already climbing
> the great front steps toward the main door, the flat case under her arm.** **He
> is on the RIGHT, turned the other way toward the narrow public stair at the
> flank of the building.** They are walking apart. **He must not be shown entering
> the front door or standing on the front steps.**
>
> Two warm-ivory balloons, each on its owner's side. Left, hers:
>
> `You are enjoying this more than I am.`
>
> Right, his:
>
> `Go inside, Haydée.`
>
> **Lettering:** all **14** text blocks exactly once — **1 caption and 13
> balloons** — in this order, with exact spelling, punctuation, capitalization and
> accents, including the accent in `Haydée`. Balloon lettering **44–50 px** on the
> 1024 × 1536 canvas, **never below 40 px** for any character; balloons
> **240–390 px** wide; warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. Caption: matte parchment rectangle, **36–42 px**,
> never below **40 px**, tail-free. **No italics, no condensed display faces, no
> all-caps.** **The Count owns eight balloons and Haydée owns five**; every balloon
> sits on its owner's side of its panel, and the two speakers never swap sides
> anywhere on the page. **This page is text-heavy: reserve every balloon lane
> before placing a single face, and never reduce lettering below 40 px to make
> text fit.** No quotation marks, speaker labels, page numbers, titles or
> pseudo-text; **no legible writing on the case or on any document.** Comfortably
> readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** the building that will process a man, seen from
> outside → the two of them waiting in a stopped carriage → the proof passing back
> into her hands, held by both of them for one image → she works out what he did
> with the timing and finds it interesting → she goes up the front steps and he
> goes up the side stair. The flat case is the same case that has held the sealed
> document since she produced it, and both of them holding it here deliberately
> repeats the night she gave it to him. **He never walks onto the floor of this
> building; from here on he is only ever above that room.**
>
> No third named figure, no interior of the Chamber, no benches, no Fernand, no
> weapon, no crowd close enough to read a face, no identity collision, duplicated
> person or hand, fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/05-haydee.png` — Haydée.
> 3. `refs/approved/19-set-chamber.png` — the exterior, the front steps and the
>    narrow public stair at the flank.
> 4. `refs/approved/21-objects.png` — the flat travelling case.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 31 — *dramatic*

**Turn:** Fernand demands to be heard by the Chamber, and begins to win — with the Count willing him on.
**Dominant:** Fernand standing at the bar — 45%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-31/candidates/page-31-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 31
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile crimson bench baize, waxed dark oak,
> heavy gilded plaster, brass rail, massed black broadcloth and enamelled
> decorations, selective hard edges at Fernand's face and hands and at the one
> black figure in the gallery. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **crimson benches, heavy gold, dark oak, and cold high daylight
> falling from above** through a high glazed ceiling or clerestory. The light
> comes down onto the floor from overhead and nothing here is warm. This is the
> volume's largest room and it must be built as **a mechanism: tiered,
> symmetrical, and made to process one man.**
>
> **Predecessor: attach the promoted page 30.** This is the inside of the building
> the reader just saw from the street, the same cold morning, minutes later. What
> carries: the same building, the same daylight, the same hour, and the same two
> people separated on the pavement — she has gone in at the front and he has gone
> up the side stair to the public gallery, which is where he is on this page.
> **Do not show** Haydée, Albert, Mercédès, Beauchamp, Villefort, any woman
> anywhere in the room, the flat case, or the sealed document. **Haydée has not
> entered yet and must not appear on this page in any panel.**
>
> **Character locks.** The 3 supplied canonical character references bind the
> named visible characters.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, heavy black brows
> set low and close, deep-set close dark eyes, weathered ruddy-olive Catalan skin,
> **heavy iron-and-black military moustache**, black hair **receding at the
> temples** and iron-grey at the sides, thick neck, heavy upright soldier's build.
> **He is wearing the full chest of decorations — orders, ribbons, wax-red seals
> and old gold, polished and displayed.** He is good at this and has been good at
> it for eleven years: **render him as a man winning a room, not as a man already
> condemned** — upright, warm, plausible, in command of the floor.
> **Baron Danglars, 55:** heavy fleshy face, small shrewd close-set eyes, thin
> mouth, high colour, thinning sandy-grey hair combed across, **full side whiskers
> and no moustache**, short and thickening, expensive clothes fitting badly, rings.
> Seen seated among the benches, untroubled.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, cultivated pallor, **unrelieved black**.
> Seen only high above the floor.
>
> Fernand must never be given the Count's clean-shaven pallor, full swept-back
> wave or columnar slimness; the moustache and the receding hairline are
> load-bearing and separate them at any scale. Danglars must never be given a
> military moustache or an upright soldier's carriage, and must never be given a
> narrow pale rigid magistrate's face.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — roughly 11% of the page, a **wide band across the top**
>
> The room from inside, **from high above and behind**: tiered crimson benches
> rising away in symmetrical banks, dark oak, gold, cold light from overhead,
> **roughly three hundred men seated in it**, and **one man alone standing at the
> bar** at the focus of every tier. He is small in this panel; the room is the
> subject. **No caption and no text of any kind in this panel** — the reader
> arrived with him and needs no label.
>
> ### Panel 2 — **DOMINANT, roughly 45% of the page**, the large upper-middle block
>
> **Fernand standing at the bar, full figure, seen from slightly below**,
> decorations across his chest, **both hands on the rail**. Behind and above him
> the crimson tiers fall away out of focus. He is speaking to the whole room and
> the room is listening. **Place him left of centre and reserve the upper right
> two-thirds of the panel as a clear balloon lane before placing the figure.**
>
> Three warm-ivory balloons, **all his, stacked down the RIGHT side in one reading
> column**, exactly:
>
> `I am accused by a newspaper of selling a fortress.`
>
> `In a war France did not fight. In a country none of you has seen.`
>
> `On the strength of a letter written in a language none of you reads.`
>
> ### Panel 3 — roughly 18%, a **wide band**
>
> **Faces on the benches, ranked and close**, leaning forward toward him —
> persuaded, warming, some nodding. **Among them Danglars**, unmistakable by the
> side whiskers and the fleshy face, **nodding along, entirely untroubled.**
> Fernand is not in this panel. **Danglars and every other man here is silent and
> receives no balloon.** **Keep the upper half of this band as calm dark oak
> panelling and empty air for the two balloons, and set the ranked faces along the
> lower half.**
>
> Two warm-ivory balloons, **both Fernand's, side by side across the top of the
> band, left one first**, with tails running off-panel toward the floor below.
> Exactly:
>
> `I have sat in this house eleven years. I was at Ligny.`
>
> `There is not a man here who has not had my hand on his shoulder.`
>
> ### Panel 4 — roughly 12%, a **wide band**
>
> Fernand turning at the bar, **opening both arms to the whole room** — and on the
> front bench **one peer already half out of his seat to answer him.** It is
> working, and the panel must show that it is working.
>
> One warm-ivory balloon, upper area, on Fernand's side, exactly:
>
> `I ask the man who wrote the paragraph to stand up and put a name to it.`
>
> ### Panel 5 — roughly 14%, a **wide band across the bottom**
>
> **High in the public gallery, alone at the rail: one black figure**, leaning
> slightly out over three hundred heads far below. The gallery woodwork and rail
> in the near ground, the crimson floor of the hall dropping away beneath.
> **He does not look worried. He looks hungry** — the appetite must be legible on
> the face at this scale, so bring the head large enough to read.
>
> One warm-ivory balloon, upper area beside his head, exactly:
>
> `Go on. Win it.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation and capitalization. Balloon lettering **44–50 px** on the
> 1024 × 1536 canvas, **never below 40 px** for any character; balloons
> **240–390 px** wide; warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps** — the last line is spoken under the noise of the room and is **not**
> to be shrunk, whispered, italicised or set in a special balloon shape; it is a
> normal balloon at normal size. **Fernand owns six balloons and the man in the
> gallery owns one. Danglars is silent, the peer half out of his seat is silent,
> and no man on the benches receives a balloon or a tail fragment.** Panel 1
> carries no text at all. No captions, no quotation marks, speaker labels, page
> numbers, titles or pseudo-text. Comfortably readable when the page is reduced to
> 600 × 900.
>
> **Continuity and meaning:** the room as a machine with one man in its focus →
> his defence, which is genuinely good → the benches coming over to him → he dares
> his accuser to show himself → and the man who built this is in the gallery
> willing him to win, because a better defence tastes better. Fernand wears every
> decoration here and is still wearing them three pages later in an empty hall.
>
> No woman anywhere in this room, no Haydée, no document, no case, no open door at
> the back of the hall, no torches, no candles, no warm light, no identity
> collision, duplicated person or hand, fused fingers, illegible text, crop sheet,
> or outer frame.
>
> ## Reference images
> 1. `refs/approved/03-fernand-1838.png` — Fernand and the decorations.
> 2. `refs/approved/06-danglars-1838.png` — Danglars on the benches.
> 3. `refs/approved/01-count-1838.png` — the figure in the gallery.
> 4. `refs/approved/19-set-chamber.png` — the interior from the floor and the view
>    from the public gallery.
> 5. `pages/page-30.png` — promoted previous page; binds the building, the hour
>    and the daylight.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 32 — *spectacle*

**Turn:** the door at the back of the hall opens.
**Dominant:** Haydée in the doorway, crimson — 70%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-32/candidates/page-32-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 32
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread. **This is the largest single image in the book and must be
> built as one.**
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile crimson bench baize, waxed dark oak,
> heavy gilded plaster, gold thread on wool, and old handled paper, selective hard
> edges at the standing woman and the door frame. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **crimson benches, heavy gold, dark oak, cold high daylight from
> above** — and the woman in the doorway in **deep crimson and gold**, so that her
> dress **rhymes with the crimson of the benches** and reads as belonging to this
> room. She is the only thing in the hall that is not French tailoring, and she is
> nevertheless the only thing in it that matches it.
>
> **Predecessor: attach the promoted page 31.** The same hall, the same cold
> overhead daylight, the same tiers, the same hour, seconds later. What carries:
> the exact architecture of the room, the crimson value of the benches, Fernand's
> position at the bar and his decorations. **Do not show** Albert, Mercédès,
> Beauchamp, Villefort, or any second woman. **Do not show the Count anywhere on
> this page** — no gallery figure, no black vertical, nothing at the rail.
>
> **Character locks.** The 2 supplied canonical character references bind the
> named visible characters.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build,
> **direct unornamented stillness — she does not arrange her face.** **Deep
> crimson-and-gold Epirote embroidery on a loose vertical silhouette, an open long
> coat over a straight underdress, no corsetry — never a French 1838 waist, never
> a French coiffure, never a bonnet, never a hat.** She is twenty-seven and must
> not read as a French comtesse of forty-two with a sculpted coiffure and a fitted
> burgundy-black gown.
> **Fernand Mondego, 46:** heavy iron-and-black military moustache, black hair
> receding at the temples, thick neck, heavy upright build, **the full chest of
> decorations**. He is **tiny at the far end of the hall** in this page and is
> identified by moustache mass, silhouette and the glint of the decorations, not
> by facial detail.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — roughly 30% of the page, a **wide band across the top**
>
> **Three hundred faces, all turned the same way at once**, at the sound of a
> door. Ranked heads and shoulders in massed black coats across the tiers, every
> one of them looking off to the same side of the frame. No speaker, no gesture,
> no standing figure. **Every man in this panel is silent and receives no
> balloon.** The unanimity of the turn is the entire content.
>
> ### Panel 2 — **DOMINANT, roughly 70% of the page**, the great lower block
>
> **The great door at the back of the hall standing open, and Haydée in it.** She
> is **small, alone, centred in the doorway, full figure**, the dark oak frame
> around her and cold daylight behind her, the **large folded document with its
> red wax seal** carried in one hand at her side. Between her and the far end of
> the hall, the whole tiered crimson room falls away in perspective — banks of
> benches, gold, massed black coats — and **at the far end, very small, Fernand at
> the bar, turned toward her.**
>
> Build the panel so that two things are true at once and legible without
> explanation: **her crimson and gold sit in the same colour family as the benches
> around her, so she looks as though the room was built for her — and Fernand, in
> black French tailoring at the far end, does not.**
>
> **This page has no balloons, no captions, no prose fields and no speaking
> characters.**
>
> **Lettering:** **this page carries no text of any kind. Zero strings.** Do not
> add a caption, a title, a date line, a sound word, a signature, a page number,
> or any lettering anywhere on the canvas. Any legible word on this page is a
> defect. The **handwriting on the sealed document must render as marks and not as
> readable words**, and the red wax seal must be clearly visible as a seal.
>
> **Continuity and meaning:** the room hears a door → the door is open and she is
> standing in it, alone, carrying the proof. The reader already knows who she is
> and knows that nobody in that hall does. She entered by the front steps two
> pages ago and she is carrying the case's contents in her own hands, as she was
> told: nobody carries it for her.
>
> No Count, no gallery figure, no black columnar man, no second woman, no soldier,
> no weapon, no crowd outside the door, no text, no identity collision, duplicated
> person or hand, fused fingers, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/05-haydee.png` — Haydée, and specifically the view of her
>    composed and about to walk into a room of three hundred men.
> 2. `refs/approved/03-fernand-1838.png` — Fernand at the far end, small.
> 3. `refs/approved/19-set-chamber.png` — the hall, the tiers and the door at the
>    back.
> 4. `refs/approved/21-objects.png` — the large folded document with the red wax
>    seal, its handwriting illegible.
> 5. `pages/page-31.png` — promoted previous page; binds the architecture, the
>    crimson value and the daylight.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 33 — *dramatic*

**Turn:** she testifies, he is finished — and the Count is leaning out of the gallery above him.
**Dominant:** Haydée and Fernand down the length of the hall — 47%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-33/candidates/page-33-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 33
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile crimson bench baize, waxed dark oak,
> heavy gilded plaster, brass rail, gold thread, red sealing wax and old handled
> paper, selective hard edges at the three faces and at the raised document.
> **Not smooth prestige-oil realism.** No glossy concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **crimson benches, heavy gold, dark oak, cold high daylight from
> above**, the woman's crimson-and-gold the one note that is not French, and **one
> hard spot of red wax** on the raised document.
>
> **Predecessor: attach the promoted page 32.** The same hall, the same hour,
> continuous — she has walked from the open door to the bar. What carries: the
> architecture, the crimson value, her dress and hair exactly as they were in the
> doorway, Fernand's decorations, and the sealed document she carried in. **Do not
> show** Albert, Mercédès, Beauchamp, Danglars in close-up, or any second woman.
>
> **Character locks.** The 3 supplied canonical character references bind the
> named visible characters, and one figure is built fresh.
> **Haydée, 27:** olive-gold skin, long unbound black hair, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build,
> **direct unornamented stillness**, crimson-and-gold Epirote embroidery on a
> loose vertical silhouette. Never a French waist, never a French coiffure, never
> the face of a woman of forty-two.
> **Fernand Mondego, 46:** heavy iron-and-black military moustache, receding
> temples, iron-grey at the sides, thick neck, heavy upright build, the full chest
> of decorations. Never clean-shaven, never pallid, never columnar.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with first grey, cultivated pallor, **unrelieved black**, seen only above the
> hall at the gallery rail.
> **The President of the Chamber is unnamed and has no reference sheet.** Build
> him fresh: **a heavy French official of about sixty**, clean-shaven or with
> short grey side whiskers, **balding with grey hair at the sides**, a plain dark
> official robe or heavy dark coat, **no military moustache, no decorations, no
> spectacles.** He must not resemble any other man in this book and must not carry
> a reserved combination: no unrelieved black columnar evening dress with
> swept-back hair and pallor; no heavy iron-black military moustache with receding
> temples; no small oval spectacles with untidy sandy hair.
>
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> ### Panel 1 — roughly 11% of the page, a **wide band across the top**
>
> **Haydée at the bar, alone, hands empty, entirely still**, the tiers rising
> behind her. She has already given the document up. Nobody else in frame close
> enough to read.
>
> One warm-ivory balloon, upper area beside her head, exactly:
>
> `My name is Haydée. My father was Ali Tebelen, Pasha of Janina.`
>
> ### Panel 2 — roughly 10%, a **narrow wide band** under panel 1
>
> **The President of the Chamber, half-risen** from a high seat above the floor,
> one hand on the desk in front of him. Head and shoulders and a little more.
>
> One warm-ivory balloon on his side of the band, exactly:
>
> `Mademoiselle. Do you know the accused?`
>
> ### Panel 3 — **DOMINANT, roughly 47% of the page**, the large middle block
>
> **One frame holding both of them with the entire crimson room in between.**
> **Haydée in the near ground at the LEFT, turned and looking down the whole
> length of the hall**, and **Fernand small at the RIGHT at the far end, looking
> back at her.** The tiers, the gold and the cold overhead light fill the distance
> between. Neither of them is moving. **Reserve the upper band of this panel as
> clear air and dark oak for three balloons before placing either figure.**
>
> Three warm-ivory balloons, **all hers, stacked down the LEFT side on her own
> side of the frame**, in this exact reading order:
>
> `He is fatter.`
>
> `He was an officer of my father's guard.`
>
> `He had the keys of the eastern gate, and he ate at our table for two years.`
>
> ### Panel 4 — roughly 18%, a **wide band**
>
> **The President of the Chamber reading aloud from the document**, holding it up
> so the hall can see it: the **large folded sheet with the red wax seal turned
> outward and clearly visible.** His face is above it. **The handwriting on the
> document must render as marks and not as readable words — nothing on this page
> depends on reading it, because he is saying it out loud.** **Place him at the
> left of the band with the raised document, and reserve the right two-thirds and
> the top of the band as a clear balloon lane.** Haydée is not in this panel.
>
> Three warm-ivory balloons, **all his**, in one reading column, in this exact
> order. **The first two strings each open and close with a literal single
> quotation mark and the first two each end with an em dash; render those marks
> exactly as given — they are part of the words he is reading out:**
>
> `'Received of the merchant El-Kobbir, four hundred thousand francs—'`
>
> `'—for a Christian slave of eleven years named Haydée, and her mother, wife of Ali Tebelen.'`
>
> `Signed, Fernand Mondego.`
>
> ### Panel 5 — roughly 14%, a **wide band across the bottom**
>
> **One frame, two figures, the height of the room between them.** Low in the
> frame: **Fernand frozen at the bar, not moving at all**, decorations still on
> his chest. High and behind him, at the top of the frame: **the gallery rail,
> and the Count with both hands flat on the wood, leaning out over the whole
> hall.** For this one panel he must look exactly like what he is — **a man at a
> killing he paid for**, and the appetite must be legible on the face. **Both
> figures are silent in this panel and neither receives a balloon.** No text of any
> kind in this band.
>
> **Lettering:** all **8** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization, apostrophes and accents — including the
> accent in `Haydée`, the hyphen in `El-Kobbir`, the em dashes, and the literal
> single quotation marks in the first two strings of panel 4. **No other quotation
> marks appear anywhere on this page.** Balloon lettering **44–50 px** on the
> 1024 × 1536 canvas, **never below 40 px** for any character; balloons
> **240–390 px** wide; warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps** — the quoted document lines are **not** to be italicised or set in a
> different face or a document-shaped box; they are normal balloons. **Haydée owns
> four balloons and the President owns four. Fernand speaks not once on this page
> and receives no balloon or tail fragment. The man in the gallery is silent.** No
> captions, no speaker labels, no page numbers, no titles, no pseudo-text, and **no
> legible handwriting on the document.** Comfortably readable when the page is
> reduced to 600 × 900.
>
> **Continuity and meaning:** she names herself and her father → the room asks the
> only question that matters → she looks down the length of the hall and identifies
> him with three flat facts → the receipt is read aloud with his signature on it →
> and the man who arranged it is leaning out over the rail above him. The document
> is the same sealed sheet she carried through the door on the previous page, and
> its content is spoken aloud here precisely so that no reader ever has to read the
> handwriting.
>
> No weapon, no violence, no chains, no second woman, no Albert, no Mercédès, no
> warm light, no candles, no identity collision, duplicated person or hand, fused
> fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/05-haydee.png` — Haydée.
> 2. `refs/approved/03-fernand-1838.png` — Fernand and the decorations.
> 3. `refs/approved/01-count-1838.png` — the figure at the gallery rail.
> 4. `refs/approved/23-page-33-chamber-objects-carrier.png` — deterministic,
>    unlettered carrier of approved sheet 19 (the floor, bar, tiers and public
>    gallery) and approved sheet 21 (the large folded red-wax-sealed document,
>    handwriting illegible); contains no character identity.
> 5. `pages/page-32.png` — promoted previous page; binds the hall, her dress and
>    hair, and the document.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 34 — *illustrated prose*

**Turn:** the hall empties; he is still wearing the decorations.
**Dominant:** Fernand alone on the crimson benches — 65%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-34/candidates/page-34-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 34
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile crimson bench baize, waxed dark oak,
> heavy gilded plaster, dust in a shaft of light, and enamel and ribbon on a
> man's chest, selective hard edges only at the single standing figure. **Not
> smooth prestige-oil realism.** No glossy concept-art surfaces, no airbrushed
> skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **crimson benches, heavy gold, dark oak, cold high daylight from
> above** — the same room as the last three pages, now nine-tenths empty, so the
> crimson reads as vacancy rather than occasion and the overhead light falls on
> rows of nobody. **Accent: the wax-red and old gold of the decorations still on
> his chest** — the only close, detailed, warm-valued thing on the page, and it is
> now worthless.
>
> **Predecessor: attach the promoted page 33.** The same hall, the same cold
> overhead daylight, minutes later. What carries: the architecture, the crimson
> value, Fernand's exact costume and **every decoration still in place on his
> chest**, and his position in the middle of the tiers. **Do not show** Haydée,
> the Count, Albert, Mercédès, Beauchamp, Danglars, the President, the sealed
> document, or any gallery figure. **One human being on this page and no other,
> apart from two small distant backs on a stair.**
>
> **Character lock.** One supplied canonical reference binds the only visible
> figure. **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, heavy black
> brows set low and close, deep-set close dark eyes, weathered ruddy-olive Catalan
> skin, **heavy iron-and-black military moustache**, black hair **receding at the
> temples** and iron-grey at the sides, thick neck, heavy upright soldier's build,
> **and the full chest of decorations still worn — orders, ribbons, wax-red seals
> and old gold, not one of them removed.** He is standing exactly as he was, and
> the posture is the content: **not collapsed, not weeping, not theatrical — a
> heavy upright man left standing because nobody has told him what to do next.**
> He must never be given a clean-shaven pallid columnar look or a full swept-back
> black wave; the moustache and the receding hairline are load-bearing.
>
> ### Panel 1 — **DOMINANT, roughly 65% of the page**, the large upper block
>
> The crimson benches **nine-tenths empty**, tier on tier, under cold light from
> above. **Fernand alone in the middle of the tiers, still standing, small in a
> very large room**, decorations catching the light on his chest. A few coats and
> hats left on benches; two small distant figures with their backs turned going
> out at a stair at the edge of the frame. Nobody is near him and nobody is
> looking at him.
>
> One matte parchment prose field, **cold ivory-grey**, set **across the upper
> area of this panel against plain empty crimson benching and dark oak — never
> over the figure, never over his chest, never over a face.** Exactly this text,
> in two paragraphs:
>
> `The vote took four minutes. Nobody spoke to him on the way out. Two men who had dined at his house in April went past him on the stair and looked at the stair.`
>
> `He stayed where he was for some time after the hall was empty, because he had not been given anything to do next, and for eleven years there had always been something to do next.`
>
> ### Panel 2 — roughly 35%, a **wide band across the bottom**
>
> **The empty doorway at the back of the hall** — the same great door that stood
> open two pages ago with a woman in it, now standing open on nothing: dark oak
> frame, cold light beyond, no figure in it at all. Straight on, symmetrical,
> still. No people anywhere in this panel.
>
> One matte parchment prose field, cold ivory-grey, in a calm area of this band,
> exactly this text, in two paragraphs:
>
> `By six o'clock the name had been taken off the door.`
>
> `His son heard it in the street, from a man selling papers.`
>
> **Lettering:** all **4** text blocks exactly once, with exact spelling, order,
> punctuation, capitalization and apostrophes. **This page has no speech balloons
> and no speaking characters.** Prose fields: **36–42 px** lettering on the
> 1024 × 1536 canvas, never below **40 px** for any character; **38–52 characters
> per line**; field width **78–88% of canvas**; internal padding **≥42 px**;
> left-aligned with a calm ragged right edge; upright mixed-case literary serif.
> **No italics, no all-caps prose, no condensed display faces.** **Two prose
> fields on this page and no more** — do not scatter the sentences into extra
> boxes. No quotation marks, speaker labels, page numbers, titles, signatures or
> pseudo-text, and **no readable lettering on any door, plaque or bench.**
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** four minutes of voting → a man left standing in an
> emptying room with every decoration still on → the door he was destroyed through,
> now empty → and by six o'clock his name is off it and his son has heard from a
> stranger in the street. He is still wearing the decorations here; the next time
> they appear they are on the floor of an empty room.
>
> No second named figure, no Haydée, no Count, no document, no crowd, no warm
> light, no candles, no weeping, no fallen body, no identity collision, duplicated
> person or hand, fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/03-fernand-1838.png` — Fernand and the decorations.
> 2. `refs/approved/19-set-chamber.png` — the tiers, the benches and the door at
>    the back of the hall.
> 3. `pages/page-33.png` — promoted previous page; binds the hall, the light and
>    his costume.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 35 — *dramatic*

**Turn:** Albert traces it back and finds the Count at the end of it.
**Dominant:** Beauchamp's face, and Albert understanding it — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-35/candidates/page-35-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 35
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile bare board, stacked newsprint,
> spilled ink, tallow candle grease, worn wool and unpainted deal table, selective
> hard edges at the two faces and at the spectacles. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **ink black, newsprint grey, tallow yellow, bare board** at night. This
> is the only unluxurious room in Paris in this book — cheap light from one or two
> tallow candles, paper everywhere, nothing gilded, nothing burgundy, nothing
> polished. **No old gold anywhere on this page.**
>
> **Predecessor:** the previous page is a different building and a hard cut; **do
> not attach it.** It is now night, and hours have passed. What carries in is the
> fact of the ruin: the young man arrives already knowing his father is finished.
> **Do not show** the Count, Haydée, Fernand, Mercédès, Danglars, Villefort, the
> Chamber, any bench, any crimson, or any other person in the office.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures, and this page carries **the volume's second-highest collision
> risk — its only two young men, together, alone.**
> **Albert de Morcerf, 22:** wide-set direct eyes and mouth, a jaw softened and
> un-weathered, **chestnut-brown hair — never raven black, never sandy** — worn
> short with a neat side part, **fair-olive skin several values lighter than any
> other man in this book**, slim and upright, clean-shaven with no side whiskers,
> **no spectacles ever**. **Costume: the volume's brightest values — a pale cream
> waistcoat and a coloured neckcloth under a dark coat that is nevertheless
> lighter and less absolute than black.** His open, quick-to-smile default is gone
> on this page: the face is closed and hard, but the structure, the hair colour and
> the costume value do not change.
> **Beauchamp, 28:** tall, thin, **slightly stooped even when seated**, **sandy-light
> brown untidy hair**, **small oval spectacles, present and legible in every panel
> he appears in**, long face, ironic mouth, ink-stained fingers, **plain dark worn
> practical clothes.** He does not lie and is not going to start tonight.
>
> **Separate them by four cues in every panel: hair colour (chestnut versus
> sandy), spectacles (never versus always), costume value (bright pale versus
> plain dark), and posture (upright versus stooped).** Albert must never read as a
> young version of a tall black-clad man of forty-two, and must never carry loose
> raven curls, an open white shirt or a red-brown sash.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law for the whole page: Albert is on the LEFT in every panel and
> Beauchamp is on the RIGHT in every panel.** They never swap sides, and every
> balloon sits on its own speaker's side.
>
> ### Panel 1 — roughly 17% of the page, a **wide band across the top**
>
> **Albert in the doorway at the left**, still in the frame of the door, night
> behind him. **Beauchamp at the right, seated at the press-room table and not
> getting up**, one hand still on a sheet of proof. The table, the stacked paper
> and one tallow candle between them.
>
> Two warm-ivory balloons, each on its owner's side. Left, Albert's:
>
> `The girl. Who is she?`
>
> Right, Beauchamp's:
>
> `Albert—`
>
> ### Panel 2 — roughly 18%, a **wide band**
>
> Albert come further in, at the left, both hands or one fist on the table edge,
> leaning in. Beauchamp at the right, seated, still. **Reserve the upper two-thirds
> of this band as a clear balloon lane before placing either figure, and keep both
> figures low in the band.**
>
> Two warm-ivory balloons, **both Albert's, stacked on the LEFT**, exactly:
>
> `She walked into the Chamber of Peers with a sixteen-year-old receipt and the name of a town nobody in France can find.`
>
> `Somebody put her there.`
>
> ### Panel 3 — roughly 15%, a **wide band**
>
> **Beauchamp at the right, deciding to answer** — the spectacles catching the
> tallow light. Albert at the left, waiting, a fraction of his face and shoulder
> in frame.
>
> Two warm-ivory balloons, each on its owner's side. Right, Beauchamp's, first:
>
> `She lives in a house on the Champs-Élysées.`
>
> Left, Albert's, second and lower:
>
> `Whose house.`
>
> ### Panel 4 — **DOMINANT, roughly 50% of the page**, the large lower block
>
> **Beauchamp's face at the right, large and close** — a man who has decided to
> say it plainly and does not enjoy it. **Albert at the left, in the same frame,
> understanding it before he is told**: the recognition arriving on his face while
> the other man is still speaking. Both faces in one frame across the cheap table,
> tallow light from below, black behind them.
>
> One warm-ivory balloon, **on the RIGHT, on Beauchamp's side**, exactly:
>
> `You've dined in it.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization, apostrophes and accents — including the
> accent in `Champs-Élysées` and the **em dash that ends** `Albert—`. Balloon
> lettering **44–50 px** on the 1024 × 1536 canvas, **never below 40 px** for any
> character; balloons **240–390 px** wide; warm ivory fill with a restrained
> charcoal-brown painted outline; upright mixed-case. **No italics, no condensed
> display faces, no all-caps.** **Albert owns four balloons and Beauchamp owns
> three**; every balloon sits on its owner's side of its panel, and the two men
> never swap sides. No captions or prose fields on this page. No quotation marks,
> speaker labels, page numbers, titles or pseudo-text, and **no readable words on
> any sheet of proof or newsprint on the table** — all such type is grey texture.
> Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** he comes for the woman's name → he says out loud that
> somebody aimed her → the honest man gives him the address instead of the name →
> and the last three words hand him the man he liked. The office is the same bare
> board room where he refused the retraction, now at night.
>
> No third figure, no printing press operating, no crowd, no gilt, no burgundy, no
> crimson, no weapon, no identity collision between the two young men, duplicated
> person or hand, fused fingers, illegible text, crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/04-albert.png` — Albert; hair colour, skin value, costume
>    value, no spectacles.
> 2. `refs/approved/07-beauchamp.png` — Beauchamp; sandy hair, spectacles, stoop,
>    plain worn dark clothes.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 36 — *dramatic*

**Turn:** he challenges the Count publicly, and the Count enjoys the answer.
**Dominant:** the Count still in a bright crowd — 55%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-36/candidates/page-36-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 36
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile gilt plaster, mirror glass, gaslight
> globes, massed pale silk, black broadcloth and kid leather, selective hard edges
> only at the two principal faces and at one glove. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **gilt, mirrors, gaslight, massed pale silk and black coats** — a
> bright, crowded, reflective public room. Everyone else is **a blur of light
> value in motion**; the accent is **one unbroken black vertical that the room does
> not touch.** Keep the crowd loose, broad-brushed and unfocused so that two faces
> and one glove are the only hard things on the page.
>
> **Predecessor:** the previous page is a different room and a hard cut; **do not
> attach it.** Later the same night, hours on. What carries in is Albert's state:
> he now knows, and he has come here to do this in front of witnesses.
> **Do not show** Haydée, Mercédès, Fernand, Beauchamp, Danglars, Villefort, or
> any identifiable second named face. The crowd is unnamed and out of focus, and
> **no figure in it may carry a complete identity stack belonging to a principal**
> — no unrelieved black columnar man with swept-back hair and pallor, no heavy
> iron-black military moustache with receding temples and decorations, no
> crimson-and-gold eastern embroidery with unbound black hair, no small oval
> spectacles with untidy sandy hair, no second young man in a pale waistcoat with
> a chestnut side part.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named visible characters, and this page carries **the volume's highest collision
> risk: these two men, alone, in one frame.**
> **The Count, 42:** tall, columnar, **unnaturally still**, clean-shaven,
> swept-back **black** hair with the first grey at the temples, deep-set
> black-brown eyes, strong straight brow, long clean nose, high cheekbones, **a
> slight asymmetry at the left corner of the mouth**, cultivated pallor,
> **unrelieved black evening dress.**
> **Albert de Morcerf, 22:** wide-set direct eyes and mouth, softened un-weathered
> jaw, **chestnut-brown hair, never raven black**, neat short side part,
> **fair-olive skin several values lighter than the Count's**, slim, upright,
> clean-shaven, no side whiskers, no spectacles, **a pale cream waistcoat and a
> coloured neckcloth** — the brightest values on the page. His open face is gone;
> he is white with rage.
>
> **Four cues separate them in every panel and none may lapse: hair colour
> (chestnut versus black), skin value (light versus pallid-cold), costume value
> (bright pale versus unrelieved black), and age (twenty-two versus forty-two).
> Albert must never read as a young version of the Count.** Neither may carry
> loose raven curls, an open white shirt or a red-brown sash.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law: Albert is on the LEFT and the Count is on the RIGHT in every
> panel where both appear.**
>
> ### Panel 1 — roughly 15% of the page, a **wide band across the top**
>
> **Albert coming through the crowd from the left**, and the crowd opening in
> front of him — perhaps forty people in evening dress under gaslight, already
> turning to look. Faces in the crowd are broad, soft and unreadable. **Keep the
> upper two-thirds of this band as clear bright air above the heads and reserve it
> as a balloon lane before placing any figure; keep Albert low and small in the
> band.**
>
> One warm-ivory balloon, **on the LEFT, on Albert's side**, in that reserved
> lane, exactly:
>
> `You came into my father's house. You took his hand on his own stairs. You ate at his table—`
>
> ### Panel 2 — **DOMINANT, roughly 55% of the page**, the large middle block
>
> **The Count, black, absolutely still, in the middle of a bright moving crowd**,
> at the right of the frame, gaslight and mirrors behind him, pale silk blurring
> past on either side. He has not shifted his weight. On his face, **the small
> flat pleasure of a line landing** — a private, contained enjoyment, not a smile,
> not serenity, not gravity. Albert at the left of the frame, nearer the edge,
> smaller, still coming at him.
>
> One warm-ivory balloon, **on the RIGHT, on the Count's side**, exactly:
>
> `I ate nothing at your father's table.`
>
> ### Panel 3 — roughly 12%, a **wide band**
>
> **Albert alone, close, struck.** The cruelty of it has landed and it is worse
> than a denial would have been. **He is silent in this panel and receives no
> balloon.** No text of any kind in this band.
>
> ### Panel 4 — roughly 10%, a **narrow wide band**
>
> **A glove in the air** — a pale kid glove thrown, caught mid-flight against the
> gilt and gaslight, with blurred faces beyond it. No full figures.
>
> One warm-ivory balloon, on the left side of the band with its tail running
> off-panel toward Albert, exactly:
>
> `Tomorrow. Eight o'clock, the Bois. Pistols.`
>
> ### Panel 5 — roughly 8%, a **narrow wide band across the bottom**
>
> **The Count's hand taking the glove out of the air without hurry**, and his face
> immediately above it at the right. For this one frame, after the pleasure,
> **something else crosses his face** — not fear and not regret, but the first
> thing in nine years he did not plan. Small, held, unmistakable.
>
> One warm-ivory balloon, **on the RIGHT, on his side**, exactly:
>
> `As you like.`
>
> **Lettering:** all **4** balloon strings exactly once, in this order, with exact
> spelling, punctuation and capitalization, **including the em dash that ends**
> `You ate at his table—`. Balloon lettering **44–50 px** on the 1024 × 1536
> canvas, **never below 40 px** for any character; balloons **240–390 px** wide;
> warm ivory fill with a restrained charcoal-brown painted outline; upright
> mixed-case. **No italics, no condensed display faces, no all-caps** — nothing on
> this page is shouted in larger type or set in a jagged balloon, including the
> challenge. **Albert owns two balloons and the Count owns two. Every person in the
> crowd is silent and receives no balloon and no tail fragment.** Panel 3 carries
> no text. No captions, quotation marks, speaker labels, page numbers, titles or
> pseudo-text. Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** the boy walks the length of a public room to say it
> in front of forty people → the answer is a joke about a glass he did not drink →
> the boy is struck → the glove → and the man takes it too quickly, and for one
> frame the appetite slips. **The refusal being mocked here is the untouched glass
> at the Morcerf dinner, and this line is the first time it is used as a weapon.**
>
> No third named figure, no Haydée, no Mercédès, no Fernand, no weapon drawn, no
> stage or performance visible, no identity collision between the young man and
> the man in black, duplicated person or hand, fused fingers, illegible text, crop
> sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/04-albert.png` — Albert; chestnut hair, light skin value, pale
>    waistcoat.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 37 — *dramatic*

**Turn:** Haydée is exultant; the Count is not, and cannot say why.
**Dominant:** Haydée standing over him; he faces the wall — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-37/candidates/page-37-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 37
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile lacquered black wood, cold plaster,
> starched linen, porcelain, silver, untouched food and gold thread, selective
> hard edges at the two faces and at the laid table. **Not smooth prestige-oil
> realism.** No glossy concept-art surfaces, no airbrushed skin, no engraved
> cross-hatching, no children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey, unpolished new gold**, the room
> enormous and **deliberately underfurnished** — no clutter, no family objects, no
> portraits, no fire, no warmth. The single accent is **the woman's crimson and
> gold: she is the only warm figure in the coldest room in the book**, and the
> warmth is hers, not the room's.
>
> **Predecessor:** the previous page is a different building and a hard cut; **do
> not attach it.** It is later the same night. What carries in is the Count's
> costume — **the same unrelieved black evening dress he was wearing in the
> crowd** — and the fact that he has agreed to a duel at eight in the morning and
> has told her nothing about it. **Do not show** Albert, Mercédès, Fernand,
> Beauchamp, Danglars, Villefort, any servant of any kind, or any other person.
> **This house has no servants: two human beings on this page and no other.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures.
> **Haydée, 27:** olive-gold skin, **long unbound black hair**, large wide-set very
> dark eyes, straight brows, small straight nose, full mouth, slight build,
> **crimson-and-gold Epirote embroidery on a loose vertical silhouette — never a
> French 1838 waist, never a French coiffure.** On this page her habitual
> stillness is gone: **she is lit up, alive and moving**, and she is the only thing
> in motion in the volume's coldest room. She must never be given a sculpted
> formal French coiffure, a fitted burgundy-black gown, or the face of a woman of
> forty-two.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, deep-set black-brown eyes, high cheekbones,
> **a slight asymmetry at the left corner of the mouth**, cultivated pallor,
> **unrelieved black evening dress.** He is seated and **the appetite is switched
> off for the first time in the volume** — not serene, not peaceful: blank,
> stopped, looking at nothing. He must never be given a military moustache,
> receding temples, or a thickened build.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law: Haydée is on the LEFT and the Count is on the RIGHT in every
> panel where both appear.**
>
> ### Panel 1 — roughly 20% of the page, a **wide band across the top**
>
> **Haydée mid-stride across the enormous black room**, turned toward the viewer,
> hands moving, alight — the most animated any figure has been in this house. The
> cold room around her is nearly empty: black floor, one tall uncurtained window
> with the night city in it, no furniture to speak of. The Count is not in this
> panel, or is only a black shape at the extreme right edge.
>
> One warm-ivory balloon, **on the LEFT, on her side**, exactly:
>
> `They have scraped his name off the door of the Chamber. I went to watch them do it.`
>
> ### Panel 2 — roughly 15%, a **wide band**
>
> **A laid table**: white linen, porcelain, silver, a decanter and a glass, food
> set out and untouched. **The Count is at it, seated at the right, and is not
> eating** — hands still, plate untouched, not looking at the table. Haydée at the
> left edge, standing, watching him.
>
> One warm-ivory balloon, **on the LEFT, on her side**, exactly:
>
> `You are not eating.`
>
> ### Panel 3 — **DOMINANT, roughly 50% of the page**, the large lower-middle block
>
> **Haydée standing over him at the LEFT, close, triumphant** — the victory is
> hers and she is not hiding it. **The Count seated at the RIGHT, turned
> three-quarters away from her toward the tall black window, looking at the wall.**
> The enormous cold room around both of them, the night city outside. The whole
> content of the panel is the mismatch: **she is exultant and he is looking at a
> wall.** **Reserve the upper right area of the panel as calm black wall for the
> two balloons before placing either figure.**
>
> Two warm-ivory balloons, **both hers, stacked on the LEFT on her own side**,
> exactly:
>
> `You have wanted this since before I was born.`
>
> `It is on the table in front of you and you are looking at the wall.`
>
> ### Panel 4 — roughly 15%, a **wide band across the bottom**
>
> Both faces close, **Haydée at the LEFT and the Count at the RIGHT**, the black
> room behind them. Three short lines cross the frame and the last one is his.
>
> Three warm-ivory balloons, alternating strictly by side — **his on the RIGHT,
> hers on the LEFT, his on the RIGHT** — in this exact reading order:
>
> `The boy is twenty-two.`
>
> `I was eleven.`
>
> `Yes.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation and capitalization. Balloon lettering **44–50 px** on the
> 1024 × 1536 canvas, **never below 40 px** for any character; short replies may
> run **48–54 px** where space allows; balloons **240–390 px** wide; warm ivory
> fill with a restrained charcoal-brown painted outline; upright mixed-case. **No
> italics, no condensed display faces, no all-caps.** **Haydée owns five balloons
> and the Count owns two, both of them in panel 4**; every balloon sits on its
> owner's side of its panel and the two never swap sides. No captions or prose
> fields on this page. No quotation marks, speaker labels, page numbers, titles or
> pseudo-text. Comfortably readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** she has been out watching them scrape the name off →
> the food is laid and he will not touch it → she stands over him in triumph and
> he faces the wall → and the only two things he says are the boy's age and a bare
> *yes* to hers. **The untouched food here is not the enemy's-roof refusal — this
> is his own house, and that is exactly why it means something different.** She is
> right, he has no answer, and he has agreed to shoot the boy at eight in the
> morning without telling her.
>
> No servant, no third figure, no fire, no candles beyond the barest, no clutter,
> no family objects, no portraits, no crimson benches, no weapon visible, no
> identity collision, duplicated person or hand, fused fingers, illegible text,
> crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/05-haydee.png` — Haydée.
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/17-set-count-house.png` — the black room, the tall window, the
>    night city.
> 4. `refs/approved/21-objects.png` — the decanter and the glass on the laid table.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 38 — *dramatic*

**Turn:** Mercédès says *Edmond.*
**Dominant:** two faces, nothing else in frame — 55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-38/candidates/page-38-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 38
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile lacquered black wood, cold plaster,
> heavy travelling wool, damp night air and one lamp's brass, selective hard edges
> at the two faces and nowhere else. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey, unpolished new gold**, at night, lit
> by **one lamp and the city beyond the tall windows.** The room is enormous and
> deliberately underfurnished. **There is no crimson and no warm accent anywhere
> on this page** — the woman is in plain travelling black and the man is in
> unrelieved black, and the only light in the volume's coldest room is the lamp
> and the far windows of other people's houses.
>
> **Predecessor: attach the promoted page 37.** The same black room, the same
> night, later. What carries: the exact room, the tall uncurtained window and the
> night city in it, the Count's unrelieved black evening dress unchanged, and the
> laid table left where it was. **Haydée has gone and must not appear anywhere on
> this page** — no crimson, no gold embroidery, no unbound black hair, not in any
> panel and not in any reflection. **Do not show** Albert, Fernand, Beauchamp,
> Danglars, Villefort, or any servant. **The house is servantless and there is
> nobody to announce her: two human beings on this page and no other.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures.
> **Mercédès, Comtesse de Morcerf, 42:** decisive dark eyes, straight nose, lean
> mature cheeks, **visible lower-lid lines and temple lines**, **restrained grey
> threads at the temple**, dark hair dressed simply, **plain dark travelling dress
> and an outdoor cloak, no jewellery**, still upright carriage. **She is forty-two
> and must be visibly forty-two — a smoothed, beautiful, youth-washed face is a
> blocking defect on this page, and this page is one of only two in this stretch
> where her age is the point.** She has come herself, at night, with no card and
> nobody to announce her, and it has cost her something to do it.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, deep-set black-brown eyes, strong straight
> brow, long clean nose, high cheekbones, **a slight asymmetry at the left corner
> of the mouth**, cultivated pallor, **unrelieved black evening dress.**
>
> Mercédès must never be given long unbound black hair, crimson-and-gold eastern
> embroidery, a loose vertical eastern silhouette, or a late-twenties face — the
> woman she must not resemble is fourteen years younger and is not on this page.
> Their faces must remain structurally distinct even in profile, reduced scale,
> grayscale, partial hair, and travel clothes.
>
> **Staging law: Mercédès is on the LEFT and the Count is on the RIGHT in every
> panel where both appear, including the dominant panel.**
>
> ### Panel 1 — roughly 13% of the page, a **wide band across the top**
>
> **A servantless hall**: a large cold empty entrance space, one lamp, a door
> standing open on the night. **Mercédès alone in the doorway at the LEFT**, in
> travelling black with the cloak still on her, no card in her hand, nobody
> beside her. **The Count at the RIGHT**, some distance off, stopped where he
> stands. Nobody has shown her in and the emptiness of the hall must say so.
>
> Two warm-ivory balloons, each on its owner's side. Right, his, first:
>
> `Madame la Comtesse. At this hour.`
>
> Left, hers, second:
>
> `Don't.`
>
> ### Panel 2 — roughly 20%, a **wide band**
>
> **She comes into the room and does not sit** — mid-room, cloak still on, upright,
> hands still. He is at the right, not moving toward her. **Reserve the upper
> two-thirds of this band as clear black wall and empty air for the two balloons
> before placing either figure, and keep both figures low in the band.**
>
> Two warm-ivory balloons, **both hers, stacked on the LEFT on her own side**,
> exactly:
>
> `I have sat in that house since the newspaper, while men I have known twenty years found reasons not to look at me.`
>
> `I have not once had to wonder who was doing it.`
>
> ### Panel 3 — roughly 12%, a **wide band**
>
> **The enormous black underfurnished room seen wide, and Mercédès very small in
> the middle of it** — black floor, tall uncurtained windows, cold grey walls,
> almost no furniture, the city lights far off outside. **The room makes her small
> and it does not make her less**: she is upright, centred and unhurried in the
> middle of all that space. The Count is not in this panel, or is a single small
> black shape at the edge. **Both figures are silent in this panel. No text of any
> kind in this band.**
>
> ### Panel 4 — **DOMINANT, roughly 55% of the page**, the great lower block
>
> **Two faces, and nothing else in the frame.** **Mercédès at the LEFT, the Count
> at the RIGHT**, close, both large, turned to each other, the background reduced
> to plain black — **no window, no furniture, no room detail, no third element of
> any kind.** Her face is doing the work of twenty-three years and every line of
> her forty-two years is visible in it. His face is the moment the appetite stops:
> not shock played large, but a man hearing his own name and having nowhere to put
> it. **This is the sentence the whole volume has been holding and the panel must
> be built around the two faces and the three balloons, nothing else.**
>
> Three warm-ivory balloons, alternating strictly by side — **hers on the LEFT,
> his on the RIGHT, hers on the LEFT** — in this exact reading order. The first is
> one word and takes the highest position on her side:
>
> `Edmond.`
>
> `Nobody has said that name to me in twenty-three years.`
>
> `I have said it every day.`
>
> **Lettering:** all **7** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and accents — specifically the apostrophe
> in `Don't` and the full stop after `Edmond.` Balloon lettering **44–50 px** on the
> 1024 × 1536 canvas, **never below 40 px** for any character; **the one-word
> balloon `Edmond.` may run 48–54 px** and there is room for it; balloons
> **240–390 px** wide; warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps** — `Edmond.` is **not** to be enlarged into display type, italicised,
> given a special balloon shape, or set as a caption; it is a normal speech
> balloon at short-reply size. **Mercédès owns five balloons and the Count owns
> two**; every balloon sits on its owner's side of its panel and the two never swap
> sides. Panel 3 carries no text. No captions or prose fields on this page. No
> quotation marks, speaker labels, page numbers, titles or pseudo-text. Comfortably
> readable when the page is reduced to 600 × 900.
>
> **Continuity and meaning:** she has come alone at night to a house with no
> servants → she says what the last weeks have been without once defending her
> husband → the room makes her small and does not make her less → and then she says
> the name, and he tells her how long it has been, and she tells him she has been
> saying it every day. This is the first time in the volume anyone calls him
> anything but the Count, and the appetite the reader has watched since the first
> window stops here.
>
> No Haydée, no crimson, no gold embroidery, no unbound black hair, no servant, no
> third figure, no fire, no clutter, no window or furniture in the dominant panel,
> no identity collision, duplicated person or hand, fused fingers, illegible text,
> crop sheet, or outer frame.
>
> ## Reference images
> 1. `refs/approved/02-mercedes-1838.png` — Mercédès, and specifically the
>    travelling-black view; her age markers are binding.
> 2. `refs/approved/01-count-1838.png` — the Count.
> 3. `refs/approved/17-set-count-house.png` — the black room, the hall, the tall
>    windows.
> 4. `pages/page-37.png` — promoted previous page; binds the room, the night and
>    the Count's costume.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

---

Assembly fragment. Written to the pattern established by pages 1 and 2 in
`12-PRODUCTION-PLAN.md` §5. Use verbatim. Copy each to
`qa/production/page-NN/prompts/page-NN-v1.md` **before** generating.

Where a prompt says to attach the promoted previous page, attach
`pages/page-[NN-1].png` as an image input. That is the continuity mechanism and
prose is not a substitute for it.

---

## PAGE 39 — *dramatic*

**Turn:** she names what he has not admitted, and he agrees, in words, to stand
still and die.
**Dominant:** two faces very close, both wrecked — 46%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-39/candidates/page-39-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 39
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile black lacquer, wool, skin, cold
> plaster and night glass, selective hard edges only at the two faces and the
> one open hand. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness, no generic grimdark.
>
> Palette: **lacquer black, ivory, cold grey-blue night, unpolished new gold**,
> warm lamp-yellow only far outside the window glass. Her **burgundy-black**
> travelling gown is the only colour on the page and it is nearly black. This is
> the coldest room in the volume and it stays cold through the whole page.
>
> **Predecessor: attach the promoted page 38.** Same enormous underfurnished
> black room, same night, same two people, continuous — no time has passed. What
> carries: her travelling black, her upright carriage, his unrelieved black, the
> room's emptiness, the single low lamp, the tall black uncurtained windows.
> **Do not show** any servant, any third figure, any fire in the grate, any
> clutter arriving in the room.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures. There is no third person on this page.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, deep-set black-brown eyes, strong straight
> brow, long clean nose, high cheekbones, **a slight asymmetry at the left corner
> of the mouth**, hollow temples, cultivated pallor, **unrelieved black 1838
> evening dress — the only unbroken black vertical in any room**. Never Fernand's
> heavy moustache or thickened soldier's build; never Albert's chestnut hair,
> pale waistcoat or open mobile face.
> **Mercédès, 42:** **visibly forty-two** — lean mature cheeks, **temple and
> lower-lid lines plainly drawn**, restrained grey threads at the temple, dark
> hair sculpted into formal 1838 dress, decisive eyes, straight nose, still
> upright carriage, **burgundy-black vertical travelling gown**. **Smoothing her
> face or youth-washing her is a blocking defect.** Never Haydée's unbound black
> hair, gold embroidery or late-twenties face.
>
> Their faces must remain structurally distinct at reduced scale and in
> grayscale.
>
> ### Panel 1 — roughly 12%, narrow band across the top
>
> The two of them close in the dark, chest-up, **Mercédès on the left facing
> right, the Count on the right facing left**, an arm's length of black air
> between them. She is speaking to him and he is looking straight back at her.
>
> Two warm-ivory balloons. Hers **upper left, on her own side**, tail to her
> mouth, exactly:
>
> `Don't kill my son.`
>
> His **lower right, on his own side**, tail to his mouth, exactly:
>
> `Your son called me out in front of forty people.`
>
> ### Panel 2 — roughly 14%, left of a two-panel tier
>
> **Mercédès on the left facing right**, closer now; the Count's shoulder and
> jaw entering frame at the right, facing her. She is not pleading with her
> body — she is standing straight and asking.
>
> Three warm-ivory balloons, top to bottom. Hers first, upper left, tail to her
> mouth, exactly:
>
> `Then let him miss.`
>
> Then his, right side, tail to his mouth, exactly:
>
> `He will not miss. He has been shooting since he was ten.`
>
> Then his second, lower right, below the first, tail to his mouth, exactly:
>
> `His father taught him.`
>
> ### Panel 3 — roughly 13%, right of that tier
>
> **The Count on the right, three-quarters, lit down one side by the single
> lamp; Mercédès' head and shoulder at the left edge, facing him.** For the first
> time in the volume the pleasure is gone out of his face and nothing has
> replaced it yet.
>
> Two warm-ivory balloons. Hers upper left, tail to her mouth, exactly:
>
> `Then don't fire.`
>
> His lower right, tail to his mouth, exactly:
>
> `You are asking me to stand still in a field and let a Mondego shoot me.`
>
> ### Panel 4 — **DOMINANT PANEL — 46%**, the centre of the page
>
> **Two faces very close and nothing else in the frame** — the largest panel in
> the volume of two people simply looking at each other. **Mercédès left, facing
> right; the Count right, facing left**, both heads large, both of them
> **wrecked**: her jaw set and her eyes wet and refusing to spill, his face
> stripped of performance. No hands, no furniture, no window, no room — black air
> and two heads. Hold her forty-two-year-old structure at this scale: temple and
> lower-lid lines are more visible here than anywhere else on the page, not less.
>
> Three warm-ivory balloons, **all hers, stacked down her own left side, top to
> bottom, each with a tail to her mouth**, in this order, exactly:
>
> `You did not do this for justice, Edmond.`
>
> `You did it so that I would see it.`
>
> `I have seen it.`
>
> **The Count is silent in this panel and receives no balloon and no tail
> fragment.**
>
> ### Panel 5 — roughly 15%, wide band across the bottom
>
> **His poised right hand, opening** — the held, ready hand of a man about to
> decide, coming open and empty. The hand is low and near, his face above and
> behind it, and there is **nothing held in reserve behind that face for the
> first time in nine years**. Mercédès is not in this panel.
>
> Two warm-ivory balloons, both his, right side, upper then lower, tails to his
> mouth, exactly:
>
> `…Very well.`
>
> `I will stand where his second puts me, and I will not raise my hand.`
>
> **Lettering:** all **12** balloon strings exactly once, in this order, with
> exact spelling, punctuation, capitalization, apostrophes and accents. The
> first string is `Don't kill my son.` and the last is `I will stand where his
> second puts me, and I will not raise my hand.` **The ellipsis in `…Very well.`
> is a single ellipsis character at the head of the line and is not three
> spaced full stops.** Balloon lettering **44–50 px** on the 1024 × 1536 canvas,
> **never below 40 px**; the short replies `Then let him miss.`, `His father
> taught him.`, `Then don't fire.` and `…Very well.` at **48–54 px**; balloons
> **240–390 px** wide; warm ivory fill, never pure digital white, with a
> restrained charcoal-brown painted outline; upright mixed-case. **No italics, no
> condensed display faces, no all-caps.** Mercédès owns six balloons, the Count
> owns six; no tail crosses between their sides of a panel. No captions and no
> prose fields on this page. No quotation marks, speaker labels, page numbers,
> titles or pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** she asks for the boy's life → he refuses on the
> facts → she narrows it to *don't fire* → the dominant panel takes everything
> else out of the frame so that she can name his real motive to his face → and
> the last thing on the page is his ready hand coming open. **Do not let him go
> serene here.** What is on his face in panels 4 and 5 is a man being told the
> truth about himself and finding he cannot answer it.
>
> No third figure, no servant, no crowd, no weapon, no fire, no identity
> collision, duplicated person or hand, fused fingers, illegible text, crop
> marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/02-mercedes-1838.png` — Mercédès, travelling-black view.
> 3. `refs/approved/17-set-count-house.png` — the black room and its windows.
> 4. `pages/page-38.png` — promoted previous page; binds the room, the light, the
>    hour and both costumes.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 40 — *illustrated prose*

**Turn:** the night before — what a man puts in order when he has agreed to lose.
**Dominant:** the Count writing by one lamp in an enormous dark room — 65%.
**Locations:** 1. **Panels:** 2.
**Output:** `qa/production/page-40/candidates/page-40-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 40
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile paper, ink, bare wood, worn leather
> and lamp-brass, selective hard edges only at the hands, the lamp and the
> paper. **Not smooth prestige-oil realism.** No glossy concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **lacquer black and one small pool of warm lamplight**, ivory paper,
> unpolished new gold on the lamp. Ninety per cent of this page is black. The
> lamp is the only light source and there is no light in the windows.
>
> **Predecessor: attach the promoted page 39.** The same black room, hours
> later — three in the morning, the same night. What carries: the room's
> emptiness and scale, the tall uncurtained windows, his unrelieved black. **He
> is alone.** Mercédès has gone; **do not show her, Haydée, any servant or any
> second figure anywhere on this page.**
>
> **Character lock.** One supplied canonical reference binds the only figure.
> **The Count, 42:** tall, columnar, clean-shaven, swept-back black hair with the
> first grey at the temples, deep-set black-brown eyes, strong straight brow,
> long clean nose, high cheekbones, slight asymmetry at the left corner of the
> mouth, hollow temples, cultivated pallor, **unrelieved black**, in shirtsleeves
> and black waistcoat with the coat still on. Never Fernand's moustache and
> thickened build; never Villefort's narrow pale inverted triangle.
>
> ### Panel 1 — **DOMINANT PANEL — 65%**, the upper two-thirds
>
> An **enormous black room with almost nothing in it**, seen from a little above
> and to one side. Near the middle of it, a **bare table** and **one lamp**, and
> the Count writing — head down, sleeve pushed back, one sheet under his hand and
> **several finished sheets squared off beside him**. The pool of light reaches
> perhaps three feet and then the room simply stops. **Everything else on this
> panel is black.**
>
> One matte parchment prose field, **upper third of the panel, over flat black
> wall — never over the lamp, the papers, or the figure.** Cold-ivory parchment.
> Exactly this text, in two paragraphs:
>
> `He wrote until three. The estate to Haydée, entire, with a man in Trieste named to see it done. A letter to a shipowner in Marseille who was old now and would not understand any of it. Instructions about a house on an island that nobody else had ever seen the inside of.`
>
> `It took him under two hours to put down everything he had made in nine years, and there was nobody on the list he had known before 1815.`
>
> ### Panel 2 — roughly 35%, a wide horizontal band across the bottom
>
> Close and low, the same lamplight: **a flat pistol case on the table, shut**,
> its lid plain and its clasps closed, and **his hand resting flat on the lid** —
> not gripping it, not opening it. No face, or at most the underside of his jaw
> at the top edge. **The case stays closed. Do not show a pistol anywhere on this
> page.**
>
> One matte parchment prose field in this band, set into the black table surface
> beside the case, exactly this text, in two paragraphs:
>
> `Then he sat with the case shut in front of him and did the one piece of arithmetic he had been avoiding since April:`
>
> `what he had spent, and what he had bought with it.`
>
> **Lettering:** all **4** prose paragraphs exactly once, in this order, with
> exact spelling, order, punctuation, capitalization, apostrophes and accents —
> including the accent in `Haydée` and the lower-case `w` that opens `what he had
> spent`. This page has **no speech balloons and no speaking characters.** Prose
> fields: **36–42 px** lettering on the 1024 × 1536 canvas, never below **40 px**
> for any character; **38–52 characters per line**; **2–5 lines per paragraph**;
> field width **78–88% of canvas**; internal padding **≥42 px**; left-aligned
> with a calm ragged right edge; upright mixed-case literary serif. **No italics,
> no all-caps prose, no condensed display faces.** No quotation marks, no speaker
> labels, no page number, no title, no pseudo-text, no signature. **No legible
> writing on the sheets of paper on the table** — the handwriting is marks and
> texture only, and no story fact is carried by it. Comfortably readable at
> 600 × 900.
>
> **Continuity and meaning:** a man alone in a black room writing his estate
> away → a shut case with his hand on it → and the last thing on the page is a
> sum he has been refusing to do since April. This is the prose page that buys
> the duel its room; it is **not** a dramatic page and it carries no dialogue.
>
> No second figure, no servant, no Haydée, no Mercédès, no open pistol case, no
> visible firearm, no fire in the grate, no clutter, no identity collision,
> duplicated person or hand, fused fingers, illegible text, crop marks, or outer
> decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/17-set-count-house.png` — the room, its scale, the night
>    windows, the low black table and single lamp.
> 3. `pages/page-39.png` — promoted previous page; binds room, hour and costume.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 41 — *dramatic*

**Turn:** Mercédès gives Albert the name, four hours before the duel.
**Dominant:** mother and son across the table with the pistol between them — 50%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-41/candidates/page-41-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 41
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile polished walnut, gun-oil rag, wool,
> candle wax and burgundy cloth, selective hard edges at faces, hands and the
> pistol parts. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness.
>
> Palette: **the Morcerf house — burgundy, polished walnut, wax red, old gold,
> dense candle amber**, but at its lowest ebb: **one candle**, a warm crowded
> room mostly in shadow. **Her travelling black is the coldest thing in it.**
>
> **Predecessor: attach the promoted page 40.** This page is the **same night,
> at the other end of Paris**, and it deliberately cuts away from the Count's
> black room to a warm one. What carries from page 40 is the hour and nothing
> else: this is a different house, a different palette, and **the Count does not
> appear on this page at all.** Mercédès is in the **same travelling black she
> wore in the Count's house on pages 38 and 39** — she has come straight home.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures. There is no third person on this page.
> **Mercédès, 42:** **visibly forty-two** — lean mature cheeks, **temple and
> lower-lid lines**, restrained grey at the temple, dark hair sculpted into
> formal 1838 dress, decisive eyes, straight nose, upright carriage,
> **burgundy-black travelling gown**. **Youth-washing her is a blocking defect.**
> Never Haydée's unbound black hair or gold embroidery.
> **Albert, 22:** **chestnut-brown hair — never raven black** — short with a neat
> 1838 side part; **fair-olive skin several values lighter than the Count's**;
> his mother's wide-set direct eyes and mouth on his father's jaw, softened and
> un-weathered; slim, upright, unmarked by work; clean-shaven, no side whiskers;
> **the volume's brightest costume values — a pale waistcoat, shirtsleeves, a
> coloured neckcloth loose at the throat.** **Albert must never read as a young
> version of the Count** and must never be given loose raven curls, an open white
> shirt or a red sash. He and his mother should read plainly as mother and son —
> same eyes, same mouth, thirty years apart.
>
> ### Panel 1 — roughly 15%, top band
>
> **Albert seated at the left at a table**, a **pistol in pieces** in front of
> him — barrel, lock, rod, an oiled rag — cleaning it because there is nothing
> else to do with his hands. **Mercédès standing in the doorway at the right**,
> still in the travelling black, still in her outdoor things. He has looked up at
> her.
>
> One matte parchment caption rectangle, **upper left, tail-free, over the dark
> panelling and never over a face**, warm-cream parchment, exactly:
>
> `The same night, at the other end of Paris.`
>
> Two warm-ivory balloons below it. His first, on his own left side, tail to his
> mouth, exactly:
>
> `You've been out.`
>
> Then hers, right side, tail to her mouth, exactly:
>
> `Yes.`
>
> ### Panel 2 — roughly 12%
>
> **Mercédès sitting down opposite him** at the same table — a thing she has not
> done in this room since he was a boy — pulling the chair in herself. Albert
> partly in frame at the left, not moving. She is on the right.
>
> One warm-ivory balloon, hers, upper right, tail to her mouth, exactly:
>
> `Put that down. I am going to tell you about 1815.`
>
> ### Panel 3 — **DOMINANT PANEL — 50%**, the middle of the page
>
> The two of them **across the table, level with each other — Albert left facing
> right, Mercédès right facing left** — with the **dismantled pistol lying
> between them** on the walnut and **one candle** doing all the lighting. She is
> looking straight at him and **she does not soften any of it**: no reaching
> hand, no comforting angle, no tears. The warm crowded Morcerf room falls away
> into shadow behind them both.
>
> Three warm-ivory balloons, **all hers, down her own right side, top to bottom,
> each tailed to her mouth**, in this order, exactly:
>
> `There was a boy in Marseille who was going to marry me. His name was Edmond Dantès.`
>
> `They arrested him at our betrothal dinner. He was nineteen.`
>
> `Danglars wrote the letter. Your father carried it to the post.`
>
> **Albert is silent in this panel and receives no balloon and no tail
> fragment.** Reserve the whole right third of this panel as a clean balloon lane
> before placing the faces.
>
> ### Panel 4 — roughly 13%
>
> **Albert not moving** — head and shoulders, close, the candle under him. Not
> shock played as melodrama: a young man holding absolutely still while something
> rearranges itself behind his face.
>
> Two warm-ivory balloons. His first, left, tail to his mouth, exactly:
>
> `You knew.`
>
> Hers, right, tail to her mouth, exactly:
>
> `I have always known.`
>
> ### Panel 5 — roughly 10%, narrow band across the bottom
>
> Close and low: **Mercédès' two hands flat on the walnut table**, side by side,
> perfectly still, a wedding ring on one. The pistol parts at the edge of frame.
> No faces.
>
> Two warm-ivory balloons above the hands, his first then hers, tails running
> off-panel toward each speaker's side — **his to the left, hers to the right** —
> exactly:
>
> `Where is he now?`
>
> `You are going to shoot at him at eight o'clock.`
>
> **Lettering:** the **1** caption and all **10** balloon strings exactly once, in
> this order, with exact spelling, punctuation, capitalization, apostrophes and
> accents — including the accent in `Dantès`. The caption is the only caption on
> the page and reads `The same night, at the other end of Paris.` Balloon
> lettering **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**; the
> short replies `Yes.`, `You knew.`, `I have always known.` and `Where is he
> now?` at **48–54 px**; balloons **240–390 px** wide; warm ivory fill with a
> restrained charcoal-brown painted outline; upright mixed-case. Caption
> lettering **36–42 px** on matte warm-cream parchment, tail-free. **No italics,
> no condensed display faces, no all-caps.** Mercédès owns seven balloons, Albert
> owns three; tails touch only their two mouths as assigned. No quotation marks,
> speaker labels, page numbers, titles or pseudo-text. Comfortably readable at
> 600 × 900.
>
> **Continuity and meaning:** a boy cleaning a duelling pistol for want of
> anything else to do → his mother sitting down opposite him for the first time
> in fifteen years → the whole 1815 story told flat across a table with the
> pistol lying between them → *you knew* → and the last line of the page tells
> him who he is meeting at dawn. The pistol must be visibly the same weapon in
> panels 1, 3 and 5, and it must stay in pieces.
>
> No Count, no third figure, no servant, no assembled or aimed firearm, no
> identity collision, duplicated person or hand, fused fingers, illegible text,
> crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/02-mercedes-1838.png` — Mercédès, travelling-black view.
> 2. `refs/approved/04-albert.png` — Albert, default view.
> 3. `refs/approved/18-set-morcerf-house.png` — the Morcerf interior, its walnut,
>    burgundy and gilt.
> 4. `pages/page-40.png` — promoted previous page; binds the hour and the
>    register across the cut.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 42 — *dramatic*

**Turn:** on the ground, Albert withdraws the challenge publicly.
**Dominant:** Albert bareheaded before the seconds — 55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-42/candidates/page-42-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 42
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile wet grass, mist, soaked black bark,
> heavy wool coats, cold steel and worn case-leather, selective hard edges only
> at Albert's face and the open case. **Not smooth prestige-oil realism.** No
> glossy concept-art surfaces, no airbrushed skin, no engraved cross-hatching,
> no children's-book softness, no photographic lens flare.
>
> Palette — **this is the one place in the volume with air in it and it must not
> look like another Paris interior**: **pale grey-green, standing mist, wet black
> trunks, and one thin band of gold at the horizon.** Open distance, a wide
> low-lying field, sky visible in every panel that has a horizon in it. Values
> are **high and cool**, the opposite of the candlelit burgundy room on the
> previous page. **No candlelight, no lamplight, no interior warmth, no gilt, no
> walls.** The only true blacks are the wet tree trunks and the men's coats.
>
> **Predecessor: attach the promoted page 41.** Four hours later, at dawn, out of
> the city. What carries: Albert himself, and **Mercédès' travelling black**,
> which will appear on the following page. What deliberately does **not** carry:
> the Morcerf palette, the candle, the interior. This is the first open sky in
> Paris in this book.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> named figures. Everyone else on this page is an unnamed background witness.
> **The Count, 42:** tall, columnar, **unnaturally still**, clean-shaven,
> swept-back black hair with the first grey at the temples, cultivated pallor,
> **unrelieved black**, in a black overcoat, hatless or hat in hand. On this page
> he is **small, apart, and does not speak**. Never Fernand's moustache and
> thickened build.
> **Albert, 22:** **chestnut-brown hair — never raven black**, short with a neat
> side part, now uncovered and damp with mist; **fair-olive skin several values
> lighter than the Count's**; his mother's wide-set direct eyes and mouth;
> clean-shaven, no side whiskers; slim and upright; **pale waistcoat under a dark
> coat — the brightest values on the page**; **his hat held in his hand, not on
> his head, from panel 2 onward.** **Albert must never read as a young version of
> the Count**, and must never be given loose raven curls, an open white shirt or
> a red sash. The two of them are in the same field on this page and must be
> unmistakable at a glance: one is black-haired, pale, black-clad and motionless;
> the other is chestnut-haired, warmer-skinned, lighter-dressed and speaking.
>
> **The unnamed figures — two seconds and a surgeon** — are ordinary Parisian
> men of forty to sixty in dark overcoats and hats. **No unnamed figure may be
> given a heavy iron-black military moustache with receding temples, unrelieved
> black with swept-back hair and pallor, small oval spectacles with untidy sandy
> hair, or a bright pale waistcoat on a young man.** Those silhouettes belong to
> named characters. Keep the witnesses' faces plain, middle-aged and generic.
>
> ### Panel 1 — roughly 20%, wide band across the top
>
> **The field, wide and cold**: standing mist to knee height, wet grass, a
> clearing among wet black trunks, thin gold at the horizon behind. In it — a
> **closed carriage** at the left, **two seconds** conferring, a **surgeon** with
> a bag set down at his feet, all small in the frame. **At the right, well apart
> from the group, the Count**, alone, already perfectly still, a black vertical
> in all that pale grey-green. No text of any kind in this panel.
>
> ### Panel 2 — **DOMINANT PANEL — 55%**, the middle of the page
>
> **Albert with his hat off**, holding it at his side, standing **in front of the
> two seconds and facing them** — he is at the left facing right, the seconds at
> the right facing him, the surgeon behind them. He is **speaking loudly enough
> for the whole field to hear it**: chin up, shoulders back, eyes level, no
> theatricality. **Nobody in the frame expected this** — read it on the
> witnesses' faces: one half-turned mid-step, one with his mouth open. Mist
> around their legs, wet black trunks and thin gold sky behind. The Count is
> **not** in this panel.
>
> One large warm-ivory balloon, **upper left, over the pale open sky on Albert's
> own side**, tail to his mouth, exactly:
>
> `I asked for this and I'm withdrawing it. Out loud, here, so nobody has to hear it from somebody else later.`
>
> Reserve this balloon's lane in the upper left of the panel before placing any
> figure.
>
> ### Panel 3 — roughly 15%, left of a lower tier
>
> **One of the seconds**, close, half-outraged — a plain middle-aged man in a
> dark overcoat, mouth tight — **holding the flat pistol case open in both
> hands**, the two duelling pistols seated in their green baize recesses,
> untouched. Nobody is holding a pistol.
>
> One warm-ivory balloon, upper area, tail to his mouth, exactly:
>
> `On what grounds, monsieur?`
>
> ### Panel 4 — roughly 10%, right of the lower tier
>
> **Albert, steady** — head and shoulders, hat still in hand, looking straight
> back at the man. Not defiant, not ashamed. Settled.
>
> One warm-ivory balloon, tail to his mouth, exactly:
>
> `On the grounds that the newspaper was right.`
>
> **Lettering:** all **3** balloon strings exactly once, in this order, with
> exact spelling, punctuation, capitalization and apostrophes — including the
> apostrophe in `I'm` and the lower-case `m` in `monsieur`. Balloon lettering
> **44–50 px** on the 1024 × 1536 canvas, **never below 40 px**; balloons
> **240–390 px** wide — the panel-2 balloon may run to the full 390 px and must
> not be shrunk to fit around a figure; warm ivory fill, never pure digital
> white, with a restrained charcoal-brown painted outline; upright mixed-case.
> **No italics, no condensed display faces, no all-caps.** Albert owns two
> balloons and one unnamed second owns one; **the Count receives no balloon and
> no tail fragment on this page**, and neither does the surgeon or the second
> second. No captions and no prose fields on this page. No quotation marks,
> speaker labels, page numbers, titles or pseudo-text. Comfortably readable at
> 600 × 900.
>
> **Continuity and meaning:** the machinery of a duel assembled in a cold open
> field → the boy takes his hat off and cancels it in front of everyone → a
> second demands a reason → and he gives one that costs him his father. The page
> must **breathe**: this is the only air, distance and open sky in the volume,
> and if it reads as another dark Paris interior the page has failed.
>
> No Mercédès on this page, no fired shot, no smoke, no raised or aimed pistol,
> no blood, no crowd beyond four witnesses, no identity collision, duplicated
> person or hand, fused fingers, illegible text, crop marks, or outer decorative
> frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/04-albert.png` — Albert, bareheaded-at-dawn view.
> 3. `pages/page-41.png` — promoted previous page; binds Albert's identity across
>    the four-hour cut.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 43 — *dramatic*

**Turn:** he gives up his father's name in front of witnesses and takes his
mother's.
**Dominant:** mother and son walking out of frame across the wet grass — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-43/candidates/page-43-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 43
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile wet grass, mist, soaked bark, heavy
> damp wool and worn leather, selective hard edges at faces and at the far
> carriage. **Not smooth prestige-oil realism.** No glossy concept-art surfaces,
> no airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: **pale grey-green, mist, wet black trunks, thin gold at the horizon** —
> continuous with the previous page and still **the only place in the volume with
> air in it.** High cool values, open distance, sky in every panel with a
> horizon. **No interior warmth anywhere on this page.**
>
> **Predecessor: attach the promoted page 42.** Same
> field, same dawn, continuous — seconds later. What carries: the exact
> clearing, the mist height, the band of gold at the horizon, the closed
> carriage, the witnesses' coats, Albert bareheaded with his hat in his hand, and
> the Count standing apart in unrelieved black.
>
> **Character locks.** The 3 supplied canonical character references bind the only
> named figures.
> **Albert, 22:** **chestnut-brown hair — never raven black**, short neat side
> part, uncovered, damp; **fair-olive skin several values lighter than the
> Count's**; his mother's wide-set direct eyes and mouth on a softened
> un-weathered jaw; clean-shaven; slim and upright; **pale waistcoat under a dark
> coat**; hat in hand.
> **Mercédès, 42:** **visibly forty-two** — lean mature cheeks, **temple and
> lower-lid lines**, restrained grey at the temple, dark hair sculpted into
> formal 1838 dress, decisive eyes, straight nose, upright carriage,
> **burgundy-black travelling gown**, the same one she has worn since page 38.
> **Youth-washing her is a blocking defect.**
> **The Count, 42:** tall, columnar, clean-shaven, swept-back black hair with the
> first grey at the temples, cultivated pallor, **unrelieved black**, and on this
> page — for the first time in the volume — **with no line ready**: the poised
> right hand half-lifted and stopping.
>
> **Albert must never read as a young version of the Count.** In panel 3 they are
> in the same frame: hair colour, skin value, costume value, age and expression
> separate them, and all five must be legible at reduced scale.
>
> **The unnamed figures — two seconds and a surgeon** — plain Parisian men of
> forty to sixty in dark overcoats and hats. **No unnamed figure may carry a heavy
> iron-black military moustache with receding temples, unrelieved black with
> swept-back hair and pallor, or a bright pale waistcoat on a young man.**
>
> ### Panel 1 — roughly 25%, top band
>
> **Albert in the near foreground at the left, three-quarters, still speaking to
> the seconds off-frame right.** Behind him, **at the far edge of the field in
> the mist, Mercédès standing beside a plain hired carriage**, small, alone,
> upright, in burgundy-black — she has been there the whole time and nobody has
> looked at her. **She is silent in this panel and receives no balloon.**
>
> Two warm-ivory balloons, both Albert's, stacked upper left over the pale sky on
> his own side, tails to his mouth, in this order, exactly:
>
> `My mother told me last night what my father did in 1815, to a man called Edmond Dantès.`
>
> `He did it for money, and he did it to marry her. The man was nineteen years old.`
>
> ### Panel 2 — roughly 12%
>
> **The two seconds and the surgeon**, together, mid-frame, **nobody moving** —
> one of them has stopped with a hand half-raised, the surgeon's bag still shut
> at his feet. Faces slack. Albert is out of frame.
>
> One warm-ivory balloon, **left edge, tail running off-panel to the left toward
> Albert**, exactly:
>
> `I've no quarrel with this gentleman. I haven't the right to one.`
>
> ### Panel 3 — roughly 13%
>
> **The Count, one step forward** — left of frame, facing right, black against
> pale mist, the poised right hand lifted and arrested halfway. **For the first
> time in the volume he has no line ready and it is on his face.** Albert at the
> right of frame, facing him, chestnut-haired and lighter-dressed, one flat hand
> up: *stop.*
>
> Two warm-ivory balloons. The Count's first, upper left on his own side, tail to
> his mouth, exactly:
>
> `Monsieur—`
>
> Albert's second, right side, tail to his mouth, exactly:
>
> `Don't.`
>
> **The em dash in `Monsieur—` is a single em dash character with no space before
> it and nothing after it.**
>
> ### Panel 4 — **DOMINANT PANEL — 50%**, the bottom of the page
>
> **Albert and Mercédès walking away from the frame across the wet grass toward
> the hired carriage, backs to us, small under a wide dawn sky** — mist to their
> knees, wet black trunks either side, the thin gold band at the horizon ahead of
> them. **Albert on the right**, bareheaded, chestnut hair and pale waistcoat
> under the dark coat; **Mercédès on the left**, burgundy-black, her sculpted
> 1838 hair, not touching him. **The Count is not in this panel at all** — do not
> put a black figure anywhere in it.
>
> One warm-ivory balloon, **upper right, over the open sky above Albert**, with a
> short tail to the back of **Albert's** head so that ownership is unmistakable
> even though both figures are turned away, exactly:
>
> `I'll take my mother's name. She was Mercédès Herrera before she was anything of his.`
>
> **Lettering:** all **6** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization, apostrophes and accents — including the
> accents in `Dantès` and `Mercédès`, the apostrophes in `I've`, `haven't` and
> `I'll`, and the em dash in `Monsieur—`. Balloon lettering **44–50 px** on the
> 1024 × 1536 canvas, **never below 40 px**; `Don't.` at **48–54 px**; balloons
> **240–390 px** wide; warm ivory fill with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps.** Albert owns five balloons, the Count owns one, **Mercédès owns none
> and receives no tail fragment anywhere on this page**, and neither do the
> seconds or the surgeon. No captions and no prose fields. No quotation marks,
> speaker labels, page numbers, titles or pseudo-text. Comfortably readable at
> 600 × 900.
>
> **Continuity and meaning:** he says the whole thing out loud in front of
> witnesses → the field freezes → the Count starts to speak and is stopped by a
> boy → and the page ends with the two of them walking away from everything they
> owned, with the Count left out of the frame. The dominant panel is the volume's
> only wide open horizon with people walking *into* it, and it must feel like
> air.
>
> No fired shot, no smoke, no raised or aimed pistol, no blood, no embrace, no
> weeping, no crowd, no identity collision, duplicated person or hand, fused
> fingers, illegible text, crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/02-mercedes-1838.png` — Mercédès, travelling-black view.
> 3. `refs/approved/04-albert.png` — Albert, bareheaded-at-dawn view.
> 4. `pages/page-42.png` — promoted previous page; binds the clearing, the mist,
>    the light and the witnesses.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 44 — *illustrated prose*

**Turn:** nobody fired — and before he reaches the city gate he has decided it
changes nothing.
**Dominant:** the Count alone in the empty field — 65%.
**Locations:** the Bois and the road back, treated as one continuous journey,
then the black room. **Panels:** 3.
**Output:** `qa/production/page-44/candidates/page-44-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 44
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile wet grass, mist, carriage glass,
> soot-grey suburb stone, black lacquered wood and cut glass, selective hard
> edges only at the distant figure, the face at the window and the decanter.
> **Not smooth prestige-oil realism.** No glossy concept-art surfaces, no
> airbrushed skin, no engraved cross-hatching, no children's-book softness.
>
> Palette: the page **drains from air back into lacquer**. Panel 1 is **pale
> grey-green, mist, wet black trunks, thin gold at the horizon.** Panel 2 is
> **cold grey suburb daylight** through glass. Panel 3 is **lacquer black, ivory
> and unpolished new gold** — the Count's house, and the last of the air is gone.
>
> **Predecessor: attach the promoted page 43.** The same field, moments later,
> then the road, then his own house. What carries: the clearing, the mist height,
> the horizon band, his unrelieved black coat, and **the wet grass of the field
> still on him**.
>
> **Character lock.** One supplied canonical reference binds the only figure on
> this page. **The Count, 42:** tall, columnar, clean-shaven, swept-back black
> hair with the first grey at the temples, deep-set black-brown eyes, high
> cheekbones, slight asymmetry at the left corner of the mouth, cultivated
> pallor, **unrelieved black**, black overcoat. **No other person appears on this
> page** — no Albert, no Mercédès, no Haydée, no seconds, no surgeon, no servant,
> no coachman's face. He has no servants and nobody attends him.
>
> ### Panel 1 — **DOMINANT PANEL — 65%**, the upper two-thirds
>
> **The Count alone in the middle of the wet field, very small under a wide pale
> sky.** Wide, high, cold. **The carriages are already going**: Albert's and his
> mother's hired carriage out through the trees at the left, the seconds' the
> other way at the right, both small and diminishing. **Nobody is looking at
> him.** He **has not moved from the place where he was told to stand** — feet
> together, arms at his sides, hat in one hand, the mist to his knees. The field
> is emptying around a man who came out here to be killed.
>
> One matte parchment prose field, **upper third of the panel, over the flat pale
> sky — never over the figure and never over the trees.** **Pale grey-green**
> parchment. Exactly this text, in two paragraphs:
>
> `He had come out to the Bois to be shot at. He had spent the night before putting his affairs in order so that a boy of twenty-two could kill him without inconveniencing anybody, and he had meant it.`
>
> `Nobody fired. He stood on the wet grass a long while afterwards working out what he felt, which took longer than he expected, and what he arrived at was not relief.`
>
> ### Panel 2 — roughly 20%, middle band
>
> **The inside of his own carriage going back into Paris**: the Count at the
> window in three-quarter profile, cold grey light on one side of his face, the
> **grey suburbs sliding past outside the glass**. **He looks like a man doing
> arithmetic** — eyes fixed on nothing, mouth closed, entirely undramatic. Not
> grief. Calculation resuming.
>
> One matte parchment prose field in this band, **set into the dark carriage
> interior beside him, never over his face or the window**, cold-ivory parchment,
> exactly this text, in two paragraphs:
>
> `At three that morning he had thought that if he were let off he would stop.`
>
> `He was wrong about that, and he knew it before the carriage reached the gate. The son had let him go. The father had not, and would be at his door before dark.`
>
> ### Panel 3 — roughly 15%, narrow band across the bottom
>
> **The black room.** Close and low across the **low black lacquered table**: the
> Count's **own bare hand** — his hand, no glove, no servant's hand, no tray —
> **setting a cut-glass decanter and one empty glass down on the black wood,
> squared to the edge of the table, and going away again.** Render the hand
> mid-withdrawal, already leaving frame, the two objects standing exactly
> parallel to the table edge. **He has no servants; this is why it is his own
> hand.** **Nobody has drunk anything: the decanter is stoppered and full, the
> single glass is empty and dry.** No face, no second glass, no bottle, no food.
> No text of any kind in this panel.
>
> **Lettering:** all **4** prose paragraphs exactly once, in this order, with
> exact spelling, order, punctuation and capitalization. This page has **no speech
> balloons, no captions, no sound labels and no speaking characters.** Prose
> fields: **36–42 px** lettering on the 1024 × 1536 canvas, never below **40 px**
> for any character; **38–52 characters per line**; **2–5 lines per paragraph**;
> field width **78–88% of canvas**; internal padding **≥42 px**; left-aligned with
> a calm ragged right edge; upright mixed-case literary serif. **No italics, no
> all-caps prose, no condensed display faces.** Two prose fields only, one in
> panel 1 and one in panel 2, never scattered. No quotation marks, speaker
> labels, page numbers, titles or pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** he was spared → he stands in the emptying field
> working out what he feels and it is not relief → in the carriage he admits to
> himself that he will not stop → and the last thing on the page is a decanter
> and one glass already put out for the man who is coming. **The final panel is
> the setup for the volume's payoff and its objects must be renderable again on
> the next page.** Do not add a second glass, do not fill the glass, and do not
> add a person.
>
> No second figure anywhere, no servant, no horse, no fired shot, no weapon, no
> identity collision, duplicated person or hand, fused fingers, illegible text,
> crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/17-set-count-house.png` — the black room, the low black table
>    and the night-window interior for panel 3.
> 3. `refs/approved/21-objects.png` — the cut-glass decanter and the tall glass,
>    empty, for panel 3.
> 4. `pages/page-43.png` — promoted previous page; binds the clearing, the mist
>    and the light.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 45 — *dramatic*

**Turn:** in his own house he pours and drinks, and tells Fernand what the
refusals meant.
**Dominant:** the Count drinking; the glass emptied — 50%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-45/candidates/page-45-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 45
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile cut glass, wine, black lacquered
> wood, damp wool, dried mud and skin, selective hard edges at the two faces, the
> pouring hand and the glass. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette: **lacquer black, ivory, cold grey afternoon daylight, unpolished new
> gold.** The one warm note on the page is **the wine in the glass**, and it is
> the only thing on the page that moves. **Fernand brings no colour with him** —
> the wax red is gone off him, no decorations, no ribbon.
>
> **Predecessor: attach the promoted page 44.** Same day, afternoon, the same
> black room, **the same decanter and the same single glass standing squared to
> the edge of the low black table where his own hand left them on the previous
> page.** What carries: the decanter's position, the glass, the room's emptiness
> and scale, and **the coat and boots he wore to the Bois — he has not been home
> long enough to change, and the wet grass of the field is still on his boots.**
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures. **There is no servant and no third person on this page** — the
> Count keeps no household, which is why he has to pour for himself.
> **The Count, 42:** tall columnar stillness, clean-shaven, swept-back black hair
> with the first grey at the temples, deep-set black-brown eyes, strong straight
> brow, long clean nose, high cheekbones, **a slight asymmetry at the left corner
> of the mouth**, cultivated pallor, **unrelieved black**, still in the black
> overcoat and mud-marked boots from the field.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, **heavy
> iron-and-black military moustache**, **black hair receding at the temples and
> iron-grey at the sides**, heavy black brows set low and close, deep-set close
> dark eyes, **weathered ruddy-olive Catalan skin, coarser and several values
> warmer than the Count's**, thick neck, heavy upright soldier's build — but the
> build is failing here: a ruined man in yesterday's coat. **The moustache and
> the receding hairline are load-bearing and appear in every panel he is in.**
> **Never** give him Danglars' fleshy face, side whiskers, short thickening body
> or badly-fitting expensive clothes; **never** give him the Count's clean-shaven
> face, full swept-back wave, pallor or columnar slimness. He is the only other
> man in this room and he must not be confusable with the Count at thumbnail
> scale: moustache versus clean-shaven, ruddy versus pallid, heavy versus
> columnar.
>
> ### Panel 1 — roughly 17%, top band
>
> **Fernand in the doorway**, filling it and small in it at the same time — **hat
> still on**, coat wrong, unshaven under the moustache, **a flat pistol case
> under one arm**. **The room is enormous around him** and the doorway is the
> only thing holding him up. He is at the left, facing right into the room.
>
> One warm-ivory balloon, upper left on his own side, tail to his mouth, exactly:
>
> `My son wouldn't fire at you. Take a pistol.`
>
> ### Panel 2 — roughly 15%
>
> **The Count seated, unhurried**, at the right facing left — still in the coat
> he wore to the Bois, **the wet grass and mud of the field still on his boots**,
> one leg crossed, hands quiet. Fernand at the left edge, upright, the case still
> under his arm.
>
> Three warm-ivory balloons, top to bottom. The Count's first, upper right on his
> own side, tail to his mouth, exactly:
>
> `No. Sit down.`
>
> Then Fernand's, left side, tail to his mouth, exactly:
>
> `You've destroyed me and you won't even—`
>
> Then the Count's second, lower right, tail to his mouth, exactly:
>
> `Sit down. You are going to be told why first.`
>
> **The em dash ending `you won't even—` is a single em dash character with
> nothing after it.**
>
> ### Panel 3 — **DOMINANT PANEL — 50%**, the middle of the page
>
> **The volume's primary motif pays off here and the drinking must be physically
> legible as an action, not an incidental prop.** Render it as one continuous
> movement across the panel, staged so a reader sees the sequence without a
> caption: **the Count standing at the low black table on the right, the
> unstoppered decanter in his left hand and the glass filling — wine visibly
> going into the glass — and then the same man, larger and nearer at the centre
> of the panel, with the glass at his mouth, head tipped back, throat working,
> drinking it down.** His eyes are open and on Fernand while he does it.
> **Fernand seated at the left, facing him, watching, and not understanding why
> it is happening** — his face is the panel's second subject and it should be
> blank with incomprehension. This is the first thing the Count has swallowed in
> the entire book. Do not stage it as a toast, do not clink anything, and **do
> not pour a second glass — there is one glass on this page and it is his.**
>
> Three warm-ivory balloons. The Count's first two, stacked down his own right
> side, tails to his mouth, in this order, exactly:
>
> `You watched me set a full glass down on your own staircase and decided I was ill.`
>
> `Your wife watched me refuse fruit out of her garden and knew what it meant inside a minute.`
>
> Then Fernand's, lower left on his own side, tail to his mouth, exactly:
>
> `What?`
>
> Reserve both balloon lanes before placing the figures; the pouring and drinking
> action occupies the lower two-thirds of the panel.
>
> ### Panel 4 — roughly 18%, bottom band
>
> Close and low: **the empty glass set down on the black wood** — drained, a red
> film in the bottom, standing where his hand has just left it — and **the
> Count's face above and behind it**, looking down the room at Fernand. The
> decanter is beside it, stoppered again. **The glass must read unambiguously as
> emptied**, and it is the same glass from panel 3 and from the last panel of
> page 44.
>
> Two warm-ivory balloons, both the Count's, upper then lower, tails to his
> mouth, exactly:
>
> `It is a rule of mine. I don't eat or drink under the roof of an enemy.`
>
> `This is my roof.`
>
> **Lettering:** all **9** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and apostrophes — including the
> apostrophes in `wouldn't`, `You've`, `won't` and `I don't`, and the em dash
> ending `you won't even—`. Balloon lettering **44–50 px** on the 1024 × 1536
> canvas, **never below 40 px**; the short replies `No. Sit down.`, `What?` and
> `This is my roof.` at **48–54 px**; balloons **240–390 px** wide; warm ivory
> fill, never pure digital white, with a restrained charcoal-brown painted
> outline; upright mixed-case. **No italics, no condensed display faces, no
> all-caps.** The Count owns six balloons and Fernand owns three; no tail crosses
> between their sides of a panel. No captions and no prose fields on this page.
> No quotation marks, speaker labels, page numbers, titles or pseudo-text.
> Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** a ruined man arrives with a pistol case and is told
> to sit down → the Count pours and drinks in his own house, which he has not
> done once in this book → he names the two refusals Fernand and Mercédès each
> witnessed → and then gives the rule that explains both of them and stops one
> sentence short of the reason. **The drinking is the page.** If a reader cannot
> see the glass fill, go to his mouth, and come down empty, the page has failed
> regardless of anything else on it.
>
> No servant, no third figure, no drawn or aimed pistol, no open pistol case, no
> food, no second glass, no fire in the grate, no identity collision, duplicated
> person or hand, fused fingers, illegible text, crop marks, or outer decorative
> frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count.
> 2. `refs/approved/03-fernand-1838.png` — Fernand, 46; moustache and receding
>    hairline load-bearing.
> 3. `refs/approved/17-set-count-house.png` — the black room, the doorway, the low
>    black table.
> 4. `refs/approved/21-objects.png` — the cut-glass decanter, and the tall glass
>    both full and empty.
> 5. `pages/page-44.png` — promoted previous page; binds the decanter and glass
>    where his own hand set them, and the coat and boots from the Bois.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 46 — *dramatic*

**Turn:** *I am Edmond Dantès.*
**Dominant:** the unmasked face, full frame — 46%.
**Locations:** 1. **Panels:** 5.
**Output:** `qa/production/page-46/candidates/page-46-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 46
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread. **This is the page the whole volume is aimed at;
> build its geometry exactly as specified.**
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile skin, wool, cold marble and black
> lacquer, **selective hard edges at the Count's face above everything else on
> the page**. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness, no generic grimdark.
>
> Palette: **lacquer black, ivory, cold grey afternoon daylight, unpolished new
> gold.** Almost monochrome. The warmest thing in the frame is the ruddy-olive of
> Fernand's face, and it drains across the page.
>
> **Predecessor: attach the promoted page 45.** The same room, continuous, no
> time has passed. What carries: the Count's black coat and mud-marked boots from
> the Bois, **the emptied glass and the stoppered decanter standing on the low
> black table**, Fernand's ruined coat and the flat pistol case, the doorway, the
> cold grey daylight.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures. There is no servant and no third person on this page.
> **The Count, 42 — this page is his face:** deep-set black-brown eyes, strong
> straight brow, long clean nose, high cheekbones, **a slight asymmetry at the
> left corner of the mouth**, hollow temples, cultivated pallor, clean-shaven,
> swept-back black hair with the first grey at the temples, **unrelieved black**.
> Never Fernand's moustache and thickened build; never Villefort's narrow pale
> inverted triangle; never Albert's chestnut hair or open mobile face.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, **heavy
> iron-and-black military moustache**, **black hair receding at the temples,
> iron-grey at the sides**, heavy low-set black brows, deep-set close dark eyes,
> **weathered ruddy-olive Catalan skin, coarser and warmer than the Count's**,
> thick neck, heavy build. **The moustache and the receding hairline appear in
> every panel he is in.** Never Danglars' fleshy side-whiskered face or short
> thickening body; never the Count's clean-shaven pallor and columnar slimness.
> At every scale on this page the two men must be separable by moustache, skin
> value and build alone.
>
> ### Panel 1 — roughly 12%, narrow band across the top
>
> **The Count, close, at the right of frame, facing left** — quiet, almost
> conversational, the poised right hand at rest. **Fernand's shoulder and the
> back of his head at the left edge**, seated. This is a man asking a question he
> has waited twenty-three years to ask and refusing to raise his voice for it.
>
> One warm-ivory balloon, upper right on his own side, tail to his mouth,
> exactly:
>
> `Do you know the name Dantès?`
>
> ### Panel 2 — roughly 18%
>
> **Fernand's face, close, beginning** — the exact moment before recognition
> arrives: the eyes moving, the mouth not yet. Not shock played large. **He is
> silent in this panel and receives no balloon and no tail fragment.**
>
> Three warm-ivory balloons, **all the Count's**, entering from the right edge
> and stacked top to bottom, **each with a tail running off-panel to the right
> toward the Count**, in this order, exactly:
>
> `February, 1815. The Pharaon.`
>
> `You could not write, so Danglars wrote it for you.`
>
> `You carried it to the post yourself, because you did not trust him to.`
>
> `Pharaon` is the name of a ship. **Letter it in the same upright mixed-case
> hand as the rest of the balloon — do not switch to a thin italic serif, do not
> add quotation marks, and do not render any asterisk or underline around it.**
> Reserve the right third of this panel as a clean balloon lane before placing
> the face.
>
> ### Panel 3 — roughly 18%
>
> **Fernand on his feet**, at the left, half-turned, **the flat pistol case
> forgotten under his arm** — he stood up and forgot he was holding it. The Count
> at the right, still seated or just risen, unmoved. Fernand is **silent in this
> panel and receives no balloon.**
>
> Two warm-ivory balloons, both the Count's, down his own right side, tails to
> his mouth, in this order, exactly:
>
> `I have been in your house. I have taken your hand on your stairs.`
>
> `I have had your son's arm through mine.`
>
> ### Panel 4 — **DOMINANT PANEL — 46%**, the centre of the page and the largest
> thing in the volume
>
> **The Count's face full in the frame, unmasked** — head and shoulders filling
> the panel edge to edge, straight to camera or a hair off it, lit flat and cold.
> **No performance left in it anywhere:** not triumph, not serenity, not a smile
> — the manner is simply gone, and what is underneath is a man of forty-two who
> has been carrying this for twenty-three years. The slight asymmetry at the left
> corner of the mouth is fully visible at this scale. **Fernand is not in this
> panel**; the panel belongs to one face and nothing else. No furniture, no
> window, no glass, no room detail — black around the head.
>
> Two warm-ivory balloons, both the Count's, placed in the black at the upper
> left and lower left so that **neither crosses his face**, tails to his mouth,
> in this order, exactly:
>
> `Look at me, Fernand.`
>
> `I am Edmond Dantès.`
>
> The second balloon is the sentence the book exists for. Give it its own clean
> lane, set it at the top of the speech range, and let nothing overlap it.
>
> ### Panel 5 — roughly 6%, narrow band across the very bottom
>
> **The empty doorway**, and beside it **the marble top where the pistol case was
> set down.** The case **is not there any more** — the marble is bare, one clean
> rectangle in the dust where it stood. No figure, no hand, no shadow of a
> person. No text of any kind in this panel.
>
> **Lettering:** all **8** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and accents — including the accents in
> `Dantès` in both the first and the last string. Balloon lettering **44–50 px**
> on the 1024 × 1536 canvas, **never below 40 px**; `Do you know the name
> Dantès?`, `Look at me, Fernand.` and `I am Edmond Dantès.` at **48–54 px**;
> balloons **240–390 px** wide; warm ivory fill, never pure digital white, with a
> restrained charcoal-brown painted outline; upright mixed-case. **No italics, no
> condensed display faces, no all-caps.** **Every balloon on this page belongs to
> the Count. Fernand does not speak on this page and must receive no balloon and
> no tail fragment in any panel.** No captions and no prose fields. No quotation
> marks, speaker labels, page numbers, titles or pseudo-text. Comfortably
> readable at 600 × 900.
>
> **Continuity and meaning:** a quiet question → the evidence laid out in three
> flat sentences while the other man's face begins to arrive → the three
> intimacies named, which are worse than the accusation → the mask off, full
> frame, in two lines → and a bare marble top where the case used to be. The last
> panel is the only thing on the page that tells you what happens next, and it
> does it with an absence.
>
> No servant, no third figure, no drawn or aimed pistol, no open pistol case in
> panels 4 or 5, no violence, no blood, no identity collision, duplicated person
> or hand, fused fingers, illegible text, crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — the Count; this page's dominant panel is
>    his face and must match this sheet exactly.
> 2. `refs/approved/03-fernand-1838.png` — Fernand, 46; moustache and receding
>    hairline load-bearing.
> 3. `refs/approved/17-set-count-house.png` — the black room and its doorway.
> 4. `pages/page-45.png` — promoted previous page; binds the room, the hour, both
>    costumes, the emptied glass and the pistol case.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 47 — *spectacle*

**Turn:** Fernand comes home to open wardrobes, and the house goes off like a
shot.
**Dominant:** the emptied bedroom, wardrobes open — 65%.
**Locations:** 1. **Panels:** 3.
**Output:** `qa/production/page-47/candidates/page-47-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 47
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile polished walnut, silk, cold gilt,
> ribbon, enamel, dust and stone, selective hard edges at the open wardrobe
> mouths and the one white window. **Not smooth prestige-oil realism.** No glossy
> concept-art surfaces, no airbrushed skin, no engraved cross-hatching, no
> children's-book softness.
>
> Palette — **this page reverses the Morcerf house.** The same burgundy, polished
> walnut, wax red, old gold and candle amber, **now cold**: dusk light with no
> lamps lit, the warmth drained out of every one of those colours, the gilt gone
> grey, the candle amber entirely absent. It is recognisably the same overstuffed
> house from earlier in the volume and it has stopped working. **No warm interior
> light anywhere on this page except the white window in panel 3.**
>
> **Predecessor: attach the promoted page 46.** An hour or two later, at dusk,
> across the city. What carries: **Fernand himself, unchanged from the Count's
> black room** — the same ruined coat, the same unshaven face under the
> moustache — and **the flat pistol case, which he took off the marble top on the
> last panel of page 46 and is carrying here.**
>
> **Character lock.** One supplied canonical reference binds the only figure.
> **Fernand Mondego, Comte de Morcerf, 46:** broad square jaw, **heavy
> iron-and-black military moustache**, **black hair receding at the temples and
> iron-grey at the sides**, heavy black brows set low and close, deep-set close
> dark eyes, weathered ruddy-olive Catalan skin, thick neck, heavy upright
> soldier's build now gone slack. **The moustache and the receding hairline are
> load-bearing and must be legible in both panels he appears in — he must never
> soften into a generic older man.** **Never** give him Danglars' fleshy face,
> full side whiskers, short thickening body or badly-fitting expensive clothes;
> **never** give him the Count's clean-shaven face, swept-back wave, pallor or
> columnar slimness. **He wears no decorations on this page.** No other person
> appears anywhere on this page.
>
> ### Panel 1 — roughly 20%, top band
>
> **The general's staircase, unlit and empty** — the same broad staircase built
> for a man who was not born to one, seen from below, its gilt grey in the dusk,
> not one candle burning on it. **Fernand climbing it alone with the case**, back
> mostly to us, small against its width. **Behind him at the bottom, the front
> door is standing open** on the darkening street, unattended: nobody shut it
> behind him and there is no servant to. No text of any kind in this panel.
>
> ### Panel 2 — **DOMINANT PANEL — 65%**, the middle and lower-middle of the page
>
> **The bedroom, wide.** **Wardrobes standing open and emptied** — doors wide,
> rails bare, one or two hangers left. **Drawers pulled out** and left out.
> **Jewel cases open on the table with everything still in them** — necklaces,
> stones, gold, untouched and catching the last grey light. **A woman's gown left
> across a chair.** And **Fernand's decorations — orders, ribbons, wax-red seals
> and old gold — on the floor**, where they were emptied out and left. **Fernand
> alone in the middle of the room with the case open in his hands**, looking at
> the jewel cases and not at the case. The room is a room whose people have gone
> and refused to take anything with them.
>
> One matte parchment caption rectangle, tail-free, **set into a calm dark area
> of the wall — never over a face, the jewels, or the open wardrobes**,
> warm-cream parchment, exactly:
>
> `His wife and son had taken nothing of his.`
>
> ### Panel 3 — roughly 15%, narrow band across the bottom
>
> **The front of the house seen from the street below**, at a low angle: the same
> great Morcerf façade, **black, shuttered and dead** — **except one upstairs
> window, which for the length of this panel is white.** A single flat white
> rectangle of light in a black front, no interior visible through it, no shape
> inside it. **No figure, no body, no wound, no weapon, no muzzle flash, no
> smoke, no blood, and nothing at all inside the window.** The death is entirely
> off-panel and is carried by the white window and the sound label alone.
>
> One small sound label — **third text level, simplified and enlarged lettering
> of the same family, set flat against the dark masonry beside the white window,
> not inside a balloon and not inside a caption rectangle** — exactly:
>
> `CRACK`
>
> **Lettering:** the **1** caption and the **1** sound label exactly once, with
> exact spelling, punctuation and capitalization. `CRACK` is set in capitals as
> the page's only capitalised string and is the only sound label in this range.
> This page has **no speech balloons and no speaking characters** — Fernand does
> not speak. Caption lettering **36–42 px** on the 1024 × 1536 canvas, never below
> **40 px** for any character, **38–52 characters per line**, field width
> **78–88% of canvas**, internal padding **≥42 px**, left-aligned, upright
> mixed-case literary serif on matte warm-cream parchment. The sound label is
> larger than the caption and smaller than a speech balloon's fill, plain,
> unornamented, **not jagged, not a starburst, not a comic-display face, and not
> outlined in colour.** **No italics, no distressed or faux-aged letterforms.**
> No quotation marks, speaker labels, page numbers, titles or pseudo-text. Text
> is under **15% of visual attention** on this page — it is a spectacle page and
> the image carries it. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** the staircase he built to prove something, unlit,
> with the door open behind him → a bedroom where the two people who owed him
> everything walked out and left the jewels on the table → and then one window in
> a dead house going white. The reader must understand what happened in panel 3
> **without being shown any part of it.** The staircase in panel 1 is the same
> staircase the Count climbed beside its owner earlier in the volume, and it must
> be redrawable as that staircase.
>
> No second figure, no servant, no Mercédès, no Albert, no Count, no body, no
> blood, no visible firearm outside the case, no discharge, no fire, no identity
> collision, duplicated person or hand, fused fingers, illegible text, crop
> marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/03-fernand-1838.png` — Fernand, 46; moustache and receding
>    hairline load-bearing.
> 2. `refs/approved/18-set-morcerf-house.png` — the general's staircase, and the
>    bedroom with the wardrobes standing open.
> 3. `refs/approved/21-objects.png` — the chest of military decorations, for the
>    orders and ribbons on the floor.
> 4. `pages/page-46.png` — promoted previous page; binds Fernand's face, his coat
>    and the pistol case he carried out.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 48 — *dramatic*

**Turn:** Mercédès and Albert take nothing, hear it, and leave anyway.
**Dominant:** both of them turned back toward the dark window — 55%.
**Locations:** 1. **Panels:** 4.
**Output:** `qa/production/page-48/candidates/page-48-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 48
> of *The Count of Monte Cristo, Volume II*** — not a prototype, proof sheet,
> mockup, cover, or spread.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile wet cobble, carriage lacquer, damp
> wool, worn leather and cold stone, selective hard edges at the two faces and
> the carriage lamp. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness.
>
> Palette: **lacquer black, wet cobble, gas-yellow.** The street is black and
> shining; the only warm light in the frame is **the single carriage lamp** and
> one distant gas lamp. **The great house behind them is entirely dark — no lit
> window anywhere in it.**
>
> **Predecessor: attach the promoted page 47.** Minutes later, at the foot of the
> same house, now full night. What carries: the Morcerf façade exactly as drawn
> on page 47 — the same building, the same shutters, the same window
> arrangement — and **the upstairs window that was white on page 47 panel 3,
> which is dark again here.** Its position in the façade must be identical.
>
> **Character locks.** The 2 supplied canonical character references bind the only
> visible figures. **Fernand does not appear on this page**, alive or otherwise;
> neither does the Count. There is no coachman's face and no servant.
> **Mercédès, 42:** **visibly forty-two** — lean mature cheeks, **temple and
> lower-lid lines**, restrained grey threads at the temple, dark hair sculpted
> into formal 1838 dress, decisive eyes, straight nose, **upright carriage that
> does not bend on this page**, **burgundy-black travelling gown**, the same one
> she has worn since page 38. **Youth-washing her is a blocking defect.** Never
> Haydée's unbound black hair, gold embroidery or late-twenties face.
> **Albert, 22:** **chestnut-brown hair — never raven black**, short with a neat
> 1838 side part; **fair-olive skin several values lighter than the Count's**;
> his mother's wide-set direct eyes and mouth; clean-shaven, no side whiskers;
> slim, upright; **a pale waistcoat under a dark travelling coat** — still the
> brightest values in the frame, but dimmed by the gaslight. **Albert must never
> read as a young version of the Count.** He and Mercédès must read as mother and
> son: the same eyes and mouth, thirty years apart.
>
> **They carry one small bag between them and nothing else.** No trunks, no boxes,
> no loaded carriage roof, no jewel case — the emptiness of their hands is the
> page.
>
> ### Panel 1 — roughly 20%, top band
>
> **Mercédès and Albert at the open door of a plain hired carriage**, wet cobble
> underfoot, gas-yellow raking across them. **One small bag stands on the stones
> between them.** Mercédès at the left facing right, Albert at the right facing
> her. **Behind and above them the great Morcerf house, entirely dark**, filling
> the top of the panel.
>
> Two warm-ivory balloons. Albert's first, upper right on his own side, tail to
> his mouth, exactly:
>
> `We could have taken the plate. It was my grandmother's.`
>
> Then Mercédès', left side, tail to her mouth, exactly:
>
> `He bought it in 1821, from a dealer in the rue Vivienne. There was no grandmother.`
>
> ### Panel 2 — roughly 12%
>
> **Albert, close**, gaslight down one side of his face, **absorbing that this is
> going to keep happening** — every object he grew up with about to turn out to
> be bought. Mercédès' shoulder at the frame edge.
>
> Two warm-ivory balloons. His, left, tail to his mouth, exactly:
>
> `You know where all of it came from.`
>
> Hers, right, tail to her mouth, exactly:
>
> `All of it.`
>
> ### Panel 3 — **DOMINANT PANEL — 55%**, the middle and lower-middle of the page
>
> **Both of them stopped and half-turned back toward the house, faces up** — seen
> from slightly below and behind so that we get both upturned faces and, above
> them, **the black façade and the one window that has gone dark again.** They
> have just heard something. **Nothing else in the street has changed:** the
> carriage stands where it stood, the lamp burns, the cobbles shine, nobody comes
> out, no shutter opens, no light goes on anywhere in the building. That
> stillness is the whole point of the panel — the street has absorbed it without
> noticing. Mercédès at the left, Albert at the right, a half-step apart, neither
> moving toward the door.
>
> Two warm-ivory balloons. Albert's first, upper right on his own side, tail to
> his mouth, exactly:
>
> `Mother—`
>
> Then Mercédès', left, tail to her mouth, exactly:
>
> `I know.`
>
> **The em dash ending `Mother—` is a single em dash character with nothing after
> it.**
>
> ### Panel 4 — roughly 13%, bottom band
>
> Close: **her hand closed on his forearm**, gripping, **holding him exactly
> where he is** — not comforting him, stopping him. Her sleeve, his sleeve, the
> wet black cobble below. Her face may be partly in frame above; his is not
> needed.
>
> Two warm-ivory balloons, both Mercédès', upper then lower, tails to her mouth,
> exactly:
>
> `Twenty-three years I lived in that house.`
>
> `Get in the carriage, Albert.`
>
> **Lettering:** all **8** balloon strings exactly once, in this order, with exact
> spelling, punctuation, capitalization and accents — including the em dash in
> `Mother—`. Balloon lettering **44–50 px** on the 1024 × 1536 canvas, **never
> below 40 px**; the short replies `All of it.`, `Mother—` and `I know.` at
> **48–54 px**; balloons **240–390 px** wide; warm ivory fill, never pure digital
> white, with a restrained charcoal-brown painted outline; upright mixed-case.
> **No italics, no condensed display faces, no all-caps.** Mercédès owns five
> balloons and Albert owns three; no tail crosses between their sides of a panel.
> No captions, no prose fields and **no sound label on this page** — the sound
> belonged to the previous page. No quotation marks, speaker labels, page
> numbers, titles or pseudo-text. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** a boy mourning a piece of plate that turns out to
> have been bought → the realisation that all of it was → the shot arriving while
> a mother and son stand in the street with one bag → and her hand on his arm
> keeping him out of the house. **Neither of them goes in, and neither of them is
> shown grieving.** The dark window in the dominant panel is the same window that
> was white on page 47 and must sit in exactly the same place in the façade.
>
> No Fernand, no Count, no body, no blood, no crowd, no gendarme, no servant, no
> trunks or luggage beyond the one small bag, no lit window in the house, no
> identity collision, duplicated person or hand, fused fingers, illegible text,
> crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/02-mercedes-1838.png` — Mercédès, travelling-black view.
> 2. `refs/approved/04-albert.png` — Albert, default view.
> 3. `pages/page-47.png` — promoted previous page; binds the façade, the shutters
>    and the exact position of the window.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

## PAGE 49 — *spectacle*

**Turn:** he watches the carriage go, and then looks up at Villefort's roof.
**Dominant:** the street, the departing lamp — 65%.
**Locations:** 1. **Panels:** 3.
**Output:** `qa/production/page-49/candidates/page-49-v1.png`

> Create one finished flattened graphic-novel story page at exactly **1024 ×
> 1536, 2:3 portrait, RGB PNG**. This is canonical-production candidate **Page 49
> of *The Count of Monte Cristo, Volume II*** — the final page of the volume, and
> not a prototype, proof sheet, mockup, cover, spread, or end-card.
>
> **Velvet Cinema** painterly realism: layered matte gouache and opaque
> watercolor over sparse charcoal and ink construction, broad visible
> brushstrokes, bold shadow masses, tactile wet cobble, soot-stained stone,
> slate, iron and night air, selective hard edges only at the carriage lamp and
> the far lit window. **Not smooth prestige-oil realism.** No glossy concept-art
> surfaces, no airbrushed skin, no engraved cross-hatching, no children's-book
> softness. **No end-of-book flourish**: no vignette, no fade, no decorative
> border, no title card.
>
> Palette: **lacquer black, wet cobble, gas-yellow.** The accent is **the
> departing carriage lamp — the last warm thing in the volume, and it is
> leaving.** The only other warm light is one small lit window at the very end of
> the page.
>
> **Predecessor: attach the promoted page 48.** The same street, continuous,
> seconds later. What carries: the wet cobble, the gas lamp, the plain hired
> carriage, and **the enormous shuttered Morcerf house, still entirely dark, on
> the left.**
>
> **Character lock.** One supplied canonical reference binds the only figure.
> **The Count, 42:** tall, columnar, unnaturally still, clean-shaven, swept-back
> black hair with the first grey at the temples, cultivated pallor, **unrelieved
> black**. **On this page he is seen small, distant and mostly in silhouette** —
> his identity is carried by the silhouette, exactly as it was on page 1: a tall
> slim man in unbroken black with a swept-back dark head. **Give no other figure
> that silhouette anywhere on this page**, and put no other person in the street.
> Mercédès and Albert are inside the departing carriage and **are not visible**.
>
> ### Panel 1 — roughly 20%, top band
>
> **The far pavement, deep in the dark**: one black figure, alone, standing
> against soot-stained stone well back from the gaslight — **he has been standing
> there the whole time**, through the previous page, and nobody in the street
> noticed him. Rendered so that the reader recognises the silhouette before the
> face; the face may be barely readable or not readable at all. **He is not
> hiding and not lurking — he is simply standing.** No text of any kind in this
> panel.
>
> ### Panel 2 — **DOMINANT PANEL — 65%**, the middle and lower-middle of the page
>
> **The street receding**, a deep one-point view straight down the wet cobbles:
> **the hired carriage going away from the frame, its single lamp small and warm
> and getting smaller**, reflections of it stretched out along the wet stone
> toward us. **The enormous shuttered house on the left**, black, dead, filling
> that side of the frame. Gas light overhead. **This is the last warm thing in
> the volume and it is leaving the picture** — compose so the lamp is small,
> centred deep in the perspective, and clearly moving away, not toward us.
>
> One warm-ivory balloon, **small, low in the frame at the near right, over the
> black of the pavement where the figure stands**, short tail to the standing
> figure's head, exactly:
>
> `One.`
>
> ### Panel 3 — roughly 15%, narrow band across the bottom
>
> **Looking steeply up past the roofline**, the way a man standing in a street
> looks up at a house further off. **This is the second of the three roofs
> established on page 1 and named on page 2 — the roof with the flagpole.**
> Render it unmistakably: a **slate roof with a flagpole on it**, at middle
> distance, other chimneys and rooflines around it, night sky behind. It is
> **not** the roof with the copper gutter and **not** the roof with every window
> lit. **One window on the second floor of that house is lit** and everything
> else in it is dark — somebody is still working in it, late. No figure in the
> window, no silhouette inside it.
>
> One matte parchment caption rectangle, tail-free, **set into the flat dark sky
> beside the roofline — never over the lit window and never over the slate**,
> cold-ivory parchment, exactly:
>
> `Villefort, the King's Attorney, kept late hours.`
>
> **Lettering:** the **1** balloon string and the **1** caption exactly once, in
> this order, with exact spelling, punctuation and capitalization — including the
> capitals in `Villefort` and `King's Attorney` and the apostrophe in `King's`.
> Balloon lettering **48–54 px** on the 1024 × 1536 canvas, **never below 40 px**;
> the balloon **240–390 px** wide even though its string is one word — do not
> shrink the balloon to the word; warm ivory fill with a restrained
> charcoal-brown painted outline; upright mixed-case. Caption lettering **36–42
> px**, field width **78–88% of canvas**, internal padding **≥42 px**, no
> essential text below **72 px** from the bottom edge, left-aligned, upright
> mixed-case literary serif. **No italics, no condensed display faces, no
> all-caps.** The Count owns the only balloon. **No sound label on this page.**
> No quotation marks, speaker labels, page numbers, titles, end-marks, `FIN`,
> `THE END`, credits or pseudo-text of any kind. Text is under **15% of visual
> attention**. Comfortably readable at 600 × 900.
>
> **Continuity and meaning:** he was there the whole time → the last warm thing
> in the book drives away from him down a wet black street → he counts it → and
> the final image of the volume is him looking up at the next roof, which the
> reader has been able to identify since page 2. **The rhyme with page 1 is the
> point of the page:** page 1 ended on three roofs at rooftop level, each with a
> lit window, the only warm thing in his world and all of them other people's
> houses. This panel is one of those same three, seen from the street instead of
> from his window, with one window still burning in it. Draw the flagpole roof so
> that a reader who has not seen page 1 in an hour still recognises it.
>
> No second figure in the street, no Mercédès or Albert visible, no Fernand, no
> body, no crowd, no gendarme, no horse rearing, no dramatic weather, no
> identity collision, duplicated person or hand, fused fingers, illegible text,
> crop marks, or outer decorative frame.
>
> ## Reference images
> 1. `refs/approved/01-count-1838.png` — binds the figure's silhouette, build and
>    costume.
> 2. `refs/approved/17-set-count-house.png` — binds **the three roofs**; panel 3
>    is the flagpole roof from view 3 of this sheet, seen from the street.
> 3. `pages/page-48.png` — promoted previous page; binds the street, the cobble,
>    the gas light, the carriage and the dark façade.
>
> All other character sheets are **prohibited generation inputs** for this page.

---

*End of pages 39–49.*

---

# 6 · The builder / critic architecture, and the per-page critic appendices

## The three roles, restated because this is where runs fail

| Role | May | May never |
|---|---|---|
| **Builder** | generate one completed candidate, record a non-gating audit, derive proofs, submit every completed candidate to the critic, prepare the next page's prompt | approve, promote, write to `pages/`, gate its own work, reroll without a critic verdict except for a failed generation, generate page N+1 before N is promoted |
| **Critic** | read, transcribe, judge, return a verdict and mandatory findings | edit, regenerate, promote, propose prompt wording |
| **Production lead** | release a page, promote bytes, hold a batch, bring a v4 ceiling and split proposal to the owner | generate, approve their own generation, autonomously redesign after v4, modify the page contract or full script |

**The critic runs as a separate agent.** A critic simulated inside the builder's
own context approves its own work. This is not a formality — it is the single
structural rule that separates this method from the run it replaced.

**Every brief this run needs is reproduced verbatim below**, under *The briefs,
verbatim*: §1 page critic · §2 builder · §2b prepare-next · §3 blind cold read ·
§4 batch sequence · §5 visual continuity · §6 whole book · §7 the verdict
contract. They are copied here from `10-CRITIC-OPERATIONS.md` so that this plan
can be executed without opening another file. The promotion sequence, the holds
table and the failure watchlist are in **§7 and §9 of this plan**, for the same
reason. `11-PRODUCTION-TOPOLOGY.md` is the same material in its source form and
travels with the folder as a cross-check, not as a dependency.

## The loop, in one screen

Release page N → copy §5's prompt to disk verbatim → resolve every reference in
`refs/approved/` → generate at 1024 × 1536 with references attached **as image
inputs** → record a non-gating self-audit → derive the 600 × 900 and 768 × 1152 proofs → hand every completed candidate to the
independent critic with §1's core brief **plus this page's appendix below** →
REVISE means redraw the whole page against the named defects only → APPROVED,
unconditional, means promote.

**The builder audit is not a gate.** A completed candidate goes to the critic
even when the builder believes it has failed. Only wrong canvas, a
corrupt/truncated output, or gross anatomical breakage is a failed generation
that may be regenerated before critic review.

## Instantiating the two agents

The separation has to exist in the *tooling*, not only in the prose. What that
means concretely:

| | Builder | Critic |
|---|---|---|
| **Started with** | §2 below, verbatim, plus §5's prompt for page N | §1 below, verbatim, plus **this page's appendix**, plus the two proofs |
| **Opens** | `qa/_plan/page-NN.md` | `qa/_plan/page-NN.md` |
| **May read** | everything | the proofs, the appendix, the brief |
| **May NOT read** | — | **the script, until after it has transcribed** |
| **Tools** | image generation, file write inside `qa/production/page-NN/` | **read-only** |
| **Returns** | a candidate, an audit, two proofs | `APPROVED` or `REVISE` + numbered mandatory findings |

- **One session per page, per role. Start a new one at every page boundary.**
  Not per ten-page batch — per page. An agent session re-sends its entire
  accumulated context on every turn, so a session that spans ten pages pays for
  page 14's transcript again on page 23. Nothing is lost by restarting, because
  every piece of state this run depends on is already on disk: the ledger, the
  critic reports, the promoted bytes, `RUN-LOG.md`. Measured on 2026-08-16: three
  long-running sessions consumed **334M input tokens in one day** against 21
  generated images, and the images were roughly three percent of the spend.
- **Nobody opens `12-PRODUCTION-PLAN.md` during production.** It is the master
  for reading and for owner edits. Both agents open `qa/_plan/page-NN.md`, which
  carries identical law and one page's prompt and appendix at about an eighth the
  size. The master is regenerated by `assemble.py`, which emits the per-page
  files in the same pass, so they cannot drift apart.
- **Two contexts, always.** The critic must not be able to see the builder's
  reasoning about why the page is fine. If the executor is Claude Code, the
  `monte-builder` and `monte-page-critic` agents already carry these briefs and
  the critic's toolset is read-only by construction. On any other executor, open
  a genuinely separate conversation and paste the brief in.
- **The critic transcribes before it reads the script.** That ordering is the
  whole value of the transcription test: a critic that has read the strings will
  see them in the proof whether they are legible or not.
- **The builder never speaks in the critic's turn** — no cover note, no "I
  already checked X", no list of things it thinks are fine. Those prime the gate.
- **The production lead is a third position, not a mood.** It is the only role
  that copies bytes into `pages/`. If one person is holding all three roles, the
  promotion step still happens as its own deliberate action, after an
  unconditional APPROVED exists in writing at `qa/production/page-NN/critic-vK.md`.
- **While the critic reviews page N, the builder prepares page N+1's prompt and
  nothing else** — §2b below. It does not generate page N+1. A page generated
  before its predecessor is promoted has attached the wrong predecessor.

## The briefs, verbatim — hand these to the agents unedited

### 1 · The page critic — core brief

Run on **every** generated page candidate. Agent: `monte-page-critic`.

**Owner override, 2026-08-15: NO SWEATING ABOUT TEXT SIZE.** The numeric type
sizes in the page prompts remain construction targets for the builder. They are
not critic gates. Exact, comfortable blind transcription at 600 × 900 is the
entire lettering-size test.

> You are the independent page critic for **The Count of Monte Cristo, Volume
> II**, a 49-page long-form illustrated novel. You are read-only: you may not
> edit, regenerate, or promote anything. You return a verdict and findings.
>
> **Page under review:** `[N]`
> **Candidate:** `qa/production/page-[NN]/candidates/page-[NN]-v[K].png`
> **Desktop proof (600 × 900):** `qa/production/page-[NN]/proofs/page-[NN]-v[K]-600.png`
> **Tablet proof (768 × 1152):** `qa/production/page-[NN]/proofs/page-[NN]-v[K]-768.png`
> **Script:** `08-FULL-SCRIPT.md`, page `[N]`
> **Prompt as issued:** `qa/production/page-[NN]/prompts/page-[NN]-v[K].md`
> **Your plan file:** `qa/_plan/page-[NN].md` — **open this one, not
> `12-PRODUCTION-PLAN.md`.** It carries the identical sections 1-10 and this
> page's appendix. The master plan is the same law repeated for forty-nine pages
> and costs roughly eight times as many tokens to hold; opening it is a defect.
>
> ## Step 1 — the transcription test. Do this first, before anything else.
>
> **Open the 600 × 900 desktop proof. Close the script. Transcribe every balloon
> and every caption you can read, from that proof alone, into your report, in
> reading order.** Do not consult the script while transcribing. Do not consult
> the 1024 × 1536 source.
>
> Then, and only then, open the script and compare.
>
> - **Any string you could not read is blocking.**
> - **Any string you read wrong is blocking.**
>
> This one pass is also the script-fidelity check, so both tests cost one read.
> This is the highest-value thing you do. Do not skip it, do not summarize it,
> and do not replace it with an assertion that the text is legible.
>
> ## Step 2 — the blocking gate
>
> Any one of these is **REVISE**:
>
> 1. **Script fidelity** — a word differs from the exact script string; a letter
>    is malformed, missing, duplicated or replaced; a string is present that is
>    not in the script.
> 2. **Speech attribution** — a tail points at the wrong speaker, a silent
>    figure, an object, or empty space; the first balloon a reader meets belongs
>    to a later speaker; the reading path crosses backward; a reader must guess
>    who is talking.
> 3. **Anatomy and generation integrity** — fused or extra fingers, duplicated
>    person, duplicated hand or object, broken limb, melted face, a figure
>    growing out of another.
> 4. **Consequential identity and continuity** — any character not recognisably
>    their approved reference; **any two characters confusable with each other**;
>    a costume, wound, object or time of day that contradicts the previous
>    promoted page.
> 5. **Page architecture** — the declared mode is not the mode rendered; there is
>    **no unmistakable single dominant panel**; more than **two** locations; more
>    than one dominant turn. **Dominant share is not a gate. Do not measure,
>    estimate or compute panel area, on the source or on the proof.** One panel
>    either owns the page at a glance or it does not, and that judgment is the
>    whole architecture test. The 45–70% target is a construction instruction for
>    the builder and is never checked against a rendered page.
> 6. **Reader comfort** — proved by Step 1, not asserted. **Step 1 is the whole
>    readability gate.** If you transcribed every string correctly off the
>    600 × 900 proof, the lettering is big enough. There is no second size test.
> 7. **Register fidelity** — the page has drifted to smooth prestige-oil realism,
>    glossy concept art, airbrushed skin, engraved cross-hatching, or
>    children's-book softness. The register is **Velvet Cinema**: layered matte
>    gouache and opaque watercolor over sparse charcoal and ink construction,
>    broad visible brushstrokes, bold shadow masses, tactile materials.
> 8. **Canvas** — anything other than 1024 × 1536 portrait.
>
> ## Step 3 — what is explicitly NOT blocking
>
> Do not raise these, and do not let them accumulate into a verdict:
>
> - **lettering size, in every form.** Do not measure glyphs. Do not estimate
>   x-height, cap height, line pitch or letterform extent, on the source or on
>   the proof. Do not compare rendered type to the numbers in §3. If a string
>   transcribed correctly in Step 1, its size passed, and the matter is closed;
>   if it did not transcribe, that is already blocking under item 6 and the size
>   number adds nothing. **A report that returns REVISE on lettering size while
>   its own transcription succeeded is a defective report**, and the finding is
>   void;
> - **panel percentages, in every form, including the dominant panel's own
>   share.** Do not measure, estimate or compute panel area. Do not compare a
>   rendered page to the shares in its prompt, its contract row or the script.
>   The only architecture question is whether one panel unmistakably owns the
>   page, answered by eye. **A report that returns REVISE on a share value is a
>   defective report**, and the finding is void. *(Owner instruction, 2026-08-16.
>   This is the same correction already made for lettering size, made for the
>   same reason: page 1 was held at 73% against a 70% target, and page 8's
>   fourteen-candidate spiral was largely a chase after a rendered share.)*;
> - tail-to-lip distance;
> - margin misses of a few pixels;
> - phone-size or 390 px performance — **not an approval gate**;
> - cosmetic polish, brushwork preference, palette taste;
> - **any deviation that does not change what the reader understands.**
>
> *This is a graphic novel, not an engineering tolerance exercise.* One page in
> the parent volume reached v77 across 143 candidates under a stricter reading of
> this list. The type targets in §3 are **construction instructions for the
> builder**, and they stay in every page prompt. They are not a gate, and they
> were never a gate the reader could feel. The transcription test is the gate,
> and it is stronger evidence than a measurement: it proves the page was read.
>
> ## Step 4 — the per-page appendix
>
> Open `qa/_plan/page-[NN].md` §6 and find this page's appendix. It names this
> page's own concrete commitments — the object states, the motif beats, the
> lookalike lanes live on this page. Check each one by name and report each by
> name.
>
> ## Step 5 — read it as a reader
>
> In your own voice, in prose, not as a checklist: does this page **work**? Is
> the dominant panel actually carrying the page's turn, or is the turn buried in
> a small panel? Is the room legible? Can you follow the eye path without effort?
> Would you turn the page?
>
> ## Verdict
>
> Return **APPROVED** or **REVISE**.
>
> - **APPROVED** must be unconditional. Do not write "approved with minor notes."
>   If you have a blocking finding, the verdict is REVISE.
> - **REVISE** must list **mandatory defects only**, numbered, each naming what
>   specifically is wrong and where on the page. Do not include wishes,
>   preferences, or polish. The builder will redraw the whole page against your
>   list, so a list padded with cosmetics wastes a generation.
>
> Include your full transcription in the report regardless of verdict.

---

### 2 · The builder brief — generate

Agent: `monte-builder`. One page at a time. Never two.

> You are the page builder for **The Count of Monte Cristo, Volume II**. You
> generate exactly one page candidate and submit it. **You never approve your own
> work, you never promote anything, and you never write to `pages/`.**
>
> **Page:** `[N]`
> **Your plan file:** `qa/_plan/page-[NN].md` — **open this one, not
> `12-PRODUCTION-PLAN.md`.** It carries the identical sections 1-10, this page's
> prompt and this page's appendix. The master plan is the same law repeated for
> forty-nine pages and costs roughly eight times as many tokens to hold; opening
> it is a defect. If you need a neighbouring page, open that page's file.
> **Prompt:** §5 of your plan file, page `[N]` — use it **verbatim**.
> **References:** exactly the manifest at the foot of that prompt, all from
> `refs/approved/`, plus the promoted previous page `pages/page-[NN-1].png` where
> the prompt says to attach it.
>
> Steps, in order:
>
> 1. Copy the prompt to `qa/production/page-[NN]/prompts/page-[NN]-v[K].md`
>    **before** generating. Every gate needs the exact prompt on disk beside the
>    candidate.
> 2. Generate at **1024 × 1536** with the reference images attached as image
>    inputs. Prose descriptions are not a substitute for attached references — a
>    run that silently degrades to prose-locking drifts in identity while its
>    ledger still says inputs were resolved.
> 3. Save to `qa/production/page-[NN]/candidates/page-[NN]-v[K].png`.
> 4. Run one **practical essentials audit** on your own candidate: is every script
>    string present and spelled right, does every tail point at its owner, is
>    there a single dominant panel, is anyone's anatomy broken, is anyone
>    confusable with anyone else. Write it to
>    `qa/production/page-[NN]/audit-v[K].md`.
>
>    **MEASURE NOTHING AND REPORT NO PERCENTAGES.** Do not estimate, compute or
>    state the rendered size of any panel, prose field, balloon or letterform, and
>    do not compare anything that rendered against a number in the prompt. "Is
>    there a single dominant panel" is answered *by eye, yes or no* — never with a
>    figure. An audit line of the form *"rendered roughly 29% against the 50%
>    target"* is prohibited, and if you write one, delete it before submitting.
>
>    **Why:** the percentages in the page prompt are steering values for the image
>    generator, not specifications it can hit. **It will never hit them, and it
>    undershoots essentially always** — pages 11, 12 and 13 of this volume asked
>    for 50%, 60% and 78–88% and rendered 29%, 46% and narrower. All three were
>    approved by the independent critic, two of them on the first candidate. The
>    gap is the generator's normal behaviour, not a defect, and it is not a
>    finding. **Reporting it is how page 8 happened:** an undershoot got read as an
>    error, "over-allocate to compensate" got invented to correct it, and the
>    fabricated number was written back into the script and the contract.
> 5. Derive the two proofs: **600 × 900** and **768 × 1152**, into
>    `qa/production/page-[NN]/proofs/`.
> 6. Submit to the independent critic. **Do not reroll on your own judgment.**
>    Every completed candidate goes to the critic. The audit you just wrote is a
>    **report, not a verdict** — you record what you found and you submit anyway,
>    including when you are confident the page has failed.
>
>    **The only regenerations you may perform without a critic verdict** are for
>    a failed *generation*, not a failed *page*: wrong canvas dimensions, a
>    corrupt or truncated file, or gross anatomical breakage. Nothing else. Not a
>    missed panel share, not a tail you think points wrong, not a composition you
>    consider weak. Those are the critic's calls and they are the reason it
>    exists.
>
>    **This is the most expensive rule in the method to break.** On page 8 of
>    Volume II, fourteen candidates were generated and only four reached the
>    critic; the builder killed ten in self-audit. The page was ultimately
>    APPROVED — meaning an unknown number of those ten would have passed, and the
>    generations were spent proving nothing to nobody. A builder that gates its
>    own work has silently deleted the critic from the run.
>
> **Never** feed a rejected candidate back in as a generation input. **Never**
> patch a balloon or a tail onto a flattened page. Regeneration is always a
> complete whole-page redraw from the approved references.

#### 2b · The builder brief — prepare next, do not generate

Issued while the critic reviews page N.

> While page `[N]` is under review, prepare the page `[N+1]` prompt only.
> Resolve its reference manifest against `refs/approved/` and confirm every file
> exists. **Do not generate page `[N+1]`.** Page `[N+1]` is released by the
> production lead only after page `[N]` is promoted, because page `[N]` is one of
> page `[N+1]`'s inputs.

---

### 3 · The blind cold read

Run at pages **10, 20, 30, 40, 49**, by an agent that has **not read the
script**. This is the only gate that measures whether the book communicates
without its own documentation.

> You are reading a graphic novel for the first time. You have not read its
> script, its outline, or any production document, and you must not open any of
> them — if you do, this gate is worthless.
>
> Read `pages/page-01.png` through `pages/page-[NN].png` **at 600 × 900**, in
> order, once, at reading speed. Then answer in prose:
>
> 1. **What happened?** Tell the story back in your own words.
> 2. **Who are these people?** Name everyone you can, describe everyone you
>    can't, and say how you tell them apart. **If any two people confused you at
>    any point, name the page.**
> 3. **Why did each thing happen?** Where did you have to supply a missing step
>    yourself?
> 4. **What changed for the main character?**
> 5. **Where did you have to stop and work?** Name the page and what stopped you
>    — a balloon you couldn't read, a face you couldn't place, a room you
>    couldn't parse, an order of events you had to reconstruct.
> 6. **Where were you bored?**
> 7. **Would you keep reading?**
>
> "Recoverable," "eventually clear" and "understandable after looking back" are
> not passing grades. They are defects. Report them as defects.

---

### 4 · The batch sequence gate

Run every ten pages, on the promoted pages only.

> You are auditing pages `[A]`–`[B]` of a 49-page illustrated novel as a
> **sequence**, not as individual pages. Each has already passed its own gate.
> You are looking for what only appears across pages.
>
> Read them in order at 600 × 900, then check:
>
> 1. **Rhythm.** Do the modes alternate, or does it read as a wall of talking
>    heads? Name any run of more than five consecutive dramatic pages.
> 2. **Identity across pages.** Does anyone drift — face, age, build, hair,
>    costume — from their first appearance in this batch to their last? Compare
>    against `refs/approved/`, not against the previous page.
> 3. **Continuity of state.** Objects, wounds, time of day, weather, who is
>    wearing what. **Named objects to track:** the wine glass, the decanter, the
>    sealed document, the flat case, Fernand's decorations, the newspaper.
> 4. **Register.** Has the painting drifted warmer, glossier, smoother, or more
>    detailed across the batch? Compare the first and last page of the batch side
>    by side.
> 5. **Palette logic.** Does each location keep its own palette, and do the
>    palettes still mean what `05-SETTINGS-AND-OBJECTS.md` says they mean?
> 6. **Turn clarity.** For each page, say in one sentence what changed. If you
>    cannot, name the page.
>
> Return APPROVED or REVISE with named pages. A REVISE here holds the next batch;
> it does not un-promote a page unless a defect is consequential.

---

### 5 · The visual continuity gate

Run after any long redraw chain, and once before the whole-book gate.

> Build a contact sheet of all promoted pages at thumbnail scale and inspect it
> as one image.
>
> 1. Does any page **jump** — brighter, glossier, flatter, more detailed, more
>    saturated — out of the sequence?
> 2. At thumbnail scale, can you still tell the eight principals apart? **Check
>    the young man in the pale waistcoat against the man in unrelieved black
>    specifically** — this is the volume's highest collision risk and thumbnail
>    scale is where it fails.
> 3. Does any page read as a different book?
>
> Name pages. Do not name preferences.

---

### 6 · The whole-book gate

Run once, at the end, before anything ships.

> All 49 pages are promoted. Verify, and report by page number:
>
> 1. Every page is exactly 1024 × 1536 portrait.
> 2. Every page's text transcribes correctly off its 600 × 900 proof. Do not
>    measure lettering; transcribe it.
> 3. Every script string in `08-FULL-SCRIPT.md` appears exactly once, on its own
>    page, spelled correctly.
> 4. Every page has one unmistakably dominant panel. Judge by eye; do not measure.
> 5. The mode distribution matches `07-PAGE-CONTRACT.md`: 33 dramatic, 8
>    illustrated prose, 7 spectacle.
> 6. No two consecutive pages are confusable in palette or location when they
>    should not be.
> 7. The six object motifs land on the pages `05-SETTINGS-AND-OBJECTS.md` says
>    they land on.
> 8. Read the whole thing at 600 × 900, cold, and say whether it is good.

---

### 7 · The verdict contract

Binding on every critic above.

- **APPROVED is unconditional.** There is no "approved with notes," no
  "approved pending," no "approved if." A critic who wants a change returns
  REVISE.
- **REVISE lists mandatory defects only.** Numbered. Each names what is wrong and
  where. Preferences, polish and wishes are omitted entirely — they cost a
  generation each.
- **Never cite an earlier gate's approval at a later gate.** Gates are
  non-transitive: an approved script does not approve references, approved
  references do not approve a page, an approved page does not approve a batch.
- **The critic never proposes a prompt edit.** It names the defect; the builder
  chooses the fix.
- **v4 ceiling.** If v4 of a page still returns REVISE, the composition has
  failed. Stop the run and report to the production lead for owner direction.
  Do not generate v5, redesign, split, add panels, or change page count.

---

## How to use an appendix

The core brief catches what is wrong with any page. An appendix catches what is
wrong with **this** page: the object states it must show, the motif beat it
carries, the identity collision that lives on it, and the specific way it is
likely to fail. The critic checks every line of the appendix **by name** and
reports each **by name**. An appendix line that goes unreported is itself a
finding against the critic, not against the page.

Appendix items are blocking on the same terms as the core brief: an object in
the wrong state, a motif beat missing, or a named collision realised is
consequential and returns REVISE. Everything else in an appendix that is marked
*watch* is context, not a gate.

## NO SWEATING ABOUT TEXT SIZE — lettering size is not a gate

**Owner override, 2026-08-15.** The type numbers in §3 are **builder
instructions**. They stay in every page
prompt, and they are what produces correct lettering. **They are not criteria the
critic checks.** No glyph is measured — not on the 1024 × 1536 source, not on the
600 × 900 proof, not by extent, x-height, cap height or line pitch.

**The transcription test is the entire text gate.** If every string transcribed
off the desktop proof, the type passed. If a string did not transcribe, that is
blocking under core-brief item 6, and no measurement adds anything to it.

**A REVISE whose only unresolved finding is lettering size, on a candidate whose
transcription succeeded, is void.** The production lead strikes the finding and
re-judges the candidate without it. If such a finding is what carried a page to
the v4 ceiling, the ceiling does not apply: strike it, re-judge, and do not
redesign a composition that was never the problem.

This is the specific failure that stalled page 1 of this volume — four reports,
each of which transcribed all four strings correctly and then returned REVISE on
glyph height anyway.

## Reading the text-density flags — the calibration

Several appendices flag a panel as a text-fit risk. Read those flags against the
only reliable evidence we have, which is **what Volume I actually shipped and the
reader judged a success**:

| Measure | Volume I's shipped ceiling |
|---|---|
| Dialogue words per share-point | **1.86** (page 7, panel 4: 39 words at 21%) |
| Balloons in one panel | **4** |
| Speech words in a panel at ≤20% share | **28** |
| Total rendered words on a page | **136**, median 71 |

Every dialogue panel in this volume is inside that envelope except the two named
on page 22. A flagged panel is therefore **a place to look hard, not a panel
presumed broken.** Do not return REVISE on a density flag because the arithmetic
looks tight — return it only because **the transcription test failed.** Treating
a within-envelope panel as broken on prediction is how a page reaches v77, and it
is the tolerance exercise this method exists to prevent.

Prose fields are a separate typography and pack far more text per share-point —
Volume I shipped a 94-word prose field in a 14% band. Never apply the balloon
numbers to a prose field.

---

## Page 1 — appendix

**Object and set state.** The room is **deliberately underfurnished** — enormous,
correct, and unlived-in. No family objects, no clutter, no warmth. If it reads as
a wealthy man's comfortable drawing room, that is blocking: the emptiness is
characterisation, and pages 15, 26, 29, 44, 45 and 46 all reuse this room.

**The three roofs are a contract with the whole volume.** They must be
countable, individually distinguishable, and each one must carry its named
feature: a copper gutter, a flagpole, and every window lit. Page 2 identifies
them one at a time by exactly those features, and **page 49's last panel returns
to one of them.** Three vague rooftops is blocking.

**Motif.** The city lights are the only warm thing in the frame, and they are
other people's houses. If the room itself is warmly lit, the page has inverted
its own accent.

**Text architecture.** Two prose fields, no balloons, no speaker. Prose fields
sit **over the dark wall, never over the window** — a field crossing the glass
kills the roofs and is blocking. Prose 36–42 px, 38–52 characters per line, field
width 78–88% of canvas, padding ≥42 px.

**Lookalike lanes:** none. One figure on this page, seen from behind.

**Likely failure.** The model furnishes the room. Second likely failure: the
figure is drawn too large, which destroys the scale relationship between the man
and the window that the whole page is built on.

**Superseded, 2026-08-16.** This appendix once carried a Page 1 only override
approving a rendered 73% share against a 70% construction target. That override
is no longer needed: **panel share is not a gate anywhere in this volume.** Page 1
passed because it has one unmistakable dominant panel and the three-roof band is
fully legible. Do not measure this page, or any page, for share.

---

## Page 2 — appendix

**Continuity in.** Same room, same window, same three roofs as page 1, promoted
`pages/page-01.png` attached. The roof arrangement must not shuffle between the
two pages — panel 2 puts the third house *through* the glass under his hand, so
the geometry established on page 1 has to survive.

**Attribution is the whole risk on this page.** Four balloons, two speakers, and
the Count has his back turned in the dominant panel. The reader must never
wonder who is speaking. Haydée owns exactly one balloon — `Which one first?` —
and the Count owns the other three. A tail on Haydée in panel 1, or a fifth
balloon anywhere, is blocking.

**Haydée's state.** She is holding a cup **she is not drinking from**, sitting
far back in the dark. She is watching *him*, not the window, in panel 3. She is
27 and must not read as a girl; she must not read as French. This is her first
appearance and it sets the lock for pages 18, 20, 22, 30, 32, 33 and 46.

**Motif — the engine.** Panel 4 is the appetite. *Pleasure in the face — not
calm. A man reading a menu.* A serene, remote, above-it-all Count in panel 4 is
blocking: it writes the engine of the book out of its second page. This is the
one item on this appendix that most deserves the critic's own voice.

**Lookalike lanes:** none yet — but this page fixes the Count's 1838 face for
every page that follows, so identity drift from `01-count-1838.png` here is
expensive later.

**Likely failure.** Four panels at 55/15/15/15 with the three small panels
collapsing into a strip that reads as one image, so panel 3's cut to Haydée is
lost and her question floats.

---

---

## Page 3 — appendix
- The cup is set down in panel 1 and is never picked up again. If any later panel shows it raised, in a hand, or absent from the table where it was set, the page fails.
- The pike and the head are spoken of and must not be depicted, not in a panel, not in a shadow shape, not on a wall, not as a silhouette in the window glass.
- The Count's raised right hand in panel 4 must read as a hand that is failing — not commanding, not gesturing, not pointing. If it reads as authority the dominant turn is inverted.
- No balloon tail may touch, cross, or terminate on that raised hand. `Haydée.` is the highest element in the panel and must be the first balloon a reader's eye reaches.
- Haydée is at the edge of the light and must hold the Epirote silhouette — unbound hair, crimson and gold, no French waist, no coiffure, no shawl arranged in the French manner — even at reduced scale and in shadow.
- Panel 1 is 20% and carries the day's first prose. Check that its lettering was widened rather than shrunk to fit — the fix for a tight prose field is a wider field, never smaller type. Judge it by transcription, not by measurement.

## Page 4 — appendix
- `You say the woman.` must render as plain upright mixed-case lettering. No italics, no bold, no asterisks, no underline, no size increase, no colour change. The emphasis in the script is not a rendering instruction.
- The woman under discussion is never depicted — no portrait, no memory panel, no figure in a doorway, no second female face anywhere on the page.
- Balloon ownership: Haydée owns five, the Count owns two. Count them. A page where the balance has drifted toward the Count has lost the turn.
- In the 10% closing band Haydée is at the door and is **not** looking back. A backward glance reverses the page.
- Haydée is the near figure and carries the page; if her face has drifted toward the Count's structure — the same brow, the same mouth asymmetry — the collision has gone the wrong direction and the page fails on identity.
- The Count is seated or still throughout; if he rises to follow her, the staging is wrong.

## Page 5 — appendix
- The candles must be visibly lower than they were on page 4. This is a stated continuity beat, not decoration, and it is checkable against the promoted predecessor.
- Panel 1 is silent by design: the right hand lies flat and poised on the sill. If a balloon has migrated into panel 1, or the hand is clenched, curled, or gesturing, the panel is wrong.
- The appetite in the dominant panel must read as *aimed* — directed at something outside the room — not as generalised brooding or melancholy.
- No glass and no decanter appear anywhere on this page. The glass motif has not begun. A glass here corrupts the object chain that pages 8, 11, 12 and 45 depend on.
- This page sits at 108 words against a dramatic ceiling of roughly 105. Panels 2 and 4 are at or over physical text capacity: verify every string transcribes exactly and comfortably from the 600 × 900 proof. Reject unreadable, crowded or clipped text, not a numeric type size.
- The window and the three lit roofs must match pages 1 and 2 exactly — same aspect, same roofline, same three.

## Page 6 — appendix
- Exactly two locations, no third. Any establishing sliver of a further place breaks the page contract.
- No face appears anywhere on this page. Not in a carriage window, not reflected, not distant in the street, not a servant's. A single face voids the page.
- `LE COMTE DE MORCERF` renders as an engraved object label on the card at 56 px or larger — the only capitals permitted on this page. It must read as engraving on paper, not as lettering drawn over the image.
- The caption is the single word `Thursday.` with the full stop. Not "Thursday" bare, not a longer phrase, not a date.
- The staircase visible through the doors must match reference sheet 18 and must match what page 8 will show. If the two disagree, page 8 inherits a defect.
- The carriage speech comes from off-panel; its tail runs off the panel edge toward the unseen speaker's established side and terminates on nothing visible.

## Page 7 — appendix
- Albert / Count collision lane is LIVE and this is its first joint page. Check all five axes at once: hair colour (chestnut versus raven black), skin (fair-olive versus pale), jaw, brow, and clothing value (pale waistcoat versus unrelieved black). One axis holding is not enough.
- Mercédès is distant and silent. She owns no balloon. At that scale she must still read as a woman in her early forties — lower-lid and temple structure legible. A smooth young face at distance is a blocking youth-wash defect, not a scale allowance.
- Albert takes the cloak from the servant's arms. The servant does not hand it to the Count, and the Count does not remove it himself.
- Neither Fernand nor any decoration appears on this page — not on a background figure, not in the crowd, not on a wall portrait.
- Panel 2 carries three balloons inside 18%. Verify all three transcribe exactly and comfortably from the 600 × 900 proof; this is the page's most likely readability failure.
- The em dash in Albert's line is an em dash, not a hyphen and not two hyphens.

## Page 8 — appendix
- Glass motif, beat one: an identical glass is **set down full** by the Count's hand. It is being set down, not lifted, not sipped, not swirled. If the level is low, or a mouth has been near it, the entire motif chain is broken at its origin.
- Two glasses are in play in the redesigned silent Panel 7. They must read as separate objects in different vertical planes: Fernand's small full glass suspended with at least one full glass-height of empty black space beneath its foot; the Count's separate full glass visibly touching marble. If both feet touch stone, or the left glass has any supporting surface beneath it, blocking.
- Panel 1 must be the unmistakable dominant field and must carry the sole entrance turn. **Judge that by eye. Do not measure it.** Share values in the prompt are construction targets and are never checked against the rendered page. *(This page shipped at a rendered 42%; the 62% figure it once carried was a compensation number invented for the generator and is not a design intent. Panel share is not a gate — owner instruction 2026-08-16.)*
- Fernand's moustache and receding temples must be present in every panel that shows him, including the tight panel and the profile. Losing the moustache in profile is the expected failure.
- Panels 2–6 are five one-speaker/one-balloon beats in exact Fernand–Count–Fernand–Count–Fernand order. Panel 5 shows only the Count saying `In Spain?`; Panel 6 shows only Fernand saying `In Greece.` No right-column panel may contain the other man or more than one balloon.
- Panel 7 is the silent glass action. The miniature/three-height language in the construction prompt is deliberate overcorrection, not a new story requirement. The critic gate remains the original locked motif: Fernand's full glass is visibly raised with no support beneath it and at least one complete glass-height of empty black below its foot, while the Count's separate full glass visibly touches marble. The Count's two final replies are isolated again: Panel 8 shows only the Count saying `Of course. Greece.`; Panel 9 shows only the Count saying `Forgive me. I am a stranger here and I get your wars wrong.` Each has exactly one balloon with its own tail to his visible mouth.
- The Count wears no decoration on this page. Fernand's worn decorations are the only decorations in frame. No military portrait, painted military figure, wall-mounted order, ribbon or decoration display appears anywhere.
- The small one-speaker panels carry one string each; check all four isolated strings transcribe exactly and comfortably from the 600 × 900 proof.
- The former Panel 2 A-B-A exchange has been structurally removed. Its three strings now occupy separate Panels 2, 3 and 4, each with one visible speaker, one balloon and one tail to that speaker's visible mouth.

## Page 9 — appendix
- Three handshakes occur. All three must be present, and the hands must be among the hardest-edged elements on the page — fingers counted, no fusing, no third hand entering frame.
- In panel 5 Villefort has **not** let go. The grip is still closed. A released or releasing hand loses the panel's whole meaning.
- Danglars has side whiskers and no moustache; Villefort is clean-shaven with the long narrow inverted-triangle face and high forehead. If both read as generic older men in black, the medium-risk lane has failed.
- The Count gives nothing away in any panel. No smile of recognition, no narrowed eye, no visible satisfaction. A legible reaction on his face is a defect.
- Danglars's expensive clothes must fit badly — that is a structural lock, not a costume note.
- The speaker in panel 5 is off-panel; the tail runs off the edge toward that speaker's established side.

## Page 10 — appendix
- Albert / Count lane LIVE again and this is the longest two-hander in the slice. Re-run all five axes panel by panel; drift here typically appears in the third or fourth panel, not the first.
- The plate is forgotten. It sits where it was set and is never eaten from, never moved, never cleared.
- The Count answers a beat late in the dominant panel. That lateness must be visible in staging — his body already turned or still, the answer arriving after Albert has moved on — not merely implied by the words.
- Panel 4 shows the emptied face while Albert remains oblivious. If Albert registers the change, the page's turn is destroyed.
- The Count owns only two balloons on this page. Albert carries the rest. Count them.
- The Count is unrelieved black and Albert pale-waistcoated in every panel; the value contrast is the page's fastest identity check at reduced scale.

## Page 11 — appendix
- Glass and refusal motif, beat two: the plate of apricots is held **level** the entire time and is never lowered. Her hand does not move, including in the 8% panel where the refusal lands.
- Her eyes are on his face, not on the fruit, throughout. An eye-line down to the plate voids the beat.
- She notices. The noticing must be legible on her face in the panel where the refusal is complete — this is the beat the whole later chain depends on.
- He never touches an apricot. No hand near the plate, no reaching, no hovering.
- Mercédès is 42 and must look 42 in every panel including the close framing: lower-lid lines, temple lines, restrained grey in the hair. Youth-washing is a blocking defect here, not a stylistic choice.
- His correction — the recovery after the refusal — must be visible in panel 5. If panel 5 shows the same face as panel 3, the page has no movement.
- Wax red is the accent and the only saturated colour; new gold belongs to the Count's house and must not appear here.

## Page 12 — appendix
- The full glass stands on the table in panels 1, 3 and 4. It is never lifted, never touched, and its level never changes. It must still be visibly full and in focus in the last panel.
- Panel 4 must carry three things legibly at once: the white knuckles, the departing black vertical, and the full glass. If any one of the three is lost to shadow or crop, the panel fails.
- The profile panel is where youth-washing usually occurs. Check her age structure in profile specifically, not just in three-quarter view.
- `*(beat)*` renders as nothing at all. It is staging, not text. No dash, no ellipsis, no empty balloon, no caption.
- The remembered resemblance is never depicted — no inset, no flashback, no younger face, no portrait, no reflection carrying another likeness.
- Panel 2 carries three balloons and 17 words inside a 12% share. This is the tightest lettering lane in the whole slice: verify all three transcribe exactly and comfortably from the 600 × 900 proof without clipping or a confused reading path.

## Page 13 — appendix
- Illustrated prose mode. There are no speech balloons anywhere on this page. A single balloon voids the mode.
- Prose field 1 is set as three paragraphs with the break falling before `But in the winter`. Not one character of the script text may differ, and no words may be moved between paragraphs to balance the block.
- She is still in the same gown as page 12. A change of dress breaks the night's continuity.
- One candle, and only one. The room's light comes from it.
- No flashback of any kind, in any form — no inset, no vignette, no ghosted figure, no younger face in the mirror.
- Her age must be legible twice: in the room and again in the mirror. Both must agree.
- Exactly one reflection. No second reflection, no doubled figure, no mirrored mirror.
- The em dash in the prose is an em dash. Verify it survived setting.

## Page 14 — appendix
- No predecessor page is attached to this page. If the rendering carries visual continuity from page 13 — the same room, the same candle, the same gown — the wrong reference was used.
- Haydée is still dressed from the evening. Not in night clothes, not changed, not with her hair rearranged.
- The Count is still in evening black although it is near dawn. The unchanged clothes against the changed light are the page's whole time-signature.
- The turn to the window **is** the lie. It must read as evasion, not as contemplation or as a man admiring the view. If the body language is serene, the turn has failed.
- Mercédès does not appear in any form, and neither do apricots — no fruit, no plate, no bowl, nothing that reads as the previous evening's object.
- The window and the three lit roofs must match pages 1, 2 and 5 — same aspect, same roofline, same three roofs, now under dawn light rather than night.
- Haydée / Mercédès lane: Mercédès is absent, so the check is one-directional — Haydée must not have drifted toward a French silhouette or a French coiffure under the changed light.

---

## Page 15 — appendix
- **The untouched glass is the page.** The glass in panel 2 must be **full to the
  poured level with a clean unmarked rim** — not half-drunk, not empty, not being
  poured, no hand near it. This is the motif's most important beat: he is in his
  own house with nobody to perform for and he still did not drink it. A drunk or
  partly drunk glass inverts the volume's argument and is blocking.
- **The light must have moved.** The script's whole point in panel 2 is elapsed
  time — a long raking shadow and a second fainter light-stain at a different
  angle. A glass with a single ordinary shadow does not carry the sentence.
- **Only one human being on the page**, small and far, unreadable as a face.
  Any second figure, servant or visitor is blocking; so is a close-up of the
  Count.
- **The room must be poorer in objects than it is rich in scale.** If any family
  object, portrait, book, flower or ornament has appeared, the room's argument is
  gone. One chair only.
- **`old friends` renders upright, unemphasised, without quotation marks,
  asterisks or italics** — the script's asterisks are markup, not content.
- **Mode check:** this is illustrated prose. Two prose fields, no balloons, no
  speaking character. A balloon anywhere on this page is blocking.

## Page 16 — appendix
- **Mercédès must look forty-two.** Temple lines, lower-lid lines and restrained
  grey must be visibly drawn at 600 × 900. A smoothed, youth-washed beauty is a
  blocking defect on this page and is the specific defect inherited from Volume I.
- **Live collision lane: Mercédès / Haydée.** Haydée is not on this page, but the
  failure mode is Mercédès drifting toward her — check for unbound black hair, an
  Epirote silhouette, gold embroidery or a late-twenties face. Mercédès' hair is
  sculpted into formal 1838 dress and her gown is burgundy-black and fitted.
- **Fernand's moustache, receding temples and decorations** must all be present;
  he is the coarser, ruddier, heavier face and must never soften toward the
  Count's clean-shaven pallor.
- **The vertical staging is the meaning.** He is above her on his own staircase
  in all three panels and she is below him. If they are level, or if she is above
  him, the page has lost its turn.
- **The caption is an orientation device and must read as one** — check it
  transcribes exactly, including the em dash, and that it sits over panelling and
  not over a face or the banister.
- **Nothing may telegraph what she nearly said.** No tear, no hand to the heart,
  no significant glance at a portrait, no reaction shot of a servant. Her face is
  closed. If the page explains her, it has failed.
- **Same staircase as pages 6, 8 and 47** — same flight, same rail, same
  proportions.

## Page 17 — appendix
- **Panel 4's smile is the page and it must be in the dominant panel.** A whole
  face open in genuine delight, reaching the eyes, slightly frightening. If the
  Count reads as serene, controlled, or coldly amused, the page has failed its
  turn — this volume's engine is appetite and this is the page that says so.
- **Panel 3 must be genuinely silent and genuinely considering.** No balloon, no
  tail fragment, no caption. If his face there is already dismissive, the flinch
  is gone and the smile in panel 4 becomes ordinary villainy.
- **Text-density risk.** Panel 2 carries 33 words in **20%** of the page — the
  share was raised from 18% at the plan level for exactly this reason, which puts
  it inside Volume I's shipped envelope. Verify by transcription at 600 × 900 that all three of its
  balloons read at full height. **The 22-word script line is deliberately set as
  two linked same-speaker balloons**; both must be present, both tailed to
  Haydée, and no word may be missing. If it came back small, it is REVISE and the
  page goes to the plan owner, not to a type reduction.
- **Two balloons on this page read `No.`** — panel 1 and panel 5, both the
  Count's. Both must be present and correctly attributed.
- **Live collision lane: Haydée / Mercédès.** Haydée is twenty-seven with unbound
  black hair and a loose vertical Epirote silhouette; check she has not acquired
  a sculpted French coiffure, a fitted waist, or a fortyish face.
- **The cloak must be the same cloak** carried over from the night before, put
  down on the table in panel 2 and still there afterwards.
- **No servant, no valet, no third person.** The Count's household is one woman;
  a servant on this page contradicts the volume's design.

## Page 18 — appendix
- **The document's handwriting must be marks, not words.** No legible French,
  Greek or Ottoman word, no readable signature, no readable figure. This is the
  Volume I tiny-prop rule and it is blocking here because the same document
  returns on pages 22, 30, 32 and 33.
- **The red wax seal must be present, broken, and the hottest colour on the
  page.** It carries Volume I's wax motif forward into evidence.
- **Neither hand touches the document in panel 3.** Four hands near it, none on
  it. That restraint is the panel's whole content and the difference between this
  page and page 22, where they both hold it.
- **Draw it to be redrawn:** same size, same fold pattern, same ink layout, same
  broken seal. Note them so the page-22 critic can compare.
- **Panel 4 is appetite badly hidden.** He is trying not to let it show and not
  entirely succeeding. A serene or merely thoughtful face there loses the beat.
- **Live collision lane: Haydée / Mercédès** — twenty-seven, unbound black hair,
  Epirote silhouette, olive-gold.
- **The dominant panel is the document, not a face.** If a face has taken over
  panel 3, the page's architecture has slipped.

## Page 19 — appendix
- **This must not look like Paris, and that is the page's only real job.** White
  limestone, cypress black, Ionian blue, sun-bleached ochre, hard high noon,
  short black shadows, horizontal composition. Any candle amber, gilt, burgundy,
  interior or northern grey is blocking.
- **There must be a real sky, and it must be a large part of the image.** This is
  the only place in the volume with one.
- **The officer has no face and no identifying mark.** No moustache, no
  decorations, no profile, no eye. If a reader can name him on this page, the
  page has spent page 20's reveal early.
- **The fortress must be redrawable** — same wall line, same round tower, same
  lake, same cypresses. It burns on page 20 and returns unburned on page 29.
- **Exactly one string on the page**, `Janina. 1822.`, on ochre parchment against
  plain sky. No signage, no inscription on the gate, no second date anywhere.
- **Mode check:** spectacle. If text or incident has crept above roughly 15% of
  visual attention, or if a second caption has appeared, the mode has drifted.

## Page 20 — appendix
- **Panel 3 is the volume's only frame holding two worlds and there must be no
  border, gutter, line or split-screen device between them.** If a panel edge,
  rule or hard vertical divider has appeared between Janina and Paris, that is
  blocking — the cut is made by composition alone.
- **The two lamps must read as the same lamp.** Same brass body, same glass
  chimney, same height, same handle — one knocked over and burning on the
  pavilion floor far and left, one standing on the black table near and right.
  If they are two different lamp designs, the match cut has not been made and the
  page's central device has failed.
- **The Count's two hands must be tense, fingers spread and pressed down**, with
  no face, head or shoulders in frame. He is inside his own mechanism being fed
  it; relaxed hands lose the only emotion in the frame.
- **The palettes must collide, not blend.** Hot orange and night blue on the left,
  lacquer black and a small pool of lamp-yellow on the right, meeting in the
  middle without a gradient that averages them.
- **Nothing carried through the town is depicted.** No severed head, no body, no
  blood, no procession, no wound. The prose carries it; the picture does not. A
  depiction here is blocking.
- **The mother and the child are silhouettes, clothed and dignified**, too small
  and too far for a face, and are never a spectacle.
- **Text-density risk:** panel 2's field is 48 words in a 25% band. Confirm by
  transcription that it reads at full height and that the pavilion, the lamp and
  the two waiting shapes are still visible as an image and not squeezed to a
  sliver. If the field has eaten the panel, that is a real finding.
- **Mode check:** illustrated prose. Two prose fields, no balloons — Haydée's
  narration is prose here, not speech.

## Page 21 — appendix
- **Restraint is blocking on this page, not advisory.** Check by name: no nudity
  or partial nudity, no chains, ropes or shackles, no platform or auction block,
  no person being handled, displayed or restrained, no crowd looking at anybody,
  no violence, no distress staged for effect. Everyone visible is fully clothed
  and doing ordinary business. If any of these appear, REVISE regardless of how
  well the page is painted.
- **Panel 2 is two hands and nothing else identifiable.** No faces, no bodies, no
  third hand, no crowd, no platform. The subject is the opening space between the
  hands. If any recognisable context has crept in, the dominant panel has lost
  its meaning.
- **Neither hand is gripped or pulled by anyone.** They are coming apart, not
  being separated by a visible person.
- **The market is Constantinople, not Janina** — no lake, no lake-fortress, no
  cypress hills, no fire. Same world, different city.
- **The ledger carries no legible writing** and no readable number.
- **The wax seal in panel 3 is the same dark red as the seal on Haydée's
  document** (pages 18 and 22). That rhyme is the page's only argument and it is
  made by colour, not by dialogue.
- **Exactly one string**, `My mother died in the afternoon. I was eleven.`, on
  ochre parchment, and it must clear 72 px from the bottom edge of the page.
- **Mode check:** spectacle. One caption, no balloons.

## Page 22 — appendix
- **The dominant panel is four hands on one document.** For one image both of
  them are holding it — her hands on the far edge, his on the near. If only one
  person is holding it, the bargain the page is about has not been drawn.
- **The document must match page 18 exactly** — same size, same fold pattern,
  same broken red wax seal, same ink layout — and its writing is still marks, not
  words.
- **Continuity from page 18 is strict:** same evening, same table, same lamp, same
  two chairs, same clothes on both. Pages 19–21 took no time in this room. Any
  change of dress, light or furniture is blocking.
- **This page was split off a denser one, and the split is the fix.** It carries
  three panels and seven strings where it once carried four and twelve. If a
  candidate arrives with a fourth panel, or with `What room?` or any of the trap
  dialogue on it, the builder has rebuilt the page the split existed to retire —
  that is blocking, and it goes back to the plan owner.
- **Panel 3 is the one to transcribe first.** Three balloons, 34 words in 34% of
  the page — inside Volume I's shipped envelope, so read it against the
  transcription test and not against arithmetic. The long middle string
  (`I will not stand at the back of a room…`) is the one at risk; if it needed
  shrinking to fit, the verdict is REVISE and the page goes back for restaging,
  never to a type reduction.
- **Attribution in panel 3:** Haydée owns the first two on the left, the Count the
  third on the right and lowest. Her two must read as one continuous speech and
  his as the answer to it.
- **The Count's face in panel 3 is interested and amused** — a man looking at a
  problem he likes. Not paternal, not indulgent, not grave. The last line is a
  promise he is enjoying making.
- **Live collision lane: Haydée / Mercédès.** She is twenty-seven and was eleven
  three pages ago; the sequence is checkable and the faces must support it.

## Page 23 — appendix
- **Continuity in is the same minute, not the next scene.** Same table, same lamp,
  same chairs, same clothes as page 22, promoted `pages/page-22.png` attached.
  The only thing that has moved is the document, which is now **in the Count's
  hands** and no longer lying on the table. A room that has been reset, relit or
  redressed is blocking.
- **The room he describes must not appear.** No Chamber, no crowd, no three
  hundred men, no doors, no inset, no vision panel. It is spoken and not shown,
  and a page that illustrates it has stopped being a scene between two people in
  the dark.
- **The dominant panel's subject is a man not looking at what he is holding.**
  He has the proof flat under the lamp and his eyes are past it. If he is reading
  the document, the panel has drawn the wrong action and the page has no image.
- **Motif — the engine, and this is the appendix line that most deserves the
  critic's own voice.** Panels 2 and 4 are appetite. The mouth asymmetry does the
  work in panel 4, not a broad smile. **A serene, remote, above-it-all Count on
  this page is blocking**: this is the page where he designs the trap, and if he
  does not enjoy it the volume's engine has been drawn out of its own turning
  point.
- **Haydée in panel 3 is working it out and not liking how simple it is.** Not
  admiring, not frightened, not blank. If she reads as a spectator to his
  cleverness, the page has demoted the person who owns the proof.
- **Attribution is by side and by panel** — Haydée left in panels 1 and 3, the
  Count right in panels 2 and 4. Five balloons across four panels is a light load;
  there is no excuse for an ambiguous tail here.
- **Text density is comfortable and the flag is elsewhere.** The heaviest panel is
  the dominant at 25 words in 46%. Both long strings (panel 2's second and panel
  4's) may take a wide shallow balloon; check they were not condensed instead.
- **Live collision lane: Haydée / Mercédès**, as on page 22.
- **Likely failure.** The four panels flatten into equal bands so panel 2 stops
  reading as dominant, and the page becomes four talking heads in a row.

## Page 24 — appendix
- **Danglars has full side whiskers and no moustache.** This is his primary
  separator from Fernand, who is not on the page but whose moustache the model
  will happily lend him. Also check he has not narrowed toward Villefort's high
  forehead and rigid pallor.
- **The Count never asks for the letter.** Nothing in the staging may show him
  suggesting, dictating, pointing at, or handing over paper. He looks at a brass
  letter-scale in panel 3 and not at Danglars — if he is leaning in or pressing,
  the mechanism of the page is destroyed.
- **Panel 5's blocking is the page:** Danglars writing in the lit half, the Count
  behind him in the dark half turned toward the reader, so **the reader sees the
  face Danglars cannot.** If the Count is beside him, in front of him, or facing
  away, the panel has lost its only idea.
- **The Count's face in panel 5 shows pleasure**, the same appetite as page 2
  panel 4. Serenity there is a defect.
- **The letter is a fresh clean unsealed sheet** — no broken red seal, nothing
  that could be mistaken for Haydée's document, and no legible writing.
- **Text-density risk:** panel 3 carries 27 words in 18% and panel 4 carries 20
  words in 10%. Transcribe both. Small type here is REVISE.
- **Brass is the accent** — the letter-scale, the strongbox, the clock. If the
  room reads as a gentleman's library rather than a machine for counting money,
  the palette's argument is missing.

## Page 25 — appendix
- **The clerk must be anonymous and must not read as Beauchamp or Albert.** No
  small oval spectacles, no untidy sandy hair, no chestnut hair, no pale
  waistcoat, no youth, no open mobile face; middle-aged, shabby brown, face
  turned away or in shadow, silent, no balloon and no tail fragment.
- **Panel 1's balloon includes its single quotation marks at both ends** —
  Danglars is reading aloud — and they are the only quotation marks anywhere on
  the page. Transcribe the string in full: it is 22 words and the longest single
  balloon in this range.
- **Panel 3's face is wounded, not cunning.** Real, offended, hurt indignation. If
  he looks calculating or pleased, the joke the volume is building (he has
  forgotten 1815 entirely) does not land.
- **Nothing on this page may suggest Danglars connects any of it to himself.**
- **`Impartial` renders upright and unemphasised** — no italics, no underline, no
  quotation marks; the script's asterisks are markup.
- **The foreign reply must look foreign and must be a different physical object**
  from the clean sheet Danglars wrote on page 24 — different paper, different
  fold, different hand — and it carries no legible writing.
- **The room must be identical to page 24** three weeks on: same desk, same
  ledgers, same strongbox, same brass letter-scale, same gaslight.

## Page 26 — appendix
- **Live collision lane: the Count / Albert — the volume's highest.** They are on
  the same page in panels 1 and 3. Check all four separators independently:
  chestnut vs black hair, fair-olive vs cold pallor, pale waistcoat vs unrelieved
  black, twenty-two vs forty-two. At 600 × 900 the two panels must not read as
  the same man in two rooms.
- **The printed paragraph must be fully transcribable at 600 × 900.** It is the
  only page in the volume where story logic depends on reading printed matter,
  and the transcription test applies to it exactly as to a balloon. Check
  `FERNAND MONDEGO` is capitalised and that nothing else is.
- **One legible column only.** The neighbouring columns, any masthead, headline,
  dateline or byline must be unreadable texture. A rendered headline or invented
  newspaper name is a string not in the script and is blocking.
- **Two locations, not three.** Panels 1 and 2 are the Count's black room; panel 3
  is the Morcerf breakfast room. If panel 2 has been given a third setting, that
  is blocking.
- **The same physical newspaper appears in all three panels** — same fold, same
  crease, same column layout.
- **Panel 1's mouth carries the page's appetite.** The face is half out of frame
  and what is left must be visibly enjoying itself. A neutral mouth wastes the
  panel.
- **Albert's face is closed, not weeping and not shouting**, and he is in the
  previous evening's clothes — which page 27 depends on.

## Page 27 — appendix
- **Live collision lane: Albert / Beauchamp — the volume's second-highest**, and
  they share every panel. Check all four separators in every panel: hair colour
  (chestnut vs sandy), spectacles (never vs always), costume value (bright pale
  vs dull dark), posture (upright vs stooped).
- **Panel 3 is the collision's weakest moment** — Beauchamp's spectacles come off
  his face. They must be visible in his hand, and the sandy hair, the stoop and
  the worn dark clothes must carry the identification alone. If the two young men
  are confusable anywhere on this page, it is here.
- **Beauchamp's offer must look genuine.** Decent, a little tired, not smug and
  not a trap. His decency is the murder weapon three pages later and the page
  fails if he reads as a schemer.
- **Albert refuses in the dominant panel, on his feet, both hands flat on the
  table.** If the refusal has been staged in a small panel, the page's turn is
  buried.
- **Text-density risk:** panel 2 carries 25 words in 18% and panel 3 carries 23
  words in 18%. Transcribe both.
- **The room must be visibly poorer than every other room in the volume** — no
  gilt, no burgundy, no polish, no candle amber, no lacquer. If it has drifted
  warm and handsome, the palette's one job is undone.
- **The newspaper from page 26 is on the table**, same fold, same crease, and
  carries no legible print.

---

## Page 28 — appendix
- **Mercédès is forty-two and must look it.** Temple lines, lower-lid lines and restrained grey at the temple must be present and visible at 600 × 900. A smoothed, beautiful face is blocking here, not cosmetic — it is the defect this volume inherited from Volume I.
- **Fernand wears no decorations on this page.** He is at home in daylight with the guests gone. Decorations on his chest here contradicts P31 and P34, where wearing them is the point.
- **The newspaper is in Fernand's fist and its type is texture.** If any word on it is legible, that is blocking — the paragraph was already given to the reader on P26 and must not be re-readable here.
- **Left/right lock:** Fernand LEFT, Mercédès RIGHT, in all five panels. Any panel where they swap sides, or where a balloon sits on the wrong side, is blocking — attribution on this page is carried by staging, not tails.
- **Panel 4 is the only panel where she speaks and he does not.** Fernand must have no balloon and no tail fragment in it.
- **The room must read as the Morcerf house in daylight, not at a party** — no candle amber, no guests, no lit chandeliers. The wax-red seals on the desk carry the accent.
- **Panel 5 carries no text at all** and is a very narrow bottom strip; check nothing has drifted into it and that no essential text sits below 72 px from the bottom edge.

## Page 29 — appendix
- **Two locations, and they must not look alike.** Panels 1–2 are Janina: white limestone, hard high sun, sky, horizontal. Panel 3 is Paris: lacquer black, one lamp, no sky. If the Janina panels read as a warm European street rather than a bleached southern one, the cut has failed.
- **Janina is unburned.** This is 1838, sixteen years after the fire. Any flame, smoke, ruin or burning wall is blocking — and the reader must still recognise it as the same town they watched burn.
- **Beauchamp's spectacles are present and legible in both panels he appears in**, and his coat is the same worn dark Paris coat in southern light. No pale waistcoat, no chestnut hair, no upright unmarked posture.
- **No face in panel 3.** Two long pale hands, the lamp, the paper. If a face appears, blocking — this panel's whole rhyme with P26 is the withheld face.
- **The old man carries no reserved identity stack** (no military moustache with receding temples, no oval spectacles with sandy hair, no black columnar evening dress, no raven curls with white shirt and sash).
- **Two prose fields, not three or four.** Field 1 is two paragraphs in panel 1; field 2 is one sentence in panel 2. Sentences scattered into extra boxes is blocking.
- **`JANINA` may appear once as newspaper headline type in panel 3 and nowhere else.** Every other word on that sheet is grey texture. No legible body text on the newspaper.

## Page 30 — appendix
- **Panel 3 — five balloons, the most in the volume.** At 45% the panel has the
  area (53 words over 45 points is a *light* load by Volume I's measure), so the
  risk is not density but **stacking**: four consecutive Count balloons in one
  vertical lane will not fit. They must be staged in two lanes — Haydée's single
  balloon in the left lane, the Count's four distributed down the right lane and
  across the width of the carriage interior. Verify by transcription at 600 × 900
  that all five read, and read in the right order. **If a string fails to
  transcribe, do not drop a string — return REVISE and
  send the page back to the plan owner.**
- **Panel 4 is now 22%, raised from 18% at the plan level**, because four
  balloons and 37 words would not fit the smaller band. Its four balloons are the
  page's fastest exchange and must alternate cleanly between the two speakers.
- **The Count never sets foot on the front steps.** Panel 5 must show him turned toward the narrow side stair at the flank while she climbs the great front steps. Him on the front steps, or entering the main door, is blocking — this is the page that establishes he is at the killing and not in the room.
- **The building must be reusable.** P31's interior is generated with this page attached; the façade, the columns, the front flight and the flank stair must be specific and consistent enough to bind an interior to.
- **The case passes and both hold it at once.** Panel 3 must show his hands still on one edge and hers closed on the other — the deliberate repeat of the night she gave it to him. One pair of hands only on it is a missed beat and is blocking.
- **The appetite is on his face**, not serenity. He is enjoying the telling in panel 3 and admits the timing in panel 4.
- **Haydée is twenty-seven with unbound black hair and no French waist**; Mercédès is not on this page and no figure may drift toward her sculpted coiffure or fitted gown.
- **The caption is a tail-free parchment rectangle, not a balloon**, upper left, and it is the only caption on the page.

## Page 31 — appendix
- **Fernand must be visibly winning.** Warm, upright, plausible, in command of the room; the benches leaning toward him; one peer half out of his seat in panel 4. If he reads as already condemned — hunched, sweating, cornered, guilty — the page has failed its purpose and the volume's climax loses its stake.
- **Full decorations worn to the bar.** Orders, ribbons, wax-red and old gold, polished and displayed. This state must match P34 exactly, where they are still on him in an empty hall.
- **Haydée is not on this page in any panel.** She has not come through the door yet. Any woman anywhere in this room is blocking.
- **The Count is in the gallery only, above the floor, never on it.** And his face must read *hungry*, not worried, not grave, not serene — the panel exists to show him willing his own victim to mount a better defence.
- **Danglars is identifiable and silent:** fleshy face, full side whiskers, **no moustache**, nodding along untroubled. If he is given a moustache he collides with Fernand; if he is given a balloon, blocking.
- **`Go on. Win it.` is a normal balloon at normal size.** Spoken under the noise of the room — but not whispered, shrunk, italicised or given a special balloon shape.
- **Panel 3 is 18% (~276 px) carrying 29 words in two balloons.** Watch this one at 600 × 900: the two balloons were specified side by side across the band precisely so they can sit at full height. If they have been stacked and shrunk to the point where a string will not transcribe, blocking.
- **Panel 1 carries no text.** No orientation caption — the reader arrived with him on the previous page.

## Page 32 — appendix
- **Zero strings. Any legible word anywhere on this page is blocking**, including a date line, a title, a sound word or a signature.
- **Her dress must rhyme with the benches.** Her crimson-and-gold must sit in the same colour family as the crimson of the hall so that she reads as belonging to the room and Fernand, in French black at the far end, does not. If her dress reads as an alien colour note fighting the room, the page's single idea has been inverted.
- **She is alone in the doorway, small, centred, full figure**, with the sealed document in her hand. Not framed heroically large, not lit theatrically, not accompanied.
- **The red wax seal is visible; the handwriting is marks, not words.**
- **The Count does not appear.** No gallery figure, no black vertical, nothing at the rail. He is absent from this page by design.
- **Fernand is tiny at the far end and identified by silhouette** — moustache mass, heavy build, the glint of decorations — not by facial detail.
- **Panel 1's three hundred faces all turn the same way, and every one of them is silent.** No balloons, no tail fragments.
- **This is the volume's single biggest image at 70%.** If the dominant panel does not dominate — if panel 1 competes with it — blocking.

## Page 33 — appendix
- **Panel 4's literal single quotation marks and em dashes are part of the script strings** and must render exactly: `'Received of the merchant El-Kobbir, four hundred thousand francs—'` and `'—for a Christian slave of eleven years named Haydée, and her mother, wife of Ali Tebelen.'` These are the only quotation marks permitted anywhere on the page. Missing quotes, straightened dashes, or a missing accent on `Haydée` are blocking; so is any *additional* quotation mark elsewhere.
- **BLOCKING RISK FLAGGED AT PLAN LEVEL — panel 4.** 18% (~276 px) carrying **three balloons, 28 words**, plus the President and the raised document. Verify by transcription at 600 × 900. If any of the three fails to transcribe, **return REVISE and send the page back to the plan owner** — do not accept a merged or trimmed string. Numeric type size is nonblocking.
- **The document's handwriting is marks, not words**, even though it is held up to the room. Its content is spoken aloud precisely so nothing depends on reading it. Legible handwriting here is blocking.
- **Panel 5: the Count is above and behind, both hands flat on the gallery rail, leaning out.** He must look like a man at a killing he paid for — appetite legible. Fernand below, frozen, decorations on. **Both silent, no text in this band.**
- **Fernand does not speak on this page at all** — no balloon, no tail fragment, in any panel.
- **The President carries no reserved identity stack** and specifically no military moustache, no decorations, no spectacles. He is the only unlocked face on the page and the folded-in Clerk; if he drifts toward Fernand or Beauchamp, blocking.
- **Haydée in panel 3 is near-ground LEFT and Fernand far RIGHT with the whole room between them, in one frame.** If the panel cheats to a cut-together or a shot-reverse, the page loses its dominant image.

## Page 34 — appendix
- **Every decoration is still on his chest.** This is the named object state for this page and it is the entire point of the image: the hall has emptied and nobody has taken them off him. Missing or partial decorations are blocking. Next appearance is on the floor of an empty room, and that beat depends on this one.
- **He is standing, upright, not collapsed.** Not weeping, not slumped on a bench, not theatrical. A heavy upright man left standing because nobody has told him what to do next.
- **The benches are nine-tenths empty and he is small in a very large room.** If the panel closes in on him, the vacancy — which is the content — disappears.
- **Panel 2's doorway is empty.** It is the same great door Haydée stood in two pages ago, now with no figure in it at all. Any figure in that doorway is blocking.
- **Two prose fields, both two-paragraph, cold ivory-grey, and neither over the figure, his chest, or a face.** Declared mode is illustrated prose; if this renders as a comic page with caption boxes, blocking.
- **No speech balloons and no speaking characters.**
- **Same hall, same cold overhead light as P33** — the palette must not warm up as the room empties.

## Page 35 — appendix
- **The volume's second-highest collision lane is live and alone on this page: Albert / Beauchamp.** Check all four separators in every panel — hair colour (chestnut vs sandy), spectacles (never vs always), costume value (bright pale vs plain dark worn), posture (upright vs stooped). If a cold reader could confuse them in any panel, blocking.
- **Beauchamp's spectacles are on in every panel.** Removing them is his P27 gesture, not this page's.
- **Albert's face is closed and hard but his costume value stays bright.** The pale cream waistcoat and coloured neckcloth are load-bearing anti-collision cues and must not be darkened for mood.
- **Beauchamp does not get up** — seated at the table for the whole page, including panel 1.
- **Left/right lock:** Albert LEFT, Beauchamp RIGHT, all four panels, balloons on their owners' sides.
- **`Champs-Élysées` carries its accent and hyphen; `Albert—` ends in an em dash.**
- **The room has no gilt, no burgundy, no crimson, no old gold.** Ink black, newsprint grey, tallow, bare board. If the newspaper office has drifted toward the warmth of the Morcerf house, blocking.
- **Panel 4's turn is Albert understanding *before* he is told** — the recognition must be arriving on his face while Beauchamp is still speaking. If Albert reads as merely listening, the page's turn is not on the page.

## Page 36 — appendix
- **The volume's highest collision lane is live and alone on this page: Albert / the Count, in one frame, in the dominant panel.** Hair colour, skin value, costume value and age must all separate them at 600 × 900. This is the pairing the visual-continuity gate is told to check specifically; a confusion here is blocking, not cosmetic.
- **BLOCKING RISK FLAGGED AT PLAN LEVEL — panel 1.** 15% (~230 px) carrying a single **20-word** balloon. The prompt reserves the upper two-thirds of the band and keeps the figure low; **if the balloon crops or a word fails to transcribe, return REVISE and send the page back to the plan owner.** Do not split the string. Numeric type size is nonblocking.
- **The Count is absolutely still in a moving crowd and the crowd does not touch him.** Everyone else is a loose bright blur of value; he is the one unbroken black vertical with hard edges. If the crowd is rendered as sharply as he is, the page's single visual idea is gone.
- **Panel 2's face carries "the small flat pleasure of the line landing"** — contained, private, not a smile, not serenity. Panel 5 carries **something else**, after the pleasure: not fear, not remorse, the first unplanned thing in nine years. Both faces must be distinguishable from each other. If panel 5 reads the same as panel 2, the page-turn hook is missing.
- **No crowd figure may carry a principal's identity stack** — check specifically for a second black columnar man, a second pale-waistcoated young man with a chestnut side part, or a moustached man with decorations.
- **Panel 3 carries no text** and Albert is silent in it.
- **The line being landed is the untouched glass.** `I ate nothing at your father's table.` is the motif's first use as a weapon; the critic should confirm nothing on the page contradicts it (no food, no glass in his hand here).

## Page 37 — appendix
- **The Count's appetite is switched off and this is the first time in the volume.** Blank, stopped, facing a wall — but **not serene and not peaceful**. If he reads as calm or wise, blocking: the page's turn is that he has no answer and cannot say why.
- **Haydée is in motion and warm; he is still and cold.** The mismatch is the dominant panel's entire content. If both are still, or both animated, the panel has failed.
- **The untouched food here is NOT the enemy's-roof motif.** This is his own house. It must not be staged as the ceremonial full-glass beat from the Morcerf pages — no raised-and-set-down glass, no toast. It is simply a laid table he will not touch.
- **There are no servants in this house.** Any servant, footman or attendant anywhere on the page is blocking.
- **Haydée must not read as a French comtesse** — unbound black hair, loose vertical crimson-and-gold silhouette, no French waist, no coiffure. Mercédès is not on this page; the lane is live for the batch critic because P38 puts her in the same room the following page.
- **Panel 4 alternates sides strictly** — his, hers, his — three short balloons. `Yes.` is one word and belongs to him. If the last balloon reads as hers, the page's ending inverts.
- **The room stays the coldest in the book**: enormous, underfurnished, no fire, no clutter, no portraits.

## Page 38 — appendix
- **Mercédès is forty-two and this page is where it matters most.** Temple lines, lower-lid lines, restrained grey, in the dominant panel at full close-up scale. Youth-washing her here is blocking — she is being looked at by a man who last saw her at nineteen, and the whole beat depends on the years being visible.
- **She is in plain travelling black with a cloak, no jewellery**, hair dressed simply. Not the burgundy-black evening gown — she has come herself, at night, unannounced.
- **Haydée is completely absent, including from reflections.** No crimson, no gold embroidery, no unbound black hair anywhere on the page. Haydée / Mercédès is the live lane here and it is live specifically because Haydée was in this exact room one page earlier.
- **The dominant panel contains two faces and nothing else** — no window, no furniture, no room detail, no third element. If the background carries the black room's architecture, the panel has not been built as specified.
- **`Edmond.` is a normal speech balloon at short-reply size, on her side, in the highest position.** Not display type, not a caption, not italicised, not enlarged, not given a special balloon shape. It owns the page by staging and silence, not by point size.
- **Panel 3 is silent and must show the room making her small without making her less** — she is centred, upright and unhurried in a room that dwarfs her. If she reads as cowed, diminished or lost, blocking.
- **Left/right lock:** Mercédès LEFT, the Count RIGHT, every panel, balloons on their owners' sides; panel 4 alternates hers / his / hers.
- **This is the first time in the volume anyone calls him anything but the Count.** Check that his face registers a man with nowhere to put his own name — not shock played large, and not the appetite carried over from P36.

---

Assembly fragment. Continues the appendix series; use with §1's core brief.

---

## Page 39 — appendix

**Object states carried:** none. No glass, no decanter, no document, no case,
no decorations on this page. If any of them has appeared, say so.

**Motif beats live on this page:**
1. **The poised right hand — opening.** Panel 5 is the volume's one release of
   the Count's signature gesture. The hand must read as a *held, ready* hand
   coming open and empty, not as a shrug, a plea, or a reach toward her. If the
   hand is closed, or is Mercédès' hand, the beat is gone.
2. **`Edmond` as a spoken name.** The dominant panel contains the second and
   third uses of it in the volume. It appears inside a balloon and must not be
   emphasised, enlarged, italicised or coloured differently from the words
   around it.

**Appetite check — the sharpest on the page.** Panels 3, 4 and 5 are the volume's
first sustained absence of the Count's pleasure, and the script names the flinch
it covers. This is the **one** place in this range where a flat, unsmiling Count
is correct. It is still not serenity: he must look like a man being told the
truth about himself, not a man at peace. Report which of the two you see.

**Lookalike lanes live in frame:** Mercédès / Haydée. Haydée is not on this page,
so the risk is one-directional — check that Mercédès has **not** drifted toward
unbound hair, gold embroidery, or a late-twenties face. **Youth-washing is
blocking**, and panel 4 is the largest her face gets in the volume: if the temple
and lower-lid lines are visible in the small panels and gone in the big one,
that is the failure to catch.

**Continuity into page 40:** he is alone at the end of this page. Mercédès must
not appear to be staying.

**Structural note for the critic:** panel 4 is 46%, at the bottom of the legal
band. Confirm it still reads as unambiguously the largest panel; five panels on
a page make a 46% dominant easy to lose.

---

## Page 40 — appendix

**Object states carried:**
1. **The pistol case — shut, his hand flat on the lid.** This is the case's
   first appearance in the volume. It must be a **flat, plain, closed** case.
   **No pistol may be visible anywhere on this page.** If the lid is open, or a
   weapon is on the table, that is a defect: the whole point is a man who has not
   looked inside it.
2. **No glass and no decanter.** He is not drinking, and it is not a scene about
   drinking. If a glass has appeared, the page 44–45 payoff is diluted and this
   is a finding.

**Motif beats live on this page:**
1. **The volume's only writing page.** The sheets of paper carry **no legible
   handwriting** — marks and texture only. Any readable word on a document is a
   defect under the volume's tiny-prop rule, even if it is correct.
2. **`Haydée` spelled with its accent** in prose field 1, and **`1815`** as the
   last thing in it. Both are load-bearing: the date is the volume's spine.

**Prose-page duties:** this is one of the four prose or spectacle pages that
cannot be cut, and its job is to let the reader breathe before the duel. Two
prose fields, one per panel, never scattered. The lower-case `w` opening `what he
had spent` is scripted and correct — **do not report it as a capitalisation
error.**

**Lookalike lanes live in frame:** none — one figure. Instead check the inverse:
**is he alone?** No Haydée, no Mercédès, no servant, no valet. The Count keeps no
household and a servant on this page contradicts pages 38, 44 and 45.

**Continuity into page 41:** the hour. Page 41 is the same night at the other end
of Paris and its caption says so.

---

## Page 41 — appendix

**Object states carried:**
1. **The duelling pistol, in pieces.** It appears in panels 1, 3 and 5 and must
   be **the same weapon, dismantled, in all three** — barrel, lock, rod, rag. It
   is never assembled, never held, never pointed. An assembled or aimed pistol on
   this page is a defect.
2. **Mercédès' travelling black** — the same gown as pages 38, 39, 43 and 48.
   She came straight here from the Count's house. A changed costume breaks four
   pages at once.

**Motif beats live on this page:**
1. **The caption `The same night, at the other end of Paris.`** is the volume's
   only cross-city time-stamp in this range and it must be the **only** caption
   on the page.
2. **She sits down opposite him** in panel 2 — a thing she has not done in this
   room since he was a boy. If she is standing over him, or kneeling to him, the
   panel's meaning is inverted.
3. **She does not soften it.** In the dominant panel there must be **no reaching
   hand, no embrace, no tears** on her side. If the staging has made this a
   comforting scene, that is a finding.

**Lookalike lanes live in frame:** **Albert / the Count — the volume's highest
risk**, live here even though the Count is absent, because this is Albert's
largest solo page and drift compounds. Check all four separators by name:
**chestnut hair, not raven; fair-olive skin several values lighter; pale
waistcoat, bright values; open mobile face.** Also check **Albert / Mercédès as
mother and son** — same wide-set eyes and mouth, thirty years apart. And check
**Mercédès not youth-washed**, which is blocking.

**Palette duty:** this is the Morcerf house at its lowest ebb — burgundy, walnut,
wax red, old gold, candle amber, all of it lit by **one candle**. If it reads as
cold and black it has borrowed the Count's palette and the cut from page 40 has
no contrast.

**Continuity into page 42:** four hours. Albert is at the Bois at eight.

---

## Page 42 — appendix

**Object states carried:**
1. **The pistol case — open in a second's hands**, pistols seated in their
   recesses, **untouched**. Nobody holds a pistol; nothing is loaded, raised or
   aimed. This is the same class of flat case as page 40 and pages 45–47.
2. **Albert's hat, off and in his hand** from panel 2 onward. Uncovering himself
   is what makes the withdrawal public. If the hat is on his head in panel 2 or
   4, the beat is gone.

**Motif beats live on this page — the biggest one in the range:**

**The Bois must have air in it.** This is Volume I's "the ending" palette
borrowed early and deliberately, and it is **the only place in this volume where
the world breathes**: pale grey-green, standing mist, wet black trunks, thin gold
at the horizon, open distance, visible sky. Judge this one hard and say so in
your report. **If this page reads as another dark Paris interior — walls, gilt,
candlelight, low values, no sky — that is a finding**, and it is a finding even
if every other element on the page is correct, because pages 42, 43 and 44 are
the volume's only relief and they only work as a set.

**Lookalike lanes live in frame:** **Albert / the Count**, both present in panel
1 and separated at small scale by silhouette alone. At the size they occupy, the
separation must survive: one is black-clad, pale, motionless and apart; the other
is chestnut, warmer-skinned, lighter-dressed and moving.

**Reserved identity stacks — check every unnamed figure.** Two seconds and a
surgeon are on this page. **None of them may carry a heavy iron-black military
moustache with receding temples (Fernand), unrelieved black with swept-back hair
and pallor (the Count), small oval spectacles with untidy sandy hair
(Beauchamp), or a bright pale waistcoat on a young man (Albert).** A witness
wearing a principal's silhouette is a real defect here, not a nitpick — the
reader will spend the panel wondering who he is.

**Speech ownership:** three balloons, two owners. The Count is present and
**silent**; confirm he has no balloon and no tail fragment.

---

## Page 43 — appendix

**Object states carried:** the field's furniture from page 42 — the closed
carriage, the surgeon's bag still shut, the witnesses' coats — must be the same
objects in the same clearing. **Mercédès' hired carriage in panel 1** is a second,
plainer vehicle at the far edge of the field; it must not be confusable with the
seconds' carriage.

**Motif beats live on this page:**
1. **The Bois still has air in it.** Same standard as page 42. The dominant panel
   is the volume's only wide open horizon with people walking *into* it.
2. **The Count with no line ready.** Panel 3 is the only frame in the volume
   where he starts to speak and is stopped. The half-lifted, arrested poised right
   hand carries it. If he looks composed and in command here, the panel has
   failed.
3. **He is absent from the dominant panel by design.** Panel 4 must contain **no
   black figure at all.** If the model has put him in the frame — even distantly,
   even watching — that is a finding, because the point of the panel is that they
   walk away and leave him out of it.
4. **`Mercédès Herrera`** — the maiden name, spelled with its accent, is the
   volume's payoff for Albert's arc. Check it letter by letter.

**Lookalike lanes live in frame:** **Albert / the Count share panel 3** at close
range — the highest-risk pairing in the volume, in its most dangerous framing.
Name all five separators in your report: hair colour, skin value, costume value,
age, default expression. Also **Mercédès not youth-washed**, including at panel
1's small background scale and in panel 4 where she is seen from behind.

**Speech ownership — the specific hazard:** in panel 4 **both figures have their
backs turned** and one balloon must belong unmistakably to Albert. If a reader
could attribute `I'll take my mother's name...` to Mercédès, that is blocking
attribution failure under the core brief, and this appendix flags it as the most
likely place on the page for it to happen. In panel 2 the balloon's tail runs
**off-panel** toward Albert, who is out of frame; confirm it does not appear to
belong to a second or the surgeon.

**Reserved identity stacks:** same check as page 42 for the seconds and surgeon.

---

## Page 44 — appendix

**Object states carried — the most important in the range:**
1. **The decanter and one glass, panel 3.** Set down **by the Count's own bare
   hand**, squared to the edge of the low black table, hand already withdrawing.
   **It must be his own hand: no glove, no tray, no servant's arm.** He has no
   household, and that is why he does it himself.
2. **Nobody has drunk anything.** The decanter is stoppered and full; the single
   glass is empty and dry. **One glass only.** If there are two glasses, or the
   glass is filled, page 45's payoff is pre-empted and this is a finding.
3. **These two objects must be redrawable on page 45** in the same positions.
   Page 45 attaches this page as its predecessor.

**Motif beats live on this page:**
1. **The palette drains from air back into lacquer** across three panels: Bois
   grey-green → cold grey suburb daylight → lacquer black. If panel 1 is not
   noticeably more open and higher-valued than panel 3, the page's shape is lost.
2. **`what he arrived at was not relief`** ends prose field 1 and **`would be at
   his door before dark`** ends prose field 2. Both are the page's whole
   argument; check them character for character.
3. **He has not moved from where he was told to stand.** Panel 1's figure is in
   the exact spot, feet together, while both carriages leave. Not walking, not
   turning away.

**Appetite check:** panel 2 is the flinch closing. He must look like **a man
doing arithmetic**, not a man grieving or repenting. Grief on this face
contradicts the prose above it.

**Lookalike lanes live in frame:** none — one figure, and no unnamed figures at
all. Instead confirm **nobody else is on this page**: no coachman's face, no
servant, no Albert, no Mercédès.

**Known, script-authorised architecture note — do not raise it as a defect.**
This page stages the Bois, the road back, and the black room. Treat the Bois and
the road as **one continuous journey**, which puts the page at **two locations**
and inside the ≤2 blocking limit. `07-PAGE-CONTRACT.md` records this page as one
location; `08-FULL-SCRIPT.md` is the stated authority where the two drift, and
the script stages all three. **Report it as noted, not as blocking**, and let the
production lead decide.

---

## Page 45 — appendix

**This page is the payoff of the volume's primary motif. Judge it first and
report it first.**

**Object states carried — the untouched glass, resolved:**

| Where | State the reader has been shown |
|---|---|
| P8 | Fernand toasts him; he raises the glass, holds it, **sets it down full** |
| P11 | He refuses Mercédès' apricots, and **she becomes certain** |
| P12 | The full glass sits between them the whole scene |
| P15 | A poured glass nobody drank, **in his own empty house** |
| **P45** | **In his own house, with Fernand in front of him, he pours and drinks it empty** |

1. **The drinking must be physically legible as an action, not an incidental
   prop.** In the dominant panel the reader must be able to see the sequence
   without a caption: **the decanter unstoppered and wine going into the glass →
   the glass at his mouth, head tipped, throat working → and in panel 4 the same
   glass standing empty on the black wood.** If you cannot narrate those three
   states from the 600 × 900 proof, **the page has failed regardless of anything
   else on it**, and that is the finding to lead with.
2. **One glass.** No second glass is poured, offered, or present. Fernand is
   given nothing.
3. **The decanter and glass are inherited from page 44 panel 3** and must be the
   same objects.
4. **Panel 4's glass reads unambiguously as emptied** — drained, a red film in
   the bottom. Not full, not half, not absent.

**Motif beats live on this page:**
1. **`This is my roof.`** is the sentence the entire motif exists to deliver.
   Check it character for character and confirm it is the last balloon on the
   page.
2. **The wet grass and mud of the Bois still on his boots**, and the same coat.
   He has not been home long enough to change; this dates the scene to hours
   after page 44 without a caption.
3. **Fernand's decorations are gone** — no orders, no ribbons, no wax red on him
   anywhere. The wax-red accent has left the Morcerf side of the book and does
   not return until it is on the floor on page 47.

**Appetite check:** this is not a serene page. He is enjoying being asked to duel
and refusing; the poised right hand, the unhurried seat, the crossed leg. If he
reads as weary or merciful, that contradicts pages 44 and 46 on either side.

**Lookalike lanes live in frame — `Fernand / the Count`, at close range, for the
whole page.** He is **46 and aged twenty-three years off his 1815 lock — the
hardest identity job in the volume.** Check by name:
- **the heavy iron-and-black military moustache**, present in every panel he is
  in — its absence is blocking;
- **the receding temples with iron-grey at the sides** — likewise;
- **weathered ruddy-olive skin, coarser and several values warmer than the
  Count's pallor**;
- **heavy build against the Count's columnar slimness.**

**He must not soften into a generic older man**, and **he must not collide with
Danglars** — Danglars is fleshy with **full side whiskers and no moustache**,
short and thickening, in expensive clothes that fit badly. If the man in this
room could be either of them, that is blocking.

**Reference discipline:** Danglars' sheet is a prohibited input here. If the
builder's ledger shows `06-danglars-1838.png` attached, report it.

---

## Page 46 — appendix

**This is the page the whole volume is aimed at. Its geometry is the appendix.**

**Geometry commitments — check each:**
1. **The dominant panel is one face, 46%, and nothing else.** The Count's head
   and shoulders edge to edge, **Fernand not in the panel**, no furniture, no
   window, no glass, no room detail. If a second figure has entered it, or the
   face has been pulled back to a two-shot, the page's whole design is gone.
2. **`I am Edmond Dantès.` has its own clean lane** and nothing overlaps it. It
   is the last balloon of the four-and-a-half-page sequence the book was built
   to reach. Check the accent on `Dantès` in **both** this string and panel 1's
   `Do you know the name Dantès?`
3. **Neither balloon in the dominant panel crosses his face.** The panel is a
   face; a balloon over it defeats it.
4. **Panel 5 is 6% and carries no text.** It is legally under the dominant-panel
   rule because panel 4 carries the page; do not report the small share as an
   architecture defect.

**Object states carried:**
1. **The pistol case, panel 3 — open? No: forgotten under his arm.** He stood up
   and forgot he was holding it. It is not opened, not offered, not set down in
   this panel.
2. **Panel 5 — the case is gone.** The marble top is **bare**, with one clean
   rectangle in the dust where it stood, and the doorway is empty. **This absence
   is the page's entire ending and it is the setup for page 47.** If the case is
   still on the marble, page 47 has no cause. If a figure or a shadow is in the
   doorway, the exit is spoiled.
3. **The emptied glass and stoppered decanter from page 45** are still on the low
   black table wherever the room is visible.

**Motif beat:** `Pharaon` is a ship's name. The script marks it italic; the
volume's typography bans the thin italic serif that a failed run rendered at 27
px, so it is lettered in **the same upright hand as the rest of the balloon**.
**Do not report the absent italics as a script-fidelity defect** — but **do**
report any rendered asterisk, underline, quotation mark, or font switch around
it, all of which are defects.

**Speech ownership — the page's one attribution hazard:** **every balloon on this
page belongs to the Count, and Fernand does not speak at all.** Eight strings,
one owner. Panel 2 is Fernand's face carrying three of the Count's balloons with
tails running **off-panel to the right**. If any of those three reads as
Fernand's, the page inverts: the man being accused would appear to be confessing.
Transcribe panel 2 with particular care and say explicitly who you believe is
speaking in it.

**Lookalike lanes live in frame:** `Fernand / the Count`, same four separators as
page 45 — moustache, receding hairline, skin value, build — now at the largest
scale either face reaches in the volume. Also confirm the Count has not drifted
toward **Villefort's** long narrow inverted triangle and very high forehead in
the full-frame panel; that collision forced a full reference redesign in Volume
I, and a big frontal face is where it would reappear.

---

## Page 47 — appendix

**Object states carried:**
1. **Fernand's decorations — on the floor of an empty room.** Their last state
   in the volume: P8 worn and polished, P31 worn to the bar of the Chamber, P34
   still on his chest in an emptying hall, **P47 on the floor.** Orders, ribbons,
   wax-red seals and old gold, emptied out and left. This is the wax-red accent's
   final appearance and it must be **on the floor**, not on him and not in a box.
2. **The jewel cases open on the table with everything still in them.** The
   jewels are **not** taken. If the cases are empty, the caption is contradicted
   by the art and the page means the opposite of what it says.
3. **The wardrobes standing open and emptied**, drawers pulled out, a woman's
   gown across a chair.
4. **The pistol case — open in his hands** in the dominant panel. It is the same
   case he carried off the marble top on page 46.

**Motif beats live on this page:**
1. **The Morcerf house reversed.** Same burgundy, walnut, wax red, old gold and
   gilt, **now cold**: dusk, no lamps, no candle amber, the gilt gone grey. It
   must be recognisably the same overstuffed house from Movement II and it must
   have stopped working. If the room is merely dark and generic, the reversal has
   not happened.
2. **The general's staircase — unlit and empty, with him climbing it alone**, and
   the front door standing open behind him with nobody to shut it. Its states:
   P6 lit and crowded, P8 the Count climbs it beside its owner, P16 its top very
   late, **P47 unlit with Fernand alone on it.** It must be the same staircase.
3. **The caption `His wife and son had taken nothing of his.`** names its
   antecedent — the jewels visible in the same panel — and it is answered on the
   next page by `We could have taken the plate.` Check it character for
   character; it is the only caption on the page.

**The death is off-panel and must stay off-panel.** Panel 3 is the façade from
the street with **one upstairs window flat white for the length of the panel**,
and a `CRACK` sound label on the masonry beside it. **Blocking if present: a
body, a wound, blood, a figure in the window, a silhouette inside the light, a
muzzle flash, smoke, or a discharging weapon.** There is nothing inside that
window. Report explicitly that you checked for each.

**The sound label is the third text level.** `CRACK`, capitals, plain, set flat
on the masonry — **not a balloon, not a caption rectangle, not jagged, not a
starburst, not a comic-display face, not colour-outlined.** It is the only
capitalised string in this page range.

**Spectacle-mode duty:** text under 15% of visual attention — one caption and one
label, nothing else. **Fernand does not speak.** Confirm no balloon anywhere.

**Lookalike lanes live in frame:** `Fernand / Danglars`. He is alone here, ruined,
in a house full of soft furnishing, which is exactly the condition in which the
model drifts him toward a fleshy side-whiskered banker. **Moustache and receding
hairline, both panels.** He must not soften into a generic older man.

**Continuity into page 48:** the façade, the shutters, and **the exact position
in that façade of the window that goes white.** Page 48's dominant panel shows
the same window, dark. Page 48 attaches this page to get it.

---

## Page 48 — appendix

**Object states carried:**
1. **One small bag between them, and nothing else.** No trunks, no boxes, no
   loaded carriage roof, no jewel case. **The emptiness of their hands is the
   page** and it is what makes page 47's caption true.
2. **The window that was white on page 47 is dark again**, in the identical
   position in the façade. This is the page's single most checkable continuity
   fact.
3. **The house is entirely dark** — no lit window anywhere in it. If any window
   in that building is burning, the shot has been survived and the page is
   wrong.
4. **Mercédès' travelling black** — the same gown as pages 38, 39, 41 and 43.

**Motif beats live on this page:**
1. **`He bought it in 1821, from a dealer in the rue Vivienne. There was no
   grandmother.`** — the purchased-legitimacy argument of the whole Morcerf house
   collapsed into one line. Check `rue Vivienne` and the date.
2. **Nothing else in the street has changed.** In the dominant panel the carriage
   stands where it stood, the lamp burns, nobody comes out, no shutter opens, no
   light goes on. **A street reacting to the shot is a finding** — the point is
   that the city absorbs it without noticing.
3. **Her hand stops him, it does not comfort him.** Panel 4 is a grip on his
   forearm holding him **exactly where he is**. If it reads as an embrace or a
   consoling touch, the panel's meaning is inverted.
4. **Neither of them goes in, and neither is shown grieving.**

**Speech ownership:** eight strings, two owners, and the exchange alternates
every panel. Panel 3's `Mother—` / `I know.` is the pair a reader is most likely
to mis-assign, because both faces are turned up and away. Say explicitly who you
believe speaks each of those two.

**Lookalike lanes live in frame:** `Albert / the Count` — the Count is not on
this page, so check for **drift**: Albert must still be chestnut, fair-olive,
light-costumed and open-faced under gaslight, which flattens colour and is where
he most easily goes raven-haired and pale. Also **Mercédès not youth-washed**,
and **Albert and Mercédès still reading as mother and son.**

**Absences to confirm:** no Fernand, no Count, no body, no crowd, no gendarme, no
servant, **and no sound label** — the sound belonged to page 47 and must not be
repeated here.

---

## Page 49 — appendix

**The last page of the volume. Its job is a rhyme, and the rhyme is checkable.**

**The page-01 rhyme — the appendix's main item:**

Page 1 ended on **three roofs at rooftop level, close enough to count**, each with
a lit window: **left, a roof with a copper gutter; centre, a roof with a
flagpole; right, a roof with every window lit.** They were the only warm thing in
the Count's world and they were all other people's houses. Page 2 named them:
**the copper gutter is the banker; the slate roof with the flagpole is the King's
Attorney; the one that entertains is the third.**

1. **Panel 3 must be the flagpole roof.** A **slate roof with a flagpole on it**,
   seen from the street instead of from his window, with **one lit window on its
   second floor** and the rest of the house dark. **If it is the copper-gutter
   roof, or a generic Paris roofline with no flagpole, the volume's closing
   rhyme fails** and the caption is pointing at nothing. This is the finding to
   lead with. Compare against page 1 directly if you can.
2. **The shuttered house on the left of the dominant panel is the third roof —
   the one that entertained, every window lit — now black.** It does not need to
   be labelled, but it must be dark.

**Object states carried:**
1. **The departing carriage lamp — the last warm thing in the volume, leaving.**
   Small, deep in the perspective, **moving away from the frame**, its reflection
   stretched toward us on the wet cobble. If the carriage is arriving, stationary,
   or large in frame, the page's one image is gone.
2. **The one lit window on the second floor** in panel 3, with **no figure and no
   silhouette in it.**

**Motif beats live on this page:**
1. **He has been standing there the whole time.** Panel 1 is the reveal that he
   watched page 48 happen. He is **not** hiding, crouching, or lurking — he is
   standing on the far pavement, and nobody in the street noticed him.
2. **Identity by silhouette, exactly as on page 1** — a tall slim man in unbroken
   black with a swept-back dark head, small and distant, face barely readable or
   not readable at all. **No other figure on the page may carry that
   silhouette**, and there should be no other figure at all.
3. **`One.`** — one word, and it is the volume's verdict on a man's death. The
   balloon must still be **240–390 px** wide; a balloon shrunk to the size of the
   word will not survive the 600 × 900 proof, and this is the single likeliest
   transcription failure on the page.
4. **`Villefort, the King's Attorney, kept late hours.`** — the volume's last
   string and the hand-off to Volume III. Check the capitals and the apostrophe.

**Appetite check — the last one in the book, and the point of the whole volume.**
He has just paid for it and it did not slow him down. What is on this page is a
man **looking up at the next roof before the carriage is out of sight.** If the
staging reads as remorse, exhaustion, mourning, or a man taking his leave of the
story, the ending has been inverted and that is a finding.

**Spectacle-mode duty:** text under 15% of visual attention — one balloon, one
caption, nothing else.

**Forbidden on the final page:** any end-of-book flourish — vignette, fade,
decorative border, title card, `FIN`, `THE END`, credit line, signature, or page
number. Also no second figure in the street, no visible Mercédès or Albert, no
body, no crowd, no gendarme.

---

*End of appendices, pages 39–49.*

---

# 7 · Revision and promotion

## What triggers a redraw

Only an independent critic's **REVISE**, and only against the **mandatory
defects it named**. Nothing else. Not the builder's taste, not a second opinion,
not a feeling that the page could be prettier.

## How a redraw is done

- **Redraw the whole page**, from the approved references and the promoted
  previous page, against the named defects only. Increment the version.
- **Never patch.** No balloon, tail, hand or object is composited onto a
  flattened page. A patched page is not a page; it is a page plus a lie about how
  it was made, and the next page will inherit the lie as an image input.
- **Never feed a rejected candidate back in as a generation input.** The vK+1
  prompt attaches exactly what the v1 prompt attached: `refs/approved/` sheets
  and the promoted previous page. A rejected candidate is evidence, and it stays
  in `candidates/` forever — but it never becomes an ancestor.
- **Nothing is deleted.** Every rejected candidate keeps its prompt, its audit,
  its two proofs and its critic report. That archive is also what makes the rule
  above checkable by inspection rather than by trust.
- **Never fix a defect by shrinking type or by lowering the ambition of the
  page.** If the text will not fit, restage the panel or split the page. An extra
  page is cheap. There is no page budget that outranks readability.

## The v4 ceiling

If **v4** of a page still returns REVISE, **the composition has failed.** Do not
generate a v5 against the same design.

**The count is total generations of the page, from v1, and it never resets.** A
redesign, a restaging, a new panel plan, a split proposal, a fresh prompt or any
other relabelling does **not** start a new count. Version numbers are sequential
across the whole page: the fourth image ever generated for page N is v4, whatever
it is called. **Four generations of a page, under any label, stops the run and
comes to the owner.**

This clause exists because the ceiling was silent on relabelling and page 8
reached **v14** without ever formally hitting it — six redesigns, six resets. A
stopping rule the executor can rename is not a stopping rule.

The owner decides whether the page geometry is redesigned or the story is split
in two. The executor does not choose or implement either path autonomously and
does not modify `07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`.

The builder may **not** redesign a page.

**Owner instruction, 2026-08-16 — the autonomous-redesign authorization is
REVOKED.** A genuine v4 ceiling **stops the run and comes to the owner.** The
executor does not redesign a page on its own initiative.

That authorization was granted earlier the same day and withdrawn within hours,
because of what it did to page 8: six autonomous redesigns, fourteen candidates,
and a page that grew 5 → 6 → 8 → 7 → 9 panels. **Every redesign subdivided; not
one of them split the page**, though splitting is the first option named above
and an extra page is cheap. Page 8 finished as the only page in the volume
outside the 2–5 panel range.

**When a page resists, propose the split.** After three independent critic
failures, propose a split to the owner before adding a sixth panel. Adding
panels to a page that is already too full is compression, and compression is
the tax paid for refusing to cut.

**Never edit `08-FULL-SCRIPT.md` or `07-PAGE-CONTRACT.md` to make a generation
behave.** Compensation numbers — deliberately exaggerated shares meant to
counteract the model's shrink — belong in the page prompt and nowhere else. Page
8's script and contract were polluted with a fabricated 62% dominant that no
candidate ever rendered; the real value was 42%.

## Promotion

On an unconditional **APPROVED** only. In this order, every time:

1. Copy bytes: `qa/production/page-NN/candidates/page-NN-vK.png` → `pages/page-NN.png`.
2. **Verify SHA-256** of source and destination match. A promotion whose hash
   does not match is not a promotion.
3. Derive the two promoted proofs at 600 × 900 and 768 × 1152.
4. Append the ledger row.
5. Release page N+1.

Nothing is promoted on a conditional approval, on a self-approval, or on a
verbal one. There is no verdict called "approved with minor notes"; if there is
a blocking finding, the verdict is REVISE.

## The holds

Production **stops** at each of these and does not continue until it clears.

| Hold | When | Clears on |
|---|---|---|
| **Reference gate** | before page 1 | all sheets promoted to `refs/approved/`, unconditional |
| **Batch sequence** | after pages 10, 20, 30, 40, 49 | batch critic returns APPROVED |
| **Blind cold read** | after pages 10, 20, 30, 40, 49 | read completed and its defects triaged |
| **v4 ceiling** | any page whose v4 returns REVISE | **stop and come to the owner** with a split proposal; the executor does not redesign |
| **Visual continuity** | after any redraw chain of 3+ consecutive pages | continuity pass returns APPROVED |

A batch hold blocks the **next** batch. It does not un-promote a page unless the
defect is consequential — a page that reads correctly on its own and drifts only
cosmetically stays promoted and is noted in the ledger.

---

# 8 · Ledger template

## The running production ledger — `qa/production-ledger.md`

One row per **promoted** page, appended at promotion, never edited afterwards.

```
| Page | Mode | Versions | Promoted vK | SHA-256 (first 12) | Gate rounds | Notes |
|------|------|----------|-------------|--------------------|-------------|-------|
| 01   | prose | 1       | v1          | 3f9a1c0b7d42       | 1           |       |
```

- **Mode** — `dramatic`, `prose`, or `spectacle`, as declared in §5. If the
  promoted page renders a different mode than the one declared, it should not
  have been promoted.
- **Versions** — how many candidates existed, including rejected ones.
- **Gate rounds** — how many times the critic was run on this page.
- **Notes** — only what a later gate would need: a lookalike that nearly
  collided, an object state that had to be corrected, a page that came close to
  the v4 ceiling, a deviation the critic accepted and why. Not praise, not
  process narration.

## The per-page QA folder

```
qa/production/page-NN/
  prompts/page-NN-vK.md        the exact prompt, written to disk BEFORE generating
  candidates/page-NN-vK.png    every candidate, kept forever
  audit-vK.md                  the builder's own essentials audit
  proofs/page-NN-vK-600.png    desktop proof — the one the critic transcribes from
  proofs/page-NN-vK-768.png    tablet proof
  critic-vK.md                 the independent critic's report, with its full transcription
```

## Batch, cold-read and continuity artifacts

```
qa/batches/batch-01-10.md   batch-11-20.md   batch-21-30.md   batch-31-40.md   batch-41-49.md
qa/cold-reads/cold-read-10.md   cold-read-20.md   cold-read-30.md   cold-read-40.md   cold-read-49.md
qa/continuity/contact-sheet.png   continuity-pass.md
qa/whole-book.md
```

---

# 9 · Failure watchlist — run this on yourself every ten pages

Each item is a documented cause of a failed run of this exact method. Run the
list at the batch boundaries — pages 10, 20, 30, 40 and 49 — and write the
results into that batch's file. A watchlist that is never written down is a
watchlist that was never run.

**1 · Is the gate looking?**
Grep the last ten critic reports for readability vocabulary:

```bash
grep -ril -E 'legible|crowded|dominant|confusing|ambiguous|who is speaking|too small|hard to follow' qa/production/page-*/critic-*.md
```

**Zero hits across ten pages means the gate has drifted into string checking.**
That is not a good sign; it is the failure. In the abandoned run, across 74
critic reports, *too small*, *dominant panel* and *too many panels* appeared zero
times while three generations were spent on an em dash.

**2 · Are references still being attached as images?**
Or has the run quietly degraded to prose locks while the ledger still says the
inputs were resolved? Open the last three prompts on disk and check the
reference manifest against what was actually passed to the tool.

**3 · Are rejected candidates being fed back in?**
Every vK+1 prompt must attach only `refs/approved/` sheets and the **promoted**
previous page. Check the last redraw by inspection.

**4 · Has any page been patched rather than redrawn?**
A composited balloon or a pasted hand is a silent corruption of every page after
it, because the next page attaches it as an image input.

**5 · Is anyone measuring lettering at all?**
Nobody should be, at any size. Under the owner's 2026-08-15 instruction — **NO
SWEATING ABOUT TEXT SIZE** — the type numbers are builder instructions and the
transcription test is the gate. A REVISE that cites glyph height while its own
transcription succeeded is void — strike it and re-judge the candidate without
it. This is the failure that took page 1 to a v4 ceiling.

**6 · Has the register drifted?**
Put page 1 and the newest page side by side. Velvet Cinema: layered matte
gouache and opaque watercolor over sparse charcoal and ink construction, broad
visible brushstrokes, bold shadow masses, tactile materials. **Not smooth
prestige-oil realism.**

**7 · Is the critic returning conditional approvals?**
There is no such verdict. "Approved with minor notes" is a REVISE that lost its
nerve.

**8 · Is the Count still hungry?**
The appetite is the engine of this book. Look at the last ten pages together: if
he reads as serene and above it all for pages at a stretch, the engine has been
drawn out of the volume even though every individual page passed. Nothing else on
this list will catch that.

---

# 10 · Handing this plan to an executor

Deliver `12-PRODUCTION-PLAN.md` together with the whole `monte-cristo-vol2/`
folder — the script, the character ledger, the settings doc, the reference plan,
the critic operations file and the topology file are all cited by this plan and
travel with it.

Then say, close to verbatim:

> Execute `monte-cristo-vol2/12-PRODUCTION-PLAN.md` literally. You are the
> production lead for a 49-page illustrated novel. Bill image generation to the
> **ChatGPT subscription (Codex in-app)** — the OpenAI API path is not approved
> for this run; if you cannot generate in-app, stop and ask rather than falling
> back. Clear the reference gate in section 4 before page 1: no page generates
> until every character visible on it has an approved permanent lock in
> `refs/approved/`. Use the builder and critic briefs in section 6 verbatim, **as
> separate agents** — a critic simulated inside the builder's own context
> approves its own work. **Submit every completed candidate to the critic; your
> self-audit is a report, not a verdict, and you may regenerate without a verdict
> only for a failed generation — wrong canvas, corrupt file, gross anatomy
> breakage.** Do not redesign any page: a v4 ceiling stops the run and comes to
> the owner. Never edit the script or the page contract. Do not
> generate prototypes — every generated
> page is a production candidate with a direct path into the finished book. Start
> at page 1 and do not start anywhere else. Stop at every hold.

Those last five sentences each correspond to a documented failure of this method.

## Self-containment check

- [x] Every page prompt in full, no placeholders — §5, pages 1–49.
- [x] The numeric typography law, as builder targets — §3.
- [x] The transcription test, inside the critic brief — §6.
- [x] The page-architecture blocking criteria — §3 and §6.
- [x] Each page's mode, dominant turn and dominant panel share — §5, page headers.
- [x] A per-page critic appendix for **every** page — §6, pages 1–49.
- [x] Followable by an executor who has never read the source novel — §5 carries
      every rendered string; no prompt requires knowledge of Dumas.
- [x] The billing decision stated, not left open — §2.
- [x] Builder self-audit is non-gating; every completed candidate reaches the separate critic — §1, §6, §7.
- [x] Autonomous redesign is revoked; a v4 ceiling stops for owner direction with a split proposal — §1, §7, §10.
- [x] The page contract and full script are owner-controlled and never carry generator compensation — §1, §7.
