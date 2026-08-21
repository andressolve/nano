# Volume II reader/publication critic

You are one fresh, zero-history GPT-5.6 Sol-medium reader critic. Review the
finished local implementation independently. Do not edit files.

## Inspect

- `index.html`
- canonical `pages/page-01.png` through `page-49.png` only as they appear in the
  reader
- `../stories.js` and the rendered root catalog
- `qa/_publication/verify-reader.py` output

Do not open production prompts, audits, rejected images, production-task
history, or the builder receipt before judging.

Use the local browser and test at a desktop viewport and a tablet viewport:

1. Page 1 loads with correct title, counter, movement, and no broken asset.
2. Previous/next, page-edge navigation, keyboard navigation, touch behavior,
   `#page-N` reload, saved position, and adjacent navigation behave coherently.
3. Contents covers all six movements and 49 pages exactly once; selection and
   bookmarks work and persist.
4. Zoom opens centered at 150%, supports all required levels, pan/scroll,
   page navigation, and clean close/return behavior.
5. Page 49 leads to a non-page ending state and then a five-question quiz;
   neither is counted as Page 50.
6. Every quiz question has one correct answer, correct feedback, and tests the
   story's causal or moral logic rather than trivia.
7. Volume I and library links resolve correctly.
8. The root catalog card appears, uses the canonical Page 1 image, and links to
   the Volume II reader.
9. There are no console errors, missing files, stale 55-page/Volume-I labels,
   clipped controls, or reader-blocking desktop/tablet layout failures.

Cosmetic preference and redesign suggestions are nonblocking. A `REVISE`
finding must name reproducible reader harm or broken publication behavior and a
concrete correction.

Write `qa/_publication/reader-critic.md` with a concise report ending in exactly
`APPROVED` or `REVISE`. Do not publish or commit.
