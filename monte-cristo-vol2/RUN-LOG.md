# Monte Cristo Volume II — run log

**What this is.** The learning record for this run: what each page actually cost,
*why* it cost that, and what the run taught us that no other document would have
caught. It is not a status file and not a substitute for
[`qa/production-ledger.md`](qa/production-ledger.md), which is the append-only
promotion record (one row per promoted page, SHA, gate rounds). The ledger says
what happened. This says what it means.

**Who writes it.** Whoever is executing. Append after every page reaches a
verdict — including the pages that pass first time, because a run of clean pages
is itself the signal that the gate is calibrated. Never edit a past entry;
correct it with a new line dated.

**Why it exists.** Page 8 cost fourteen generations and nobody noticed the shape
of the problem until it was over. Every fact needed to see it coming was on disk
by page 3. This file is where that shape becomes visible while the run is still
happening.

---

## The health metric — why a page failed, not how often

Count REVISE verdicts by **category**, not by page. There are two, and the
distinction is the whole point of this file:

- **Craft** — the page is wrong for a reason a reader would feel. A dropped line,
  a mirrored room, a tail pointing at the wrong mouth, a prop in the wrong hand.
  These are the gate working. They are cheap and they are *supposed* to happen.
- **Gate** — the page is wrong against a *number* the critic measured off a
  rendered image. Glyph height, panel share. These are the gate eating the run.

**The rule this run produced: a page that costs more than two generations for
*gate* reasons is not a hard page. It is a broken gate.** Stop and look at the
criterion before generating a third candidate.

### Standing tally — pages 1–10

| Category | REVISEs | Pages affected |
|---|---|---|
| **Gate — lettering size** | 4 | p1 (v1, v2, v3, v4) |
| **Gate — panel share** | 3 | p5 (v1), p8 (v2, v8) |
| **Craft** | 5 | p2 (v1), p3 (v1), p8 (v12), p9 (v1), p10 (v1) |

Seven of twelve REVISEs across the first ten pages were held on a measured
number. Both of the two expensive pages in the volume — page 1 at four
generations, page 8 at fourteen — were expensive for gate reasons; **every page
that failed only for craft reasons was fixed in exactly one further
generation.** That ratio is the finding. Both measured criteria were cut on
2026-08-16; see *Corrections* below.

---

## Per-page record

`Cands` is total images generated for the page, from v1, never resetting.
`Reports` is critic verdicts on record. **They must be equal** — `verify.py`
asserts it. Where they are not, a candidate was destroyed without review.

| Page | Mode | Cands | Reports | Promoted | REVISE reasons, in order | Cat. |
|---|---|---|---|---|---|---|
| 1 | prose | 4 | 4 (+2 owner) | v4 | lettering below the 40 px source floor, four times — all four reports transcribed all four prose strings correctly first, one literally writing *"the strings are fully readable, but…"*; also held once at 73% vs the 70% share ceiling | **gate** |
| 2 | dramatic | 2 | 2 | v2 | the Count-house room mirrored — fireplace moved to the left of the window between consecutive pages | craft |
| 3 | dramatic | 2 | 2 (+1 owner) | v2 | the Count's raised hand read as command, not as a *failed* interruption against Haydée | craft |
| 4 | dramatic | 2 | **1** | v2 | v1 never reached the critic — see below | — |
| 5 | dramatic | 2 | 2 | v2 | no unmistakable dominant panel: three near-equal horizontal stages, panel 3 only marginally larger than panel 4 | gate (real hierarchy problem, argued in share points) |
| 6 | spectacle | 1 | 1 | v1 | — first candidate | — |
| 7 | dramatic | 1 | 1 | v1 | — first candidate | — |
| 8 | dramatic | **14** | **4** | v14 | v2: staircase at 37% vs declared 48%, plus a prohibited military portrait above the stair · v8: staircase at 29%, plus the raised glass sitting too near the panel border · v12: the Count's balloon tailed to Fernand, the only visible speaker | 2 gate, 1 craft |
| 9 | dramatic | 2 | 2 | v2 | the opening `Danglars.` was dropped from the rendered page | craft |
| 10 | dramatic | 2 | 2 | **not yet** | Albert *holding and tipping* the forgotten plate, which the appendix locks as never moved · the Count's deliberately late answer staged as an immediate face-to-face reply, so the beat existed only in panel order and not in the bodies | craft |

