# French Comics — session handoff

Updated: 2026-08-19

## Current state

The French Comics collection is live and published inside Nano.

- Nano: `https://andressolve.github.io/nano/`
- Collection: `https://andressolve.github.io/nano/french/`
- First comic: `https://andressolve.github.io/nano/french/les-jeux-video/`
- First-collection commit: `7918a1174cde0b4d155b70a95ca9f8a5ca820872` (`Add French Comics collection`)
- Second-comic commit: `6f73790eadd139ba038f570fbb3df7161b66843c` (`Add second French Starter comic`)
- Third comic: `Où est la bibliothèque ?`, produced 2026-08-19, folder
  `french/ou-est-la-bibliotheque/`. Commit hash and live-URL confirmation to be
  added here once pushed — see "Third comic published" below.

The second comic, `Demain, il fait beau !`, was approved, completed, committed,
and published on 2026-08-13. Its two finished pages, reader, optional checks,
production evidence, and catalog entry are under
`french/demain-il-fait-beau/`.

- Live reader: `https://andressolve.github.io/nano/french/demain-il-fait-beau/`
- GitHub Pages deployment: successful
- Both public page PNGs were downloaded after deployment and matched their
  canonical local files byte-for-byte by SHA-256.

`Les jeux vidéo` is the first accepted French comic after several failed approaches. Treat it as the working model unless the user explicitly changes direction.

## New-session setup note

The current ChatGPT thread continued to display **Ultra** even after the user
asked to move to **Extra High**. The user-level Codex config now contains:

```toml
model = "gpt-5.6-sol"
model_reasoning_effort = "xhigh"
```

The desktop build in this session did not recognize `/reasoning`. When opening
the replacement session, verify that the new chat displays **Extra High**
before beginning production. If it still displays Ultra, fully quit and reopen
ChatGPT, then create a new chat. Do not tell the user that changing
`config.toml` retroactively changes an already-open thread.

## Read first in a new session

1. Root `AGENTS.md` — especially local command stability, image-generation billing, reference locking, lettering, and direct-to-`main` publishing rules.
2. `french/README.md` — collection structure and publishing rules.
3. This handoff.
4. `french/les-jeux-video/00-PROJECT-BIBLE.md` — the successful comic’s script and constraints.
5. `french/les-jeux-video/QA.md` — accepted result and known imperfection.
6. `french/demain-il-fait-beau/00-PROJECT-BIBLE.md` — the accepted two-page
   structure and exact script.
7. `french/demain-il-fait-beau/QA.md` — page hashes, generation audits, and
   final sequence gate.
8. `french/ou-est-la-bibliotheque/00-PROJECT-BIBLE.md` — the third comic's
   script and constraints (Lesson 13, directions in town).
9. `french/ou-est-la-bibliotheque/QA.md` — its builder/critic review trail,
   including the one revision round.
10. `french/catalog.js` — the learner-facing French catalog.

Source course: `https://francisco-french-starter.brutus.chatgpt.site/course/`,
which now ships as **two separate JS data files**: `course/course-data.js`
(Lessons 1–10) and `course/course-chapter-2.js` (Lessons 11–18). Fetch both
when re-extracting vocabulary — trusting only the first file silently misses
everything past Lesson 10.

The user confirmed on 2026-08-18 that the children had **completed through
Lesson 13** (superseding the 2026-08-13 confirmation of Lesson 11 below).
Lesson 12 is a pure review quest of Lessons 1–5 with no new language. This is
the authoritative learner boundary as of this update — re-confirm with the
user before writing a fourth comic, since this number has moved twice already.
The live course contained eighteen lessons at last check:

1. Hello and how are you?
2. Getting help in French
3. Introduce yourself
4. Numbers and age
5. Likes and dislikes
6. Read a whole tiny conversation
7. School and free time
8. Order at a café
9. Talk about family
10. Make a simple plan
11. Weather and what to wear
12. The passport checkpoint — review of Lessons 1–5
13. Find your way around town
14. Tell the story of your day
15. The mystery picnic — review of Lessons 6–10
16. Choose and buy something
17. Say how you feel—and why
18. The French adventure finale — whole-course review

