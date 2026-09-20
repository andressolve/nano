# The Three Musketeers, Volume I — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 49-page reader for `books/three-musketeers-vol1/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/three-musketeers-vol1/HANDOFF.md` (the Phase line and the last few rows).
2. `/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/index.html` — the
   proven reader: copy its behavior, structure, and visual template wholesale
   and adapt the identity below. Its routing, contents, bookmarks, zoom view,
   end state, and quiz are the model.
3. `books/three-musketeers-vol1/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/three-musketeers-vol1/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/three-musketeers-vol1/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `The Three Musketeers, Volume I: The Queen's Diamonds`;
- 49 canonical story pages at `pages/page-01.png` … `pages/page-49.png`
  (relative to the book directory);
- storage keys `monte_inspired:three-musketeers-vol1:page` and
  `monte_inspired:three-musketeers-vol1:bookmarks`;
- no library link and no other-volume link: remove those anchors (the end
  state may promise that the story continues in a Volume II, as text
  only, no link);
- the end state heading: `End of Volume I`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 49
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-50") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-51") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 49 titles as a simple `const titles = [` array of JSON
strings, in order:

1. The Yellow Horse
2. Three Gifts at the Gate
3. The Man in the Window
4. The Stool and the Letter
5. Then So Do I
6. Paris
7. The Door and the Scar
8. A Shoulder in the Way
9. The Baldric
10. The Handkerchief
11. A Quarter to Twelve
12. Noon, and Five Red Cloaks
13. Four of Us
14. The Best Fight of His Life
15. The Third Time, You Stay
16. Four Abreast
17. Two Livres a Week
18. Weeks
19. Out of the Window
20. The Lantern in the Puddle
21. She Only Carries It
22. Only Two
23. She Gave Them Away
24. Are You Asking?
25. So That One Arrives
26. All for One
27. The Saint-Denis Gate
28. I Drink to the Queen
29. I'll Hold the Road
30. He Held the Road
31. I Have the Wine and I Have the Door
32. The Sea
33. Closed by Order of the Cardinal
34. Steel on a Plank
35. The Bearer
36. The Richest Man in England
37. Ten
38. Send for My Jeweler
39. Tell Her
40. The Road Home
41. The Kitchen Door
42. Ten Is Ten
43. The Queen Came In
44. Twelve
45. d'Artagnan
46. The Ring
47. Did You Arrive?
48. A Fair Trade
49. A Man in Red at a Window

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Yellow Horse`, 1–7
- `II · Three Duels at Noon`, 8–16
- `III · The Girl Downstairs`, 17–22
- `IV · All for One`, 23–27
- `V · The Road`, 28–35
- `VI · London`, 36–40
- `VII · Twelve`, 41–49

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences a ten-year-old and a seven-year-old can follow. Test the
story's causes and choices, never trivia, on these five ideas:

1. Why the boy picks a side at the Carmelite field when he could stand back (he
   is told he is not one of them; he has no cloak but has a sword and a heart,
   and standing with the outnumbered side is how he becomes one of them).
2. Why the Cardinal wants only two diamonds and not all twelve (a man would
   miss twelve, nobody counts to two; the Queen must be caught short at the
   ball, not robbed).
3. Why the three friends ride to London without asking what the letter says
   (if nobody knows, nobody can be made to tell; and it takes four so that one
   arrives).
4. Why the Duke has two new diamonds made instead of sending the ten (the
   Cardinal's trap is to produce the two she is missing in front of the court;
   with twelve on her shoulder the trap has nothing to catch).
5. What the Cardinal learns at the end that the boy did not mean to give him
   (his name, read off the father's letter stolen at Meung; the boy has won,
   and the most powerful man in France now knows who he is).

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.
