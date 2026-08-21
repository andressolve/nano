# PRODUCTION PLAN — The Count of Monte Cristo, Volume II

**49 portrait pages. Paris, 1838.**

> **Remaining-run override — 2026-08-21.** Pages 1–32 are canonical. Pages
> 33–49 use the intent-first architecture in
> `14-INTENT-FIRST-BUILDER-CRITIC-RULES.md`: individually rewritten builder-only
> prompts, separate page intents and numbered critic cards, a blind critic that
> never sees the generation prompt or builder audit, and the targeted → clean
> prompt reset → resistant-defect hold router. Production starts from
> `SESSION-START.md`, not from this large assembled plan. Where older general
> prose below conflicts with current Sections 6–7 or the compact `qa/_run/`
> packets, the current sections and compact packets govern Pages 33–49.

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
| **Builder** | generate one completed candidate, record a non-gating audit, derive proofs, submit every completed candidate to the critic | approve, promote, write to `pages/`, gate its own work, reroll without a critic verdict except for a failed generation |
| **Critic** | read, transcribe, judge, return a verdict | edit, regenerate, promote, propose prompt wording |
| **Production lead** | release a page, promote bytes, hold a batch, bring a v4 ceiling and split proposal to the owner | generate, approve their own generation, autonomously redesign after v4, modify the page contract or full script |

Run the critic as a **genuinely separate agent**. A critic simulated inside the
builder's context approves its own work.

## Standing rules

1. **The builder may not redesign or gate a page.** Every completed candidate is
   audited, proofed and submitted to the independent critic. The audit records
   findings; it is not a verdict.
2. **Pages 1–32 are canonical.** The remaining run starts at the first
   unpromoted page inside the bounded current session; Page 33 is next.
3. **There are no prototypes.** Every generated page is a production candidate
   with a direct path into the finished book.
4. **One page in flight at a time.** Do not generate or prepare an alternate
   candidate while the critic reviews page N.
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
12. **Production roles open only compact `qa/_run/` packets.** A fresh builder
    and fresh critic are created for every candidate. The critic's blind
    entrypoint is separate from its script/intent/card packet and never exposes
    the generation prompt or audit. The batch orchestrator covers only Pages
    33–40 or Pages 41–49 and never opens images or the large plan.

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

**Reader turn:** Haydée testifies; Fernand is finished; the Count watches the
killing he arranged.

Build five clearly ordered moments in the same occupied Chamber of Peers. Keep
Haydée calm and still, Fernand heavy and decorated, and the Count a clean-shaven
black vertical above the hall. The President is an older balding French
official, visually distinct from Fernand and the Count.

1. Haydée alone at the bar, hands empty: `My name is Haydée. My father was Ali Tebelen, Pasha of Janina.`
2. The President half-risen: `Mademoiselle. Do you know the accused?`
3. The dominant image holds Haydée and Fernand in one continuous frame with the
   whole crimson hall between them. All three balloons belong to Haydée, in
   order: `He is fatter.` / `He was an officer of my father's guard.` / `He had the keys of the eastern gate, and he ate at our table for two years.`
4. The President raises and reads the large folded document. Its handwriting is
   unreadable texture; the evidence is spoken. His three balloons, in order:
   `'Received of the merchant El-Kobbir, four hundred thousand francs—'` /
   `'—for a Christian slave of eleven years named Haydée, and her mother, wife of Ali Tebelen.'` /
   `Signed, Fernand Mondego.` A red wax seal may be visible, but do not make its
   microscopic clarity compete with the President, document, or text.
5. Fernand is frozen below; high behind him the Count grips the gallery rail and
   leans over the room with appetite. Both men are silent.

Render exactly those eight balloon strings, once each, with clear ownership and
no other text. Preserve all punctuation, including `Haydée`, `El-Kobbir`, the em
dashes, and the literal single quotation marks around the first two document
lines.

### Approved image inputs

1. `refs/approved/05-haydee.png`
2. `refs/approved/03-fernand-1838.png`
3. `refs/approved/01-count-1838.png`
4. `refs/approved/23-page-33-chamber-objects-carrier.png`
5. `pages/page-32.png`

Attach only these five images.

---

## PAGE 34 — *illustrated prose*

**Reader turn:** the hall empties; Fernand remains upright in all his now-worthless decorations.

Use two images in the same Chamber. The dominant upper image shows tier after
tier of crimson benches almost empty under cold daylight. Fernand stands alone
in the middle, small but recognizable by his heavy moustache, receding hair,
soldier's build, and complete chest of decorations. He is not collapsed,
weeping, or theatrical. At most two tiny departing backs may remain at a distant
stair; nobody acknowledges him.

Place this exact prose in one comfortable field:

`The vote took four minutes. Nobody spoke to him on the way out. Two men who had dined at his house in April went past him on the stair and looked at the stair.`

`He stayed where he was for some time after the hall was empty, because he had not been given anything to do next, and for eleven years there had always been something to do next.`

The lower band shows the great doorway standing empty, with no person framed in
it. Place this exact prose in a second field:

`By six o'clock the name had been taken off the door.`

`His son heard it in the street, from a man selling papers.`

Render only those two prose fields. No balloons, labels, newspaper headline,
page number, signature, or pseudo-text.

### Approved image inputs

1. `refs/approved/03-fernand-1838.png`
2. `refs/approved/19-set-chamber.png`
3. `pages/page-33.png`

Attach only these three images.

---

## PAGE 35 — *dramatic*

**Reader turn:** Albert traces Haydée to the Count and understands who destroyed his father.

Build four ordered moments in Beauchamp's ink-black, newsprint-grey newspaper
office at night. Albert is twenty-two, clean-shaven, upright, chestnut-haired,
fair-olive, and bright-valued. Beauchamp is twenty-eight, tall, thin, stooped,
sandy-haired, always in small oval spectacles and plain dark clothes. Their
faces and silhouettes must never merge.

1. Albert in the doorway; Beauchamp remains seated: `The girl. Who is she?` / `Albert—`
2. Albert presses him: `She walked into the Chamber of Peers with a sixteen-year-old receipt and the name of a town nobody in France can find.` / `Somebody put her there.`
3. Beauchamp refuses to lie: `She lives in a house on the Champs-Élysées.` / Albert: `Whose house.`
4. Dominant close view of Beauchamp as Albert understands before the answer:
   `You've dined in it.` Albert's reaction must remain present or unmistakable,
   even if Beauchamp occupies most of the frame.

Render exactly those seven strings once each, in order, with unmistakable
speaker ownership. No captions, names, headlines, legible background copy, or
other text.

### Approved image inputs

1. `refs/approved/04-albert.png`
2. `refs/approved/07-beauchamp.png`

Attach only these two images.

---

## PAGE 36 — *dramatic*

**Reader turn:** Albert challenges the Count publicly; the Count enjoys it, then briefly flinches.

Build five ordered moments in the crowded gilt-and-mirror Opera foyer. Keep the
crowd secondary and impressionistic. Albert is the bright, mobile,
chestnut-haired young man; the Count is forty-two, clean-shaven, pallid,
swept-back black hair touched with grey, and the only still unbroken black
vertical in the moving room.

