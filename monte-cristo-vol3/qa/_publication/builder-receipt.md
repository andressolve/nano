# Reader builder receipt — Monte Cristo Volume III

**Built:** `books/monte-cristo-vol3/index.html`, the 56-page reader for
*The Count of Monte Cristo, Volume III: The King's Attorney*.
`verify-reader.py` prints CLEAN.

**Adapted from `books/beowulf-vol1/index.html`.** The structure, CSS, and
script came over unchanged and were edited only by targeted replacements:

- Title, sr-only heading, top-bar identity ("The Count of Monte Cristo" /
  "Volume III · …movement"), meta description, stage aria-label, and image
  alt text.
- 56 titles and 6 movements exactly as issued (covering 1–56 once).
- Storage keys `monte_inspired:monte-cristo-vol3:page` / `:bookmarks`.
- Routing boundaries: `#page-57` → end state, `#page-58` → quiz; the progress
  bar initial width is now 1/58 (56 pages + end + quiz). End and quiz never map
  to image files.
- Counters, contents eyebrow, and zoom labels say 56 pages; initial page is
  "The Second Man".
- End state: eyebrow "End of Volume III" (also the folio title while the end
  state shows), four short paragraphs (Auteuil house, red bottle, Valentine's
  false death, the trial, the bill, the word "Two", Valentine's hand closing),
  plain-text "The story continues in Volume IV." with no link, then the quiz link.
- Quiz "Test your understanding": five new questions on the five issued ideas,
  three options each, one `data-answer`, correct/incorrect feedback drawn from
  the script's own lines. Answers vary (b, a, c, b, a).
- Every Beowulf name, title, quiz item, and Chronicle reference removed. The
  template had no library or other-volume link (only an empty spacer), so
  nothing further was removed there.

**Preserved unchanged:** prev/next buttons, tap zones, keyboard and touch
navigation, exact `#page-N` links, saved position, contents with bookmarks and
quick return, adjacent preloading, fullscreen, zoom (Fit/125/150/200/250/300%,
pan, double-click, zoom-view page nav), race-safe loading (`renderRequest`,
`displayedPage`, `pendingPageLoads`, `image.decode()`, `aria-busy`).

**Not preserved:** nothing. No story page or reference image was touched.
Nothing committed.
