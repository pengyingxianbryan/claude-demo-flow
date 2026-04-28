# DemoFlow

A Claude Code plugin that turns a SaaS product into **accurate demo scripts** — angles, short-form scripts, shot lists, recording checklists, and exportable markdown. Optionally grounds the script against your real product via credentialed login, seeded mock data, and per-shot screenshots so you can verify before recording.

## What it does

You describe your product. DemoFlow gives you:

1. **Demo angles** — different framings of the same product, ranked by priority
2. **A recommended 30-second script** — voiceover, on-screen captions, screen actions
3. **A shot list** — practical, ready for Loom / Tella / Screen Studio / OBS / CapCut
4. **A recording checklist** — demo account setup, sample data, browser/screen, VO, QC
5. **Critique + rewrite** of any draft you bring it
6. **Clean markdown export** for Notion, Google Docs, CapCut, Screen Studio
7. **Optional script verification** — log in to your real app, seed mock data, screenshot every shot so you can walk the script against actual screens before recording

## Install

From inside Claude Code:

```
/plugin marketplace add pengyingxianbryan/claude-demo-flow
/plugin install claude-demo-flow
```

That's it. The five `/demoflow:*` commands are now available.

To update later:

```
/plugin marketplace update claude-demo-flow
/plugin install claude-demo-flow
```

To uninstall:

```
/plugin uninstall claude-demo-flow
/plugin marketplace remove claude-demo-flow
```

### Local development

If you've cloned the repo and want to install from your local checkout:

```
/plugin marketplace add /path/to/claude-demo-flow
/plugin install claude-demo-flow
```

## Commands

**Planning (no credentials needed):**

| Command | What it does |
|---|---|
| `/demoflow:plan` | Start here. Product info → full demo plan in one pass. |
| `/demoflow:script` | Regenerate scripts for a different angle, length, style, or platform. |
| `/demoflow:review` | Paste a script or shot list — get a critique and rewrite. |
| `/demoflow:export` | Bundle the current plan as clean copy-paste markdown. |

**Credentialed verification (optional, requires `.env`):**

| Command | What it does |
|---|---|
| `/demoflow:prep` | Log into the app, seed the mock data the script describes, screenshot every shot so you can verify the script against the real app. |

