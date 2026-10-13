# King Arthur, Volume I — reader critic report

Fresh, zero-history review of `index.html`, the canonical pages as the reader
references them, and `verify-reader.py` (output: `CLEAN`, exit 0).

## Judgments

1. **Page 1 load / file mapping — pass.** Static markup and `render(current, true)`
   both show "The Storm", "Page 1 of 59", movement "The Hidden King". `titles`
   has 59 entries; `fileFor` maps index 0–58 to `pages/page-01.png`–`page-59.png`;
   `preload` and `loadPage` callers never step beyond index 58. Disk holds exactly
   page-01…page-59.
2. **Navigation at both ends — pass.** Prev disabled at page 1; next from page 59
   goes to End, then Quiz, where next is disabled. Tap zones, arrow/PageUp/PageDown,
   Home/End, swipe all route through `goPrevious`/`goNext`/`render`. `#page-N`
   (and bare `#N`) reload to N for 1–59; `#end`/`#quiz` reload to those states;
   an out-of-range hash (e.g. `#page-99`) falls back to the saved position and the
   URL is rewritten. Saved position is clamped to page 59, so leaving from End/Quiz
   reopens on 59. Space is suppressed on End/Quiz; arrow keys on quiz radios are
   left to the browser.
3. **Contents / bookmarks — pass.** Seven movements, ranges 1–7, 8–19, 20–27,
   28–36, 37–43, 44–50, 51–59: each of 59 pages exactly once. Bookmarks and
   position persist under `monte_inspired:king-arthur-vol1:bookmarks` / `:page`,
   filtered to valid story indices; bookmarking is disabled on End/Quiz.
4. **Zoom — pass.** Opens at 150% horizontally centered at the top; levels Fit,
   125, 150, 200, 250, 300%; +/−/0 keys, Fit button, double-click toggle; native
   scroll plus mouse-drag pan; in-zoom prev/next with next disabled at page 59
   (never enters End); Escape/× close back to the same page.
5. **Ending / quiz — pass.** End and Quiz are non-page states (counter "End"/
   "Quiz", zoom and bookmark disabled, no image). End links only to `#quiz`; nothing
   unpublished is referenced. Five questions.
6. **Chronicle pages — pass.** Pages 7, 19, 27, 36, 50, 59 are ordinary entries
   ("Who Built the Walls?", "Did It Really Happen?", "Was There a Real Arthur?",
   "Shining Armour", "Two Magic Swords?", "Who Made It Up?"), counted and routed
   like every other page; proofs of 19 and 59 confirm vellum Chronicle content.
7. **Quiz — pass.** One `data-answer` per question; check logic compares the
   selected value, locks the question, shows the matching feedback, and tallies
   score. Questions test causes and choices (why he pulled the sword; what really
   won Bedegraine; why he refuses Pellinore; why the table is round; how we know
   the stone is legend). Answers verified against pages 10, 30–32, 48, 52, 19, 59.
   Language is plain and followable.
8. **Stale terms / IDs — pass.** No Monte Cristo, Musketeers, or Three Kingdoms
   terms, keys or links; no 50-page labels; no duplicate IDs; every
   `getElementById` target exists.

## Nonblocking notes

- Navigating pages inside zoom resets scroll to top-left rather than re-centering
  horizontally (cosmetic; the page is fully reachable by scroll).
- A hash changed in-session to an out-of-range value is ignored without rewriting
  the URL (no reader harm).
- `#page-60`/`#page-61` are aliases for End/Quiz; they are never displayed as page
  numbers.

APPROVED