1. Albert advances through a crowd opening around him: `You came into my father's house. You took his hand on his own stairs. You ate at his table—`
2. Dominant image: the Count perfectly still in the bright crowd, answering with
   small cruel pleasure: `I ate nothing at your father's table.`
3. Albert absorbs the cruelty; no text.
4. Albert throws a glove: `Tomorrow. Eight o'clock, the Bois. Pistols.`
5. The Count catches it without hurry: `As you like.` Above the glove, preserve
   a slight involuntary change after the pleasure—not broad remorse or fear.

Render exactly those four strings once each with clear ownership. No captions,
signage, labels, page number, pseudo-text, or extra dialogue.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/04-albert.png`

Attach only these two images.

---

## PAGE 37 — *dramatic*

**Reader turn:** Haydée celebrates Fernand's fall; the Count cannot enjoy it because Albert is twenty-two.

Build four ordered moments in the Count's enormous underfurnished black room at
night. Haydée is twenty-seven, olive-gold, slight, long unbound black hair,
crimson-and-gold Epirote clothing, warm and moving. The Count is pallid,
clean-shaven, black-clad, still, and turned away. Keep them unmistakably
different in age, silhouette, hair, and value.

1. Haydée enters alive with triumph: `They have scraped his name off the door of the Chamber. I went to watch them do it.`
2. A laid table; the Count has not eaten: `You are not eating.`
3. Dominant image: Haydée stands over him while he looks toward a wall or dark
   window instead of at the meal: `You have wanted this since before I was born.` /
   `It is on the table in front of you and you are looking at the wall.`
4. Their stripped-down exchange: Count, `The boy is twenty-two.` / Haydée,
   `I was eleven.` / Count, `Yes.`

Render exactly those seven strings once each, in order, with clear attribution.
No captions, labels, page number, legible table paper, pseudo-text, or extra
dialogue. The food and glass support his refusal to eat; their exact design is
not a focal test.

### Approved image inputs

1. `refs/approved/05-haydee.png`
2. `refs/approved/01-count-1838.png`
3. `refs/approved/17-set-count-house.png`
4. `refs/approved/21-objects.png`

Attach only these four images.

---

## PAGE 38 — *dramatic*

**Reader turn:** Mercédès comes alone and says “Edmond.”

Build four ordered moments in the Count's black room, continuous with the
night. Mercédès is visibly forty-two: decisive eyes, lean mature cheeks, lower
lid and temple lines, restrained grey at the temples, dark hair dressed in 1838
fashion, travelling black, upright and unsentimental. The Count is forty-two,
clean-shaven, pallid, swept-back black hair with first grey, unrelieved black.

1. Mercédès alone in the doorway, unannounced: Count, `Madame la Comtesse. At this hour.` / Mercédès, `Don't.`
2. She enters but does not sit: `I have sat in that house since the newspaper, while men I have known twenty years found reasons not to look at me.` / `I have not once had to wonder who was doing it.`
3. A silent wide image makes her small in the enormous underfurnished room
   without diminishing her authority.
4. Dominant close frame of only their two faces: Mercédès, `Edmond.` / Count,
   `Nobody has said that name to me in twenty-three years.` / Mercédès,
   `I have said it every day.`

Render exactly those seven strings once each, in order, with clear ownership.
No captions, labels, clocks, page number, pseudo-text, extra people, or Haydée.

### Approved image inputs

1. `refs/approved/02-mercedes-1838.png`
2. `refs/approved/01-count-1838.png`
3. `refs/approved/17-set-count-house.png`
4. `pages/page-37.png`

Attach only these four images.

---

## PAGE 39 — *dramatic*

**Reader turn:** Mercédès names the real motive; Edmond agrees not to fire on Albert.

Continue in the same black room with Mercédès and the Count only. Build five
ordered moments, progressively closer. Preserve her mature travelling-black
identity and his pallid clean-shaven black-clad identity.

1. Mercédès, `Don't kill my son.` / Count, `Your son called me out in front of forty people.`
2. Mercédès, `Then let him miss.` / Count, `He will not miss. He has been shooting since he was ten.` / `His father taught him.`
3. Mercédès, `Then don't fire.` / Count, `You are asking me to stand still in a field and let a Mondego shoot me.`
4. Dominant close image of two wrecked faces looking directly at each other:
   Mercédès, `You did not do this for justice, Edmond.` / `You did it so that I would see it.` / `I have seen it.`
5. His poised right hand opens, with nothing held back in his face: `…Very well.` /
   `I will stand where his second puts me, and I will not raise my hand.`

Render exactly those twelve strings once each, in order, with unmistakable
ownership. Preserve the leading ellipsis in `…Very well.` No captions, labels,
page number, pseudo-text, extra people, or weapons.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/02-mercedes-1838.png`
3. `refs/approved/17-set-count-house.png`
4. `pages/page-38.png`

Attach only these four images.

---

## PAGE 40 — *illustrated prose*

**Reader turn:** at three in the morning, the Count puts his affairs in order and counts the cost of revenge.

Use two images in the Count's enormous black room lit by one lamp. The dominant
image shows him alone at a bare table, writing inside a small pool of warm light;
everything beyond it falls to black. Keep his clean-shaven pallid identity and
the same black coat as the prior page.

Place this exact prose in one comfortable field:

`He wrote until three. The estate to Haydée, entire, with a man in Trieste named to see it done. A letter to a shipowner in Marseille who was old now and would not understand any of it. Instructions about a house on an island that nobody else had ever seen the inside of.`

`It took him under two hours to put down everything he had made in nine years, and there was nobody on the list he had known before 1815.`

The lower band isolates a closed pistol case on the table with his hand resting
on its lid. Place this exact prose in a second field:

`Then he sat with the case shut in front of him and did the one piece of arithmetic he had been avoiding since April:`

`what he had spent, and what he had bought with it.`

Render only those two prose fields. No balloons, labels, legible writing on the
papers, page number, pseudo-text, open case, or displayed pistol.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/17-set-count-house.png`
3. `pages/page-39.png`

Attach only these three images.

---

## PAGE 41 — *dramatic*

**Reader turn:** Mercédès tells Albert who Edmond Dantès is and whom Albert is due to shoot.

Build five ordered moments in Albert's room at the Morcerf house, four hours
before dawn. One candle; walnut and old gilt subdued by night. Albert is
twenty-two, clean-shaven, chestnut-haired, fair-olive and upright. Mercédès is
forty-two with mature lines, grey-threaded formal dark hair and travelling
black. A disassembled pistol lies between them as an ordinary consequential
object, never pointed or brandished.

1. Albert cleans the pieces at a table; Mercédès stands in the door. Caption:
   `The same night, at the other end of Paris.` Albert: `You've been out.`
   Mercédès: `Yes.`
