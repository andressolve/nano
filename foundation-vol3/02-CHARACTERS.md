# Characters — Foundation: Book Three — The Merchants

Rules in force (Vol 1–2 QA lessons, user directives):
1. **Any character on 2+ pages gets a reference image.** Prose locks only for true one-page walk-ons.
2. **There is no "anonymous" in a recurring room** — design unnamed extras out of recurring scenes or give them refs.
3. **Whole-page anchors preserve sets, not faces** — crop validated group pixels when reusing an ensemble.
4. **Distinct recurring characters need distinct COSTUMES, not just faces.** Prompts state: "REFERENCE X and REFERENCE Y are TWO DIFFERENT characters who must never be merged."
5. Never put the famous name inside a prompt's lock block — the visual description is the lock.

## Cast audit (page-by-page)

| Character | Pages | Count | Lock type |
|---|---|---|---|
| Mallow | P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P15 | 11 | REF (solo, new face) |
| Sutt | P4, P10, P11, P12 | 4 | REF (Terminus group sheet) |
| Twer | P4, P5, P11 | 3 | REF (Terminus group sheet) |
| Commdor Asper Argo | P6, P7, P15 | 3 | REF (Korell group sheet) |
| Commdora Licia | P6, P14 | 2 | REF (Korell group sheet) |
| Ponyets | P2, P3 | 2 | REF (prologue group sheet) |
| Pherl | P2, P3 | 2 | REF (prologue group sheet) |
| Seldon hologram | P1 (flashback) | 1 | REF (reuse `../foundation/refs/ref_seldon_hologram.png`) |
| Onum Barr | P8 | 1 | prose lock |
| Imperial tech-man | P9 | 1 | prose lock |
| Publis Manlio | P12 | 1 | prose lock |
| Eskel Gorov | P2 (cell) | 1 | prose lock (background figure) |
| Jord Parma ("missionary") | P5 | 1 | prose lock |

## Costume matrix (rule 4 — all recurring cast instantly tellable apart)

| Character | Costume | Hair/face key |
|---|---|---|
| Mallow | COPPER-BROWN trader jacket over metal-mesh shirt, broad belt, steel wristband | ~45, black cropped hair, trim black beard, heavy brows |
| Sutt | SLATE-BLUE bureaucrat tunic, high stiff collar | ~50, thin pale face, receding sandy hair, cold eyes |
| Twer | rumpled TAN trader coat | ~55, stocky, round florid face, bushy grey side-whiskers |
| Commdor Asper | plain DOVE-GREY high-collar coat, single gold chain of office | ~60, stooped thin, sparse white hair, ingratiating smile |
| Commdora Licia | WINE-PURPLE imperial-style gown, jewels | ~40, sharp handsome face, dark hair coiled high |
| Ponyets | DENIM-BLUE work coverall | ~35, short ginger hair, freckled, quick-eyed |
| Pherl | SAFFRON-AND-WHITE layered Elder robes, gold sun medallion | ~50, shaved head, bronze skin, smooth guarded face |

## Locks

### HOBER MALLOW, Master Trader (carries the volume)

**Ref:** `refs/ref_mallow.png` — new face, solo generation.

**Lock (paste verbatim):**
> Powerfully built man of about forty-five, broad shoulders, black hair cropped short, trim black beard, heavy dark brows, shrewd unimpressed dark eyes, weathered olive skin; copper-brown spacer's trade jacket over a fine metal-mesh shirt, broad utility belt, a plain steel band on his left wrist. Confident, physical, amused — a man who owns every room he walks into and has paid for none of them.

### JORANE SUTT (the Mayor's secretary, the schemer)

**Lock:**
> Thin precise man of about fifty, pale indoor face, receding sandy hair combed flat, long nose, cold measuring eyes; slate-blue bureaucrat's tunic buttoned to a high stiff collar. Steepled fingers, never raises his voice.

### JAIM TWER (the planted "friend")

