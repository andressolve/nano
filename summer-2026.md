# Summer 2026 — Reading Project Journal & Backlog

A running log of the summer's reading material for Francisco (9) and Sebastian (7).
Part **journal** (dated entries — what we built, what the kids thought, what we learned)
and part **backlog** (the living idea list with status). Read top-to-bottom to catch up.

---

## Direction this summer

**Sole purpose: nurture and grow mature, sophisticated intellectuals.** That is the only goal.
Every subject and every choice serves that — depth, seriousness, real ideas. We do NOT pick
subjects to fill demographic or representation "gaps," and we do NOT pitch by age. Francisco and
Sebastian are serious readers, not their ages. (See the CRITICAL FRAMING RULE in CLAUDE.md: write
so any first-time reader can follow — a clarity standard, never an age standard.)

Two proven formats carry most of the work:
- **Tech explainer** (Sky Duel, Scattergun register) — machines/systems, premium engineering plate.
- **Biographical graphic novel** (Newton, Gauss, da Vinci... register) — ideas through a life.

**The loose spine** connecting this summer's interests:
machines that move → machines that sense & decide → machines that think → life as information.
(tanks/missiles → autonomous turrets → AI → cells & genetics as code)

**What makes a subject worth doing:** a real human-scale story carrying real ideas, deep enough to
reward a serious reader. Resilience, ethics, the texture of how discoveries actually happen — these
are good *because they grow the mind*, not because they tick a box. Pick the subject that is most
intellectually alive, full stop.

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
| Tesla | shipped | "Tesla — The Man Who Gave the World Its Power." Biographical graphic novel, resilience/generosity arc (gave away the royalty fortune, died broke, vision won). Folder `tesla/`. 18 pages + cover + reader + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. **Shipped 2026-06-22 (commit b6f86c6, pushed). User QA passed ("great work"); kid-QA pending.** |
| Darwin | shipped | "Darwin — The Man Who Let Nature Speak." 2nd summer biography; the great turn from imposing design on nature to induction from overwhelming evidence. Spine = Darwin's patience (get it right, not first); Galápagos told honestly (NO epiphany), Gould's reading of the specimens as the real turn. Folder `darwin/`. 18 pages + cover + reader + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. **Shipped 2026-06-23 (commit 036a9f3, pushed). User QA passed ("absolutely brilliant" — named a gold-standard volume); kid-QA pending.** |
| Cicero | shipped | "Cicero — The Man Who Fought With Words." First Roman biography, first non-scientist on the bio shelf — the human face of the Republic→Empire hinge the two Rome essays describe from above. Spine = the word as power, and its limits against armies; engine = the Catiline knot (finest hour AND lawless execution-without-trial). Folder `cicero/`. Cover + 18 pages + reader + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. **Shipped 2026-06-26 (commit a0f92ec, pushed + deployed). User-QA + kid-QA pending.** |
| Kepler | shipped | "Kepler — The Man Who Trusted the Data." Spine = data over beauty; engine = the eight minutes (tore down his own best-ever circle theory over an 8′ discrepancy → the ellipse → Astronomia Nova). Companion to Newton (his laws are what gravity explains); prequel-in-spirit to Gauss. Folder `kepler/`. Cover + 19 pages + 7 refs + reader (Mars-red `#d1603d`) + WHY-quiz + landing card. **Produced/finished by Codex; shipped 2026-07-03 (commit 75b07c7, pushed — same commit as the catalog reorg). User-QA + kid-QA pending.** |
| Euler | idea | Math lineage (Gauss, Newton, Pythagoras, Descartes). Blind-but-prolific = resilience. |
| Jensen Huang | idea | Frame around the near-bankruptcy years and the long bet on a then-unproven idea, not coronation. |

### Science explainers / hybrids
| Topic | Status | Notes |
|-------|--------|-------|
| The cell | idea | Tech-explainer frame ("the cell is a factory/city" cutaway). |
| Mendel | shipped | "Mendel — The Monk Who Counted." The mechanism of inheritance after Darwin's pattern; spine = the man who COUNTED (turned heredity into arithmetic). Folder `mendel/`. Cover + 17 pages + reader + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. **Shipped 2026-06-24 (commit c5e3778, pushed). User QA passed ("great work. thanks!"); kid-QA pending.** Companion piece: "The Pea Square" clarity rewrite (illustrated-essay format, shipped 2026-06-25, commit 593f65a). |
| Genetics (other angles) | idea | If a 2nd genetics piece later: Rosalind Franklin (the data-vs-credit arc, how evidence gets read) or a "cell as factory" tech-explainer. |

### History / ideas (illustrated essay)
| Topic | Status | Notes |
|-------|--------|-------|
| Why Rome won | shipped | "Why Rome Kept Winning." Text-led illustrated essay (shock-of-florence lineage) that tests the claim "Rome won because it was uniquely organized." Honest answer: discipline was real but NOT unique (Assyria/Macedon/Qin were as drilled) — the real reasons were manpower (the socii), resilience (Cannae → raise new armies), and adaptation (stole the sword, the warship, the formation). Folder `why-rome-won/`. Cover + 8 pages + four-pillar synthesis + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. Produced 2026-06-25 autonomously. |
| How Rome Became the World | shipped | The **sequel** to "Why Rome won" — an HONEST follow-up (NOT a misconception-buster; user: "I am interested in the actual story"). Spine mirrors book one's four pillars, each followed across six centuries until it transforms Rome: allies → Social War → citizenship; army → professionalization → loyalty to generals → Augustus/Empire; the centre → one throne → Third-Century Crisis (Romans vs Romans); absorption → foederati → 376 Danube → Adrianople → the West inherited. 476 = a title quietly lapsing (crown in a box), East endures as "Roman" to 1453. Accent shifts oxblood→imperial purple `#702963`. Folder `rome-became-world/`. Cover + 9 pages + four-pillar synthesis + WHY-quiz + landing card. ZERO regens / ZERO safety rejections across 10 images. Produced 2026-06-26 autonomously. |

