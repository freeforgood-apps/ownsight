# Ownsight: progress

New chat? Read this first, then how-to-update.md before editing anything. The steady brief comes first; the changing status is at the bottom.

## What it is

A free web app that helps each person understand themselves and what it means for their life, in the most straightforward way. Write what's on your mind and tap where it's at: **Thinking about it**, **Planning it** or **Did it**. That one tap saves it. Then, if you like, tap whether it **lifts you** or **weighs on you**. Each thought moves along as you make a plan and do it. The See tab shows, in plain counts, where your thoughts sit, what lifts you and what weighs on you, and which thoughts are waiting for a plan, with a look back at your week from Friday to Sunday.

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
  - Saved data: IndexedDB database `ownsight-v1` (version 1, store `data`, record `state` = `{ rev, json }`; data that couldn't be read is set aside as `damaged-<rev>`). Small settings: localStorage keys starting `ownsight-v1-`. Windows tell each other about saves on the BroadcastChannel `ownsight-v1`.
  - Offline cache names start with `ownsight-`.
  - Backup codes start with `OWNSIGHT1:`. Backup files are named `ownsight-backup-YYYY-MM-DD.json`.
- **Shared address:** freeforgood-apps.github.io is shared with Till Payday, Study Coach and the other free apps. Every key, database and cache name keeps the `ownsight-` prefix, and nothing ever clears storage it doesn't own.
- **Files** (Till Payday's layout, flat at the top of the repo): `index.html` (the whole app), `sw.js`, `manifest.webmanifest`, the icons, `rebuild.py`, `README.md` (toolkit README outline), `CHANGELOG.md`, `how-to-update.md`, `SECURITY.md` and `.gitignore` (toolkit Baseline kit), and `.github/workflows/tag-new-versions.yml` (copied unchanged from Best Guess). Still to come: `selftest.html` (the safety-net stage), which `rebuild.py` will build.

## How it works: the remake (0.4.0, Nov 14, 2026)

The owner asked for a remake, rethought from the goal: simpler to understand and use, and straightforward. The hardest parts were picking 1 of 6 stages and too much on Patterns. The owner approved a mockup of the screens below (a private design canvas, not linked here), and 0.4.0 builds them.

### Three tabs, at the bottom: Write, See, More

1. **Write** (the app opens here)
   - One box, "What's on your mind?", then "Where is it at? Tap one to save it." and three big buttons with short hints: **Thinking about it** (On my mind, no plan yet), **Planning it** (I know what I'll do), **Did it** (Done, or doing it now). The tap saves.
   - Right after saving, a card above the tabs: "Saved as Thinking about it." with **Undo**, and "Does it lift you or weigh on you?" with **Lifts me** and **Weighs on me**, then "Optional. Skip it if you're not sure." It's the Undo bar with the question added, and it stays about 20 seconds.
   - **Recent** under the box, newest first. Tapping a thought opens it.
2. **A thought, opened** (a sheet): its words, its stage and since when (plus when it was written, once it has moved), the lines written when it moved along ("Your plan", "How it went"), then **Next step**, one big button. At Thinking: **Make a plan** ("What will you do about it?"), plus **I already did it**. At Planning: **I did it** ("How did it go?"). Each asks for an optional line, then moves the thought along. At Did it, there's no next step. Lifts or weighs can be set, changed or cleared here. Then **Edit** (the words) and **Delete**, each with Undo.
3. **See** (plain counts, from 5 thoughts; before that, one line: "3 of 5 so far")
   - "From your 12 thoughts", a headline from the biggest stage ("You do a lot of thinking.", "You make a lot of plans." or "You get a lot done."; a tie: "Your thoughts are spread out."), the count ("8 of your 12 thoughts are still at Thinking about it."), one bar in three parts, and a key with the counts.
   - **What lifts you, and what weighs on you:** how many of each and the newest 3, then "What do the ones that lift you have in common?" Shows once at least one thought has been tapped.
   - **N thoughts are waiting for a plan** (those at Thinking) with **Show me one**, which opens the oldest one at Thinking.
   - **Your week,** at the top from Friday to Sunday (the person's own time): the last 7 days, "You wrote 9 thoughts and did 2 of them", what lifted you and what weighed on you, and "What would you like more of next week?" (nothing to fill in). Only when there's at least one thought that week.
   - "Just counts from your own thoughts. A mirror, not a diagnosis."
4. **More:** text size, Add to Home Screen, About (backups join with the safety net).

### What it saves (data version 2)

```
{
  v: 2,
  thoughts: [{
    id, text,
    stage: "thinking" | "planning" | "did",
    feel: "lifts" | "weighs" | null,
    at,                            // when it was written (ISO time)
    steps: [{ stage, at, note }]   // each move along, with its optional line
  }],
  settings: {}
}
```

The database, the record layout, the save count, the read-back and the damaged and newer rules all stay; only what's inside `json` changes. Moving up from version 1 (0.2.0 and 0.3.0, test thoughts only): each entry becomes a thought, with Notice, Question and Idea → thinking, Plan → planning, and Do and Check → did. `feel` starts empty and `steps` start empty. Topics, `from` links, `profile` and `bigFive` go. A 0.3.0 window left open sees version 2 as newer and won't save over it. Limits: 1,000 characters for a thought or a note, and 10,000 thoughts.

### Stages (one build chat each, each ending verified, saved here and recorded below)

1. **Shell:** done (0.1.0).
2. **The first thinking loop:** done (0.2.0 and 0.3.0), now replaced by the remake.
3. **The remake:** done (0.4.0): the screens above, version 2 data and the move up from version 1.
4. **Safety net:** automatic copies, backup file and code (optional password), two-tap restore (including a `damaged-<rev>` copy), backup reminders, optional app lock, the full About, the self-test and the first release (1.0).

**Ideas for later** (offered to the owner, not chosen): a 3-minute personality check (20 public-domain IPIP statements, shown as five plain sentences, never a type), and one question a day.

## Security plan (from the plan review)

- **Worth protecting:** people's private thoughts and what they show about them. **Risks:** data lost, someone holding the phone, a booby-trapped backup code or file, a bug in another app on the shared address.
- **Built in from the start:** the privacy lock (`default-src 'none'`, `connect-src 'none'`), every entry shown as text only through `el()`, backups checked with `parseBackup()` and a size cap before restore, a password option on backups, an optional app lock (PBKDF2-SHA256 with AES-256-GCM, Web Crypto only; a wrong password never wipes anything; a forgotten one can't be recovered), a generic page title with no entry text in titles or link previews, built-in fonts only (no Google Fonts), and the `ownsight-` prefix on every name.
- **Avoid:** any outside request, AI feature or analytics, and anything that clears storage it doesn't own.

## Decisions

Why some things are the way they are, so nobody "fixes" them by mistake:
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
- **The app lock is optional and off by default.**
- **The shared freeforgood-apps address was chosen over a separate org.** It's simpler, and the prefixes and privacy lock keep apps apart.
- **Tabs sit at the bottom** (Nov 14, 2026), not at the top like Till Payday's and Best Guess's, so they stay in thumb reach, as app-new-project Part 3 asks.
- **Warm clay color and the loop icon** (Nov 14, 2026), chosen by the owner. Clay is `#A3482B` in light mode and `#EB8F70` in dark, distinct from Till Payday's teal, Best Guess's indigo and Study Coach's navy. The icon is the thinking loop: 6 dots in a ring, the first a little bigger.
- **Versions stay at 0.x until the first release** (1.0, with the safety net), like Best Guess.
- **Text size and a short About came early,** in stage 1. The full About (self-test link, backups) comes with the safety net.
- **Text size stays a small localStorage setting** (`ownsight-v1-size`), not in the saved data, so it applies before the thoughts load. `settings` in the saved data is kept for later (the app lock).
- **`el()` and `parseBackup()` arrive with the code that uses them,** so there's no unused code before then.
- **The app always opens on Write,** with no remembered tab, since writing is the main job.
- **The logic tests stay out of the repo for now,** to keep Till Payday's flat layout. The self-test carries them, along with the Done when lines code can test.
- **The name Ownsight was checked on Nov 14, 2026.** Thinkprint, Groundwork, Open Mind, Mind Reader, MindLoop and Thought Compass were ruled out by existing trademarks or apps in this space. A pending "Ownersight" application covers property and building software and was judged low risk.

## Where things stand (Nov 14, 2026)

- **0.4.0 (the remake) is live on Pages,** not shared yet. Thoughts saved by 0.2.0 and 0.3.0 carry over.
- **Tested in headless Chrome:** 19 logic tests in 12 time zones, 191 browser checks, 11 of 11 planted bugs caught, and the accessibility checker clean on every tab, sheet and card (CHANGELOG.md has the details). The test scripts aren't in the repo yet (see Decisions); the self-test will carry them.
- **Not tested yet:** the owner's iPhone check of 0.4.0 (below), VoiceOver on a real iPhone (at the first release), and the Android Install button (headless Chrome never offers one).
- **The iPhone checks for 0.2.0 and 0.3.0 were dropped,** since the remake replaced those screens. Stage 1's iPhone check passed (Nov 14, 2026).
- **Tags:** `v0.1.0`, `v0.2.0` and `v0.3.0`, all added by the "Tag new versions" workflow (its runs passed). `v0.4.0` comes from the same workflow when 0.4.0 reaches main.
- The repo is on the monthly app security sweep's list.

## Next up

- **The owner's iPhone check of 0.4.0,** on the live site:
  1. Save a thought in one tap, open it, tap Make a plan, and it moves to Planning it.
  2. On See, you can tell at a glance where your thoughts sit and what lifts you or weighs on you.
- **Safety net** (then 1.0). The self-test checks that the app opens offline with its version shown, carries the logic checks and the Done when lines code can test, and uses its own database name, never `ownsight-v1`. Once the self-test can open the sheets with made-up thoughts, the seed and draft steps in how-to-update.md retire. Before building, draft its Done when lines.
