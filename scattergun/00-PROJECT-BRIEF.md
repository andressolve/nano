# 00 — PROJECT BRIEF

**Title:** Scattergun
**Subtitle:** How Shotguns Actually Work
**Format:** Illustrated technical explainer — second of the genre (sibling to `sky-duel/`)
**Target reader:** Francisco (10) and Sebastian (7) — both requested it after Sky Duel passed kid QA.
**Image model:** gpt-image-2 standard via `mcp__openai-image-2__{generate_image,edit_image}` (session runs inside nano scope — MCP available, no direct-API fallback needed), 1536×1024 (3:2 landscape), quality high.
**Page count target:** 14 content pages + cover. Target, not contract.

## The one-sentence window

Hitting a fast-flying target with a single bullet is nearly impossible — this book follows the four-hundred-year engineering answer: a machine that throws a precisely shaped cloud, and every clever idea (shell, choke, pump, self-loading action) stacked inside it.

## Narrative spine (the editorial bet)

**The problem IS the story.** Not a parts catalog — a single engineering problem and its accumulating answers:

flying target → throw a cloud (shot) → package the cloud (the shell) → control the cloud (choke) → repeat faster (pump) → let the gun do the work (Auto-5)

Human anchor in the middle act: John Moses Browning — a boy raised in his father's frontier gunsmith shop in Ogden, Utah, who built a working gun from scrap at about ten, patented his first design at 24, and went on to invent both the pump-action and the first self-loading shotgun. Same role McLean played in Sky Duel.

Frame device: open at a trap field the instant a clay disc shatters (P1) with the question unanswered; re-read the same instant near the end (P13), now fully readable; close with the four-century stack-of-answers montage (closing-as-invention, P14).

## Density plan

POSTER/cutaway hero pages T4–T5 (gpt-image-2 single-shot territory). Cinematic FIELD beats T3–T4. No page past T5.

## Caption clarity commitments

- Every technical term glossed inline on first use: shot, pellet, primer, wad, smoothbore, gauge, choke, recoil, semi-automatic, trap, skeet.
- No cryptic teasers; say the punchline plainly.
- Names grounded on first use ("a gunsmith's son named John Moses Browning", "the Auto-5 — the first shotgun that loaded itself").
- A real engineering book that happens to be readable by a 7-year-old. Clear, not dumbed down.

## Content guardrails

- Physics, engineering, sport, and history only. **Nothing living is shot anywhere in the book.** Targets depicted: clay discs, historical glass balls, paper pattern sheets. Hunting acknowledged in captions as history and use, never illustrated as a kill.
- No muzzle ever points at the viewer or at a person in any composition.
- No military/combat pages (the WWI trench-gun chapter of shotgun history is deliberately omitted).
- gpt-image-2 safety: sporting-range, workshop, and poster contexts only.

## Deliberate departures / notes

- Clay-pigeon inventor disputed (Kimble vs Ligowsky) → script says "around 1880, American inventors."
- Browning boyhood-gun age varies across sources (10 with brother Matt vs 13) → script says "about ten years old."
- "About 450 pellets" derives from Wikipedia's 410-per-ounce for #8 shot × a 1⅛ oz target load.
- "More than 300 times the pressure in a car tire" derives from ~10,500 psi ÷ ~32 psi.

## Facts discipline

Every date/number in `04-SCRIPT.md` traces to `research/RESEARCH-NOTES.md`. No model-memory facts.