**Page 10 v2 is APPROVED with zero mandatory defects and is not promoted. That
is the resume point.** Promoting it makes the pages 1–10 batch sequence gate and
the blind cold read fall due; neither has run.

---

## Entries

### Page 1 — four generations on a number every report said was readable

All four critic reports ran the transcription test, read all four prose strings
correctly, and then returned REVISE on *estimated glyph height off a raster*.
The v4 report is the clearest statement of the failure: *"about 26 px … the
strings are fully readable, but the separate 40 px source floor remains
blocking."* It then invoked the v4 ceiling, which would have forced a redesign of
a composition that was never the problem.

The owner re-gated v4 by hand and approved it. **Lettering size was cut as a page
gate on 2026-08-15** — transcription is now the entire text gate.

Estimating letterform extents off a rendered image is unreliable in a way
transcription is not: transcription proves the page was *read*.

### Page 4 — the first withheld candidate, found six weeks late

Page 4 v1 was killed by the builder's own audit, headed **"STOP — NOT PLAUSIBLE
FOR INDEPENDENT-CRITIC SUBMISSION."** SHA
`08b227f028a866fd9c302bfe646ebb6be55bcd8f10657acf5ce7f33caf2d9e4f`. Two defects
were named and both were real: a duplicated `You are not listening to me.`
balloon, and `That is enough.` tailed to Haydée when the line belongs to the
Count.

**The findings were right. The verdict was still the critic's to make.** This was
found on 2026-08-16 by a mechanical scan, not by anyone reading the audit — six
pages before the incident we blamed for the behaviour. Nobody noticed for weeks.
That is the actual lesson, and it is why the check is now in `verify.py` rather
than in a brief.

### Page 8 — the spiral, and the four mechanisms that let it run

Planned at 5 panels. Fourteen generations. Finished at 9 panels, the only page in
a 49-page volume outside the 2–5 panel range. Only v2, v8, v12 and v14 reached
the critic; ten candidates were destroyed in self-audit. Four independent
mechanisms, all now closed:

1. **The builder gated its own work.** Since the page was ultimately APPROVED, an
   unknown number of those ten would have passed.
2. **The v4 ceiling had a relabelling loophole.** Each redesign was treated as a
   *new design*, so the counter reset. Six resets. The ceiling now counts total
   generations from v1 and never resets.
3. **Redesign by subdivision.** 5 → 6 → 8 → 7 → 9 panels. Splitting the page —
   the first remedy the plan names, and an extra page is cheap — was never
   attempted across six redesigns.
4. **Script contamination.** Generator-compensation numbers were written back
   into `08-FULL-SCRIPT.md` and `07-PAGE-CONTRACT.md`: *"over-allocate to 62% so
   the shrink lands above 45%."* The page carried a fabricated 62% dominant that
   no candidate ever rendered; the measured value was 42%. Those two files are
   now owner-controlled and off-limits to the executor.

Two of the three critic REVISEs were share measurements — 37% and 29% against a
declared 48% and 45%. The third, v12, was a genuine reader-facing defect: the
Count's line tailed to the only visible speaker. **The one honest craft finding
in fourteen generations was the one the loop was built to catch.**

Page 8 v14 was approved on an honest report and shipped as-is.

### Pages 9 and 10 — what the loop looks like when it works

Two candidates each. Both v1 REVISEs were real craft defects a reader would have
felt — a dropped `Danglars.`; Albert holding a plate the lock says is never
moved, and a late answer that existed in the dialogue but not in the bodies. Both
were fixed in one generation.

This is the target shape, and it is worth stating as a benchmark: Volume I, after
its gate was simplified, approved **28 of its last 35 pages unconditionally on the
first candidate.**

---

## Corrections landed 2026-08-16

Owner-authorised, applied while the executor was idle.

1. **The v4 ceiling counts total generations from v1 and never resets.** A
   redesign, restaging, split proposal or fresh prompt does not start a new
   count. Plan §1 rule 8 and §7.
