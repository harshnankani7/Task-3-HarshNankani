# 06 - Decision Tree

```mermaid
flowchart TD
    A[Incoming Suspicious Email] --> B{Sender and headers verified?<br/>From / Return-Path / SPF-DKIM-DMARC}
    B -- No --> M[MALICIOUS]
    B -- Yes --> C{Links, attachments or request suspicious?}
    C -- Yes, clear malicious intent --> M
    C -- Unclear or minor flags --> S[SUSPICIOUS]
    C -- No flags --> F[SAFE]
    F --> F1[Close]
    S --> S1[Warn user. Verify out-of-band.<br/>Do not click or reply.]
    M --> M1[Block domain and escalate to security team.<br/>Report, do not just delete.]
```

## Actionable outcomes
| Classification | Action |
|----------------|--------|
| Safe | **Close** |
| Suspicious | **Warn User** and verify through a separate channel |
| Malicious | **Block Domain and Escalate** |

## Pause, Verify, Report
1. **Pause:** recognize the cognitive trigger and stop interacting. Apply the Five-Minute Rule.
2. **Verify:** confirm through a secondary channel, such as a call to a known directory number.
3. **Report:** use the report-phishing button. Reporting lets security purge the threat from other inboxes.
