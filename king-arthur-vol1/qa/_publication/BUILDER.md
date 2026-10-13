# King Arthur, Volume I — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 59-page reader for `books/king-arthur-vol1/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/king-arthur-vol1/HANDOFF.md` (the Phase line and the last few rows).
2. `books/three-kingdoms-vol1/index.html` — the proven reader from the last
   volume (itself built from Three Musketeers' and Monte Cristo Vol II's): copy its behavior,
   structure, and visual template wholesale and adapt the identity below. Its
   routing, contents, bookmarks, zoom view, end state, and quiz are the model.
   Remove every Three Kingdoms name, key, title, and quiz item.
3. `books/king-arthur-vol1/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/king-arthur-vol1/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/king-arthur-vol1/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `King Arthur, Volume I: The Sword and the Table`;
- 59 canonical pages at `pages/page-01.png` … `pages/page-59.png` (six of them are Chronicle pages — vellum history pages inside the story; they are ordinary pages in the reader, counted and routed like every other page)
  (relative to the book directory);
- storage keys `monte_inspired:king-arthur-vol1:page` and
  `monte_inspired:king-arthur-vol1:bookmarks`;
- no library link and no other-volume link: remove those anchors (the end
  state may promise that the story continues in a Volume II, as text
  only, no link);
- the end state heading: `End of Volume I`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 59
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-60") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-61") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 59 titles as a simple `const titles = [` array of JSON
strings, in order:

1. The Storm
2. My Arthur
3. Thirteen Years
4. A Rider from London
5. That Isn't an Answer
6. London
7. Who Built the Walls?
8. The Sword in the Stone
9. Where's My Sword?
10. The Locked Inn
11. Like a Stick out of Snow
12. Kay Knows That Sword
13. Swear on the Book
14. I'm Not Your Father
15. All I've Got Is a Sword
16. When Nobody's Listening
17. Don't Make a Song of It
18. Alone with the Sword
19. Did It Really Happen?
20. The King of the Hens
21. We Will Have Arthur
22. The Crowning
23. A Gift of Swords
24. Uther's Son
25. I'd Do It Again
26. All of Us, Together
27. Was There a Real Arthur?
28. The Night Before
29. Bedegraine
30. Alone, Too Far
31. You're Very Bad at This
32. Thirty Torches
33. It Doesn't Look Like Winning
34. What It Cost
35. The Songs
36. Shining Armour
37. Kings Send Knights
38. Alone at Midnight
39. The Knight at the Fountain
40. The Sword Breaks
41. Kings Don't Yield
42. Me
43. Nearly Died for a Song
44. The Arm in the Lake
45. Whatever You Ask
46. Excalibur
47. Sword or Scabbard
48. That's Cheating
49. Every Day
50. Two Magic Swords?
51. A Knife over a Chair
52. That's a Cartwheel
53. Nine Oak Trees
54. Names in Gold
55. Level with Nobody
56. I'll Swear First
57. The Empty Chair
58. Goodnight, Father
59. Who Made It Up?

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Hidden King`, 1–7
- `II · The Sword in the Stone`, 8–19
- `III · The Kings Who Laughed`, 20–27
- `IV · The First Battle`, 28–36
- `V · The Knight at the Fountain`, 37–43
- `VI · The Lady of the Lake`, 44–50
- `VII · The Round Table`, 51–59

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences a ten-year-old and a seven-year-old can follow. Four test
the story's causes and choices, never trivia; one tests the book's Chronicle
pages (what is legend and what is history). On these five ideas:

1. Why Arthur pulls the sword out of the stone (the inn was locked and Kay
   needed a sword for the tournament; he did not even think about the gold
   letters or becoming king).
2. What really won the battle at Bedegraine (Kay brought Arthur back to his
   own people, the townspeople's spear line held against Lot's charge, and
   only then did the sword blaze; Arthur charging alone nearly lost it).
3. Why Arthur refuses to fight Pellinore the second time, when he has a better
   sword (with the scabbard on he cannot bleed, so it would not be a fair
   fight; he has learned that pride nearly killed him).
4. Why Arthur makes the table round (so that no knight sits higher than any
   other, not even the king, and the knights stop fighting over seats).
5. From the Chronicle pages: did the sword in the stone really happen?
   (almost certainly not: the oldest Arthur stories have no stone; it first
   appears in a story from around 1200, about seven hundred years after a
   real Arthur could have lived).

The end state may say, as text only, that the story continues in Volume II
(the Lady of the Lake's gift, and the empty seat).

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.
