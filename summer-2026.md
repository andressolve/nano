# Summer 2026 — Reading Project Journal & Backlog

A running log of the summer's reading material for Francisco (9) and Sebastian (7).
Part **journal** (dated entries — what we built, what the kids thought, what we learned)
and part **backlog** (the living idea list with status). Read top-to-bottom to catch up.

---

## Direction this summer

The kids are becoming more sophisticated, mature thinkers — the goal is to **keep that
evolution going**, not pitch down. (See the CRITICAL FRAMING RULE in CLAUDE.md: write so any
first-time reader can follow, never "for ages 7–10.")

Two proven formats carry most of the work:
- **Tech explainer** (Sky Duel, Scattergun register) — machines/systems, premium engineering plate.
- **Biographical graphic novel** (Newton, Gauss, da Vinci... register) — ideas through a life.

**The loose spine** connecting this summer's interests:
machines that move → machines that sense & decide → machines that think → life as information.
(tanks/missiles → autonomous turrets → AI/Jensen Huang → cells & genetics as code)

**Themes the catalog is missing that we want to hit this summer:**
- **Failure / resilience** — Tesla (died broke), Euler (went blind, kept working), Huang (near-bankruptcy years).
- **Ethics** — autonomous weapons is the ideal first place to pose "should a machine decide to kill?"
  to kids old enough to sit with a question that has no clean answer.
- **Women scientists** — catalog is almost all boys/men; genetics-via-Rosalind Franklin would help.
- **Living / modern subjects** — Jensen Huang would be the first; intellectual history is still being written.

---

## Backlog

Status key: `idea` → `planned` → `in-progress` → `shipped`

### Mil-tech explainers (kid-requested interest)
| Topic | Status | Notes |
|-------|--------|-------|
| Autonomous turrets / counter-drone guns | shipped | OPENER. "The Gun That Aims Itself." Engineering-only (no ethics thread, per user). New gritty military-tech register, distinct from Sky Duel. 14 pages + cover. Shipped 2026-06-22 (commit 259ac5a). |
| Tanks | shipped | "The Iron Triangle — How a Tank Does Three Impossible Things at Once." Mil-tech #2. Folder `iron-triangle/`. 14 pages + cover. Shipped 2026-06-22 (commit 137fb0d, pushed). User QA passed; kid-QA pending. |
| Missiles | greenlit | Guidance, propulsion, seekers — pairs with Sky Duel's heat-seeker/radar content. Mil-tech #2 candidate. |
| Rocket launchers | idea | MLRS/HIMARS-style — area fire vs. precision. |

### Biographical graphic novels
| Subject | Status | Notes |
|---------|--------|-------|
| Tesla | in-progress (QA-ready) | "Tesla — The Man Who Gave the World Its Power." Biographical graphic novel, resilience/generosity arc (gave away the royalty fortune, died broke, vision won). Folder `tesla/`. 18 pages + cover + reader + WHY-quiz + landing card. Production complete 2026-06-22, ZERO regens / ZERO safety rejections. Awaiting user QA before commit. |
| Euler | idea | Math lineage (Gauss, Newton, Pythagoras, Descartes). Blind-but-prolific = resilience. |
| Jensen Huang | idea | First living/modern subject. Frame around the near-bankruptcy years, not coronation. |

### Science explainers / hybrids
| Topic | Status | Notes |
|-------|--------|-------|
| The cell | idea | Tech-explainer frame ("the cell is a factory/city" cutaway). |
| Genetics | idea | Tell it through a person — Mendel (patience/method) or Rosalind Franklin (woman scientist + credit/injustice arc). |

---

## Journal

### 2026-06-22 — Summer kickoff
- Reviewed the inspiration list with Andres: mil-tech (tanks, missiles, rocket launchers, autonomous
  turrets), basic bio/cells, genetics, and bios of Euler, Jensen Huang, Tesla.
- Agreed the list maps onto the two proven formats + one new decision (how to frame cells/genetics).
- Identified the through-line spine and the missing themes (resilience, ethics, women scientists, living subjects).
- **Decision: start with mil-tech.** First explainer TBD (leaning autonomous turrets as the opener — richest bridge to the AI thread).
- **Decision: keep this journal/backlog as the project-of-record** (one file, both purposes).

### 2026-06-22 — Mil-tech opener chosen & scoped
- **Topic: autonomous turrets / counter-drone guns.** Title: "The Gun That Aims Itself — How Machines Learned to Shoot Down Drones." Tech-explainer format (Sky Duel/Scattergun lineage).
- **Decision: engineering-only.** No ethics/autonomy thread this volume (user chose pure how-it-works). The "machines that decide" moral question is deferred — likely better placed in the AI/Jensen Huang piece later.
- **Decision: NEW gritty military-tech register**, deliberately distinct from Sky Duel's glossy aerospace look (desaturated modern-battlefield palette, harsher contrast, field-photo framing).
- **Safety framing:** the target is always a *drone (a machine)*, never a person — keeps it clean for the image filter and age-honest.
- 14-page engineering spine locked (hook → problem → why humans can't → sensing → recognizing → tracking → the shot → jamming → other counters → not-new history → full kill chain → re-read → where it's going). 4 POSTER + 10 cinematic, frame device P1↔P13.
- Next: source facts (Ukraine counter-drone, Phalanx, FPV specs) before writing planning docs.