2. She sits opposite him: `Put that down. I am going to tell you about 1815.`
3. Dominant two-shot across the table: `There was a boy in Marseille who was going to marry me. His name was Edmond Dantès.` / `They arrested him at our betrothal dinner. He was nineteen.` / `Danglars wrote the letter. Your father carried it to the post.`
4. Albert: `You knew.` / Mercédès: `I have always known.`
5. Her hands flat on the table. Albert: `Where is he now?` / Mercédès:
   `You are going to shoot at him at eight o'clock.`

Render exactly that caption and those ten dialogue strings once each, in order,
with clear ownership. No other text, labels, page number, legible paper, or
additional person.

### Approved image inputs

1. `refs/approved/02-mercedes-1838.png`
2. `refs/approved/04-albert.png`
3. `refs/approved/18-set-morcerf-house.png`
4. `pages/page-40.png`

Attach only these four images.

---

## PAGE 42 — *dramatic*

**Reader turn:** Albert publicly withdraws the duel.

Build four ordered moments in the Bois at dawn: pale grey-green mist, wet black
trunks, thin gold at the horizon. Albert is bareheaded, chestnut-haired and
bright-valued; the Count stands apart as a clean-shaven black vertical. The
seconds and surgeon are unnamed supporting figures and must not resemble the
two principals.

1. Establish the field: principals, carriage, two seconds, surgeon's bag. The
   Count already stands still. No text.
2. Dominant image: Albert, hat off, addresses everyone: `I asked for this and I'm withdrawing it. Out loud, here, so nobody has to hear it from somebody else later.`
3. A startled second beside an open pistol case: `On what grounds, monsieur?`
4. Albert steady: `On the grounds that the newspaper was right.`

Render exactly those three strings once each with clear ownership. No caption,
labels, page number, pseudo-text, shot, smoke, raised pistol, or wound.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/04-albert.png`
3. `pages/page-41.png`

Attach only these three images.

---

## PAGE 43 — *dramatic*

**Reader turn:** Albert gives up his father's name and leaves with Mercédès.

Continue in the same misty Bois. Albert is bareheaded and steady; Mercédès waits
at the edge of the field in travelling black; the Count is the still black
figure who, for once, has no prepared answer.

1. Albert speaks with Mercédès visible behind him near a hired carriage:
   `My mother told me last night what my father did in 1815, to a man called Edmond Dantès.` /
   `He did it for money, and he did it to marry her. The man was nineteen years old.`
2. The seconds and surgeon listen: `I've no quarrel with this gentleman. I haven't the right to one.`
3. The Count takes one step: `Monsieur—` Albert stops him: `Don't.`
4. Dominant wide image: Albert and Mercédès walk away across wet grass toward
   the carriage, backs to frame, small under the dawn sky. The Count is absent
   from this final image. Albert: `I'll take my mother's name. She was Mercédès Herrera before she was anything of his.`

Render exactly those six strings once each, in order, with clear ownership. No
caption, labels, page number, shot, smoke, raised pistol, or extra dialogue.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/02-mercedes-1838.png`
3. `refs/approved/04-albert.png`
4. `pages/page-42.png`

Attach only these four images.

---

## PAGE 44 — *illustrated prose*

**Reader turn:** spared at dawn, the Count decides before reaching Paris that nothing changes.

Use three ordered images. First, a dominant wide field in the misty Bois: the
Count very small and alone on wet grass under a pale sky while carriages depart
in opposite directions. Nobody looks back.

Place this exact prose in one comfortable field:

`He had come out to the Bois to be shot at. He had spent the night before putting his affairs in order so that a boy of twenty-two could kill him without inconveniencing anybody, and he had meant it.`

`Nobody fired. He stood on the wet grass a long while afterwards working out what he felt, which took longer than he expected, and what he arrived at was not relief.`

Second, inside his carriage entering grey Paris, his face at the window like a
man doing arithmetic. Place this exact prose in a second field:

`At three that morning he had thought that if he were let off he would stop.`

`He was wrong about that, and he knew it before the carriage reached the gate. The son had let him go. The father had not, and would be at his door before dark.`

Third, in the black room, his hand sets a decanter and one empty glass square to
the table edge and withdraws. Nobody drinks yet. No text in this image.

Render only those two prose fields. No balloons, labels, page number,
pseudo-text, or displayed weapon.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/17-set-count-house.png`
3. `refs/approved/21-objects.png`
4. `pages/page-43.png`

Attach only these four images.

---

## PAGE 45 — *dramatic*

**Reader turn:** under his own roof, the Count drinks and tells Fernand what the refusals meant.

Build four ordered moments in the Count's enormous black room that afternoon.
The Count remains in his Bois coat with wet grass on his boots: tall,
clean-shaven, pallid, swept-back black hair touched with grey. Fernand is
forty-six, heavy, moustached, receding and iron-grey at the sides, still ruined
but upright. Keep the two men structurally distinct. A closed pistol case stays
with Fernand until he sets it down; it is not opened here.

1. Fernand in the doorway, hat on, case under his arm: `My son wouldn't fire at you. Take a pistol.`
2. The Count seated: `No. Sit down.` Fernand: `You've destroyed me and you won't even—` Count: `Sit down. You are going to be told why first.`
3. Dominant image: the Count pours in his own house, drinks, and lowers the
   glass empty. `You watched me set a full glass down on your own staircase and decided I was ill.` /
   `Your wife watched me refuse fruit out of her garden and knew what it meant inside a minute.` /
   Fernand: `What?`
4. The empty glass on black wood, the Count above it: `It is a rule of mine. I don't eat or drink under the roof of an enemy.` / `This is my roof.`

Render exactly those nine strings once each, in order, with clear attribution.
No captions, labels, page number, pseudo-text, additional people, raised pistol,
or open case.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/03-fernand-1838.png`
3. `refs/approved/17-set-count-house.png`
4. `refs/approved/21-objects.png`
5. `pages/page-44.png`

Attach only these five images.

---

## PAGE 46 — *dramatic*

**Reader turn:** the Count removes the mask and tells Fernand he is Edmond Dantès.

Continue in the same black room with the same two men and the closed pistol
case. Keep the Count clean-shaven, pallid, tall and black-clad; keep Fernand
heavy, moustached, receding and soldier-built.

1. The Count: `Do you know the name Dantès?`
2. Fernand begins to recognize what is happening while the Count says:
   `February, 1815. The Pharaon.` / `You could not write, so Danglars wrote it for you.` /
   `You carried it to the post yourself, because you did not trust him to.`
   Render *Pharaon* in italics if feasible, but exact transcription matters more
   than typographic styling.
3. Fernand stands, case still under his arm: `I have been in your house. I have taken your hand on your stairs.` / `I have had your son's arm through mine.`
4. Dominant full-face unmasking of the Count with no theatrical disguise effect:
   `Look at me, Fernand.` / `I am Edmond Dantès.`
5. Narrow silent aftermath: empty doorway and bare marble top. Fernand and the
   pistol case are both gone.

