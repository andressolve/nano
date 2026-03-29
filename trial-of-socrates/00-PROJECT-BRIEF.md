# The Trial of Socrates

## Overview

**Title:** The Trial of Socrates
**Format:** Graphic novel (single volume)
**Target Audience:** Young readers 10+ (Francisco & Sebastian)
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 15 story pages + back cover (17 total images)

---

## Story Summary

Athens, 399 BC. Told through the eyes of Alexis, a 14-year-old potter's son who has been attending Socrates' informal conversations in the agora for about a year.

**Act 1: The Gadfly (Pages 1–4).** We meet Alexis watching Socrates in the agora — magnetic, funny, relentless in his questioning. We meet Doros, Alexis's father, a practical potter who thinks philosophers are dangerous. The charges come: corrupting the youth, introducing new gods. Doros forbids Alexis from attending the trial.

**Act 2: The Trial (Pages 5–9).** Alexis goes anyway. We see the Dikasterion — 501 jurors, the open-air court. Meletus presents the accusation. Socrates mounts his defense: the Oracle at Delphi, the gadfly metaphor, his refusal to grovel. The vote: guilty, 280 to 221. Then the counterproposal — instead of exile, Socrates suggests Athens reward him with free meals. The jury votes death.

**Act 3: The Hemlock (Pages 10–15).** Crito arranges an escape. Socrates refuses — a man who flees his own convictions has none. Alexis visits the prison. The final morning: Socrates drinks the hemlock, calm, even joking. His last words about the rooster. Alexis walks through an Athens that hasn't changed — and everything has changed.

**Theme:** *What does it mean to believe something so strongly you'd die for it? And what do you do when someone you admire makes a choice you can't understand?*

**Connection to existing work:** Athens is already established in the collection (Salt and Stone Life Two, House of Atreus Vol 2's trial scene). The theme of public justice echoes the Oresteia's climax.

---

## Palette

- **Warm honey-gold** — Athenian sunlight, agora warmth, everyday life
- **Marble white** — columns, architecture, the ideal Athens represents
- **Terracotta** — pottery, domestic life, the human world
- **Shadow blue** — the courtroom, the prison, what Athens becomes
- **Olive green** — life, the natural world, what persists

**Palette shift:** Pages 1–4 are warm and golden (the agora, home). Pages 5–9 shift to harder light — marble white and shadow (the court). Pages 10–13 are prison: warm lamplight against cold stone. Pages 14–15 return to golden light but with something absent.

---

## Production Notes

### Critical Rules
1. Keep prompts under ~800 words.
2. Reference images do 80% of character locking. Text is reinforcement only.
3. 3–4 panels per page maximum.
4. Upload character reference images with EVERY page prompt.
5. Do NOT pad prompts with atmospheric description.

### File Structure
```
~/nano/trial-of-socrates/
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
1. **Alexis** — appears all pages
2. **Socrates** — appears Pages 1, 3, 5, 7, 8, 9, 10, 11, 12, 13
3. **Doros** — appears Pages 2, 4, 15
4. **Meletus** — appears Pages 5, 6

#### Phase 2: Page Generation
Generate sequentially: Cover → Pages 1–15 → Back Cover.

### Anti-Drift Watch Pages
- **Page 6 (Meletus speaks)** — courtroom crowd, risk of losing character detail
- **Page 9 (Counterproposal)** — emotional intensity, risk of children's book softness
- **Page 13 (Hemlock)** — critical emotional scene, must stay grounded and cinematic

If drift occurs, add to prompt:
```
STYLE REINFORCEMENT: This is NOT a children's book. Render in serious, mature graphic novel style with realistic proportions and cinematic composition.
```

### Run in Automode
Do not ask for approval between generations. Generate all reference sheets and all pages sequentially without pausing. Only stop if a generation fails.
