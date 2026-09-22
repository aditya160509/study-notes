# Waive — Admissions Command Center

A private, local-first application built around Aditya Balaji's 2027 university list. It tracks official application pages, deadlines, fee-waiver research, editable outreach drafts, follow-up dates, and responses for 29 institutions.

## Live

https://waive-aditya-balajis-projects.vercel.app — public. Deployment
protection is off, so anyone with the link can open it. `robots.txt` and an
`X-Robots-Tag: noindex` header keep it out of search engines, but the link
itself is the only thing standing between this page and a stranger.

Note that the seeded Common App personal statement is compiled into the
JavaScript bundle, so it travels with the link. Everything you type afterwards
stays in your own browser's local storage and is never uploaded. To take the
site private again:

```bash
cd app && npx vercel project protection enable waive --sso
```

## Run it

```bash
cd app
npm install
npm run dev
```

Open the local address shown by Vite. For a production build, run `npm run build`.

## Included

### Verified research layer
Fee-waiver routes, international aid policy, deadlines and requirement lists are
researched from each institution's own site and stored in `app/src/research.ts`
with a source URL and a verification date shown beside every value. Anything
older than 30 days is flagged for re-checking. See `docs/research-queries.md`.

### One page per university
Overview, Requirements, Essays, Documents, Recommendations, Fee waiver,
Financial aid, Emails, Timeline, Submission audit and Decision — everything for
one institution on one screen. Official requirements convert to tracked tasks in
a click.

### Tasks, recommendations, documents
A seven-state task system (Not started through Confirmed received) with due
dates, priority, owner, links and notes; due-today / this-week / 30-day /
waiting-on-someone / overdue views and a month calendar. Recommenders are
tracked by request, assignment and confirmation — never by letter content.
Documents record status and location only; no sensitive file is copied into
browser storage.

### Email centre and submission audit
Per-university drafts with duplicate-send warnings, reply tracking, follow-up
dates and an Open-in-Gmail action. Nothing is ever sent automatically. The
submission audit checks essays, contacts, deadlines, fee route, aid policy and
recommenders automatically, then gates the rest behind a manual confirmation
list.

### Comparison, portfolio, command palette
An editable-weight comparison table (no hidden ranking), a research and maker
portfolio with per-university reuse tracking, and a ⌘K palette across every
university, essay, task, story and contact.


- The current 29-school list from `aditya/voice-profile.md`, grouped by region
- Common App, MIT, UCAS, and direct-application routes
- Fall 2027 deadlines already present in the source material
- Policy checklists, research notes, response statuses, and follow-up dates
- Deadline overview, urgency counts, and core-document checklist
- Full application comparison table with fees and research readiness
- Full essay editor: prompt beside draft, autosave, version history with word-level diffs and restore, word/character counters with a limit bar, find and replace, full-screen writing, `.txt`/Word/PDF export, paste-without-formatting, and a final lock
- Prompt database per response: official wording, limit and unit, required or optional, undergraduate school, major, round, source URL, date verified, prompt status, and a warning when the wording changes from last cycle
- Writing-quality flags (never automatic rewrites): over-limit, unfilled placeholders, another university named, unanswered prompt clauses, repeated phrasing, generic admissions language, AI-sounding wording, unsupported claims, overly formal words, very long sentences, résumé-like bullets, and mechanical slips
- Story-reuse map: tag each response with the stories it uses, get warned when a story is already used elsewhere, and see the full matrix across your set
- Pre-filled applicant profile and Gmail connection status
- A personalized first-year international applicant draft for Aditya
- Copy and `mailto:` actions; nothing is sent automatically
- Browser local storage plus JSON export and import

Official admissions emails are included only where a credible contact was available. Blank contacts are intentional and should be filled only after checking the linked official admissions page.

The Exa research audit and remaining verification queue are recorded in `docs/exa-research-2026-09-22.md`.
