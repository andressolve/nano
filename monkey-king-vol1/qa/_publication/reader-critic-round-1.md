# Reader critic — Monkey King, Volume I (local reader)

Inspected: `books/monkey-king-vol1/index.html` (full read, script traced by
hand), `pages/page-01.png … page-48.png` (48 files present, nothing beyond),
and `verify-reader.py` output (`CLEAN`, exit 0). No production material opened.

## Point-by-point

1. **Page 1 / mapping — OK.** `#page-1` → index 0 → title "The Stone Splits",
   counter "Page 1 of 48", movement label "Havoc in Heaven · The Stone and the
   Waterfall". `fileFor()` yields `pages/page-01.png`…`page-48.png`; it is only
   called on story indices, and `preload()` clips to 0–47. `titles` has 48
   unique entries.
2. **Navigation at both ends — OK for page states.** `prev` disabled at index 0;
   `next` disabled at the quiz (index 49). Arrow/PageUp/PageDown/Space, Home,
   End, tap zones, and swipe all route through the same guarded `render()`.
   `#page-0`, `#page-99`, `#foo` → null → saved position; `#page-49`/`#page-50`
   are silently aliased to `#end`/`#quiz` and rewritten. Saved position stores
   `min(current, 47)`, so a reload after the ending returns to page 48. Fresh
   visit (`getItem` → null → 0) opens page 1. See finding 3 for the failure
   branch.
3. **Contents / bookmarks — OK for page states.** Seven movements, ranges
   1–7, 8–14, 15–19, 20–29, 30–34, 35–38, 39–48: contiguous, 48 pages exactly
   once. Keys `monte_inspired:monkey-king-vol1:page` and `…:bookmarks`;
   bookmarks are filtered to 0–47 on load and persisted sorted. See finding 2.
4. **Zoom — OK for page states.** Opens at 150% horizontally centered, top of
   page; levels Fit/125/150/200/250/300; scroll, mouse drag, +/−/0 keys,
   double-click toggle; prev/next inside zoom re-render with loading guard;
   × and Escape close, focus returns via native dialog. See finding 1.
5. **Ending and quiz — OK.** Page 48 → `#end` (counter "End", main hidden,
   end card shown) → `#quiz`. Neither is labelled Page 49 in the counter,
   folio, or URL. The end card mentions Volume II in prose only; no link.
6. **Quiz — OK.** Five questions, each with one `data-answer`, one correct
   and one incorrect feedback block, inputs and button locked after checking.
   All five test causes or choices (why he leaves, why the Master expels him,
   why a title not soldiers, what changes in the furnace, why Old Ma climbs).
   Language is plain; Q4 is the longest and asks two things in one breath —
   nonblocking.
7. **Stale material — OK.** No Monte Cristo names, keys, or links. 44 IDs, all
   unique; every `getElementById` target exists. Only residue: the
   `#page-49`/`#page-50` hash aliases in `indexFromHash()` and an unused
   `params.delete("set")` — both invisible, nonblocking on their own.

## Findings

**1. (blocking) Zoom at the End or Quiz state opens a broken dialog labelled
"Page 49 of 48".** The topbar Zoom button, the `Z` key, and `tapZoom` remain
live when `current >= titles.length`. `openZoom()` → `updateZoomPage()` sets
`zoomTitle` to `undefined`, `zoomPageLabel` to "Page 49 of 48", then because
`displayedPage !== current` it shows "Loading Page 49…" permanently with the
image hidden. Pressing → inside that dialog moves to the quiz and unhides the
stale page-48 image under the "undefined / Page 49 of 48" header. Repro: read
to page 48, click →, press `Z`. Correction: in `openZoom()` return early when
`current >= titles.length`, and disable `zoomButton` (and `zoomBookmark`) in
the non-story branch of `render()`.

**2. (blocking) Bookmarking at the End or Quiz state creates a "49 undefined"
entry.** `toggleBookmark()` has no story-state guard. At `#end`, the topbar
Bookmark button or `B` adds index 48: toast reads "Bookmarked Page 49", the
Contents bookmarks section lists "49 undefined ★", and the entry vanishes on
reload because `loadBookmarks()` filters it. Repro: read to page 48, click →,
press `B`, open Contents. Correction: return early from `toggleBookmark()`
when `current >= titles.length` and disable `bookmarkButton` in that state.

**3. (blocking, one line) Storage failure sends a first-time reader to the
last page.** `savedIndex()` returns `titles.length - 1` (page 48, the finale)
both when `localStorage` access throws (site data blocked — Chrome "Block all
cookies", Firefox `dom.storage.enabled=false`) and when the stored value is
not an integer. A child opening the book for the first time on such a browser
lands on the ending. Correction: fall back to `0` in both branches (keep the
"out of range high → last page" case if that was intended, but never for the
catch or NaN case).

Nonblocking: `#quizScore` is never populated (empty element); `#page-49`/`#page-50`
aliases could be dropped so nothing in the file refers to a page 49; Q4 could
be split or shortened for the seven-year-old.

REVISE