Render exactly those eight strings once each, in order, with all dialogue owned
by the Count. No captions, labels, page number, pseudo-text, visible weapon,
extra person, or dialogue for Fernand.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/03-fernand-1838.png`
3. `refs/approved/17-set-count-house.png`
4. `pages/page-45.png`

Attach only these four images.

---

## PAGE 47 — *spectacle*

**Reader turn:** Fernand reaches an emptied bedroom, and the dark house answers with one shot.

Use three ordered images at the Morcerf house at dusk. Keep Fernand's heavy
moustached identity and the same coat and closed pistol case from Page 46.

1. The general's staircase is unlit and empty. The front door stands open behind
   Fernand as he climbs alone with the case. No text.
2. Dominant bedroom: wardrobes and drawers open and emptied of clothing; jewel
   cases and valuables deliberately remain; one woman's gown lies across a
   chair. Fernand stands alone with the pistol case now open in his hands.
   Caption exactly: `His wife and son had taken nothing of his.`
3. Exterior street view: the whole shuttered façade is black except for one
   upstairs window, stark white. No person is visible. Against the dark masonry,
   a small sound label exactly: `CRACK`

Render only that caption and sound label. No balloons, page number, signs,
pseudo-text, body, blood, wound, muzzle flash, interior firing pose, or second
Fernand.

### Approved image inputs

1. `refs/approved/03-fernand-1838.png`
2. `refs/approved/18-set-morcerf-house.png`
3. `refs/approved/21-objects.png`
4. `pages/page-46.png`

Attach only these four images.

---

## PAGE 48 — *dramatic*

**Reader turn:** Mercédès and Albert hear the shot, understand it, and leave without returning to the house.

Build four ordered moments on the wet gas-yellow street outside the Morcerf
house at night. One hired carriage waits. Mercédès, visibly forty-two in
travelling black, and Albert, twenty-two and chestnut-haired, have only one
small bag between them. Keep both identities stable and the great house dark.

1. At the carriage door, Albert: `We could have taken the plate. It was my grandmother's.` Mercédès: `He bought it in 1821, from a dealer in the rue Vivienne. There was no grandmother.`
2. Albert: `You know where all of it came from.` Mercédès: `All of it.`
3. Dominant image: both stop and half-turn toward the upstairs window, now dark
   again. Albert: `Mother—` Mercédès: `I know.`
4. Her hand closes on his arm and holds him in place: `Twenty-three years I lived in that house.` / `Get in the carriage, Albert.`

Render exactly those eight strings once each, in order, with clear ownership.
No caption, sound label, page number, street sign, pseudo-text, visible body,
weapon, extra luggage, jewellery, plate, or person at the window.

### Approved image inputs

1. `refs/approved/02-mercedes-1838.png`
2. `refs/approved/04-albert.png`
3. `pages/page-47.png`

Attach only these three images.

---

## PAGE 49 — *spectacle*

**Reader turn:** the Count watches the last warm light leave, counts Fernand, and looks toward Villefort's roof.

Use three connected night images on the same wet street. The Count is a single
clean-shaven black-clad figure at observation distance; keep his silhouette
recognizable but do not turn this ending into a portrait.

1. On the far pavement, deep in shadow, reveal that the Count has been standing
   there alone. No text.
2. Dominant wide street: the hired carriage recedes away from the frame, its one
   lamp small, warm, and diminishing. The enormous shuttered Morcerf house is
   dark on the left. The Count, still on the far pavement, says exactly: `One.`
3. Look upward beyond the Morcerf roofline to a different, more distant house
   with one lit second-floor window. No person is visible there. Caption exactly:
   `Villefort, the King's Attorney, kept late hours.`

Render only that one balloon and one caption. No page number, signs,
pseudo-text, visible Villefort, reopened Morcerf window, second carriage, second
Count, or warm light other than the departing lamp and the distant target
window.

### Approved image inputs

1. `refs/approved/01-count-1838.png`
2. `refs/approved/17-set-count-house.png`
3. `pages/page-48.png`

Attach only these three images.

---

# 6 · Intent-first builder / critic architecture

Pages 33-49 use three separate compact transports per page:

- the builder packet contains the shared generation frame, page intent,
  builder-only rewritten prompt, reference manifest, and output contract;
- the blind critic entrypoint contains only neutral image paths, staged review
  order, and the report schema;
- the critic-card packet, opened only after the blind read, contains the exact
  script, page intent, materiality threshold, and numbered blocking criteria.

The critic never receives the generation prompt or builder audit. The builder
audit never gates submission. The orchestrator is nonvisual and validates the
report contract and numbered retry route mechanically.

Each numbered criterion is a stable defect signature. A repeat after a targeted
correction triggers a clean prompt reset; persistence after that reset stops for
the owner. Any v4 REVISE remains an owner hold.

## Current operations, verbatim

---

### 1 · The page critic

Run one fresh zero-history critic on every completed candidate. Never reuse a
critic context.

#### Blind-first transport

The critic receives only:

1. `qa/_run/page-NN-critic.md`;
2. neutral candidate, 600 × 900 proof, and 768 × 1152 proof paths;
3. after completing the blind read,
   `qa/_run/page-NN-critic-card.md`.

The critic never receives or opens the generation prompt, builder packet,
builder audit, reference manifest, prior candidates, prior reports, version
number, master plan, or builder/orchestrator task history.

Stage 1, script closed: from the 600 × 900 proof, state what happens, who owns
the page, what changes or causes the turn, and transcribe every visible string
with speaker/source attribution.

Stage 2: open the separate critic-card packet. It contains only the exact
owner-controlled script, reader-facing page intent, materiality threshold, and
short numbered blocking criteria.

#### Release threshold

The critic is a reader-facing release gate, not a defect collector. A visible
issue blocks only when it materially harms one of:

- the page event or reason to turn;
- exact comfortable text transcription, order, or attribution;
- recognition/separation of named or focal characters;
- consequential continuity or object state needed to understand the story;
- focal anatomy or generation integrity;
- the dominant dramatic relationship.

These are nonblocking when the reader event remains intact:

- repeated or similar anonymous background faces;
- minor background anatomy, hands, texture, or finish;
- tiny-prop indistinctness when the reader need not identify the prop;
- exact hue, scale, coordinate, geometry, panel share, margin, or type size;
- prompt variance without material reader harm;
- any technically true observation that does not justify risking a complete
  redraw of an otherwise successful page.

No typography measurement exists at the page gate. Exact comfortable blind
transcription from the 600 × 900 proof is the complete readability test.

#### Verdict contract

Return only `APPROVED` or `REVISE`. Reports use the exact schema in the emitted
critic entrypoint and are mechanically validated.

Every `REVISE` finding must:

1. cite one numbered page-card criterion;
2. state the visible observation;
3. explain the material reader harm;
4. explain why that harm is substantial enough to risk replacing the complete
   page.

If the fourth statement cannot be made concretely, the verdict is `APPROVED`.
Omit praise, suggestions, optional polish, and minor observations. The critic
does not edit, regenerate, promote, or propose prompt wording.

---

### 2 · The builder

Run one fresh zero-history builder per candidate. Never reuse an image-bearing
builder context.

The builder receives only:

