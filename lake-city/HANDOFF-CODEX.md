# HANDOFF — CODEX EXECUTION

> ## ⚠️ STATUS 2026-08-02 — REVISED EDITION COMPLETE; AWAIT USER QA / COMMIT
>
> The original production run was committed and pushed to `main` as `3864f3d` (`Publish The Lake City book one`). After publication, the script was revised for effortless reading and the revisions were propagated into a complete local replacement edition. **Do not regenerate or redesign it.** The active local reader map is Page 1 v3, 2 v2, 3 v2, 4 v6, 5 v3, 6 v3, 7 v6, 8 v3, 9 v3, 10 v4, 11 v3, 12 v7, 13 v2, 14 v3, 15 v4, 16 v5, 17 v4, 18 v3, 19 v4, 20 v4, 21 v3, 22 v3; cover remains `cover-v2.png`.
>
> Both independent critics passed the earlier frozen revised script and rendered book. During user QA, Page 4 P2 was still found semantically ambiguous: `My son says no` did not name the decision, and the attendant could be mistaken for the son. `page-04-v6.png` is the active repair, with explicit wording and clearly subordinate attendant staging. User QA also caught `AHIEAD` for `AHEAD` in Page 12 P1; `page-12-v7.png` is the active exact-text repair. Page 15 P4's vague `this city could arrange that` was replaced in `page-15-v4.png` with an explicit account of the rulers maintaining the encirclement and preventing salt purchases. The evidence and iteration history are in `SCRIPT-CRITIC-REPORT.md`.
>
> Remaining work: **user QA, then—only when explicitly requested—commit and push the revised edition.** Stage only the changed/untracked files inside `lake-city/`; the worktree contains extensive unrelated user work. Do not stage root `index.html`, `stories.js`, or anything outside `lake-city/` unless the user explicitly expands scope. The checkout is `main`, and the repo rule is to publish routine completed work directly to `origin/main`.
>
> Image production used the built-in subscription-backed Codex image path. No `OPENAI_API_KEY`, CLI, or separately billed API path was used. If any later image repair is requested, inspect the active page and every referenced PNG first, use one whole-page edit with all refs, fix one defect only, save a versioned sibling, and rerun both critics.
>
> **Everything below this box is the original production brief, kept for the record.**

Planning is done. Everything in this folder is finished and approved. **Your job is production only: nine refs, three prototypes, twenty-three pages, then the reader, the quiz, and the landing card.** Do not redesign the book. If something in the script genuinely cannot be rendered, say so in writing rather than quietly substituting.

---

## 1. Read order

Read all six, in this order, before generating anything.

1. `00-PROJECT-BRIEF.md` — what the book is, the arc, the editorial rules.
2. `01-STYLE-GUIDE.md` — the verbatim style block, the anti-drift block, the validated panel grids, the lettering rulebook, the six-block prompt template.
3. `RESEARCH.md` — **ground truth. If the script and this file disagree, this file wins.** It also lists what must never be depicted or quoted.
4. `02-CHARACTERS.md` — the nine locks and the ref template.
5. `03-SETTINGS.md` — the thirteen locations.
6. `04-SCRIPT.md` — cover + 22 pages, each with GRID / REFS / T / panel beats / verbatim lettering.

Then open `style-samples/sample-A-codex-inkline.png` and look at it. That image is the register the user approved. Open it again any time a page starts feeling off.

---

## 2. Tooling

| | |
|---|---|
| Generate | `mcp__openai-image-2__generate_image` |
| Edit / anchor on refs | `mcp__openai-image-2__edit_image` |
| Size | `1536x1024` — **always. Never portrait.** |
| Quality | `"high"` — always. `medium` collapses caption legibility. |
| `thinking` | Leave it off. It is broken in the current build (HTTP 400). |
| Refs per call | `imagePaths` accepts **1–16**. |

