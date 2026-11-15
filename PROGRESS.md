# Ownsight: progress

New chat? Read this first, then how-to-update.md before editing anything. The steady brief comes first; the changing status is at the bottom.

## What it is

A free web app that helps each person understand themselves and what it means for their life, in the most straightforward way. Write what's on your mind and tap where it's at: **Thinking about it**, **Planning it** or **Did it**. That one tap saves it. Then, if you like, tap whether it **lifts you** or **weighs on you**. Each thought moves along as you make a plan and do it. The See tab shows, in plain counts, where your thoughts sit, what lifts you and what weighs on you, and which thoughts are waiting for a plan, with a look back at your week from Friday to Sunday. Backups (a file or a code, with an optional password) and automatic copies keep the thoughts safe, with gentle reminders. An optional PIN lock hides it on a shared phone, and a self-test anyone can run checks it works in their own browser.

## Ground rules

- **Free forever.** No ads, accounts, tracking, paid services or AI. Everything stays on the device. No entry text is ever sent anywhere, to AI or anyone else. The person does the interpreting, helped by good prompts and their own numbers.
- **A mirror, not a diagnosis.** Patterns are shown as plain counts in the person's own terms ("8 of your 12 thoughts are still at Thinking about it"), never as a type or a label. Small numbers say they're only a first look. It's not therapy, a clinical test or professional advice, and the app says so.
- **Each person, for themselves.** Nobody, including the owner, ever sees anyone else's entries or results. There is no sharing feature.
- **Anonymous.** The only public identity is freeforgood-apps. No real names, personal emails, locations, links to Claude chats or Claude page IDs in the code, commits or this repo. Commits use the account's private GitHub noreply address as the author and keep Claude's default committer, so GitHub shows them as Verified. Commit in UTC. Leave out the Claude session link line tools may suggest adding, and check the message (`git log -1 --format=%B`) before pushing. Every push goes through the toolkit's push-check.
- **Plain, warm, simple wording,** around a 6th to 8th grade reading level, for anyone, including people having a hard day.
- **Feedback** goes to freeforgood-apps+ownsight@proton.me.
- **Verify before handing anything over:** parse-check, run it in a browser, test awkward cases (empty data, old saved data, undo, small phone screens, dark mode), check nothing else broke, and do the math in code. Then say what was checked and what couldn't be.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- **Web address (never changes):** https://freeforgood-apps.github.io/ownsight/ (GitHub Pages, from main, / (root)).
- **Names that never change,** or people lose their data:
  - Saved data: IndexedDB database `ownsight-v1` (version 1, store `data`, record `state` = `{ rev, json }`; record `copies` = the automatic copies; data that couldn't be read is set aside as `damaged-<rev>`). Small settings: localStorage keys starting `ownsight-v1-` (text size, the Home Screen card, the PIN lock and its wait). Windows tell each other about saves on the BroadcastChannel `ownsight-v1`.
  - Offline cache names start with `ownsight-`.
  - The self-test's own storage: database, settings and BroadcastChannel `ownsight-selftest-v1`, never `ownsight-v1`.
  - Backup codes start with `OWNSIGHT1:`. Backup files are named `ownsight-backup-YYYY-MM-DD.json` (`-locked.json` with a password), and say `app: "Ownsight"` inside.
- **Shared address:** freeforgood-apps.github.io is shared with Till Payday, Study Coach and the other free apps. Every key, database and cache name keeps the `ownsight-` prefix, and nothing ever clears storage it doesn't own.
- **Files** (Till Payday's layout, flat at the top of the repo): `index.html` (the whole app), `sw.js`, `manifest.webmanifest`, the icons, `rebuild.py`, `README.md` (toolkit README outline), `CHANGELOG.md`, `how-to-update.md`, `SECURITY.md` and `.gitignore` (toolkit Baseline kit), `.github/workflows/tag-new-versions.yml` (copied unchanged from Best Guess), and `selftest.html`, which `rebuild.py` builds from `index.html` (the runner's source is its last script).

## How it works: the remake (0.4.0, Nov 14, 2026)

The owner asked for a remake, rethought from the goal: simpler to understand and use, and straightforward. The hardest parts were picking 1 of 6 stages and too much on Patterns. The owner approved a mockup of the screens below (a private design canvas, not linked here), and 0.4.0 builds them.

### Three tabs, at the bottom: Write, See, More

1. **Write** (the app opens here)
   - One box, "What's on your mind?", then "Where is it at? Tap one to save it." and three big buttons with short hints: **Thinking about it** (On my mind, no plan yet), **Planning it** (I know what I'll do), **Did it** (Done, or doing it now). The tap saves.
   - Right after saving, a card above the tabs: "Saved as Thinking about it." with **Undo**, and "Does it lift you or weigh on you?" with **Lifts me** and **Weighs on me**, then "Optional. Skip it if you're not sure." It's the Undo bar with the question added, and it stays about 20 seconds.
   - **Recent** under the box, newest first. Tapping a thought opens it.
   - **Backup reminder** (0.5.0), a card under the box when it's time, with **Back up now** and **Later**. The Add to Home Screen card waits while it shows.
2. **A thought, opened** (a sheet): its words, its stage and since when (plus when it was written, once it has moved), the lines written when it moved along ("Your plan", "How it went"), then **Next step**, one big button. At Thinking: **Make a plan** ("What will you do about it?"), plus **I already did it**. At Planning: **I did it** ("How did it go?"). Each asks for an optional line, then moves the thought along. At Did it, there's no next step. Lifts or weighs can be set, changed or cleared here. Then **Edit** (the words) and **Delete**, each with Undo.
3. **See** (plain counts, from 5 thoughts; before that, one line: "3 of 5 so far")
   - "From your 12 thoughts", a headline from the biggest stage ("You do a lot of thinking.", "You make a lot of plans." or "You get a lot done."; a tie: "Your thoughts are spread out."), the count ("8 of your 12 thoughts are still at Thinking about it."), one bar in three parts, and a key with the counts.
   - **What lifts you, and what weighs on you:** how many of each and the newest 3, then "What do the ones that lift you have in common?" Shows once at least one thought has been tapped.
   - **N thoughts are waiting for a plan** (those at Thinking) with **Show me one**, which opens the oldest one at Thinking.
   - **Your week,** at the top from Friday to Sunday (the person's own time): the last 7 days, "You wrote 9 thoughts and did 2 of them", what lifted you and what weighed on you, and "What would you like more of next week?" (nothing to fill in). Only when there's at least one thought that week.
   - "Just counts from your own thoughts. A mirror, not a diagnosis."
4. **More** (0.5.0): **Back up your thoughts** (Save a backup file, Copy backup code, an optional password), **Restore a backup** (choose a file or paste a code; two taps when it would replace thoughts, with Undo), **Automatic copies** (the last 3 days, two taps to bring one back, with Undo), **Lock with a PIN** (1.0), text size, Add to Home Screen, About (with **Run the self-test**, 1.0), and **Delete everything** (two taps).
5. **The PIN screen** (1.0, when the PIN lock is on): Ownsight's name, "Enter your PIN", **Unlock**, and **Forgot your PIN?**, which explains that the only way in is to erase everything here and offers **Erase and start over** (two taps). It covers everything, an open thought too.
6. **The self-test** (1.0, `selftest.html`): the app on its own storage with a panel at the bottom: **Run self-test**, then a report (passed or what failed, the browser and what it can do) to copy or email.
7. **Beside the name** (0.5.0): "No backup yet" or "Backed up 3 days ago", in place of "Saved on this device" once there are thoughts, and never in place of a note that saving has stopped. Tapping it opens the backups.

### What it saves (data version 3)

```
{
  v: 3,
  thoughts: [{
    id, text,
    stage: "thinking" | "planning" | "did",
    feel: "lifts" | "weighs" | null,
    at,                            // when it was written (ISO time)
    steps: [{ stage, at, note }]   // each move along, with its optional line
  }],
  settings: {},
  backup: { at, n, snooze }        // the day of the last backup ("" for none), changes since, the day Later waits until
}
```

Version 3 (0.5.0) adds `backup`. Version 2 data gets one with each thought counted as a change, so the first reminder comes soon.

The database, the record layout, the save count, the read-back and the damaged and newer rules all stay; only what's inside `json` changes. Moving up from version 1 (0.2.0 and 0.3.0, test thoughts only): each entry becomes a thought, with Notice, Question and Idea → thinking, Plan → planning, and Do and Check → did. `feel` starts empty and `steps` start empty. Topics, `from` links, `profile` and `bigFive` go. A 0.3.0 window left open sees version 2 as newer and won't save over it. Limits: 1,000 characters for a thought or a note, and 10,000 thoughts.

### Stages (one build chat each, each ending verified, saved here and recorded below)

1. **Shell:** done (0.1.0).
2. **The first thinking loop:** done (0.2.0 and 0.3.0), now replaced by the remake.
3. **The remake:** done (0.4.0): the screens above, version 2 data and the move up from version 1.
4. **Safety net, part 1:** done (0.5.0): automatic copies, backup file and code (optional password), two-tap restore (also when saved data can't be read), backup reminders, Delete everything, and a fuller About.
5. **Safety net, part 2:** done (1.0.0): the optional PIN screen, the self-test (and its link in About) and the first release.

**Ideas for later** (offered to the owner, not chosen): a 3-minute personality check (20 public-domain IPIP statements, shown as five plain sentences, never a type), and one question a day.

## Security plan (from the plan review)

- **Worth protecting:** people's private thoughts and what they show about them. **Risks:** data lost, someone holding the phone, a booby-trapped backup code or file, a bug in another app on the shared address.
- **Built in from the start:** the privacy lock (`default-src 'none'`, `connect-src 'none'`), every entry shown as text only through `el()`, backups checked with `parseBackup()` and a size cap before restore, a password option on backups, an optional PIN screen (1.0, Till Payday's: it hides the app on a shared phone and doesn't encrypt; only a salted PBKDF2 hash of the PIN is kept; a wrong PIN never wipes anything), backup passwords with PBKDF2-SHA256 and AES-256-GCM (Web Crypto only; a wrong password never changes anything; a forgotten one can't be recovered), a generic page title with no entry text in titles or link previews, built-in fonts only (no Google Fonts), and the `ownsight-` prefix on every name.
- **Avoid:** any outside request, AI feature or analytics, and anything that clears storage it doesn't own.

## Decisions

Why some things are the way they are, so nobody "fixes" them by mistake:
- **The PIN lives in a device setting** (`ownsight-v1-pin`, 1.0), not in the saved data or backups, like Till Payday's. It can lock before the thoughts load, and it belongs to this phone, so a backup restored elsewhere never brings a PIN along. `settings` in the saved data stays empty, kept for later.
- **The PIN screen is a modal dialog** (1.0), so it sits above an open thought (itself a modal dialog) and everything behind it is out of reach for taps, the keyboard and VoiceOver. Esc can't close it, and if a browser closes it anyway, it opens again. Unlocking puts you back where you were.
- **Leaving covers the screen at once; a minute away asks again** (Till Payday's timing). Back sooner, the cover goes by itself.
- **The wait after wrong tries is said once, not counted down** (1.0), since VoiceOver would read every second. It never lasts more than 5 minutes from now, even if the phone's clock is turned back. Typing again after it's over lets Unlock work right away.
- **The PIN uses the same rounds as backup passwords** (600,000, `PIN_ITER`), and each PIN keeps its own count, so it can rise later. There's no step yet to re-save older PINs with more rounds, since there aren't any (Till Payday has one).
- **Turning the PIN off needs the PIN; changing it is off, then on.** Another window turning it on locks this one; turning it off, or deleting everything, opens it.
- **Forgot your PIN? erases everything (two taps), then opens Restore a backup** (1.0). Erasing only happens if deleting works; otherwise the PIN screen stays and says so.
- **Backups while the PIN is on: a short tip, not a forced password** (Nov 14, 2026, the owner's choice). The PIN card and the backup card say the PIN doesn't cover backups and suggest a password. Backups stay quick, and a forgotten password can't lose a backup nobody chose to protect.
- **The self-test is built from the app** (1.0): `rebuild.py` makes `selftest.html` from `index.html` on its own storage (`ownsight-selftest-v1`), so it always tests the app as it ships. The runner's source is the last script in `selftest.html`, and its copy of the logic is refreshed from `index.html` every build. It drops its own PIN when it opens, so its Run button can always be reached, and it checks it's on its own storage before changing anything.
- **The self-test checks locking through the same lock another window's PIN uses** (it can't reopen itself mid-run). Ownsight locking when it really opens is checked in headless Chrome and on the owner's iPhone.
- **`selftest.html?look` replaced the seed and draft pages** (1.0). It writes made-up thoughts into the self-test's own storage, never real ones, so it's safe to publish, and the accessibility checker can reach every sheet with taps alone.
- **The self-test link opens in a new tab,** like Till Payday's.
- **The safety net in two chats** (Nov 14, 2026, the owner's choice): backups, copies, reminders and Delete everything first (0.5.0), then the PIN screen, the self-test and 1.0.
- **A PIN screen, not an encrypted lock** (Nov 14, 2026, the owner's choice): the same as Till Payday's, so it hides the app on a shared phone without encrypting the thoughts. A forgotten PIN means restoring a backup or starting over, never losing thoughts to a forgotten password.
- **The backup record lives in the saved data** (version 3), like Till Payday's, so it travels with saves between windows. Backups leave it out, since it's about this device. Moving up from version 2 counts each thought as a change, so someone with thoughts but no backup gets the first reminder soon.
- **Every backup is checked to restore before it's handed out,** and restoring accepts exactly what saved data accepts (no extra limits), so anything Ownsight can hold can always come back. parseBackup()'s 5,000,000-character cap bounds it. A backup bigger than that is refused with a plain message; it would take thousands of very long thoughts.
- **Backup passwords use 600,000 PBKDF2 rounds** (OWASP's number, checked Nov 2026). Till Payday uses 250,000. Each backup stores its own number, so it can rise later without breaking old backups.
- **Copies are made from the saved data as it was:** when Ownsight opens, and before the first change of a new day, since a Home Screen app can stay open overnight. Not of damaged or newer data, and not again when nothing changed since the newest copy.
- **Restoring a copy doesn't count as a backup** (it's only on this device), so reminders keep counting. Restoring a backup counts as backed up today, like Till Payday.
- **Two taps only when something would be replaced.** With no thoughts, or when saved data couldn't be read, one tap restores. The first tap on Restore says what's in the backup and how many thoughts it replaces, and waits 8 seconds (other second taps wait 5), so there's time to read it. Every restore over thoughts has Undo.
- **Nothing is backed up or restored over data from a newer Ownsight,** or data that couldn't be opened. Updating, or Try again, comes first. An empty backup can't be made.
- **Leaving More clears the backup code on screen and both password boxes,** so nothing about a backup stays on a shared phone.
- **Copying a code asks the clipboard right away** (with the code to follow), so a password's half-second of work doesn't lose the tap on iPhone. If copying doesn't work, the code shows to copy by hand, like Till Payday.
- **Delete everything clears Ownsight's own store and settings only,** and other windows pick it up and can't bring anything back.
- **The remake** (Nov 14, 2026, the owner's choice): rethought from the goal to be straightforward. Three stages in plain words (Thinking about it, Planning it, Did it), and one tap saves.
- **A thought moves along** (Thinking → Planning → Did it) instead of making new linked thoughts, so there's nothing like trails to follow.
- **Lifts me or weighs on me** (Nov 14, 2026, the owner's choice of the simplest way to learn more about yourself). It's optional and comes right after saving, so saving stays one tap.
- **Your week shows from Friday to Sunday** (Nov 14, 2026, the owner's choice), so it feels like a small end-of-week ritual.
- **Show me one opens the oldest thought at Thinking** (kept from 0.3.0, now "waiting for a plan"). It opens the thought itself, so it can be read first.
- **Edit fixes the words only** (0.4.0). Where a thought is at changes only by moving it along, and only forward, so its steps always match its stage. A wrong tap when saving is caught by the Undo right after.
- **The card after saving is the Undo bar with the question** (0.4.0). It stays 20 seconds (other Undo bars 10), longer while it has focus, so there's time to read and answer. Focus moves into it, so keyboard and VoiceOver users reach Undo and the question right away. Answering keeps it showing, so Undo is still there.
- **Your week counts what was written in the last 7 days, today included,** in the person's own time, and "did" means how many of those are at Did it now. A week with none done just says how many were written, never "did 0", for people having a hard week.
- **Version 1 data moves up when it's read** and is saved as version 2 only with the next change, so opening 0.4.0 changes nothing by itself, and an old window left open still works until then (after that it sees newer data and stops saving).
- **The bar on See is extra, not the only way to read it:** the counts are in words beside it, and it's hidden from screen readers. Further along is a deeper color in light mode and a brighter one in dark.
- **A pressed Lifts me or Weighs on me shows a ring and a check mark,** not only a color.
- **What has focus scrolls clear of the Undo bar** (`keepClear()`, 0.4.0). Testing showed a thought moved along could sit under the bar.
- **See shows from 5 thoughts.** Fewer than that means too little. Before that it's one plain line, with no example, to keep it straightforward.
- **Replaced by the remake,** so nobody brings them back by mistake: the six-stage loop, topics (with renaming and the filter), Move forward into new linked thoughts and trails, the Map, the heading and the stuck point, the marked example, and the Decide and Me tabs (decisions, Moments, How I decide, Fuels & drains, the Big Five). They went to keep it straightforward. Topics or a personality check can come back if the owner asks.
- **Straight to a web app, no Claude artifact first** (Nov 14, 2026). It's free for anyone, nothing gets built twice, and Home Screen apps keep their data better than artifact storage. It matches the retired Claude copies rule across freeforgood-apps.
- **No AI, nothing sent anywhere.** The person does the interpreting. That keeps the privacy promise simple and true.
- **No sharing.** Each person uses it for themselves. Seeing anyone else's results would need a server and accounts and break the promise.
- **Saved data lives in IndexedDB, not localStorage.** Thoughts grow over time, and the roughly 5 MB of localStorage is shared with every app on freeforgood-apps.github.io.
- **One saved record with a save count** (Nov 14, 2026). A save only goes ahead when the stored count still matches the window's, and it's read back to check. If another window saved first, the newest wins and the window says its last change wasn't saved. Windows also tell each other about saves and re-check when shown, so that's rare. Nothing can change until the saved data has loaded.
- **Damaged data is set aside** (`damaged-<rev>`), with a two-tap Start fresh, because saving must never write over what it can't read. Bringing a copy back comes with the safety net. Data saved by a newer version is shown but never saved over.
- **Reading saved data keeps every field,** so an older version or a tab left open never trims what a later version added. It skips `__proto__`, `constructor` and `prototype`.
- **Undo sits in a bar above the tabs** for 10 seconds (longer while it has focus) and goes away on a tab switch, so it never covers another tab. Delete uses Undo rather than a two-tap confirm.
- **The PIN screen is optional and off by default.**
- **The shared freeforgood-apps address was chosen over a separate org.** It's simpler, and the prefixes and privacy lock keep apps apart.
- **Tabs sit at the bottom** (Nov 14, 2026), not at the top like Till Payday's and Best Guess's, so they stay in thumb reach, as app-new-project Part 3 asks.
- **Warm clay color and the loop icon** (Nov 14, 2026), chosen by the owner. Clay is `#A3482B` in light mode and `#EB8F70` in dark, distinct from Till Payday's teal, Best Guess's indigo and Study Coach's navy. The icon is the thinking loop: 6 dots in a ring, the first a little bigger.
- **Versions stayed at 0.x until the first release,** like Best Guess. 1.0.0 is the first full release.
- **Text size and a short About came early,** in stage 1. About gained backups and what stays where in 0.5.0, and the PIN line and the self-test link in 1.0.
- **Text size stays a small localStorage setting** (`ownsight-v1-size`), not in the saved data, so it applies before the thoughts load. `settings` in the saved data is kept for later.
- **`el()` and `parseBackup()` arrive with the code that uses them,** so there's no unused code before then. `parseBackup()` arrived in 0.5.0, inside the logic markers so the tests reach it.
- **The app always opens on Write,** with no remembered tab, since writing is the main job.
- **The logic tests live in the self-test** (1.0), not in separate test files, to keep Till Payday's flat layout. The self-test carries them, checked a second way, along with the Done when lines code can test.
- **The name Ownsight was checked on Nov 14, 2026.** Thinkprint, Groundwork, Open Mind, Mind Reader, MindLoop and Thought Compass were ruled out by existing trademarks or apps in this space. A pending "Ownersight" application covers property and building software and was judged low risk.

## Where things stand (Nov 14, 2026)

- **1.0.0, the first full release, is ready** and on main. Thoughts saved by 0.2.0 through 0.5.0 carry over (saved data is still version 3).
- **Tested in headless Chrome:** the self-test (368 checks) at 3 sizes, in 13 time zones and on 4 days of the week; 16 of 16 planted bugs caught; 29 more checks of the PIN lock on the real app; the accessibility checker clean in 29 runs covering every screen, sheet and PIN state at 4 sizes in light and dark (CHANGELOG.md has the details).
- **Not tested yet:** the owner's iPhone check of 1.0 and 0.5.0 (below), the self-test on a real iPhone, VoiceOver, the share sheet and the clipboard in Safari, and the Android Install button (headless Chrome never offers one).
- **Tags:** `v0.1.0` to `v0.5.0`, all added by the "Tag new versions" workflow. `v1.0.0` comes when it reaches main.
- The repo is on the monthly app security sweep's list.

## Next up

- **The owner's iPhone check of 1.0,** on the live site (Done when):
  1. Turn on a PIN lock in More, close Ownsight and open it again: it asks for the PIN before any thought shows, a wrong PIN changes nothing, and the right one opens it.
  2. Open the self-test from About, tap Run self-test, and it says Passed.
- **And 0.5.0's, done at the same time:**
  1. Copy a backup code into Notes, delete everything from this device, paste the code back, and every thought returns.
  2. Delete a thought by mistake, and after Undo is gone, More brings back this morning's automatic copy in two taps.
- **The 5-minute VoiceOver check** (accessibility-check's iPhone test), once.
