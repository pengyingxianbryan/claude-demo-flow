# Example: Product walkthrough — BudgetBee CSV import

This is the full DemoFlow workflow for **`demo_type = walkthrough`**, using BudgetBee again so it pairs with [`finance_tracker.md`](./finance_tracker.md).

The goal here is **comprehension, not conversion**: a 90-second onboarding clip showing a logged-in user how to bulk-import a month of transactions from a CSV. Use this as the quality bar when `/demoflow:plan` runs in walkthrough mode.

---

## User input

```
/demoflow:plan
Demo type: product walkthrough
Product: BudgetBee
URL: https://app.budgetbee.app
Description: A simple finance tracker for freelancers. CSV importer maps bank exports to BudgetBee transactions.
Audience: Existing BudgetBee users on day 1, fresh from signup
Pain: Manual entry of last month's transactions is the #1 reason users churn before week 2
Features: Sign in, + New transaction → Upload CSV, drag-and-drop, column mapping, confirm import
Goal: User completes their first CSV import end-to-end without help
Format: 90-second walkthrough
Platform: In-app onboarding modal + help center docs page
Tone: Calm, instructional, second-person
CTA: (implicit — viewer is already in-product)
```

---

## `/demoflow:plan` output

### 1. Product Snapshot

- **Product name:** BudgetBee
- **Product URL:** https://app.budgetbee.app
- **Product type:** Personal finance tracker (freelancer niche)
- **Target audience:** Newly signed-up BudgetBee users on day 1
- **Main user pain:** Manual entry blocks them from seeing their data; ~40% of new users churn before week 2 because they never finish onboarding
- **Demo type:** **walkthrough**
- **Demo goal:** Viewer completes their first CSV import unassisted
- **Preferred platform:** In-app onboarding modal + help-center docs
- **Tone:** Calm, instructional, second-person
- **CTA:** Implicit — they're inside the product

### 2. Assumptions Made

- Sign-in form has standard email/password fields with a **Sign in** button. Confirm selectors against live app before recording.
- "+ New transaction" button is on the dashboard's primary toolbar.
- Upload modal supports drag-and-drop **and** click-to-browse (we only show drag-and-drop in the happy path).
- CSV column auto-mapping works on the first try for the demo file. Unmapped-columns is an edge case, not in this walkthrough.

### 3. DemoFlow Context Block

```demoflow-context
{
  "product_name": "BudgetBee",
  "product_url": "https://app.budgetbee.app",
  "description": "Finance tracker for freelancers — CSV importer maps bank exports to BudgetBee transactions.",
  "target_audience": "Newly signed-up users on day 1",
  "product_category": "Personal finance / cashflow tracker",
  "key_features": [
    "Email/password sign-in",
    "+ New transaction → Upload CSV flow",
    "Drag-and-drop file drop zone",
    "Column auto-mapping with manual override",
    "Confirm import → returns to dashboard with transactions visible"
  ],
  "main_user_pain": "Manual entry blocks them from seeing their data; many churn before completing onboarding.",
  "demo_type": "walkthrough",
  "demo_goal": "Viewer completes their first CSV import end-to-end without help",
  "demo_format": "90-second walkthrough",
  "preferred_tone": "Calm, instructional, second-person",
  "platform": "In-app onboarding modal + help-center docs",
  "call_to_action": "(implicit — already in-product)",
  "assumptions": [
    "Sign-in is email + password (no SSO in the demo)",
    "+ New transaction lives on the dashboard primary toolbar",
    "CSV auto-maps on first try; unmapped columns are out of scope",
    "Demo file demo-jan.csv lives in the seeded test account"
  ]
}
```

### 4. Demo Readiness

- **Score: 9/10**
- **Main strength:** Tight scope (one workflow, end-to-end), clear starting state, clean failure mode (just the happy path).
- **Main risk:** Real CSV uploads can be slow or the auto-mapping can miss columns. Pre-flight the demo file once before recording so the timing is consistent.

### 5. Top Demo Angles  *(skipped — walkthrough mode produces one literal script, not 5 angles)*

