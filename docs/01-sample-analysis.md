# 01 - Sample Message Analysis

## Sample 1: Fake Microsoft security alert (mass phishing)
File: `samples/sample1-fake-microsoft.txt`

**Suspicious links and keywords**
- Link: true root domain is `logins-updates.com`. "microsoft" is only a fake subdomain (read right to left).
- Keywords: "Urgent", "locked in 30 minutes", "verify now", "unusual sign-in activity".

**Red flags**
1. Sender-domain mismatch: display name says Microsoft, address is `logins-updates.com`.
2. Fake forwarded chain: "FW:" on a conversation the user was never part of.
3. Dangerous attachment: `.iso` file posing as a security update.
4. Urgency: artificial 30-minute deadline.
5. Activity alert pointing straight to a login link.
6. Generic greeting ("Dear User").

**Why it is unsafe:** The sender is not Microsoft. The link leads to a credential-harvesting page and the attachment likely delivers malware. The deadline is designed to trigger panic and skip checking.

**Verdict: MALICIOUS. Action: Block domain and escalate.**

---

## Sample 2: CEO wire transfer (BEC / whaling)
File: `samples/sample2-ceo-wire.txt`

**Suspicious keywords:** "IMMEDIATE ACTION REQUIRED", "strictly confidential", "do not discuss with anyone", "bypass standard procedure".

**Red flags**
1. Authority trigger: impersonates the C-suite.
2. Urgent bypass request: demands secrecy and skipping procedure.
3. Payment action requested by email.
4. External lookalike domain (`executive-update.com`).
5. Display name stuffed with "STRICTLY CONFIDENTIAL" to look official.

**Why it is unsafe:** Real executives do not ask staff to bypass finance controls. Secrecy prevents the victim from verifying with colleagues. This matches the Quanta Computer fraud pattern, where spoofed domains and forged documents led to losses of over $100M.

**Verdict: MALICIOUS. Action: Block domain and escalate.** Verify by phoning a known directory number.

---

## Sample 3: Parcel delivery text (smishing)
File: `samples/sample3-smishing.txt`

**Suspicious links and keywords:** shortened URL hiding the real destination; "could not be delivered", "fee", "within 2 hours".

**Red flags**
1. Unknown sender number, no tracking ID or order reference.
2. Shortened link hides the destination.
3. Small payment request (card-details harvest).
4. Urgency: 2-hour deadline.

**Why it is unsafe:** Couriers do not ask for fees via shortened links. The page will capture card details and OTPs.

**Verdict: MALICIOUS. Action: Report the number, delete, warn others.** Track parcels only via the courier's official app or site.

---

## Sample 4: Fake subscription renewal (callback phishing / TOAD)
File: `samples/sample4-callback-toad.txt`

**Suspicious keywords:** "charged", "overdue", "call ... to cancel immediately". No links at all.

**Red flags**
1. Callback scam: only a phone number, so link scanners see nothing.
2. Lookalike sender domain (`msft-renewals.net`).
3. Fear trigger: unexpected charge.
4. Invoice for a purchase the user never made.

**Why it is unsafe:** Calling connects you to a scammer who asks for remote access or payment details.

**Verdict: MALICIOUS. Action: Block domain, report, do not call.**

---

## Sample 5: Routine internal status update
File: `samples/sample5-safe-internal.txt`

**Findings:** Sender domain matches the company, tone is calm with no pressure, the attachment is a standard `.pdf`, and the context fits the user's work. Still confirm SPF/DKIM/DMARC pass in the headers.

**Verdict: SAFE (after header check). Action: Close.**

---

## Summary
| # | Type | Key red flags | Verdict | Action |
|---|------|---------------|---------|--------|
| 1 | Mass phishing | Domain mismatch, .iso, fake subdomain, urgency | Malicious | Block and escalate |
| 2 | BEC / whaling | Authority, secrecy, bypass procedure | Malicious | Block and escalate |
| 3 | Smishing | Short link, fee, urgency | Malicious | Report and delete |
| 4 | TOAD | Phone-only lure, fear | Malicious | Block and report |
| 5 | Routine internal | None | Safe | Close |
