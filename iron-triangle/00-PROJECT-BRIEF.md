# 00 — PROJECT BRIEF · "The Iron Triangle"

## What this is
An illustrated **engineering explainer** (tech-explainer format, **fourth** in the series after Sky Duel,
Scattergun, and "The Gun That Aims Itself") on **how a main battle tank actually works** — gun, armor,
mobility, fire control, crew — all organized around the central design tension. 14 pages + cover +
dark-flipper reader + 5-question WHY-quiz.

## Why
Summer 2026, **mil-tech #2** (see `../summer-2026.md`). Kid-QA on the counter-drone turret book passed
("kids LOVED it") and tanks were greenlit with no STOP gate. Tanks are the obvious next machine, and the
book closes the loop with the turret book: cheap drones now hunt these 60-ton machines (P14).

## Audience standard
Honor the CRITICAL FRAMING RULE: write so any first-time reader can follow — no age-pitching. Clear, not dumbed down.

## The organizing idea (the spine)
**The iron triangle.** A tank must do three impossible things at once — **hit hard (firepower)**,
**survive being hit (protection)**, and **move fast (mobility)** — and you can never max all three. Every
tank is a compromise among the three corners. The whole book hangs the gun / armor / engine chapters off
this triangle, then shows the arms race that keeps redrawing it.

## Scope decisions
- **Engineering only**, same as the turret book. No ethics thread.
- **Reuse the gritty military-tech register** validated on "The Gun That Aims Itself" (see 01) — desaturated
  gunmetal/olive/concrete, single hot accent, painted documentary realism, dark schematic POSTER plates.
- **Safety framing:** machines as subjects, no human casualties depicted. Crew shown for scale only. The
  Somme history beat is framed as the machine crossing trenches and wire, never by what it killed.
- **Frame device:** P1 (a tank charging out of dust/smoke) re-read and annotated on P13.
- **Series tie-in:** P14 brings back the FPV-drone-vs-armor thread and the APS/counter-drone shield from
  the previous book — the two books snap together.

## Spine (14 pages)
P1 hook → P2 three impossible jobs → **P3 POSTER the triangle** → P4 the gun → **P5 POSTER dart vs jet** →
P6 fire control (hit while moving) → **P7 POSTER armor (sloped/composite/spaced)** → P8 the arms race
(ERA → active protection) → P9 mobility (engine + tracks) → P10 the crew → P11 not new (Somme 1916) →
**P12 POSTER the whole machine cutaway** → P13 re-read the opening → P14 where it's going (drones vs tanks).

## Production plan (per gemini_thin.md + tech-explainer retros)
1. Refs: hero MBT ("Bastion"), human commander (scale anchor, "Marko"), WWI Mark I (history) + 1 PIL
   composite plate (tank + commander). → `refs/`
2. Prototype 3 pages spanning format/density: **P3 (POSTER triangle)**, **P1 (cinematic hook, composite)**,
   **P12 (POSTER cutaway, text-dense)**. Validate before bulk.
3. Bulk-generate the remaining ~11 pages + cover in two parallel waves.
4. Reader (dark flipper, **amber accent `#d98a3d`**, IRON-TRIANGLE footer strip) + quiz + landing card.
5. User QA → audit regens → commit `iron-triangle/` + `index.html` only when asked.

## Cost envelope
~15 images + 3–4 refs + 1 composite on gpt-image-2 standard 1536×1024 ≈ **$3.5–4.0** (turret was $4.40,
inflated by P7 safety retries; this book has no comparable safety hotspot, so target the low end).

## Tooling note
Session scoped to nano, so `mcp__openai-image-2__*` should be available. Composite plate built locally with PIL.