### 6. Recommended Script (90s walkthrough)

| Step | Time | User action | Voiceover | On-screen caption | Expected screen |
|---|---|---|---|---|---|
| 1 | 0:00–0:04 | Land on `/login` | "Head to **app.budgetbee.app** to sign in." | 1. Sign in | Login form, both fields empty |
| 2 | 0:04–0:10 | Click **Email** field, type `demo@budgetbee.app` | "Click the email field and enter your email." | — | Email field focused, value typed |
| 3 | 0:10–0:16 | Click **Password** field, type password | "Then your password." | — | Password field focused, dots visible |
| 4 | 0:16–0:22 | Click **Sign in** | "Click **Sign in**. Your dashboard loads." | — | Dashboard, empty transactions table, "$0 net" header |
| 5 | 0:22–0:28 | Pause on dashboard | "This is your dashboard — empty for now." | — | Dashboard idle, cursor still |
| 6 | 0:28–0:34 | Click **+ New transaction** (top-right of toolbar) | "To bulk-import, click **+ New transaction** in the top-right." | 2. Bulk-import | Modal opens with two tabs: **Manual** and **Upload CSV** |
| 7 | 0:34–0:40 | Click the **Upload CSV** tab | "Switch to the **Upload CSV** tab." | — | Drop zone visible, "Drag a CSV here or click to browse" |
| 8 | 0:40–0:50 | Drag `demo-jan.csv` onto the drop zone | "Drag in your CSV — your bank export works." | 3. Drag-and-drop | File preview appears: 28 rows, 4 columns |
| 9 | 0:50–1:02 | Pause on column-mapping screen | "BudgetBee auto-maps the columns. Date, Description, Amount, Category — all set." | — | Mapping table, all 4 columns green-checked |
| 10 | 1:02–1:08 | Click **Confirm import** | "Click **Confirm import**." | — | Loading spinner, then success toast "28 transactions imported" |
| 11 | 1:08–1:18 | Wait for dashboard to refresh; pan to net number | "Your dashboard updates. 28 transactions, net **+$3,420**." | 4. Done | Dashboard with populated table + net figure highlighted |
| 12 | 1:18–1:30 | Hold result screen 4s | "That's it. You're set up — categorise next, or import another month." | (no caption) | Dashboard idle, transactions visible, cursor hovering categorise button |

**Total length:** ~90 seconds. 12 steps, one UI action each.

### 7. Shot List

| Shot | Timestamp | Screen / page | Action shown | Voiceover line | On-screen caption | Recording note |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:04 | `/login` | Page load | "Head to app.budgetbee.app to sign in." | 1. Sign in | Start from logged-out state. Window 1280×800. |
| 2 | 0:04–0:10 | `/login` | Click `[data-testid=login-email]`, type | "Click the email field and enter your email." | — | Cursor moves slowly, pause 0.3s before typing |
| 3 | 0:10–0:16 | `/login` | Click `[data-testid=login-password]`, type | "Then your password." | — | Show dots, not characters |
| 4 | 0:16–0:22 | `/login` → `/dashboard` | Click `[data-testid=login-submit]`, wait | "Click Sign in. Your dashboard loads." | — | Capture full transition; no skipped frames |
| 5 | 0:22–0:28 | `/dashboard` | Idle 4s | "This is your dashboard — empty for now." | — | Cursor parked top-right; let the empty state read |
| 6 | 0:28–0:34 | `/dashboard` | Click `[data-testid=new-transaction]` | "Click + New transaction in the top-right." | 2. Bulk-import | Soft cursor halo; modal opens with fade |
| 7 | 0:34–0:40 | Modal | Click `[data-testid=tab-upload-csv]` | "Switch to the Upload CSV tab." | — | Hold drop zone in frame for 1s before next shot |
| 8 | 0:40–0:50 | Modal: drop zone | Drag `demo-jan.csv` from desktop | "Drag in your CSV — your bank export works." | 3. Drag-and-drop | File icon should be visible during drag; ~1.5s motion |
| 9 | 0:50–1:02 | Modal: mapping screen | Idle pan | "BudgetBee auto-maps the columns…" | — | All 4 columns must show green checks; if any miss, retake |
| 10 | 1:02–1:08 | Modal | Click `[data-testid=confirm-import]` | "Click Confirm import." | — | Capture spinner + success toast in same shot |
| 11 | 1:08–1:18 | `/dashboard` | Pan to net number | "Your dashboard updates. 28 transactions, net +$3,420." | 4. Done | Highlight net figure with soft outline |
| 12 | 1:18–1:30 | `/dashboard` | Hold 4s, hover categorise CTA | "That's it. You're set up — categorise next, or import another month." | — | End on still frame; no fade-out |

