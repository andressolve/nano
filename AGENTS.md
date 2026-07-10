# AGENTS.md — Project Notes for nano

## Graphic-Novel Execution Lessons

The completed `honda-soichiro/` project is the model for future biographical graphic-novel execution. The earlier `honda/` folder had useful research and planning, but execution failed when it drifted into one-off overlay demos, under-dense pages, skipped reference locking, and workaround thinking.

- **Image-generation billing rule:** For future image production, use the Codex in-app image generation path intended to run under the user's Codex/ChatGPT subscription entitlement. Do **not** use `OPENAI_API_KEY`, the bundled imagegen CLI, or any direct OpenAI API path for production images unless the user explicitly approves separate API billing in that conversation. If a workflow note says "from this Codex session," interpret that as subscription-backed Codex image generation, not API-key CLI generation.
- Preserve useful plans, then execute them directly: production folder, refs, prototype pages, full page run, reader, quiz, and landing card.
- Do not plan blank speech bubbles, blank caption boxes, or "caption bottles" with text added later in HTML/SVG. Dialogue and captions must be baked into the generated page image, or the page/script must be redesigned until in-image lettering is feasible.
- The reader displays finished pages and handles navigation/quiz only. It is not a lettering system for graphic novels.
- Do not make terse pages that force the reader to infer the missing story. For biography/expository comics, use enough native page text to answer what changed and why it matters. The Honda fix used T4-T5 density, roughly 90-150 words on hard pages, when the model/tool could handle it.
- Generate and approve character/object refs first. Do not skip directly from script to pages.
- Prototype the hardest page types before the full run: cinematic hook, technical explanation, and two-character partnership/business logic.
- If text rendering fails, diagnose model/tool, prompt shape, density, and composition. Do not fall back to blank bubbles or post-hoc SVG/HTML lettering.
- Treat speech attribution as scene blocking, not a lettering repair. Put speakers in dialogue order, keep bubbles on the speaker's side, and map every balloon by ordinal, speaker, verbatim text, position, and tail endpoint.
- For A-B-A dialogue in one panel, use two tiers: A upper-left, B upper-right, A lower-left. If the exchange remains risky, use one visible speaker and one bubble per panel.
- Explicit tail instructions reduce but do not eliminate errors. Inspect for tails that stop at torsos or empty space, orphan tail fragments, wrong balloon counts, and supposedly silent characters who receive dialogue.
- If attribution fails, revise the staging and regenerate the full page. Never crop-patch tails or swap text between existing balloons.
- Validate generated canvas dimensions. Panel-layout instructions can override a requested aspect ratio even when the prompt states it explicitly.
- Treat a successful external execution as evidence. When another tool or agent completes a project cleanly, study the artifact and adopt the working pattern instead of defending the earlier plan.
