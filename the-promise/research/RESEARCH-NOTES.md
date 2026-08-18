# The Promise — research notes and editorial honesty flags

Web-verified 2026-08-17. Every claim in the essay traces to this file. The
**DO NOT CLAIM** items are the traps; popular retellings of this exact subject
fall into all of them.

---

## 1. Euclid, *Elements* Book IX, Proposition 20

**Exact wording (Heath, Dover 1956):**
> "Prime numbers are more than any assigned multitude of prime numbers."

- Euclid **never wrote "infinitely many."** Greek mathematics worked with the
  *potential* infinite (Aristotle's distinction), and the proposition is
  deliberately phrased finitely: for any given multitude, there are more.
- **DO NOT CLAIM:** that Euclid proved "the set of primes is infinite." That is
  our sentence, not his. Safe framing: *"He did not say the primes are infinite.
  He said something more careful."* — this is a genuine beat in the essay, not a
  footnote.

## 2. It is NOT a proof by contradiction

The single most common error in popular accounts.

- **Source of the correction:** Michael Hardy & Catherine Woodgold, *"Prime
  Simplicity,"* The Mathematical Intelligencer 31 (2009), 44–52. Follow-up:
  Hardy, *"Three Thoughts on 'Prime Simplicity,'"* Math. Intelligencer 35 (2013).
- Euclid's argument is **direct and constructive**: given any finite set of
  primes, it *produces* a prime not in that set. There is no opening "suppose
  there are only finitely many."
- **Nuance (keep honest):** there IS a small local reductio *inside* one branch —
  the new prime G cannot equal A, B or C, else G would measure the unit, "which
  is absurd." So: a contradiction step nested in a constructive proof, not a
  reductio on the theorem.
- **Euclid used THREE primes** (A, B, C), and formed the **least number measured
  by them** (an LCM) plus the unit — *not* `p₁·p₂·…·pₙ + 1`. There is no "n" in
  Euclid.
- **DO NOT CLAIM:** "Euclid assumed there were finitely many primes and derived a
  contradiction."
- Consequence for our plates: `plate-03` shows the **modern** form and its footer
  says so explicitly.

## 3. Euclid the person — almost nothing is known

- Essentially all biography comes from **Proclus (c. 410–485 AD)**, writing
  **~750–800 years later**. Correct form: **"flourished c. 300 BC,"** Alexandria,
  under **Ptolemy I Soter** (r. 323–285 BC).
- **"No royal road to geometry"**: Proclus only, no contemporary corroboration;
  **Stobaeus tells the identical story about Menaechmus and Alexander** — a
  migratory anecdote. **DO NOT CLAIM as fact.** Hedge: *"Proclus, writing some
  eight centuries later, reports…"*
- Jean Itard's three hypotheses: a real individual; the leader of an Alexandrian
  team; or a **collective pen name** (the "Bourbaki" hypothesis).
- **DO NOT CLAIM** firm birth/death dates. MacTutor's "325–265 BC" is a
  conventional guess, not evidence.
- *Essay use:* this is a feature. The proof outlived the biography of its author
  so completely that we are not certain he was one person.

## 4. Fermat and F₅

- **1640**, in correspondence with **Frénicle de Bessy** and **Mersenne**. Checked
  n = 0–4: 3, 5, 17, 257, 65537.
- **He explicitly admitted he had no proof**, and conceded the same again ~18
  years later. **This strengthens the essay** — he was honest; the point is that
  even honest, world-class case-checking is not knowledge.
- **Euler, 1732** (paper E26, presented St. Petersburg 1732, published 1738):
  F₅ = 2³² + 1 = **4,294,967,297 = 641 × 6,700,417**. 1640 → 1732 ≈ **92 years**
  ("ninety-odd" is safe).
- **DO NOT CLAIM** that Euler used his divisor theorem in 1732 — he did not say
  how he found 641. The theorem (every divisor of Fₙ, n ≥ 2, has the form
  k·2ⁿ⁺¹ + 1) came ~15 years later in **E134** (Novi Commentarii 1, 1747/48, pub.
  1750). Safe hedge: *"he never said how."*

## 5. n² + n + 41

- Verified locally: prime for **n = 0 … 39** (41 through 1601); fails at
  **n = 40 → 1681 = 41 × 41**.
- The formula is **Euler's**; he did not claim it was a law.

## 6. Gödel, 1931 — precise statement

> Any **consistent**, **effectively axiomatized** formal system **strong enough to
> represent a modest fragment of arithmetic** is incomplete: there is a sentence
> in its language it can neither prove nor refute.

- Gödel's own 1931 proof assumed **ω-consistency**; **Rosser (1936)** weakened it
  to plain consistency.
- **DO NOT CLAIM (standard manglings):**
  - "There are true statements that can never be proved." — unprovable *in that
    system*; provable in stronger ones.
  - "No system can be complete." False: **Presburger arithmetic** is consistent,
    complete and decidable. *Strength is the hinge.*
  - "Gödel showed mathematics is uncertain / inconsistent / arbitrary."
    Consistency is a *hypothesis* of the theorem.
  - Any leap to minds, computers, physics, or "nothing can be known."
  - Don't conflate the first theorem with the second (a system cannot prove its
    own consistency).

## 7. Parallel postulate → non-Euclidean geometry → Einstein

- ~2,000 years of failed attempts to derive Postulate 5 (Proclus, Ibn al-Haytham,
  Khayyam, Saccheri 1733, Lambert, Legendre).
- **Lobachevsky:** presented Kazan 1826, published **1829–30**. **János Bolyai:**
  the *Appendix* to his father's *Tentamen*, **1832**. Independent.
- **Gauss** had it privately earlier but **never published** — no priority claim.
  On reading Bolyai's Appendix he said praising it would be praising himself,
  which devastated János. (Ties to our own `gauss-vol2/`.)
- **DO NOT CLAIM** Einstein used Bolyai's or Lobachevsky's hyperbolic geometry.
  The actual tool is **Riemannian / Lorentzian** geometry — Riemann's 1854
  habilitation lecture (pub. 1868), tensor calculus via Ricci-Curbastro and
  Levi-Civita (1900), brought to Einstein by **Marcel Grossmann** from 1912;
  field equations **November 1915**.
- **SAFE framing:** Bolyai/Lobachevsky/Gauss established that *consistent
  alternatives to Euclid exist* — that geometry is a matter of axioms, not of
  necessity — which made Riemann's theory of curved space thinkable, and that is
  what physics eventually needed.

## 8. Arithmetic verified locally (`tools/build_plates.py`)

| Claim | Verified |
|---|---|
| 2·3·5·7·11·13 + 1 = 30,031 = **59 × 509** (composite) | yes |
| Products+1 for the first five prime lists (3, 7, 31, 211, 2311) are prime | yes |
| F₅ = 4,294,967,297 = 641 × 6,700,417 | yes |
| n²+n+41 prime for n=0..39, 1681 = 41² at n=40 | yes |
| Primes per hundred to 1000: 25, 21, 16, 16, 17, 14, 16, 14, 15, 14 | yes |
| Primes in 999,901–1,000,000: **8** | yes |

Note the thinning is **not monotonic** (the fifth hundred holds 17, more than the
16 before it) — stated on the plate rather than hidden.
