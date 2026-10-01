# 03 - SOP: URL Checks

1. **Hover, do not click.** Read the full URL. On mobile, long-press to preview.
2. **Read right to left.** Find the true root domain (the last two parts before the first `/`).
   - `www.decodelabs.tech.login-update.com` -> root is `login-update.com` (malicious).
3. **Check for lookalikes.**
   - Typosquatting: `amaz0n.com`
   - Homoglyph: `paypal.com` using a Cyrillic "a"
   - Combosquatting: `yourcompany-secure-login.com`
4. **Check protocol and extras.** HTTPS alone does not mean safe. Watch for `@` symbols, raw IP addresses and excessive hyphens.
5. **Expand shortened links** with a URL expander or sandbox before visiting.
6. **Never enter credentials via an emailed link.** Navigate to the site manually.
7. **Dangling DNS.** A trusted-looking subdomain can be hijacked if its cloud resource was deleted but the DNS record remained. Report odd behavior on trusted links.

## Quick examples
| URL | Real root | Verdict |
|-----|-----------|---------|
| `https://accounts.google.com/signin` | google.com | Likely legitimate |
| `https://google.com.secure-check.net/login` | secure-check.net | Malicious |
| `https://amaz0n-support.com` | amaz0n-support.com | Malicious (typo + combo) |