**Lock:**
> Stocky man in his mid-fifties, round florid face, bushy grey side-whiskers, anxious eager eyes; rumpled tan trader's coat worn open. Talks with his hands, laughs a little too quickly.

### COMMDOR ASPER ARGO, "the Well-Beloved" (ruler of Korell)

**Lock:**
> Thin stooped man of about sixty, sparse white hair, hollow cheeks, a practiced humble smile that never reaches his sharp little eyes; plain dove-grey coat with a high collar, its only ornament a single gold chain of office. Poverty worn as a costume.

### COMMDORA LICIA (his wife, a viceroy's daughter)

**Lock:**
> Handsome sharp-faced woman of about forty, dark hair coiled high in imperial court fashion, imperious arched brows; rich wine-purple gown with jeweled collar and rings — deliberately, defiantly overdressed for her drab world. Contempt held just behind courtesy.

### LIMMAR PONYETS (prologue trader)

**Lock:**
> Wiry quick-eyed trader of about thirty-five, short ginger hair, freckled weathered face, crooked practical grin; denim-blue spacer's work coverall with tool pockets and belt, sleeves pushed up. (Ref rendered the coverall denim-blue; lock updated to match the ref — ref is truth.)

### PHERL (prologue, Askonian councilor)

**Lock:**
> Smooth guarded man of about fifty, shaved head, bronze skin, watchful hooded eyes; layered saffron-and-white robes of a planetary Elder, a gold sun-disk medallion on his chest. Ambition dressed as piety.

### SELDON HOLOGRAM (P1 flashback only)

Reuse `../foundation/refs/ref_seldon_hologram.png` unchanged (elderly man, wheelchair, closed book, luminous pale blue-white, only light source).

## Prose locks (one-page walk-ons)

- **ONUM BARR (P8):** gaunt old man near eighty, long white hair and short white beard, deep-lined proud face; threadbare once-fine dark patrician robe with faded silver edging. Dignity in ruin.
- **IMPERIAL TECH-MAN (P9):** fat self-important man of about fifty, oiled black hair, soft hands heavy with rings; gunmetal-grey technician's uniform with a polished SPACESHIP-AND-SUN badge and a jeweled collar of rank.
- **PUBLIS MANLIO (P12):** elderly silver-haired priest-politician, thin austere face; magnificent crimson-and-gold robes of the Foundation's own church (same costume family as Vol 2's Verisof — deliberately: the church side of the old guard).
- **ESKEL GOROV (P2, background):** lean grey-bearded prisoner in plain dark spacer clothes, seen through a cell's light-barrier.
- **JORD PARMA (P5):** wild-eyed man in torn RED priest's robes, shaved scalp, theatrical bandage on one arm; nothing visibly wrong beneath it. (His KSP wrist tattoo is INVISIBLE on P5 — it exists only in the P11 ultraviolet freeze-frame.)

## Ref production plan (Vol 2 group-sheet technique, validated)

1. `refs/ref_mallow.png` — solo `generate_image`, 3:2 landscape: portrait head-and-shoulders LEFT + full-length standing RIGHT, neutral warm background, no text.
2. `refs/ref_group_terminus.png` — **single `generate_image` call, 3:2**: TWO figures in a row, full-length, large clear faces, thin labels A/B beneath: [Sutt lock] · [Twer lock].
3. `refs/ref_group_korell.png` — **single call**: TWO figures, labels A/B: [Commdor Asper lock] · [Commdora Licia lock].
4. `refs/ref_group_traders.png` — **single call**: TWO figures, labels A/B: [Ponyets lock] · [Pherl lock].
5. Review gate: every face checked against its lock (age, costume, distinctness) BEFORE any page. If any single face fails, regenerate the whole sheet or fall back to a solo ref for the failed character.
6. Per page, pass `imagePaths: [ref_mallow, ref_group_korell, ...]` as needed. Every multi-ref prompt must include: "These inputs are REFERENCE SHEETS, not layouts to keep — paint ONE NEW unified single-scene image using the references; ignore any printed labels. The referenced people are DIFFERENT characters and must never be merged."
