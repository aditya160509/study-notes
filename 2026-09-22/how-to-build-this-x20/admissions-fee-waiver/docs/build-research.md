# Best way to build the admissions fee-waiver tool

## Direct answer

Yes. The best version is a **fee-waiver application assistant**—not a mass email scraper.

The app should help one student research each college's official process, prepare a personalized request, review it, and track the response. The student should remain in control of the final email.

This is the best approach because college fee-waiver rules differ, official contacts are more reliable than scraped personal addresses, and a review step prevents incorrect claims or messages from being sent.

## What the product should do

### 1. Add a college

The student enters:

- College name
- Official admissions email
- Admissions or fee-waiver webpage
- Application platform, such as Common App
- Application term and deadline
- Notes about the college's instructions

### 2. Record the fee-waiver process

For each college, the app should show whether the student has checked:

- Common App fee waiver
- NACAC fee-waiver form
- The college's own fee-waiver policy
- Any required counselor or school-official verification

Common App says students can request its fee waiver from their profile and that a counselor may need to confirm eligibility. It also says colleges may have separate institutional fee waivers. [Source: Common App](https://www.commonapp.org/static/f9d54dd41c76d04ef3e91779d03f7b93/Resource_FY_AppFees_ENG_2025.06.25_0.pdf)

NACAC says its form is sent directly to the college's admission office, that a qualified school or community official verifies the request, and that each college makes the final decision. [Source: NACAC](https://www.nacacnet.org/student/fee-waivers/)

### 3. Generate a personalized draft

The app should create an editable email using the college's name, the application term, and the student's actual situation. It should never invent financial circumstances, eligibility, deadlines, or policy details.

### 4. Review before sending

The student should be able to:

- Edit the subject and message
- Copy the message
- Open a `mailto:` link
- Later create a Gmail draft
- Mark the message as sent manually

Gmail's API supports creating unsent drafts, which makes draft-first review a good future integration. Google also recommends requesting the narrowest permission necessary. [Source: Gmail API](https://developers.google.com/workspace/gmail/api/guides/drafts)

### 5. Track replies

Use simple statuses:

```text
Not started
Researching policy
Draft ready
Sent
Awaiting reply
Approved
Declined
No response
```

Add an optional follow-up date, but do not send repeated follow-ups automatically.

## The best technical plan

### Phase 1: local MVP

Build a small private web app with:

- React and TypeScript, or plain TypeScript if keeping it very simple
- Browser local storage for the first version
- A clean school list and detail view
- Editable email templates
- Copy-to-clipboard and `mailto:` actions
- JSON export and import

This version can be useful without Google login, a database, or an email service.

### Phase 2: policy research workflow

Add a place to save the official admissions URL, fee-waiver URL, policy notes, and the date the page was checked. The student should paste or confirm the contact information instead of relying on an unverified email scraper.

### Phase 3: Gmail drafts

Add Google OAuth only after the local version works. The app should create a Gmail draft and leave the final send action to the student. Gmail permissions should be kept as narrow as possible. [Source: Google OAuth and Gmail scopes](https://developers.google.com/workspace/gmail/api/auth/scopes)

## Recommended email template

**Subject:** Application fee-waiver question for [application term]

Dear Admissions Team,

My name is [student name], and I am preparing an application to [college name] for [application term] as a [first-year/transfer] applicant.

I am writing to ask whether your institution offers an application fee waiver or another fee-waiver process for students experiencing financial hardship. I am reviewing the Common App and NACAC options and would appreciate guidance on which process your office accepts and whether any verification is required.

Thank you for your time and guidance.

Sincerely,  
[student name]  
[email address]

## What should not be included in version one

- Automatic scraping of every admissions employee's email address
- Bulk or repeated automated email
- Automatic sending without the student's review
- Claims about eligibility that the student has not verified
- Impersonation of a parent, counselor, school, or admissions office
- Unnecessary storage of financial documents or other private records

## Final recommendation

Build this as a **private school tracker with policy notes, personalized email drafts, and response tracking**. Add Gmail draft creation later. That is the most useful, reliable, and realistic version to build first.

