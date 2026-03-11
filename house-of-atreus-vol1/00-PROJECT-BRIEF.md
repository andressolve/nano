# The House of Atreus — Volume 1: "The Curse"

## Overview

**Title:** The House of Atreus
**Subtitle:** Volume 1: The Curse
**Chapter:** 1 of 2
**Target Audience:** Young readers 10+ (Francisco & Sebastian), sophisticated narrative
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 15 story pages + back cover (17 total images)

---

## Story Summary

The origin of the curse on the House of Atreus, spanning three generations.

**Chapter 1: The Feast of Tantalus (Pages 1–4).** Tantalus, king of Sipylus, kills his son Pelops and serves him to the Olympian gods at a banquet — testing whether they truly see everything. The gods detect the crime instantly (except Demeter, who eats a piece of shoulder). Zeus restores Pelops to life with an ivory shoulder. Tantalus is condemned to eternal torment in Tartarus — standing in water he can never drink, beneath fruit he can never eat.

**Chapter 2: The Chariot Race (Pages 5–8).** Young Pelops seeks the hand of Princess Hippodamia. Her father King Oenomaus challenges suitors to a chariot race — lose and you die. Thirteen skulls line the gate. Pelops bribes the king's charioteer Myrtilus to sabotage the royal chariot. Pelops wins. But when Myrtilus demands his reward, Pelops throws him from a cliff into the sea. Dying, Myrtilus curses Pelops and all his descendants. The second curse on the house.

**Chapter 3: The Brothers (Pages 9–15).** Pelops's sons Atreus and Thyestes inherit Mycenae and each other's hatred. Thyestes seduces Atreus's wife and steals the golden fleece — symbol of kingship. Atreus discovers the betrayal. He pretends to reconcile, invites Thyestes to a feast, then reveals he has killed Thyestes's young sons and served them to their father. Thyestes flees, cursing the house again. The sun reverses its course in horror. An oracle tells Thyestes that only a son born of his own daughter can avenge him. That child — Aegisthus — is raised as a weapon. Volume ends with Thyestes and young Aegisthus approaching Mycenae under moonlight.

**Theme:** *Sin passes from parent to child — each generation believes it is justified, and each makes things worse.*

---

## Palette

- **Warm sandstone** — architecture, ground, human warmth, the deceptive beauty of the world
- **Olive green** — Mediterranean landscape, life, the natural world that witnesses human horror
- **Terracotta brown** — earth, blood dried to brown, the weight of the past
- **Aegean blue** — the sea, distance, the world beyond the curse
- **Golden amber** — sunlight, divine presence, feasts (both real and corrupted)

**Palette shift:** Pages 1–8 are warm and golden. Pages 9–11 shift progressively darker as Atreus's revenge unfolds. Page 12 (the sun reversing) uses the palette at its most distorted — amber becomes sickly, gold becomes bile. Pages 13–15 are cold moonlight and shadow.

---

## Production Notes for Claude Code

### Critical Rules
1. Keep prompts under ~800 words.
2. Reference images do 80% of character locking. Text is reinforcement only.
3. 3–4 panels per page maximum.
4. Upload character reference images with EVERY page prompt.
5. Do NOT pad prompts with atmospheric description.

### File Structure
```
~/nano/house-of-atreus-vol1/
├── refs/          ← Character reference sheets
├── pages/         ← Cover + story pages + back cover
├── 00-PROJECT-BRIEF.md
├── 01-STYLE-GUIDE.md
├── 02-CHARACTERS.md
├── 03-SETTINGS.md
└── 04-SCRIPT.md
```

### Generation Order

#### Phase 1: Character References
1. **Tantalus** — appears Pages 1–3
2. **Pelops** — appears Pages 3–7
3. **Hippodamia** — appears Pages 4, 7
4. **Myrtilus** — appears Pages 5–7
5. **Atreus** — appears Pages 8–11, 14
6. **Thyestes** — appears Pages 8–13, 15

#### Phase 2: Page Generation
Generate sequentially: Cover → Pages 1–15 → Back Cover.

### Anti-Drift Watch Pages
- **Page 3 (Tartarus/Restoration)** — high-contrast scene, risk of going too fantasy/painterly
- **Page 6 (Chariot race)** — action scene, risk of style going cartoonish
- **Page 11 (Feast reveal)** — emotional intensity, risk of going soft/children's book
- **Page 12 (Reversed sun)** — surreal sky, risk of over-stylization

If drift occurs, add to prompt:
```
STYLE REINFORCEMENT: This is NOT a children's book. Render in serious, mature graphic novel style with realistic proportions and cinematic composition.
```

### Run in Automode
Do not ask for approval between generations. Generate all reference sheets and all pages sequentially without pausing. Only stop if a generation fails.
