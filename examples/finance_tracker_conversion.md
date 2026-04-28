# Example: BudgetBee end-to-end

This is the full DemoFlow workflow for **BudgetBee**, a fictional finance tracker for freelancers. Use it as the quality bar for what each command should produce.

---

## User input

```
/demoflow:plan
Product: BudgetBee
URL: https://budgetbee.app
Description: A simple finance tracker for freelancers to track income, expenses, and monthly cashflow.
Audience: Freelancers and solopreneurs
Goal: Get users to try the free tracker
Format: 30-second social short
Platform: TikTok, Reels, YouTube Shorts
Tone: practical, founder-led, not too salesy
CTA: Try the free tracker
```

---

## `/demoflow:plan` output

### 1. Product Snapshot

- **Product name:** BudgetBee
- **Product URL:** https://budgetbee.app
- **Product type:** Personal finance tracker (freelancer niche)
- **Target audience:** Freelancers and solopreneurs, mostly first 1–3 years
- **Main user pain:** No clear picture of monthly cashflow; tax season is stressful
- **Demo goal:** Get viewer to try the free tracker
- **Preferred platform:** TikTok, Reels, YouTube Shorts
- **Tone:** Practical, founder-led, not salesy
- **CTA:** Try the free tracker (link in bio)

### 2. Assumptions Made

- Specific features (categories, charts, monthly summary) are inferred from the "finance tracker" category. Marked as assumptions in the context block.
- Assumed the free plan is the lead magnet (not a free trial).
- Assumed mobile-first since target is freelancers and platform is short-form video.
- Assumed no integrations with banks/Stripe/etc. unless the user adds them later.

### 3. DemoFlow Context Block

```demoflow-context
{
  "product_name": "BudgetBee",
  "product_url": "https://budgetbee.app",
  "description": "A simple finance tracker for freelancers to track income, expenses, and monthly cashflow.",
  "target_audience": "Freelancers and solopreneurs, primarily 1–3 years in",
  "product_category": "Personal finance / cashflow tracker",
  "key_features": [
    "Add income (assumption)",
    "Add expenses by category (assumption)",
    "Monthly cashflow summary (assumption)",
    "Category breakdown chart (assumption)"
  ],
  "main_user_pain": "No clear picture of monthly cashflow; tax season is stressful",
  "demo_goal": "Get viewer to try the free tracker",
  "demo_format": "30-second social short",
  "preferred_tone": "Practical, founder-led, not salesy",
  "platform": "TikTok / Reels / YouTube Shorts",
  "call_to_action": "Try the free tracker (link in bio)",
  "assumptions": [
    "Free plan is the lead magnet, not a trial",
    "Mobile-first product",
    "Specific feature names inferred from category"
  ]
}
```

### 4. Demo Readiness

- **Score: 7/10**
- **Main strength:** Clear audience and pain. Easy to write a viewer-feels-seen hook.
- **Main risk:** Without specific feature names confirmed, the screen recording could feel generic. Worth confirming what screens actually exist before recording.

### 5. Top 5 Demo Angles

| # | Angle title | Hook | Feature shown | Outcome shown | Best platform | Priority |
|---|---|---|---|---|---|---|
| 1 | Tax season panic | "Every March I lost a weekend to receipts. Then I built this." | Add expense + category | Monthly summary auto-totals | TikTok / Reels | 9 |
| 2 | The 30-second freelance ledger | "If you can't tell me your last month's profit in 5 seconds, watch this." | Dashboard summary | Profit number on screen | TikTok | 8 |
| 3 | Stop using Notion for money | "Notion is great. For finance it's a trap." | Quick add flow | One-tap entry | LinkedIn / X | 8 |
| 4 | Freelance cashflow in one screen | "This is what your freelance month should look like." | Monthly chart | Visual cashflow | Reels / Shorts | 7 |
| 5 | Founder origin | "I'm a freelancer. I lost $3k to bad bookkeeping. So I built BudgetBee." | App tour 5s | Trust + outcome | LinkedIn / YouTube | 7 |

### 6. Recommended 30-second Script

Using **Angle 1: Tax season panic** (priority 9, founder-led, pain-led).

