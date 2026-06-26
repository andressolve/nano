# HANDOFF — The Pea Square (resume here)

**Status (2026-06-25):** Full first pass BUILT, NOT committed. Open task = a **clarity pass** (user said "I think we can make it clearer"). Specifics of what reads unclear are TBD — ask the user at the top of the new session.

## What exists
- 5 planning docs (`00`–`04`) — source of truth for spine, style, exact LETTERING per page.
- 5 object refs in `refs/`: `ref_tiles` (T t Y y R r), `ref_plant` (tall/short), `ref_seeds` (round/wrinkled × yellow/green), `ref_blossom` (violet/white), `ref_grid` (blank 2×2). All clean, validated.
- Cover + P1–P14 in `pages/` (15 images). `page-11-v1.png` is the superseded P11 (kept as sibling; reader uses `page-11.png`).
- `index.html` reader — cloned from `../mendel/index.html`, violet `#9176c4`, **footer concept-strip** (factor→2×2→3:1→1:2:1→4×4→9:3:3:1, highlights current page's stage), **5-question WHY-quiz** (answers a/b/c/a/b).
- Landing card + footer entry already added to repo-root `index.html`.

## How pages were generated (reuse this)
- **2×2 grid pages (P5, P6, P7, cover):** `edit_image` anchored on `refs/ref_grid.png` — preserves the hand-ruled pencil grid, then fill cells + edge tiles + callouts. Worked single-shot.
- **4×4 P11:** fresh `generate_image`, seeds-in-cells (NOT letters) to dodge the 16-cell letter-failure mode. Hero `9:3:3:1` + edge cards `RY Ry rY ry` correct.
- **Object pages (P10):** `edit_image` on the relevant ref (`ref_seeds`).
- **Cameo pages (P1, P14):** fresh generate, Mendel locked clean-shaven, NO beard/moustache (model loves to add facial hair), gold oval spectacles, black habit; P14 adds silver pectoral cross. Both passed.
- Tool quirks: `thinking=true` is REJECTED by this MCP build (both edit + generate) — don't pass it. `edit_image` takes exactly ONE `imagePath`. Occasional 500 server error → just retry.
- All images 1536×1024, gpt-image-2 standard, q=high. Run cost so far ≈ $5.

## Known nits already fixed
- P2 first came out with `A a` tiles + "twòs" typo → regenerated with `T t`, fixed.
- P11 margin legend "green Y" → targeted edit to lowercase `y` (current `page-11.png`).

## Clarity-pass candidates to eyeball (unconfirmed — user to direct)
Look hardest at the text-dense / multi-element pages where a first-time reader could stall:
- **P7 (1:2:1)** — the phenotype-vs-genotype distinction is the subtlest idea in the book.
- **P9 (test cross)** — two side-by-side outcome grids; check the "half short → Tt" panel reads clearly.
- **P11 (9:3:3:1)** — 4×4 is busiest; confirm the four colour-groups + counts read at a glance.
- **P8 (coins)** / **P10 (two traits)** — check label density.
Per style guide: ≤3 text zones + diagram per page; if a page needs more, SPLIT or simplify rather than shrink text.

## Ship steps remaining
1. Clarity pass (regenerate/edit only the pages the user flags; keep versioned siblings).
2. User QA → audit regens.
3. Commit `pea-square/` + repo-root `index.html` diff ONLY when the user asks. Leave other untracked work alone.
4. Write retrospective `project_pea_square_retrospective.md` + flip this book from active to RECENT SHIP in MEMORY.md.
