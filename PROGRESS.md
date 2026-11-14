# Ownsight: progress

New chat? Read this first, then how-to-update.md before editing anything (it arrives with the first build stage). The steady brief comes first; the changing status is at the bottom.

## What it is

A free web app that helps each person understand their own unique psychology and what it means for their life. People catch thoughts, decisions and moments, tag each one with a stage of one thinking loop (Notice → Question → Idea → Plan → Do → Check), and see their own patterns: where their thinking leans, where it gets stuck, which way it's heading, how they decide, what fuels and drains them, and their Big Five. It's a home base for making better decisions and making sense of everyday life.

## Ground rules

- **Free forever.** No ads, accounts, tracking, paid services or AI. Everything stays on the device. No entry text is ever sent anywhere, to AI or anyone else. The person does the interpreting, helped by good prompts and their own numbers.
- **A mirror, not a diagnosis.** Patterns are shown as plain counts in the person's own terms ("so far, 3 of 5 were Ideas"), never as a type or a label. Small numbers say they're only a first look. It's not therapy, a clinical test or professional advice, and the app says so.
- **Each person, for themselves.** Nobody, including the owner, ever sees anyone else's entries or results. There is no sharing feature.
- **Anonymous.** The only public identity is freeforgood-apps. No real names, personal emails, locations, links to Claude chats or Claude page IDs in the code, commits or this repo. Commits use the account's private GitHub noreply address as the author and keep Claude's default committer, so GitHub shows them as Verified. Commit in UTC. Leave out the Claude session link line tools may suggest adding, and check the message (`git log -1 --format=%B`) before pushing. Every push goes through the toolkit's push-check.
- **Plain, warm, simple wording,** around a 6th to 8th grade reading level, for anyone, including people having a hard day.
- **Feedback** goes to freeforgood-apps+ownsight@proton.me.
- **Verify before handing anything over:** parse-check, run it in a browser, test awkward cases (empty data, old saved data, undo, small phone screens, dark mode), check nothing else broke, and do the math in code. Then say what was checked and what couldn't be.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- **Web address (never changes):** https://freeforgood-apps.github.io/ownsight/ (Pages gets turned on after the first stage is pushed).
- **Names that never change,** or people lose their data:
  - Saved data: IndexedDB database `ownsight-v1`. Small settings: localStorage keys starting `ownsight-v1-`.
  - Offline cache names start with `ownsight-`.
  - Backup codes start with `OWNSIGHT1:`. Backup files are named `ownsight-backup-YYYY-MM-DD.json`.
