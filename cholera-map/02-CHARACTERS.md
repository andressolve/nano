# 02 — CHARACTERS

Recurring cast = 3 humans + 1 object-character (the Map). Per the refs-not-prose rule
every one of them gets locked pixels before any page is generated. Locks below never
name the famous figures — the visual is the lock; names live in the script and
filenames only.

## Lock blocks

### SNOW — the physician-detective (~41, throughout)
English physician in his early forties, pale English complexion, high forehead with
receding light-brown hair swept back and thinning at the crown, clean-shaven, deep-set
thoughtful grey-blue eyes, angular serious face with a firm set jaw. Formal dark
frock coat over a high white winged collar and black cravat neatly tied. Lean, composed
build; still, observant posture — a man who watches doorways and faces, not just
patients. Carries a black leather notebook and a physician's bag.

### WHITEHEAD — the second detective (~29, P15–P16, P19)
Young English clergyman in his late twenties, fair English complexion, light-brown hair
neatly parted to one side, clean-shaven, gentle earnest brown eyes, softer and rounder
face than Snow's, an open approachable expression. Black clerical coat, plain white
clerical bands at the collar. Slightly built, warm forward-leaning posture — a man used
to being welcomed through doors, not turned away from them.

### FARR — the rival statistician (~mid-forties, P4–P5, P19)
Respected English statistician and civil servant in his mid-forties, fair complexion,
neat grey-flecked hair receding at the temples, trimmed side-whiskers framing a composed
official face, keen pale analytical eyes, faint permanent furrow of concentration
between the brows. Formal black coat, high stiff collar, government-office bearing —
a man who trusts tables and numbers, upright and unhurried in manner. Often seen with
ledgers and column-ruled paper.

### THE MAP (object-character, P8, P11–P14, P16–P17, P19 inset)
A hand-drawn cream exhibit board: a simplified period street plan of Soho — Broad
Street, Cambridge Street, Poland Street, Berwick Street, Marlborough Street meeting at
odd angles — with small black rectangular bars stacked like tally-marks at every house
where a death occurred, and small circle-and-cross symbols marking the neighbourhood's
public water pumps. The bars are visibly densest and tallest in a tight cluster around
ONE pump on Broad Street, thinning outward with distance. Ink on cream paper, ruled
margin, a small hand-lettered title. Never shown "solved" with an added ring or arrow
until after the reveal pages — see 01-STYLE-GUIDE §5 for the annotated/unannotated pair.

## Master cast plate — ONE single generation

`refs/ref_cast_plate.png` — 1536×1024, `generate_image`, quality high.

Prompt skeleton (final assembly at production): STYLE BLOCK + REGISTER GUARD + —
> Character reference plate, four subjects in a row against a plain warm parchment
> background, museum-lineup style, each subject large and clearly lit, thin hand-written
> name label below each. From left: (1) [SNOW lock]; (2) [WHITEHEAD lock]; (3) [FARR
> lock]; (4) [THE MAP lock], shown upright on a low wooden easel at true relative scale.
> Faces LARGE and readable; three-quarter view; neutral expressions. No text other than
> the four name labels.

Casting gate: age right (Snow visibly older/more severe than Whitehead), era right
(1850s English dress, not later Victorian), realistic, distinct (Snow's gaunt watchful
stillness vs. Whitehead's open warmth vs. Farr's official composure must read
differently at a glance). Register matches §1. The Map must clearly show the pump
cluster pattern even at plate scale.

## Solo refs (after plate passes, each anchored on the plate via imagePaths)

| File | Content |
|---|---|
| `refs/ref_snow.png` | Snow, portrait + full body, parchment bg |
| `refs/ref_whitehead.png` | Whitehead, portrait + full body |
| `refs/ref_farr.png` | Farr, portrait + full body |

## Map exhibit plates (PIL-built, not generated — see 01 §5)

| File | Content |
|---|---|
| `refs/plate_map_full.png` | Fully labeled map: streets, pump symbols, death-bar cluster, title |
| `refs/plate_map_unannotated.png` | Same map, pump positions marked, no explanatory ring/arrow — for the P11 reader-race page |
| `refs/plate_map_solved.png` | Same map with the discovery ring around the Broad Street pump added, for post-reveal pages |
| `refs/plate_cesspool_diagram.png` | Cross-section diagram: the well shaft and the leaking cesspool three feet apart, labeled |
| `refs/plate_grand_experiment_table.png` | Simple two-column table: Southwark & Vauxhall (315/10,000) vs. Lambeth (37/10,000) |

## Incidental (prose-only allowed — single-page walk-ons)

The Vestry Board of Guardians (P12: half a dozen anonymous mid-Victorian gentlemen in
dark coats around a table, no named faces). Brewery workers and workhouse residents
(P9: anonymous figures, work clothes, tankards/institutional dress — never named or
given recurring faces). Susannah Eley, the Hampstead widow (P10: an elderly woman
glimpsed at a cottage doorway, prose-only, no ref — handled with the same dignity as
any incidental elderly figure, no illness depicted). Baby Frances Lewis and Constable
Thomas Lewis (never rendered as characters at all — represented only by a closed door,
a black ribbon on a knocker, and a name in a written register; see 01-STYLE-GUIDE §8).
Filippo Pacini (P19 inset only: distant silhouette at a microscope in a sunlit Florence
room, no close-up face required).
