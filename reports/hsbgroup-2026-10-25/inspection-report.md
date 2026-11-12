# hsbgroup.net — public website inspection

Inspected: 25 October 2026 (India time). Target: https://hsbgroup.net/login

## Assessment

The public login interface works in the inspected browser, but this review does **not establish that the operator is legitimate or that the service safely handles money or personal data**. The most consequential concern is missing verifiable operator information despite financial-services language and references to Indian regulators. Several accessibility and usability defects are confirmed. The edge serves useful security headers, with room to tighten its content security policy.

No exploitable critical/high technical vulnerability was confirmed. This was a non-destructive, unauthenticated external review, not a penetration test or security certification. Priority below describes remediation urgency, not a claim of proven exploitation.

## Findings

### 1. High priority — operator identity and regulatory claims cannot be verified from the inspected pages

**Evidence:** The login identifies the brand only as “HS.” The entire inspected Agreement at https://hsbgroup.net/legal/account_agreement refers to “this platform,” says it complies with SEBI, RBI and PMLA requirements, and describes submission of PAN, Aadhaar and bank details. It supplies no legal entity name, registered address, regulatory registration number, or grievance contact. The inspected privacy policy also does not name the operator.

**Impact:** A prospective user cannot reliably identify the counterparty or match the website to a regulated entity. Mentioning a regulator does not establish registration. This is a trust/disclosure concern, not a finding that the operator is unregistered or fraudulent.

**Action:** Publish the legal entity, address, appropriate registration and exchange details, support and grievance contacts, and precise service scope. Independently match the entity, registration and official website through SEBI's recognised-intermediary directory before providing identity documents or money. SEBI itself recommends checking registration before investing: https://investor.sebi.gov.in/Investor-support.html

### 2. Medium priority — privacy rights lack an actionable contact route

**Evidence:** https://hsbgroup.net/legal/privacy_policy describes collection of identity, banking, transaction and device data. Its Customer Rights section says users may request inspection or amendment but supplies no email, contact form, responsible entity or request instructions. Retention is described only as satisfying statutory obligations; no effective/revision date is shown. Sharing recipients are broad categories.

**Impact:** Users cannot readily exercise the rights described or understand who is responsible for their data.

**Action:** Identify the responsible entity and privacy/grievance contact, give request instructions, explain retention criteria and recipient categories more specifically, and show an effective/revision date. This is a transparency assessment, not a legal compliance determination.

### 3. Medium priority — direct login URL returns an access-denied response to an ordinary HTTP client

**Evidence:** A normal HTTPS GET to /login returned HTTP 403 with Amazon S3 XML containing AccessDenied. The root / returned HTTP 200 with the app HTML. The in-app browser nevertheless rendered /login. A separate content fetch saw only “System loading, please wait...” and the initial title “mock-trader-app-v2 · Login.” See saved response headers and HTML.

**Impact:** Access depends on client/request path; link previews, crawlers, monitoring and potentially some fresh navigations may fail. The observed difference does not prove all browser reloads fail. It may reflect CDN routing, caching or request handling.

**Action:** Verify CDN handling of client-side routes and genuine missing assets, reproduce fresh direct navigations in supported browsers, and provide a useful loading-failure message. Do not treat every 403 as a security feature or blanket-convert all errors to success.

### 4. Medium priority — browser zoom is explicitly restricted

**Evidence:** Public root HTML, line 8, contains viewport settings `minimum-scale=1, maximum-scale=1, user-scalable=no`.

**Impact:** This asks browsers to restrict enlargement and can hinder low-vision users, although enforcement varies by browser.

**Action:** Remove the zoom restrictions and verify text enlargement and layout at 200% zoom.

### 5. Medium priority — modal keyboard focus can remain behind the dialog

**Evidence:** Clicking Register opens an invitation-code dialog with `role="dialog"` and `aria-modal="true"`. Focus remains on the underlying Register button. Pressing Tab moves to the underlying Agreement button; a DOM check confirmed the focused element was outside the dialog. The recovery dialog also initially left focus on its trigger.

**Impact:** Keyboard and assistive-technology users can navigate background controls while a modal covers the page.

**Action:** Move focus into the dialog on open, contain focus while it is open, make the background inert, and restore focus to the trigger on close. Verify Escape handling too; it was not tested here.

### 6. Low priority — password visibility control is unnamed; required state is visual only

**Evidence:** The password visibility button has no text, aria-label or title and appears as an unnamed button in the accessibility tree. Phone/password inputs have accessible names through aria-label, but no associated label elements and neither `required` nor `aria-required`, despite visible asterisks.

