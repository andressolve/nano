# The Three Musketeers, Volume I — what this production taught

Written 2026-09-08 at ship, for whoever runs the next book. The full paper
trail is `HANDOFF.md` (every ruling, dated) and `RUN-LOG.md` (every verdict,
per-page costs, the health metric). This file is the short version, and it
says where each lesson now lives so nobody has to remember it.

## Numbers

| | |
|---|---|
| Pages | 49 (46 at greenlight; the script gate added three) |
| Script gate | 6 rounds, 20 findings, alive in every round |
| References | 33 locks from 87 candidates; 3 whole-cast gate rounds; 10 locks superseded |
| Pages | 120 candidates, 2.4 per page; 69 REVISE routes: 53 craft, 16 gate |
| Promotions by advisor ruling | 7 (a rejected candidate promoted over an invalid finding) |
| Pages regenerated after a batch gate | 8 (12, 13, 15 twice, 28, 35, 41, 43) |
| Gates | 5 batches, 3 of them rerun; whole-book APPROVED with no findings; reader critic 2 rounds |
| Cost | the ChatGPT subscription for every image; one Claude session; about a day and a half |

## The lessons, and where they now live

1. **Attach only the focal sheets.** Two, at most three inputs per page. With
   three or more character sheets attached the generator sometimes returns a
   collage of the sheets: figures in a row, no scene, no text. Describe every
   other named figure in words. After this ruling the road and London pages
   landed on their first candidate. *Lives in:* `templates/book/qa/_assembly/PACKET-SPEC.md`
   item 6, the frame's "never a montage" sentence, `method/07-FAILURE-MODES.md`.

2. **The in-app image tool takes five reference images.** A six-input page
   fails silently three times before a builder says why. *Lives in:*
   `templates/book/book.toml` (`max_refs_per_call = 5`), `verify.py` blocks a
   sixth, `07-FAILURE-MODES.md`.

3. **Write the critic's tolerances into the first card.** Codex critics block
   on a space after a dash, a missing comma, "dueling" for "duelling", four
   guards where the line says five, a tail that wanders on a line only one
   mouth could say. Sixteen of sixty-nine rejections were of that kind. *Lives
   in:* the packet spec's C1 clause, the cards template, `07-FAILURE-MODES.md`
   ("The literal critic").

4. **The first candidate is often the generator's own story.** On about half
   the pages the first candidate ignored the packet and invented its scene and
   dialogue, twice quoting the source novel. The targeted second candidate
   almost always landed. Treat one miss per page as the price, not a defect;
   act only when the second misses too. *Lives in:* `07-FAILURE-MODES.md`
   ("The invented page, seen again at scale").

5. **When a reset drifts, promote the clean earlier candidate.** A builder's
   full prompt reset can drift further from the packet than the first
   candidate did. Four pages were held at the ceiling with a clean v2 or v3
   sitting in the folder; each was promoted by advisor ruling. *Lives in:* the
   skill's page-loop paragraph, `07-FAILURE-MODES.md`.

6. **Stacked full-width panels rescue dense pages.** Nine-balloon pages (10,
   12, 25, 46, 47) landed once restaged as four stacked panels with
   single-speaker beats and the busiest line alone in its own panel. *Lives
   in:* the packet spec's staging guidance (single-speaker beats, first
   speaker left); the advisors' resets in `HANDOFF.md` are the worked examples.

7. **Spectacle pages: stage the figure small and from behind from the start.**
   The generator prefers the hero portrait and rewrites long captions. Page 6
   cost four candidates learning this. *Lives in:* `HANDOFF.md` row for page 6.

8. **Counted props only where the story invites the count.** The casket on
   page 41 was drawn with fourteen studs while Constance counts to twelve; the
   fix was to stage the casket so it reads as a cluster under her hands, not a
   grid. Elsewhere (guards in a melee, stones in a fist) counts are nonblocking.
   *Lives in:* the packet spec's counted-object clause.

9. **Fresh gates catch what the first pass missed.** Athos wearing Rochefort's
   scar on pages 12–13 passed two page critics and the first continuity gate;
   a second continuity critic caught it. "that" for "what" on page 35 passed
   the page critic; the cold read caught it. Non-transitive gates with fresh
   critics are what found these; a batch rerun is worth its cost.

10. **Register drift lives in bare rooms and gold ballrooms.** Two setting
    plates and page 43 came out photographic. Pin the register in the prompt
    for interiors with little to draw. *Lives in:* `HANDOFF.md` rows for the
    study, Athos's room, and page 43.

11. **Tool notes.** The gate brief hardcoded Volume I's collision pairs
    (`refbrief.py` now reads the ledger); the silhouette board was a grayscale
    crop (`boards.py` now thresholds to a flat shape); the driver misread a
    verdict on a heading line (`pagerun.py`'s parser is wider); a hand
    promotion skips the driver's batch gates (run `--gates END` yourself); a
    hiccup-only watchdog (`pagerun-watch.sh` in the session scratchpad)
    relaunches the driver after a missing candidate and never after a hold.

12. **Packet edits go to the assembled sources.** The driver's advisors edit
    `qa/_assembly/prompts.md` and `cards.md` in place; a generator that rewrites
    whole movements will overwrite their restages. The generator under
    `qa/_assembly/generator/` is an archive of how the packets were first
    written, not a live source.

13. **A typo is an edit, not a residual.** The whole-book critic's
    nonblocking list was shipped as "a reader may notice" and the owner had
    to ask why a one-word typo was not simply edited. Now `EDIT` mode exists
    (`04-PAGE-LOOP.md` §4), the nonblocking list is worked before the reader
    is built, and the answer to "can't this be fixed?" is the fix. *Lives in:*
    `01-PIPELINE.md` Phase 6, `04-PAGE-LOOP.md` §4, `07-FAILURE-MODES.md`
    (two entries), the skill's Phase 6, `pagerun.py --edit`.

## What a reader may still notice

Recorded by the whole-book critic as below the redraw threshold:

- page 31: the boy holds a cream, red-sealed letter (the father's) where the
  Queen's blue-sealed one is sewn into his coat;
- page 36: an eighteenth-century footman in a 1625 scene;
- page 45: Rochefort's sling not visible for one panel.

Page 40's "Muskeeer" was fixed after ship by the driver's new edit mode
(`pagerun.py --page 40 --edit "…"`): the approved page goes to the generator
as the source image with one correction, the result is a normal candidate
(v3) through the blind critic, and it superseded the promotion on the first
try. Any of the above is the same one-liner; a lettering typo no longer costs
a regeneration.
