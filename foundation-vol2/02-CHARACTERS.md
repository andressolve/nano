# Characters — Foundation: Book Two — The Priests

Rules in force (Vol 1 QA lessons, user directives 2026-07-05):
1. **Any character on 2+ pages gets a reference image.** Prose locks only for true one-page walk-ons.
2. **There is no "anonymous" in a recurring room** — design unnamed extras out of recurring scenes or give them refs.
3. **Whole-page anchors preserve sets, not faces** — crop validated group pixels when reusing an ensemble.
4. **Distinct recurring characters need distinct COSTUMES, not just faces.** Prompts state: "REFERENCE X and REFERENCE Y are TWO DIFFERENT characters who must never be merged."
5. Never put the famous name inside a prompt's lock block — the visual description is the lock.

## Cast audit (page-by-page)

| Character | Pages | Count | Lock type |
|---|---|---|---|
| Hardin (62) | P1, P2, P3, P4, P6, P8, P9, P12, P13, P14, P15 | 11 | REF (aged from Vol 1) |
| Sermak | P2, P4, P14 | 3 | REF (Terminus group sheet) |
| Verisof | P3, P11, P14 | 3 | REF (Terminus group sheet) |
| Wienis | P5, P8, P9, P12, P13 | 5 | REF (Anacreon group sheet) |
| Lepold | P5, P8, P14 | 3 | REF (Anacreon group sheet) |
| Aporat | P7, P10 | 2 | REF (Anacreon group sheet) |
| Lefkin | P7, P10, P12 (screen) | 3 | REF (Anacreon group sheet) |
| Seldon hologram | P15 | 1 | REF (reuse `../foundation/refs/ref_seldon_hologram.png`) |
| Yohan Lee (older) | P6 | 1 | prose lock (single page) |
| Sermak's delegation | P2 background | 1 | unnamed background, never recur |

## Costume matrix (rule 4 — all eight must be instantly tellable apart)

| Character | Costume | Hair/face key |
|---|---|---|
| Hardin | plain charcoal statesman's coat, open collar, NO ornament | iron-grey short hair, wry half-smile |
| Sermak | sharp pale-grey civic suit, high collar | young, dark hair, jutting chin |
| Verisof | CRIMSON priest robes, gold Spirit sigil | round genial face, greying temples |
| Aporat | WHITE priest robes, gold trim | gaunt, black pointed beard |
| Wienis | dark GREEN-and-gold regent uniform, sash | heavy, jowled, balding grey |
| Lepold | white-and-silver royal dress | slight fair teenager, 16 |
| Lefkin | NAVY admiral uniform, gold epaulettes | lean, dark waxed mustache |
| Lee | plain dark brown workman's coat | compact, white close-crop |

## Locks

### SALVOR HARDIN, age 62 (carries the volume)

**Ref:** `refs/ref_hardin_old.png` — **build via `edit_image` anchored on `../foundation/refs/ref_hardin.png`**: "the same man aged thirty years." NEVER a fresh unrelated face — cross-volume continuity is the point.

**Lock (paste verbatim):**
> Man of about sixty, iron-grey hair cut short and practical, strong lined jaw, alert grey eyes, deep smile-creases, the same wry confident half-smile; plain charcoal statesman's coat over an open-collared shirt — frontier practicality grown into quiet authority, no ornament, no uniform.

### SEF SERMAK (Action Party leader)

**Lock:**
> Young politician around thirty, thick dark hair swept back, jutting chin, burning impatient dark eyes, sharp pale-grey civic suit with a high collar; leans forward when he talks, a fist on the table.

### POLY VERISOF (ambassador & High Priest)

**Lock:**
> Man in his fifties, round genial well-fed face, shrewd amused eyes, greying temples, clean-shaven; magnificent crimson high-priest robes with a gold spiral sigil on the chest. A politician's warmth wearing a prophet's costume.

### PRINCE REGENT WIENIS

**Lock:**
> Heavy powerful man in his sixties, jowled face, balding grey hair, small hard ambitious eyes, thick neck; dark green-and-gold royal uniform with a broad gold sash and jeweled orders. Radiates blunt appetite for power.

### KING LEPOLD I, age 16

**Lock:**
> Slight fair-haired boy of sixteen, smooth uncertain face trying to look regal, pale blue eyes, slender build; white-and-silver royal dress uniform. A child wearing a kingdom.
> Realistic teenage anatomy, NOT cute, NOT mascot proportions.

### THEO APORAT (priest of the flagship)

**Lock:**
> Gaunt intense priest around forty, hollow cheeks, black pointed beard, deep-set burning dark eyes; plain WHITE priest robes with narrow gold trim (deliberately simpler and whiter than the High Priest's crimson). Righteous, fearless.

### ADMIRAL PRINCE LEFKIN (Wienis's son)

**Lock:**
> Lean arrogant officer around thirty-five, dark waxed mustache, his father's small hard eyes in a narrower face; navy-blue admiral's uniform with gold epaulettes and braid.

### SELDON HOLOGRAM (P15)

Reuse `../foundation/refs/ref_seldon_hologram.png` unchanged (elderly man, wheelchair, closed book, luminous pale blue-white, only light source).

### YOHAN LEE, older (P6 only — prose lock)

> Compact hard-faced man around seventy, white close-cropped hair, watchful narrow eyes, plain dark brown workman's coat; stands slightly behind the Mayor, arms folded. (Continuity: the same man as Vol 1's Yohan Lee, aged thirty years.)

## Ref production plan — the GROUP-SHEET EXPERIMENT

User directive (2026-07-05): try **one group ref sheet generated in a SINGLE call** — "we don't need the same guy 5 different angles, more important to have all guys in one spot." Faces must stay large; ≤4–5 entities per sheet.

1. `refs/ref_hardin_old.png` — `edit_image` on Vol 1 `ref_hardin.png`, aged 30 years (NOT part of any group generation; continuity with Vol 1 overrides the experiment for him).
2. `refs/ref_group_anacreon.png` — **single `generate_image` call, 3:2 landscape**: four figures standing in a row against a neutral warm background, each full-length with large clear face, thin name-free labels A/B/C/D beneath: [Wienis lock] · [Lepold lock] · [Lefkin lock] · [Aporat lock]. One coherent light source and scale — this is the experiment's test case.
3. `refs/ref_group_terminus.png` — **single `generate_image` call**: two figures, [Sermak lock] · [Verisof lock], same treatment.
4. Review gate: every face checked against its lock (age, costume, distinctness) BEFORE any page. If any single face fails, regenerate the whole sheet or fall back to solo refs for the failed character.
5. Per page, pass `imagePaths: [ref_hardin_old, ref_group_anacreon, ...]` as needed (multi-ref). If multi-ref is unavailable at production time, PIL-crop individuals from the group sheets into Vol 1-style composite plates (method A).

Every multi-ref prompt must include: "These inputs are REFERENCE SHEETS, not layouts to keep — paint ONE NEW unified single-scene image using the references; ignore any printed labels. The referenced people are DIFFERENT characters and must never be merged."
