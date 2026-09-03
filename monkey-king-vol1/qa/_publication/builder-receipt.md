# Reader builder receipt — Monkey King, Volume I

**Date:** 2026-09-03
**Built:** `books/monkey-king-vol1/index.html` (56.6 KB, single file, no dependencies)
**Template:** `/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/index.html`, copied wholesale and adapted by exact-match substitution (every substitution asserted to hit once). No story page, proof, or reference image was opened, edited, or regenerated. No image generation.

## What was preserved unchanged from the template

Responsive 2:3 stage; previous/next buttons; page-edge tap zones (prev 30% / zoom 40% / next 30%); keyboard navigation (arrows, PageUp/Down, Space, Home, End, Z, C, F, B; +/−/0/B inside zoom); touch swipes; `#page-N` links with `history.replaceState`; saved reading position; movement-based Contents with `aria-current` and scroll-into-view; device-local bookmarks with quick return from Contents; adjacent-page preloading; fullscreen toggle; centered zoom view with Fit / 125 / 150 / 200 / 250 / 300 %, scroll and mouse-drag pan, double-click zoom, and prev/next inside zoom; the race-safe loading path (`renderRequest`, `displayedPage`, `pendingPageLoads`, `image.decode()`, `aria-busy`); status toast; reduced-motion rule; the quiz check logic.

## What was adapted

- `<title>`, meta description, top-bar heading, image `alt` strings: `Monkey King, Volume I: Havoc in Heaven`; movement label reads `Havoc in Heaven · <movement>`.
- 48 titles as `const titles = [...]` (JSON strings) and seven movements as `const movements = [...]`, exactly as the packet lists them; pages map to `pages/page-01.png` … `pages/page-48.png` via the template's `fileFor()`.
- Storage keys `monte_inspired:monkey-king-vol1:page` and `monte_inspired:monkey-king-vol1:bookmarks`.
- Routing boundaries updated for 48 pages: `#page-49` → end state, `#page-50` → quiz; the seven verifier lines are present verbatim. End and quiz are never story pages and never map to an image.
- Progress bar initial width `calc(100% / 50)` (50 states = 48 pages + end + quiz), matching the script's `totalStates`.
- Contents eyebrow `Volume I · 48 pages`; folio and zoom labels `Page 1 of 48`; initial title `The Stone Splits`.
- Library link (`../index.html`) removed; replaced by an empty `home-spacer` span so the top-bar grid keeps the title centered. The `.home` CSS was replaced by `.home-spacer`; the mobile `.home-label` rule dropped.
- End state: eyebrow `Five hundred years`, heading `End of Volume I`, text only (the journey west continues in a Volume II; no anchor to any unpublished page); the other-volume link removed.
- Quiz: five new `class="question"` items, one `data-answer` each, testing the five causes/choices named in the packet (leaving the mountain; the pine tree; title over soldiers; waiting in the furnace / made of a rock; Old Ma's peach and the Buddha's words). Feedback written from the script's own facts (pp 6, 11, 13, 19, 27, 40–42, 45–46, 48) in plain sentences.

## Verification

`node --check` on the extracted script: clean. The verifier prints `CLEAN` when run against the real book directory (index.html + pages/).

## Could not preserve / needs attention

- **The publication packet is in the wrong directory.** `BUILDER.md`, `CRITIC.md`, and `verify-reader.py` live at `books/monkey-king-vol1/books/monkey-king-vol1/qa/_publication/` (a nested stray `books/monkey-king-vol1/` inside the book), not at `books/monkey-king-vol1/qa/_publication/`. The verifier resolves the book root from its own location, so at the nested path it finds no pages and no index.html and reports 26 problems; at the packet's intended path it does not exist. I did not move it (the packet forbids touching qa/ beyond this receipt). To run the exact command the packet and CRITIC.md name, move the three files: `mv books/monkey-king-vol1/books/monkey-king-vol1/qa/_publication/* books/monkey-king-vol1/qa/_publication/` and remove the stray nested `books/` folder. I confirmed `CLEAN` by running a copy of the verifier from a scratchpad directory that symlinks the real `pages/` and `index.html`.
- Nothing else from the template was dropped.

Not committed.

## Correction round (2026-09-03, after reader-critic REVISE)

- Finding 1 (zoom on End/Quiz): `openZoom()` now returns early when `current >= titles.length`, which covers the topbar button, the `Z` key, and the tap zone; `render()` sets `zoomButton.disabled = true` in the non-story branch and `false` in the story branch; `.tool:disabled` styled inert (hover rule scoped to `:not(:disabled)`).
- Finding 2 (bookmark on End/Quiz): `toggleBookmark()` returns early when `current >= titles.length` (covers the topbar button, the `B` key, and the zoom-dialog bookmark); `bookmarkButton` disabled/enabled alongside `zoomButton` in `render()`.
- Finding 3 (storage fallback): `savedIndex()` now returns `0` (page 1) both when `localStorage` throws and when the stored value is missing, non-integer, or out of range; it never falls back to page 48.
- Nothing else changed. Verifier at the real path `books/monkey-king-vol1/qa/_publication/verify-reader.py`: CLEAN; `node --check` on the script: clean. Not committed.
