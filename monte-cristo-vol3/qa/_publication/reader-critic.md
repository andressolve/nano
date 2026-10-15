# Reader critic: Monte Cristo Volume III

Fresh, zero-history review of `index.html`, with page 1 and page 56 proofs checked against the reader's labels, plus `verify-reader.py`.

**Verifier:** `CLEAN` (exit 0).

## Checks

1. **Page 1 load:** The static markup and `render(current, true)` both show `pages/page-01.png`, "The Second Man", "Page 1 of 56", and Movement I. `titles` has 56 entries. `fileFor` pads to `page-NN.png`. Page loading and preloading are limited to indexes 0–55. All 56 files exist, and nothing exists beyond page 56. The page 1 art (title page, Villefort introduced as the second man) and the page 56 art ("She's holding on.") match their titles.
2. **Navigation:** `goPrevious` and `goNext` are clamped to 0..57. `prev` is disabled on page 1, and `next` is disabled on the quiz. Tap zones, arrow, PageUp and PageDown keys, and horizontal swipes (at least 52 px, mostly horizontal) all use the same functions. Space moves forward on story pages only. Home and End go to pages 1 and 56. The `#page-N` and `#N` hashes route to 1–56. `#end` and `#page-57` route to the ending, and `#quiz` and `#page-58` route to the quiz. Any other hash (for example `#page-99` or `#page-0`) returns null, so the saved position is used instead. The saved position is clamped to 0–55, so a stored ending or quiz never becomes a phantom page. `updateUrl` rewrites the hash with `replaceState`.
3. **Contents and bookmarks:** Six movements (1–8, 9–18, 19–27, 28–39, 40–47, 48–56) are contiguous and cover all 56 pages exactly once. The header reads "56 pages". Bookmarks are stored under `monte_inspired:monte-cristo-vol3:bookmarks` and the position under `monte_inspired:monte-cristo-vol3:page`. Both are filtered to valid indexes, and storage is wrapped in try/catch. Bookmarks are disabled on the ending and the quiz.
4. **Zoom:** Zoom opens at 150% (one of six levels: Fit, 125, 150, 200, 250, 300), scrolled to the top and centered horizontally. The −, +, Fit, and double-click controls work, and the keys + / − / 0 / B work. The view pans by scrolling and by dragging with a mouse, and touch pinch is allowed. The previous and next buttons inside zoom are disabled at pages 1 and 56. Close uses `dialog.close()`, and zoom is unavailable on the ending and the quiz.
5. **Ending and quiz:** After page 56, the next state is "End of Volume III" with the counter "End". Next comes the quiz with the counter "Quiz". Neither is labeled Page 57. The ending's only link is the in-page `#quiz` link. "The story continues in Volume IV" is plain text.
6. **Quiz questions:** Each of the five questions has one correct radio answer (b, a, c, b, a), and the feedback matches the answer key. Each question tests a cause or a choice: why he hands over the bottle, why Villefort says "Don't tell me", why the false death, how the trial destroys Villefort, and why the Count can't say "Two". The language is plain. Each question can be checked once, without a selection a "Pick one" prompt appears, and the running and final scores are correct.
7. **Hygiene:** There are no Beowulf, Arthur, Three Kingdoms, Musketeers, or Volume II terms or keys, and no 57-page labels. All 45 element IDs are unique. Every `getElementById` target exists.

## Nonblocking notes

- A `hashchange` to an out-of-range hash leaves the bad hash in the URL while the page stays the same. This causes no harm to the reader.
- In zoom, the arrow keys do not turn pages. The on-screen previous and next buttons do.

APPROVED
