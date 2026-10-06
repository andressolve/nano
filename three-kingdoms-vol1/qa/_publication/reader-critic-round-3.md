# Three Kingdoms, Volume I — reader critic (fresh, zero-history)

Inspected: `index.html` (markup and script traced in full), `pages/page-01.png`…`page-50.png` (present, nothing beyond), `verify-reader.py` output (`CLEAN`). Quiz facts checked against `08-FULL-SCRIPT.md` dialogue only. No prompts, audits, candidates, QA reports, or builder receipt opened.

## Checks

1. **Load / mapping — pass.** With no hash and no saved position the reader opens on Page 1: "The Yellow Sky", "Page 1 of 50", movement "The Peach Garden Oath · The Peach Garden". `fileFor` maps index 0–49 to `pages/page-01.png`…`page-50.png`; `preload` and `loadBookmarks` are bounded to `titles.length` (50).
2. **Navigation — pass.** `#page-1` → index 0; `#page-50` → 49; `#end`/`#page-51` → end state; `#quiz`/`#page-52` → quiz; out-of-range (`#page-0`, `#page-99`) → falls back to the saved position, and the URL is rewritten to the real page. Prev is disabled on Page 1 and Next on the quiz. Space does not move past the end card. Arrow keys are ignored while a radio button has focus, so the quiz radios still work. Swipes are ignored while a dialog is open. The saved position is capped at Page 50, so reloading from the end or quiz without a hash returns to Page 50, and a hash reload keeps the state the hash names.
3. **Contents / bookmarks — pass.** The seven movements cover 1–9, 10–16, 17–22, 23–30, 31–38, 39–46, 47–50: every page appears once, with no gaps or overlaps. Keys are `monte_inspired:three-kingdoms-vol1:page` and `…:bookmarks`. Bookmarks are filtered to 0–49 and disabled on the end and quiz states.
4. **Zoom — pass.** Opens at 150%, centred horizontally at the top of the page. Levels are Fit/125/150/200/250/300, with +/−/0 keys, double-click, mouse-drag pan and native scroll. Prev/next buttons work inside zoom (disabled at Pages 1 and 50), and the bookmark button works inside zoom. It closes with × or Esc. Zoom cannot open on the end or quiz states.
5. **Ending — pass.** Page 50 → the "End of Volume I" card (counter "End") → the quiz (counter "Quiz"). Neither is labelled Page 51. "The story continues in Volume II." is plain text, not a link. The only link points to the quiz, and it is handled in script.
6. **Quiz — one finding (below).** Each question has exactly one correct option. The feedback text matches the script: "That's why they'll chase me"; "Kill him and we are the rebels"; "you'll tell the world… rather betray the whole world"; "before it is cold… still warm"; Yuan Shao's guards claim; "could not see all of his enemies at once". All five questions test a cause or a choice. Answer key is c, a, b, c, a (the letters vary). Length strategies fail: always-longest scores 1/5 and always-shortest scores 1/5. (Always-middle scores 3/5. That is noted, but it is not a requirement.)
7. **Hygiene — pass.** No Monte Cristo or Musketeers terms. No "49" or "of 49" labels (the only "49" is an rgba value). No duplicate IDs. Every `getElementById` target exists.

## Findings

1. **Q3's question is unclear: it can be read as Cao Cao killing his own family, or as the old man killing his.** It reads: "On the road, Cao Cao meets the old man coming home with the wine, after killing his family by mistake." "His" could mean Cao Cao, and "after killing…" sits right after "the old man", so a young reader can take it either way. Both readings get the story wrong. A seven-year-old should not have to untangle the question before answering it. **Fix:** "On the road, Cao Cao meets the old man coming home with the wine. Cao Cao has just killed the old man's whole family by mistake. Why does he kill the old man too?"

## Nonblocking notes

- Shortcut keys ignore Ctrl/Cmd: Cmd/Ctrl+C opens Contents, Cmd/Ctrl+F also toggles full screen, and Cmd/Ctrl+B toggles a bookmark. Suggest returning early when `event.metaKey || event.ctrlKey || event.altKey`.
- Turning pages inside zoom resets the scroll to the left edge (`updateZoomPage(true)` → `scrollTo left 0`) rather than centring, as opening zoom does.
- If the hash is changed to an out-of-range value while reading, the bogus hash stays in the URL. This is harmless.

REVISE
