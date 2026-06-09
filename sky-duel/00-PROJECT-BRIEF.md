# 00 — PROJECT BRIEF

**Title:** Sky Duel
**Subtitle:** How Fighter Jet Weapons Actually Work
**Format:** Illustrated technical explainer — FIRST of its genre in the nano collection (not a biography, not fiction)
**Target reader:** Sebastian (7, reads upward, asked specifically about fighter jet weapons / likely heat-seeking missiles). Francisco (10) secondary.
**Image model:** gpt-image-2 standard, 1536×1024 (3:2 landscape), quality high. Called via direct API helper (`tools/genimg.mjs`) because the openai-image-2 MCP is not registered in this session — same key, same billing.
**Page count target:** 14 content pages + cover. Target, not contract — stop when the arc lands.

## The one-sentence window

A missile and a jet have been trying to out-think each other since 1947 — this book follows one heat-seeking missile from a desert workbench to a duel in the sky, and every clever idea it forced the other side to invent.

## Narrative spine (the editorial bet)

**The arms race IS the story.** Not a parts catalog — a duel of moves and counter-moves:

gun → heat-seeker → flares → smarter seekers → radar missiles → chaff/RWR → stealth

Human anchor in the middle act: Bill McLean's China Lake story (unofficial project, volunteer evenings, skeptics, first drone kill 1953) gives the book its human spine — the heat-seeker was built by a small stubborn team in the desert, not a faceless factory.

Frame device: open mid-duel (two jets, one missile, flares blooming) with the question unanswered; return to the same duel near the end, now fully readable by the reader; close with the arms-race spiral as the page structure (closing-as-invention).

## Density plan

Hero/cutaway pages T4–T5 (gpt-image-2 single-shot territory). Cinematic beats T2–T3. No page past T5 — split instead.

## Caption clarity commitments

- Every technical term glossed inline on first use: infrared, seeker, gimbal, reticle (call it the "spinning wagon-wheel disk"), proportional navigation, hardpoint, radar, chaff, radar cross-section.
- No cryptic teasers; say the punchline plainly.
- Names grounded on first use ("an engineer named Bill McLean", "the AIM-9 Sidewinder — America's heat-seeking missile").
- This is a real engineering book that happens to be readable by a 7-year-old. Clear, not dumbed down.

## Content guardrails

- Engineering and physics focus. The duel framing is jets vs jets as machines; no depictions of pilots dying, no burning crews, no ground casualties. Drone-target kills and "the missile found the flare instead" carry the drama.
- gpt-image-2 safety: explosions rendered as distant flak-bursts / target-drone hits, never cockpit-level violence.

## Deliberate departures / notes

- First combat kill (24 Sept 1958, Taiwan Strait) says "MiG fighters" — sources disagree on MiG-15 vs MiG-17.
- Hero jet is a real F-16 (universal, wingtip Sidewinder rails); adversary is a generic dark twin-tail fighter, deliberately not named to keep the duel timeless.
- Falklands hit-rate stated as "almost 9 of every 10" per source (24 fired / 88%).

## Facts discipline

Every date/number in `04-SCRIPT.md` traces to `research/RESEARCH-NOTES.md`. No model-memory facts.