- `qa/_run/page-NN-builder.md`;
- its page number, version, and route mode;
- the explicitly permitted revision inputs for that mode;
- the approved image inputs listed in the packet.

The builder generates one complete flattened page, writes the exact issued
prompt, records one concise intent/technical audit, derives the desktop and
tablet proofs, and submits the candidate. It never approves or promotes.

The audit asks whether the reader-facing intent appears to land. It is a report,
not a gate, and it does not grade prompt variance. Every completed candidate
reaches the independent critic. The only pre-critic rerun is a failed generation:
wrong canvas, corrupt/truncated output, or gross focal anatomical breakage.

#### Revision modes

- `BASE`: the assembled shared generation frame plus the page's rewritten
  builder-only prompt.
- `TARGETED`: the base packet, immediately preceding issued prompt, and latest
  validated critic report. Correct only the cited material criteria and protect
  the successful facts recorded by the blind read.
- `FULL_PROMPT_RESET`: the base packet plus the last two compact validated
  reports and repeated criterion numbers. Do not open an earlier issued prompt,
  rejected candidate, proof, audit, or builder history. Replace the complete
  generation prompt and composition strategy while preserving the locked
  intent, exact strings, story facts, references, and page count.

Never patch, crop, composite, inpaint, reletter, or feed rejected art back as an
image input.

---

### 3 · Retry and stopping

The critic-card numbers are stable defect signatures. The nonvisual
orchestrator compares numbers, not artwork.

1. `v1 REVISE` → targeted v2.
2. The same criterion on v1 and v2 → clean-slate v3 prompt rewrite.
3. The same criterion after that reset → resistant-defect owner hold before v4.
4. If v2 introduces only new criteria, v3 is targeted; a v2/v3 repeat receives
   the one available clean reset at v4.
5. Any `v4 REVISE` → owner hold. No v5.

The only routes are `PROMOTE`, `TARGETED`, `FULL_PROMPT_RESET`,
`RESISTANT_DEFECT_HOLD`, `V4_OWNER_HOLD`, and `INVALID_CRITIC_REPORT`.

---

### 4 · Sequence, cold-read, and continuity critics

After Page 40, run three fresh independent roles:

- Pages 31–40 uninterrupted sequence review against exact story and
  reader-facing continuity;
- script-blind Pages 1–40 cold read from reduced proofs only;
- Pages 31–40 visual-continuity review against approved locks.

After Page 49, run:

- Pages 41–49 uninterrupted sequence review;
- script-blind Pages 1–49 cold read;
- whole-book visual-continuity review;
- whole-book release gate.

These roles never see generation prompts, builder audits, rejected candidates,
or prior reports. They apply the same materiality threshold. A sequence finding
must name the affected pages, state reader harm, and justify any proposed
complete-page redraw. Cosmetic drift alone does not reopen a promoted page.

---

### 5 · Promotion boundary

Only the orchestrator promotes an `APPROVED` candidate. Promotion copies exact
bytes, verifies matching SHA-256, derives promoted proofs, appends the ledger,
and only then releases the next page.

The orchestrator never looks at the art. An invalid report stops for a fresh
critic contract decision; it does not authorize regeneration. An owner override
is recorded beside the original report and never rewritten as critic approval.

---

## How to use the numbered page cards

For Pages 33-49, use only the emitted `qa/_run/page-NN-critic-card.md` after the
blind image read. A finding must cite a numbered criterion, state material
reader harm, and justify a complete redraw. True but nonconsequential defects
are omitted and the page is approved.

Pages 1-32 below retain their historical appendices as production evidence;
they are not inputs to the remaining-page critic.

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

---

## Page 29 — appendix
- **Two locations, and they must not look alike.** Panels 1–2 are Janina: white limestone, hard high sun, sky, horizontal. Panel 3 is Paris: lacquer black, one lamp, no sky. If the Janina panels read as a warm European street rather than a bleached southern one, the cut has failed.
- **Janina is unburned.** This is 1838, sixteen years after the fire. Any flame, smoke, ruin or burning wall is blocking — and the reader must still recognise it as the same town they watched burn.
- **Beauchamp's spectacles are present and legible in both panels he appears in**, and his coat is the same worn dark Paris coat in southern light. No pale waistcoat, no chestnut hair, no upright unmarked posture.
- **No face in panel 3.** Two long pale hands, the lamp, the paper. If a face appears, blocking — this panel's whole rhyme with P26 is the withheld face.
- **The old man carries no reserved identity stack** (no military moustache with receding temples, no oval spectacles with sandy hair, no black columnar evening dress, no raven curls with white shirt and sash).
- **Two prose fields, not three or four.** Field 1 is two paragraphs in panel 1; field 2 is one sentence in panel 2. Sentences scattered into extra boxes is blocking.
- **`JANINA` may appear once as newspaper headline type in panel 3 and nowhere else.** Every other word on that sheet is grey texture. No legible body text on the newspaper.

---

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

---

## Page 31 — appendix
- **Fernand must be visibly winning.** Warm, upright, plausible, in command of the room; the benches leaning toward him; one peer half out of his seat in panel 4. If he reads as already condemned — hunched, sweating, cornered, guilty — the page has failed its purpose and the volume's climax loses its stake.
- **Full decorations worn to the bar.** Orders, ribbons, wax-red and old gold, polished and displayed. This state must match P34 exactly, where they are still on him in an empty hall.
- **Haydée is not on this page in any panel.** She has not come through the door yet. Any woman anywhere in this room is blocking.
- **The Count is in the gallery only, above the floor, never on it.** And his face must read *hungry*, not worried, not grave, not serene — the panel exists to show him willing his own victim to mount a better defence.
- **Danglars is identifiable and silent:** fleshy face, full side whiskers, **no moustache**, nodding along untroubled. If he is given a moustache he collides with Fernand; if he is given a balloon, blocking.
- **`Go on. Win it.` is a normal balloon at normal size.** Spoken under the noise of the room — but not whispered, shrunk, italicised or given a special balloon shape.
- **Panel 3 is 18% (~276 px) carrying 29 words in two balloons.** Watch this one at 600 × 900: the two balloons were specified side by side across the band precisely so they can sit at full height. If they have been stacked and shrunk to the point where a string will not transcribe, blocking.
- **Panel 1 carries no text.** No orientation caption — the reader arrived with him on the previous page.

---

## Page 32 — appendix
- **Zero strings. Any legible word anywhere on this page is blocking**, including a date line, a title, a sound word or a signature.
- **Her dress must rhyme with the benches.** Her crimson-and-gold must sit in the same colour family as the crimson of the hall so that she reads as belonging to the room and Fernand, in French black at the far end, does not. If her dress reads as an alien colour note fighting the room, the page's single idea has been inverted.
- **She is alone in the doorway, small, centred, full figure**, with the sealed document in her hand. Not framed heroically large, not lit theatrically, not accompanied.
- **The red wax seal is visible; the handwriting is marks, not words.**
- **The Count does not appear.** No gallery figure, no black vertical, nothing at the rail. He is absent from this page by design.
- **Fernand is tiny at the far end and identified by silhouette** — moustache mass, heavy build, the glint of decorations — not by facial detail.
- **Panel 1's three hundred faces all turn the same way, and every one of them is silent.** No balloons, no tail fragments.
- **This is the volume's single biggest image at 70%.** If the dominant panel does not dominate — if panel 1 competes with it — blocking.