### 8. Recording Checklist

**Demo account**
- Use a dedicated walkthrough demo account, **not** the marketing demo account
- Account must be in clean state: logged out, no transactions, no leftover modal state
- Reset script: deletes all transactions and signs out so the recording can be re-run idempotently
- `demo-jan.csv` lives in `~/Desktop/` of the recording machine — same path every time

**Sample data**
- `demo-jan.csv` — exactly 28 rows, 4 columns: Date, Description, Amount, Category
- All vendor names obviously fake: "Figma", "AWS", "Cafe Moka", "Acme Co — invoice #042"
- Net total comes out to **+$3,420** when imported (matches step 11 voiceover)
- No real PII, no real bank account numbers, no real client names

**Browser & screen**
- Chromium / Chrome window at exactly **1280×800**
- Cursor highlighting on (system or recorder-level)
- No browser extensions visible (clean profile)
- Hide bookmarks bar, devtools, all tabs except the demo
- DPR 2× for crisp text on the rendered MP4

**Voiceover**
- Calm, second-person, ~140 wpm
- One re-take per line, pick the most relaxed take
- TTS is fine for v1 (this is the demo type that handles synthetic voice best)
- No music during VO; light pad acceptable in post

**QC**
- First 4 seconds: login screen visible, no leftover state from prior session
- Every clicked button matches the voiceover label exactly (case + punctuation)
- The 28 / +$3,420 numbers in step 11 are readable
- Total length 85–95s; reshoot if outside that band
- Final frame holds 4s — long enough that a viewer reading slowly finishes the last sentence

### 9. Recommended Next Step

> **Next:** `/demoflow:prep` — this walkthrough is a perfect fit for credentialed automation. The shot list maps 1:1 onto Playwright actions and the voiceover synthesizes cleanly via TTS.

Other useful commands:
- `/demoflow:review` — once you have a draft VO recorded in your own voice
- `/demoflow:export type:full` — bundle this for the docs / help-center page

---

## Notes on the credentialed pipeline for this walkthrough

This is the example to copy-paste into `.demoflow/<ts>/plan.json` if you want to dry-run `/demoflow:prep` end-to-end.

- **`/demoflow:prep`** will use Chrome DevTools MCP to log into `https://app.budgetbee.app`, then click into "+ New transaction" → "Upload CSV" once to discover real selectors (the `data-testid` values above are illustrative; the prep agent should overwrite them with what it finds). It seeds the account by deleting any existing transactions and uploading `demo-jan.csv` once to confirm the import flow works, then deletes the test transactions to leave the account in clean state for the recording.
- **`/demoflow:record`** generates a Playwright recorder that performs steps 1–12 with the timings above. The drag-and-drop in step 8 needs `page.evaluate` with a synthetic `DataTransfer` event — Playwright's `setInputFiles` is the simpler alternative if the modal accepts click-to-browse.
- **`/demoflow:produce`** synthesizes 12 voiceover clips, stitches them, builds `captions.srt` from measured TTS durations, and renders **16:9** (`platform: in-app onboarding modal + help-center docs` → docs is wide-format). Override to **9:16** in the conversation if you want a vertical version for in-app mobile onboarding.

For walkthroughs longer than 60 seconds, consider splitting into two recordings (sign-in + import as one, categorisation as a second). A single 4-minute auto-generated MP4 has too many compounding failure points.
