# Salt and Stone — Life Three: The Man

## Overview

**Title:** Salt and Stone — Life Three: The Man
**Subtitle:** A Graphic Novel in Three Lives
**Chapter:** Life Three — The Man (age 19-20) — FINALE
**Target Audience:** Francisco and Sebastian
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 20 story pages + back cover (22 total images)

---

## What Happened Before

### Life One: The Boy (age 9-10)
Nikos was a Greek boy on a small Aegean island. His father Alexios was a shipbuilder. A Persian raid destroyed the island. Alexios put Nikos on a trade ship to save him; the ship was wrecked in a storm. Nikos washed ashore near Sidon, a Phoenician city allied with Persia. He was taken in by Hasdrubal, a Phoenician shipwright. He discovered Hasdrubal builds ships for the same Persian navy that destroyed his home. He chose to stay.

### Life Two: The Youth (age 14-15)
Five years later, Nikos is conscripted into Xerxes' fleet. He fights against Greeks at the Battle of Salamis — from the Persian/Phoenician side. His ship is rammed. He's in the water again. Pulled from the sea by Athenian sailors, he survives because he speaks Greek. He ends up in Athens during its post-war golden age, working the Piraeus shipyards, witnessing democracy up close.

### Visual Throughlines (MUST carry into Life Three)
- **Shell necklace** on leather cord (from his mother — never removed)
- **Scar on left palm** (from chisel slip as a child)
- **The carved wooden ship** (Greek-style, pocket-sized — made by his father)
- **New in Life Two:** A burn scar on his right forearm from Salamis

---

## Life Three Story Summary

Four years after Salamis. Nikos is 19-20, established in Athens. He has a trade (shipwright at Piraeus), a home, a wife named Lyra. He is Athenian now — or so he tells himself. Athens is projecting power through the Delian League, demanding tribute from island states, building an empire while calling it an alliance.

Nikos is conscripted — again — this time onto an Athenian trireme for a League expedition across the Aegean toward the Black Sea. His shipmate Philo, a talkative Athenian sailor, becomes his companion. A storm wrecks the ship off the northern Black Sea coast, in Scythian territory.

Nikos washes ashore — for the third time. But this time there are no cities, no shipyards, no timber trade to save him. The Scythians are steppe nomads. No walls, no writing, no fixed anything. Everything Nikos has built his identity around — Greek, Phoenician, Athenian, shipwright — is meaningless here.

He is found by Asha, a Scythian rider and scout. Brought to the camp of Chief Targitaos. He must learn to ride, to herd, to live under open sky. He discovers a people who think cities are prisons and the sea is madness — and who are not wrong.

Over months, he stops trying to get back. He realizes he has been building other people's lives in other people's cities his entire life. The steppe offers something none of his previous lives did: the freedom to simply be, without performing an identity.

He stays. He chooses freedom over civilization.

**Theme:** *Who are you when everything you've built is gone — again? What survives every shipwreck is the only thing that's truly yours.*

---

## Palette

Life Three's palette is the most radical shift yet:
- Life One: warm Mediterranean golds and terra cotta
- Life Two: dark ocean blues and fire
- **Life Three: vast open greens, golden grassland, pale sky, earth brown, amber firelight**

The Athens pages (1-4) still carry Life Two's bronze-gold Athenian tones. The sea/storm (5-7) returns briefly to dark blues. But from page 8 onward — the steppe — the palette opens up dramatically. Huge skies, endless grass, warm earth, soft amber light. It should feel like breathing after being underwater.

---

## Production Notes for Claude Code

### Critical Rules
1. **Keep prompts under ~800 words.** Nano Banana degrades with long prompts.
2. **Reference images do 80% of character locking.** The text lock block is reinforcement only — keep it to 4-5 lines.
3. **3-4 panels per page maximum.** More panels = longer prompts = worse results.
4. **Upload character reference images with EVERY page prompt.** Always include: "featuring the same characters shown in the reference images"
5. **Do NOT pad prompts** with atmospheric description the model won't use. Be precise, be lean.

### File Structure
```
~/nano/salt-and-stone-life-three/
├── refs/           ← character reference sheets (generate first)
├── pages/          ← story pages (generate sequentially)
├── 00-PROJECT-BRIEF.md
├── 01-STYLE-GUIDE.md
├── 02-CHARACTERS.md
├── 03-SETTINGS.md
└── 04-SCRIPT.md
```

### Generation Order

#### Phase 1: Character References
Generate reference sheets in this order:
1. **Nikos (Man, age 19-20)** — most important, generate first
2. **Lyra** (Athenian wife) — appears pages 1-4 only
3. **Philo** (Greek sailor) — appears pages 4-7
4. **Asha** (Scythian rider) — appears pages 8-20, key character
5. **Chief Targitaos** (Scythian elder) — appears pages 10-16
- Save each to `~/nano/salt-and-stone-life-three/refs/`
- If Life Two Nikos (Youth) reference exists in `~/nano/salt-and-stone-life-two/refs/`, upload it when generating the adult Nikos reference for facial continuity

#### Phase 2: Page Generation
1. Read `04-SCRIPT.md`
2. Generate pages sequentially (Cover → Page 1 → ... → Page 20 → Back Cover)
3. For EVERY page:
   - Upload the relevant character reference image(s)
   - Paste the 3-line style block from `01-STYLE-GUIDE.md`
   - Paste the lean character lock block from `02-CHARACTERS.md`
   - Include: "featuring the same characters shown in the reference images"
   - Use the exact prompt from `04-SCRIPT.md`
4. Save pages to `~/nano/salt-and-stone-life-three/pages/`

#### Anti-Drift Rules
- The steppe pages (8-20) are at HIGH RISK of going "fantasy illustration" or "children's book pastoral." They must feel grounded, real, cinematic — like a Terrence Malick film, not a fairy tale.
- Nikos at 19-20 must look like a man, not a teenager. Broader shoulders, weathered face, stubble.
- Scythian characters should look Central Asian/Eurasian, not European. Historically accurate.
- If drift occurs, add: `STYLE REINFORCEMENT: This is NOT a children's book. Render in serious, mature graphic novel style with realistic proportions and cinematic composition.`

### Run in Automode
Do not ask for approval between generations. Generate all reference sheets and all pages sequentially without pausing. Only stop if a generation fails completely.
