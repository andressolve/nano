# Pre-production context map

Status: LOCKED

## Authority

Reads: owner purpose; locked adaptation; locked full script; locked page contract; recorded owner approvals
Writes: authority receipts only
Never reads: unprotected source-fidelity arguments
Never does: lower or rewrite owner-controlled authority

## Script builder

Reads: locked adaptation; story architecture; graphical direction; current script and contract drafts
Writes: full script; page contract
Never reads: generation prompts; reference artifacts; critic history
Never does: approve its own work; generate images

## Readability critic

Reads: complete full script; complete page contract
Writes: readability report
Never reads: builder history; research; sources; references; generation prompts; rejected candidates
Never does: rewrite the script; approve after rereading is required

## Packet builder

Reads: one script page; matching contract page; graphical direction; approved page binding map
Writes: one page intent; one builder prompt; one critic card
Never reads: neighboring page bodies; research; sources; rejected history
Never does: change story authority; copy builder context into critic context

## Casting and reference builder

Reads: casting ledger; setting and object ledger; graphical direction; reference plan; approved anchors
Writes: reference candidates; methods; hashes
Never reads: generation history from rejected references
Never does: edit story authority; approve outputs; generate story pages

## Reference critic

Reads: neutral reference artifacts first; then casting ledger; setting and object ledger; reference plan; reference gate
Writes: reference report
Never reads: reference generation prompts; builder audits; rejected history
Never does: edit; generate; promote

## Production orchestrator

Reads: clean gate receipts; owner production approval; compact handoff; current page packet
Writes: deterministic packets; ledger; promotion receipts; dynamic handoff
Never reads: research; sources; whole script; neighboring packets; rejected art
Never does: judge art; rewrite story authority; generate images

## Handoff boundary

Reads: disk state only
Writes: paths; hashes; verdicts; page count; packet digest; holds; next bounded action
Never reads: task transcripts
Never does: carry hidden context across tasks
