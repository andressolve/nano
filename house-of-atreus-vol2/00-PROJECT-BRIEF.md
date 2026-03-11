# The House of Atreus — Volume 2: "The Reckoning"

## Overview

**Title:** The House of Atreus
**Subtitle:** Volume 2: The Reckoning
**Chapter:** 2 of 2
**Target Audience:** Young readers 10+ (Francisco & Sebastian), sophisticated narrative
**Image Generation Model:** Google Nano Banana Pro (Gemini 3 Pro Image) via MCP
**Pages:** Cover + 18 story pages + back cover (20 total images)

---

## What Happened Before

Volume 1 covered three generations of the curse on the House of Atreus:

1. **Tantalus** killed his son Pelops and served him to the gods. The gods restored Pelops with an ivory shoulder. Tantalus was condemned to eternal torment.
2. **Pelops** won Princess Hippodamia by bribing charioteer Myrtilus to sabotage the king's chariot. Then Pelops threw Myrtilus from a cliff. Dying curse #2.
3. **Atreus and Thyestes**, sons of Pelops, destroyed each other. Thyestes stole Atreus's wife and throne. Atreus retaliated by killing Thyestes's sons and serving them at a feast. Dying curse #3. The sun reversed its course in horror. An oracle told Thyestes that only a son by his own daughter could avenge him — that child, **Aegisthus**, was raised as a weapon.

**Visual throughlines from Volume 1:**
- The bronze serving dish (Tantalus's feast → Atreus's feast)
- The road to Mycenae's Lion Gate (Thyestes fleeing → Aegisthus approaching)
- The Lion Gate itself — appears in both volumes as the seat of cursed power
- The cycle: feast → betrayal → curse → repeat

---

## Story Summary

The curse reaches its climax and resolution across the Trojan War generation.

**Chapter 4: The Sacrifice (Pages 1–5).** Agamemnon, son of Atreus, commands the Greek fleet at Aulis bound for Troy. But Artemis becalms the winds. The seer Calchas reveals the price: Agamemnon must sacrifice his daughter Iphigenia. He lures her with a false promise of marriage to Achilles. Clytemnestra discovers the truth too late. Iphigenia walks to the altar herself. The wind blows. The fleet sails. Something dies in Clytemnestra.

**Chapter 5: The Homecoming (Pages 6–11).** Ten years pass. Clytemnestra takes Aegisthus as lover and co-ruler, nursing her rage. Troy falls. Agamemnon returns triumphant with captive Cassandra — prophetess cursed to speak truth and never be believed. Clytemnestra welcomes him with a purple carpet. She and Aegisthus murder him in the bath, tangled in a robe. Cassandra, who foresaw everything, is killed too. A servant smuggles baby Orestes to safety.

**Chapter 6: The Trial (Pages 12–18).** Years later. Electra, Agamemnon's daughter, has been made a servant in her own home. Orestes returns from exile. Apollo commands him to avenge his father. Orestes kills Aegisthus, then faces his mother. Clytemnestra bares her breast — can he kill the woman who nursed him? He does. The Furies descend — ancient spirits of blood vengeance, shrieking, relentless. Orestes flees, maddened. Athena intervenes. She convenes the first jury trial in Athens. Both sides argue. The vote is tied. Athena casts the deciding vote: mercy. The Furies become the Eumenides. The cycle breaks. Justice replaces vengeance.

**Theme:** *The cycle of blood can only be broken by choosing justice over vengeance.*

---

## Palette

Same 5 base colors as Volume 1, but the balance shifts dramatically:

- **Warm sandstone** — architecture, continuity with Vol 1
- **Olive green** — landscape, life
- **Terracotta brown** — earth, blood, the past
- **Aegean blue** — the sea, distance, and in this volume: the cold gray of Aulis, the clean blue of Athens
- **Golden amber** — sunlight, Iphigenia's warmth, Apollo's presence, and the final Athenian daylight

**Palette progression:**
- **Pages 1–2 (Aulis):** Gray and muted. Overcast sky, flat sea, no golden light. Oppressive.
- **Pages 3–4 (Iphigenia arrives):** Warm golden light returns — she brings it. Then it dies at Aulis.
- **Page 5 (Sacrifice):** Gray breaking to gold as wind fills sails. But Clytemnestra is cold.
- **Pages 6–9 (Homecoming/Murder):** Warm golden return is ironic — beauty masking the trap. Then blood-red interior.
- **Pages 10–11 (Aftermath):** Cold torchlight, darkness.
- **Pages 12–13 (Orestes returns):** Soft dawn light — fragile hope.
- **Pages 14–15 (Killings):** Interior torchlight, then cold blue-black as Furies arrive.
- **Page 16 (Furies):** Palette DIES — cold blue-black dominates, warmth completely gone.
- **Pages 17–18 (Trial/Resolution):** Clean bright Athenian daylight. A NEW kind of warmth — not the deceptive golden of feasts, but honest, clear, open.

---

## Production Notes for Claude Code

### Critical Rules
1. Keep prompts under ~800 words. (Vol 1 hit one length error — trim even more aggressively.)
2. Reference images do 80% of character locking. Lean lock blocks only.
3. 3–4 panels per page maximum. Prefer 3.
4. Upload character reference images with EVERY page prompt.
5. Do NOT pad prompts with atmospheric description.

### File Structure
```
~/nano/house-of-atreus-vol2/
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
1. **Agamemnon** — appears Pages 1–5, 7, 9
2. **Clytemnestra** — appears Pages 3–10, 15
3. **Iphigenia** — appears Pages 3–5
4. **Cassandra** — appears Pages 7–8, 10
5. **Orestes** — appears Pages 12–18
6. **Electra** — appears Pages 11–13, 15–16
7. **Aegisthus** — appears Pages 6, 9–10, 14
8. **Athena** — appears Pages 17–18
9. **The Furies** — appears Pages 16–18

#### Phase 2: Page Generation
Generate sequentially: Cover → Pages 1–18 → Back Cover.

### Anti-Drift Watch Pages
- **Page 5 (Sacrifice):** Emotional peak, risk of children's book softness
- **Page 8 (Cassandra's vision):** Prophetic overlay, risk of going fantasy/painterly
- **Page 12 (Reversed sun full-page from V1 equivalent):** N/A but watch Page 16
- **Page 16 (Furies appear):** Supernatural horror, risk of cartoon monsters or over-stylization
- **Page 18 (Final page):** Bright Athens, risk of going too soft/optimistic

### Run in Automode
Do not ask for approval between generations. Generate all reference sheets and all pages sequentially without pausing. Only stop if a generation fails.
