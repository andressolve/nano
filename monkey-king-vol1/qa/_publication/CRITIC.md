# Monkey King, Volume I — reader critic

You are one fresh, zero-history reader critic. Review the finished local
implementation independently. Do not edit files.

## Inspect

- `books/monkey-king-vol1/index.html`
- canonical `books/monkey-king-vol1/pages/page-01.png` through `page-48.png`
  only as the reader references them
- the output of `python3 books/monkey-king-vol1/qa/_publication/verify-reader.py`

Do not open production prompts, audits, candidates, QA reports, or the builder
receipt before judging.

Read the HTML and script closely (you have no browser): trace the routing for
`#page-1`, `#page-48`, `#end`, `#quiz`, and an out-of-range hash; the contents
list generation; bookmark persistence; zoom-view behavior; the quiz check
logic. Judge:

1. Page 1 loads with the correct title, counter, and movement; every page
   index maps to `pages/page-NN.png` for 1–48 and nothing beyond.
2. Previous/next, page-edge, keyboard, touch, `#page-N` reload, and saved
   position behave coherently at both ends of the book.
3. Contents covers all seven movements and 48 pages exactly once; bookmarks
   persist under the book's own storage keys.
4. Zoom opens centered, supports the required levels, pan/scroll, page
   navigation, and clean close/return.
5. Page 48 leads to a non-page ending state and then a five-question quiz;
   neither is counted as Page 49; the ending links to nothing unpublished.
6. Every quiz question has one correct answer, correct feedback, and tests the
   story's causes or choices rather than trivia, in language a seven-year-old
   can follow.
7. No stale Monte Cristo terms, keys, links, or 49-page labels remain; no
   duplicate element IDs; no script references to missing IDs.

Cosmetic preference and redesign suggestions are nonblocking. A `REVISE`
finding must name reproducible reader harm or broken behavior and a concrete
correction.

Write `books/monkey-king-vol1/qa/_publication/reader-critic.md` with a concise
report ending in exactly `APPROVED` or `REVISE`, and return only that word.
