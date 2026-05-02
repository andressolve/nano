# Newton Vol 1 — Session Handoff

**Last updated:** 2026-05-02
**Status:** ✅ Vol 1 shipped. All 24 pages generated on `gpt-image-2` standard, reader + landing card built, two commits pushed to `origin/main`.

---

## Where we are

1. ✅ All 12 planning markdown docs written (00–11)
2. ✅ All 10 reference sheets unified on `gpt-image-2` standard mode
3. ✅ Cover + 23 story pages generated on `gpt-image-2` standard (no thinking)
4. ✅ `index.html` reader built (dark theme, page-flipper, 5-question quiz). Page labels are `Page N of 23` (cover is "Cover", not page 1)
5. ✅ Landing-page card added to `../index.html`
6. ✅ Production log captured in `08-PRODUCTION-LOG.md` (Runs 1–6)
7. ⏸ **NEXT:** No Vol 2 planned yet. If pursued, Newton's later life (Mint, Royal Society, Optics, Leibniz feud) would be the natural arc.

## Key decision recorded

A hybrid pipeline (NB2 for narrative pages + `gpt-image-2` for geometry-critical pages) was tested and rejected because the two models produce visibly different aesthetics on shared-page scenes. The whole book runs on a single `gpt-image-2` standard pipeline. See `08-PRODUCTION-LOG.md` Run 5.

## Image model in use

**OpenAI `gpt-image-2`** (standard mode, no thinking) via the custom MCP at `~/.claude/mcp-servers/openai-image-2/`.

- Project-scoped in `~/.claude.json` at `projects["/Users/andresrodriguez/Documents/nano"].mcpServers["openai-image-2"]`
- `thinking` is **opt-in only** — never pass `thinking: true` without a documented reason. Not needed for any of the 24 Newton pages including the geometry-heavy ones (10, 11, 14, 15, 23)
- ~$0.21/page at 1024×1536 high. Total Newton Vol 1 image cost ≈ $7.35 (refs + smoke + 24 pages)
- See `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/reference_openai_image_2_mcp.md` for full setup details and the API-key-rotation reminder

## Reference sheets (in `refs/`)

All on `gpt-image-2`. Old gpt-image-1.5 versions retained as `-gpt15.png` siblings, and the older child v1 as `ref-newton-child-v1.png`.

| File | Subject |
|------|---------|
| `ref-newton-child.png` | ~6–7, pages 2–4 |
| `ref-newton-schoolboy.png` | ~14–15, pages 5–6 |
| `ref-newton-young-scholar.png` | ~22–25, pages 7–18 + cover |
| `ref-newton-mature-professor.png` | ~40+, pages 19–24 |
| `ref-halley.png` | Edmond Halley, page 20 |
| `ref-hannah.png` | Hannah Ayscough Newton, pages 3, 6 |
| `ref-grandmother-margery.png` | Margery Ayscough, page 3 |
| `ref-prism-apparatus.png` | Object plate (prism setup) |
| `ref-reflecting-telescope.png` | Object plate (reflector) |

**Face lock for Newton (all ages):** narrow long face + slightly downturned mouth + heavy-lidded watchful eyes + auburn-to-brown hair (lengthens with age, no wig). Repeat in every page prompt that drifts.

## Reader notes

- Pattern matches `../einstein/index.html` and `../descartes/index.html`.
- 5-question quiz at end: fragile birth, plague years of invention, second-prism proof, moon-as-perpetual-fall, Halley prompting the *Principia*.
- Cover is page index 0 with label `Cover`. Story pages are 1–23. Quiz is the final entry. The "Next →" button reads "Quiz →" on the penultimate page.
- Preload guard checks `pages[current + 1].file` is non-null before prefetching, so the quiz entry doesn't trigger a bad fetch.

## Cost discipline reminder

The custom MCP exists specifically to keep `gpt-image-2` from defaulting to thinking mode (which is what Codex did and burned cost). **Do not pass `thinking: true` casually.** A standard 1024×1536 high call is ~$0.21. Thinking mode can climb to $0.50–$1+ per call.

If a future page demonstrably needs thinking mode, document the reason in `08-PRODUCTION-LOG.md` before opting in.

## Untracked on disk (intentional)

These are not committed and don't need to be:

- `../output/imagegen/newton-vol1/` — generation drafts (`-v1.png` siblings of finals)
- `../output/imagegen/smoke/` — `page-15-mcp-standard-test.png` from Run 4
- `../tmp/` — scratch
- `../pythagoras-vol2/` — planning only, no refs/pages yet

## Files to read when starting a new session

Priority order:
1. This file (`HANDOFF.md`)
2. `08-PRODUCTION-LOG.md` (full run-by-run history including model decision)
3. `../CLAUDE.md` (project conventions, current workflow calibration)
4. `02-CHARACTERS.md` and `01-STYLE-GUIDE.md` if continuing or making Vol 2

The user's memory system at `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md` is loaded automatically.