- **Shared address:** freeforgood-apps.github.io is shared with Till Payday, Study Coach and the other free apps. Every key, database and cache name keeps the `ownsight-` prefix, and nothing ever clears storage it doesn't own.
- **Planned files** (Till Payday's layout, flat at the top of the repo): `index.html` (the whole app), `sw.js`, `manifest.webmanifest`, the icons, `selftest.html`, `rebuild.py`, `README.md` (toolkit README outline), `CHANGELOG.md`, `how-to-update.md`, `SECURITY.md` and `.gitignore` (toolkit Baseline kit), and `.github/workflows/tag-new-versions.yml` (copied from Best Guess).

## The plan

### One loop, three kinds of entries

Every entry has a kind, a stage and a topic.
- **Thought:** anything on your mind. Type it, then tap a stage (tap 1) and a topic (tap 2). The second tap saves it.
- **Decision:** the choice, 2 to 4 options, your gut pick, how sure you are (1 to 5), and a date to check back. On that date it asks how it went (better, as expected, worse) and for one line on what you learned.
- **Moment:** something that happened. Prompts walk it through the loop: What happened? → What's the real question? → Two ways to read it → What will I do? Then one tap: fueled me, drained me, or neither.
- **Move forward:** any entry can start its next stage. The new entry links back to the old one (`from`), which is what draws the Map.

### Tabs

1. **Catch:** log a thought, decision or moment. Recent entries underneath.
2. **Patterns:**
   - **Lean:** the stage that gets most of your entries, in one plain sentence, plus 6 bars with counts and percents. Shows from 5 entries.
   - **Stuck point:** where things stop moving, like "4 Ideas for every 1 Plan".
   - **Heading:** whether newer entries sit later in the loop (closer to doing) or earlier (closer to noticing). Shows from 10 entries.
   - **Map:** the 6 stages as a loop with counts. The stuck point is highlighted, and entries can be followed from start to finish.
   - Topics show where your mind is heading, like "mostly Work, at the Idea stage".
3. **Decide:** open decisions, check-backs due, and your track record.
4. **Me** (the groundwork, all on one page):
   - **How I decide:** about 6 quick sliders. Draft list, settled in that stage: gut ↔ plan, fast ↔ slow, alone ↔ ask others, safe ↔ bold, head ↔ heart, stick ↔ switch. Later shown next to what your real decisions show ("You said gut. 7 of 10 picks were gut picks, and 5 of those went well.").
   - **Fuels & drains:** your own two lists. Moment taps then show what actually fuels or drains you, next to what you wrote.
   - **Big Five:** the 50-item IPIP representation of the Goldberg (1992) markers for the Big-Five factor structure (public domain, ipip.ori.org), scored on the device. Shown as where you sit on each scale compared with the scale's middle, never against other people and never as a type. Retake any time to see change.
   - Your lean and stuck point.
5. **More:** backup, restore, optional lock, text size, delete everything (two taps), About.

### What it saves (data version 1, built for every stage now)

```
{
  v: 1,
  entries: [{
    id, kind: "thought" | "decision" | "moment",
    text, stage: "notice" | "question" | "idea" | "plan" | "do" | "check",
    topic,            // a topic id
    at,               // ISO time
    from,             // id of the entry this moved forward from, or null
    // decisions only
    options: [text], pick, sure, checkOn, outcome, learned,
    // moments only
    effect: "fuel" | "drain" | "neither", readings: [text, text]
  }],
  topics: [{ id, label }],
  profile: { decide: { answers, at }, fuels: [{ id, text }], drains: [{ id, text }] },
  bigFive: [{ at, answers }],   // 50 answers, 1 to 5
  settings: { textSize, lock }
}
```

Store what people enter and compute everything else (scores, lean, heading, stuck point, track record), so nothing stored can go stale. Every text and list has a limit with a friendly message (to settle in the saving stage).

### Stages (one build chat each, each ending verified, saved here and recorded below)

1. **Shell:** installable, offline, light and dark, safe areas, version shown, privacy lock on.
2. **Thinking loop:** Catch for thoughts, Patterns (lean, stuck point, heading, Map), Move forward, and saving on the device with each save read back.
3. **Safety net:** automatic copies, backup file and code (optional password), two-tap restore, damaged data set aside, backup reminders, optional app lock, About. Self-test and first release (1.0).
4. **Me:** How I decide, Fuels & drains, Big Five.
5. **Decide:** decisions and check-backs.
6. **Moments:** making sense of the day.

## Security plan (from the plan review)

- **Worth protecting:** people's private entries and self-portraits. **Risks:** data lost, someone holding the phone, a booby-trapped backup code or file, a bug in another app on the shared address.
- **Built in from the start:** the privacy lock (`default-src 'none'`, `connect-src 'none'`), every entry shown as text only through `el()`, backups checked with `parseBackup()` and a size cap before restore, a password option on backups, an optional app lock (PBKDF2-SHA256 with AES-256-GCM, Web Crypto only; a wrong password never wipes anything; a forgotten one can't be recovered), a generic page title with no entry text in titles or link previews, built-in fonts only (no Google Fonts), and the `ownsight-` prefix on every name.
- **Avoid:** any outside request, AI feature or analytics, and anything that clears storage it doesn't own.

## Decisions

Why some things are the way they are, so nobody "fixes" them by mistake:
- **Straight to a web app, no Claude artifact first** (Nov 14, 2026). It's free for anyone, nothing gets built twice, and Home Screen apps keep their data better than artifact storage. It matches the retired Claude copies rule across freeforgood-apps.
- **No AI, nothing sent anywhere.** The person does the interpreting. That keeps the privacy promise simple and true.
- **No sharing.** Each person uses it for themselves. Seeing anyone else's results would need a server and accounts and break the promise.
- **Topic is the second tap.** Default topics are Work, Home, People, Money and Me, and people can rename them. Topics have ids, so renaming one keeps its history.
- **Lean shows from 5 entries, heading from 10.** Fewer than that means too little.
- **Full 50-item Big Five, not the 20-item one,** for steadier results (10 questions per trait).
- **Values were left out of the groundwork on purpose.** The groundwork is How I decide, Fuels & drains and the Big Five.
- **Saved data lives in IndexedDB, not localStorage.** Entries grow over time, and the roughly 5 MB of localStorage is shared with every app on freeforgood-apps.github.io.
- **The app lock is optional and off by default.**
- **The shared freeforgood-apps address was chosen over a separate org.** It's simpler, and the prefixes and privacy lock keep apps apart.
- **The name Ownsight was checked on Nov 14, 2026.** Thinkprint, Groundwork, Open Mind, Mind Reader, MindLoop and Thought Compass were ruled out by existing trademarks or apps in this space. A pending "Ownersight" application covers property and building software and was judged low risk.

## Where things stand (Nov 14, 2026)

- Planning is done. The repo has the README and this file only. Nothing is built, and Pages isn't turned on yet.

## Next up

- **Stages 1 and 2: the owner's quick check on an iPhone, on the live site:**
  1. Type a thought, tag it in 2 taps, and see it saved.
  2. After 5 thoughts, the Patterns tab says which way you lean and shows the numbers.
  3. Close the app, reopen it, and the thoughts are still there.
- After stage 1 is pushed: turn on Pages (Settings → Pages → Deploy from a branch, main, / (root)).
- Ask the owner whether to add this repo to the monthly app security sweep.
