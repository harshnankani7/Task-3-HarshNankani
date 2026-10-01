#!/usr/bin/env python3
"""Simple phishing indicator checker (educational).

Usage: python tools/phish_check.py <message.txt>
Flags urgent keywords, shortened URLs, risky attachments, lookalike domains,
and the subdomain trap. This is a teaching aid, not a replacement for judgment.
"""
import re
import sys

URGENT = ["urgent", "immediately", "immediate action", "verify now", "locked",
          "overdue", "expires", "within 2 hours", "strictly confidential",
          "do not discuss", "bypass", "act now", "fee", "charged",
          "could not be delivered", "cancel"]
NEGATIONS = ["non-urgent", "no immediate action is required", "no urgent action"]
SHORTENERS = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "ow.ly"]
BAD_EXT = [".iso", ".js", ".scr", ".exe", ".vbs", ".bat"]
COMBO = ["secure", "login", "verify", "update", "account", "support", "billing"]
BRANDS = ["microsoft", "google", "paypal", "amazon", "apple"]


def root_domain(host):
    parts = host.lower().split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def analyze(text):
    low = text.lower()
    for n in NEGATIONS:  # ignore calm phrasing such as "Non-Urgent"
        low = low.replace(n, "")
    findings = []

    if re.search(r"call\s+[+\d(][\d\-x() ]{6,}", low) and not re.search(r"https?://", low):
        findings.append("Callback lure: phone number to call and no links (TOAD pattern)")

    for kw in URGENT:
        if kw in low:
            findings.append(f"Urgency/pressure keyword: '{kw}'")

    for ext in BAD_EXT:
        if re.search(re.escape(ext) + r"\b", low):
            findings.append(f"Risky attachment type: {ext}")

    for url in re.findall(r"https?://[^\s<>\"']+", text):
        host = re.sub(r"^https?://", "", url).split("/")[0]
        root = root_domain(host)
        if any(s in host.lower() for s in SHORTENERS):
            findings.append(f"Shortened URL hides destination: {url}")
        for b in BRANDS:
            if b in host.lower() and not root.startswith(b + "."):
                findings.append(f"Brand '{b}' only in subdomain/lookalike; real root is {root}")
        if any(c in root for c in COMBO) and "-" in root:
            findings.append(f"Possible combosquatting domain: {root}")
        if re.search(r"[a-z]\d[a-z]", root.split(".")[0]):
            findings.append(f"Digit-for-letter lookalike: {root}")

    m = re.search(r"^from:\s*(.*?)<([^>]+)>", text, re.I | re.M)
    if m:
        name, addr = m.group(1).strip().lower(), m.group(2).lower()
        domain = addr.split("@")[-1]
        for b in BRANDS:
            if b in name and b not in domain:
                findings.append(f"Sender mismatch: display '{b}' but address domain is {domain}")

    return findings


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()
    findings = analyze(text)
    score = len(findings)
    verdict = "SAFE" if score == 0 else "SUSPICIOUS" if score <= 2 else "MALICIOUS"
    print(f"File: {sys.argv[1]}")
    for item in dict.fromkeys(findings):
        print(f"  [!] {item}")
    print(f"Indicators: {score}  ->  Verdict: {verdict}")
    print({"SAFE": "Action: Close",
           "SUSPICIOUS": "Action: Warn User",
           "MALICIOUS": "Action: Block Domain & Escalate"}[verdict])


if __name__ == "__main__":
    main()
