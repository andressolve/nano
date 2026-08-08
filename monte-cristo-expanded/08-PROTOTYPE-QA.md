# The Count of Monte Cristo — Pages 12–18 Prototype QA

## Status

**Continuous portrait prototype completed and internally QA-passed on
2026-07-27.**

The accepted pages are:

1. [`pages/page-12.png`](pages/page-12.png)
2. [`pages/page-13.png`](pages/page-13.png)
3. [`pages/page-14.png`](pages/page-14.png)
4. [`pages/page-15.png`](pages/page-15.png)
5. [`pages/page-16.png`](pages/page-16.png)
6. [`pages/page-17.png`](pages/page-17.png)
7. [`pages/page-18.png`](pages/page-18.png)

All seven are finished, flattened 1024 × 1536 portrait images with integrated
story text.

## Production Path

- Built-in subscription-backed Codex image generation.
- No `OPENAI_API_KEY`, direct API, or separate API billing.
- Accepted first-edition character, object, setting, and page references were
  supplied to every generation.
- Page 14's first generation was rejected because the last panel placed
  Villefort's reply before Edmond's question in the visual reading order.
- The script blocking was corrected and the full page regenerated.
- No balloon, tail, face, panel, or text was patched after generation.

## Dimension Check

| Page | Width | Height | Format |
| ---: | ---: | ---: | --- |
| 12 | 1024 | 1536 | pass |
| 13 | 1024 | 1536 | pass |
| 14 | 1024 | 1536 | pass |
| 15 | 1024 | 1536 | pass |
| 16 | 1024 | 1536 | pass |
| 17 | 1024 | 1536 | pass |
| 18 | 1024 | 1536 | pass |

## Page-Level Audit

### Page 12 — Two Betrothals

- Prose field is stable, comfortable, and free of busy art.
- Villefort, Renée, and the Marquise remain distinct.
- Every balloon belongs to the correct speaker.
- No silent guest receives a tail.
- Noirtier is explicitly established as Villefort's father.
- The accusation enters through the final doorway with the correct page turn.

**Result:** pass.

### Page 13 — A Dying Captain's Word

- Edmond and Villefort remain visually continuous.
- Captain Leclère appears only as a silent memory.
- The duty chain is complete: Leclère → Bertrand → sealed letter.
- Edmond's final line makes honor, not politics, his motive.
- All seven balloons read in causal order.

**Result:** pass.

### Page 14 — Innocent

- Villefort tests political intent, opportunity, and the unsigned accusation.
- The sealed letter remains separate and intact.
- Villefort clearly states belief in Edmond.
- Regenerated final panel now places Edmond's question on the left before
  Villefort's answer on the right.
- The last line creates the correct addressee page turn.

**Result:** pass after full-page regeneration.

### Page 15 — Noirtier

- The name appears before the facial change.
- A–B–A dialogue in the dominant panel is correctly tiered and attributed.
- Villefort's still hand receives a silent panel.
- Edmond's trust occupies a separate reaction panel.
- The unanswered final question lands beside the blank detention order.

**Result:** pass.

### Page 16 — The Choice

- The true letter visibly burns.
- Edmond gives his word after the evidence is destroyed.
- The separate order is visibly signed after Edmond says he trusts Villefort.
- The final “Guard.” balloon belongs to Villefort; the guard remains silent.
- Edmond's “Monsieur?” is correctly attributed.

**Result:** pass.

### Page 17 — The Black Island

- Prose cleanly carries corridor, carriage, and harbor transition.
- The continuous-time strip repeats one Edmond rather than multiplying
  characters.
- Marseille recedes before Château d'If dominates the page.
- Only Edmond and the principal guard speak.
- The final gate provides a silent architectural consequence.

**Result:** pass.

### Page 18 — Prisoner Thirty-Four

- Clerk, jailer, and silent guard have distinct roles.
- Register classification is spoken rather than delegated to handwriting.
- Panel 2's A–B–A order is unambiguous.
- Panels 3–4 place Edmond left and the jailer right in spoken order.
- The door closes on Edmond's name and the final reply substitutes his number.

**Result:** pass.

## Mobile Readability

Every accepted page was downscaled to a 390 px-wide display equivalent and
inspected without zoom.

- Speech remained readable.
- The Page 12 and Page 17 prose fields remained readable.
- No text touched the crop, page edge, face, hand, letter, flame, register,
  key, or door.
- No balloon became ambiguous when the page was reduced.

**Result:** pass.

## Continuous Causal Audit

| Question | Answer supplied by the finished sequence |
| --- | --- |
| What future does Villefort want? | Marriage to Renée and entry into her restored royalist family's future. |
| Who is Noirtier? | Villefort's father and a Bonapartist name the Saint-Mérans fear. |
| Why is Noirtier dangerous to Villefort? | Villefort's royalist identity and advancement depend on separating himself from his father. |
| Why did Edmond stop at Elba? | He gave dying Captain Leclère his word. |
| Did Edmond read the letter? | No; he knew only the address needed for delivery. |
| Does Villefort believe Edmond is guilty? | No. He identifies the accusation as an unsigned trap and says he believes Edmond. |
| What changes at Noirtier's name? | Villefort's personal future becomes threatened; Edmond's conduct does not change. |
| What evidence does Villefort destroy? | The sealed letter to Noirtier. |
| What document does Villefort create? | A separate signed detention order. |
| Why do officials ignore Edmond's innocence? | They accept Villefort's order as the truth they are required to enforce. |
| How does Edmond become Thirty-four? | The clerk enters the classification, the jailer accepts it, and the prison door closes on the number. |

## Prototype Gate Result

The sequence demonstrates:

- dialogue-driven story rather than historical survey;
- prose used only for orientation and transit;
- one legible cause-and-effect chain across seven page turns;
- portrait compositions that retain wide cinematic panels;
- native integrated lettering at readable density;
- stable character, room, object, and palette continuity;
- page intelligence through hierarchy, repeated hands, paper, doors, distance,
  and visual consequence.

The prototype therefore passes the internal production gate. A reader response
may still identify refinements, but no known technical or causal blocker
remains before full expanded-edition scripting.