### New directions (brainstormed 2026-07-05 — untouched domains of thought, not gap-filling)
| Direction | Status | Notes |
|-----------|--------|-------|
| Intellectual detective stories | vol 1 shipped | A NEW SHELF: true stories told as genuine mysteries — the reader follows the evidence to the reveal; the deduction IS the story. Adds the one tone the collection lacks (mystery) at full intellectual seriousness. **Vol 1 chosen 2026-07-05: Champollion & the Rosetta Stone**, narrative-mystery-comic chassis (multi-panel whodunit pacing, clues on-page). **Vol 2 leading candidate (user: "great idea"): John Snow's cholera map.** Also on deck: Neptune discovered by pure math (Le Verrier); Linear B (Ventris). |
| Money & human systems | idea | First economics piece — an entire domain of thought untouched. "What Is Money?" (shells → coins → paper → numbers on a screen — why any of it works) or "How a Price Is Set." Text-led illustrated essay (argument payload). |
| The idea as protagonist | shipped | "The Promise." Every math book before this one was a mathematician, never the mathematics — this is the hero-is-an-idea-itself volume: proof vs. pattern, Euclid's infinite primes walked through honestly as the payoff. Illustrated-essay format, folder `the-promise/`. Cover + 9 pages + 5-Q quiz + landing card. **Shipped 2026-08-18 (commit bd84bc8, pushed).** User QA passed ("absolutely love it"); kid-QA pending. |
| How music works | idea | New sensory domain: vibration → pitch → why an octave sounds "the same" → harmony vs. dissonance → why a chord resolves. Pythagoras volume on the shelf gives it a hook. Explainer chassis, but about something you hear, not a machine. |

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
- **Status: ✅ Shipped 2026-06-22 (commit b6f86c6, pushed).** User QA passed ("approved. great work."); committed+pushed on user request. Backlog row flipped to `shipped`. **Kid-QA (Francisco + Sebastian) still pending.** First summer biography done; next could be Euler/Jensen Huang (bios) or missiles (greenlit mil-tech #3).

### 2026-06-23 — Next bio chosen: Mendel (handoff to a new session)
- After Darwin shipped and passed QA ("absolutely brilliant"), user confirmed he likes the bio arc and chose **Mendel** as the next biography (over Euler / Faraday-Maxwell / a tech-explainer).
- **Rationale:** the mechanism of inheritance is the direct sequel to Darwin's pattern — Darwin had no theory of how traits pass; Mendel found it in pea plants (1865) and was ignored for ~35 years until rediscovered in 1900. Honest "let the subject be" story: patient, quantitative, overlooked. Pairs with Darwin the way Gauss Book Two pairs with Book One.
- **Watch-out for production:** narrower visual range than a voyage — lean on the Brno abbey/garden/greenhouse register and clean statistical-diagram pages (the 3:1 ratio, the Punnett-style cross) rather than spectacle. Same pipeline: research-first → 5 planning docs → refs → 3 prototypes → bulk → reader → landing card.
- **Status: planned, not started.** A fresh session should start from research (`darwin/`-style `research/RESEARCH-NOTES.md`), holding to [[feedback-let-the-subject-be]] and the gold-standard bar in [[feedback-brilliant-exemplars]].

### 2026-06-23 — 2nd summer biography chosen & produced autonomously: "Darwin"
- User picked **Darwin** as the next bio (Darwin first, then Mendel later — pattern then mechanism), and asked for it to be run **autonomously, end-to-end.**
- **CRITICAL editorial direction from the user (do not violate, logged as a durable feedback memory):** "let the facts speak for themselves. it's a big step in intellectual history — not forcing the worldview on nature, but letting nature speak. don't box it or contort. let it be. focus on the intellectual milestones/breakthroughs and the personalities that brought them." So the book is built **milestone-first, NOT around a manufactured emotional spine.** The honest human through-line is Darwin's own character as a thinker: the patience to get it right rather than the haste to get it first. That patience IS the method, and the method is the milestone.
- **Title: "Darwin — The Man Who Let Nature Speak."** Window: beetle-collecting boy in Shrewsbury (1809) → On the Origin of Species (1859) → burial beside Newton. 18 pages + cover.
- **Editorial honesty (research-first, `darwin/research/RESEARCH-NOTES.md`, web-verified, skeptical):** the central deliberate choice is that **Galápagos is told WITHOUT the lightning-bolt myth** — Darwin had NO epiphany on the islands; he collected carelessly, the famous finches told him nothing yet; the pattern only emerged from **Gould's expert analysis of the specimens back in London (1837)**. That myth-correction IS the book's "let the facts speak" milestone (P6 → P7), not a weakness to paper over. Finches demoted to their true role (mockingbirds + tortoises drove the early doubt). Wallace given real co-credit (the convergence proves the idea was in the facts). Myths explicitly avoided: "survival of the fittest" wasn't Darwin's phrase, Origin is barely about humans, the Lady Hope deathbed-conversion story is a fabrication.
- **Visual signature:** oil-painting realism (Newton/Gauss/da Vinci/Tesla lineage); naturalist's specimen-cabinet sepia & mahogany pierced by the **green-gold of living nature** as the one warm accent (life breaking into the scholar's brown world); a quiet **branching-form motif** (coral, roots, rigging, river deltas) recurring across the volume and culminating in the **P18 Tree of Life** closing-as-invention finale.
- **BEARD DISCIPLINE (load-bearing, Darwin grew the famous beard only ~1862):** four Darwin age-phases — boy ~9, young ~23 CLEAN-SHAVEN, mid ~48 balding/side-whiskers only, old ~70 the iconic white beard. Stated explicitly in every page prompt; held perfectly across all 19 images (no drift to the bearded-sage default on the pre-1862 pages).
- **No composite ref needed** — every multi-character page is ≤2 named faces (Strategy 1: lock the harder/secondary face via `edit_image`, prose Darwin). Henslow, FitzRoy+Beagle, Gould, Emma, Wallace, Hooker+Lyell all handled this way single-shot.
- **Cleanest-tier run: ZERO regens, ZERO safety rejections across all 19 images + 12 refs.** (The Edinburgh surgical-theatre page P2 — a known moderation risk — passed first time by draping the body entirely and anchoring on Darwin's recoil, NO gore.) 12 refs → 3 prototypes (P8 "I think" notebook / P9 Malthus annotated / P18 Tree of Life, all single-shot) → cover + 15 pages in two parallel waves. Est. cost ≈ **$6.50** (~31 single-shot image calls), in line with the bio envelope.
- **Reader built** (`darwin/index.html`): dark Palatino flipper cloned from Tesla, **living leaf-green `#6fa86b`** accent. 5-question WHY-quiz per the CRITICAL QUIZ RULE (length-matched distractors, answers shuffled a/b/c/a/b): why Galápagos gave no instant answer, why Gould mattered, why Darwin waited 20 years, what Wallace's letter proved, why the Tree of Life is the right picture. End interstitial "He Let Nature Tell Its Own Story."
- Landing card + footer folder-list entry added to root `index.html`.
- **Status: ✅ Shipped 2026-06-23 (commit 036a9f3, pushed).** User QA passed with the strongest praise in the project to date ("absolutely brilliant"), named among his 4 gold-standard volumes (Darwin/Gauss/Descartes/Newton). Backlog row flipped to `shipped`. **Kid-QA (Francisco + Sebastian) still pending.** Next bio candidate per the user's own sequencing = **Mendel** (the mechanism after the pattern).

### 2026-06-24 — "Mendel — The Monk Who Counted" shipped (autonomous)
- 3rd summer biography, the planned Darwin companion (pattern → mechanism). Folder `mendel/`: cover + 17 pages + reader (violet `#9176c4`) + WHY-quiz + landing card. Spine = the man who COUNTED; editorial honesty held (uncut-paper legend avoided as myth, "My time will come" framed as traditionally-attributed, Fisher "too good" critique deliberately omitted).
- **ZERO regens, ZERO safety rejections** across 18 images + 10 refs (~$6); clean-shaven discipline held on every page across 4 age phases.
- **Status: ✅ Shipped 2026-06-24 (commit c5e3778, pushed).** User QA passed ("great work. thanks!"); kid-QA pending.

### 2026-06-25 — New direction: a history essay correcting a claim the user makes to his kids ("Why Rome Kept Winning")
- This one started as a "next bio?" conversation but the user pivoted: *"i keep telling them that order is good. that the roman army was so goddamn successful because they were organized. unlike anyone else. is that right? can we do something about this?"* — explicitly asked to **look stuff up, not rely on model knowledge.** The intent is a research-honest piece that tests his own claim, not a flattering confirmation of it.
- **Format decision (a new durable rule).** User: *"the last explainer was too 'image-heavy', currently working on revising it to more of 'text accompanied by great images'. which you think is more appropriate here?"* — answer: a **text-led illustrated essay** (the `shock-of-florence/` lineage), because the payload here is an *argument*, not a physical object you look at. Logged as feedback memory `feedback_explainer_text_led.md`: image-led is right for things-you-look-at; text-led is right for reasoning/argument subjects.
- **The honest finding (the intellectual heart of the book).** The claim is *half right*. Roman discipline was real and extreme — every night on the march they built a fortified camp from scratch (Polybius Bk 6). But organization was **not unique and not the differentiator**: Assyria (year-round professional army), Macedon (the full-time sarissa phalanx), and Qin China (universal conscription, ranked crossbowmen) were all as disciplined or more. So the book *corrects* the "unlike anyone else" part the user tells his kids, and gives the real three-part answer: **manpower** (the Italian *socii* supplied ~half of every Roman army), **resilience** (after Cannae wiped out ~8 legions in an afternoon, Rome refused terms and raised new armies), and **adaptation** (Rome stole the gladius from Spain, copied a wrecked Carthaginian warship + invented the corvus, took the manipular legion from the Samnites who beat it).
- **Research-first.** Full web-verified archive at `why-rome-won/research/RESEARCH-NOTES.md` with explicit editorial-honesty flags: never say Rome "fielded 700,000" (that's a theoretical census pool, disputed — give Cannae casualties as a *range*, Polybius ~70k / Livy ~48k); never claim the organization was unique; admit the alliance *partly* defected (Capua and much of the south went over to Hannibal) while >80% held; note the corvus was later abandoned; no anachronistic "citizenship for all" (the Social War that broadened it is 91–88 BC, off-window); the closing line is the author's own, not a fake ancient quote.
- **Build.** Folder `why-rome-won/`: 5 planning docs (brief/style/subjects/settings/script) + research archive. Cover + 8 content pages, two image sub-registers under one warm palette (painted museum-reconstruction scenes + antique tactical-map/cartography for the socii map and the Cannae double-envelopment), oxblood-red `#9a2f2f` accent, bronze `#9c6b2e` for Part Three. Period accuracy locked to the **mid-Republic** (Montefortino helmets, oval scutum, mail/bronze pectoral — explicitly NOT the imperial segmented-armor Hollywood legionary). The four-pillar synthesis (Discipline / Manpower / Resilience / Adaptation) is built as a **CSS block**, not a generated image, to keep in-image text near zero.
- **Production: ZERO regens, ZERO safety rejections across all 9 images.** The two moderation-risk scenes passed first time by register discipline — Cannae rendered as a tactical schematic (not a killing-floor), the corvus naval boarding dramatic-not-gory, the post-Cannae Forum dignified-mourning (Rome itself was never sacked). Reader cloned from shock-of-florence: light parchment body, Cormorant Garamond, fact boxes + pull-quotes, 5-question WHY-quiz (answers b/d/a/c/b, length-matched distractors), dark cover + dark end page. Landing card + footer entry added to root `index.html`.
- **Status: ✅ Produced 2026-06-25 autonomously (user stepped away for a couple hours and asked for it QA-ready on return). NOT committed — no commit was requested.** Awaiting user QA, then kid-QA. First history-essay subject of the summer and first piece that exists to *correct* something the user himself was teaching.

### 2026-06-26 — The sequel, autonomously: "How Rome Became the World"
- User liked the last two essays (Pea Square rewrite + Why Rome Kept Winning) and asked for the next one, **not** constrained to the summer reading plan, fitting the essay format. After a miss (I pitched generic pop-science myth-busters — *"you are not at all taking into account our particular context"*), the right idea was the **direct sequel** to Why Rome Kept Winning: how does the unbeatable machine ever *stop*?
- **Framing is the whole point and was set explicitly by the user:** *"frame it as natural follow up to the previous reading. not 'trivia night' framing, not 'common misconceptions' framing... i dont give two shits about dispelling common misconceptions. i am interested in the actual story."* So this is NOT a "barbarians-didn't-really-sack-Rome" myth-buster. It tells the real story honestly, as a continuation of book one's reading.
- **The honest spine (mirrors book one's four pillars, each followed to its end across six centuries):** the **allies** demand to *be* Rome → Social War → citizenship → Italy becomes Roman; the **army** professionalizes → loyalty shifts from Republic to general → Caesar/Rubicon → Augustus → Empire; the **centre** becomes one throne → Third-Century Crisis (>20 emperors in 50 yrs, Romans killing Romans, plague, coinage collapse, empire splits three ways) → Diocletian/Constantine rebuild → Constantinople, heart moves east; **adaptation** takes in whole armed nations (foederati) → 376 Danube crossing → Adrianople 378 → sacks of 410/455 → the West is *inherited*. 476 = Odoacer letting the title lapse (crown in a box, sent east), and the honest BOTH/AND: real material decline in the West *and* deep continuity. The East never falls — to 1453 — and calls itself *Roman* (*Rhomaioi*); "Byzantine" is a later coinage.
- **Research-first.** Full web-verified archive at `rome-became-world/research/RESEARCH-NOTES.md` with 8 editorial-honesty flags: NO single "Marian reform" (professionalization was gradual, completed under Augustus — 21st-c. specialists call the 107 BC reform a Mommsen-era construct); don't swap one myth for another (hold the Brown vs Ward-Perkins/Heather debate honestly); 476 is a convention not a thunderclap; Rome ≠ the capital by then (Ravenna from 402); the "barbarians" were peoples Rome had fought/hired/settled for centuries; figures as ranges (~two-thirds of the army at Adrianople); no fake ancient quotes.
- **Build.** Folder `rome-became-world/`: 5 planning docs + research archive. Cover + 9 content pages, same two-register/one-palette chassis, but accent shifts from book one's Republican **oxblood `#9a2f2f`** to imperial **"Byzantium" purple `#702963`** (the emperors' Tyrian purple, literally the color named for the city the story ends in). New period-accuracy challenge handled: **kit evolves by era** across the volume (late-Republic mail/Montefortino → high-Empire segmented plate [the look BANNED in book one, now period-correct] → third-century transitional → late-Roman ridge helmets/oval shields → Eastern Roman lamellar). The **aquila eagle** is the visual through-line: opens the cover in dusk shadow, returns on P9 as a Byzantine labarum a thousand years later. Four-pillar synthesis (THE ALLIES / THE ARMY / THE CENTRE / THE GENIUS FOR ABSORBING) is a CSS block, not an image.
- **Production: ZERO regens, ZERO safety rejections across all 10 images.** Two prototypes single-shot (the empire-extent map with clean ROMA/MARE NOSTRUM labels; the cover's west-dusk/east-dawn light device), then the remaining 8 in two parallel waves, all single-shot. Moderation-risk pages passed by register discipline: the Third-Century-Crisis page rendered as Roman-against-Roman with the same eagle on both sides (grim, not gory); the 476 page as a dignified hall with the crown placed in a chest (a title lapsing, NOT a sack); the Danube crossing as refugees-and-army (tense, not a battle). Reader cloned from why-rome-won: purple accent, 12 sections, 5-question WHY-quiz (answers c/a/d/b/c, length-matched distractors). Landing card + footer entry added to root `index.html`.
- **Status: ✅ Produced 2026-06-26 autonomously, taken all the way to commit + push per user request ("take it all the way autonomously, all the way to commit and push").** Kid-QA pending. Second history-essay of the summer; first sequel in the essay format.

### 2026-06-26 — Next piece chosen: Cicero (biography, handoff to a new session)
- After shipping the two Rome essays, user wanted to follow them with a **biography of a Roman** — zoom from the system down to one human inside it. Considered Cicero, Marcus Aurelius (overlaps the existing `marcus/` fiction piece), and Pliny the Elder (science-bio wildcard). **User chose Cicero.**
- **Why Cicero fits:** he is the human face of the exact Republic→Empire hinge the two essays describe from above (esp. *How Rome Became the World* P3 — Caesar/Rubicon/Augustus). The collection's bios are all scientists/inventors; Cicero adds a new kind of mind — the orator/statesman, with the **word** as the weapon. Milestone-first, honest material is rich (vain, vacillating, brave at the end).
- **Format = biographical graphic novel** (the bio.md playbook — Newton/Gauss/Darwin/Mendel lineage, oil-painting register), NOT the illustrated-essay format the two Rome pieces used. (If the next session prefers, the illustrated-essay format is also defensible for an idea-led figure — but default is the bio graphic-novel chassis.)
- **Handoff notes for the next session live in memory: `project_cicero_handoff.md`** (decision, spine, rubric, research-first requirement, anti-patterns). RESEARCH the life before committing the brief — do not rely on model knowledge for dates/quotes (no fake ancient quotes; Cicero's real letters/speeches exist, quote accurately or paraphrase honestly).

### 2026-06-26 — "Cicero — The Man Who Fought With Words" shipped (autonomous)
- Produced end-to-end per the handoff: research-first (web-verified, no fake quotes; one iconic Latin line on P5 with English helper), cover + 18 pages + reader + WHY-quiz + landing card. Folder `cicero/`.
- Spine = **the word as power — and its limits against armies**; engine = the Catiline knot (his finest hour AND a lawless execution-without-trial → exile). Death dignified, implied via a Rostra inset. Lamp-gold `#d4a84b` accent = the voice: full → dim → gone at death → returns in the scrolls (P18).
- **ZERO regens, ZERO safety rejections** across 19 images + 10 refs (~$6). Strategy 1 throughout (≤2 named faces/page, no composite).
- **Status: ✅ Shipped 2026-06-26 (commit a0f92ec, pushed + deployed).** First Roman biography, first non-scientist bio. User-QA + kid-QA pending.

### 2026-07-02 — "Icarus — The Boy Who Touched the Sun" launches the myth/epic shelf; landing page reorganized
- First volume of the new **myth/epic narrative comic** shelf (true multi-panel dialogue comics; ink-line + flat-color "Olympians" register; landscape 3:2; one-shot whole-page text bake). Folder `icarus/`. Cover + 14 pages + dark-flipper reader + 5-Q quiz + landing card.
- Spine = appetite-and-consequence + Daedalus's grief; the "middle way" taught as safety between two real dangers. Near-flawless run: ZERO drift across 15 images; ~$5. Durable lesson: for a recurring apparatus that renders wrong (P14 wings-on-chest), mint a dedicated ref of the character *wearing* it rather than fighting per-page prose.
- Root `index.html` reorganized the same day: flat 37-card grid → a "Latest · just shipped" 6-card strip + 7 compact category shelves. (Committed 2026-07-03 as part of the Kepler commit.)
- **Status: ✅ Shipped 2026-07-02 (commit 2731377, pushed).** Kid-QA pending; next myth TBD.

### 2026-07-03 — "Kepler — The Man Who Trusted the Data" shipped (finished by Codex); catalog reorg committed
- **Produced/finished by Codex** (not this Claude session), on the bio graphic-novel chassis (oil-painting register, Newton/Gauss/Darwin/Mendel/Cicero lineage). Folder `kepler/`: full planning docs + RESEARCH.md, cover + 19 pages, 7 refs (4 Kepler age phases + Tycho, Barbara, Katharina), dark reader with Mars-red `#d1603d` accent + WHY-quiz.
- Spine = **data over beauty**, milestone-first: the wrong-but-fertile Mysterium → **the eight minutes** (tore down his own best-ever circle theory over an 8′ discrepancy → area law → ellipse → Astronomia Nova 1609) → third law five days before the Defenestration of Prague → the witch trial fought with forensic error analysis (the 8′ integrity as a family trait) → Rudolphine Tables → vindication coda.
- Editorial discipline per its RESEARCH.md: verbatim-quotes-bank only, no Tycho-poisoning wink, brass nose not silver, anti-myth thesis stated explicitly (mysticism supplied motivation, never evidence he accepted against data), witch trial dignified (no torture depicted).
- Companion to `newton-vol1/` (Kepler's laws are what Newton's gravity explains); the Thirty Years' War backdrop is the collection's first step into the 17th century. Run metrics (regens/cost) not logged — Codex run; brief budgeted ~$6.30.
- **Status: ✅ Shipped 2026-07-03 (commit 75b07c7, pushed — same commit finalizes the landing-page catalog reorg: Kepler card added to the Latest strip + biographies shelf).** User-QA + kid-QA pending.

### 2026-07-05 — Four new directions brainstormed (backlog section added above)
- User asked for "something we haven't really thought about, a new direction" — explicitly beyond the proven lanes (next myth, Foundation Vol 2, missiles, next bio).
- Surveyed what the collection does NOT touch as *domains of thought*: no economics, no language/linguistics, no music, no pure-idea book (math pieces are all mathematicians, never the mathematics), and tonally no mystery.
- Four candidates logged in the backlog: **intellectual detective stories** (new shelf; Rosetta/Neptune/cholera-map), **money & human systems**, **the idea as protagonist** (Infinity/Zero/Proof), **how music works**. User reaction: "oh wow, that's great stuff" — all noted, none chosen yet.

### 2026-07-04 — "Foundation — Book One: The Plan" shipped: the sci-fi shelf opens
- First volume of the new **sci-fi shelf** and the second literary adaptation (after Name of the Rose). Asimov's *Foundation* Parts I–II (The Psychohistorians + The Encyclopedists). Folder `foundation/`: full planning docs, cover + 16 landscape pages, 7 refs (Gaal, Seldon, Seldon-hologram, Hardin, Pirenne + 2 composite plates), dark-flipper reader with teal `#45c9be` accent + 5-Q WHY-quiz + landing card + a new "Graphic novels · science fiction" shelf on the landing page.
- Register = **1970s British SF paperback airbrush** (teal/magenta/amber, chrome starships, monumental haze), validated on two prototypes in `foundation/style-tests/` the day before — both slotted directly in as P1 (Trantor arrival) and P5 (Seldon's trial). The v4 lettering rulebook (speakers staged left-to-right in speaking order) held at production scale: 14 of 15 dialogue pages landed attribution single-shot; the one failure (P4, a 3-beat exchange) was fixed by restaging the script, not patching tails.
- All baked quotes source-verified (Seldon Crisis transcripts + LitCharts): "Violence is the last refuge of the incompetent", "I am Hari Seldon", the fraud reveal, "obvious as all hell". Dorwin's dropped-R drawl rendered exactly, framed by caption as characterization. Run: ~21 images ≈ $4.40, ONE regen, ZERO safety rejections.
- **Status: ✅ Produced 2026-07-04, NOT committed.** User-QA + kid-QA pending. Vols 2–3 mapped ("The Priests" = The Mayors; "The Merchants" = The Traders + Merchant Princes).

### 2026-07-05 — Foundation user-QA passed and fully repaired (three rounds), committed + pushed
- User-QA verdict: "what a beauty." Three repair rounds followed: P6 commissioner clones (PIL-crop of validated P5 bench pixels), P10/P12 inconsistent trustee (new `ref_fara.png`), then Fara-vs-Pirenne costume collision (recolored Fara russet-brown, rebuilt composites, regenned P10/P12 v3). All committed+pushed (db089cb → 1844997 → 0c231ba). Foundation Vol 1 live; kid-QA open → gate for Vol 2 "The Priests".
- Same day, the **multi-reference unlock**: OpenAI `/images/edits` accepts up to 16 `image[]` inputs — the one-ref limit was our wrapper's, not the model's. `edit_image` upgraded to take `imagePaths` (1–16), smoke-tested (2 Kepler refs → one plate, both faces faithful). Composite plates and lock-the-harder-face demoted to fallbacks; native multi-ref is the new default (`gemini_thin.md` C.7 Strategy 0).

### 2026-07-05 — "The Riddle of the Stone" ships Case No. 1 of the intellectual-detective shelf (autonomous)
- **The new shelf opens.** Champollion & the Rosetta Stone as a true whodunit: the reader is handed the same clues as the detective (cartouche exhibits WITH letter annotations on P7/P10, a deliberately unannotated exhibit on P12 so the reader can race him to RA-MES-SES) and the reveal is earned, not announced. Folder `rosetta/`: RESEARCH.md + 5 planning docs, cover + 17 landscape pages, dark reader with lamplight-gold `#d9a441` accent + persistent CASE-FILE strip (THE SILENCE · THE STONE · FALSE TRAILS · THE CLUES · THE REVEAL · THE LANGUAGE, active stage lit per page) + 5-Q WHY-quiz + landing card + new "Intellectual detective stories" shelf on the landing page.
- Register = "ink & lamplight" (Register-B ink-line tuned to a nocturnal case-file palette: ink-blue/charcoal + parchment + amber; Egypt scenes sun-bleached ochre as the counter-world). Structure = detective beats: the silence (Philae 394), the evidence (the stone, three bands, the break), false trails (symbols-not-sounds; even the detective believed it until 1821), the rival (Young — real credit given honestly on P15), the cross-check (P10 splash: P/O/L landing in both cartouches, predicted before looking), the cascade, the reveal ("Je tiens mon affaire !" + the faint — verified), the confession scene, the language coming back (Coptic gives MEANING: re + mise).
- **New load-bearing technique validated: PIL-built hieroglyph exhibits.** Every load-bearing glyph string (Ptolemy, Cleopatra, Ramesses, Thutmose cartouches + clue key + the P10 cross-check board) was rendered from verified Gardiner sign sequences via Noto Sans Egyptian Hieroglyphs (`rosetta/tools/build_cartouche_plates.py`) — the model NEVER freehands a cartouche; plates are passed as refs with "COPY EXACTLY, do not invent/add/alter any hieroglyph." Crop-zoom review confirmed sign-for-sign fidelity on every exhibit page. This is the volume's whole credibility and it held.
- **First full production run on native multi-ref `imagePaths`** (unlocked yesterday): master cast plate (5 subjects incl. the Stone as object-character, single generation, user directive) → 5 solos → pages each passed plate/solo/exhibit refs natively. Multi-character pages (boy+brother, detective+brother, detective+rival ×2) all landed without composites.
- **Run: ZERO regens, ZERO safety rejections across 24 images** (18 pages + 6 refs/plates generated; PIL plates free), ≈ $5.04 vs $5.70 budget. Two accepted nits: a period-plausible invented book-spine on P13, helpful city tags on P3.
- **Status: ✅ Shipped 2026-07-05 autonomously (committed + pushed, `rosetta/` + root index.html only). User-QA PASSED 2026-07-06 — "wow, that was an amazing story. BRAVO!!!" — and the user asked to keep production notes because "we need to be able to make more of these" (shelf recipe distilled into memory).** Kid-QA pending. Vol 2 leading candidate: John Snow's cholera map (user-endorsed "great idea").

### 2026-07-05 — "Foundation — Book Two: The Priests" produced (autonomous): the sci-fi shelf grows
- Asimov's *Foundation* Part III (The Mayors / "Bridle and Saddle") as Vol 2 of 3. Folder `foundation-vol2/`: 5 planning docs (written earlier the same day, script pre-verified against sources), cover + 16 landscape pages, 3 refs, dark-flipper reader + 5-Q WHY-quiz + landing card (Latest strip + sci-fi shelf, Rome-became-world card rotated out to its essay shelf).
- Spine = the religion of science as **bridle and saddle**: Hardin lets Wienis aim the resurrected battlecruiser at Terminus, then the priesthood itself pulls the trigger (Aporat's curse → interdict blackout → Lefkin's broadcast → the beam breaking on the force shield). Seldon's second Vault appearance seeds Vol 3 (spiritual power "not sufficient to attack in turn" → trade).
- **Two production firsts validated:** (1) cross-volume aging — `ref_hardin_old` built by edit_image on Vol 1's `ref_hardin` ("same man aged thirty years"), continuity landed first try; (2) the **single-generation GROUP ref sheet** experiment — all 6 new recurring characters locked in just 2 generate calls (4-figure Anacreon court + 2-figure Terminus pair), every face passed the review gate, and multi-ref `imagePaths` fed the sheets to every page. Refs went from ~10 calls (Vol 1 pattern) to 3.
- Moderation designed out at script level held: Wienis's end caption-implied only, Nyak hunt pursuit-only, blaster beam breaks harmlessly — the blaster page passed first try.
- **Run: ZERO regens, ZERO safety rejections across 20 images** (3 refs + cover + 16 pages), ≈ $4.20 — on budget, cleanest multi-character volume yet.
- **Status: ✅ Shipped — produced 2026-07-05 autonomously, user-QA PASSED 2026-07-06 ("amazing work! well done!"), committed+pushed 2026-07-06.** Kid-QA pending. Vol 3 "The Merchants" mapped and plantable.

### 2026-07-07 — "Foundation — Book Three: The Merchants" produced (autonomous): the trilogy is complete
- Asimov's *Foundation* Parts IV–V (The Traders + The Merchant Princes) as Vol 3 of 3 — the full first novel is now adapted. Folder `foundation-vol3/`: 5 planning docs, cover + 16 landscape pages, 4 refs, dark-flipper reader with trade-gold `#d9a441` accent + 5-Q WHY-quiz + landing card (Latest strip + sci-fi shelf, Icarus card rotated out to the myth shelf).
- Spine = the volume's handover of light: blue-white (science-as-religion) → amber-gold (trade). Ponyets' transmuter prologue plants the idea; Hober Mallow proves it at scale — refuses the priesthood on Korell, sells gadgets naked, turns his own treason trial into a mayoral campaign with the ultraviolet freeze-frame (Parma's KSP tattoo), then wins Seldon's third crisis with an embargo: dead washing machines and dark kitchens beat dreadnoughts. "Surrender without a shot."
- Vol 2's group-ref technique held and tightened: 7 recurring characters locked in 4 calls (1 Mallow solo + 3 two-figure group sheets), each face review-gated; native multi-ref `imagePaths` fed sheets per page with "use ONLY figure A/B" clauses — partial group-sheet use worked every time. Seldon hologram reused unchanged from Vol 1's ref (third volume, same ghost).
- Moderation design-outs held again: missionary mob = distant torchlight through a viewport, his fate caption-only; the war = looming dreadnoughts vs. withdrawing traders, nothing fired upon; embargo hardship = cold and stillness, no suffering bodies. ZERO safety rejections.
- **Run: ZERO content regens across 21 images** (4 refs + cover + 16 pages), ≈ $4.40 — on budget. One transient 502 retried (P9). Two accepted nits: Ponyets' ref rendered his coverall denim-blue instead of scripted grey-green (ref-is-truth: lock updated to match); P12 caption has a ~2px stray accent ("Fouńdation"), invisible at reading size (Gauss P12 precedent).
- **Status: ✅ Shipped — produced 2026-07-07 autonomously, user-QA PASSED 2026-07-07 ("excellent work. well done!"), committed+pushed (f635d53).** Kid-QA open. The sci-fi shelf's first complete trilogy.

### 2026-07-06/07 — "The Riddle of the Well" ships Case No. 2 of the intellectual-detective shelf (autonomous, committed+pushed 2026-07-07)
- John Snow's 1854 Broad Street cholera investigation as a true whodunit: miasma treated as a serious rival theory (not a strawman), the door-to-door death map, two predictive tests (brewery/workhouse; the Hampstead widow), the honest-doubt beat about the pump handle, Whitehead's independent cesspool discovery, and Farr's own 1866 conversion to Snow's method. Folder `cholera-map/`: cover + 19 pages, dark reader with well-water teal `#4a9b95` accent + CASE-FILE strip (THE FEAR · THE OUTBREAK · THE FALSE TRAIL · THE MAP · THE REVEAL · THE CURE) + 5-Q WHY-quiz + landing card.
- **5 PIL exhibit plates** (`tools/build_broad_street_map.py`, modeled on Rosetta's cartouche-plate precedent): unannotated map (reader-race page), full labeled map, solved map with discovery ring, cesspool diagram, Grand Experiment number table. New reusable "label halo" technique — a small cream rounded-rectangle drawn behind text labels so they stay legible over dense death-bar clutter.
- One caught+fixed defect: P17 (Grand Experiment page) — the model invented an unscripted "nine-fold" claim that numerically contradicted the scripted "nearly eightfold" caption. One regen with an explicit "do not invent extra captions / no additional numeric claims" instruction landed clean.
- Dignified-death and honest-mystery discipline held with zero fixes needed (Susannah Eley and the cesspool-house infant handled entirely off-page).
- **Run: ZERO regens beyond the one P17 fix, ZERO safety rejections across 20 images + 4 refs.**
- **Status: produced 2026-07-06, user approved "commit and push" 2026-07-07, committed+pushed (23d9767).** User-QA + kid-QA open.

### 2026-07-08 — "A Wizard of Earthsea — The Shadow and the Name" ships (autonomous, committed+pushed)
- Le Guin adaptation, first Narrative Mode volume run fully end-to-end by a single autonomous session with no check-ins. Folder `earthsea/`: cover + 20 pages, "sea-mist ink-line" register (cold maritime flats, gold reserved strictly for fire/werelight/spell-glow, THE SHADOW always flat matte black), "voyage-strip" reader (teal `#5aa8a2`, highlights active isle: GONT · ROKE · LOW TORNING · PENDOR · OSSKIL · IFFISH · THE OPEN SEA) + 5-Q WHY-quiz + landing card.
- Skin-tone discipline required two targeted regens (`ref_ged_young`, `ref_ged_scarred` first-passed light/olive despite the brief naming skin tone the volume's non-negotiable, per Le Guin's own stated intent) — fixed with unambiguous "DEEP RED-BROWN COPPER, NOT pale, NOT olive" language. Lesson: cross-check refs against the stated non-negotiable explicitly, not just "does it look okay."
- **Run: 3 prototypes passed first try; ZERO regens across the entire 18-page bulk batch** (21 images total), ≈ on-budget. Group ref sheets (Foundation-validated) worked cleanly for two multi-character casts.
- **Status: ✅ Shipped — produced + committed+pushed 2026-07-08 (8b6c2fc), fully autonomous; user-QA PASSED 2026-07-08 ("absolutely amazing. bravo!!!").** Kid-QA open.
- **The QA pass came with a pacing critique, now a standing rule:** the volume compressed all 10 chapters into 20 pages and parts felt rushed, with events happening off-page. User: "no need to rush. if we need many volumes, so be it… don't skimp on pages/volumes." → Never cram a source into one volume; partition at natural arc boundaries, as many volumes as the story needs. **Next: Vol 2 = *The Tombs of Atuan*, Part One — planning docs first, image generation deferred to a later session.**

### 2026-08-08 — *The Count of Monte Cristo* expanded edition completes its 55-page production run

- Folder `monte-cristo-expanded/` now contains all 55 canonical 1024 × 1536
  portrait pages with native lettering and a complete local reader. The run is
  production-complete, locally verified, and published from `main` on
  2026-08-08 after Andres's final approval.
- User QA on the working result: **"so far looking great. i think you nailed the
  workflow on this one."** The praised workflow is now recorded as the durable
  long-run builder/critic pattern for **narrative/dialogue-driven graphic
  novels** in the workspace-wide `dialogue.md` playbook, with a summary in
  `IMAGE_GENERATION_GUIDE.md` and the binding subset in `AGENTS.md`.
  Per Andres's explicit follow-up, this does **not** change the previous
  biographical graphic-novel workflow; `bio.md` and the `honda-soichiro/` model
  remain authoritative and unchanged.
- **Builder/critic separation was the key.** The builder generated one plausible
  page after one essentials check; the independent critic—not the builder—owned
  pass/fail. Prompt preparation for the next page ran during review, but the next
  generation stayed held until the current canonical page was approved and
  promoted.
- **How the critic was actually built is now recorded, not inferred from its
  reports.** It was a separate agent repeatedly given the candidate path and
  sibling prompt/audit/proofs, then asked to judge exact script/story, clear
  attribution, obvious generation/anatomy integrity, consequential
  identity/continuity, actual desktop/tablet comfort, and a short page-specific
  checklist drawn from that page's script and prompt. Its output was constrained
  to a saved report plus `APPROVED` or `REJECTED` with mandatory findings only;
  it could not edit or promote art. See
  `monte-cristo-expanded/36-BUILDER-CRITIC-RUN-NOTES.md` for the actual task
  templates and control flow.
- **Regeneration was rare and evidence-based.** Complete redraws occurred only
  for real defects: reversed dialogue causality, response-before-sound order,
  and a missing required line. Rejected versions were preserved; no crop patch,
  post-hoc lettering, failed-page reference reuse, or opportunistic polish loop
  was allowed.
- **Approved state drove continuity.** Every new page used the latest canonical
  predecessor plus the minimum needed identity/object references. Approved
  candidates were promoted byte-for-byte with prompt, audit, proofs, critic
  report, and hash retained.
- **Batch gates mattered.** Fresh uninterrupted reviews of Pages 21–30, 31–40,
  41–50, and 51–55 all passed. The gates evaluated the story as a reader sees it,
  catching the class of cross-page problem that isolated page inspection cannot.
- Production used subscription-backed in-app ImageGen throughout, never an API
  key or separately billed image-generation path.
- Volume II is next, as a separate production rather than Pages 56 onward. Its
  substantial new-session brief is `MONTE-CRISTO-VOLUME-2-HANDOFF.md`; research,
  remaining-series rebudgeting, complete-script review, and reference gates
  precede any new image generation.

### 2026-08-18 — "The Promise" ships: the idea-as-protagonist essay, first of its kind (committed+pushed)

- Folder `the-promise/` — cover + 9 essay pages + 5-Q quiz + end page, illustrated-essay
  format (parchment theme, no fictional protagonist). Fills the backlog item
  "the idea as protagonist" (line 72 above, brainstormed 2026-07-05): the hero
  is a piece of mathematics itself, not a mathematician. Spine: the difference
  between **pattern/evidence** (a pile of confirming cases, always revisable)
  and **proof** (finished, permanent), with Euclid's proof that there are
  infinitely many primes as the payoff the whole essay is built to deliver.
- **Editing was entirely iterative, not a single generation pass** — this volume
  was built through many rounds of granular user feedback across a single long
  session: line-level phrasing cuts, an Opus-agent-drafted rewrite of the
  Euclid-proof paragraph (with the user demanding the key inference be stated
  explicitly rather than implied), and progressively more aggressive structural
  cuts. Content removed entirely during the session: a "now watch it break"
  recap section, a full "What He Actually Said" footnote page on Euclid's
  proof's exact historicity, and a whole "The Fence" / "The Thing Gödel Found"
  detour into the limits of proof — all judged well-written but tangential.
- **The Fermat-vs-Euler swap.** Part One originally carried two "pattern that
  breaks" examples (Fermat's 2^k+1 primes, breaking at k=32; Euler's n²+n+41,
  breaking at n=40). User first cut Euler and kept Fermat, then reversed that
  decision a turn later ("fermat page puts more things under the rug") on an
  Opus agent's recommendation: Fermat's break (641 × 6,700,417) is asserted,
  not derived — "Euler produced the factor like a man pulling a card out of a
  deck" — while Euler's break is fully constructible on-page from
  n(n+1)+41, which is the essay's actual thesis (reasoning beats counting).
  Fermat was cut outright, including its "the honest mathematician" historical
  color — no trimmed remnant kept, per the session's cut-fully-or-not-at-all
  pattern.
- **Closing move: a full-essay clarity audit.** After all structural cuts
  landed, the user asked for one more Opus-agent pass across the *entire*
  finished essay — not for more content cuts, but hunting line-level
  "impress the reader" writerly flourishes surviving inside otherwise-kept
  pages (rhetorical throat-clearing like "this is the hinge the whole essay
  turns on," redundant closing beats restating a point already made, a
  history-of-scholarship detour on page 6 that delayed its own payoff). All
  11 flagged fixes were applied as recommended.
- User verdict, verbatim: **"absolutely love it. great work."** New standing
  principle recorded from this session: [[feedback-single-idea-focus]] — drive
  ONE idea, cut anything that's a side show even if individually well-written,
  and when cutting, cut fully rather than leaving a softened remnant.
- **Status: ✅ Shipped — committed+pushed 2026-08-18 (bd84bc8).** Not yet
  linked from the root `index.html` landing-page card grid — offered, not yet
  actioned. User-QA + kid-QA open.
