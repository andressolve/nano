# Monkey King, Volume III: Sent Away — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 49-page reader for `books/monkey-king-vol3/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/monkey-king-vol3/HANDOFF.md` (the Phase line and the last few rows).
2. `books/monkey-king-vol2/index.html` — the proven reader of the previous
   volume: copy its behavior, structure, and visual template wholesale and adapt
   the identity below. Its routing, contents, bookmarks, zoom view, end state,
   and quiz are the model. Replace every Volume II title, key, quiz item and
   reference. This book has no Chronicle pages.
3. `books/monkey-king-vol3/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/monkey-king-vol3/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/monkey-king-vol3/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `Monkey King, Volume III: Sent Away` (the third
  volume of a series; Volume I was *Havoc in Heaven*, Volume II *The Road West*);
- 49 canonical pages at `pages/page-01.png` … `pages/page-49.png` (relative to
  the book directory);
- storage keys `monte_inspired:monkey-king-vol3:page` and
  `monte_inspired:monkey-king-vol3:bookmarks`;
- no library link and no other-volume link: remove those anchors (the Nano
  publication copy adds its own library links later);
- the end state heading (the eyebrow, and the page-title text shown while the
  end state is displayed): `End of Volume III`; the quiz heading:
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

1. Still Walking West
2. One Bite
3. I Can Fly Peaches
4. Rice and Noodles
5. The Skull Under the Smile
6. Look in Her Basket
7. He Fooled Me Once
8. Like a Walnut
9. Same Skull
10. Did You See the Mist?
11. Gold, Hold Fast
12. Behind
13. I'm Asking You First
14. You'll Be Alive to Do It
15. Faster Than the Mist
16. Read It!
17. Not My Disciple
18. Four Bows
19. The Whole Way Home
20. The King Comes Home
21. Leave the Robe
22. Looking at the Weather
23. A Pagoda!
24. No Monks
25. May Not!
26. He's, Um, Busy
27. One Breath
28. I Sent Him Away
29. Claws and Teeth
30. Paws Together
31. Before He Was a Horse
32. The Cage
33. Listen to Me
34. Only When It Matters
35. The Worst Flyer in the Sky
36. I Don't Know Any Pigs
37. Try Again
38. The True One
39. On a Cloud Like Yours
40. He Waited for the Pig
41. The First Disciple
42. Krang
43. A Star That Ran Away
44. Going Home
45. Any Face
46. Not Even a Tiger
47. I Heard You
48. Wrong Together
49. Just a Lady with Lunch

Use exactly these six movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Ridge`, 1–5
- `II · Three Faces`, 6–19
- `III · Home`, 20–22
- `IV · The Yellow Robe`, 23–34
- `V · Going Back`, 35–40
- `VI · The Star in the Pagoda`, 41–49

Use straight apostrophes (`'`) in titles and movements exactly as written.

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences anyone can follow. All five test the story's causes and
choices, never trivia. On these five ideas:

1. Why the monk kept saying the words when Wukong was right (only Wukong's
   eyes, smoked in Heaven's furnace, could see the skull under the faces; the
   monk saw a girl, an old woman and an old man struck down, and Bajie told
   him Wukong was tricking him).
2. What Wukong did differently with the third face (he asked first; when the
   monk said no and the old man reached for the monk, he struck anyway to save
   him, knowing he would be sent away: "You'll be alive to do it").
3. Why the tiger would not eat the meat (the monk had never eaten meat or let
   anything die for his supper; the Yellow Robe bet that with claws he would
   turn into a beast, and he kept his rule anyway).
4. What Bajie had to do to bring Wukong back (go all the way to Flower-Fruit
   Mountain and tell the truth: he had lied about the bones because he wanted
   to be the monk's favourite; the horse told him to).
5. How Wukong beat the Yellow Robe, and why he let him go (he saw the runaway
   star under the demon's face and threatened to tell Heaven, so the star went
   home; Wukong let him go because he had a monk to get).

The end state should close the volume in a few plain sentences (three faces on
a white ridge, a monkey sent away for saving his master, a monk who would not
be a beast even as a tiger, a horse who spoke once, a pig who told the truth,
and a monk who now looks to Wukong first) and then link to the quiz. It may say
the road west continues in Volume IV, as plain text with no link.

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.
