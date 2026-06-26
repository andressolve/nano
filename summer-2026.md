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
| Darwin | shipped | "Darwin — The Man Who Let Nature Speak." 2nd summer biography; the great turn from imposing design on nature to induction from overwhelming evidence. Spine = Darwin's patience (get it right, not first); Galápagos told honestly (NO epiphany), Gould's reading of the specimens as the real turn. Folder `darwin/`. 18 pages + cover + reader + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. Produced 2026-06-23; **awaiting user QA, not yet committed.** |
| Euler | idea | Math lineage (Gauss, Newton, Pythagoras, Descartes). Blind-but-prolific = resilience. |
| Jensen Huang | idea | Frame around the near-bankruptcy years and the long bet on a then-unproven idea, not coronation. |

### Science explainers / hybrids
| Topic | Status | Notes |
|-------|--------|-------|
| The cell | idea | Tech-explainer frame ("the cell is a factory/city" cutaway). |
| Mendel | planned | **CHOSEN as next bio (2026-06-23).** The mechanism of inheritance after Darwin's pattern — peas in a monastery garden (1865), quantitative/patient method, ignored until 1900. Pairs directly with Darwin (pattern → mechanism), like Gauss Bk1→Bk2. Watch visual variety (garden/abbey/statistical-diagram register, not spectacle). |
| Genetics (other angles) | idea | If a 2nd genetics piece later: Rosalind Franklin (the data-vs-credit arc, how evidence gets read) or a "cell as factory" tech-explainer. |

### History / ideas (illustrated essay)
| Topic | Status | Notes |
|-------|--------|-------|
| Why Rome won | shipped | "Why Rome Kept Winning." Text-led illustrated essay (shock-of-florence lineage) that tests the claim "Rome won because it was uniquely organized." Honest answer: discipline was real but NOT unique (Assyria/Macedon/Qin were as drilled) — the real reasons were manpower (the socii), resilience (Cannae → raise new armies), and adaptation (stole the sword, the warship, the formation). Folder `why-rome-won/`. Cover + 8 pages + four-pillar synthesis + WHY-quiz + landing card. ZERO regens / ZERO safety rejections. Produced 2026-06-25 autonomously. |
| How Rome Became the World | shipped | The **sequel** to "Why Rome won" — an HONEST follow-up (NOT a misconception-buster; user: "I am interested in the actual story"). Spine mirrors book one's four pillars, each followed across six centuries until it transforms Rome: allies → Social War → citizenship; army → professionalization → loyalty to generals → Augustus/Empire; the centre → one throne → Third-Century Crisis (Romans vs Romans); absorption → foederati → 376 Danube → Adrianople → the West inherited. 476 = a title quietly lapsing (crown in a box), East endures as "Roman" to 1453. Accent shifts oxblood→imperial purple `#702963`. Folder `rome-became-world/`. Cover + 9 pages + four-pillar synthesis + WHY-quiz + landing card. ZERO regens / ZERO safety rejections across 10 images. Produced 2026-06-26 autonomously. |

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
