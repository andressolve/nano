# References run — Phase 3, driven by `tools/refrun.py`

**Book:** Monkey King, Volume I: Havoc in Heaven · `books/monkey-king-vol1/`
**Scope:** generate, criticize, and lock the reference system (nine character
sheets, six boards, twelve plates), then clear the whole-cast reference
gate. **No story page is generated in this phase.**
**Image path:** Codex's built-in image generation on the ChatGPT
subscription, recorded in `book.toml`. No API key, no image CLI, no
separately billed path anywhere in this phase.

Nobody pastes anything. The orchestrator is a script.

## One command

```
python3 tools/refrun.py monkey-king-vol1 --all
```

runs the whole phase: character sheets in the plan's order, the two
deterministic boards, the four generated boards, the twelve plates, then the
gate. It stops on an owner hold and says why; fix the hold, rerun the same
command, and locked sheets are skipped. `python3 tools/refrun.py
monkey-king-vol1 01-wukong` runs one sheet. `--gate` runs the gate only.
`--hold-on-revise` stops after any REVISE instead of applying the
prescription. `--dry-run` prints the calls and generates nothing.

## What happens per candidate

1. `tools/refbrief.py` writes two briefs under `qa/references/<sheet>/`
   from disk state: the builder brief with the exact prompt from
   `09-REFERENCE-PLAN.md` (register paragraph and anti-collision clause
   substituted verbatim), the anchor inputs the manifest names (approved
   files only), the output paths, the audit rules, the submit rule; and the
   critic brief, which names only the candidate, the approved sheets, and the
   report path, and never mentions a version, a prompt, or an audit.
2. **Builder**: a fresh, ephemeral `codex exec` process (default model
   `gpt-5.6-luna`) told one line: read the builder brief and do exactly what
   it says. It generates once with the built-in image tool, saves the PNG
   byte for byte to `refs/candidates/<sheet>-vK.png`, saves the issued
   prompt beside it, writes a non-gating audit, and exits. It never judges,
   never regenerates on its own opinion, never reads the plan or the ledger.
   The driver refuses the candidate if it is not a 1536 × 1024 PNG.
3. **Critic**: a second fresh, ephemeral `codex exec` (default `gpt-5.6-sol`)
   told one line: read the critic brief and do exactly what it says. Two
   stages per `method/03-CASTING-AND-REFERENCES.md` §4: the candidate
   against the approved sheets under adversarial conditions, then against
   the ledger. Writes `qa/references/<sheet>/critic-vK.md` with a verdict
   line, a collision matrix, mandatory findings with exact structural
   requirements, and nonblocking notes.
4. **Verdict**, read by the driver from the report's first line.
   `APPROVED` → `tools/refs.py promote`, byte-identical copy to
   `refs/approved/`, hash in `qa/reference-ledger.md`.
   `REVISE` → a third fresh `codex exec` applies the critic's exact
   prescriptions to that sheet's block in `09-REFERENCE-PLAN.md`, changing
   nothing else; the diff is saved as `prescription-vK.diff`. If a
   prescription would change a trait in the ledger's structural lock or
   Never list, the applier replies `HOLD` and the sheet stops for the owner.
   Otherwise the loop continues to v(K+1).
5. **Ceiling**: four candidates per sheet, total, never reset. A fourth
   REVISE is an owner hold. `refbrief.py` refuses a fifth.

Every verdict appends a line to `RUN-LOG.md`. State is on disk;
`python3 tools/status.py monkey-king-vol1` reads it.

## Boards and plates

- `board-heads` and `board-silhouette-grayscale` are assembled by
  `tools/boards.py` from approved pixels, promoted with a machine report
  that says so, and never generated.
- The four generated boards (`adversarial-subhuti-laozi`,
  `adversarial-wukong-old-ma`, `adversarial-emperor-laozi`,
  `live-pair-wukong-old-ma`) and the twelve plates go through the same
  loop, with the two named approved sheets attached as inputs for boards
  and none for plates. Their critic briefs point Stage 2 at the pair's
  collision-matrix row (boards) or at `05-SETTINGS-AND-OBJECTS.md` (plates).
- All board names carry `board`, `adversarial`, or `live-pair`, so
  `imagegen.py`, `verify.py`, and `refbrief.py` refuse them as generation
  inputs for pages later.

## The gate

After everything is locked, the driver writes `qa/references/gate-brief.md`
and runs one more fresh critic on the entire `refs/approved/` folder as a
system, per §4 of the casting method. It writes
`qa/references/reference-gate.md`. On REVISE, the named sheets go back
through the loop from their next version number. On APPROVED, Phase 3 is
done and the next step is Phase 4 packets, in a Claude session.

## Holds: the advisor decides. The owner does not.

The owner's standing directive (2026-09-02): he makes no character, design,
or story-mechanics decisions during a run. His priorities are, in order,
**great storytelling** (no gaps, engaging for the two readers) and **no
speech-bubble or lettering errors**. Everything below that is delegated.

When a sheet would stop — an applier HOLD, an applier that changed nothing,
a report with no verdict line, or the fourth candidate REVISE — the driver
spawns a fresh **advisor** (strong model) with that delegated authority. It
reads the reports, the ledger, and the prompt block, then edits: it may
clarify or amend the ledger's lock, redesign a trait for distinctness, adapt
a prescription, or at the ceiling rewrite the sheet's prompt block cleanly
and grant two more candidates. It keeps what the character is for the
story. Every ruling is one row in the decisions table in `HANDOFF.md` and a
saved diff (`advisor-vK.diff`). The run continues.

The driver stops only for things that are not decisions: a tool failure, an
exhausted subscription, a missing file. Those it names and exits.

## Where to look

- Candidates and issued prompts: `refs/candidates/`
- Locks and the hash ledger: `refs/approved/`, `qa/reference-ledger.md`
- Per-sheet briefs, replies, reports, prescription diffs:
  `qa/references/<sheet>/`
- The gate: `qa/references/reference-gate.md`

A critic report that mentions a version number, a prior candidate, or what
the builder changed has seen something it should not have; that is worth a
look at the brief that produced it.
