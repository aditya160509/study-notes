# Refreshing the research layer

`app/src/research.ts` holds every fact the app presents as verified. Each value
carries the page it came from and the day it was checked. Nothing goes in
without both.

## Why it lives in a file, not in the browser

The Exa API key must never ship in the client bundle. The research runs here, in
Claude Code, and the results are committed as source. The deployed app is still
a static site with no backend and no keys.

## Refreshing

Ask Claude Code, in this repo:

> Re-run the admissions research for <university>. Use Exa, confirm every value
> on the institution's own domain, and update `app/src/research.ts` with the
> source URL and today's date.

Anything older than 30 days renders with a "re-check" flag in the app
(`isStale` in `research.ts`), so staleness is visible rather than silent.

## The six queries

For each university, search its own domain and read the page before recording:

1. **Fee waiver** — fee amount, accepted waiver routes, whether internationals
   are eligible, and whether the institution issues its own waiver.
2. **International aid** — need-blind or need-aware for non-citizens, whether
   international aid exists at all, whether full need is met, which aid form
   (CSS Profile / institutional / alternative for applicants who cannot pay the
   CSS fee from India).
3. **Deadlines** — application and aid deadlines, noting where the
   international deadline differs from the domestic one.
4. **Requirements** — everything required of an international first-year
   applicant, including easily-missed items.
5. **Prompts** — the supplemental essay questions and their limits, plus
   whether the wording has changed from last cycle.
6. **Contact** — the admissions or international-office address, confirmed as
   appearing on an official page.

## What the first pass found

Four universities are recorded, and each turned up something that would not
have been guessed:

- **MIT** — waivers requested inside MIT's own application; a counsellor letter
  is accepted; MIT prefers the College Board form.
- **Princeton** — a Princeton-specific waiver needing no counsellor approval,
  and a **graded written paper** that many applicants miss entirely.
- **Yale** — issues **no waiver of its own**; you must qualify under the Common
  App's criteria. International EA aid documents are due **1 December**, not
  the 1 November domestic date.
- **Stanford** — **need-aware** for international citizens, and an international
  who declines aid on the application can never apply for it in four years.
