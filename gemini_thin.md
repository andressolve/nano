# gemini_thin.md — Setup notes for the `gemini-pro-thin` MCP

A custom local MCP server that wraps the Gemini image-generation endpoint **without** the upstream `gemini-nanobanana-mcp` package's hard 2000-character prompt cap. Built 2026-05-02 during Honda Soichiro Vol 1 production after the cap kept silently trimming exactly the disambiguating clauses that prevented page bugs (driver presence, classmate ages, ethnicity locks, era-correct clothing, lettering placement, verbatim caption text).

This file documents how to set the MCP up on a fresh machine or recover after losing the registration. The MCP itself lives at `~/.claude/mcp-servers/gemini-pro-thin/`.

---

## Why it exists (what problem it solves)

The upstream `gemini-nanobanana-mcp` npm package enforces a **wrapper-side** prompt-length limit of 2000 characters. The underlying Gemini API has no such cap. Under that wrapper, biographical-mode prompts (Style Block + register block + character lock + panel description + verbatim lettering + restrictions block) routinely exceed 2000 chars — and the wrapper either errored out with a `too_big`-style rejection or quietly trimmed the prompt, dropping the load-bearing disambiguation at the end. Either way: a recurring failure mode that wasted budget on bad pages.

`gemini-pro-thin` is a drop-in replacement at the tool-name level. Same surface, no cap, and a couple of small ergonomic improvements (overwrites instead of `_1`/`_2` collision suffixes; longer 120s timeout for slow Pro responses on T5 pages).

---

## What's in the package

```
~/.claude/mcp-servers/gemini-pro-thin/
├── index.mjs           # ~330 lines, the actual MCP server
├── package.json        # depends on @modelcontextprotocol/sdk
├── node_modules/       # installed via `npm install` after the manifest is in place
└── HANDOFF.md          # build notes (not required at runtime)
```

Tool surface (mirrors nanobanana, called as `mcp__gemini-pro-thin__*`):

- `generate_image(prompt, saveToFilePath)`
- `edit_image(prompt, image{path|dataBase64, mimeType?}, saveToFilePath)`
- `compose_images(prompt, images[2..10], saveToFilePath)`
- `style_transfer` is intentionally **not** implemented — this collection never uses it.

---

## Setup from scratch

### 1. Create the MCP folder

```
mkdir -p ~/.claude/mcp-servers/gemini-pro-thin
cd ~/.claude/mcp-servers/gemini-pro-thin
```

### 2. Drop in `package.json`

```json
{
  "name": "gemini-pro-thin-mcp",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "description": "Thin local MCP for Gemini image-generation endpoints. No artificial prompt char limit.",
  "main": "index.mjs",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.17.4"
  }
}
```

### 3. Drop in `index.mjs`

The full server is ~330 lines. The canonical copy lives at `~/.claude/mcp-servers/gemini-pro-thin/index.mjs`. If recovering from a backup or another machine, copy that file as-is. Architectural shape:

- Reads `GEMINI_API_KEY` and `GEMINI_IMAGE_ENDPOINT` from env, exits if either is missing.
- Exposes 3 tools through `@modelcontextprotocol/sdk` over stdio.
- Each tool builds a Gemini `:generateContent` request (text part + optional inline-data image parts), POSTs to `${ENDPOINT}?key=...`, retries up to 3× on 429/5xx with exponential backoff, 120s per-request timeout.
- Saves the first inline image part to `saveToFilePath` (overwriting any existing file at that path), creating parent directories as needed.