---

## Page 33 — appendix

### C1 — Testimony text or ownership fails
Any required script string cannot be transcribed comfortably from the 600 × 900
proof, is altered/duplicated/reordered, or cannot be assigned confidently to
Haydée or the President. Fernand and the Count must remain silent.

### C2 — The testimony does not build to conviction
The page does not read in order as Haydée naming herself, identifying Fernand,
the President reading the sale, and the room reaching the end of the case.

### C3 — The accuser–accused relationship fails
Haydée and Fernand are not held in one readable hall-spanning relationship, one
is unrecognizable, or the staging makes another figure the apparent accuser or
accused.

### C4 — The evidence action fails
The President is not visibly reading and presenting a document, so the spoken
sale appears ungrounded. Exact handwriting and microscopic seal resolution are
nonblocking when the raised evidence action is clear.

### C5 — The Count's position changes the story
The Count is absent from the final relationship, appears on the Chamber floor,
is confused with Fernand, or does not read as an intent observer above Fernand.
Exact hand placement, railing geometry, and facial micro-expression are not
gates when that relationship lands.

### C6 — Consequential generation failure
A duplicated named figure, identity collision, gross focal anatomical break, or
corruption materially disrupts the testimony. Anonymous crowd repetition,
background hands, and decorative artifacts are nonblocking unless they dominate
attention or change who is present.

---

## Page 34 — appendix

### C1 — Prose transcription fails
Either prose field is missing, altered, duplicated, reordered, or not
comfortably transcribable at 600 × 900; or invented readable text appears.

### C2 — Fernand is not abandoned by the Chamber
The dominant image does not clearly show Fernand still upright and substantially
alone as the crimson hall empties, or it turns the moment into collapse,
weeping, confrontation, or public spectacle.

### C3 — The decorations or identity change the consequence
Fernand is unrecognizable/confused with the Count, or his decorations are absent
enough that the irony of still wearing them is lost. Exact medals, ribbons,
colors, count, and tiny hardware are nonblocking.

### C4 — The outward consequence disappears
The empty doorway/lower image and its prose do not carry the action from the
finished vote to the removed name and Albert hearing the news.

### C5 — Consequential generation failure
A duplicate/fused Fernand, gross focal anatomy error, corruption, or a crowd
that makes the hall look fully occupied materially breaks the page. Minor
background figures, bench geometry, and texture do not.

---

## Page 35 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the seven exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or Albert and Beauchamp's balloons cannot be
assigned confidently.

### C2 — Albert's deduction fails
The page does not read as Albert pressing for Haydée's source and understanding
from Beauchamp's final answer that the Count arranged his father's destruction.

### C3 — Albert and Beauchamp collide
The two named young men cannot be distinguished consistently by face,
spectacles, hair/value, or posture, materially confusing who knows and who asks.

### C4 — The final answer lacks a receiver
`You've dined in it.` appears without Albert's comprehension being visible or
otherwise unmistakable, so the dominant turn is lost.

### C5 — Consequential generation failure
A duplicate named man, gross focal anatomy error, corruption, or invented focal
actor disrupts the exchange. Paper clutter, background type texture, office
accuracy, and cosmetic artifacts are nonblocking.

---

## Page 36 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the four exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or Albert and the Count's speech ownership is
unclear.

### C2 — The public challenge does not read
Albert's accusation, thrown glove, challenge, and the Count's acceptance do not
form a clear causal sequence, or the glove/catch is absent enough that the duel
challenge becomes confusing.

### C3 — The dramatic contrast fails
Albert is not the angry advancing young man, the Count is not the still black
figure in the bright crowd, or their identities collide.

### C4 — The Count's reaction changes the story
The Count reads only frightened, apologetic, or serene; or his pleasure is so
broad that the slight later disturbance cannot exist. Exact micro-expression is
nonblocking when cruel confidence followed by some change is readable.

### C5 — Consequential generation failure
A duplicate principal, gross focal anatomy error, corrupt text/image, or crowd
artifact that dominates the principals materially disrupts the page. Similar
anonymous faces and background hands are otherwise nonblocking.

---

## Page 37 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the seven exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or Haydée and the Count's lines cannot be
assigned confidently.

### C2 — Triumph versus emptiness fails
Haydée does not read as alive and triumphant while the Count does not eat and
looks away from the victory, or their relationship reverses.

### C3 — The final moral exchange fails
`The boy is twenty-two.` / `I was eleven.` / `Yes.` does not read in that order
as the reason he cannot celebrate.

### C4 — Named identity or continuity fails
Haydée is confused with Mercédès, the Count is confused with Fernand/Albert, or
the room/time changes enough to break continuity. Exact food, decanter, glass,
table setting, and wall detail are nonblocking.

### C5 — Consequential generation failure
A duplicate principal, gross focal anatomy error, corruption, or invented
speaker materially disrupts the exchange. Minor tableware, hands, background
texture, and finish do not.

---

## Page 38 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the seven exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or Mercédès and the Count's lines are unclear.

### C2 — Mercédès' arrival loses its force
She is not alone and unannounced at night, she becomes passive or socially
decorative, or another figure changes the confrontation.

### C3 — The name reveal fails
The dominant close image does not make `Edmond.` the unmistakable break in the
Count's persona and the emotional center of the page.

### C4 — Identity and age fail materially
Mercédès is confused with Haydée or youth-washed enough to become a different
character; the Count is unrecognizable; or the two faces merge. Exact wrinkles,
grey-strand count, coiffure detail, and skin finish are nonblocking.

### C5 — Consequential generation failure
A duplicate principal, gross focal anatomy error, corruption, or invented
speaker materially disrupts the encounter. Furnishing precision, empty-space
percentages, and minor background artifacts do not.

---

## Page 39 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the twelve exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or speaker ownership is unclear.

### C2 — The argument's causal progression fails
Mercédès' request, the Count's practical objections, her accusation about his
real motive, and his final agreement do not read as one escalating exchange.

### C3 — The dominant accusation fails
The close confrontation does not make `You did it so that I would see it.` and
`I have seen it.` the emotional defeat of the Count.

### C4 — The agreement not to fire fails
The final moment does not clearly show the Count yielding and promising not to
raise his hand. Exact finger position or hand anatomy is nonblocking unless a
focal gross break obscures the surrender.

### C5 — Identity or generation integrity fails materially
Mercédès and the Count collide, a principal is duplicated, focal anatomy is
grossly broken, or corruption disrupts the scene. Room detail, pose precision,
and cosmetic artifacts do not.

---

## Page 40 — appendix

### C1 — Prose transcription fails
Either prose field is missing, altered, duplicated, reordered, or not
comfortably transcribable at 600 × 900; or invented readable text appears.

