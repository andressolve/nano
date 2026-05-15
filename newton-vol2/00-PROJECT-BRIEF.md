# The Invisible Forces — Book Two — Project Brief

## Title

**The Invisible Forces: Isaac Newton, Book Two**

Subtitle for the cover: *The Mint, the Society, the Reckoning.*

## One-sentence window

This volume covers Isaac Newton from the exhaustion that followed the *Principia* (1687) through the breakdown of 1693, the Mint years and the prosecution of William Chaloner, the publication of the *Opticks*, the Royal Society presidency, the long war with Leibniz, the private alchemy and chronology by candlelight at Kensington, the South Sea Bubble, and his death and burial at Westminster Abbey on 28 March 1727.

## Page count

**24 pages = cover + 23 story pages,** mirroring Book One's structure.

## Image model

OpenAI **gpt-image-2 standard** (no thinking) via `mcp__openai-image-2__{generate_image,edit_image}`. Same pipeline as Book One. Oil-painting realism. 1536×1024 landscape. Locked.

## Cost envelope

~$7.50:
- ~11 refs × $0.21 ≈ $2.31
- 24 pages × $0.21 ≈ $5.04
- Prototype regens / retries ≈ $0.30–$0.50

## Subject test (one sentence)

> The same obsessive mind that solved gravity in his thirties spent his sixties hunting counterfeiters through London taverns, ran the Royal Society like a kingdom, refused to publish the book that would humiliate his dead enemy, and outlived every rival who had ever crossed him.

If the script drifts away from *"obsession turned outward at the world,"* pull it back.

## Editorial spine

Book One was a discoverer's story. Book Two is the same man's life **after** discovery — power, prosecution, rivalry, private heresy. The interesting beat is that the same mind that solved gravity then turned its full force onto counterfeiters and rivals, and that in private the same man spent his nights on alchemy and prophecy. **Do not soften this into a "great old man" book.** The darker register is the editorial purpose.

The protagonist is not the ideas (*Opticks*, fluxions, the Mint reform). The protagonist is **the man, late in life, pressing on the world.**

## Key reminders

- This is the **biographical mode** book format established by Newton Vol 1, Honda, and da Vinci Vol 1: 3:2 landscape, oil-painting realism, in-image captions, full-width caption bands on T4–T5 pages, fixed circular side-arrow reader.
- **Reader who has never heard of Newton can follow on first read.** Captions carry the context. Bio.md framing rule (do not pitch by age, just do not assume prior knowledge).
- **Verbatim text from `04-SCRIPT.md` into the page prompts.** The script is the source of truth. Do not paraphrase at generation time.
- **Anchor on the artifact, not the body**, on the prosecution and breakdown pages. Newton's interrogation page (P8) shows ledger and depositions, not violence. The Tyburn page (P9) shows Newton reading the warrant; the gallows is distant in the window. The 1693 breakdown page (P2) shows spilled ink and unanswered letters in a candlelit study.
- **Quiz rule (Vol 2 from day one).** Tests WHY not WHAT. Correct answer not always longest, not always in the same position. Distractors substantive with period detail. Verify all five questions against this rule before shipping.
- **Voltaire** appears as a single named witness at the funeral — not a character. One margin caption only.

## Deliberate chronology departures

None significant. The book proceeds in date order from 1687 to 1727. The only soft compression is that the alchemy/Arian theology page (P20) is placed near the end, **after** all the public-life beats, even though Newton's alchemy and theology were continuous through his entire life. This is an editorial choice: the "private Newton" is the reveal that recontextualises everything before it, so it earns the late-book slot. Documented here so the choice is intentional.

## Curricular hook

The Lyceum currently has no exposed curriculum reference file (only `index.html`). **Default weighting** for Vol 2:
- Heavier on the **prosecution / Mint** beats and the **Leibniz priority war** (these are the human-drama spine).
- Medium on the **Opticks** annotated breakthrough (one strong page, P12, as Prototype 2).
- Lighter touch on the alchemy/heresy and South Sea pages (one page each).

If the kids are studying optics or color theory when Vol 2 ships, P12 carries the curricular weight. If they are studying money/economics, P5 (the Recoinage) and P21 (the Bubble) carry it.

## Cross-volume links

- **Book One** is the discoverer's volume (1642–1687, age 0–44). Captions in Book Two may reference Book One in passing (the apple, the prism in Cambridge, the *Principia* at the Royal Society) but should NEVER re-stage them.
- **Pythagoras Vol 1**, **Descartes**, and **Einstein** all live in the same nano shelf. The Newton ↔ Leibniz beat is the kind of "two minds, same idea, different fates" story that pairs with the *Salt and Stone* displacement theme — accidental thematic resonance, not engineered.

## Production order

Per `bio.md`:

1. ✅ Research dossier (`newton-vol2-research/source-dossier.md`)
2. Planning docs (00–04) — this brief, style guide, characters, settings, script
3. References (refs/) — gate before pages
4. Three prototype pages (Mint interrogation T4 / Opticks prism T5 / Closing finale T5) — gate before bulk
5. Bulk batch in parallel waves (cover + ~20 remaining pages)
6. Reader (index.html), quiz, landing card
7. Retrospective, memory update, commit + push