`/demoflow:plan` itself can also do read-only credentialed work if a `.env` is present — see [Plan modes](#plan-modes--tiered-grounding-v090) below.

The skill also auto-activates without slash commands when you describe a SaaS product and ask for demo help.

## How context works

`/demoflow:plan` emits a **DemoFlow Context Block** — a fenced JSON block holding your product details. Every later command reads the most recent block in the conversation, so you don't repeat yourself.

If you want to override a field (e.g. switch platforms), just say it in your message: "use LinkedIn instead." The command will use your override.

To start a fresh project, just run `/demoflow:plan` again with new info — it emits a new context block.

## Plan modes — tiered grounding (v0.9.0+)

`/demoflow:plan` asks **how deep you want it to go** before any other intake questions. The mode you pick changes which questions get asked, what the command does in the background, and what gets recommended next.

| Mode | What runs | Time | Touches the app? |
|---|---|---|---|
| `dry` | Plan only, pure description-based. No `.env` needed. | ~30s | No |
| `ground` | Plan + read-only recon (login, walk screens, capture real names + selectors) before drafting. **Default if `.env` is present.** | ~1–3 min | Reads only |

Data seeding is a separate, opt-in step via `/demoflow:prep` — it never runs from inside `/demoflow:plan`.

### How plan guides you

1. **First turn**: plan asks which mode you want, with a one-sentence pitch for each. Pick `dry` or `ground`. If you have a `.env`, `ground` is the default.
2. **Second turn**: plan asks the relevant intake questions (skips `.env` + repo questions in `dry` mode).
3. **Phase 1.5** (only if `ground`): read-only recon. Logs in, walks screens, captures real screen names + button text. Reads README + routes if you gave a repo.
4. **Phase 2**: produces the plan. Section 2 splits into **Observed during grounding** vs **Still inferred**. Any discrepancies between your intake and what was observed get flagged.
5. **Section 9 — Recommended Next Step**: tailored to your mode. `dry` users get "set up `.env` and re-run with `ground`"; `ground` users get "run `/demoflow:prep` to verify the script against the real app".

### Skipping the mode question

You can pass mode as a flag to skip Step 1.2: `/demoflow:plan --ground`. The user prompt also accepts `dry` / `ground` as a one-word reply at the mode gate. Saying **"just guess"** at any point sets `mode = dry` and produces a description-only plan with assumptions called out.

### Context block fields

The context block downstream commands read includes:

```jsonc
{
  "github_repo": "",
  "grounded_via": "live | repo | both | none",
  "observed_screens": [],
  "mode": "dry | ground"
}
```

`/demoflow:prep` reuses `observed_screens` to skip its own exploration pass when the plan already did it.

### Security & destructive-action rules

- **Never paste passwords into chat.** Plan refuses inline passwords and walks you through `cp .env.example .env` if needed.
- `/demoflow:prep` is the only command that writes to your app; you invoke it explicitly. Use a non-MFA, non-production demo account. Seeding into a real customer-facing account is on you.

## Quick start

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

Then optionally:

```
/demoflow:script angle: 3 length: 15s style: contrarian platform: tiktok
```

```
/demoflow:review

(paste your draft script)
```

```
/demoflow:export type: full
```

Two end-to-end examples set the quality bar:

- [`examples/finance_tracker_conversion.md`](examples/finance_tracker_conversion.md) — marketing demo (30s social short with hooks, angles, talking-head + screen)
- [`examples/finance_tracker_walkthrough.md`](examples/finance_tracker_walkthrough.md) — product walkthrough (90s in-app onboarding: sign-in → drag-and-drop CSV → confirm import)

## Two demo types

`/demoflow:plan` asks up front which kind of demo you want. The output shape changes accordingly:

| Type | When to pick it | Output |
|---|---|---|
| **Marketing** | Reel / Short / LinkedIn / landing page. Goal is conversion. | 5 angles, 30s hook-led script, 4–7-shot list. |
| **Walkthrough** | Onboarding / sales call / docs / tutorial. Goal is comprehension. | One literal step-by-step script: sign-in page → click email → type password → click **Sign in** → click **+ New transaction** → drag CSV → confirm. 8–20 shots. |

## Templates

Three reference patterns in `templates/`:

- [`social_shorts.md`](templates/social_shorts.md) — TikTok / Reels / YouTube Shorts (marketing)
- [`founder_led.md`](templates/founder_led.md) — talking-head + screen recording (marketing)
- [`product_walkthrough.md`](templates/product_walkthrough.md) — literal step-by-step product walkthroughs

Walkthroughs are the **best fit** for `/demoflow:prep` — they map cleanly onto Playwright actions (one click/fill/drag per shot), so the seeder can populate the app and screenshot every step for verification.

## Repo layout

```
claude-demo-flow/                       # marketplace + plugin root
  .claude-plugin/
    marketplace.json                    # marketplace manifest
    plugin.json                         # plugin manifest
  skills/
    demoflow/SKILL.md                   # auto-activating skill
  commands/                             # slash commands
    plan.md
    script.md
    review.md
    export.md
    prep.md                             # credentialed: seed + screenshot for script verification
  scripts/                              # Python automation
    util.py
    seed.py
  templates/
    social_shorts.md
    founder_led.md
    product_walkthrough.md
  examples/
    finance_tracker_conversion.md       # marketing demo example
    finance_tracker_walkthrough.md      # product walkthrough example
  requirements.txt
  README.md
```

## How to test the skill

After installing in Claude Code:

1. **Plan**: paste the BudgetBee quick-start block above. Confirm output includes a `demoflow-context` fenced block (now with `github_repo`, `grounded_via`, `observed_screens` fields), ≥5 angles, a 30s script table, shot list, and checklist.
2. **Plan with grounding**: drop a `.env` with valid `DEMOFLOW_*` keys into your project root, run `/demoflow:plan`, and answer "yes" when it asks about live access. Confirm it spends ~1–3 minutes exploring before drafting, and that section 2 contains an "Observed during grounding" sub-list with real screen names from your app.
3. **Script**: run `/demoflow:script angle:3 length:15s style:contrarian`. Confirm it reads the prior context (doesn't re-ask product info) and outputs a fresh 15s script.
4. **Review**: paste a deliberately weak script. Confirm scorecard + 5 better hooks + rewritten version.
5. **Export**: run `/demoflow:export type:full`. Confirm output is a single copy-paste markdown block.
6. **Auto-activate**: in a fresh thread, type "I have a SaaS for freelancers, help me make a demo video." DemoFlow should engage and offer `/demoflow:plan`.

## Credentialed verification

If you want DemoFlow to ground the script against your real product — not just plan from a description — you'll need a `.env` file with credentials.

### Where the `.env` file goes

Create it **at the root of the project where you're running Claude Code** — i.e. the working directory you launched `claude` from, not the plugin install directory. `/demoflow:prep` (and `ground`-mode `/demoflow:plan`) read `.env` from `process.cwd()`.

For most users, that means:

```
~/Projects/my-demo-project/        ← you launched `claude` here
├── .env                           ← put credentials here
├── .demoflow/                     ← session artifacts land here (auto-created, gitignored)
└── (your other project files)
```

If you don't have a dedicated demo project yet, create one:

```bash
mkdir ~/demo-runs && cd ~/demo-runs
claude
```

Then create `.env` in `~/demo-runs/`.

### What goes in `.env`

```bash
# Required for /demoflow:prep and ground-mode /demoflow:plan
DEMOFLOW_APP_URL=https://app.example.com/login
DEMOFLOW_USERNAME=demo@example.com
DEMOFLOW_PASSWORD=your-password-here
```

### Make sure `.env` is gitignored

The plugin ships a `.gitignore` that excludes `.env` and `.demoflow/`. If you're adding `.env` to a repo that doesn't have those entries yet:

```bash
echo -e ".env\n.demoflow/" >> .gitignore
```

Verify before committing anything:

```bash
git check-ignore .env && echo "ignored ✓"
```

### One-time install

```bash
pip install -r requirements.txt        # from the plugin directory, or copy requirements.txt into your project
playwright install chromium
```

### Run verification

After `/demoflow:plan` (in `ground` mode, walkthrough demo type for best results):

```
/demoflow:prep      # logs in, seeds mock data, screenshots every shot for verification
```

All artifacts land in `<your-project>/.demoflow/<YYYYMMDD-HHMM>/`. Each run creates a new timestamped session — old sessions stay untouched until you delete them. Walk the screenshots row-by-row against the script; if anything disagrees, refine via `/demoflow:script` or `/demoflow:review` and re-run prep.

### Rotating credentials

If your demo password changes, edit `.env` directly and re-run `/demoflow:prep`. There's nothing cached — the scripts read fresh from `.env` on every invocation.

### Honest limits

1. **Selector drift.** Generic SaaS apps change their DOM. The seeder is regenerated from live exploration on every `/demoflow:prep` run, so this self-heals — but expect the occasional retry.
2. **Auth friction.** Apps with SSO, MFA, or captcha will block prep. Provision a non-MFA demo account.
3. **Recording is on you.** This repo plans and verifies the script. The actual screen recording, voiceover capture, editing, music, and polish happen in your tool of choice (Loom / Tella / Screen Studio / OBS / CapCut).

## Future expansion

If real usage demands it:

- `/demoflow:variants` — A/B hook testing in bulk
- More templates (landing-page demo, before-after, problem-solution, feature-walkthrough)
- A second example for a non-finance product (e.g. devtool, B2B SaaS)
- Integration with a video-generation tool when one exists that's actually good
