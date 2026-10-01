# 04 - SOP: Email Header Checks

1. Open the full headers ("Show original" or "View message source").
2. **From:** compare display name with the real address and domain.
3. **Return-Path:** should match the From domain. A mismatch is suspicious.
4. **Reply-To:** a different domain than From means replies go to the attacker.
5. **Received:** trace the first external hop. Is the origin plausible for this sender?
6. **Authentication-Results:** check SPF, DKIM and DMARC.
   - All pass: sending domain is authentic, but still verify content.
   - Any fail: treat as suspicious.
   - Passing checks can still be malicious if the domain itself is a lookalike.
7. **Subdomains:** flag brands that appear only as a subdomain.
8. **Date and timestamps:** inconsistent or out-of-order values suggest forgery.

## Display name spoofing vs true domain spoofing
| Type | What happens |
|------|--------------|
| Display name spoofing | A trusted friendly name hides a rogue address (e.g. `hacker@gmail.com`). Mobile clients are especially vulnerable. |
| True domain spoofing | The From address matches the company domain, usually because SPF/DKIM/DMARC are missing on the target domain. |

**Triage mandate: always inspect the full email headers.**
