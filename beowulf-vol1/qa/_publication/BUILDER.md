# Beowulf: The Hall, the Mere, and the Dragon — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 57-page reader for `books/beowulf-vol1/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/beowulf-vol1/HANDOFF.md` (the Phase line and the last few rows).
2. `books/king-arthur-vol1/index.html` — the proven reader from the last
   book (itself built from Three Kingdoms', Three Musketeers', and Monte
   Cristo Vol II's): copy its behavior, structure, and visual template
   wholesale and adapt the identity below. Its routing, contents, bookmarks,
   zoom view, end state, and quiz are the model. Remove every King Arthur
   name, key, title, and quiz item.
3. `books/beowulf-vol1/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/beowulf-vol1/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/beowulf-vol1/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `Beowulf: The Hall, the Mere, and the Dragon`
  (a standalone book: no volume number anywhere);
- 57 canonical pages at `pages/page-01.png` … `pages/page-57.png` (six of them
  — pages 7, 14, 23, 36, 42, and 57 — are Chronicle pages: vellum history
  pages inside the story; they are ordinary pages in the reader, counted and
  routed like every other page) (relative to the book directory);
- storage keys `monte_inspired:beowulf-vol1:page` and
  `monte_inspired:beowulf-vol1:bookmarks`;
- no library link and no other-volume link: remove those anchors. This book
  is complete in itself: the end state promises no sequel and names no
  other volume;
- the end state heading (the eyebrow, and the page-title text shown while
  the end state is displayed): `The End`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 57
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-58") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-59") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 57 titles as a simple `const titles = [` array of JSON
strings, in order:

1. Something in the Fen
2. Heorot
3. Out of the Fen
4. Thirty Men
5. Twelve Winters
6. Who's Coming with Me?
7. Who Were the Danes and the Geats?
8. White Cliffs
9. The Stone Road
10. I'll Fight Him with These
11. Seven Nights in the Water
12. Nine Sea-Monsters
13. What a Geat Can Do
14. What Was a Hall Like?
15. The Queen's Cup
16. Nothing in His Hands
17. Out of the Moor
18. Looking for Me?
19. He Left His Arm Behind
20. The Claw over the Doors
21. Like a Son
22. A Song about Beowulf
23. Who Was the King's Poet?
24. Grendel Had a Mother
25. She Came Anyway
26. The Black Lake
27. Hrunting
28. She Was Waiting
29. The Sword Would Not Bite
30. A Sword Made by Giants
31. Like Ice in Spring
32. Did You Think I Wasn't Coming Back?
33. A Good Sword
34. They Come for Everyone
35. Home
36. Why Did a Sword Have a Name?
37. The Old King
38. One Golden Cup
39. It Came Out Burning
40. No Army
41. Every Time
42. Why Does a Dragon Sleep on Gold?
43. Sickness, or the Sword
44. This Isn't Your Fight
45. Come Out, Dragon!
46. The Fire Came Again
47. We Promised Him!
48. I Came Anyway
49. Under the Fire
50. Today I Did
51. A Banner of Gold
52. The Sea Wind in His Hair
53. You've Lost Your Names
54. Who Will Keep Us Safe Now?
55. The Gentlest of Kings
56. Beowulf's Barrow
57. How Do We Still Know This Story?

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Hall That Sang`, 1–7
- `II · The Stranger Who Boasted`, 8–14
- `III · Grendel`, 15–23
- `IV · The Mother in the Mere`, 24–32
- `V · The Old King's Warning`, 33–36
- `VI · Fifty Winters`, 37–42
- `VII · The Dragon`, 43–57

Use straight apostrophes (`'`) in titles and movements exactly as written
above.

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences a ten-year-old and a seven-year-old can follow. Four test
the story's causes and choices, never trivia; one tests the book's Chronicle
pages (the history and culture around the poem — context that enriches the
story, never a debunking of it). On these five ideas:

1. Why Beowulf crosses the sea to fight Grendel (years before, King Hrothgar
   saved Beowulf's father: he paid a debt for him that nobody else would pay
   and gave him a home; now it is Beowulf's turn to help Hrothgar).
2. Why Beowulf gives Hrunting back and calls it a good sword, even though it
   failed under the lake (Unferth, who had mocked him, was generous enough
   to lend his own sword; Beowulf thanks him in front of the whole hall, and
   the rivals become friends).
3. Why old Beowulf tells Wiglaf and the ten men to stay on the hill and
   fights the dragon alone (for fifty years they had sung that he never
   needed anyone, and he was too proud to start now; it is the pride old
   Hrothgar warned him about, and the warning he only remembers on the
   headland).
4. Why Wiglaf runs into the fire when the ten men run away (they had all
   promised to stand by their king if he ever needed them, his father said
   their family always stands by Beowulf, and Beowulf told him he was afraid
   every time; Wiglaf is afraid too, and comes anyway — and together they
   kill the dragon).
5. From the Chronicle pages: how do we still know Beowulf's story after more
   than a thousand years? (every word comes from one single book, copied by
   two scribes in England about a thousand years ago; it was nearly burned
   in a library fire in 1731, and you can still see its scorched pages in
   the British Library in London).

The end state should close the whole story in a few plain sentences (the
boy everyone laughed at, Grendel, the mother in the mere, the old king's
warning, the dragon, Wiglaf, Beowulf's Barrow) and then link to the quiz. It
promises no sequel.

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.