Lessons 14–18 are live but are **not** part of the confirmed learner boundary.
Do not use their language until the user says the children have completed it.
There is no need to ask again about Lessons 7–13 (Lesson 12 is the review
quest noted above); their completion is already confirmed here.

## What Lessons 1–11 now support

In familiar, strongly cued situations, the children have encountered enough
French to:

- greet someone, ask how they are, introduce themselves, and give a basic age;
- use communication-repair phrases such as asking for repetition, slower
  speech, or a meaning;
- express likes and dislikes about familiar interests, school, and free time;
- place a small café order and answer `Et avec ça ?`;
- mention a close family member with `J’ai` and use `il` or `elle` to give a
  name;
- invite someone, accept or decline, and state a simple plan for tomorrow;
- recognize `Il fait beau/chaud/froid`, `Il pleut`, four clothing items, and
  rehearse a tiny weather-and-clothing report.

The safest overall description is **pre-A1 moving into early A1 task
performance**. Recognition is likely ahead of cold production. Do not claim
global A1 proficiency: the course through Lesson 11 is only about 2–2.75 hours,
and it does not establish free writing, natural-speed listening, pronunciation
accuracy, or flexible grammar transfer.

The course engine distinguishes objective checks completed independently from
those completed after a hint or after the answer was shown. Its speaking step
is self-attested, so lesson completion proves exposure and supported rehearsal,
not spontaneous oral mastery. Lesson 11 also uses device-dependent browser
speech synthesis rather than fixed recorded audio. A useful optional cold
check is to hide the models, show a new weather situation, and ask each child
for `Aujourd’hui, il...` plus `Je porte...`.

## What the user wants

The children enjoy Tintin and Asterix, but that is a reading-taste signal—not a request for elaborate mysteries, period settings, imitation, lore, or clever plot machinery.

The target is:

- A simple, pleasant, entertaining short comic.
- French they have already learned, used naturally.
- A situation that makes the language feel real and relevant.
- Enough personality and visual pleasure to feel like a real comic rather than a worksheet.
- No need to impress anyone or make the premise “earth-shattering.”

The most important user calibration from this session:

> Do not try to be cute or clever. Do not manufacture a twist merely to justify a lesson phrase.

Every line must have an obvious, natural meaning in the scene. If a reader cannot tell exactly why a character says a phrase, the line or concept is not ready.

## Successful format

`Les jeux vidéo` succeeded with:

- One portrait comic page.
- Four large panels in a 2×2 grid.
- Two children.
- One ordinary modern setting.
- One simple interaction.
- One visible speaker and one balloon per panel.
- Four exact lesson-aligned exchanges.
- One combined cast/prop reference followed by one full-page generation.
- Dialogue baked into the page image.
- A lightweight reader and three optional checks after the comic.

Do not split a future page into separately generated panels unless the user explicitly changes their preference. The user questioned that approach, and the successful page was generated as one cohesive image.

The user has now explicitly said that the next comic may be **a bit more than
one page when appropriate**. This authorizes considering a compact two-page
story; it does not authorize padding. For a two-page comic, keep the proven
four-large-panels-per-page pattern, generate each page as one cohesive image,
approve Page 1 before generating Page 2, and perform a final uninterrupted
two-page read for continuity and comprehension.

## Image-generation rule

Use the subscription-backed built-in Codex ImageGen path.

Do not use:

- `OPENAI_API_KEY`
- the bundled image-generation CLI
- direct OpenAI API image calls

unless the user explicitly approves separate API billing in that conversation.

Generate and inspect a combined character/prop reference first. For a similarly small one-page comic, stop reference iteration once identity, clothing, major props, and overall register are usable. Do not repeat the `Train de nuit` failure of spending many generations perfecting a complicated reference plate.

## Accepted recurring cast

The first comic established two reusable boys:

- **Hugo:** ten; pale olive skin; tousled dark-brown hair; green overshirt over an orange T-shirt; charcoal trousers; red canvas trainers; curious and initially reserved.
- **Léo:** eleven; deep brown skin; short tight black curls; mustard-yellow hoodie; dark navy jeans; white trainers; relaxed and welcoming.

