# Reader publication verification — Monkey King, Volume I

- **Page integrity:** 48 canonical pages, `pages/page-01.png` … `page-48.png`, each 1024 × 1536 RGB, hashes in `qa/production-ledger.md`; all gates cleared (`qa/whole-book.md` APPROVED 2026-09-03).
- **Manifest coverage:** `const titles` 48 entries; `const movements` seven ranges covering 1–48 exactly once; verified by `qa/_publication/verify-reader.py` → CLEAN.
- **Reader features:** responsive 2:3 pages, prev/next, page-edge, keyboard, touch, `#page-N` routing, saved position, contents with bookmarks (`monte_inspired:monkey-king-vol1:*`), adjacent preloading, fullscreen, centered zoom view (fit/125/150/200/250/300, pan, page navigation), race-safe image loading; End (`#end`) and Quiz (`#quiz`) as non-page states; zoom and bookmark inert on those states; saved-position fallback to page 1.
- **Quiz coverage:** five questions on causes and choices (leaving the mountain; the expulsion; titles instead of soldiers; waiting in the furnace; Old Ma's peach), one correct answer each with feedback.
- **Critic verdict:** round 1 REVISE (zoom/bookmark live on End/Quiz; saved-position fallback) → fixed; round 2 REVISE (CSS `!important` overriding `hidden`) → fixed; round 3 **APPROVED** (`qa/_publication/reader-critic.md`).
- **Library copy:** this directory is a copy of `~/Documents/monte_inspired/books/monkey-king-vol1/` with the reader's "Return to the library" link added; raw candidates, proofs, and rejected renders excluded (`.gitignore`). Catalog card in `../stories.js`.
- **Browser check:** not performed by the orchestrating session (no browser); the critic traced routing and states from the source.
