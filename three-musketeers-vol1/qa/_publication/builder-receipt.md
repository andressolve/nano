# Reader builder receipt — The Three Musketeers, Volume I

Date: 2026-09-08. Built by a fresh implementation builder from
`qa/_publication/BUILDER.md`.

## Built

`books/three-musketeers-vol1/index.html` (single file, ~55 KB, no external
assets beyond `pages/page-01.png` … `pages/page-49.png`).

Derived from `/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/index.html`
by exact-string substitution (each substitution asserted to match once), so the
template's CSS, markup skeleton, and script are carried over unchanged except
for the identity edits below. `node --check` passes on the script;
`verify-reader.py` prints CLEAN.

## Preserved from the template, unchanged

- Responsive 2:3 stage; previous/next buttons; page-edge tap zones (30/40/30);
  keyboard navigation (arrows, PageUp/Down, Space, Home, End, Z, C, F, B;
  +/−/0 and B while zoomed); touch swipes.
- `#page-N` deep links, `hashchange` routing, saved reading position in
  `localStorage`, `history.replaceState` URL sync.
- Contents dialog built from the movement array, every page listed exactly
  once, current page highlighted and scrolled into view; device-local
  bookmarks section at the top of Contents with quick return.
- Adjacent-page preloading; fullscreen toggle.
- Centered zoom view: Fit, 125%, 150%, 200%, 250%, 300%; scroll/pan with
  mouse drag; double-click toggles Fit/200%; prev/next while zoomed;
  bookmark from the zoom toolbar.
- Race-safe loading: `renderRequest`, `displayedPage`, `pendingPageLoads`,
  `image.decode()`, `aria-busy`, loading label, failure status toast.
- End state and quiz as two extra non-page states (`#end`, `#quiz`), never
  mapped to image files; saved position clamps to the last story page.
- Quiz mechanics (radio options, Check answer, correct/incorrect feedback,
  inputs disabled after checking).

## Adapted

- `<title>`, meta description, header strong/span, stage aria-label, image
  alt text (initial and runtime), zoom title: `The Three Musketeers, Volume I:
  The Queen's Diamonds` / `The Queen's Diamonds · <movement>`.
- `const titles` — the 49 titles from the brief, in order, as JSON strings.
- `const movements` — the seven approved ranges (1–7, 8–16, 17–22, 23–27,
  28–35, 36–40, 41–49).
- Storage keys `monte_inspired:three-musketeers-vol1:page` and
  `monte_inspired:three-musketeers-vol1:bookmarks`.
- Routing literals kept for 49 pages (`#page-50` → end, `#page-51` → quiz).
- Contents eyebrow: `Volume I · 49 pages`.
- End state: eyebrow `End of Volume I`, heading `All for one, and one for
  all`, a three-sentence closing paragraph, and the text-only line `The
  story continues in Volume II.` No links.
- Quiz heading `Test your understanding`; five new questions on the five
  ideas in the brief (Carmelite field, only two diamonds, not asking what
  the letter says, the jeweler, the name off the Meung letter), each with
  three options, one `data-answer`, and plain-language correct/incorrect
  feedback drawn from the script's own lines (pp. 13, 22, 25, 38, 45–46).

## Removed

- The `← Stories` library anchor (`../index.html`) in the top bar, replaced
  by an empty `.home-spacer` so the three-column top-bar grid keeps the book
  title centered. Its `.home` / `.home-label` CSS rules were dropped.
- The end-state links to the other volume and the library.

## Not preserved / notes

- Nothing else was lost. No story page, proof, reference image, prompt, or QA
  report was opened or touched. Not committed.

## Correction round 1 — 2026-09-08

Bounded correction of the five blocking findings in `reader-critic-round-1.md`.
Only `index.html` changed; titles, movements, storage keys, routing literals,
quiz content, and every story page are untouched. Verifier: `CLEAN`.

1. CSS `body.reader-state .reader-status-card { display: block !important; }`
   replaced with `body.reader-state .reader-status-card:not([hidden]) { display: block; }`
   so End and Quiz are mutually exclusive; `render()` calls `window.scrollTo(0, 0)`
   on entering the Quiz state.
2. `openZoom()` returns early when `current >= titles.length`; the Z key is
   guarded on the same condition; `render()` sets `zoomButton.disabled = !isStory`.
3. `toggleBookmark()` returns early when `current >= titles.length`; the B key
   is guarded the same way; `render()` sets `bookmarkButton.disabled = !isStory`.
4. `savedIndex()` now falls back to `0` (Page 1) both when the stored value is
   not an in-range integer and when storage throws.
5. Keydown `targetIsControl` narrowed to `input, select, textarea`, so arrow
   keys and shortcuts work after clicking a nav or tap button.

Nonblocking notes taken: Space advances only on story pages (so it scrolls the
quiz); the hidden loading elements in End/Quiz receive the story-only label
(`Loading Page 49…`) instead of Page 50/51.
