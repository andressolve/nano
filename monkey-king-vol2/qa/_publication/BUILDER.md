# Monkey King, Volume II: The Road West — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 48-page reader for `books/monkey-king-vol2/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/monkey-king-vol2/HANDOFF.md` (the Phase line and the last few rows).
2. `books/monte-cristo-vol3/index.html` — the proven reader from the last book:
   copy its behavior, structure, and visual template wholesale and adapt the
   identity below. Its routing, contents, bookmarks, zoom view, end state, and
   quiz are the model. Remove every Monte Cristo name, key, title, quiz item,
   and reference. This book has no Chronicle pages.
3. `books/monkey-king-vol2/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/monkey-king-vol2/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/monkey-king-vol2/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `Monkey King, Volume II: The Road West` (the second
  volume of a series; Volume I was *Havoc in Heaven*);
- 48 canonical pages at `pages/page-01.png` … `pages/page-48.png` (relative to
  the book directory);
- storage keys `monte_inspired:monkey-king-vol2:page` and
  `monte_inspired:monkey-king-vol2:bookmarks`;
- no library link and no other-volume link: remove those anchors (the Nano
  publication copy adds its own library links later);
- the end state heading (the eyebrow, and the page-title text shown while the
  end state is displayed): `End of Volume II`; the quiz heading:
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

1. Five Hundred Years
2. Get in Line
3. Kings Get Paid
4. He Kept Walking
5. A Monkey in the Mountain
6. Your Other Left
7. Out
8. Every Mile on the Ground
9. The Spare Robe
10. Is It Always This Slow?
11. First Fight
12. The Needle
13. No Better Than He Is
14. Tea with a Dragon
15. The Shoe
16. Gold, Hold Fast
17. Don't Make a Speech
18. Another Present
19. Promise Me
20. The Band
21. It Was a Trap
22. Yes
23. I'm Sorry
24. Gulp
25. It Ate Your Horse
26. Your Mother Was a Tadpole
27. Oh No
28. Saddle and All
29. The White Horse
30. Gao's Farm
31. The Bride
32. Darling, I'm Home
33. Not Anymore
34. Hello, Dumpling
35. The Pilgrim?
36. I Gave You a Robe
37. Eight Rules
38. Big Brother
39. No Feather Floats
40. Not One Mile
41. Clang
42. Soup
43. Pilgrim!
44. The Tenth One
45. At My Back
46. The Raft
47. Slower Than a Shoe
48. Then He Waited

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · Five Hundred Years`, 1–4
- `II · The Seal`, 5–10
- `III · The Robbers and the Shoe`, 11–17
- `IV · The Band`, 18–23
- `V · The Dragon in the Stream`, 24–29
- `VI · The Bride of Gao Village`, 30–37
- `VII · The River of Flowing Sand`, 38–48

Use straight apostrophes (`'`) in titles and movements exactly as written.

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences anyone can follow. All five test the story's causes and
choices, never trivia. On these five ideas:

1. Why Wukong will not fly the monk west on his cloud, even at the river
   (it is the monk's own road: if Wukong flies him over, the monk never
   crossed it — Guanyin's rule, and the monk's, which Wukong gives back to him).
2. Why Wukong came back after the quarrel with the robbers (the Dragon King
   showed him a painting of a boy who kept going back for an old man's dropped
   shoe; "if a boy can go back for a shoe, I can go back for a monk").
3. Why the monk said "Gold, hold fast" the first time, and what he was sorry
   for (he was frightened when the staff swung past his nose, not because
   Wukong had done anything; and he had called the cap a present when he knew
   it was a trap).
4. How Wukong caught the pig at Gao Village (he let the girl out and turned
   himself into the bride, told the pig her father had hired the Great Sage,
   then turned round with his own face).
5. Why the monk takes the river ogre even though he ate nine monks (the ogre
   told the worst thing about himself first, and nobody made him; the monk
   chooses to walk with him at his back and not be afraid).

The end state should close the volume in a few plain sentences (the mountain
opened, the robe, the band, the dragon who became a horse, the pig, the ogre
and the raft of nine, and a monkey who could cross the world in one leap,
waiting for the slowest of them) and then link to the quiz. It may say the
road west continues in Volume III, as plain text with no link.

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.
