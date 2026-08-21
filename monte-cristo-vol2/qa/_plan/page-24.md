# PAGE 24 — production plan

---

> **This is the whole plan for this page.** It carries the same sections 1-4,
> the same section 6 briefs and the same sections 7-10 as
> `12-PRODUCTION-PLAN.md`, plus this page's prompt and this page's appendix
> and nothing else. Do not open the master plan — it is the identical law for
> forty-nine pages at once, and loading it is what the run's token cost was.
> If you need a neighbouring page, open that page's file.

---

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