**Impact:** The icon's purpose and mandatory state are not fully conveyed to screen-reader users. This is not evidence that the server accepts missing fields.

**Action:** Name the control “Show password”/“Hide password,” expose its state, associate visible labels with fields, and express required state programmatically while retaining server-side validation.

### 7. Medium priority — password recovery provides no explanation of its support code

**Evidence:** Forgot password opens a dialog requesting Mobile and “Support verification code.” The dialog gives no explanation of where to obtain that code and no support link. No code was requested or submitted.

**Impact:** A locked-out user may have no clear next step. The UI alone cannot establish whether support identity checks, code expiry, attempt limits or replay protection are secure.

**Action:** Explain the recovery process and provide a verified support route. Separately audit code issuance, expiry, one-time use, identity verification and abuse controls on the server.

### 8. Security hardening — CSP allows dynamic evaluation and broad outbound destinations

**Evidence:** Both the successful root response and the /login error response contain `script-src 'self' 'unsafe-eval'` plus named Salesmartly/Cloudflare origins, and `connect-src 'self' blob: https: wss:`. Framing is permitted by self and two admin origins. See saved headers.

**Impact:** `unsafe-eval` weakens protection against some script-injection paths. Broad connection destinations provide less containment if malicious JavaScript executes. These settings alone do not prove XSS, data exfiltration, or that the permitted third-party scripts actually load.

**Action:** Identify and remove runtime evaluation requirements where feasible, restrict connections to the actual API/vendor origins, and confirm each permitted framing origin is intentional and controlled. Test proposed restrictions in report-only mode before enforcement.

## Additional observations

- **Domain history:** The .net registry RDAP response records registration on 17 September 2026, roughly 38 days before inspection, and expiration on 17 September 2027. New registration is context, not proof of fraud. Source: https://rdap.verisign.com/net/v1/domain/hsbgroup.net (saved locally).
- **Registration is invitation gated:** Register first requests an invitation code. This may be intentional, but the initial page does not explain eligibility or how to obtain one. Later registration steps could not be inspected.
- **Production naming:** Public runtime configuration exposes a `__MOCK_TRADER_RUNTIME_CONFIG__` identifier; the initial fetch title also uses mock-trader naming. Internal naming is not proof that live funds are simulated, nor proof of a vulnerability. The public product should clearly explain whether it is a simulation or a financial service.
- **Mobile appearance:** At the inspected 467 × 827 viewport, the page fit horizontally, the logo and flag loaded, and the main controls were visible. No desktop/tablet or device matrix was tested.
- **Indexability:** The root is an app shell with an initially empty title and no description; rendering supplies the branded title. A login page may intentionally avoid search indexing, so this is a product decision, not automatically an SEO defect.

## Positive controls observed

- HTTPS succeeded with certificate validation enabled in the HTTP client.
- HTTP /login redirected to HTTPS /login with status 301.
- Responses carried HSTS, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, a CSP, and a Permissions Policy disabling geolocation, microphone and payment permissions.
- CSP includes `object-src 'none'`, `base-uri 'self'`, `form-action 'self'` and an explicit `frame-ancestors` allowlist.
- Root HTML was served with `Cache-Control: no-cache, no-store, must-revalidate`. This does not establish caching policy for private API responses.
- Password input is masked and uses `autocomplete="current-password"`; phone fields have telephone autocomplete hints.
- Empty sign-in and first-step registration/recovery actions are disabled. Agreement and Privacy Policy navigation worked; both modal close actions worked.

## Scope and unresolved checks

Inspected the rendered login, public agreement and privacy policy, initial registration and recovery dialogs, keyboard focus, DOM accessibility metadata, a mobile-sized layout, root/login responses, HTTP redirect, referenced public runtime config and two delivered JavaScript assets, and registry registration dates. Asset inspection was limited and cannot establish full application behavior. No source repository was reviewed or changed.

Not tested: successful or failed authentication, MFA enforcement, rate limiting, credential stuffing resistance, account enumeration, session cookie attributes after login, session rotation/revocation, recovery-code security, authorization/IDOR, CSRF, injection, uploads, authenticated data exposure, trading correctness, deposits/withdrawals, infrastructure access control, dependency inventory, backend code, full TLS configuration, uptime, load, Core Web Vitals, automated accessibility conformance, or full browser/device compatibility. No credentials, invitation codes, personal information, recovery codes or attack payloads were submitted; no accounts were created.

A complete audit needs owner-authorized source/backend review and controlled test accounts or staging. This review cannot certify the site as secure or legitimate.