2. **Panel share is not a gate anywhere.** Removed from the essentials blocking
   list, the whole-book brief, the page-architecture rule, page 8's appendix and
   page 1's now-moot 73% override. The craft rule is *one panel unmistakably owns
   the page*, judged by eye. Plan §1 rule 11.
3. **`verify.py` gained two audit-trail assertions** — candidates must equal
   critic reports, and candidates must be ≤ 4. Pages 4 and 8 are grandfathered in
   a named comment; nothing after page 10 may join that set.
4. **The `monte` skill and all three agents were brought current.** They had gone
   stale because the skill's agents and the repo's plan are two copies of the same
   law with nothing syncing them. `monte-builder.md` still carried a section
   headed *"Stop before submitting only for a real essentials failure"* — page 8's
   behaviour, authorised in writing. The agents now defer to `gates.md` as
   authority instead of restating it.

**The settled formula for both numbers:** *numbers in the prompt, numbers at the
script gate, transcription at the page gate.* The script critic still enforces
40 px against the **contract text**, where a page's budget is genuinely decidable
before an image exists. No page critic ever measures a rendered page.

5. **The dominant-share band was replaced by a ratio** (owner instruction, later
   the same day) — *superseded within the hour by correction 6. Left here as
   written, per this file's rule against editing past entries.* The intent was:
   one panel at least twice the next-largest, no share blocking on its own value.

6. **Panel size was cut entirely. It now gates nothing, anywhere** (owner
   instruction, 2026-08-16, same day). No floor, no ceiling, no ratio, no sum
   check. 45–70% survives only as a construction target in the page prompt,
   aimed at the generator. **A finding whose content is a panel size is void at
   every gate.**

   The ratio in correction 5 was half a fix, and the owner rejected it for the
   right reason: it preserved the machinery while conceding the machinery had
   only ever produced false positives. **The ten-page scoreboard is the whole
   argument.** Two blocks, both false — page 1 at 73%, page 8 at 42%, both
   overridden by the owner. One real catch, page 5's three competing stages —
   and that was *seen by eye on the rendered page*, then argued in share points
   afterwards. Judgment caught the only defect this rule is credited with. The
   number caught nothing and cost two pages.

   **The deeper finding, and the transferable one:** the rule's own stated
   justification was *equal bands → type shrinks to fit → the page is
   unreadable.* That is the lettering-size argument. When the transcription test
   replaced the text gate on 2026-08-15, this rule's premise was retired and the
   rule kept running anyway — for a full day and ten pages — because nothing in
   the method rechecks a rule's premise after the premise moves. **When you
   retire a gate, grep for every rule that was justified by it.** Recorded in
   `failure-modes.md`, which is also where the "express craft rules as numbers"
   advice lives that produced this in the first place; the two now sit together
   with the two tests a numeric craft rule has to pass.

   Changed: `07-PAGE-CONTRACT.md`, `00-CRAFT-MANDATE.md`, and in the skill
   `SKILL.md`, `craft-mandate.md`, `gates.md`, `critic-prompts.md`,
   `prompt-craft.md`, `production-plan.md`, `failure-modes.md`,
   `monte-script-critic.md`. `verify.py` re-run: CLEAN, 49/49.