| Time | Section | Voiceover | On-screen text | Screen / action |
|------|---------|-----------|----------------|-----------------|
| 0:00–0:03 | Hook | "Every March I lost a weekend to receipts." | TAX SEASON HIT DIFFERENT | Talking head, kitchen table, scattered receipts B-roll |
| 0:03–0:10 | Problem | "I'm a freelancer. I had no idea what I made or spent month to month." | NO IDEA WHAT I MADE | Cut to messy spreadsheet, fast scroll |
| 0:10–0:22 | Product action | "So I built BudgetBee. Add an expense in three taps. Pick a category. Done." | ADD EXPENSE → 3 TAPS | Phone screen recording: open app → add expense modal → pick "Software" → save |
| 0:22–0:27 | Result | "End of the month, I see exactly what's left." | $3,420 LEFT | Dashboard with monthly summary, $ figure visible |
| 0:27–0:30 | CTA | "It's free. Link in bio." | FREE — LINK IN BIO | Talking head + text overlay |

### 7. Shot List

| Shot | Timestamp | Screen / page | Action shown | Voiceover line | On-screen caption | Recording note |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Talking head | Direct to camera, sit down, exhale | "Every March I lost a weekend to receipts." | TAX SEASON HIT DIFFERENT | Natural light, eye contact, no logo |
| 2 | 0:03–0:07 | B-roll: receipts | Pile of paper receipts on table | "I'm a freelancer." | — | Quick handheld pan, 2s |
| 3 | 0:07–0:10 | Spreadsheet | Fast vertical scroll through messy sheet | "I had no idea what I made or spent month to month." | NO IDEA WHAT I MADE | Pre-blur sensitive cells |
| 4 | 0:10–0:14 | App: home | Tap "+ Add expense" | "So I built BudgetBee. Add an expense in three taps." | ADD EXPENSE → 3 TAPS | Phone vertical, slow tap, screen recording at 60fps |
| 5 | 0:14–0:18 | App: add expense modal | Type "$45 — Figma" | (continues VO) | — | Make sure keyboard isn't covering action |
| 6 | 0:18–0:22 | App: category picker | Tap "Software" → Save | "Pick a category. Done." | — | Capture confirmation toast |
| 7 | 0:22–0:27 | App: monthly summary | Pan to "Net this month" | "End of the month, I see exactly what's left." | $3,420 LEFT | Make sure number is bold and visible |
| 8 | 0:27–0:30 | Talking head + overlay | Smile, shrug | "It's free. Link in bio." | FREE — LINK IN BIO | Hold last frame an extra 0.5s |

### 8. Recording Checklist

**Demo account**
- Create a fresh demo account (not your real freelance data)
- Pre-fill last 30 days with ~12 expenses and ~4 income entries
- Verify monthly summary shows a believable net number ($2k–$5k)
- Reset state script ready in case you need a second take

**Sample data**
- Realistic vendor names (Figma, Notion, AWS, coffee shop names)
- Mix of categories (Software, Travel, Food, Subscriptions)
- 1–2 income entries from real-sounding clients ("Acme Co — invoice #042")
- No real client names, no real amounts

**Browser & screen**
- Phone in Do Not Disturb
- Status bar shows full battery, full signal, no notifications
- Brightness at 80% for clean capture
- Use a clean, default phone wallpaper if home screen is shown
- Record at 60fps, vertical 9:16

**Voiceover**
- Record VO separately in a quiet room (not on the phone mic)
- Read each line twice; pick the more natural take
- Pace: under 15 words per line, breathe between sections
- No music vocals during VO sections

**QC**
- First 2 seconds: hook line is on screen and audible
- Net dollar amount in shot 7 is readable on a small phone
- Captions match VO word-for-word
- No personal info visible
- Final frame holds long enough to read the CTA

### 9. Recommended Next Step

> **Next:** `/demoflow:review` — once you draft the script in your own voice, paste it back to get a critique and a sharper rewrite before recording.

Other useful commands:
- `/demoflow:script angle:3 style:contrarian` — try the "Stop using Notion for money" angle
- `/demoflow:export` — bundle this plan into copy-paste markdown for Notion / CapCut

---

## `/demoflow:script` follow-up

### User input

```
/demoflow:script angle: 3 length: 15s style: contrarian platform: tiktok
```

### Selected Angle

**Angle 3: Stop using Notion for money.** Contrarian fits — it picks a fight with a well-loved tool the audience already uses, which gives the hook tension.

### Script (15s, contrarian)

