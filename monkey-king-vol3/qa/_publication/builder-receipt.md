# Builder receipt — Monkey King, Volume III: Sent Away reader

**Built:** `books/monkey-king-vol3/index.html`, a single-file reader for the 49 canonical pages (`pages/page-01.png` … `pages/page-49.png`), plus an end state (`#end`, also `#page-50`) and a quiz (`#quiz`, also `#page-51`). Neither is counted as a story page or mapped to an image.

**Adapted from the template** (`books/monkey-king-vol2/index.html`, copied wholesale):
- Title, sr-only heading, meta description, image alt text, topbar label (`Volume III · <movement>`), folio and zoom defaults now point to Volume III and page 1, "Still Walking West".
- The 49 titles and six movements are taken exactly as given in BUILDER.md.
- Storage keys are `monte_inspired:monkey-king-vol3:page` and `monte_inspired:monkey-king-vol3:bookmarks`.
- Routing boundaries moved to `#page-50` (end) and `#page-51` (quiz). The progress bar width is now 1/51.
- Contents eyebrow reads "49 pages". The end-state eyebrow and page title read "End of Volume III". The quiz heading reads "Test your understanding".
- New end-state text (three faces, the monkey sent away, the tiger who would not eat meat, the horse who spoke, the pig who told the truth, the monk who looks to Wukong first), with plain-text "continues in Volume IV" (no link).
- Five new quiz questions on the five specified ideas, with feedback drawn from the script's own facts and lines.

**Preserved unchanged:** responsive 2:3 stage; prev/next buttons, tap zones, keyboard, swipe; exact hash links and saved position; movement contents; device-local bookmarks; adjacent-page preloading; fullscreen; the zoom view (Fit/125/150/200/250/300%, pan, double-click, page navigation); race-safe loading (`renderRequest`, `displayedPage`, `pendingPageLoads`, `image.decode()`, `aria-busy`).

**Library/other-volume links:** the template had none, so there was nothing to remove.

**Could not preserve:** nothing.

`verify-reader.py`: CLEAN.
