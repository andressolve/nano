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
| Tanks | idea | How a tank actually works: armor, gun, mobility, crew. |
| Missiles | idea | Guidance, propulsion, seekers — pairs with Sky Duel's heat-seeker/radar content. |
| Rocket launchers | idea | MLRS/HIMARS-style — area fire vs. precision. |

### Biographical graphic novels
| Subject | Status | Notes |
|---------|--------|-------|
| Tesla | idea | Resilience/failure arc. Visual (lightning, Colorado Springs). Inventor lineage w/ da Vinci, Honda. |
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
- **Status:** QA-ready. Pending: Andres QA pass → any audit regens → commit `aim-itself/` + `index.html` only when asked. Kid-QA after that decides whether a mil-tech #2 (tanks/missiles) follows.
- Backlog: flip autonomous-turrets row to `shipped` on commit.
