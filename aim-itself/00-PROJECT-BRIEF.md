# 00 — PROJECT BRIEF · "The Gun That Aims Itself"

## What this is
An illustrated **engineering explainer** (tech-explainer format, third in the series after Sky Duel and
Scattergun) on **autonomous / semi-autonomous counter-drone turrets** — how a machine detects, identifies,
tracks, and shoots down a drone on its own. 14 pages + cover + dark-flipper reader + 5-question WHY-quiz.

## Why
Summer 2026 opener (see `../summer-2026.md`). The kids are into military weapons and recently saw video of
autonomous anti-drone machine guns in Ukraine — this answers exactly that. Folds the modern drone war into
the same "how it actually works" format Sebastian already loved.

## Audience standard
Honor the CRITICAL FRAMING RULE: write so any first-time reader can follow — no age-pitching. Clear, not dumbed down.

## Scope decisions (locked with user 2026-06-22)
- **Engineering only.** No ethics / "should a machine decide to kill" thread this volume. (That question is
  deferred to the planned AI / Jensen Huang piece.)
- **New gritty military-tech register**, deliberately distinct from Sky Duel's glossy aerospace look (see 01).
- **Safety framing:** the target is always a *drone (a machine)*, never a person. No casualties depicted.
- Frame device: P1 night intercept re-read on P13.

## Spine
Problem (cheap drones) → why humans can't keep up → how it SEES (radar / cameras+thermal+acoustic / recognition)
→ how it SHOOTS (lead + the burst) → other counters (jam / net / laser / interceptor / gun) → it's not new
(Phalanx 1980, border sentry guns) → the full kill chain → where it's going (swarms vs. layered defense).

## Production plan (per gemini_thin.md + tech-explainer retros)
1. Refs: turret, FPV drone, Shahed-style drone, operator (Lena) + 1 PIL composite plate. → `refs/`
2. Prototype 3 pages spanning format/density: **P4 (POSTER radar)**, **P1 (cinematic hook, composite)**,
   **P12 (POSTER kill-chain, text-dense)**. Validate before bulk.
3. Bulk-generate the remaining ~10 pages + cover in two parallel waves.
4. Reader (dark flipper, phosphor-green `#5fb86a` accent, optional KILL-CHAIN footer strip) + quiz + landing card.
5. User QA → audit regens → commit `aim-itself/` + `index.html` only when asked.

## Cost envelope
~15 images + 4–5 refs on gpt-image-2 standard 1536×1024 ≈ **$3.5–4.0** (Sky Duel $4.0, Scattergun $3.6).

## Tooling note
This session is scoped to the nano project, so `mcp__openai-image-2__*` should be available. If a future
session runs from outside nano scope, fall back to `sky-duel/tools/genimg.mjs` (same key/billing).
