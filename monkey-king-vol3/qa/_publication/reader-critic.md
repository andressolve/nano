# Reader critic — Monkey King, Volume III: Sent Away

Fresh zero-history review of `index.html`, canonical pages (as referenced), and
`verify-reader.py` output (CLEAN, exit 0).

1. **Load / mapping** — Static markup shows Page 1, "Still Walking West", "Page 1 of 49",
   "Volume III · Sent Away"; render() then sets the movement label to "The Ridge"
   (regex strips the roman numeral). `fileFor(i)` gives `pages/page-NN.png`; 49
   titles; preload and story rendering are bounded to `< titles.length`. Pages
   01–49 exist at 1024×1536, nothing beyond.
2. **Navigation** — `totalStates` = 51 (49 pages + end + quiz). Prev disabled at
   index 0, next disabled at quiz. Tap zones, arrows/PageUp/PageDown, Space
   (pages only), Home/End, swipe (52px, horizontal-dominant) all go through
   goPrevious/goNext. `#page-1` → 0, `#page-49` → 48, `#end` → end state,
   `#quiz` → quiz, `#page-0`/`#page-99`/junk → null → saved position
   (validated 0–48) or 0; hashchange ignores invalid hashes. Saved position is
   clamped to 48, so a reload after the end opens on Page 49, and the URL hash still
   holds `#end`/`#quiz` exactly.
3. **Contents / bookmarks** — Six movements 1–5, 6–19, 20–22, 23–34, 35–40,
   41–49: contiguous, each page once. Bookmarks stored under
   `monte_inspired:monkey-king-vol3:bookmarks`, position under `…:page`,
   filtered to valid indices, try/catch guarded; disabled on non-page states.
4. **Zoom** — Opens at 150% horizontally centered, top-aligned; levels
   Fit/125/150/200/250/300; +/−/0 keys, double-click, mouse drag-pan, native
   scroll; prev/next inside zoom with disabled ends; close returns to the same
   page; resize re-fits; zoom disabled on end/quiz.
5. **Ending** — Page 49 → "End of Volume III" (counter "End") → quiz (counter
   "Quiz"); neither counted as Page 50. Only link is the internal `#quiz`;
   Volume IV mentioned as plain text only.
6. **Quiz** — Five questions, one `data-answer` each, a/b/c values all valid;
   pick-first prompt, inputs lock after checking, score tally correct. Questions
   test causes and choices (why the monk kept saying the words, Wukong asking
   first, the tiger's refusal, Bajie's confession, the star sent home).
   I checked the claims against pages 14, 33, 43 and they match the art and dialogue.
   Nonblocking: the correct option is usually the longest.
7. **Hygiene** — No stale foreign or Vol II terms, no 48-page labels, no
   duplicate IDs, no getElementById reference to a missing ID.

No reproducible reader harm found.

APPROVED