Allowed input MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/gif`. Path traversal (`../`) is rejected.

### 4. Install dependencies

```
cd ~/.claude/mcp-servers/gemini-pro-thin
npm install
```

This pulls only `@modelcontextprotocol/sdk` and its transitive deps. Should be fast.

### 5. Register the server with Claude Code

Edit `~/.claude.json` and add a `gemini-pro-thin` block to the `mcpServers` map for the **project that needs it**. For nano specifically, the block lives under the nano project's settings (alongside `openai-image-2`):

```json
"gemini-pro-thin": {
  "type": "stdio",
  "command": "node",
  "args": [
    "/Users/andresrodriguez/.claude/mcp-servers/gemini-pro-thin/index.mjs"
  ],
  "env": {
    "GEMINI_API_KEY": "<your-google-ai-studio-key>",
    "GEMINI_IMAGE_ENDPOINT": "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent"
  }
}
```

Notes on the env vars:

- **`GEMINI_API_KEY`** — required. A Google AI Studio key. The MCP exits at startup with a clear error if missing.
- **`GEMINI_IMAGE_ENDPOINT`** — required. The full endpoint URL **including** the `:generateContent` suffix. The model identity is selected by this URL, not by the MCP code. To switch models without touching the server:
  - Pro: `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent`
  - Flash (NB2): `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent`

For nano, the endpoint is currently pinned to **Pro** because biographical-mode hero pages are calibrated to Pro's T5 ceiling. Switch to Flash for cheap T1–T3 pages by editing the env var and restarting Claude Code.

### 6. Restart Claude Code

After any change to `~/.claude.json`'s MCP block, **Claude Code must be restarted** before the new MCP loads. New tool names will appear as `mcp__gemini-pro-thin__generate_image`, `mcp__gemini-pro-thin__edit_image`, `mcp__gemini-pro-thin__compose_images`.

### 7. Smoke test

Call `generate_image` once with a deliberately long prompt (>2000 chars) and confirm:

1. Returns a saved PNG (no error response).
2. The saved file path matches `saveToFilePath` exactly — no `_1` / `_2` suffix.
3. The image visibly matches the prompt's subject.

Save the artifact under `output/imagegen/smoke/gemini-pro-thin-smoke-<date>.png` so future regressions have a baseline. The 2026-05-02 baseline lives there already.

A short smoke prompt template:

> A 2900-character oil-painting-realism prompt describing a single 3:2 landscape scene with full Style Block, character lock, panel description, lettering instructions, and restrictions block. The exact contents do not matter — what's being verified is that the wrapper does not reject or trim it.

---

## Behavior differences vs upstream `gemini-nanobanana-mcp`

| Aspect | nanobanana (upstream) | gemini-pro-thin |
|---|---|---|
| Prompt length cap | 2000 chars | none |
| File collision | appends `_1`, `_2`, ... | overwrites `saveToFilePath` directly |
| Transport | stdio | stdio |
| Retries | 3× exponential backoff on 429/5xx | same |
| Request timeout | shorter | 120s (Pro can be slow on T5) |
| Logging | verbose | minimal |
| `style_transfer` | provided | not implemented |

The overwrite behavior eliminates the recurring `mv page-07_1.png page-07.png` step that nanobanana forced after every regen. If you genuinely want collision-safe writes, choose a unique `saveToFilePath` yourself.

---

## Common failure modes and fixes

- **`MCP "gemini-pro-thin" failed to start`** after restart → check `~/.claude.json` for a typo in the absolute path under `args`. The path must be the literal `index.mjs` location; relative paths and `~` expansion are not honored here.
- **`GEMINI_API_KEY not set in env`** in the startup log → the MCP block in `~/.claude.json` is missing the `env` field, or the key is empty. Restart after fixing.
- **`Gemini API 400: ...`** at call time → endpoint URL is wrong (missing `:generateContent`, or pointing at a non-image model), or the key doesn't have access to image-gen models. Check both before debugging the prompt.
- **`Gemini API 429`** → quota / rate limit. The MCP retries 3× with backoff before surfacing. If it still fails after retries, slow down the call cadence or switch endpoint to Flash for cheaper traffic.
- **`request timed out after 120s`** → real Pro outage or unusually heavy T5 page; retry. The 120s ceiling is intentional, not a bug.
- **No image returned, just a JSON dump in the error** → the model refused (safety filter) or returned only text. Read the error's first 600 chars; usually the cause is obvious. Edit the prompt and retry.
- **MCP not visible in `ToolSearch` after restart** → confirm the MCP block sits under the **correct project's** entry in `~/.claude.json`. MCPs are project-scoped, not global. The nano block is the canonical one.

---

## Operational reminders

- The active model identity is set by the endpoint env var, not by the MCP. To switch Pro ↔ Flash, edit `GEMINI_IMAGE_ENDPOINT` and restart.
- Codex and Claude both consuming the same Gemini key on the same project can knock the MCP off mid-session (rate-limit interference). If the tool disappears, check whether another agent is also calling Gemini.
- The MCP's `saveToFilePath` is treated as authoritative — any stale file at that path is overwritten without prompting. Version important pages by giving them unique names rather than relying on the wrapper to preserve old ones.
- `compose_images` requires 2–10 refs. Use it when a page genuinely needs multiple distinct faces locked simultaneously. For single-ref work, `edit_image` is the right call.

---

## Memory cross-reference

- `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/reference_gemini_pro_thin_mcp.md` — the canonical memory note (more compact; this file is more procedural).
- `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md` — repo-level pointer to this MCP as the nano-project default.
- `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/reference_image_model.md` — model-ladder context (Pro vs Flash vs gpt-image-2).
- `bio.md` (this folder) — biographical-mode workflow that consumes this MCP.

---

*Last updated 2026-05-03. Update both this file and `reference_gemini_pro_thin_mcp.md` if the MCP shape, env vars, or default endpoint change.*
