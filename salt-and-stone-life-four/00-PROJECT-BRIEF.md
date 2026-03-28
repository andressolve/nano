# Salt and Stone — Life Four: The Father

## Overview

**Title:** Salt and Stone — Life Four: The Father
**Subtitle:** A Graphic Novel in Four Lives
**Chapter:** Life Four — The Father (age 25-26)
**Target Audience:** Francisco and Sebastian
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 20 story pages + back cover (22 total images)

---

## What Happened Before

### Life One: The Boy (age 9-10)
Nikos was a Greek boy on a small Aegean island. His father Alexios was a shipbuilder. A Persian raid destroyed the island. Alexios put Nikos on a trade ship to save him; the ship was wrecked in a storm. Nikos washed ashore near Sidon, a Phoenician city allied with Persia. He was taken in by Hasdrubal, a Phoenician shipwright who built ships for the Persian navy. Nikos chose to stay.

### Life Two: The Youth (age 14-15)
Five years later, Nikos was conscripted into Xerxes' fleet. He fought against Greeks at the Battle of Salamis — from the Persian/Phoenician side. His ship was rammed. Pulled from the sea by Athenian sailors, he ended up in Athens during its golden age, working the Piraeus shipyards, married to Lyra.

### Life Three: The Man (age 19-20)
Conscripted again by the Delian League, Nikos was shipwrecked for the third time and washed ashore on the Black Sea coast. Found by Asha, a Scythian rider, he was brought to the camp of Chief Targitaos. He learned to ride, discovered a people who thought cities were prisons. He burned the carved wooden ship — his last material tie to his Greek past — and chose to stay. He kept only the shell necklace his mother gave him.

### Visual Throughlines (MUST carry into Life Four)
- **Shell necklace** on leather cord (from his mother — never removed until this volume)
- **Scar on left palm** (from chisel slip as a child)
- **Burn scar on right forearm** (from Salamis)
- **No more wooden ship** — burned in Life Three. A new object emerges: a carved wooden horse.

---

## Life Four Story Summary

Six years after choosing the steppe. Nikos is 25-26, fully Scythian in dress and habit. He and Asha have a son, Kian, about four years old — a boy with his mother's high cheekbones and his father's deep brown eyes. Nikos rides, herds, lives under open sky. The shell necklace still hangs at his throat.

But Kian asks questions. About the necklace. About the sea ("What is the sea?"). About why his father's hands move differently when they work — faster, more precise, shaping wood in ways no Scythian does. Nikos deflects.

Chief Targitaos is aging. His body is failing, though his mind remains sharp. He sees what Nikos won't admit: that a man who carries stories in silence is building a wall, not freedom.

Greek traders from Olbia, a Black Sea colony, arrive at the camp. Nikos hears Greek spoken for the first time in years. The lead trader, Demetrios, recognizes something in Nikos — the scars, the accent beneath his Scythian, the shell necklace. He brings news from Athens, offers passage south. Nikos refuses. But the encounter cracks something open.

Nikos begins carving — a small wooden horse for Kian. His shipwright's hands shaping something new. He realizes: he burned the ship but his hands remember everything. The question isn't whether to go back. It's whether to let his son know the world is bigger than the steppe.

Targitaos dies — quietly, in winter. Nikos helps build the burial mound. The old chief's last words to Nikos echo: "A man who hides his past from his son makes a prison of silence."

Under the stars, Nikos tells Kian everything. The island. The fire. His father's hands. Hasdrubal. Salamis. Athens. Lyra. The shipwrecks. The sea. Then he removes the shell necklace — for the first time since his mother put it on him — and places it around Kian's neck.

Spring. The camp moves. Kian rides his own pony between his parents — shell necklace at his throat, carved wooden horse in his hand. He looks forward at the horizon. And once, over his shoulder, toward the south. Toward the sea he's never seen.

**Theme:** *Life One began with a father losing a son. Life Four ends with a father freeing a son. What we inherit isn't a place or a craft — it's the stories that let us choose for ourselves.*

---

## Palette

Life Four's palette tracks the seasons — and the emotional arc:

- **Pages 1-6 (Winter steppe):** Silver-gray grass, pale blue-white sky, frost on felt tents, warm amber firelight indoors. Cold, beautiful, austere.
- **Pages 7-9 (Traders arrive):** Mediterranean gold and terra cotta bleed into the steppe palette — bronze goods, olive oil amphorae, Greek clothing. The past invading the present.
- **Pages 10-14 (Late winter / conflict):** Muted, heavy. Gray sky, muddy earth, bare ground. The steppe at its least romantic.
- **Pages 15-17 (Death and grief):** Frost and silence. Pale, cold, still. The camp in mourning.
- **Pages 18-20 (Spring / resolution):** Green returning. Golden-green steppe, warm sunrise light, the most hopeful palette in the entire series. Life beginning again.

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
~/nano/salt-and-stone-life-four/
├── refs/           <- character reference sheets (generate first)
├── pages/          <- story pages (generate sequentially)
├── 00-PROJECT-BRIEF.md
├── 01-STYLE-GUIDE.md
├── 02-CHARACTERS.md
├── 03-SETTINGS.md
├── 04-SCRIPT.md
└── index.html      <- reader
```

### Generation Order

#### Phase 1: Character References
Generate reference sheets in this order:
1. **Nikos (Father, age 25-26)** — use Life Three Nikos reference from `~/nano/salt-and-stone-life-three/refs/` for facial continuity
2. **Asha (mid-to-late 20s)** — use Life Three Asha reference for continuity
3. **Kian (4-5, Nikos and Asha's son)** — use both parents' refs for blended features
4. **Targitaos (early 60s)** — use Life Three Targitaos reference, age him
5. **Demetrios (Greek trader, ~40)** — new character, no prior reference
- Save each to `~/nano/salt-and-stone-life-four/refs/`

#### Phase 2: Page Generation
1. Read `04-SCRIPT.md`
2. Generate pages sequentially (Cover -> Page 1 -> ... -> Page 20 -> Back Cover)
3. For EVERY page:
   - Upload the relevant character reference image(s)
   - Paste the 3-line style block from `01-STYLE-GUIDE.md`
   - Paste the lean character lock block from `02-CHARACTERS.md`
   - Include: "featuring the same characters shown in the reference images"
   - Use the exact prompt from `04-SCRIPT.md`
4. Save pages to `~/nano/salt-and-stone-life-four/pages/`

#### Anti-Drift Rules
- Kian is 4-5 and MUST look like a real child, not a cute cartoon. Include "NOT a children's book. Serious mature graphic novel, realistic proportions" in every prompt with Kian.
- Winter steppe should feel harsh and real — NOT a winter wonderland.
- The traders' arrival should feel intrusive, not exciting. Mediterranean gold disrupting the steppe palette.
- Targitaos's death is quiet, not dramatic. No theatrical poses.
- If drift occurs, add: `STYLE REINFORCEMENT: This is NOT a children's book. Render in serious, mature graphic novel style with realistic proportions and cinematic composition.`

### Run in Automode
Do not ask for approval between generations. Generate all reference sheets and all pages sequentially without pausing. Only stop if a generation fails completely.