| Time | Section | Voiceover | On-screen text | Screen / action |
|------|---------|-----------|----------------|-----------------|
| 0:00–0:02 | Hook | "Notion is great. For finance, it's a trap." | NOTION ≠ FINANCE TOOL | Talking head, deadpan |
| 0:02–0:05 | Problem | "Freelancers spend 40 minutes a week on a database that doesn't do math." | 40 MIN/WEEK | B-roll: messy Notion finance template |
| 0:05–0:11 | Product action | "BudgetBee. Add an expense. Pick a category. Done in 5 seconds." | 5 SECONDS | Phone screen recording: tap +, $45 Figma, Software, save |
| 0:11–0:15 | Result + CTA | "Real cashflow. Free. Link in bio." | FREE → LINK IN BIO | Dashboard with $3,420 net + text overlay |

### 2 Alternative Hooks

1. "Your Notion finance template is a glorified spreadsheet." — direct attack, may rile up Notion fans (good for engagement)
2. "Notion finance templates have a 90% drop-off in week 2." — invented stat would be dishonest; instead: "Most freelancers stop updating their Notion finance template by week 2."

### 2 Alternative CTAs

1. "Free, no card. Link in bio." — lower friction signal than "Try the free tracker"
2. "Comment 'switch' and I'll send you the link." — drives engagement loop on TikTok algorithm

### Recommended Next Step

> **Next:** `/demoflow:review` — paste this script back once you've adjusted the wording in your voice.

---

## `/demoflow:review` follow-up

### User input

```
/demoflow:review

Hey freelancers, are you struggling to track your finances? Notion is great
for notes but it's not really designed for money. With BudgetBee you can
easily add expenses, categorize them, and see your monthly cashflow at a
glance. We make it simple to stay on top of your freelance finances. Try
BudgetBee free today!
```

### Verdict

**Weak.** Reads like a website paragraph, not a 30-second video. No hook, no pain, no specific product moment.

### Scorecard

| Area | Score /10 | What works | What's weak | Fix |
|---|---|---|---|---|
| Hook | 2 | Mentions audience | "Hey freelancers, are you struggling to…" is the most-skipped opener on short-form. No tension. | Open with the painful moment, not a question. |
| Pain clarity | 4 | Notion comparison is something | "track your finances" is generic | Name the specific painful moment: tax season, end-of-month, "where did $400 go" |
| Product action | 3 | Mentions add + categorize | Lists features instead of showing one. No screen action implied. | Pick **one** action (add expense, 3 taps) and write it visually. |
| Outcome clarity | 3 | "Stay on top" — vague | No specific outcome. No number. | Show a concrete number on screen: "$3,420 left this month." |
| Pacing | 4 | Short paragraph | But it's prose, not a script with timing | Convert to a 5-row table with timestamps. |
| CTA | 5 | Has an ask | "Try BudgetBee free today" is generic | "Free. Link in bio." Or "Free, no card." |
| Trust / believability | 4 | No false claims | Reads like marketing copy, not a person | Use first person. Founder voice. |
| Platform fit | 3 | — | This won't work on TikTok at all in this form | Rewrite as 30s table with on-screen text |

### What to cut

- "Hey freelancers, are you struggling to…" — kill the question opener
- "We make it simple to stay on top of…" — pure filler
- "easily" "simple" "great" — soft adjectives, no information
- Any sentence the viewer can't picture as a shot

### What to make clearer

- The painful moment. When does it hurt? (Answer: end of month, tax season.)
- The specific product action. What happens on screen?
- The result. Show a number, not "stay on top."

### 5 Better Hooks

1. "Every March I lost a weekend to receipts." (founder-led)
2. "Notion is great. For finance, it's a trap." (contrarian)
3. "If you can't tell me your last month's profit in 5 seconds, watch this." (pain-led)
4. "I lost $3k to bad bookkeeping in year one." (social-proof / specific number)
5. "POV: it's the 31st and you have no idea what you made." (situational)

### 5 Better CTAs

1. "Free. Link in bio."
2. "Free, no card. Link in bio."
3. "Comment 'switch' and I'll send you the link."
4. "DM me 'BudgetBee' and I'll get you set up."
5. "Try the free tracker — link in bio."

### Improved Version

| Time | Section | Voiceover | On-screen text | Screen / action |
|------|---------|-----------|----------------|-----------------|
| 0:00–0:03 | Hook | "Notion is great. For finance, it's a trap." | NOTION ≠ FINANCE | Talking head, deadpan |
| 0:03–0:10 | Problem | "I tried tracking my freelance income in Notion. By week 3 I'd stopped updating it." | STOPPED BY WEEK 3 | B-roll: half-filled Notion finance template |
| 0:10–0:22 | Product action | "So I built BudgetBee. Add an expense in three taps. Pick a category. Done." | ADD EXPENSE → 3 TAPS | Phone: tap +, $45 Figma, Software, save |
| 0:22–0:27 | Result | "End of the month, I see exactly what's left." | $3,420 LEFT | Dashboard with net number visible |
| 0:27–0:30 | CTA | "Free. Link in bio." | FREE → LINK IN BIO | Talking head + text overlay |