Reference: `french/les-jeux-video/refs/ref-hugo-leo-gaming.png`

Reusing them is encouraged when natural, but the collection does not require an ongoing serialized plot.

## Collection architecture

```text
french/
  index.html             collection landing page
  catalog.js             published French comics only
  french.css
  home.js
  README.md
  HANDOFF.md
  les-jeux-video/
    index.html            comic reader and optional checks
    pages/page-01.png     finished page
    refs/                 production reference
    project notes and QA
  demain-il-fait-beau/
    index.html            two-page reader and optional checks
    pages/                two canonical finished pages
    refs/                 accepted supplemental reference
    qa/                   candidates and reduced sequence proofs
    project notes and QA
  ou-est-la-bibliotheque/
    index.html            comic reader and optional checks
    pages/page-01.png     finished page, plus kept revision candidates
    project notes and QA (no new refs/; reused prior comics' references)
```

Nano’s main `stories.js` contains one entry for the **French Comics** collection. Do not add every one-page French comic to the main catalog. Add future accepted comics only to `french/catalog.js`.

## Legacy work

The following are failed or superseded production history and are intentionally unlinked:

- `french-comics/`
- `train-de-nuit/`

Do not continue either project or copy its production architecture into a new comic. Read them only if a specific postmortem is needed.

Failure patterns to avoid:

- Unrelated bridge vocabulary driving the premise.
- Six-panel pages with too many actors, balloons, props, and causal staging demands.
- Historical machinery, crowds, labelled diagrams, exact numbering, mixed scribble balloons, or other brittle generation requirements.
- Using `Je ne comprends pas.` as a generic reaction when the reader cannot tell what is not understood.
- Building a mystery, thief, magical object, or twist merely to make course phrases “do plot work.”
- Treating beginner French as preschool material.

## Git and worktree safety

The repository has many unrelated modified and untracked files. Never stage broadly.

For a requested commit/push:

- Verify the branch is `main`.
- Fetch and ensure `main` is synchronized with `origin/main`.
- Stage explicit French-task paths only.
- Commit directly to `main`.
- Push `origin main`.
- Wait for GitHub Pages and verify the public Nano homepage, French collection, target reader, and page image.

Never use `git add -A`, stash, reset, clean, a feature branch, or a pull request unless the user explicitly requests it.

## Second comic published

The user approved the proposed two-page comic **Demain, il fait beau !**. It
reuses Hugo and Léo, adds one café server, and is complete and live.

Production files:

- project bible: `french/demain-il-fait-beau/00-PROJECT-BIBLE.md`
- exact prompts: `french/demain-il-fait-beau/01-IMAGE-PROMPTS.md`
- QA ledger: `french/demain-il-fait-beau/QA.md`
- approved supplemental reference:
  `french/demain-il-fait-beau/refs/ref-rain-cafe-football.png`
- canonical pages: `french/demain-il-fait-beau/pages/page-01.png` and
  `french/demain-il-fait-beau/pages/page-02.png`
- finished local reader: `french/demain-il-fait-beau/index.html`
- live reader:
  `https://andressolve.github.io/nano/french/demain-il-fait-beau/`

Both pages are 1024×1536. Each has exactly four panels, four correctly
attributed balloons, and the exact approved text. The final two-page sequence
proof is `french/demain-il-fait-beau/qa/two-page-sequence-proof.png`.

### Final exact script

Two portrait pages, exactly four large panels per page, read left-to-right and
top-to-bottom. One visible speaker and one balloon per speaking panel.

#### Page 1 — Rain and the café

1. Rain begins while Hugo and Léo are outside. A football is already visible
   so the later invitation has a visual source. HUGO: `Il pleut.`
2. They enter a warm café. HUGO: `Bonjour ! Je voudrais un chocolat chaud,
   s’il vous plaît.`
3. The server continues the order. SERVER: `Et avec ça ?`
4. Léo indicates the pastry display. LÉO: `Un croissant, s’il vous plaît.`

#### Page 2 — Tomorrow’s plan