### C2 — Preparation for death fails
The Count is not clearly alone writing at three in the morning as he puts his
affairs in order, or the page reads as ordinary office work rather than final
preparation.

### C3 — The pistol-case turn fails
The lower image does not clearly present a closed pistol case under his resting
hand, or shows an open/brandished weapon that changes the scene. Exact case
hardware, scale, and hand placement are nonblocking.

### C4 — Identity and atmosphere fail materially
The Count is unrecognizable or the room becomes warm, busy, domestic, or
daylit enough to lose the isolated night vigil.

### C5 — Consequential generation failure
A duplicate Count, gross focal anatomy error, corruption, or text collision
materially disrupts the page. Paper detail, handwriting texture, lamp design,
and background finish do not.

---

## Page 41 — appendix

### C1 — Caption/dialogue transcription or ownership fails
The exact caption or any of the ten dialogue strings is missing, altered,
duplicated, reordered, or not comfortably transcribable; or mother and son's
lines cannot be assigned confidently.

### C2 — The 1815 revelation fails
Mercédès' account does not clearly name Edmond, the arrest, Danglars' letter,
and Fernand posting it as the causal truth she is giving Albert.

### C3 — The duel consequence fails
The final exchange does not make Albert understand that Edmond Dantès is the man
he is scheduled to shoot at eight.

### C4 — Mother, son, and pistol relationship fails
Mercédès and Albert collide or reverse roles, or the disassembled pistol is
absent/brandished in a way that materially changes the conversation. Exact
parts, cleaning technique, table geometry, and candle design are nonblocking.

### C5 — Consequential generation failure
A duplicate principal, gross focal anatomy error, corruption, or invented
speaker materially disrupts the scene. Minor hands, gun-part detail, furnishing,
and finish do not.

---

## Page 42 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the three exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or Albert and the second's lines are unclear.

### C2 — The public withdrawal fails
Albert is not visibly addressing the witnesses with his hat off, or his first
speech does not read as a public cancellation of the duel he demanded.

### C3 — The expected duel is unclear
The Count, seconds, and enough duelling context are absent for Albert's action
to make sense; or a shot/wound/raised weapon falsely suggests the duel occurs.
Exact number or placement of anonymous attendants and case hardware are
nonblocking.

### C4 — Albert and the Count collide
The principals are confused, or the Count becomes the speaker/owner of Albert's
withdrawal.

### C5 — Consequential generation failure
A duplicate principal, gross focal anatomy error, corruption, or crowd artifact
that dominates the public act materially disrupts the page. Anonymous face
similarity, mist, trees, and costume finish do not.

---

## Page 43 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the six exact strings is missing, altered, duplicated, reordered, or not
comfortably transcribable; or Albert and the Count's lines are unclear.

### C2 — Albert's moral account fails
Albert's statements about 1815, money, marriage, and having no right to a
quarrel do not read as the reason he withdraws.

### C3 — The Count's interruption fails
The Count's attempted `Monsieur—` and Albert's `Don't.` do not read as the
usually prepared Count being stopped without an answer.

### C4 — The final departure fails
Albert and Mercédès do not clearly leave together toward the carriage, Albert's
new-name line is not theirs, or the Count appears in the dominant final image
and retakes ownership of the page.

### C5 — Identity or generation integrity fails materially
Albert, Mercédès, and the Count collide; a principal is duplicated; gross focal
anatomy or corruption disrupts the choice. Mist, distant witnesses, carriage
detail, and background artifacts do not.

---

## Page 44 — appendix

### C1 — Prose transcription fails
Either prose field is missing, altered, duplicated, reordered, or not
comfortably transcribable at 600 × 900; or invented readable text appears.

### C2 — The empty-field aftermath fails
The Count is not clearly left alone after the carriages depart, or the page
reads as relief, triumph, or an active duel rather than survival without relief.

### C3 — The decision to continue fails
The carriage image and second prose field do not communicate that he decides
before reaching Paris that Albert's mercy changes nothing.

### C4 — The waiting-glass turn fails
The final image does not clearly show his hand setting out a decanter and one
glass in the black room for what comes next. Exact vessel design, alignment,
liquid level, and hand placement are nonblocking.

### C5 — Consequential generation failure
The Count is duplicated/unrecognizable, gross focal anatomy or corruption
disrupts the page, or an invented person changes the aftermath. Carriage,
weather, tableware, and background finish do not.

---

## Page 45 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the nine exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or the two men's speech ownership is unclear.

### C2 — Fernand's armed demand and the Count's refusal fail
Fernand does not arrive ruined with the closed case, or the Count appears to
accept the duel rather than making him sit and hear the reason first.

### C3 — The drink action fails
The dominant moment does not clearly show the Count pouring and drinking the
glass empty in his own house. Exact glass design, liquid color, swallow pose,
and tiny object state are nonblocking when the first completed drink is clear.

### C4 — The roof/enemy meaning fails
The final two lines do not land as the explanation of the earlier refusals and
the assertion that Fernand is now under the Count's roof.

### C5 — Identity or generation integrity fails materially
The Count and Fernand collide, a principal is duplicated, gross focal anatomy
or corruption disrupts the scene, or the case visibly opens/weapon is raised
and changes the event. Grass specks, décor, glass detail, and minor hands do not.

---

## Page 46 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the eight exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or any line appears to belong to Fernand rather
than the Count.

### C2 — The 1815 reconstruction fails
The name Dantès, February 1815, the *Pharaon*, Danglars writing, and Fernand
posting the letter do not read as one accumulating recognition. Italic styling
of *Pharaon* is nonblocking when the word transcribes exactly.

### C3 — The unmasking fails
`Look at me, Fernand.` / `I am Edmond Dantès.` is not the dominant full-faced
revelation, or the Count remains an unreadable theatrical persona.

### C4 — The pistol-case exit fails
The last band does not show that Fernand has gone through the doorway and taken
the case, leaving its prior surface empty. Exact case visibility, marble grain,
and doorway geometry are nonblocking when absence and removal are clear.

### C5 — Identity or generation integrity fails materially
The Count and Fernand collide, a principal is duplicated, gross focal anatomy
or corruption disrupts the recognition, or a visible weapon adds an action not
in the script. Background and costume finish do not.

---

## Page 47 — appendix

### C1 — Caption or sound text fails
The exact caption or `CRACK` is missing, altered, duplicated, reordered, or not
comfortably transcribable; or invented readable text appears.

### C2 — Fernand's return and continuity fail
Fernand is not recognizably the same ruined man climbing his empty staircase
with the case, or another person accompanies/confronts him.

### C3 — The family took nothing of his fails
The bedroom does not read as emptied of Mercédès and Albert while valuables
remain, making the caption false or unclear. Exact jewels, drawer count,
wardrobe contents, gown design, and prop placement are nonblocking.

### C4 — The off-panel suicide fails
The final exterior does not show one white upstairs window against an otherwise
dead house with the sound outside it, or it instead depicts a body, gore,
impact, muzzle flash, or visible firing action that changes the chosen restraint.

