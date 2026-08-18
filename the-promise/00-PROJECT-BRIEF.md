# The Promise — project brief

**Full title:** The Promise — How We Know Things That Can Never Be Wrong
**Folder:** `the-promise/`
**Format:** Text-led illustrated essay (`shock-of-florence` / `why-rome-won` lineage)
**Length:** 13 sections + cover + 5-question WHY-quiz

## What this is

The first volume on the shelf where **the hero is an idea, not a person.** Every
mathematics piece we have built so far is a biography of a mathematician —
Gauss, Kepler, Mendel. This one is about *proof itself*: what it is, what it
buys you, and what it costs.

The reader should finish owning one proof outright — Euclid's, that the primes
never run out — and understanding why that kind of owning is different from
every other kind of knowing they have.

## The spine

**Evidence can never finish. Proof can.**

Not "math is beautiful," not "Euclid was a genius." The essay is built on a
single honest contrast that runs from the first page to the last:

- You know the sun will rise tomorrow because it always has. That is a bet — an
  excellent bet, and still a bet.
- You know the primes never run out because of half a page of reasoning written
  around 300 BC. That is not a bet, and it will never become one.

## Why this subject earns a volume

The payload is an **argument you reason through**, not a thing you look at — so
it is text-led per the explainer-text-led calibration. Images support; they never
carry the argument. Every load-bearing numeral is code-built (`tools/build_plates.py`),
never drawn by an image model.

The essay is honest in three places where popular accounts are not, and those
three places are the best pages in it:

1. **The pattern breaks.** 2·3·5·7·11·13+1 = 30,031 = 59 × 509 — *not* prime.
   Nearly every retelling implies the construction yields a new prime. It yields
   a new prime **factor**. Showing the break makes the proof stronger and teaches
   the reader to distrust a pretty pattern.
2. **Euclid did not argue by contradiction**, did not say "infinite," and used
   three primes, not n. (Hardy & Woodgold 2009.)
3. **Gödel is stated precisely**, with the usual pop manglings explicitly refused.

See `research/RESEARCH-NOTES.md` for every source and every DO-NOT-CLAIM flag.

## The three-act shape

- **Part One — Two Ways of Knowing** (§1–6). Establishes the crisis honestly:
  primes thin out, so "they stop" is a *reasonable* thing to believe; you cannot
  check your way to an answer; and two of the greatest arithmeticians who ever
  lived were wrong doing exactly that (Fermat's F₅, Euler's n²+n+41).
- **Part Two — The Machine** (§7–9). Alexandria, the proof walked slowly enough
  that the reader gets it, then what Euclid *actually* wrote.
- **Part Three — The Price** (§10–13). Proof never expires; but it only works
  inside agreed rules (the parallel postulate); and even inside them it cannot
  reach everything (Gödel). Close on what the reader now owns.

## Register and palette

**Ink on paper.** The world of this essay is a working surface — parchment,
notebook, slate — not a cinematic scene. Painted images are quiet, warm,
lamplit, and few; the plates are crisp cream exhibits.

- Paper `#f3ecdd`, ink `#26221e`
- **Lapis `#2e5c8a` = holds / proven / prime**
- **Vermillion `#b4442e` = breaks / fails / composite**

That two-colour logic is not decoration — it does argument work, consistently,
on every plate. Reader accent: lapis `#2e5c8a` (distinct from every shipped
volume).

## Editorial discipline

- No fake quotations. The "no royal road" anecdote appears **only** as
  "Proclus, writing some eight centuries later, reports…" — and the essay notes
  the same story is told about someone else entirely.
- Euclid is drawn **faceless / turned away**, because we do not know who he was.
  The caption says so. That is the honest image and also the better one.
- No mysticism about infinity, no "mathematics is the language of God," no leap
  from Gödel to minds or computers.
- The reader is never told a thing is beautiful. They are shown it and left alone.
