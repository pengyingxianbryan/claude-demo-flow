# Template: Product Walkthrough

For **`demo_type = walkthrough`**.

This is the literal, step-by-step style you'd ship as: in-app onboarding video, sales-call screen-share recording, "how to use" docs page, support troubleshooting clip, or feature tutorial inside a help center.

## When to use this template

- Goal is **comprehension**, not conversion.
- The viewer is already past the marketing layer — they're a logged-in user, a prospect on a sales call, or a support requester.
- You want to show the literal happy path: every click, every field, every confirmation screen.
- Length is driven by the workflow, not by an attention-budget. Typical range: 45s for one feature, 3–5 min for full onboarding.

If the goal is to make a stranger watch and convert, use `social_shorts.md` or `founder_led.md` instead.

## Structure

Walkthroughs are step-driven, not section-driven. There is no "hook" — the viewer is already paying attention.

| Block | Purpose | Length |
|---|---|---|
| Setup (optional) | One-line context: "Let's import your transactions." | 0–3s |
| Steps | One UI action per step, in order. | bulk of the video |
| Confirmation | Show the result screen long enough to read. | 3–5s |
| Next-step hand-off (optional) | "Now you can categorise. We'll cover that next." | 2–3s |

## Step rules

1. **One UI action per step.** Click, type, drag, scroll, wait. Not "click Sign in and wait for the dashboard" — those are two steps.
2. **Name UI elements exactly as they appear.** Bold the literal label: click **Sign in**, click **+ New transaction**, drag onto **Drop a CSV here**. Mismatched labels are the #1 reason walkthrough viewers get lost.
3. **Cover the happy path only.** Unhappy paths (validation errors, edge cases) are separate walkthroughs, not asides in this one.
4. **Voiceover is instructional, second-person.** "Head to the sign-in page." "Click the email field." "You'll see your dashboard load." No "we built…" "our mission is…" "try it now!"
5. **Pace is calm.** ~3 seconds per simple click, ~6–8 seconds per typed input, ~5 seconds per "wait for screen to load" step. Do not race.
6. **Pause on the result.** After the workflow completes, hold the success screen for 3–5 seconds so the viewer reads it.

## Voiceover patterns

| Pattern | Example |
|---|---|
| Direct instruction | "Click the email field and enter your email." |
| Forward-looking | "Next, you'll add a transaction." |
| Confirmation | "You'll see the upload preview, with each column mapped to a field." |
| Hand-off | "Now your transactions are imported. Let's categorise them." |

Avoid: hooks ("Tired of manual entry?"), claims ("the easiest way to…"), CTAs that don't fit ("sign up free!"). The CTA in a walkthrough is usually implicit — the viewer is already inside the product.

## Shot list rules

One shot per step. For each shot, recording notes should specify:

- **Selector** if known (e.g. `[data-testid=upload-csv]`) — the recorder needs this.
- **Cursor motion** ("move slowly from top-right to centre, ~1.5s").
- **What to highlight** (cursor halo, soft zoom, brief outline of the clicked element).
- **What to hide** (sidebar names, account email, anything PII).
- **Timing** ("hold result screen 4s before transitioning").

## Recording checklist additions

On top of the standard checklist, walkthroughs need:

- **Clean starting state.** Every recording begins from a known screen (logged out, or a fresh empty dashboard). Reset between takes.
- **Pre-completed onboarding.** If the workflow assumes the user is past first-run setup, do that setup once off-camera so the recording starts at the actual workflow.
- **Stable test data.** Use the same fake CSV / fake project name / fake email every time. This makes retakes idempotent.
- **No real PII.** All names, emails, dollar amounts, file names should be obviously fake (`demo@example.com`, `Acme Inc`, `transactions-jan.csv`).
- **Cursor visibility.** Turn on cursor highlighting in the recorder (or post in CapCut). Walkthroughs without visible cursors are unwatchable.

## Compatibility with credentialed automation

Walkthrough mode is the **best fit** for `/demoflow:prep` → `/demoflow:record` → `/demoflow:produce`:

- The shot list maps cleanly onto Playwright actions (one click/fill/drag per shot).
- The voiceover is calm and instructional — TTS handles it well, no founder personality required.
- The recording is fully deterministic — no emotional pacing, no "feel" to nail.

For walkthroughs longer than 60 seconds, consider chunking into multiple shorter walkthroughs (one per workflow) and letting the user stitch them in CapCut. A single 4-minute auto-rendered walkthrough is harder to fix if any step glitches.

## Examples of good walkthrough framings

| Product | Walkthrough |
|---|---|
| BudgetBee | "Bulk-import a month of transactions from CSV." |
| A scheduling tool | "Connect your Google Calendar and create your first booking link." |
| A code review tool | "Open a pull request and turn on AI review." |
| A CRM | "Import 50 leads from a CSV and assign them to a sequence." |

Each is **one workflow**, end-to-end. Not "here's our whole product." A great walkthrough leaves the viewer thinking "I could do that" — not "wow, look at all those features."
