# How to update Ownsight

This repo (freeforgood-apps/ownsight) is the source. `index.html` is the whole app. `rebuild.py` (in this repo) refreshes the privacy lock, sets the version and builds `selftest.html` from `index.html`.

## Steps for any change
1. Get the current files from this repo.
2. Edit `index.html`. Keep the app in one file.
3. Run `python3 rebuild.py <new version>` in the repo folder (or `python3 rebuild.py` to refresh the lock only). It refreshes the privacy lock, sets the version in `index.html`, `sw.js` and the self-test, and builds `selftest.html` from `index.html`. `python3 rebuild.py --check` changes nothing and says if the lock, the self-test or the versions are out of date. Never edit the app part of `selftest.html` by hand: it's rebuilt every time. The self-test's own code (the runner) is the last script in `selftest.html`; edit it there, then run `rebuild.py`, which refreshes its copy of the app's logic.
4. Test everything the "Verify" rule in PROGRESS.md lists. Set the toolkit up first (see its README), serve this folder on port 8770, then run the release check. It runs the self-test at 3 sizes and the accessibility checker on the pages listed and each `--click`:
   ```
   bash /tmp/toolkit/release-check.sh . selftest.html 'selftest.html?look' 'selftest.html?look=damaged' 'selftest.html?look=due' 'selftest.html?look=overdue' 'selftest.html?look&pin' --click '#tab-see' --click '#tab-more' --click '#writeStages button[data-stage="thinking"]'
   ```
   The sheets and the screens that need saved thoughts or typed words come from the self-test page with made-up thoughts (`selftest.html?look`). It writes them into the self-test's own storage, never into anyone's real thoughts, and hides the self-test panel. Its options, added after `?look`:
   - `=damaged`, `=due` or `=overdue`: saved thoughts that can't be read, or a backup 9 or 40 days ago (plain `?look` has no backup yet, so the first reminder shows).
   - `&draft` (made-up words in the box, for the card after saving), `&code` (the backup code box, as when copying doesn't work), `&locked` (a password backup pasted, so its password box shows), `&restore` (a plain backup pasted), `&pinon` (the PIN lock on) and `&pin` (the PIN lock on, with the PIN screen showing).

   Then run the accessibility checker on every sheet and state (`L=http://127.0.0.1:8770/selftest.html`):
   ```
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#bkCopy' http://127.0.0.1:8770/index.html
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#recentList button.entry' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#recentList li:nth-child(2) button.entry' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#recentList li:nth-child(3) button.entry' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' --click '#waitGo' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' --click '#waitGo' --click '#sheetBody button.next' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-see' --click '#waitGo' --click '#sheetBody button.next' --click '#sheetBody .actions button.primary' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#recentList button.entry' --click '#sheetBody .actions.sep button:first-child' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#recentList button.entry' --click '#sheetBody .actions.sep button:nth-child(2)' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#writeStages button[data-stage="thinking"]' "$L?look&draft"
   node /tmp/toolkit/a11y-check.mjs --click '#writeStages button[data-stage="planning"]' --click '#undoFeel button[data-feel="lifts"]' "$L?look&draft"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' "$L?look" "$L?look=damaged"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#bkProtect' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#bkRestore' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#wipeAll' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#copyList li:first-child button' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#warnBtn' "$L?look=damaged"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' "$L?look&code" "$L?look&locked"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#bkRestore' "$L?look&restore"
   node /tmp/toolkit/a11y-check.mjs --click '#lockForgot' "$L?look&pin"
   node /tmp/toolkit/a11y-check.mjs --click '#lockForgot' --click '#lockWipe' "$L?look&pin"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' "$L?look&pinon"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#pinSet' "$L?look"
   node /tmp/toolkit/a11y-check.mjs --click '#tab-more' --click '#pinOffBtn' "$L?look&pinon"
   ```
   Those are: the backup code just copied; the full See tab; a thought at Did it; one with Lifts me pressed; one at Planning it; the thought Show me one opens (at Thinking about it); Make a plan; the Undo bar after a move; Edit; the Undo bar after Delete; the card after saving, and with a choice pressed; More with thoughts and copies, and with damaged data; the password box; the restore error; Delete everything and a copy each waiting for a second tap; Bring back a copy; the backup code box and the restore password box; the note before a restore replaces thoughts; Forgot your PIN?, and Erase waiting for its second tap; the PIN card when it's on (with the tip on the backup card); and both PIN errors. Add a line for every new sheet or screen. A `matched nothing` error means the taps changed, so fix the list. Check once that each really opened (its heading, card or message is on the page) before trusting a clean result. Your week only shows from Friday to Sunday, so run the See line on one of those days to cover it. The self-test's own report screen is checked by running the self-test first, so check it by hand (or with axe) after a change to the runner.

   Also run the self-test in a few time zones (puppeteer's `emulateTimezone`), and plant a couple of bugs on purpose in a scratch copy to see them caught.
5. Save the changed files to this repo, plus a new CHANGELOG.md entry, an update to PROGRESS.md, and README.md (a new headless Chrome row at the top of **Tested on**, and any feature or wording change). All files sit flat at the top of the repo, except the tag workflow. They can also be uploaded by hand from a phone.
6. The "Tag new versions" workflow adds the `vX.Y.Z` tag when a new version reaches main. Check its run passed.
7. Open the live site on a real iPhone and do the Done when check in PROGRESS.md.
8. Ask for the self-test to be run on a real iPhone, on the live site (About → Run the self-test), and record the result in CHANGELOG.md, PROGRESS.md and README.md's **Tested on** table.

## Things that must not break
- **The privacy lock.** `index.html` carries a Content-Security-Policy that only lets scripts run whose exact sha256 fingerprint is listed, and blocks every outside request (`connect-src 'none'`). Any edit to a script changes its fingerprint. Always run `rebuild.py` after editing, or the app won't start.
- **Names that never change, or people lose their data.** Small settings use localStorage keys starting `ownsight-v1-` (so far `ownsight-v1-size` for text size, `ownsight-v1-install` for the Home Screen card, `ownsight-v1-pin` for the PIN lock and `ownsight-v1-pinwait` for the wait after wrong tries). Thoughts live in the IndexedDB database `ownsight-v1`, version 1, store `data`: record `state` holds `{ rev, json }` (the save count and the saved data as JSON), record `copies` holds the automatic copies (`[{ day, at, n, json }]`, newest first, at most 3), and records `damaged-<rev>` hold data that couldn't be read, set aside. Windows tell each other about saves on the BroadcastChannel `ownsight-v1` (a number only, never any data). Backup codes start `OWNSIGHT1:`, and backup files are named `ownsight-backup-YYYY-MM-DD.json` (`-locked.json` with a password). A backup is `{ app: "Ownsight", v, saved, thoughts, settings }`, or `{ app, v, saved, encrypted: { v: 1, kdf, cipher, iter, salt, iv, data } }` with a password, where `data` opens to the plain backup.
- **Saved data is version 3** (`{ v: 3, thoughts, settings, backup }`, where `backup` is `{ at: "YYYY-MM-DD" or "", n: changes since then, snooze: "YYYY-MM-DD" or "" }`). Version 2 (0.4.0) had no `backup`; it gets one with each thought counted as a change. Version 1 (0.2.0 and 0.3.0: `entries`, six stages, topics) moves up in `readSaved()` when it's read: Notice, Question and Idea → `thinking`, Plan → `planning`, Do and Check → `did`. Older data is written as version 3 with the next change, never before. A `backup` that doesn't check out starts over, so it never hides any thoughts. Any later change to what's saved gets a new `v` and one more small step in `readSaved()`, tested against saved samples of every older version.
- **Backups always come back.** `fromBackup()` accepts exactly what `readSaved()` accepts, and `makeBackup()` checks each backup restores before handing it out. Restoring builds fresh objects from known fields only, after the toolkit's `parseBackup()` (copied as it is, inside the logic markers). Passwords use PBKDF2-SHA256 (`BK_ITER`, 600,000 rounds, OWASP's number in Nov 2026, stored in each backup so it can rise later) and AES-256-GCM, with a fresh salt and IV every time. A password is never kept: leaving More clears the password boxes and any backup code on screen.
- **Automatic copies** are made from the saved data as it was: when Ownsight opens, and before the first change of a new day (for when it stays open overnight). One a day, the newest 3 kept, none of damaged or newer data. Restoring one doesn't count as a backup.
- **Delete everything** clears only the `data` store of Ownsight's own database and localStorage keys that are `ownsight-v1` or start with `ownsight-v1-`. Never `localStorage.clear()`, never another app's database.
- **Saving stays safe.** A save only goes ahead when the stored `rev` still matches this window's (`dbWrite`), so an out-of-date window can't save over newer thoughts. Every save is read back (`trySave`). Data that can't be read is set aside and never saved over (`hold = "damaged"`), and data with a newer `v` is shown but never saved over (`hold = "newer"`). Nothing can change until the saved data has loaded. `readSaved()` keeps every field, so an older version never trims what a later stage added, and it never copies `__proto__`, `constructor` or `prototype`.
- **The PIN lock is a privacy screen, not encryption.** Only `{ v: 1, salt, iter, hash }` is kept (a salted PBKDF2-SHA256 hash, `PIN_ITER` rounds, the same as backup passwords), never the PIN, and the PIN boxes are cleared after use. A wrong PIN never changes anything: after 5 wrong tries in a row Unlock waits 30 seconds, doubling up to 5 minutes, never longer even if the clock is turned back. The PIN screen is a modal `<dialog>`, so it covers an open thought too and everything behind it is out of reach; Esc can't close it, and if a browser closes it anyway it opens again. It locks before anything else when Ownsight opens (the first thing in "start"), covers the screen at once when Ownsight is left, and asks again after a minute away. Forgot your PIN? erases everything (two taps), then opens the restore part of More. Another window turning the PIN on locks this one; turning it off or deleting everything opens it.
- **The self-test never touches real thoughts.** `rebuild.py` makes `selftest.html` from `index.html` by swapping the line `const PREFIX = "ownsight-v1";` for `"ownsight-selftest-v1"` (so keep that line exactly as it is), giving it its own title, adding a first script that drops only the self-test's own PIN, and adding the runner last. Everything the self-test saves, `?look` included, goes under `ownsight-selftest-v1`. Before changing anything, the runner checks that the app on its page saves under that name, and stops if not. It ends by deleting everything it saved and checking the real `ownsight-v1` settings and database weren't touched.
- **The self-test's standard hooks** stay as they are, so the toolkit's runner works: **Run self-test** is `#st-go`, and the report box `#st-sum` starts with PASSED or FAILED.
- **The logic markers.** The plain functions sit between `// ==== logic: start ====` and `// ==== logic: end ====`, with no screen or storage inside, so tests can pull them out and run them on their own. `rebuild.py` copies them into the self-test's runner (between its `logic copy` markers), and the runner checks them a second way. Keep them that way.
- **The offline cache name** must start with `ownsight-`. The site shares freeforgood-apps.github.io with Till Payday, Study Coach and other apps, and `sw.js` only clears its own caches. Nothing in the app may ever clear storage it doesn't own (no `localStorage.clear()`, no deleting every database or cache).
- **The offline copy is only the app.** `sw.js` saves a page for offline use only when it's the app itself (`./` or `index.html`), so opening another page here (like the self-test) can't replace it.
- **No outside requests.** Fonts are built in (Atkinson Hyperlegible, Bricolage Grotesque, DM Mono, all SIL Open Font License), the same as Till Payday's. Don't add Google Fonts or any CDN. The lock would block them anyway.
- **APP_VERSION** in the app, the version in `sw.js` and the self-test's must match. `rebuild.py` sets them all. The tagging workflow (`.github/workflows/tag-new-versions.yml`, a copy of Best Guess's) reads it to add the version tag, so keep it written as `APP_VERSION = "X.Y.Z"`.
- **Anything from saved data or typing goes on screen as text only,** through the toolkit's `el()` or `textContent`, never `innerHTML`. Backups get checked with the toolkit's `parseBackup()` before restoring.
- **The tab bar is fixed at the bottom.** Page content keeps enough space below it (`.wrap`'s bottom padding and `scroll-padding-bottom`, both from `--bar-h`), so nothing hides behind the bar. If the bar gets taller, raise `--bar-h`. The Undo bar (and the card after saving, which is the same element) sits above it: while it shows, `--undo-h` is set to its measured height (`sizeUndo()`), and what has focus is scrolled clear of it (`keepClear()`).
- **Colors are variables** with light and dark values. After changing one, recompute its contrast in code: 4.5:1 for text, 3:1 for large text, icons and borders that matter.
- **Spoken names match the screen.** A button with an aria-label must include the words on it (WCAG 2.5.3), and every text box needs a label you can see.

## Phone steps
- **Turn on the website** (once): repo **Settings** → **Pages** → under **Build and deployment**, set **Source** to **Deploy from a branch**, branch **main**, folder **/ (root)** → **Save**. Then check **Enforce HTTPS**.
- **Upload files by hand:** repo → **Add file** → **Upload files**.
- **Install it:** open the link in Safari → **Share** → **Add to Home Screen**.

What changed in each version, and how it was tested, is in CHANGELOG.md.