### C5 — Consequential generation failure
A duplicate Fernand, gross focal anatomy error, corruption, or impossible case
continuity materially disrupts the sequence. Minor furniture, hands, façade,
window, and texture artifacts do not.

---

## Page 48 — appendix

### C1 — Dialogue transcription or ownership fails
Any of the eight exact strings is missing, altered, duplicated, reordered, or
not comfortably transcribable; or Mercédès and Albert's lines are unclear.

### C2 — They have taken nothing fails
Mercédès and Albert do not clearly have only one small bag, or visible valuables
and attendants change their refusal of Fernand's possessions. Exact bag design
and scale are nonblocking.

### C3 — Hearing and understanding the shot fails
Their shared turn toward the now-dark window and `Mother—` / `I know.` do not
read as immediate understanding of the off-panel event.

### C4 — Mercédès prevents the return fails
Her hand and final lines do not clearly hold Albert outside and move them toward
the carriage rather than back into the house. Exact grip, arm angle, and
carriage motion are nonblocking.

### C5 — Identity or generation integrity fails materially
Mercédès and Albert collide, a principal is duplicated, gross focal anatomy or
corruption disrupts the scene, or a visible body/weapon/person at the window
changes the story. Cobble, gaslight, façade, and background artifacts do not.

---

## Page 49 — appendix

### C1 — Final text fails
`One.` or `Villefort, the King's Attorney, kept late hours.` is missing,
altered, duplicated, reordered, not comfortably transcribable, or joined by
invented readable text.

### C2 — The Count's observation fails
The first two images do not reveal one recognizable black-clad Count watching
from the far pavement, or he becomes a close portrait/active pursuer that
changes the ending.

### C3 — The departing warmth fails
The dominant street image does not clearly make the receding carriage lamp the
last warm human element leaving the dark Morcerf house.

### C4 — The next target fails
The final image does not point beyond the Morcerf roof to a different distant
house with one lit window, or it visibly depicts Villefort and prematurely
turns the promise into a scene. Exact roof geometry, window floor, distance,
and architecture are nonblocking when the new target is clear.

### C5 — Consequential generation failure
The Count is duplicated/unrecognizable, the carriage direction is materially
confused, gross focal anatomy or corruption disrupts the ending, or a reopened
Morcerf window changes continuity. Night texture, reflections, masonry, and
minor background artifacts do not.

---

# 7 · Revision, routing, and promotion

## Valid redraw authority

Only a mechanically valid independent `REVISE` authorizes another candidate.
Every finding must cite a numbered page-card criterion, state material reader
harm, and justify risking a complete redraw. An out-of-card, cosmetic, numeric,
or harm-free finding is an invalid critic report—not an art defect.

The builder audit never authorizes a redraw. It records the intent read,
transcription, and technical facts, then submits every completed candidate.

## Targeted correction

A targeted builder receives the base builder packet, immediately preceding
issued prompt, and latest validated critic report. It corrects only the cited
material criteria and protects the successful reader facts from the blind read.
No unrelated polish pass, patch, crop, composite, inpaint, or rejected-image
input is allowed.

## Clean prompt reset

If the same numbered criterion survives v1 and targeted v2, v3 is a full
clean-slate rewrite of the generation prompt and composition strategy. The
fresh builder receives the base packet, last two compact reports, and repeated
criterion numbers. It does not receive earlier issued prompts, candidates,
proofs, audits, or builder history.

The reset may rethink framing, staging, hierarchy, and panel composition. It
may not change exact strings, page intent, story facts, approved references,
critic card, page count, `07-PAGE-CONTRACT.md`, or `08-FULL-SCRIPT.md`.

If that repeated criterion survives the clean reset, stop before another
generation as a resistant-defect owner hold. If repetition first appears from
v2 to targeted v3, v4 may be the clean prompt reset.

## The v4 ceiling

The count is total completed candidates from v1 and never resets. Any v4
`REVISE` stops the run. No v5, autonomous redesign, split, component generation,
or story-document change. The owner decides what happens next.

## Mechanical routes

After the critic report is validated, the router returns exactly one:

- `PROMOTE`
- `TARGETED`
- `FULL_PROMPT_RESET`
- `RESISTANT_DEFECT_HOLD`
- `V4_OWNER_HOLD`
- `INVALID_CRITIC_REPORT`

The orchestrator never opens the art or substitutes its own visual judgment.

## Promotion

On unconditional validated `APPROVED` only:

1. copy the exact candidate bytes into `pages/page-NN.png`;
2. verify source and destination SHA-256 match;
3. derive promoted 600 × 900 and 768 × 1152 proofs;
4. append the authoritative ledger row with version, report, and hash;
5. run the bundled verifier once;
6. release Page N+1.

An owner tolerance is recorded beside the unchanged original critic report; it
is never rewritten as critic approval.

## Holds

| Hold | Trigger |
|---|---|
| Invalid critic report | report violates the numbered material-harm contract |
| Resistant defect | same criterion survives targeted correction and clean reset |
| v4 ceiling | any valid v4 `REVISE` |
| Batch milestone | after Page 40 and Page 49 |
| Protected authority | proposed edit to page contract or full script |

---

# 8 · Evidence and ledger

The append-only running record is `qa/production-ledger.md`. One row is added
only after promotion.

```text
qa/production/page-NN/
  prompts/page-NN-vK.md
  candidates/page-NN-vK.png
  audits/page-NN-vK.md
  proofs/page-NN-vK-600x900.png
  proofs/page-NN-vK-768x1152.png
  critic-vK.md
```

The neutral review capsule contains only the current candidate and two proofs,
plus the critic's neutral report path. It never contains a prompt or audit and
is not historical evidence; the archived production folder is.

Rejected candidates and their evidence remain on disk but never become image
inputs or continuity anchors.

---

# 9 · Remaining-run failure watchlist

At each batch boundary verify:

1. Every completed candidate has exactly one archived independent critic report.
2. No builder or critic context was reused.
3. No critic received a generation prompt, builder audit, prior report, or
   version history.
4. No orchestrator opened a candidate, proof, or image-tool result.
5. No rejected candidate was attached as an image input.
6. Every `REVISE` passed the numbered material-harm/redraw validator.
7. Every repeated criterion followed targeted → clean reset → owner-hold
   routing, with no improvised extra attempts.
8. Nobody measured lettering or panel shares; blind transcription and the
   reader event remained the gates.
9. No “still processing” polling turns were emitted.
10. Canonical bytes match the approved candidate hashes.

---

# 10 · Current executor entry point

Do not execute this large master plan inside production. It is the assembled
authority and audit artifact. The remaining run begins from the compact current
entry point:

```text
SESSION-START.md
```

That starts one fresh Luna-medium orchestrator for Pages 33–40. After the Page
40 milestone passes, it stops. A brand-new task begins from:

```text
SESSION-START-PAGES-41-49.md
```

All image generation is subscription-backed Codex in-app. No API-key, bundled
CLI, or separately billed API fallback is authorized.