### Recommended Next Step

> **Next:** `/demoflow:export type:full` — this version is shippable. Bundle the full plan and start recording.

---

## `/demoflow:export` follow-up

### User input

```
/demoflow:export type:full
```

### Output

```markdown
# BudgetBee — Demo Plan

## Product context
- Audience: Freelancers and solopreneurs, primarily 1–3 years in
- Pain: No clear picture of monthly cashflow; tax season is stressful
- Demo goal: Get viewer to try the free tracker
- Platform: TikTok / Reels / YouTube Shorts
- Tone: Practical, founder-led, not salesy
- CTA: Free tracker — link in bio

## Recommended script (30s, contrarian / founder-led)

| Time | Section | Voiceover | On-screen text | Screen / action |
| --- | --- | --- | --- | --- |
| 0:00–0:03 | Hook | "Notion is great. For finance, it's a trap." | NOTION ≠ FINANCE | Talking head, deadpan |
| 0:03–0:10 | Problem | "I tried tracking my freelance income in Notion. By week 3 I'd stopped updating it." | STOPPED BY WEEK 3 | B-roll: half-filled Notion finance template |
| 0:10–0:22 | Product action | "So I built BudgetBee. Add an expense in three taps. Pick a category. Done." | ADD EXPENSE → 3 TAPS | Phone: tap +, $45 Figma, Software, save |
| 0:22–0:27 | Result | "End of the month, I see exactly what's left." | $3,420 LEFT | Dashboard with net number visible |
| 0:27–0:30 | CTA | "Free. Link in bio." | FREE → LINK IN BIO | Talking head + text overlay |

## Shot list

| Shot | Timestamp | Screen | Action | Voiceover | Caption | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0:00–0:03 | Talking head | Sit, exhale, deadpan | "Notion is great. For finance, it's a trap." | NOTION ≠ FINANCE | Natural light, no logo |
| 2 | 0:03–0:07 | B-roll: Notion | Half-filled template, scroll | "I tried tracking my freelance income in Notion." | — | Blur any real names |
| 3 | 0:07–0:10 | B-roll: Notion | Stale "last edited 3 weeks ago" | "By week 3 I'd stopped updating it." | STOPPED BY WEEK 3 | Show timestamp clearly |
| 4 | 0:10–0:14 | App: home | Tap "+ Add expense" | "So I built BudgetBee." | ADD EXPENSE → 3 TAPS | Slow tap, 60fps vertical |
| 5 | 0:14–0:18 | App: add expense modal | Type "$45 Figma" | "Add an expense in three taps." | — | Keyboard not covering field |
| 6 | 0:18–0:22 | App: category picker | Tap "Software" → save | "Pick a category. Done." | — | Capture confirmation |
| 7 | 0:22–0:27 | App: monthly summary | Pan to "Net this month" | "End of the month, I see exactly what's left." | $3,420 LEFT | Bold, readable on small phone |
| 8 | 0:27–0:30 | Talking head + overlay | Smile, shrug | "Free. Link in bio." | FREE → LINK IN BIO | Hold final frame +0.5s |

## Recording checklist

**Demo account**
- Fresh demo account, not real data
- Pre-fill 30 days: ~12 expenses, ~4 income entries
- Net summary should show $2k–$5k
- Reset script ready for second takes

**Sample data**
- Realistic vendors (Figma, Notion, AWS)
- Mixed categories (Software, Travel, Food, Subscriptions)
- 1–2 fake clients ("Acme Co — invoice #042")
- No real client names or amounts

**Browser & screen**
- Phone in Do Not Disturb
- Full battery, full signal, no notifications in status bar
- Brightness 80%
- Default wallpaper if home screen shown
- Record vertical 9:16 at 60fps

**Voiceover**
- Record VO separately in a quiet room
- Two takes per line; pick the natural one
- Under 15 words per line
- No music during VO

**QC**
- First 2s: hook on screen and audible
- $3,420 number readable on small phone
- Captions match VO word-for-word
- No personal info visible
- Final frame holds long enough to read CTA
```

**What to do next:** Record shots 1–3 (talking head + B-roll) first while your energy is fresh. Screen recording shots 4–7 are easier to retake.

**Next:** `/demoflow:review` once you have a rough cut, or `/demoflow:script` to test another angle on a B-account.
