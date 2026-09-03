# Monkey King, Volume I — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 48-page reader for `books/monkey-king-vol1/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/monkey-king-vol1/HANDOFF.md` (the Phase line and the last few rows).
2. `/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/index.html` — the
   proven reader: copy its behavior, structure, and visual template wholesale
   and adapt the identity below. Its routing, contents, bookmarks, zoom view,
   end state, and quiz are the model.
3. `books/monkey-king-vol1/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/monkey-king-vol1/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/monkey-king-vol1/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `Monkey King, Volume I: Havoc in Heaven`;
- 48 canonical story pages at `pages/page-01.png` … `pages/page-48.png`
  (relative to the book directory);
- storage keys `monte_inspired:monkey-king-vol1:page` and
  `monte_inspired:monkey-king-vol1:bookmarks`;
- no library link and no other-volume link: remove those anchors (the end
  state may promise that the journey west continues in a Volume II, as text
  only, no link);
- the end state heading: `End of Volume I`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 48
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-49") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-50") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 48 titles as a simple `const titles = [` array of JSON
strings, in order:

1. The Stone Splits
2. Old Ma's Hand
3. The Dare
4. The Water Curtain Cave
5. Handsome Monkey King
6. Kings Die Too
7. The Raft
8. Out of a Rock
9. Years of the Broom
10. Three Taps
11. The Third Watch
12. The First Somersault
13. The Pine Tree
14. Home in One Leap
15. Down Through the Water
16. The Pillar Named
17. Smaller
18. Take It and Go
19. The Hall of Jade
20. Come Back
21. The South Gate
22. Keeper of the Heavenly Horses
23. The Stables
24. Below Rank
25. The Banner
26. The Army Comes Down
27. Give Him the Words
28. Because They Said It
29. A House of Gold
30. The Peach Garden
31. Am I Invited?
32. The Empty Hall
33. The Five Gourds
34. Send Erlang
35. Which One Do I Hit First?
36. Shape for Shape
37. The Temple and the Flagpole
38. The Ring from Behind
39. Equals Don't Kneel
40. The Furnace Sentence
41. Forty-Nine Days
42. The Lid
43. Send for the Buddha
44. The Wager
45. The Five Pillars
46. The Writing on the Finger
47. The Hand Comes Down
48. Someone Will Come

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Stone and the Waterfall`, 1–7
- `II · The Master`, 8–14
- `III · The Staff`, 15–19
- `IV · The Stable Boy`, 20–29
- `V · The Peaches`, 30–34
- `VI · Erlang`, 35–38
- `VII · The Furnace and the Hand`, 39–48

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences a ten-year-old and a seven-year-old can follow. Test the
story's causes and choices, never trivia, on these five ideas:

1. Why Wukong leaves the mountain after Old Ma has crowned him king (kings die;
   he wants to find an immortal and make him teach, so none of them has to
   die).
2. Why the Master throws him out (he used the shape to be admired, the one
   thing the Master warned him not to do).
3. Why Laozi tells the Emperor to give him a title instead of sending soldiers
   (words cost nothing; a monkey with a title holds still; soldiers cost more
   than titles).
4. What Wukong does inside the furnace that he has never done before, and why
   the furnace does not destroy him (he waits; the furnace gives back what a
   thing is made of, and he is made of a rock).
5. Why Old Ma climbs up with a peach every year at the end (he cannot come
   back, so she comes to him; she says the Buddha's words back: someone will
   come, wait).

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.
