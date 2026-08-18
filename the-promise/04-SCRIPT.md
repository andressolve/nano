# The Promise — section plan, image briefs, and exhibit map

The **final prose lives in `index.html`** (single source of truth — this file is
the blueprint, not a duplicate transcript). This document fixes the section
order, what each section must accomplish, which exhibit or image carries it, and
the exact wording of every fact box and pull quote.

Legend: **PLATE** = code-built exhibit (`tools/build_plates.py`, exact numerals).
**PAINT** = generated painted image (supporting, never load-bearing).

---

## COVER
Title: *The Promise* / subtitle: *How We Know Things That Can Never Be Wrong*
**PAINT `cover.png`** — a plain wooden writing surface at dusk, lamplight from
the left: a sheet of paper with a short geometric construction drawn on it, a
stylus, and beyond the pool of light, darkness. No face, no figure. The paper is
lit as though it matters more than the room. Warm parchment, lapis and ink.

---

# PART ONE — TWO WAYS OF KNOWING

## §1 · The Two Kinds of Knowing
**Job:** set the whole essay's contrast in one page, using something the reader
already believes without ever having examined it.

Sunrise: you know it because it always has. That is a pile of evidence, and a
pile of evidence is a bet — a magnificent bet, still a bet. Europeans knew every
swan was white; the knowledge was built the same way; then they reached
Australia. Then the turn: *some things you know differently.* Nobody checks
whether 2+2 might be 5 on a large enough pair of numbers.

**PAINT `image-ledger.png`** — a night-watchman's ledger on a sill, ruled columns
of dated entries for sunrise after sunrise, hundreds of lines, the earliest ink
faded; through the window behind it, the first grey of dawn. Evidence
accumulating and never finishing.

> **Pull quote:** "A pile of evidence, however enormous, is still a bet."

## §2 · Numbers That Refuse to Be Rectangles
**Job:** define prime *visually and exactly*, before any notation, so the rest of
the essay has a floor. Dots that can be arranged into a rectangle vs. dots that
can only ever be a line.

**PLATE `plate-01-rectangles.png`**

> **Fact box — Did you know?** Because primes cannot be broken down, everything
> else can be built up out of them, and in exactly one way. 12 is 2 × 2 × 3 and
> nothing else. This is why they are called the atoms of arithmetic.

## §3 · They Are Running Out
**Job:** make "the primes stop" a *reasonable* belief. If the reader does not
feel the pull of the wrong answer, the proof lands on nothing.

25 in the first hundred. 8 in the hundred before a million. They genuinely thin.
Note honestly that the thinning is untidy — the fifth hundred holds more than
the fourth.

**PLATE `plate-02-thinning.png`**

> **Pull quote:** "They get rarer the further you walk. Do they eventually stop?"

## §4 · You Cannot Check
**Job:** close the escape hatch. The list has no end to walk to; a computer that
verifies a trillion numbers has said nothing about the trillion-and-first. This
is the honest limit of evidence, and it is a wall, not a difficulty.

**PAINT `image-ledgers.png`** — the interior of an enormous archive: identical
ledgers on shelves receding into darkness in both directions, a single lamp on a
reading desk in the foreground illuminating one open volume. The shelves do not
end anywhere in frame.

> **Fact box — Did you know?** Computers have now checked far past a trillion.
> It proves nothing about the next number. A search that cannot finish cannot
> answer a question about *all* of them — not slowly, not ever.

## §5 · Five Cases Were Not Enough
**Job:** first of two demonstrations that checking fails *for the best people
alive*. Fermat, 1640, on 2^(2ⁿ)+1. Five cases, all prime. He said he believed
they all were — **and honestly admitted he could not prove it.** Ninety-odd
years later Euler cracked the sixth: 4,294,967,297 = 641 × 6,700,417. Euler
never said how he found 641.

**PLATE `plate-04-fermat.png`**

## §6 · The Formula That Worked Forty Times
**Job:** the same lesson, sharper and closer to the reader's hand — they can
check these themselves. n² + n + 41 gives a prime for n = 0 … 39. At n = 40 it
gives 1681 = 41 × 41. The formula is Euler's own; he knew better than to call it
a law.

**PLATE `plate-05-forty-one.png`**

