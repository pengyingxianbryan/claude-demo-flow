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

### Step 1.2 — Pick the depth (mode gate)

Before asking the long question list, ask **one question first** and wait for the answer. The user's answer changes which questions you ask next and which phases you run. Use this exact framing:

> Before I ask the rest, how deep do you want this run? Three options:
>
> | Mode | What I do | Time | Touches your app? |
> |---|---|---|---|
> | **`dry`** | Plan only, no live access. Pure description-based. | ~30s | No |
> | **`ground`** | Plan + read-only recon (login, walk screens, capture real names + selectors) before drafting. **Default if you have a `.env`.** | ~1–3 min | Reads only |
> | **`full`** | `ground` + after the plan, I seed mock data and screenshot every shot so you're recording-ready. | ~5–8 min | **Writes data** |
>
> Reply with `dry`, `ground`, or `full`. If you don't have an app yet or just want to brainstorm → pick `dry`. If unsure → `ground` is the safe middle.

Quick recommend:
- If `.env` with `DEMOFLOW_APP_URL/USERNAME/PASSWORD` is present in CWD → recommend `ground` next to the table.
- If no `.env` and no repo URL provided → recommend `dry`.
- Never auto-pick `full`. Seeding is destructive; the user must opt in explicitly.

**Stop after asking. Wait for the user to pick.** Once they answer, store the choice as `mode` and continue to Step 1.3.

### Step 1.3 — Ask for the missing details

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
**Conditional questions — only ask these if `mode` is `ground` or `full`:**

