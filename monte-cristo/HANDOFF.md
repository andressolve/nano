# The Count of Monte Cristo — Project Handoff

> **Source of truth across restarts.** Read this document and
> [`CREATIVE-MANDATE.md`](CREATIVE-MANDATE.md) before resuming.

## Status

**Volume I is complete and locally QA-passed.**

Completed:

- public-domain English/French source archive and 117-chapter map;
- locked story mandate: dialogue-driven dramatic adaptation, not a historical
  or narrative treatise;
- selected Velvet Cinema graphic direction;
- locked **3:2 landscape, 1536 × 1024** production format;
- five-volume working dramatic architecture;
- complete 32-page Volume I script;
- 19 accepted Volume I reference plates;
- three accepted hard dialogue prototypes;
- cover and all 32 finished story pages;
- landscape reader and end interstitial;
- five-question quiz;
- root-library landing card;
- desktop and 390 × 844 mobile-browser QA;
- production log and generation rules.

Not yet done:

- publication to the live library.

## Read First

1. [`../EPIC-LIBRARY-BRAINSTORM-2026-07-24.md`](../EPIC-LIBRARY-BRAINSTORM-2026-07-24.md)
2. [`../MONTE-CRISTO-DEVELOPMENT-NOTES.md`](../MONTE-CRISTO-DEVELOPMENT-NOTES.md)
3. [`CREATIVE-MANDATE.md`](CREATIVE-MANDATE.md)
4. [`00-PROJECT-BRIEF.md`](00-PROJECT-BRIEF.md)
5. [`01-STYLE-GUIDE.md`](01-STYLE-GUIDE.md)
6. [`04-SERIES-ARCHITECTURE.md`](04-SERIES-ARCHITECTURE.md)
7. [`06-VOLUME-1-SCRIPT.md`](06-VOLUME-1-SCRIPT.md)
8. [`07-PRODUCTION-LOG.md`](07-PRODUCTION-LOG.md)

For exact story words and page turns, the Volume I script is authoritative.

## Non-Negotiable Mandate

This is a story. Dialogue, desire, opposition, discovery, reversals, decisions,
consequences, intimacy, wonder, and spectacle carry the adaptation.

- Do not turn the book into a historical survey, illustrated synopsis, lesson,
  or explanatory treatise.
- History and technical facts enter only through live dramatic need.
- Captions connect; they do not lecture.
- First-time readers must understand what changed and why without filling gaps.
- The Count should first fascinate, then frighten.
- Mercy must arrive as action and consequence, not a final moral caption.

## Landscape Lock

Every story page, cover, prototype, and reference canvas is **1536 × 1024,
3:2 landscape**.

- Never generate or approve a portrait or square story page.
- Never rotate or crop a page into compliance.
- Validate the actual file dimensions after every generation.
- Internal panels may be tall or narrow, but the page canvas remains landscape.
- The reader must display the finished landscape pages without re-lettering
  them.

## Current Story Shape

The working adaptation uses five volumes. Volume I, *Edmond*, moves through:

> homecoming → promise → trap → erasure → friendship → new mind → death and
> rebirth → apparent omnipotence → first act of grace

Its final turn is the restored *Pharaon*, not the treasure. Edmond's new power
first gives life before he begins to weaponize it.

## Finished Reader

Open [`index.html`](index.html). It contains:

- cover plus 32 finished landscape pages;
- navigation by buttons, keyboard, click zones, swipe, and hash deep links;
- page titles, count, progress, fullscreen, and an end interstitial;
- a five-question comprehension quiz with immediate feedback.

The story canvas never changes shape: every cover and page asset is exactly
**1536 × 1024**. A portrait phone viewport letterboxes the landscape art rather
than cropping, rotating, or reflowing it.

## Accepted Visual Proof

The strongest quick proof of the chosen direction is:

- [`style-exploration/03-velvet-cinema.png`](style-exploration/03-velvet-cinema.png)
- [`pages/prototype-01-examination.png`](pages/prototype-01-examination.png)
- [`pages/prototype-02-faria-conspiracy.png`](pages/prototype-02-faria-conspiracy.png)
- [`pages/prototype-03-mercedes-recognizes-edmond.png`](pages/prototype-03-mercedes-recognizes-edmond.png)

The full accepted reference inventory and repair history are recorded in
[`07-PRODUCTION-LOG.md`](07-PRODUCTION-LOG.md).

## Resume Here

If publishing is requested:

1. Re-run dimension, syntax, and browser smoke checks.
2. Review the explicit Monte Cristo and catalog diff.
3. Work directly on `main`; stage only the Monte Cristo-related paths,
   `MONTE-CRISTO-DEVELOPMENT-NOTES.md`, and `stories.js`.
4. Push `origin main`, verify local `HEAD` equals `origin/main`, wait for GitHub
   Pages, and test both the public library card and reader.

If revising Volume I, regenerate the full affected page. Do not patch balloons,
tails, faces, or words onto existing art, and do not add reader-based story
lettering.

Use the built-in subscription-backed Codex image generation path. Do not use an
API key, bundled image-generation CLI, or separately billed direct API path
unless the user explicitly approves it in a future conversation.

## Repository Note

The worktree contains unrelated user changes. Volume I is complete locally but
has not been committed, pushed, or deployed as part of this production pass.