1. Still at the counter, Hugo closes the order. HUGO: `C’est tout, merci.`
2. At a table, with the same football visibly beside them, Hugo makes the
   invitation. HUGO: `Tu veux jouer demain ?`
3. Léo accepts. LÉO: `Oui, avec plaisir !`
4. Clear next-day transition: bright sun, changed outdoor location, and both
   boys playing football. LÉO: `Il fait beau !`

All eight balloons use exact language already encountered in Lessons 8, 10,
and 11. The causal spine is intentionally plain: rain leads to a café stop; the
boys make a plan; good weather lets them play the next day. Rainwear and boots
may carry Lesson 11 visually without forcing unnatural dialogue.

### Production record and locks

- Reuse the accepted Hugo/Léo identity reference.
- Make one minimal supplemental reference for rainwear, the football, the café
  counter, and the single server; do not overdevelop the reference sheet.
- Keep the football present from Page 1 through the café scene so it does not
  materialize only when the invitation is spoken.
- No additional dialogue, captions, translations, labels, prices, menu text,
  logos, or sound effects.
- Generate and inspect each complete page through subscription-backed built-in
  Codex ImageGen. Do not use an API key or the imagegen CLI.
- Do not generate Page 2 until Page 1 has passed exact-text, attribution,
  identity, anatomy, and reader-comfort review.
- After both pages pass individually, review them as one uninterrupted story
  before building the reader or catalog entry.

## Third comic published

The user approved a third comic, **Où est la bibliothèque ?**, built this
session (2026-08-19) after confirming the children had reached Lesson 13.

- One portrait page, 1024×1536, the same four-panel 2×2 grid as `Les jeux
  vidéo`.
- Hugo asks a neighbor where the library is; she says go straight, then left
  (two visually distinct gestures); Léo spots the library.
- All language is Lesson 13 ("Find your way around town") plus the
  established Lesson-1 `Bonjour !` greeting.
- Reused both prior comics' existing references
  (`french/les-jeux-video/refs/ref-hugo-leo-gaming.png` and
  `french/demain-il-fait-beau/refs/ref-rain-cafe-football.png`); no new
  reference art was generated.
- Built by a Claude Code session, not a Codex/ChatGPT session — this session
  only had the `gemini-pro-thin` image MCP available, so pages were generated
  with `compose_images` rather than the Codex ImageGen path. Re-verify which
  image tooling is available at the start of a session rather than assuming
  the rule above always applies unchanged.
- One builder/critic revision round was needed: the first candidate drifted
  Léo's identity (pale skin, loose light-brown wavy hair instead of deep
  brown skin and short tight black curls) and left a stray "2" numeral in the
  bottom margin. A targeted repair pass fixed both; the second candidate was
  approved. Full trail: `french/ou-est-la-bibliotheque/QA.md`.
- Production files: `french/ou-est-la-bibliotheque/00-PROJECT-BIBLE.md`,
  `01-IMAGE-PROMPTS.md`, `QA.md`, `index.html`, `pages/page-01.png`.
- Added to `french/catalog.js` (not root `stories.js`, per the rule above).

### Exact start for the next session

1. Verify that the new chat shows **Extra High** (Codex-session note; not
   applicable if working from a Claude Code session).
2. Read the files listed in “Read first in a new session,” then inspect
   `french/ou-est-la-bibliotheque/QA.md` for the most recent production
   record.
3. Treat the first three comics as complete. Do not regenerate any reference
   or page unless the user identifies a concrete defect.
4. The authoritative confirmed learner boundary is Lesson 13 as of
   2026-08-18/19 — this has moved twice already (11 → 13). If the user wants
   another story, re-confirm the boundary first rather than trusting this
   document; do not silently use Lessons 14–18.
5. There is no approved fourth-comic concept or script yet. Begin with the
   children’s current lesson boundary and the same natural-scene standard.
6. Do not commit or push unless the user asks. If asked, follow the root rule:
   stage only the relevant French paths, commit directly to `main`, push
   `origin main`, wait for GitHub Pages, and verify the collection and new
   reader publicly.

The bar is not novelty. The bar is: would the children willingly read this small scene, and does every French line make immediate sense?