> **Pull quote:** "Forty pieces of evidence, and the forty-first says no.
> Certain is not the same as right."

---

# PART TWO — THE MACHINE

## §7 · A Man in Alexandria
**Job:** place the proof historically while being scrupulously honest that we do
not know its author. Flourished c. 300 BC, Alexandria, Ptolemy I. Everything
biographical comes from Proclus, writing ~800 years later. The "no royal road"
line is his, and the identical story is told about Menaechmus and Alexander.
Some scholars think "Euclid" may have been a team, or a shared name.

Land the point: *the proof outlived its author so completely that we are no
longer sure he was one person — and the proof does not care.*

**PAINT `image-alexandria.png`** — a figure seen from behind and slightly above,
seated at a low table in a colonnade of pale stone, Mediterranean light, working
on a wax tablet with a compass beside it. **The face is not visible and must not
be.** Robes, sandals, scrolls in a rack. Quiet, ordinary, no grandeur.
*Caption states outright that no portrait of Euclid exists.*

> **Fact box — Did you know?** We have no idea what Euclid looked like. Every
> painting and statue of him ever made was invented by the artist. What survives
> is the reasoning.

## §8 · The Trick
**Job:** THE page. Walk the construction slowly enough that the reader owns it.

Hand me any finite list of primes. Multiply them all together. Add one. Now ask
what divides that new number: not the first prime on your list (remainder 1),
not the second, not any of them. So either the new number is itself prime, or it
has a prime factor — and that factor is not on your list. **Either way you now
have a prime your list did not contain.** Since this works on *any* list, no
list is ever complete.

Then the honest break: run it on 2·3·5·7·11·13 and you get 30,031, which is
**not** prime — it is 59 × 509. The construction does not promise a new prime.
It promises a new prime *factor*. 59 and 509 were not on the list either. The
machine still wins.

**PLATE `plate-03-euclid-machine.png`**

> **Pull quote:** "You now know something about numbers larger than anyone will
> ever write down. Nobody has seen them. Nobody ever will. And you know."

## §9 · What He Actually Said
**Job:** the adult page — reward the reader for having understood by showing them
that the famous version they will meet elsewhere is a modernisation.

Three corrections, all from `RESEARCH-NOTES.md`:
1. Euclid never wrote "infinite." Heath's translation: *"Prime numbers are more
   than any assigned multitude of prime numbers."* Greek mathematics avoided
   completed infinity; he phrased it finitely, and more carefully than we do.
2. It is not a proof by contradiction. Almost everyone says it is. Euclid's is
   direct: hand it a list, it builds you a new prime. (Hardy & Woodgold, 2009.)
3. He used three primes, not n, and a least common multiple, not a product.

> **Pull quote:** "He did not say the primes are infinite. He said something more
> careful: that they are more than any multitude you care to name."

---

# PART THREE — THE PRICE

## §10 · The Knowledge That Never Expires
**Job:** the payoff of the whole essay. Science's best claims are provisional by
design — Newton's gravitation was the most successful theory in history and
Einstein still corrected it. That is not a failure of science; it is how science
works, and it is why science can learn. Proof is the other bargain: IX.20 has not
been amended once in twenty-three centuries. Nothing found in the next twenty-three
can touch it.

**PAINT `image-survives.png`** — a ruined classical floor, weeds through cracked
marble, columns broken off; scratched into a surviving flagstone, still perfectly
legible, a simple geometric figure. Late afternoon light. The building failed; the
diagram did not.

> **Fact box — Did you know?** Newton's law of gravitation was replaced.
> Ptolemy's astronomy was replaced. Euclid IX.20 has never been corrected,
> because there is nothing in it that could turn out to be untrue.

## §11 · The Fence
**Job:** the cost. Proof buys certainty by demanding you grant the rules first.
It tells you what *follows from* what; it cannot tell you which rules the world
obeys.

The parallel postulate: for 2,000 years mathematicians tried to prove Euclid's
fifth from the other four, and every proof smuggled it back in. Lobachevsky
(published 1829–30) and Bolyai (1832) independently found you can *deny* it and
get a perfectly consistent geometry. Gauss had it first, privately, and never
published — and told the young Bolyai that praising the work would be praising
himself.