### 2026-06-22 — "The Gun That Aims Itself" production complete (QA-ready, not yet committed)
- Ran the full pipeline autonomously: research-sourced facts (`research/RESEARCH-NOTES.md`), 5 planning docs,
  4 refs (turret/FPV/Shahed/Lena) + 1 PIL composite plate, 3 prototypes (P4 radar POSTER, P1 cinematic hook, P12 kill-chain POSTER), then 11 bulk pages + cover.
- **New gritty military-tech register validated** — desaturated gunmetal/olive/concrete, single hot accent (muzzle-orange / phosphor-green), painted photographic realism, dark schematic POSTER plates. Holds consistently across cinematic + dense-text pages; clearly distinct from Sky Duel's glossy look.
- **One safety-filter snag:** P7 (the lead/aim diagram) was rejected twice by output moderation even after softening — a full page about weapon-aiming reads as instructions. Fixed by reframing the whole page as **"STEP TWO — PREDICT THE PATH"** (pure motion-prediction, no aim/bullet/crosshair/target words). Lesson logged. All other 14 images + 4 refs + composite passed single-shot.
- **Reader built** (`aim-itself/index.html`): dark flipper cloned from Scattergun, **phosphor-green `#5fb86a`** accent, sans-serif (not Palatino), plus a persistent **KILL-CHAIN footer strip** (Detect · Identify · Track · Aim · Fire) that lights the active step per page. 5-question WHY-quiz per the CRITICAL QUIZ RULE (length-matched distractors, shuffled answers b/d/a/c/b): cost asymmetry, machine-beats-guard, sensor fusion, predict-the-path, why the gun came back. End interstitial "THE RACE HAS ONLY BEGUN."
- Landing card + footer folder-list entry added to root `index.html`.
- **Cost ≈ $4.40** (21 calls incl. 2 failed P7 attempts) — a touch over the $3.5–4 envelope, the P7 retries drove it.
- **Status:** ✅ Shipped 2026-06-22 (commit 259ac5a, pushed). Backlog row flipped to `shipped`.

### 2026-06-22 — Kid-QA PASSED
- **"kids LOVED it. great job!"** — Francisco + Sebastian read the finished book; clear win.
- This is the 3rd tech explainer to pass with the kids (Sky Duel → Scattergun → this), so the tech-explainer
  format is firmly validated as a recurring medium. **Mil-tech #2 (tanks or missiles) is greenlit** whenever
  Andres wants to pick it up — no STOP gate needed, just choose the topic.
- The new gritty military-tech register is now a proven second tech-explainer look (alongside Sky Duel's glossy one).

### 2026-06-22 — Mil-tech #2 chosen, scoped & produced: "The Iron Triangle" (QA-ready)
- **Topic: how a main battle tank works.** Title: "The Iron Triangle — How a Tank Does Three Impossible Things
  at Once." Tech-explainer format, **reusing the gritty military-tech register** from the turret book (so the
  two sit together on the shelf), with a new **amber `#d98a3d`** reader accent (turret was phosphor-green).
- **Organizing idea: the iron triangle.** Firepower / Protection / Mobility, three demands that fight each
  other — you can never max all three; every tank is a compromise. The whole book hangs the gun/armor/engine
  chapters off the triangle, then shows the arms race that keeps redrawing it.
