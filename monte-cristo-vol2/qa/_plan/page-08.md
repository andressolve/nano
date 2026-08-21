# PAGE 8 — production plan

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
