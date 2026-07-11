# Handoff - Expanded Earthsea Part Two

## Status

**Complete, 2026-07-10.** `earthsea-wizard-part2/` is the continuation of *A Wizard of Earthsea*, not `earthsea-vol2/` (*The Tombs of Atuan*). It contains a cover, 30 finished pages, seven locked reference sheets, three hard-page prototypes, the expanded Chapters 3-4 script, a responsive reader, afterword, five-question why quiz, QA record, and reproducible prompt system.

Open the reader at `http://127.0.0.1:8765/earthsea-wizard-part2/` while the workspace server is running.

## Story boundary

- Begins aboard *Shadow* after Ged leaves Gont.
- Covers Thwil, entry to the Great House, Nemmerle, the Long Table, Vetch and Jasper, the Roke curriculum, the Isolate Tower, Hoeg, Ged's rivalry, Moon's Night, the loosing of the shadow, Nemmerle's death, Ged's recovery, Gensher's warning, Vetch's true-name gift, and the final Doorkeeper test.
- Ends with Ged carrying a yew staff aboard a modest vessel bound west for Low Torning.
- A future Part Three has not been scoped here.

## Production path

- Built-in subscription-backed Codex image generation only.
- No `OPENAI_API_KEY`, bundled image CLI, or direct API billing.
- Native multi-reference generation with locked Part Two identity sheets and an approved finished-page style reference.
- All captions and dialogue are baked into the raster pages.
- All failed images were replaced by full-page regeneration; no crop patches or lettering overlays.

## Shipped artifacts

- `00-PROJECT-BRIEF.md` - scope and editorial standard.
- `01-STYLE-GUIDE.md` - exact visual and lettering register.
- `02-CHARACTERS.md` - identity and canon locks.
- `03-SETTINGS.md` - Roke environment locks.
- `04-SCRIPT.md` - cover, 30 pages, panel text, and balloon attribution maps.
- `05-PRODUCTION-QA.md` - prototype, regeneration, attribution, dimension, reader, and catalog QA.
- `06-GENERATION-PROMPT-SET.md` - fixed prompt, attachment order, and page reference matrix.
- `refs/` - seven 1536x1024 production identity sheets.
- `research/prototypes/` - accepted threshold, teaching, and summoning prototypes.
- `pages/` - cover plus Pages 1-30, all 1536x1024.
- `index.html` - responsive reader, zoom, route strip, afterword, and quiz.

## Non-negotiables for continuation

1. Read this handoff, `05-PRODUCTION-QA.md`, the Part One speech-attribution study, the style guide, script, and finished pages before planning.
2. Preserve the same generous scene pacing. Do not compress travel, teaching, consequence, or recovery into terse summaries.
3. Generate and approve new identity/object refs before pages that depend on them.
4. Attach every relevant identity ref plus an approved finished-page visual reference to each page generation.
5. Treat speech attribution as scene blocking. Map ordinal, speaker, text, balloon position, character position, and tail endpoint before generation.
6. Inspect full resolution for exact text, balloon count, wrong speaker, silent-character violations, orphan fragments, identity drift, and 1536x1024 canvas size.
7. Regenerate the entire page when any of those checks fail. Never crop-patch or letter in HTML/SVG.
8. Use the built-in subscription-backed Codex image-generation path unless the user explicitly approves separate API billing in that conversation.

## Catalog integration

The shared root catalog in `../stories.js` carries Part Two as the newest published reading. Part One remains separate; *The Tombs of Atuan* is retained as a hidden draft until it is ready.
