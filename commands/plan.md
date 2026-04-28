---
description: Turn product info into a full demo plan — angles, recommended script, shot list, recording checklist.
argument-hint: [optional product info — URL, description, audience, goal, format, platform, tone, CTA]
---

You are running `/demoflow:plan`, the entry point of the DemoFlow workflow.

## What the user gave you

`$ARGUMENTS`

(May be empty, a single sentence, or a partial brief. Do not assume anything that wasn't stated.)

## Phase 1 — Intake (default behavior)

**Do not generate a plan on the first turn unless the user has explicitly provided every required field below.** Inferring a product, audience, or goal from a URL or one-liner produces a generic plan. Ask first.

### Step 1.1 — Echo what you parsed

Show a compact list of what the user *did* provide, mapped onto the schema fields. Mark anything you did not receive as `— missing —`. Do not guess.

### Step 1.2 — Ask for the missing details

Ask the user to fill in the missing fields, in one consolidated message. Use this structure:

> I need a few details before I draft the plan. Please answer what you can — anything you skip, I'll flag as an assumption.

Then list the questions, **only for fields that are still missing**, in this order:

1. **Demo type** — which of these two?
   - **Marketing demo** (Reel / Short / LinkedIn-style) — hook in 3s, fast cuts, every shot has to earn its place. Goal is conversion or attention.
   - **Product walkthrough** (onboarding / sales call / docs) — literal step-by-step. Show the sign-in page, click the username field, type the password, click Sign In, click + New Transaction, drag-and-drop a CSV, confirm the upload, etc. Goal is comprehension.
2. **Product name** — what is it called?
3. **Product URL** — link, if any.
4. **One-line description** — what does it actually do? (Not the marketing tagline — the literal function.)
5. **Target audience** — who is this for? Be specific (e.g. "freelance designers who invoice 5–20 clients/month", not "small businesses").
6. **Main user pain** — what problem does it solve, in their words?
7. **Key features to show** — 1–4 features that matter for *this* demo. (If unsure, say so — I'll suggest.)
8. **Demo goal** — what should a viewer do or feel after watching? (Sign up, book a call, understand the category, share with a friend, complete onboarding…)
9. **Format & length** — short-form (15–60s), walkthrough (1–3min), long-form (3min+)?
10. **Platform** — TikTok, Reels, YouTube Shorts, YouTube long, X, LinkedIn, landing page hero, in-app onboarding, sales-call screen-share, docs page…
11. **Tone** — founder-led / casual / polished / technical / playful / deadpan / instructional…
12. **Call to action** — what's the exact CTA line or destination?

End the intake message with:

> Reply with whatever you have — even partial answers move us forward. If you'd rather I just guess and produce a draft, say **"just guess"** and I'll generate with assumptions called out.

**Then stop. Wait for the user's reply. Do not produce any sections from Phase 2 yet.**

### Escape hatches

- If the user's first message says **"just guess"**, **"infer"**, **"go ahead"**, **"draft anyway"**, or similar → skip Phase 1 and run Phase 2 with assumptions explicitly called out in section 2. Default `demo_type` to `marketing` unless the wording strongly implies a walkthrough ("onboarding video", "tutorial", "step-by-step", "show how to use").
- If the user has already supplied **all 12 fields** in `$ARGUMENTS` → skip Phase 1 and run Phase 2 directly.
- If the user supplied **most** fields (≥ 9/12) and the missing ones are minor → ask one short follow-up for just the missing items, do not re-list the full questionnaire. **Never skip the demo-type question** — it changes the entire output shape.

## Phase 2 — Plan generation

Run this only after intake is satisfied (user answered, said "just guess", or supplied everything upfront). Produce **all sections below in order**, in one response.

**Branch on `demo_type`:**
- `marketing` → use the existing structure (sections 1–9 below). Hook-led, short-form, conversion-focused. Reference `templates/social_shorts.md` and `templates/founder_led.md`.
- `walkthrough` → keep sections 1–4 the same, but in section 5+ produce a **product walkthrough** instead of marketing angles. See "Walkthrough mode" below. Reference `templates/product_walkthrough.md`.

### 1. Product Snapshot

Compact list:
- Product name
- Product URL (or "not provided")
- Product type / category
- Target audience
- Main user pain (one sentence)
- **Demo type** (`marketing` or `walkthrough`)
- Demo goal (one sentence)
- Preferred platform
- Tone
- CTA

### 2. Assumptions Made

Bullet every detail you inferred or guessed. If the user answered fully, this list should be short or empty. Be honest about what is inferred. Do **not** invent specific features as if you saw them.

### 3. DemoFlow Context Block

Output the canonical context as a fenced code block with the `demoflow-context` language marker:

````
```demoflow-context
{
  "product_name": "",
  "product_url": "",
  "description": "",
  "target_audience": "",
  "product_category": "",
  "key_features": [],
  "main_user_pain": "",
  "demo_type": "marketing | walkthrough",
  "demo_goal": "",
  "demo_format": "",
  "preferred_tone": "",
  "platform": "",
  "call_to_action": "",
  "assumptions": []
}
```
````

This block is what later commands read. Get it right.

### 4. Demo Readiness

- **Score: X/10** — overall.
- **Main strength:** one line.
- **Main risk:** one line. The single biggest thing that could make the demo flop.

### 5. Top 5 Demo Angles  *(marketing only — skip in walkthrough mode)*

Markdown table with columns: `#`, `Angle title`, `Hook`, `Feature shown`, `Outcome shown`, `Best platform`, `Priority (1–10)`.

Angles must be distinct from each other (different hooks, different pain framings, different audiences within the niche). No generic "show the dashboard" angles. Each angle must connect a specific viewer pain to a specific product moment to a specific outcome.

### 6. Recommended Script

**If `demo_type = marketing`:** pick the highest-priority angle. Write a 30-second script in this exact format:

| Time | Section | Voiceover | On-screen text | Screen / action |
|------|---------|-----------|----------------|-----------------|
| 0:00–0:03 | Hook | … | … | … |
| 0:03–0:10 | Problem | … | … | … |
| 0:10–0:22 | Product action | … | … | … |
| 0:22–0:27 | Result | … | … | … |
| 0:27–0:30 | CTA | … | … | … |

Voiceover should sound like a real founder talking to a real user. No "introducing X, the all-in-one platform for…" energy. Direct, specific, human.

**If `demo_type = walkthrough`:** write a literal step-by-step script. Length is whatever the user asked for (default 90s if unspecified). Use this format:

| Step | Time | User action | Voiceover | On-screen caption | Expected screen |
|------|------|-------------|-----------|-------------------|-----------------|
| 1 | 0:00–0:05 | Land on `/login` | "Head to the sign-in page." | "1. Sign in" | Login form |
| 2 | 0:05–0:12 | Click email field, type `demo@…` | "Enter your email…" | — | Email field focused, value typed |
| 3 | 0:12–0:18 | Click password field, type, click **Sign in** | "…and your password, then sign in." | — | Dashboard loads |
| 4 | 0:18–0:30 | Click **+ New transaction** → click **Upload CSV** | "To bulk-import, click New transaction, then Upload CSV." | "2. Bulk-import" | Upload modal |
| 5 | 0:30–0:42 | Drag `demo.csv` onto drop zone | "Drag in your file." | — | File preview, column mapping |
| … | … | … | … | … | … |

Walkthrough rules:
- **One UI action per step.** "Click Sign in" and "Wait for dashboard" are two steps, not one.
- **Name buttons exactly as they appear on screen.** "Click **Sign in**" not "log in".
- **Cover the unhappy paths only if the user asked for them.** Default is the happy path.
- **No marketing voice.** Instructional, calm, second-person ("Head to…", "Click…", "You'll see…"). No hooks, no hype.
- Every step's `Expected screen` column is what the recorder needs to verify — be precise.

### 7. Shot List

Markdown table for the recommended script. Columns: `Shot`, `Timestamp`, `Screen / page`, `Action shown`, `Voiceover line`, `On-screen caption`, `Recording note`.

- **Marketing**: 4–7 shots is right.
- **Walkthrough**: one shot per script step (so 8–20+ is normal). Recording notes should specify exact selectors when known (e.g. "click `[data-testid=upload-csv]`"), cursor speed, where to pause, what to highlight.

### 8. Recording Checklist

Five short groups. 3–5 bullets each. Demo-account, sample-data, browser/screen, voiceover, QC. Be specific to this product where possible.

- **Marketing**: emphasize seed data realism (e.g. "load 6 fake freelance invoices, mix paid and unpaid").
- **Walkthrough**: emphasize **clean state** — every recording starts from a known starting screen, with no leftover data from a prior run. Note any signup/onboarding steps that need to be pre-completed before recording.

### 9. Recommended Next Step

Pick **exactly one**. Routing logic:

- If product context is thin / mostly assumptions → `/demoflow:plan` again with more detail (be direct: "your context is thin, here's what to add").
- If user asked for ideas / a-b options → `/demoflow:script` with a different style or length.
- If user already has a draft to evaluate → `/demoflow:review`.
- If the plan looks shippable as-is → `/demoflow:export`.

Format:

> **Next:** `/demoflow:<command>` — one-sentence reason.

Then add 2–3 other useful commands as a short list, no commentary.

## Style rules

- Do not pretend to have inspected the URL. If a URL is given, treat the name and any provided description as primary; mark inferred features as assumptions.
- Do not feature-dump. Translate every feature into a viewer-facing pain → action → outcome.
- **Marketing scripts** are short-form video, not pitch decks. Lines under ~15 words. No "we believe…" "our mission is…" type filler.
- **Walkthrough scripts** are literal. Every UI element named exactly. Every step is one user action. No skipped clicks. If the user has to wait for something to load, that is its own step.
- If the product context is too thin to produce a strong demo, say so plainly in section 4 ("main risk") and recommend the user run `/demoflow:plan` again with the missing details — but **still produce sections 5–8 as best-effort drafts**.
