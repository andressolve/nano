# OÙ EST LA BIBLIOTHÈQUE ? — QA

## Production result

- References reused (none newly generated): `french/les-jeux-video/refs/ref-hugo-leo-gaming.png`, `french/demain-il-fait-beau/refs/ref-rain-cafe-football.png`
- Finished page: `pages/page-01.png` — 1024×1536, SHA-256 `712a4ababe1eaabde5cce723a11336697d5a9ff87f8901762829a8bdf55addbb`
- Candidates kept for the record: `pages/page-01-candidate-v1.png` (REVISE), `pages/page-01-candidate-v2.png` (APPROVED, identical bytes to `page-01.png`)
- Reader: `index.html`
- Image path: `mcp__gemini-pro-thin__compose_images` (Gemini image endpoint), run inside a Claude Code session. Not the Codex/ChatGPT ImageGen path used for the two prior comics.

## Review trail (independent builder/critic agent loop)

### Round 1 — candidate v1 — verdict REVISE

| Check | Result |
|---|---|
| Exactly four panels, clean 2×2 grid | PASS |
| Exactly four balloons, one per panel | PASS |
| Panel 1 text exact — `Bonjour ! Où est la bibliothèque ?` | PASS |
| Panel 2 text exact — `Va tout droit.` | PASS |
| Panel 3 text exact — `Puis, tourne à gauche.` | PASS |
| Panel 4 text exact — `La bibliothèque est là !` | PASS |
| Accents, apostrophes, French spacing before `!`/`?` | PASS |
| Panel 1 balloon tail terminates at Hugo's mouth | FAIL — landed in empty space/foliage above his head |
| Hugo matches reference | PASS |
| Léo matches reference (deep brown skin, short tight black curls) | **FAIL — rendered with pale skin and loose light-brown wavy hair** |
| Woman consistent across panels 1–3 | PASS |
| Panel 2 vs. panel 3 gestures visually distinct | PASS |
| Panel 4 library cues, woman/dog correctly absent | PASS |
| No stray text/marks outside the four balloons | **FAIL — stray "2" numeral in bottom margin** |
| Art register matches prior comics | PASS |

**Required fixes:** correct Léo's skin tone/hair; remove the stray numeral; improve (not required to perfect) the panel-1 tail.

### Round 2 — candidate v2 (repair pass) — verdict APPROVED

| Check | Result |
|---|---|
| Léo's skin tone/hair corrected, consistent across all four panels | PASS |
| Stray numeral removed; full-page margin/gutter scan clean | PASS |
| Panel 1 balloon tail | Improved — lands near Hugo's head/hairline, not pixel-perfect at the mouth; accepted as a minor, non-blocking imperfection |
| All Round-1 passes re-verified with no regressions | PASS |
| Total cast: Hugo, Léo, the woman, one dog | PASS |

No further revision rounds were needed.

## Reader audit

- Responsive portrait-page sizing at desktop and mobile widths, matching the `les-jeux-video` reader template exactly (single-page pattern, not the two-page `demain-il-fait-beau` variant).
- Comic appears before any lesson commentary or questions.
- Three optional comprehension checks use only language already present in French Starter lesson 13 (plus the established `Bonjour !` greeting).
- Correct answers are revealed after each choice; final score appears after all three questions.
- Direct link returns to the shared French Starter course.
- Not yet verified in a live browser this session — recommend a quick manual open before considering the reader fully signed off.

## Accepted imperfection

The neighbor is drawn holding a walking stick/cane in addition to the dog's lead — not specified in the prompt, but harmless (doesn't add text, doesn't change cast count, doesn't touch any lesson content) and was accepted rather than triggering a third revision round. The panel-1 balloon tail (see Round 2) is likewise accepted as a minor, non-blocking imperfection.

## Curriculum note

At session start the user confirmed the children have now completed through **Lesson 13** (previously confirmed boundary was Lesson 11, per `french/HANDOFF.md` 2026-08-13). Lesson 12 is a pure review quest of Lessons 1–5 with no new language. Lesson 13, "Find your way around town," is the first genuinely new lesson since the second comic and is the sole new-vocabulary source for this comic (plus one already-established Lesson 1 greeting). Full Lesson 13 content was re-extracted from the live course's `course-chapter-2.js` rather than trusted from memory.
