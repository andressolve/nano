# Builder receipt — The Three Musketeers, Volume II: Milady reader

**Built:** `books/three-musketeers-vol2/index.html`, the 58-page reader.

**Adapted from** `books/three-musketeers-vol1/index.html`, copied wholesale (styles,
markup, script) and changed only in identity:

- title, meta description, top-bar heading, stage label, initial image alt and folio:
  `The Three Musketeers, Volume II: Milady`, page 1 "Only Three Blue Cloaks", "Page 1 of 58";
- progress segment width `100% / 58`; contents eyebrow `Volume II · 58 pages`;
- the 58 titles and seven movements exactly as issued (straight apostrophes);
- storage keys `monte_inspired:three-musketeers-vol2:page` / `:bookmarks`;
- routing boundaries `#page-59` → end, `#page-60` → quiz (logic otherwise untouched);
- end state: eyebrow and folio title `End of Volume II`, a closing paragraph in plain
  sentences, "The story continues in a later volume." as plain text, and a link to
  `#quiz` (new `.quiz-link` style, the template's gold pill);
- quiz `Test your understanding`: five cause-and-choice questions (Milady learns of the
  convent; Athos and the lily; the bastion breakfast; "Not like this" at the ferry; the
  commission), answers b, c, a, b, c, with balanced options; the correct option is the
  longest in two of five.

**Preserved unchanged:** prev/next buttons, edge tap zones, keyboard, swipes, `#page-N`
links, saved position, movement contents, bookmarks and quick return, preloading,
fullscreen, zoom view (fit–300%, pan, double-click, in-zoom navigation), race-safe
loading (`renderRequest`, `displayedPage`, `pendingPageLoads`, `image.decode()`,
`aria-busy`).

**Not preserved / removed:** nothing. The template already had no library or
other-volume links. No pages, references, or images touched.

`verify-reader.py`: CLEAN. Script passes `node --check`.