**`edit_image` takes multiple refs natively.** The graphic-novel skill still documents a one-ref hard limit and a composite-plate workaround — that section is **out of date**; the wrapper was upgraded and smoke-tested 2026-07-05. Do not build composite plates for this volume. Attach every locked character on a page via `imagePaths`.

Output paths:

- refs → `lake-city/refs/ref_<name>.png`
- pages → `lake-city/pages/page-NN.png`, cover → `lake-city/pages/cover.png`

---

## 3. The prompt is six blocks, in this order

Verbatim from `01-STYLE-GUIDE.md`. **Do not reorder and do not paraphrase.**

```
LAYOUT     → the GRID line from the script, verbatim, + the panel-border line
STYLE      → the style block, verbatim
ANTI-DRIFT → the anti-drift block, verbatim
CHARACTERS → the lock blocks, verbatim from 02-CHARACTERS.md
PANELS     → the panel beats from the script
LETTERING  → "LETTERING — verbatim, render exactly:" + every text element + the restrictions block
```

Why the order matters: layout and style pin the register before subject content can pull it; anti-drift lands before a teenage protagonist enters the locks; lettering goes last so caption words don't get painted onto clothing.

Non-negotiables inside the blocks:

- **Never write a famous person's name into a prompt.** Not "Moctezuma," not "Cortés," not "Malintzin." The visual description IS the lock. Names in prompts pull the model toward stock Wikipedia portraits. Names live in the script's narration and in the ref filenames only.
- Every speech-bubble tail must be pointed at a **named visible figure** ("tail pointing to the barefoot boy in the coarse pale-brown cloak on the LEFT"). An unassigned tail is how a line ends up in the wrong mouth.
- Close every prompt with the restrictions block from `01-STYLE-GUIDE.md`, including `DO NOT include any quotation marks inside speech bubbles — the bubble shape is the quote.`
- **One-shot whole-page bake.** Every panel and every word in a SINGLE call. Never generate panels separately and composite. Never add text with code — the user's standing rule is that code-lettering never works for him.

---

## 4. Refs first — the gate

Nine refs, `generate_image`, one at a time, template in `02-CHARACTERS.md` §Reference-sheet generation. ≈$1.90.

```
ref_olin.png                  ref_malintzin.png
ref_tototl.png                ref_captain.png
ref_xicotencatl_younger.png   ref_speaker.png
ref_xicotencatl_elder.png     ref_xiuhtototzin.png
ref_maxixcatzin.png
```

Run the casting gate in `02-CHARACTERS.md` on each one. The check that matters most is **caste**: coarse maguey fibre, above the knee, barefoot, no jewellery on the commoners; cotton to the ankle, jade, sandals on the nobles. If Olin looks well-dressed, the ref failed — regenerate. Also verify Olin's uncut nape lock, the Speaker's thin sparse beard and gold-soled sandals, and the red-and-white Tlaxcalan headbands.

**No page is generated until all nine pass.**

Two hard rules once you start pages:

1. **`ls refs/` immediately before each page batch and confirm every filename you are about to pass exists.** The MCP does not fail loudly on a missing ref — it silently substitutes something plausible and the page is unusable as a locked page.
2. **Re-Read the actual ref PNG and write one line describing what you see, before writing the page prompt.** Not from memory, not from the lock block. The lock was the *target*; the ref is the *truth*, and the ref is what the page will look like.

---

## 5. Prototypes before any bulk run

Three pages, reviewed individually, before you generate anything else. They were chosen to span the three ways this book can break.

| Order | Page | Tests |
|---|---|---|
| 1 | **P9** — the hero splash, first sight of the lake | Can the register carry a full-bleed landscape at maximum turquoise? This is the page the whole book is written to earn. |
| 2 | **P12** — the causeway meeting | Four locked characters in one page at T5 density. If multi-ref anchoring holds here it holds everywhere. |
| 3 | **P14** — Turquoise Bird | Four-panel quiet dialogue at T5. Tests small-panel face consistency and heavy lettering in the same frame. |

Stop after each and check: register match, face consistency against the refs, caption legibility, spelling, correct tail assignment, no duplicated text, no invented captions. Only proceed when all three are right.