13. **Live access** — is there a `.env` in this repo with `DEMOFLOW_APP_URL`, `DEMOFLOW_USERNAME`, `DEMOFLOW_PASSWORD`? Reply `yes`, `no` (and I'll show you how to set one up), or `skip live access` (use repo only).
    - **Do not paste passwords into chat.** If creds aren't in `.env`, set them up there. If the user pastes a password inline, refuse and re-instruct.
    - If they don't have a `.env` yet, give them the one-liner: `cp .env.example .env` (or show the keys to add). Wait for them to confirm before continuing.
14. **Source repo (optional)** — public GitHub URL or a local path. If provided, I'll skim the README, route definitions, and main components. Skip if proprietary or unavailable.

End the intake message with:

> Reply with whatever you have — even partial answers move us forward. If you'd rather I just guess and produce a draft, say **"just guess"** and I'll generate with assumptions called out.

**Then stop. Wait for the user's reply. Do not produce any sections from Phase 2 yet.**

### Escape hatches

- If the user's first message says **"just guess"**, **"infer"**, **"go ahead"**, **"draft anyway"**, or similar → set `mode = dry`, skip Phase 1 and Phase 1.5, run Phase 2 with assumptions explicitly called out in section 2. Default `demo_type` to `marketing` unless the wording strongly implies a walkthrough ("onboarding video", "tutorial", "step-by-step", "show how to use").
- If the user explicitly typed `--dry`, `--ground`, or `--full` in `$ARGUMENTS` → skip Step 1.2 (mode gate), accept their choice, ask only for any missing fields the chosen mode needs.
- If the user has already supplied **all required fields** in `$ARGUMENTS` (the 12 core fields plus a chosen mode) → skip Phase 1 and continue to Phase 1.5 if `mode` is `ground` or `full`, otherwise jump to Phase 2.
- If the user supplied **most** fields (≥ 9/12 core) and the missing ones are minor → ask the mode question plus a short follow-up for just the missing items, do not re-list the full questionnaire. **Never skip the demo-type or mode questions** — they change the entire output shape and runtime.

## Phase 1.5 — Grounding pass (only if `mode` is `ground` or `full`)

Skip this phase entirely if `mode = dry`. If skipped, set `grounded_via: "none"` in the context block and proceed straight to Phase 2.

Tell the user one line before starting: `> Grounding the plan against your <app|repo|both> — back in ~1–3 min.` Then do the work below before generating any plan sections.

### 1.5a — Live app exploration (if `.env` creds were confirmed)

Verify the keys exist:

```bash
test -f .env && grep -E '^DEMOFLOW_(APP_URL|USERNAME|PASSWORD)=' .env | wc -l
```

If less than 3, surface which keys are missing and ask the user to add them or say "skip live access" — do not proceed to login.

Then use Chrome DevTools MCP for a **lightweight** pass (this is plan-time grounding, not the full seeding that `/demoflow:prep` does):

1. `mcp__chrome-devtools__new_page` to `${DEMOFLOW_APP_URL}`.
2. `take_snapshot` of the login form. `fill` username + password from env. `click` submit.
3. After landing post-login, walk the primary nav: list the top-level routes, the main empty-state screens, and the create/upload entry points. **Cap this at ~8 navigations.**
4. For each screen, capture: route path, screen name as it appears in the UI, the 1–3 most prominent CTAs/buttons (verbatim text), and any obvious empty states.
5. If MFA, SSO, captcha, or a paywall blocks login → stop, do not retry, surface the blocker, and continue Phase 2 without grounding (mark `grounded_via: "none"` and add the blocker to assumptions).

Keep notes in a short running log in your head — you don't need to write a file; the goal is to inform sections 1, 5, 6, 7 of the plan with **observed** product surface instead of guesses.

### 1.5b — Repo skim (if a GitHub URL or local path was provided)

For a public GitHub URL, use `WebFetch` on the README and the routes/pages directory listing. For a local path, use `Read` and `Glob`. Look for:

- README — actual one-line description, install/run commands, claimed features.
- Route or page files (`pages/`, `app/`, `routes/`, `src/views/`) — the real list of screens.
- Auth/login flow file if obvious — confirms the login UX you'll be demoing.
- Any `demo`, `seed`, `fixtures`, or `mock` directories — existing seed data to reuse.

Cap this at ~10 file reads. Do not read the whole codebase.

### 1.5c — Reconcile

Before generating the plan, compare grounding findings to what the user said in intake. If anything contradicts (e.g. user said "drag-and-drop CSV upload" but you found no upload route), flag it in section 2 (Assumptions) under a new sub-bullet `Discrepancies found during grounding:`.

## Phase 2 — Plan generation

Run this only after intake is satisfied (user answered, said "just guess", or supplied everything upfront). Phase 3 below only runs if `mode = full` and only after the user re-confirms. Produce **all sections below in order**, in one response.

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

If grounding ran (Phase 1.5), split this section into two sub-lists:

- **Observed during grounding:** facts confirmed by live login or repo skim (real screen names, real button text, real routes, real auth flow).
- **Still inferred:** anything not directly observed.

Add a `Discrepancies found during grounding:` sub-bullet only if intake claims contradicted what you observed.

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
  "github_repo": "",
  "grounded_via": "live | repo | both | none",
  "observed_screens": [],
  "mode": "dry | ground | full",
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

Pick **exactly one**. Routing logic is **mode-aware** — guide the user toward the natural next action based on what they picked:

**If `mode = dry`:**
- Context is thin / mostly assumptions → tell them to set up `.env` and re-run `/demoflow:plan` in `ground` mode for a much better plan.
- Plan looks plausible but they want to validate against the real app → re-run with `ground`.
- They want to iterate on hooks/length/tone → `/demoflow:script`.
- Plan looks shippable as a brainstorm → `/demoflow:export`.

**If `mode = ground`:**
- Plan reads accurate and they want to record → `/demoflow:prep` to seed the app, then `/demoflow:record`.
- Discrepancies were found → fix the intake, re-run plan.
- They want to A/B different angles → `/demoflow:script`.

**If `mode = full`:** stop here — Phase 3 will handle the next step (seed → record).

Format:

> **Next:** `/demoflow:<command>` — one-sentence reason tied to the mode they picked.

Then add 2–3 other useful commands as a short list, no commentary.

## Phase 3 — Seeding (only if `mode = full`)

Skip entirely unless `mode = full`. Do not run silently — seeding writes data into the user's app and they must re-confirm after seeing the plan.

After Phase 2's section 9, append this prompt:

> **Ready to seed?** You picked `full` mode. Next step is to write mock data into `DEMOFLOW_APP_URL` and screenshot every shot — this is destructive (creates real records in that account). Reply `seed` to continue, `stop here` to keep just the plan and run `/demoflow:prep` later, or `change mode` to drop back to `ground`.

**Stop and wait.** Do not seed without explicit `seed` confirmation. Reactions:
- `seed` → continue with the seeding handoff below.
- `stop here` → end the turn. They have a complete plan + grounding; they can run `/demoflow:prep` whenever they're ready.
- `change mode` → set `mode = ground`, end the turn, no seeding.

Seeding handoff (only on `seed`):
1. Reuse the context block already in this conversation — do not re-ask anything.
2. Follow `commands/prep.md` Steps 1–3, 5–7 (seeder generation, run, report).
3. **Skip prep's Step 4 (live exploration)** — `observed_screens` is already populated from Phase 1.5a. The selectors and screen names you captured there feed directly into the seeder template.
4. When prep finishes, override section 9's recommendation: `> **Next:** /demoflow:record` — the app is now seeded and ready.

## Style rules

- Do not pretend to have inspected the URL. If a URL is given, treat the name and any provided description as primary; mark inferred features as assumptions. **If Phase 1.5 grounding ran, you *did* inspect — use real screen names, real button text, and real routes verbatim, and credit them in section 2 under "Observed during grounding".**
- **Never echo or log credentials.** Reading from `.env` is fine; printing the password back to the user is not. If you need to confirm login worked, echo only the username.
- **Cap the grounding pass.** ~8 navigations live, ~10 file reads in the repo. The plan command is not the seeder — that's `/demoflow:prep` (or Phase 3 in `full` mode).
- **Always confirm before destructive actions.** Phase 3 only runs after the user replies `seed`. Never seed silently, even if `mode = full` was set in `$ARGUMENTS`. Show the plan first, ask second, seed third.
- **Tailor the next-step recommendation to the mode.** Don't tell a `dry`-mode user "go record now" — they have no recon. Don't tell a `full`-mode user (post-seed) "run /demoflow:prep" — it's already done.
- Do not feature-dump. Translate every feature into a viewer-facing pain → action → outcome.
- **Marketing scripts** are short-form video, not pitch decks. Lines under ~15 words. No "we believe…" "our mission is…" type filler.
- **Walkthrough scripts** are literal. Every UI element named exactly. Every step is one user action. No skipped clicks. If the user has to wait for something to load, that is its own step.
- If the product context is too thin to produce a strong demo, say so plainly in section 4 ("main risk") and recommend the user run `/demoflow:plan` again with the missing details — but **still produce sections 5–8 as best-effort drafts**.
