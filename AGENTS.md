# AGENTS.md — Project Notes for nano

## Active library planning

Before proposing or beginning a retained epic-story candidate, read
`EPIC-LIBRARY-BRAINSTORM-2026-07-24.md` and the applicable project dossier, such
as `MONTE-CRISTO-DEVELOPMENT-NOTES.md` or `HEIKE-DEVELOPMENT-NOTES.md`.
Project-specific handoffs remain the authority for already existing works.

New long-form narrative and dialogue-driven graphic novels use the specialized
studio under `dialogue/`. Start from `dialogue/AGENTS.md`, create the work under
`dialogue/works/<project-slug>/`, and launch production sessions from that
project directory. Do not treat older root manuals as active authorities.

## Git publishing rule — use `main`

For this `nano` repository, the user's standing instruction is to publish
routine completed work directly to `main`.

- A request to "commit and push" means: verify the checkout is on `main`, stage
  only the files belonging to the requested task, commit them on `main`, and
  push `origin main`.
- Do not create, reuse, or push a feature branch, Codex branch, agent branch, or
  pull request unless the user explicitly asks for one in that conversation.
- If work was accidentally completed on another branch, first verify that
  `origin/main` is an ancestor and that a fast-forward is safe. Move the
  intended commits to `main` without force-pushing or rewriting history, then
  switch the local checkout to `main`.
- The worktree often contains unrelated user changes. Stage explicit task paths
  only; never use `git add -A`, stash, reset, clean, or otherwise alter
  unrelated files.
- After pushing, verify local `HEAD` equals `origin/main`. When the site is
  affected, wait for GitHub Pages deployment and verify the public index and
  target reader before reporting completion.

## Graphic-novel workflow routing

- Biographical graphic novels follow `bio.md` and the completed
  `honda-soichiro/` model. The dialogue studio does not supersede that workflow.
- Long-form narrative/dialogue graphic novels follow `dialogue/AGENTS.md`,
  `dialogue/PLAYBOOK.md`, and `dialogue/PROMPTING.md`.
- Production images use subscription-backed Codex in-app image generation. Do
  not use `OPENAI_API_KEY`, the bundled image-generation CLI, or another
  separately billed API path unless the owner explicitly approves it in the
  current conversation.
- Do not generate throwaway prototype story pages, prototype ranges, academic
  page exercises, or other noncanonical story-page proofs. Validate a risky
  form on the first real production page that requires it. Reuse an already
  approved script-faithful image when the owner directs.
- Dialogue, captions, letters, and sound cues are baked into the finished page
  image. The reader handles navigation, zoom, bookmarks, ending, and quiz; it is
  not a lettering system. Never solve a failed page with blank balloons,
  HTML/SVG overlays, crop patches, composites, or post-hoc relettering.