**Careful on the physics** (`RESEARCH-NOTES.md` §7): do NOT say Einstein used
their geometry. Correct framing: they proved consistent alternatives to Euclid
exist — geometry is a matter of axioms, not necessity — which made Riemann's
curved-space theory thinkable, and that is what physics eventually needed.

**PLATE `plate-06-parallels.png`** — three panels, same construction, three
surfaces: flat (exactly one parallel through the point), sphere (none), saddle
(many). Code-built.

> **Pull quote:** "Proof does not tell you what is true of the world. It tells
> you what follows from what."

## §12 · The Thing Gödel Found
**Job:** the last and hardest honesty. State it precisely; refuse the manglings.

1931, Vienna. Any consistent system of rules, listable by a definite procedure,
strong enough to do ordinary arithmetic, contains a statement it can neither
prove nor disprove. Not a gap someone will patch — a permanent feature.

**Must include the correction:** this is not "there are truths no one can ever
prove." Such a statement can be proved in a *stronger* system. And it is not
"nothing is certain" — consistency is an assumption *of* the theorem, and
Euclid's proof is untouched. Gödel found the edge of the method, not a hole in it.

**PAINT `image-vienna.png`** — a small university lecture room, winter light,
half a dozen empty wooden chairs, a blackboard with faint erased chalk, one
overcoat on a hook. Quiet, unremarkable, cold. No portrait, no crowd.

> **Fact box — Did you know?** Gödel did not show that mathematics is broken or
> uncertain. Some systems *are* complete — a weaker arithmetic, proved complete
> and decidable, exists. Strength is the hinge: the more a system can say, the
> more it must leave unsettled.

## §13 · The Promise
**Job:** close on possession, not awe.

Return to the sunrise. That is still a bet. But somewhere around 300 BC someone
in Alexandria wrote down half a page of reasoning, and if you followed §8 you now
hold the same thing they held — not a report of it, not a summary, the thing
itself. It has not aged. It cannot be taken back by a new instrument or a better
telescope. It is the oldest thing the reader owns that is still exactly as good
as the day it was made.

**PAINT `image-desk.png`** — a modern child's desk at night, homework light, a
pencil and an ordinary lined exercise book on which the six-row prime
construction has been worked out by hand, the last line circled. Same lamplit
warmth as the cover. Twenty-three centuries, same reasoning.

> **Pull quote:** "It is the oldest thing you own that is still exactly as good
> as the day it was made."

---

## Exhibit / image manifest

| # | Asset | Kind | Status |
|---|---|---|---|
| — | `cover.png` | PAINT | to generate |
| §1 | `image-ledger.png` | PAINT | to generate |
| §2 | `plate-01-rectangles.png` | PLATE | built |
| §3 | `plate-02-thinning.png` | PLATE | built |
| §4 | `image-ledgers.png` | PAINT | to generate |
| §5 | `plate-04-fermat.png` | PLATE | built |
| §6 | `plate-05-forty-one.png` | PLATE | built |
| §7 | `image-alexandria.png` | PAINT | to generate |
| §8 | `plate-03-euclid-machine.png` | PLATE | built |
| §9 | — (text only, deliberately) | — | — |
| §10 | `image-survives.png` | PAINT | to generate |
| §11 | `plate-06-parallels.png` | PLATE | to build |
| §12 | `image-vienna.png` | PAINT | to generate |
| §13 | `image-desk.png` | PAINT | to generate |

7 painted images, 6 plates. §9 carries no image on purpose — it is the page where
the reader is trusted with the text alone.

## WHY-quiz (5 questions, answers shuffled, distractors length-matched)

1. Why can't checking numbers one by one prove the primes never run out?
   → *because the list has no end, so the search can never finish* (**c**)
2. 2·3·5·7·11·13+1 = 30,031 = 59 × 509. Why doesn't this break Euclid's proof?
   → *the proof promises a new prime factor, not that the number itself is prime* (**a**)
3. Why does the essay call Fermat's mistake a good mistake to study?
   → *he checked five cases honestly and still turned out to be wrong* (**d**)
4. What does proof demand in exchange for certainty?
   → *that you agree on the starting rules first* (**b**)
5. What did Gödel actually show?
   → *a strong enough consistent system always leaves some statement unsettled* (**c**)

Incorrect-answer feedback must teach the distinction, not just say "no."
