# FOUNDATION — Book Two: The Priests

**Format:** Narrative-mode graphic novel (fictional, dialogue-driven, multi-panel pages)
**Source:** Isaac Asimov, *Foundation* (1951) — Part III "The Mayors" (originally "Bridle and Saddle", 1942)
**Series:** Foundation, Vol 2 of 3 planned (Vol 1 "The Plan" shipped 2026-07-04; Vol 3 "The Merchants" = The Traders + The Merchant Princes)
**Pages:** Cover + 16 landscape pages (3:2, 1536×1024) + reader + 5-question WHY-quiz
**Model:** gpt-image-2 standard (`mcp__openai-image-2__generate_image` / `edit_image`), quality high
**Folder:** `foundation-vol2/` (register inherited verbatim from `foundation/`)

## The one-sentence window

Thirty years after the first crisis, the Foundation rules its four barbarian neighbors through a religion of science — and when Prince Regent Wienis aims a resurrected Imperial battleship at Terminus, Salvor Hardin lets the religion itself pull the trigger.

## Register

**1970s British SF paperback airbrush** — identical to Vol 1, style block verbatim from `../foundation/01-STYLE-GUIDE.md`. Do not drift toward oil-painting (bio shelf) or ink-line flat color (myth shelf). Vol 1's finished pages are the register anchors.

## Structure

- **Act 1 — Terminus, 80 F.E. (P1–P4):** thirty-years-later establishing + the religion of science → Sermak's Action Party confronts Hardin → Verisof (ambassador/High Priest) briefs him on Wienis → the derelict Imperial battlecruiser and Hardin's decision to repair it (with a buried secret).
- **Act 2 — Anacreon (P5–P9):** the royal court (Lepold, Wienis) → Hardin publicly announces he will attend the coronation → the flagship *Wienis* and priest Theo Aporat → coronation night spectacle → Wienis springs the trap.
- **Act 3 — Midnight (P10–P14):** Aporat curses the flagship → planet-wide interdict blackout → Lefkin's forced broadcast → the blaster and the force shield → surrender, "bridle and saddle."
- **P15 — The Vault, again:** Seldon's second appearance — spiritual vs temporal power, plus the warning that seeds Vol 3.
- **P16 — Closing-as-invention:** the Foundation as lamp, the four armed kingdoms as helpless moths.

## Structural calls

- **The Foundation itself is the protagonist**; Seldon's hologram recurs as the face across volumes (P15).
- Hardin carries the volume as an **aged continuation of Vol 1's lock** (62, not mid-thirties) — new ref extracted by aging the Vol 1 ref, never a fresh unrelated face.
- Talky-risk mitigation: staged spectacle beats — the temple reactor-altar (P1/P3), the derelict cruiser adrift (P4), the Nyak hunt (P5), the coronation aura + floating throne (P8), the planetary blackout (P11), the galaxy finale (P16).
- Sermak's arc (fire-breathing opposition → concession) frames the volume; his delegation companions stay unnamed background (single-page walk-ons).

## Research & editorial honesty

Verified 2026-07-05 (Wikipedia Foundation-novel plot section, asimovreviews.net, BookRags chapter summaries, Goodreads verbatim quote lists, Asimov Fandom "Bridle and Saddle", asimovseries.com):

- Timeline: **80 F.E., thirty years** after the Encyclopedists / Hardin's bloodless coup. Hardin is **62**.
- The Foundation controls the Four Kingdoms by selling atomic technology wrapped in **the religion of science**: the Galactic Spirit, priests trained on Terminus, miracles that are machines.
- **Poly Verisof** = Foundation ambassador to Anacreon AND its High Priest (the double life is canon).
- **Sef Sermak**, young City Councilman, leads the Action Party against Hardin's "appeasement."
- Anacreon salvages a **derelict Imperial battlecruiser**; Wienis demands the Foundation repair it; Hardin agrees over furious opposition; Foundation engineers secretly install an **ultrawave relay** (kill switch).
- **King Lepold I is sixteen**, hunts giant **Nyak birds**; his uncle **Prince Regent Wienis** rules until his majority and plots the coup; **Admiral Prince Lefkin** (Wienis's son) commands the flagship, renamed ***Wienis***.
- Coronation night = the fleet's launch hour. **Theo Aporat**, priest aboard the flagship, curses the ship in the name of the Galactic Spirit as the relay shuts it down deck by deck; the crew mutinies; Lefkin is forced to **broadcast** the fleet's stand-down and demand Wienis answer for the war.
- At midnight the priests place Anacreon under **interdict** — every Foundation machine and temple goes dark at once; the mob turns on Wienis, not the Foundation.
- Wienis fires a blaster at Hardin point-blank; Hardin wears a **personal force shield**; the beam is harmless; **Wienis turns the weapon on himself** (rendered OFF-PAGE — see production notes).
- Verbatim Hardin epigrams used in this volume (all verified as Foundation/Hardin): "Never let your sense of morals prevent you from doing what is right!" · "It pays to be obvious, especially if you have a reputation for subtlety." · "To succeed, planning alone is insufficient. One must improvise as well." · "Violence is the last refuge of the incompetent" (Vol 1's line, returned as a callback against Wienis — in the book Hardin's epigram is explicitly in play during the confrontation).
- Hardin's resolution line (near-verbatim): the religion of science was their **"bridle and saddle,"** because it placed the lifeblood of atomic power in the hands of the priesthood — and every priest answers to Terminus.
- Seldon's second Time Vault appearance (verbatim anchor): **"The Spiritual Power, while sufficient to ward off attacks of the Temporal, is not sufficient to attack in turn."** Religion defends the Foundation but cannot carry expansion — the explicit seed of Vol 3 (trade).

### Deliberate departures / compressions

- Timeline compressed: repair of the cruiser, coronation, and crisis are staged as one continuous arc (the book spreads them over months of chapters).
- Wienis's suicide is **stated obliquely in caption ("Wienis did not leave that room alive"), never depicted and never named as suicide** — audience-appropriate and required by image moderation (self-harm filter).
- The Nyak hunt shows pursuit, never a kill (moderation: nothing living is shot, per Scattergun discipline).
- Sermak's on-page concession (P14) compresses the book's closing council scene.
- The secret relay is flagged plainly to the reader on P4 ("one thing Anacreon never learned about") — clear suspense, not a withheld fact, per the caption-clarity rule.

## Production notes

- Lettering rulebook v4 (01-STYLE-GUIDE) is LAW. Speakers staged left-to-right in speaking order; attribution designed out at script level.
- **Refs, not prose** (user directive 2026-07-05): every character on 2+ pages gets a reference image. This volume's audit puts SEVEN characters over the line — see 02-CHARACTERS for the ref plan, including the **single-generation GROUP ref sheet experiment** on the Anacreon court.
- **Distinct recurring characters get distinct COSTUMES** (Vol 1 round-3 QA lesson) — costume matrix in 02-CHARACTERS.
- Multi-ref `edit_image` (`imagePaths`, up to 16) is the intended workflow — **verify the reconnected MCP schema exposes `imagePaths` before production**; fallback is Vol 1's PIL composite plates.
- `thinking=true` is broken in the openai-image-2 MCP (unknown `reasoning` param → 400). Standard mode only.
- Cover credits Asimov: "after the novel by ISAAC ASIMOV".
