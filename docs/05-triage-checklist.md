# 05 - Non-Expert Triage Checklist

Any "yes" in sections A or B means stop.

## A. Sender
- [ ] Does the display name differ from the real email address?
- [ ] Is the domain misspelled, a lookalike, or free webmail for an "official" sender?
- [ ] Is the Reply-To or Return-Path a different domain?

## B. Content
- [ ] Does it create urgency or a deadline?
- [ ] Does it threaten consequences or promise rewards?
- [ ] Does it ask for passwords, OTP/MFA codes or payment details?
- [ ] Does it ask for secrecy or to bypass normal procedure?
- [ ] Is the greeting generic or the context unexpected?

## C. Links and attachments
- [ ] Does the real link domain differ from the displayed text?
- [ ] Is it a shortened link or a QR code?
- [ ] Is the attachment unusual (.iso, .js, .scr, .exe, macro-enabled)?

## D. Channel
- [ ] Does it contain only a phone number to call?
- [ ] Did it arrive by SMS, voicemail or a live call demanding urgent action?

## E. Scoring
| Result | Classification | Action |
|--------|----------------|--------|
| 0 flags and headers authenticate | Safe | Close |
| 1-2 minor flags, or uncertain | Suspicious | Warn User |
| Spoofing, credential or payment request, or dangerous attachment | Malicious | Block Domain and Escalate |
