# Reader critic — Monkey King, Volume II: The Road West

Inspected: `index.html` (read fully), the `verify-reader.py` output (`CLEAN`), the canonical page set (`page-01.png` through `page-48.png`, nothing else), and canonical pages 15, 20, 23, 33, 34, 40 and 45, opened only to check the quiz claims against the story.

## Routing and boundaries
- Static markup loads `pages/page-01.png`, title "Five Hundred Years", "Page 1 of 48", and movement label "Volume II · The Road West". On render, the movement label becomes "Volume II · Five Hundred Years". `fileFor` zero-pads to `page-NN.png`. The 48 titles map to 01–48. `preload` and the load path stay below `titles.length`, so nothing loads past page-48.
- `#page-1` / `#1` gives index 0. `#page-48` gives index 47. `#end` (and the inherited `#page-49` alias) gives the end state. `#quiz` (and `#page-50`) gives the quiz. An out-of-range hash such as `#page-99` returns null, so the reader falls back to the saved position or page 1, and `updateUrl` replaces the hash with a valid one. During a session, an invalid `hashchange` is ignored.
- The prev, next, edge-tap, swipe, arrow, PageUp/PageDown, Space, Home/End, and in-zoom prev/next controls all go through `clampIndex`, `goPrevious` or `goNext`. At page 1, prev is disabled. Page 48 moves forward to End, then to Quiz, where next is disabled. Space does not advance past page 48. Arrow keys are ignored while a quiz radio has focus.
- The saved position is clamped to 47, so reloading without a hash after the end or quiz reopens page 48. A reload with a hash keeps the exact state. On End and Quiz the counter reads "End" and "Quiz", never "Page 49". Zoom and bookmark are disabled there.

## Contents and bookmarks
- The seven movements run 1–4, 5–10, 11–17, 18–23, 24–29, 30–37 and 38–48. That covers all 48 pages with no repeats, and the contents eyebrow reads "48 pages". The current page is highlighted and scrolled into view.
- Storage keys are `monte_inspired:monkey-king-vol2:page` and `monte_inspired:monkey-king-vol2:bookmarks`. Saved bookmarks are filtered to valid indices and wrapped in try/catch. The star marks and the bookmark list both refresh on toggle.

## Zoom
- Zoom opens as a modal at 150%, scrolled to the horizontal center and the top of the page. It has six levels (Fit, 125, 150, 200, 250 and 300%) and the readout shows the current one. Panning works by native scroll plus mouse drag. Double-click switches between Fit and 200%. Prev/next work inside zoom and stop at pages 1 and 48. The keys +, -, 0 and B work. Close is the × button or Esc on the native dialog. On resize the image is recomputed.

## Ending and quiz
- The end state "End of Volume II / Then He Waited" is not counted as a page. Its only link is the in-page `#quiz` link. It mentions Volume III in plain text only, with no link.
- All five questions have one keyed answer (c, a, b, c, a). The feedback for right and wrong answers is accurate. The "pick first" prompt and the running and final score work. Each question asks about a cause or a choice: why Wukong refuses to fly the monk over, why he came back, why the monk said the words and what he apologized for, how the pig was tricked, and why the ogre is accepted. The claims match the pages: p15 shoe painting and "going back to my monk"; p23 apology wording; p33 Great Sage line; p34 the pig bursts through the roof; p40 "your road… first day"; p45 "worst thing… at my back".

## Hygiene
- No duplicate IDs, and no script reference to a missing ID (checked independently). No foreign-book terms. The only "Monte" hits are the `monte_inspired` storage-key prefix. No 49-page labels. The progress bar's 50 states match `totalStates`.

## Nonblocking notes
- In every quiz question the correct option is the longest one, which a reader could notice. This is cosmetic and not reader harm.

APPROVED