---

## 6. Bulk waves

After the prototypes pass, run in waves and review each wave before launching the next.

| Wave | Pages | Notes |
|---|---|---|
| A | Cover, P1, P2, P3, P5 | Tlaxcala. Ochre-and-dust country — hold the turquoise back. |
| B | P4, P6, P7, P8 | P4 is the T5 council page (three lords + Olin). P7 has a moderation note. |
| C | P10, P11, P13 | P11 plants the liftable beam bridge — it is the hinge of Books Two and Three. Do not soften it. |
| D | P15, P16, P17 | The city set pieces. P16 has a moderation note. |
| E | P18, P19, P20, P21, P22 | P20 and P21 have moderation notes. P22 is the closing splash. |

---

## 7. When a page gets refused

Known trap, learned the hard way on earlier volumes: **a page whose entire subject is a killing will be refused even when the words are softened.** More softening does not work.

**The fix is to change what the page is *about*** — onto the artifact, the witness, or the aftermath — and regenerate. The script has already done this preemptively on the four flagged pages (P7, P16, P20, P21); the inline notes explain what each page is deliberately *not* showing. If one is still refused:

1. Re-read the page's moderation note and the sacrifice rule in `01-STYLE-GUIDE.md`.
2. Move the camera further onto the witness — Olin's face while he listens, a scrubbed stone, smoke over a wall.
3. Regenerate. **Do not delete the honest caption to get the image through.** The book does not lie about the violence; it just doesn't depict it.
4. If a page is refused twice, stop and report it rather than watering it down a third time.

Absolute bans regardless of framing: the act of sacrifice, a body on the stone, a blade at a chest, a close study of the skull rack or any face in it, any wound or gore.

---

## 8. Repair discipline

- **One defect per regen.** Fixing three things at once produces a page with four new problems.
- Prefer a targeted `edit_image` anchored on the good page over a full reroll — *except for in-image typos.* A typo cannot be repaired by anchoring on the page that contains it; the model reproduces the misspelling. **Reword the script line and fresh-regen from the clean refs.**
- **Never overwrite an accepted page.** Save siblings — `page-10-v2.png`, `page-10-v3.png` — and only promote a replacement when it is clearly better.
- Drift check every page against the refs before moving on. Do not batch-review at the end; drift compounds.

---

## 9. Cost envelope

Refs $1.90 + 23 pages at ~$0.21 ≈ $4.85 + a small regen allowance. **Target ~$5–6 for the volume.** If you cross $8, stop and report.

---

## 10. After the pages: reader, back matter, quiz, card

**`lake-city/index.html`** — dark page-flipper, matching the collection's convention:

- `#15171c` background, Palatino serif, off-white text, `max-width: min(1400px, 96vw)`.
- Accent **turquoise `#35a7a0`**.
- Edge-anchored circular ←/→ arrows, vertically centred. Keyboard arrows + spacebar. Click left-third / right-two-thirds. Swipe on mobile. Top progress bar. Lazy-prefetch of the next page.
- **Footer concept-strip — the four acts:** `The Hatred · The Road · The City · The Silence`, lighting the active act per page, hidden on the cover. The act boundaries are in `00-PROJECT-BRIEF.md`.
- After P22: the **"A note on what is true"** back matter from the end of `04-SCRIPT.md`, rendered as an interstitial. It is not optional — it is where the book's three honest uncertainties live.
- Then the **5-question WHY quiz**, verbatim from `04-SCRIPT.md`. Correct answers are already shuffled b/c/a/d/b. Do not reorder the options; the distractors were written to be the same length and equally plausible.

**`~/Documents/nano/index.html`** — add the card. Per the landing-page convention: add it to the "Latest · just shipped" strip, drop the oldest of the six, and add a link in the graphic-novel shelf list.

**Do not commit until the user has looked at the pages.** When you do, stage `lake-city/` and the root `index.html` only — the repo has unrelated uncommitted work in other folders that must be left alone.
