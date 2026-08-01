# 00 — PROJECT BRIEF

## THE LAKE CITY
### Book One: The Boy Who Wanted the War

| | |
|---|---|
| **Format** | Narrative-mode graphic novel (true multi-panel, dialogue-driven) |
| **Orientation** | 3:2 **landscape**, 1536×1024 — desktop reading. Do not mix orientations. |
| **Register** | Codex ink-line + flat color. See `01-STYLE-GUIDE.md`. Anchor image: `style-samples/sample-A-codex-inkline.png` (user-approved 2026-07-25) |
| **Model** | gpt-image-2 standard, `quality: "high"` |
| **Page target** | Cover + 22 pages. Target, not a contract — expand if the arc needs it. |
| **Volume window** | Tlaxcala, autumn 1519 → the seizure of Moctezuma, November 1519 |
| **Series** | Three books. This is Book One. |
| **Execution** | Planning by Claude; **page generation handed to Codex.** See `HANDOFF-CODEX.md`. |

---

## The one-sentence window

A Tlaxcalan boy who has been taught from birth to hate the Mexica walks into their capital beside the strangers who intend to destroy it — and finds the most magnificent city in the world.

## What this book is

An adventure told from the winning side, by someone who ends up mourning the loss.

Our protagonist is **not** one of the Spaniards. He is a seventeen-year-old commoner from Tlaxcala — a city-state that had fought the Mexica for three generations, had never been conquered, and had never been allowed to be at peace. He arrives with Cortés's column as a runner and errand-boy attached to the interpreter's household: the kid nobody notices, sent through every door, present in every room where something is decided. That is the engine of the book. He is a boy made of ears.

He wants the war. He gets it. Books Two and Three are the bill.

## Why this POV was chosen

Three reasons, all load-bearing:

1. **The cultural window opens from the inside.** A Spanish POV makes the Nahua world a curiosity to be described. A Tlaxcalan POV makes it a world our narrator already belongs to — he knows what a tribute-list means, what the calendar is counting, why a lord's cloak is the length it is. The reader learns the culture the way he learns the *city*: as a native of the world and a stranger to its capital.
2. **He can talk to everyone.** He shares a language with the Mexica and a cause with the strangers. Every scene is available to him, and every scene is a conversation with something at stake. This is what makes a dialogue-driven book possible at all.
3. **He is morally implicated.** He is not a witness. He helps. The book has no innocent narrator and no villain-shaped enemy, which is the same reason *House of Atreus* worked.

## The story spine

**He wanted the war more than he understood the city.** Every volume tests that sentence again with a higher price attached.

Not a thesis about conquest, not a lesson about empires. A boy, a city, and what he helped do to it.

## Book One arc

| Act | Beats |
|---|---|
| **I — The Hatred (Tlaxcala)** | Who he is and what the Mexica cost his family. The lords' debate: ally with the strangers, or destroy them. He is sent along. |
| **II — The Road (Cholula → the pass)** | The alliance's first taste of what it has joined itself to. He crosses the volcano pass and sees the lake for the first time. |
| **III — The City (Tenochtitlán)** | The causeway. The meeting. The market. The temple. The city is not what he was told. He starts to love the thing he came to help kill. |
| **IV — The Silence** | The strangers seize the king inside his own palace. He understands, before anyone tells him, what is coming — and says nothing. |

**Closing beat:** the last page is the boy alone on a rooftop over the lit city, having said nothing. The reader knows what he knows.

## Series map

| Book | Title | Window | Arc |
|---|---|---|---|
| **One** | The Boy Who Wanted the War | Autumn 1519 → Nov 1519 | Arrival. The city at its height. The king taken. His silence. |
| **Two** | The Broken Bridges | Spring–summer 1520 | The festival massacre, the king's death, the night the strangers are driven out across the causeways — and Tlaxcala takes them in anyway. Then the sickness arrives. |
| **Three** | The Siege | 1521 | The boats on the lake, the causeway fighting, the young last king, the fall. Tlaxcala wins. He walks through the ruins of the city he coveted. |

Books Two and Three are mapped, **not written.** Do not let Book One's script reach for their material — Book One ends on the silence.

## Editorial rules for this volume

- **Research-first.** Every date, name, place, and protocol detail is checked against `RESEARCH.md` before it enters the script. Disputed material is written *around*, not asserted. No invented quotation is ever attributed to a real person — where the sources give us only a literary reconstruction of a speech, our characters speak our own plain words instead, and the script says so in a note.
- **Only the protagonist is invented.** Moctezuma, Cortés, Malintzin, the Tlaxcalan lords, Cuitláhuac are real and are handled accurately.
- **The Mexica are not scenery and not monsters.** The city is rendered as what it was: the largest, cleanest, best-fed city most of these characters would ever stand in. Its violence is told honestly and never as spectacle — see the sacrifice rule in `01-STYLE-GUIDE.md`.
- **No treatise.** Context arrives through dialogue, argument, and what characters want from each other. If a caption is explaining rather than telling, cut it and give the fact to somebody who has a reason to say it out loud.
- **Every caption stands alone.** No cryptic teasers, no withheld facts, no unglossed period vocabulary, no name without a one-line role on first use. A first-time reader who knows nothing about any of this must be able to follow every page on first read.
- **Nahuatl words get an English helper in-panel, always** — `tlatoani — the Speaker, their king`. The reader should end this book with a dozen Nahuatl words they actually own.

## Production notes

- Refs before pages. No page is generated until every character on it has an approved ref in `refs/`.
- Three prototypes spanning density and layout before any bulk run.
- Multi-reference `edit_image` is available (`imagePaths`, up to 16) — use it for multi-character pages rather than describing unanchored characters in prose.
- Cost envelope: ~$5–6 for the volume (refs + 23 images at ~$0.21 each + a small regen allowance).

## Settled by research — no open questions remain

All three of the things this book was resting on were checked before a line of script was written. Two of them were wrong. Details and sources in `RESEARCH.md`.

- **Protagonist's name: OLIN**, single *l* — the scholarly orthography, "movement," the day-sign of the current Sun, which is prophesied to end in earthquake. Confirmed plausible for a commoner youth and attached to no well-known historical figure. The honorific `-tzin` is a form of *address*, not part of a commoner's name — it is held back and spent once, deliberately, as a warmth beat.
- **The POV mechanism is documented, not invented.** Bernal Díaz records Tlaxcalans offering ten thousand men and a thousand being accepted as porters and road-clearers, quartered with the Spanish in the outer courts of the Axayacatl palace, and warning Aguilar from *inside* the city. Olin's access needed no fallback.
- **The Tlaxcalan debate is father against son, not lord against lord.** Maxixcatzin *and* Xicotencatl the Elder were both for the alliance; only Xicotencatl the Younger argued against it. The council page (P4) was rewritten around the blind father overruling his son — which is a better scene than the one it replaced.
- **The emotional engine is the salt-and-cotton encirclement, not the "captive farm."** The claim that the Mexica deliberately kept Tlaxcala unconquered as a source of sacrificial captives rests on Andrés de Tapia alone, is denied by Muñoz Camargo, and is rejected or heavily qualified by modern scholarship. It appears in this book **only as a Mexica boast in someone's mouth**, never as narration. Olin's hatred is footed instead on the blockade — no salt, no cotton — which comes from Xicotencatl's own recorded words.
- **Never a precise population figure.** The range 200,000–300,000 and "very probably larger than any city in western Europe." Never a number.
- **The seizure of the Speaker is deliberately ambiguous** on the page, because it is deliberately ambiguous in the sources. See P20.