- **Series tie-in:** P8 (active protection) and P14 (cheap FPV drones diving on the tank's thin roof) bring
  back the cost-asymmetry + counter-drone shield from "The Gun That Aims Itself" — the two books snap together.
- 14-page spine: hook → three impossible jobs → POSTER triangle → the gun → POSTER dart-vs-jet → fire control
  → POSTER armor → arms race (ERA→APS) → mobility → crew of four → not-new (Somme 1916) → POSTER cutaway →
  re-read → drones-vs-tanks. 4 POSTER + 10 cinematic, frame device P1↔P13.
- **Cleanest run to date: ZERO regens, ZERO safety rejections** across cover + 14 pages + 3 refs + 1 PIL
  composite. Research-sourced facts first (`research/RESEARCH-NOTES.md`), 5 planning docs, 3 refs (generic
  MBT "Bastion", commander "Marko", WWI Mark-I), composite plate, 3 prototypes (P3/P1/P12), then 12 bulk
  images in two parallel waves. Generic-hardware rule (no real models/flags/insignia) held throughout.
  Est. cost ≈ **$3.80** (~18 image calls), at the low end of the envelope.
- **Reader built** (`iron-triangle/index.html`): dark flipper cloned from the turret book, amber accent,
  IRON-TRIANGLE footer strip (Firepower · Protection · Mobility) that lights the corner each page is about.
  5-question WHY-quiz per the CRITICAL QUIZ RULE (length-matched distractors, answers shuffled c/a/d/b/c):
  why a tank is always a compromise, why armor is sloped, why the gun needs a leading computer, why tracks
  over wheels, why a cheap drone threatens a tank. End interstitial "THE RACE GOES ON."
- Landing card + footer folder-list entry added to root `index.html`.
- **Status: ✅ Shipped 2026-06-22 (commit 137fb0d, pushed).** User QA passed ("great stuff. well done."); committed+pushed on user request. Backlog row flipped to `shipped`. **Kid-QA (Francisco + Sebastian) still pending** before mil-tech #3 (missiles is the obvious greenlit candidate).

### 2026-06-22 — First summer BIOGRAPHY chosen & scoped: "Tesla"
- User asked for another graphic book, picked **Tesla** from 4 options (over Missiles / Jensen Huang / Rosalind Franklin). First biographical graphic novel of the summer; switches from tech-explainer format to the oil-painting bio register (Newton/Gauss/da Vinci lineage).
- **Title: "Tesla — The Man Who Gave the World Its Power."** Double meaning: electrical power + the fortune/power he gave away.
- **Spine = generosity/resilience/failure-then-vindication** (NOT a parade of inventions): gave the world AC, tore up the royalty contract that could have made him one of the richest men alive, over-reached on wireless power and lost everything, died broke feeding pigeons — but the future he worked for arrived. Moral hinge = P10 torn contract. Technical scaffolding (what AC is) concentrated in one P5–P6 block to avoid Einstein's intellectual-spine failure.
- **Structure:** 1943 Hotel-New-Yorker frame (P1 open / P17 close); chronological body; montage finale (P18) carries the lasting vindication (the world AC built + the SI unit "tesla", 1960). 18 pages + cover.
- **Research done first** (`tesla/research/RESEARCH-NOTES.md`, web-verified, skeptical). Key myths deliberately avoided: NO Topsy the elephant in the War of Currents; NOT "Supreme Court declared Tesla invented radio"; torn-contract framing kept conditional ("could have made him"); no internet fake quotes; staged Colorado photo labeled as a trick; lightning "over 100 feet"; height ~6'2".
- 5 planning docs written. No composite ref needed (every multi-char page is 2 people → Strategy 1). 12 refs planned (3 Tesla age phases + childhood cast + 3 industrialists + pigeon/tower/coil objects). Next: refs → 3 prototypes (P5 epiphany, P6 AC explainer, P18 montage) → bulk batch.

### 2026-06-22 — "Tesla" production complete (QA-ready, not yet committed)
- Ran the full pipeline autonomously: 12 refs (all on-model, single-shot) → 3 prototypes (P5 Budapest epiphany / P6 AC annotated diagram / P18 montage finale, all single-shot) → cover + remaining 15 pages in two parallel waves.
- **Cleanest possible run: ZERO regens, ZERO safety rejections across all 19 images + 12 refs.** Matches the Iron Triangle and Gauss-vol2 standard. The bio-mode template (oil-painting register + locked refs + six-block prompt + prototype-then-bulk) held perfectly on the Tesla material.
- **Oil-painting register validated again:** Gilded-Age sepia/gunmetal pierced by cold electric blue-white as the single hot accent. The deliberate *absence* of blue in the late hotel pages (P1, P15–P17) landed as designed — grey city + warm lamp only, the arc-light of his life gone. The torn-"CONTRACT" moral hinge (P10) read clean and central; the P15 "DEATH RAY" newspaper headline rendered legibly and ties to its caption; all quote artifacts (Faust P5, pigeon P16, 1927 future-quote P17) rendered correctly in period serif.
- **Editorial honesty held** per research flags: torn-contract kept conditional ("could have made him"), Colorado photo labeled a double-exposure trick, "by Tesla's account" on the Edison $50k story, lightning "over a hundred feet."
- **Reader built** (`tesla/index.html`): dark Palatino flipper cloned from Gauss-vol2, **electric-blue `#4db8ff`** accent. 5-question WHY-quiz per the CRITICAL QUIZ RULE (length-matched distractors, answers shuffled b/a/c/c/b): the AC no-brushes insight, why AC won the current war, why he tore up the contract, why free wireless power couldn't be sold, why the future proved him right. End interstitial "THE LIGHTS OF THE WORLD ARE HIS MONUMENT."
- Landing card + footer folder-list entry added to root `index.html`.
- Est. cost ≈ **$6.50** (~31 image calls, all single-shot), in line with the bio envelope.
- **Status: QA-ready, NOT committed.** Awaiting user QA pass before commit/push. Kid-QA pending after that.