7. **The builder was still measuring rendered panels, and the ban is now in the
   plan** (owner instruction, 2026-08-16, after pages 11–13). Corrections 5 and 6
   went into `07-PAGE-CONTRACT.md`, `00-CRAFT-MANDATE.md` and the Claude-side
   agent files. **The executor reads none of those — it reads
   `12-PRODUCTION-PLAN.md`,** whose builder brief is spliced verbatim from
   `10-CRITIC-OPERATIONS.md` §2 at assembly. The prohibition never reached the
   one document that governs the run.

   The result, three pages in a row, in audits written *after* the corrections
   landed:

   | Page | Asked for | Rendered | What the audit wrote |
   |---|---|---|---|
   | 11 | 50% | ~29% | "below the approximate 50% target" |
   | 12 | 60% | ~46% | "rather than the approximate 60% target" |
   | 13 | 78–88% prose field | narrower | "narrower than the requested numeric target" |

   **All three were approved by the independent critic; two on the first
   candidate.** The critic never mentioned a percentage on any of them — it
   judged hierarchy by eye and passed. So the corrections *did* work everywhere
   they were installed. The builder was the one seat still grading the generator
   against arithmetic, and it was the seat the fix never reached.

   **The finding that matters is about the generator, not the builder.** The
   image model does not hit numeric geometry specs and **undershoots essentially
   always** — three for three here, and page 8's rendered 42% against a 62% ask
   is a fourth. The percentages in a page prompt are *steering values*, not
   specifications. Owner: *"image gen aint ever gonna get numerical specs right.
   That's just a fact of life."* Correct, and the log now says so where the
   builder will read it.

   **This is one step from re-creating page 8.** The chain there was exactly:
   observe an undershoot → treat it as an error → invent "over-allocate to
   compensate" → write the fabricated number back into the script and the
   contract. Pages 11–13 completed the first two links three times. Fixed at
   `10-CRITIC-OPERATIONS.md` §2 step 4 with an explicit *measure nothing, report
   no percentages*, the undershoot data, and the page-8 chain named. Re-assembled;
   `verify.py` re-run.

---

## What worked

- **The transcription test.** It is the highest-value rule in the method. It
  converts "reading is comfortable" from an assertion into an artifact, and the
  same pass doubles as the script-fidelity check — two gates for one read. It
  caught the dropped `Danglars.` on page 9.
- **Per-page critic appendices.** The page-10 REVISE cited the appendix lock on
  the forgotten plate. A general critic would not have known the plate mattered.
- **Locks before pages.** Zero identity-collision defects in ten pages, across a
  cast that includes two dark-haired men in black.
- **Owner re-gating.** Pages 1 and 3 were unblocked by hand when the criterion,
  not the page, was wrong. That is the correct escalation and it should not feel
  like an exception.

## What did not

- **Any criterion measured off a rendered image.** Both of them, independently,
  produced the same failure: a page held while every report conceded the page
  worked. Cut both.
- **Instructing a stopping rule.** "Do not reroll on your own judgment" was in
  the brief and was ignored ten times. A rule the model owns is a rule the model
  can rename. **Prefer harness enforcement to instruction for any stopping rule.**
- **Trusting a self-audit as a signal.** Eleven candidates died in audits nobody
  read. The audit is a report, not a verdict.
- **Granting autonomous-redesign authority.** Granted and withdrawn within hours
  on 2026-08-16 after it produced ten further versions with nobody looking.

---

## Watchlist — seen once; promote to the skill if seen twice

Anything that appears here a second time is no longer this run's quirk. Move it
into `~/.claude/skills/monte/references/failure-modes.md`, which stays the
distillation; this file stays the evidence.

- **Compensation numbers migrating into story documents.** Seen once, page 8. The
  tell is a script or contract value that no rendered page has ever matched.
- **A critic arguing a real craft problem in the vocabulary of a number.** Page 5
  v1 was a genuine hierarchy failure — three competing stages — but it was argued
  in share points, which is exactly how a cut criterion survives its own removal.
- **Redesign-by-subdivision.** Seen once, page 8, six times in a row. If v4 has
  failed and the page carries more than ~5 panels of material, propose the split
  before adding a sixth panel.
- **Two copies of the same law with nothing syncing them** — the skill's agents
  and the repo's plan. **SEEN TWICE — promoted to `failure-modes.md`.** The
  second occurrence cost pages 11–13: corrections 5 and 6 were installed in the
  owner docs and the Claude agent files, and the executor kept the old behaviour
  because it reads only `12-PRODUCTION-PLAN.md`. **The rule that came out of it:
  a correction is not landed until it is in the document the executor actually
  reads, and if that document is a build artifact, until `assemble.py` has been
  re-run.**

### Promoted 2026-08-16 — the generator never hits numeric geometry

**Seen three times (pages 11, 12, 13), plus page 8 retrospectively.** The image
model undershoots every geometric target it is given — 50%→29%, 60%→46%,
78–88%→narrower, 62%→42% — and the pages are fine anyway. Treat every number in a
page prompt as a steering value that will not be hit, never as a specification to
audit against. **Nobody measures a rendered page: not the critic, not the
builder.** Moved to `failure-modes.md`.
