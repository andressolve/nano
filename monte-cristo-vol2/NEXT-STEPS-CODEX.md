# Next steps for Codex — Monte Cristo Volume II

> **Superseded as a resume prompt on 2026-08-20.** This file stops at Page 15.
> Current state and the efficient Pages 32–49 orchestration are in
> [`HANDOFF.md`](HANDOFF.md) and [`SESSION-START.md`](SESSION-START.md).
> Keep this file as historical evidence; do not execute its session blocks.

Written 2026-08-16, replacing the earlier version of this file (page 10 has since
been promoted at v4 and both due gates have run). Paste the relevant block into a
Codex session started in
`/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/`.

## Where the run actually is

- **15 pages promoted** (`pages/page-01.png` … `pages/page-15.png`).
- Page 10 was re-promoted at **v4** (`69339f925a84`) after the pages 1–10 batch
  sequence gate caught Albert in a pale travel coat. The ledger carries both the
  v2 and the v4 row; that is correct, do not collapse them.
- The pages 1–10 **batch sequence gate** and **blind cold read** have both run —
  `qa/batches/batch-01-10.md`, `qa/cold-reads/cold-read-10.md`.
- `qa/production-ledger.md` is current through page 15.
- **`RUN-LOG.md` is stale.** Its page table stops at page 10 and still names page
  10 v2 as "the resume point." That is now false.

---

## ⚑ Two changes to how you run, effective immediately

These are the only method changes. Nothing about the gates, the roles, the
transcription test or the v4 ceiling has moved.

### 1. Work from `qa/_plan/page-NN.md`. Do not open `12-PRODUCTION-PLAN.md`.

`assemble.py` now emits, in the same pass that builds the master plan, one
self-contained file per page in `qa/_plan/`. Each carries the **identical**
sections 1–4, the identical section 6 briefs, the identical sections 7–10, plus
that one page's prompt and that one page's appendix — and nothing else.

The master plan is ~135K tokens. A per-page file is ~17K. They cannot drift,
because one script writes both, and `verify.py` now fails if `qa/_plan/` is
missing, short, stale, or leaking a neighbouring page's prompt.

The master file stays as the owner's reading copy and as the edit target for
sections 1–4. **Production never opens it.**

### 2. One session per page, per role. Not one per ten-page batch.

Start a fresh Codex session at every page boundary. An agent session re-sends its
whole accumulated context on every turn, so a session that spans ten pages pays
for page 14's transcript again while working page 23.

Nothing is lost by restarting. Every piece of state this run depends on is on
disk: `qa/production-ledger.md`, the per-page `critic-vK.md` reports, the
promoted bytes in `pages/`, and `RUN-LOG.md`.

**Why both changes exist.** On 2026-08-16 three long-running sessions consumed
**334 million input tokens in one day** against 21 generated images. The images
were roughly three percent of the spend. The other ninety-seven percent was the
same 135K-token plan being re-read on every turn of every session.

---

## Session A — backfill `RUN-LOG.md` (model: `gpt-5.6-luna`)

Bookkeeping only. Generates nothing, promotes nothing, judges nothing.

> You are updating the run log for The Count of Monte Cristo, Volume II, in
> `/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/`. This session
> generates no images and promotes nothing.
>
> `RUN-LOG.md`'s page table stops at page 10 and still records page 10 as
> promoted "not yet". Bring it current through the last promoted page.
>
> 1. Read `qa/production-ledger.md` and, for each page from 10 onward, the
>    `qa/production/page-NN/critic-v*.md` reports.
> 2. Append one row per page to the table in `RUN-LOG.md`, in the existing
>    column order: Page | Mode | Cands | Reports | Promoted | REVISE reasons, in
>    order | Cat. `Cands` is total images generated from v1 and never resets.
>    `Reports` is critic verdicts on record. The REVISE-reasons column takes the
>    actual mandatory findings, in order, not a summary.
> 3. Correct the page 10 row: it promoted at **v4**, not "not yet", and the extra
>    two generations were caused by the batch gate catching Albert's pale travel
>    coat. Add the v4 row alongside rather than rewriting history.
> 4. Delete the stale paragraph asserting that page 10 v2 is the resume point,
>    and replace it with the true current position.
> 5. Do not edit any entry above the page table. That file's own rule is that
>    past entries are never revised — corrections are appended.
>
> Then run `python3 qa/_assembly/verify.py` and report its output verbatim.

## Session B — resume production (model: `gpt-5.6-sol`)

**One page. Then stop and start a new session for the next page.**

> You are the production lead for The Count of Monte Cristo, Volume II, in
> `/Users/andresrodriguez/Documents/nano/monte-cristo-vol2/`.
>
> Work page **[N]** and only page [N]. When page [N] is promoted, stop. The next
> page gets its own session.
>
> **Open `qa/_plan/page-[NN].md`. Do not open `12-PRODUCTION-PLAN.md`** — it is
> the same law repeated for forty-nine pages and costs about eight times as many
> tokens to hold. Your per-page file carries identical sections 1–10 plus this
> page's prompt and appendix.
>
> Run the loop exactly as §6 of that file describes: the builder generates one
> candidate and submits it unchanged; an independent critic in a separate context
> transcribes the 600 × 900 proof with the script closed and returns APPROVED or
> REVISE; you promote bytes only on an unconditional APPROVED.
>
> Standing rules that have not changed:
> - The builder never gates its own work. Every completed candidate goes to the
>   critic, including ones the builder dislikes.
> - **Measure nothing.** Do not state the rendered size of any panel, prose
>   field, balloon or letterform, and never compare a rendered page against a
>   number in the prompt. The percentages and pixel values in the prompt are
>   steering values for the image generator, which never hits them and always
>   undershoots. Hierarchy is judged by eye, yes or no. Reading is judged by
>   transcription.
> - A v4 ceiling stops the run and comes to the owner. The count is total
>   generations from v1 and never resets.
> - Never edit `07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`.
> - Image generation is the built-in Codex/ChatGPT subscription path only. Do not
>   call the OpenAI API or `~/.codex/skills/imagegen/`.
>
> Update `qa/production-ledger.md` and append the page's row to `RUN-LOG.md`
> before you stop. Then run `python3 qa/_assembly/verify.py` and report it.

## Gates falling due

The pages **11–20 batch sequence gate** and the **blind cold read at page 20**
fall due once page 20 is promoted. The cold read must be run by an agent that has
**not** read the script — contamination is irreversible, so give it its own fresh
session and hand it nothing but the brief and the promoted pages.

## If you edit any rule

`12-PRODUCTION-PLAN.md` is a build artifact from `## PAGE 3` onward. Never
hand-edit sections 5–10 in it. Edit the fragment in `qa/_assembly/`, or
`10-CRITIC-OPERATIONS.md` for the role briefs, then run:

```
python3 qa/_assembly/assemble.py && python3 qa/_assembly/verify.py
```

Sections 1–4 are hand-editable directly in `12-PRODUCTION-PLAN.md`; `assemble.py`
reads them back off disk each run. Either way the per-page files are regenerated
in the same pass, so a correction reaches the executor. **A correction is not
landed until it is in the file the thing doing the work actually opens.**
