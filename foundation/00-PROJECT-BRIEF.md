# FOUNDATION — Book One: The Plan

**Format:** Narrative-mode graphic novel (fictional, dialogue-driven, multi-panel pages)
**Source:** Isaac Asimov, *Foundation* (1951) — Part I "The Psychohistorians" + Part II "The Encyclopedists"
**Series:** Foundation, Vol 1 of 3 planned (Vol 2 "The Priests" = The Mayors; Vol 3 "The Merchants" = The Traders + The Merchant Princes)
**Pages:** Cover + 16 landscape pages (3:2, 1536×1024) + reader + 5-question WHY-quiz
**Model:** gpt-image-2 standard (`mcp__openai-image-2__generate_image` / `edit_image`), quality high
**Folder:** `foundation/` (register prototypes in `style-tests/`, validated 2026-07-04)

## The one-sentence window

A mathematician proves the Galactic Empire must fall, is exiled for saying so — and fifty years later, on a bare rock at the edge of the Galaxy, his exiles discover their whole civilization was a chess move he made before they were born.

## Register

**1970s British SF paperback airbrush** — validated on two prototypes (`style-tests/test-trantor-airbrush.png`, `test-trial-airbrush-v4.png`), both user-approved. See 01-STYLE-GUIDE.md. This register is the sci-fi shelf's signature; do not drift toward oil-painting (bio shelf) or ink-line flat color (myth shelf).

## Structure

- **Act 1 — Trantor (P1–P7):** Gaal arrives → meets Seldon → psychohistory + the calculator → arrest → trial → Chen's bargain/exile → the Plan revealed to Gaal.
- **Act 2 — Terminus, 50 years later (P8–P15):** frontier colony → Rodric's visit and the plutonium slip → the Board's paralysis ("Violence is the last refuge of the incompetent") → Lord Dorwin → ultimatum + coup plan → Time Vault reveal (the Encyclopedia was a fraud) → resolution ("Obvious as all hell").
- **P16 — Closing-as-invention:** the Plan itself as the page — galaxy spiral, thousand-year arc, Terminus a glowing seed at the rim.

## Structural calls (from the greenlight session)

- The **Foundation itself is the protagonist**; Seldon's recorded presence is the recurring face across volumes (the Salt-and-Stone solution to the rotating cast).
- Gaal is the Act-1 POV and is deliberately dropped at the time jump, exactly as Asimov drops him. The P8 caption owns the jump explicitly — the reader is never left to infer it.
- Talky-risk mitigation: staged spectacle beats — Trantor orbital vista (P1), the metal world (P2), the trial hall (P5), Terminus frontier vista (P8), the Time Vault hologram (P13–14), the galaxy finale (P16).
- **P1 and P5 are already produced:** the two validated style-test pages slot in directly (arrival page, trial page). Copy into `pages/` — do not regenerate.

## Research & editorial honesty

All baked-in quotes verified against sources 2026-07-04 (Seldon Crisis transcripts of both parts + LitCharts + quote checks):
- Trantor: 40 billion people, all-metal single world-city. Empire has stood **12,000 years**.
- Trial: "Trantor will lie in ruins within the next three centuries." Interregnum **30,000 years**, reducible to **one thousand**.
- Gaal's calculator check: fall of Trantor within three centuries at **92.5%** probability.
- Chen (Chief Commissioner, the real power): "Dr. Seldon, you disturb the peace of the Emperor's realm." Seldon: "I shall not be alive half a decade hence." Exile = **20,000 families** to Terminus. "I accept exile."
- Second Foundation: "at the other end of the Galaxy... at Star's End."
- Encyclopedists (50 AF): Lewis Pirenne (Board chairman), Salvor Hardin (first Mayor), Anselm haut Rodric (Sub-prefect of Pluema, Envoy Extraordinary of Anacreon), the plutonium slip ("You still have nuclear power?"), Lord Dorwin (curled hair, blond sideburns, snuff box, drops his r's), symbolic-logic analysis (Dorwin's five days of talk = nothing; the treaty = no protection at all), Jord Fara and the Vault (opens on the 50th anniversary), Yohan Lee (Hardin's coup).
- Vault speech verbatim anchors: "I am Hari Seldon." / smoke line / "The Encyclopedia Foundation ... is a fraud, and always has been!" / "one, and only one, path" / "seeds ... of the Second Galactic Empire" / "the solution to your dilemma — is obvious!"
- Section's famous last line: "Obvious as all hell!"

Dialogue is **condensed adaptation** (bubbles ≤ ~8 words where possible); the iconic lines above are kept verbatim or near-verbatim. No invented facts; no invented numbers.

## Production notes

- Lettering rulebook (01-STYLE-GUIDE) is LAW — evolved v1→v4 on the trial prototype. Speakers staged left-to-right in speaking order. Design attribution out at script level; do not chase it in QA.
- `thinking=true` is broken in the openai-image-2 MCP (unknown `reasoning` param → 400). Standard mode only.
- Multi-character pages: composite plates per act (Act 1: Gaal+Seldon; Act 2: Hardin+Pirenne). P6 anchors on the finished P5 trial page to keep hall + commissioners + Seldon identical. Vault pages anchor on `ref_seldon_hologram` (dedicated apparatus ref — the Icarus winged-Daedalus lesson).
- Cover credits Asimov: "after the novel by ISAAC ASIMOV".
