# The Three Musketeers, Volume II: Milady — handoff

**Updated:** 2026-10-17

This is the one dynamic state file. `tools/status.py` derives state from disk;
this file records what disk cannot: owner decisions, holds, and the next
bounded action.

## Phase

`ADAPTATION` → `SCRIPT_GATE` → `REFERENCES` → `PACKETS` → `PRODUCTION` → `PUBLICATION`

Current: **PUBLISHED (Nano, 2026-10-18)**

## Owner decisions on record

| Date | Decision |
|---|---|
| 2026-10-17 | Batch gate 41–50 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-17 | Page 37: owner's lettering correction (Change only one word in the first line of the prose field: the name Constance must be lettered as one word with even let) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 16: owner's lettering correction (Change only the lettering inside the prose field: re-letter the whole prose field, keeping its position, size and serif ) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 6: owner's lettering correction (Change only the light and weather of the whole scene: it is bright hazy summer NOON on the river road, dry, warm dayligh) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 44: owner's lettering correction (Two changes only. First, the young woman in the white cap lying in the boy's arms wears a plain dove-grey dress with a w) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 50: edit candidate v2 for (Change only the top right of the image: remove the three standing figures in hats on the landing steps, leaving empty we) returned TARGETED; the earlier promotion stands; needs a Claude session. |
| 2026-10-17 | Page 32: owner's lettering correction (Change only the hat of the slim fair-haired Musketeer second from the left: it must be a black hat with ONE white plume,) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 49: owner's lettering correction (Change only the woman kneeling on the raft: her hair must be very pale ash-gold, almost silver-gold, in long loose ringl) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Book created from `notes/NEXT-SESSION-THREE-MUSKETEERS-VOL2.md`: fully autonomous run; slug, parent (three-musketeers-vol1), register "Lantern and Steel" inherited verbatim, no Chronicle pages, cast ceiling 8, returning sheets copied as parents. Publication to Nano waits for the owner's word. |
| 2026-10-17 | Billing: Codex in-app on the ChatGPT subscription (the owner's standing decision of 2026-09-07); `book.toml` carries it. `max_versions = 6`. |
| 2026-10-17 | **Greenlight ① given in advance by the owner** (kickoff prompt). Story presented below and in the session reply; the run goes straight on to the script. |
| 2026-10-17 | Advisor: reset Rochefort after four candidates by making his short square face, compact build, left-only scar, clean moustache-only chin, and all-black costume authoritative over the parent, preserving his unmistakable separation from Athos at page scale. |
| 2026-10-17 | Advisor: Reset `02-athos` around one unmistakable drenched-through-the-chest river state while retaining his approved face, still silhouette and cast separation. |

## The story as greenlit (Phase 0–1, summary)

- **Engine:** a woman nobody suspects comes between four friends who swore all
  for one — and the only one of them who knows what she is has never told
  anyone.
- **Spine:** Milady, the Cardinal's second hand, stages a runaway carriage and
  lets the boy in by her front door; he tells her Constance is hidden in a
  convent in the north; he overhears, sees the lily on her shoulder, and Athos
  tells the story of the wife he hanged. At La Rochelle her poisoned wine
  misses the boy; at the Red Dovecote Athos hears her price (the boy, and the
  girl at Béthune) and takes the Cardinal's blank pardon from her. The four
  win leave by holding the bastion through breakfast; they reach Béthune an
  hour late, and Constance dies in the boy's arms. At a flooded ferry Athos,
  held by the other three, offers Milady his hand and a trial; she chooses
  the river. The Cardinal, handed his own pardon, signs a Musketeer's
  commission with the name blank; the three refuse it; Athos writes the boy's
  name.
- **Movements (57 pp):** I The Lady in the Carriage (1–9) · II The Lily
  (10–18) · III The Red Dovecote (19–25) · IV The Bastion (26–35) · V Béthune
  (36–44) · VI The River (45–51) · VII The Paper (52–57).
- **Cast (8):** d'Artagnan, Athos, Porthos, Aramis, Constance, the Cardinal,
  Rochefort (returning, parents in `refs/parents/`), Milady (new).
- **Cuts:** Milady's whole English half (de Winter, Felton, Buckingham's
  death), Kitty, de Wardes, the executioner of Lille and the night trial, the
  servants, the King and Queen, Tréville. Buckingham does not return.
- **Phase 0 story rulings (delegated authority):** Constance dies, quietly, on
  the page; Milady's end is her own refusal of Athos's hand at the river, off
  image; Athos's hanging of his wife is told once in prose and never drawn in
  use; the ending is the blue cloak. See `00-VOLUME-MANDATE.md`.

## Rulings log

| Date | Ruling |
|---|---|
| 2026-10-17 | Script round 1: REVISE, 16 findings (alive; "the chain of four men in the flood is the image of the book"). All taken; see the round history in `08-FULL-SCRIPT.md`. Round 2 sent to a fresh critic. |
| 2026-10-17 | `09-REFERENCE-PLAN.md` written by a fresh agent (8 characters, 13 boards, 22 plates). References started in parallel with the script gate (characters do not depend on script wording): three detached workers under `notes/three-musketeers-vol2-run-scripts/` (chars1: milady, dartagnan, athos, rochefort; chars2: aramis, constance, porthos, cardinal; plates: the 15 new plates). Logs `qa/_logs/refrun-*.log`. |
| 2026-10-17 | Seven inherited plates relocked as Volume I's approved parents, unchanged, each by a fresh reference critic (all APPROVED, `qa/references/<name>/critic-parent-relock.md`): obj-horse, set-paris, set-house, obj-casket-pouch-ring (critic-only, never attached to a page), set-carmelite-field, set-cardinal-study, set-athos-room. Packet notes from their reports: p8 no handcart by the coach; pp 53–54 the paper and the commission are single sheets in a hand, never one of the desk maps; the other three horses on the road are dark (bay, brown, black), never yellow. |

| 2026-10-17 | Script rounds 2–4: REVISE with 8, 1, 2 findings (all taken; p26 split added the boy's confrontation with Athos, now 58 pages). Round 5 sent. |
| 2026-10-17 | Round 5 APPROVED (findings NONE); three of its notes taken as storytelling gains (the broken promise felt on p36, a hollow "Good." on p26, "half a day ahead"), reopening the gate. Round 6 REVISE, 1 finding (the boy's choice to stay off the page on p26, caused by the added "Good."); fixed. **Round 7: APPROVED, findings NONE — script gate cleared at 7 rounds, 58 pages.** Owner-optional notes from round 7 (not taken; each would reopen the gate): p26 Athos's "But get leave first" could take on the boy's demand; p52's last clause explains; p4 "where the Queen hides that girl"; p27/30 one more line of private bastion talk. p53 staging (Athos hands the paper) goes into the packet. `07-PAGE-CONTRACT.md` generated. |

| 2026-10-17 | Packets: seven fresh writers (one per movement) from `PACKET-SPEC.md` + `WRITER-NOTES.md` + the frame (register "Lantern and Steel", Volume II background rules) into `qa/_assembly/parts/`; concatenated; `assemble.py` 58 pages. `verify.py` clean except inputs not yet locked (02-athos, 07-rochefort, set-bastion, set-north-road, set-bethune-cloister, set-bethune-gate, set-ferry-night, set-ferry-dawn). Every card's C1 carries the tolerances; at most three inputs per page; 30 prompts carry a register-emphasis section. |

| 2026-10-17 | `02-athos` advisor RESET at v4 (hair redrawn straight; the river state made unmistakable); **locked at v5**. `07-rochefort` reached the six-candidate ceiling (advisor RESET at v4 had rewritten ledger §7 toward a square, compact, collar-length man the generator never held). Ruling (owner-delegate, Monkey King III dragon precedent): **relock Volume I's approved Rochefort unchanged** — same character, already gated, and returning readers know this face. First relock critic: REVISE, every finding a sheet-vs-ledger contradiction; ruling: the ledger conforms to the sheet (§7 rewritten: high-cheekboned face of middle length, wavy black hair to the shoulders, upturned moustache, clean chin, gilt furniture; views (a)–(c) only), Athos/Rochefort row restated (beard, colour, plume, posture, scar, height; hair does not separate them), Porthos/Rochefort row added; packets aligned (Rochefort descriptors and a "first three views only, ignore any mark under the lip" sentence on his six attached pages). Fresh critic: **APPROVED** (`qa/references/07-rochefort/critic-parent-relock.md`); promoted. A duplicate Rochefort run started by the chars1 lane was killed before it spent a candidate. |

| 2026-10-17 | Boards: two generated silhouette boards, five adversarial boards, one live pair, plus the driver's heads and crop-and-place boards (the latter superseded by the generated pair). **Whole-cast reference gate APPROVED at round 1 — 40 locks.** `verify.py` CLEAN. Page run launched: `nohup bash notes/monkey-king-vol3-run-scripts/supervise.sh three-musketeers-vol2`, log `qa/_logs/pagerun.log`, `max_versions = 6`. |

| 2026-10-17 | p8 v1–v2 REVISE on C1/C3/C4 (no lettering; a night-rain doorway copied from `set-house`; the boy in a blue cape from his sheet's fourth view). Advisor restage of the prompt source (applies from the next candidate after the running v3): p8 drops the multi-study `set-house` plate (dawn street from words); and on all 33 prompts that attach `01-dartagnan` on pp 1–56 the exclusion "drawn only from the first three views; the fourth view, the blue cassock, is never drawn on this page". |

| 2026-10-17 | Pages 1–10 promoted (p3 v2, p8 v3, the rest v1). **Batch 01–10: sequence, continuity, cold-read all APPROVED.** |

| 2026-10-17 | Pages 11–20 promoted (p11 v2, the rest v1). **Batch 11–20: sequence, continuity, cold-read all APPROVED.** |

| 2026-10-17 | Pages 21–30 promoted, all on v1. **Batch 21–30: sequence, continuity, cold-read all APPROVED.** |

| 2026-10-17 | Pages 31–40 promoted, all on v1. **Batch 31–40: sequence, continuity, cold-read all APPROVED.** |

| 2026-10-17 | p47 v1 came back as Milady's model sheet copied (no text), v2 an invented condolence scene — both REVISE on C1/C2; v3 (full reset) running on the original packet. Advisor restage (Volume I lesson 1, three character sheets → collage): pp 47, 48, 50, 53 cut to two focal sheets (47 drops Milady, 48 drops Aramis, 50 drops the boy, 53 drops Athos — each drawn from words with his or her carriers) and a "one new staged scene, never a model sheet or lineup" line. pp 34 and 44 already promoted with three sheets and passed; left alone. |

| 2026-10-17 | Pages 41–50 promoted (p47 v3 on the restaged two-sheet packet, the rest v1). **Batch 41–50: sequence, continuity, cold-read all APPROVED.** |

| 2026-10-17 | Pages 51–58 promoted, all v1. **Batch 51–58: sequence, continuity, cold-read all APPROVED. All 58 pages promoted; six batches, eighteen gate critics, all APPROVED on the first pass.** Supervisor exited cleanly (rc 0). Whole-book gate next. |

| 2026-10-17 | **Whole-book gate APPROVED, mandatory findings NONE** (`qa/whole-book.md`); the critic's blind retell matched the book end to end. Nonblocking work list → in-generator edits (`notes/three-musketeers-vol2-run-scripts/edits1.sh`, each naming everything that must not move, balloon tails included, and restating the register): p49 Milady's hair dark → pale gold; p32 Aramis wearing a red plume → white; p50 three stray onlookers removed; p44 Constance's apron removed and the stemmed glass made a tumbler; p6 dusk-and-rain → noon (p5 says noon); p16 prose re-lettered with its missing quotation marks; p37 "Con stance" spacing. Not taken (reads fine, composition-level): p58 the boy second from left and his feather; p11/p22 balloon zigzag order (both read). Then `--gates 58` for the touched batches. Reader built in parallel (`index.html`, verifier CLEAN; the new quiz-balance check caught the correct answer longest in 4 of 5 and the builder rebalanced). |

| 2026-10-17 | Edit pass: p49, p32, p44, p6, p16 (quotation marks verified by a fresh narrow transcription), p37 promoted as edits; p50's edit blocked by its critic on an untouched rope coil → advisor override after a one-question check (card clause clarified to "no noose"); the clarified card made packets stale and refused three edits until `assemble.py` was rerun. Regates 01–10, 11–20, 31–40 APPROVED; 41–50 continuity caught p50's edit drifted into glossy photographic realism → regenerated with a register-emphasis section → promoted first try → 41–50 APPROVED. A fresh check found two small hatted figures still on the quay steps on p50: ruled acceptable (they read as Porthos and Aramis holding the chain from the landing, as on p49; every gate approved; a further edit risks the register again). Reader critic APPROVED; its stale zoom placeholder ("The Yellow Horse") fixed in `index.html`; verifier CLEAN. Ship record in `RUN-LOG.md`, journal in `10-PRODUCTION-MEMOIR.md`; method/07 updated (four entries), packet-spec template updated; selftest CLEAN; infra re-frozen, INFRA INTACT. |

| 2026-10-18 | Owner: "commit and push" — **published to Nano**: commit `6f58a9f` (only `.gitignore`, `stories.js` and `three-musketeers-vol2/` staged; nano's other uncommitted work untouched). Publication copy adds the toolbar and ending library links; its verifier requires them and reports CLEAN; pages byte-identical to production; card first on the shelf. Pages run `39142420610` success; live at https://andressolve.github.io/nano/three-musketeers-vol2/index.html (reader 200 with the correct title, pages 1 and 58 200, card first in live `stories.js`). |

## Open holds

NONE

## Next bounded action

Done and published. Volume III (Twenty Years After): paste the kickoff in `notes/NEXT-SESSION-THREE-MUSKETEERS-VOL3.md`. Journal: `10-PRODUCTION-MEMOIR.md` (Part V threads, Part VI publication). Run scripts: `notes/three-musketeers-vol2-run-scripts/`.
