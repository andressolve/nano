# Builder receipt — Monkey King, Volume II reader

Built: `books/monkey-king-vol2/index.html`, the 48-page reader.

## Adapted from the template (`books/monte-cristo-vol3/index.html`)

Copied wholesale: CSS and visual template, layout, all markup structure, and
the full script (routing, contents, bookmarks, saved position, preloading,
race-safe loading with `renderRequest` / `displayedPage` / `pendingPageLoads` /
`image.decode()` / `aria-busy`, fullscreen, keyboard, touch swipes, page-edge
tap zones, zoom view with Fit/125/150/200/250/300%, drag pan, double-click zoom,
zoom-view page navigation, end state, and quiz scoring).

Changed:
- Identity: `<title>`, sr-only heading, meta description, top-bar label
  (`Monkey King` / `Volume II · The Road West`), stage aria-label, page and zoom
  alt texts, initial page title (`Five Hundred Years`), `Page 1 of 48`,
  `48 pages` in Contents.
- `const titles` (the 48 given titles) and `const movements` (the seven given
  ranges, 1–48 covered once).
- Storage keys `monte_inspired:monkey-king-vol2:page` / `:bookmarks`.
- Routing boundaries: `#page-49` → end, `#page-50` → quiz; progress bar base
  `calc(100% / 50)` (48 pages + end + quiz).
- Movement label prefix and end-state page title: `Volume II`, `End of Volume II`.
- End state rewritten (heading "Then He Waited"; mountain, robe, band, dragon
  who became a horse, the pig, the ogre and the nine-skull raft, the monkey
  waiting for the slowest; "continues in Volume III" as plain text, no link).
- Quiz rewritten: five causal questions from `08-FULL-SCRIPT.md` (the monk's
  own road at the river; the shoe painting; why "Gold, hold fast" and the
  apology; the bride trick at Gao Village; why the monk takes the ogre).
  Answers c, a, b, c, a.

The template already had no library or other-volume anchors (a spacer sits in
their place); none were added. No Monte Cristo names, keys, or quiz items
remain. No Chronicle pages. No images touched.

## Could not preserve

Nothing. `verify-reader.py` prints CLEAN; the script passes `node --check`.
