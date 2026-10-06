# Three Kingdoms, Volume I — reader critic (fresh, independent)

Inputs: `index.html` (read in full), the page images the reader references
(`pages/page-01.png` … `page-50.png`, with the 768×1152 proofs of 09, 10, 15, 27,
28, 34, 36, 43–48 opened to fact-check the quiz), and
`verify-reader.py`, which printed `CLEAN` and exited 0. No prompts, audits,
candidates, QA reports, prior critic reports, or builder receipt were opened.

## Routing trace

- `#page-1` → index 0. `#page-50` → index 49. `#end` (and the `#page-51` alias) → index 50,
  the end state. `#quiz` (and `#page-52`) → 51. An out-of-range hash (`#page-0`,
  `#page-99`, `#foo`) → `null` → saved position (or 0), and `updateUrl` rewrites the
  hash to the real state. `fileFor` is only reached for story indexes and `preload`
  is clamped to 0–49, so nothing past `page-50.png` is ever requested.
- Page 1: title "The Yellow Sky", counter "Page 1 of 50", label "The Peach Garden
  Oath · The Peach Garden". End state counter reads "End", quiz reads "Quiz"; neither
  is labelled Page 51. Saved position clamps to 49, so a hashless reload after the
  end lands on Page 50.
- Prev is disabled on Page 1, Next on the quiz. Arrow keys, PageUp/Down, Space (story
  pages only), Home/End, tap zones, and swipes all route through the same
  `goPrevious`/`goNext` guards. Radio inputs swallow arrow keys correctly.
- Contents: seven movements, 1–9, 10–16, 17–22, 23–30, 31–38, 39–46, 47–50, so all 50
  pages appear exactly once. Bookmarks are saved under
  `monte_inspired:three-kingdoms-vol1:bookmarks` and the position under `…:page`,
  filtered to 0–49 on load.
- Zoom opens at 150%, scrolled to the top and centred horizontally. Levels: Fit, 125,
  150, 200, 250, 300. Drag-pan, scroll and touch pan work, +/−/0 keys and the Prev/Next
  buttons work inside zoom (disabled at the ends), and it closes with × or Escape.
  It is disabled on the end and quiz states.
- Page 50 → end card → "Test your understanding" → quiz. The end card links only to
  `#quiz`; "Volume II" is plain text, not a link.
- No duplicate IDs. Every `getElementById` target exists. No Monte Cristo or
  Musketeers terms, and no 49-page labels. The only "monte" strings are the required
  `monte_inspired:` storage prefix.

## Quiz

- Correct letters: c, a, b, c, a. They vary.
- Length strategies: always-longest gets 2/5 (Q2, Q5), always-shortest gets 1/5 (Q4),
  always-middle gets 2/5, always-a gets 2/5, always-c gets 2/5. None of them passes.
- Each answer checked against the pages:
  - Q1 matches p.9–10: "You're the worst fighter" / "That's why they'll chase me."
  - Q2 matches p.15: "Kill him and we are the rebels" and the shaking hands.
  - Q3 matches p.27–28: "you'll tell the world."
  - Q4 matches p.34 and p.36: "before it is cold" / "still warm."
  - Q5 matches p.43–45 and p.48: two brothers fail; Liu Bei leaves the hill; Lü Bu
    "could not see all of his enemies at once"; Yuan Shao's guards claim.
- Each question has one defensible answer, and the correct and incorrect feedback
  both fit it. All five ask about causes or choices, not trivia.
- Every stem is clear for a seven-year-old. Two nonblocking notes:
  - "snub" (Q2) is the hardest word, but the stem explains it in the sentence before.
  - "grab his wrist" (Q2): the panel shows Liu Bei's hand clamped over Zhang Fei's
    hand on the spear. A child will still recognise the moment.

## Findings

1. **On phones and tablets (≤860 px wide), the fixed Prev/Next buttons cover the
   quiz score.**
   - Steps to reproduce: open `#quiz` at 390×844, check all five answers, and scroll
     to the bottom.
   - Cause: under the 860 px media query, `.nav` is fixed at
     `bottom: max(12px, env(safe-area-inset-bottom))` and is 46 px tall. So it covers
     the band 12–58 px from the bottom, or about 34–80 px on iPhones with a home
     indicator. At maximum scroll, `#quizScore` sits about 42–70 px from the bottom,
     because the card has only `padding-bottom: 42px`.
   - Effect: the two buttons sit over the centred line "Final score: N of 5 correct"
     (or the "…so far" line). On a plain phone they hide the lowercase letters across
     most of the line. On an iPhone they cover the whole line where they overlap.
   - Why it matters: the reader cannot scroll any further to reveal the score, and the
     score is the quiz's payoff.
   - Fix: in the `@media (max-width: 860px)` block, give the status cards room below
     the buttons, for example
     `.reader-status-card { padding-bottom: calc(80px + env(safe-area-inset-bottom)); }`.
     Keep the desktop padding as it is.

All other behaviour listed in CRITIC.md items 1–7 is correct.

REVISE
