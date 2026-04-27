# DemoFlow

A Claude Code plugin that turns a SaaS product into a recordable demo plan: angles, short-form scripts, shot lists, recording checklists, and exportable markdown. No video rendering, no API calls, no setup — just a skill and four slash commands.

## What it does

You describe your product. DemoFlow gives you:

1. **Demo angles** — different framings of the same product, ranked by priority
2. **A recommended 30-second script** — voiceover, on-screen captions, screen actions
3. **A shot list** — practical, ready for Loom / Tella / Screen Studio / OBS / CapCut
4. **A recording checklist** — demo account setup, sample data, browser/screen, VO, QC
5. **Critique + rewrite** of any draft you bring it
6. **Clean markdown export** for Notion, Google Docs, CapCut, Screen Studio

## Install

From inside Claude Code:

```
/plugin marketplace add pengyingxianbryan/claude-demo-flow
/plugin install claude-demo-flow
```

That's it. The four `/demoflow:*` commands are now available.

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

## The four commands

| Command | What it does |
|---|---|
| `/demoflow:plan` | Start here. Product info → full demo plan in one pass. |
| `/demoflow:script` | Regenerate scripts for a different angle, length, style, or platform. |
| `/demoflow:review` | Paste a script or shot list — get a critique and rewrite. |
| `/demoflow:export` | Bundle the current plan as clean copy-paste markdown. |

The skill also auto-activates without slash commands when you describe a SaaS product and ask for demo help.

## How context works

`/demoflow:plan` emits a **DemoFlow Context Block** — a fenced JSON block holding your product details. Every later command reads the most recent block in the conversation, so you don't repeat yourself.

If you want to override a field (e.g. switch platforms), just say it in your message: "use LinkedIn instead." The command will use your override.

To start a fresh project, just run `/demoflow:plan` again with new info — it emits a new context block.

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

See [`examples/finance_tracker.md`](examples/finance_tracker.md) for the full BudgetBee walkthrough and the actual quality bar each command should hit.

## Templates

Two reference patterns live in `templates/`:

- [`social_shorts.md`](templates/social_shorts.md) — TikTok / Reels / YouTube Shorts (15–45s, vertical)
- [`founder_led.md`](templates/founder_led.md) — talking-head + screen recording (LinkedIn, YouTube, landing page hero, 45–90s)

Together they cover the majority of SaaS demo cases.

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
  templates/
    social_shorts.md
    founder_led.md
  examples/
    finance_tracker.md
  README.md
```

## How to test the skill

After installing in Claude Code:

1. **Plan**: paste the BudgetBee quick-start block above. Confirm output includes a `demoflow-context` fenced block, ≥5 angles, a 30s script table, shot list, and checklist.
2. **Script**: run `/demoflow:script angle:3 length:15s style:contrarian`. Confirm it reads the prior context (doesn't re-ask product info) and outputs a fresh 15s script.
3. **Review**: paste a deliberately weak script. Confirm scorecard + 5 better hooks + rewritten version.
4. **Export**: run `/demoflow:export type:full`. Confirm output is a single copy-paste markdown block.
5. **Auto-activate**: in a fresh thread, type "I have a SaaS for freelancers, help me make a demo video." DemoFlow should engage and offer `/demoflow:plan`.

## What's intentionally not here

- No login, billing, database, or web app
- No browser automation, screenshot capture, or video rendering
- No external API calls
- No Python helpers
- No 14-command workflow — trimmed from the original spec because most commands overlap with `/demoflow:plan` and would rarely get used

## Future expansion

If real usage demands it:

- `/demoflow:variants` — A/B hook testing in bulk
- More templates (landing-page demo, before-after, problem-solution, feature-walkthrough)
- A second example for a non-finance product (e.g. devtool, B2B SaaS)
- Integration with a video-generation tool when one exists that's actually good
