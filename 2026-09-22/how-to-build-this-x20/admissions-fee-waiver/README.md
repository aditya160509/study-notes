# Waive — Admissions Command Center

A private, local-first application built around Aditya Balaji's 2027 university list. It tracks official application pages, deadlines, fee-waiver research, editable outreach drafts, follow-up dates, and responses for 29 institutions.

## Run it

```bash
cd app
npm install
npm run dev
```

Open the local address shown by Vite. For a production build, run `npm run build`.

## Included

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
