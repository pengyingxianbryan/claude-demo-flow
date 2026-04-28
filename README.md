# DemoFlow

A Claude Code plugin that turns a SaaS product into a recordable demo plan: angles, short-form scripts, shot lists, recording checklists, and exportable markdown. With optional credentialed automation, it can also seed mock data, capture the recording, and render a finished MP4.

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

## Commands

**Planning (no credentials needed):**

| Command | What it does |
|---|---|
| `/demoflow:plan` | Start here. Product info → full demo plan in one pass. |
| `/demoflow:script` | Regenerate scripts for a different angle, length, style, or platform. |
| `/demoflow:review` | Paste a script or shot list — get a critique and rewrite. |
| `/demoflow:export` | Bundle the current plan as clean copy-paste markdown. |

**Credentialed automation (optional, requires `.env`):**

| Command | What it does |
|---|---|
| `/demoflow:prep` | Log into the app, seed the mock data the script needs, screenshot every shot. |
| `/demoflow:record` | Drive Playwright through the shot list, capture a screen recording. |
| `/demoflow:produce` | Synthesize voiceover, burn captions, render `final.mp4` (9:16 / 16:9 / 1:1). |

`/demoflow:plan` itself can also do read-only credentialed work if a `.env` is present — see [Grounding the plan against your real product](#grounding-the-plan-against-your-real-product-v060) below.

The skill also auto-activates without slash commands when you describe a SaaS product and ask for demo help.

## How context works

`/demoflow:plan` emits a **DemoFlow Context Block** — a fenced JSON block holding your product details. Every later command reads the most recent block in the conversation, so you don't repeat yourself.

If you want to override a field (e.g. switch platforms), just say it in your message: "use LinkedIn instead." The command will use your override.

To start a fresh project, just run `/demoflow:plan` again with new info — it emits a new context block.

## Grounding the plan against your real product (v0.6.0+)

Plans drafted from descriptions alone tend to be generic — they invent screen names, miss real flows, and pick angles that don't match what your product actually does. To fix this, `/demoflow:plan` now asks two optional questions during intake:

1. **Live access** — if you have a `.env` with `DEMOFLOW_APP_URL`, `DEMOFLOW_USERNAME`, and `DEMOFLOW_PASSWORD`, plan will log in and walk the primary nav (capped at ~8 navigations) before drafting.
2. **Source repo** — public GitHub URL or local path. Plan reads the README, route definitions, and main components (capped at ~10 file reads) to confirm what the product actually surfaces.

When grounding runs, section 2 of the output splits into **Observed during grounding** (real screen names, real button text, real routes) versus **Still inferred**. Any contradictions between your intake answers and what was observed get called out under a `Discrepancies` sub-bullet.

The context block schema gains three fields downstream commands can use:

```jsonc
{
  "github_repo": "",
  "grounded_via": "live | repo | both | none",
  "observed_screens": []
}
```

**Security note:** never paste passwords into chat. If you don't already have a `.env`, say "skip live access" and plan will run from descriptions only.

**What grounding *doesn't* do:** it does not seed mock data, generate the Playwright seeder, or screenshot every shot. That's still `/demoflow:prep`. Grounding is read-only recon to inform the plan; prep makes the app demo-ready for recording.

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

Walkthroughs are the **best fit** for the credentialed automation path — they map cleanly onto Playwright actions (one click/fill/drag per shot), and instructional voiceover sounds natural via TTS.

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
    prep.md                             # credentialed: data seeding
    record.md                           # credentialed: screen recording
    produce.md                          # TTS + ffmpeg → final.mp4
  scripts/                              # Python automation
    util.py
    seed.py
    record.py
    tts.py
    edit.py
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

## Credentialed automation

If you want DemoFlow to actually produce the video — not just plan it — you'll need a `.env` file with credentials.

### Where the `.env` file goes

Create it **at the root of the project where you're running Claude Code** — i.e. the working directory you launched `claude` from, not the plugin install directory. The credentialed commands (`/demoflow:prep`, `/demoflow:record`, `/demoflow:produce`) read `.env` from `process.cwd()`.

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
# Required for /demoflow:prep and /demoflow:record
DEMOFLOW_APP_URL=https://app.example.com/login
DEMOFLOW_USERNAME=demo@example.com
DEMOFLOW_PASSWORD=your-password-here

# Required for /demoflow:produce — pick ONE TTS provider:

# Option A: OpenAI (default, simpler)
OPENAI_API_KEY=sk-...
DEMOFLOW_TTS_VOICE=alloy           # optional: alloy | echo | fable | onyx | nova | shimmer

# Option B: ElevenLabs (better voice quality, your own clone)
ELEVENLABS_API_KEY=...
ELEVENLABS_VOICE_ID=...            # find in ElevenLabs dashboard → Voices
```

If both providers are set, ElevenLabs wins.

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
brew install ffmpeg                    # macOS — for Linux: apt/pacman/etc.
```

### Run the pipeline

After `/demoflow:plan` (in walkthrough mode for best results):

```
/demoflow:prep      # logs in, seeds mock data, verifies each screen with a screenshot
/demoflow:record    # drives Playwright through the shot list, saves recording.webm
/demoflow:produce   # TTS + ffmpeg → final.mp4
```

All artifacts land in `<your-project>/.demoflow/<YYYYMMDD-HHMM>/`. Each run creates a new timestamped session — old sessions stay untouched until you delete them.

### Rotating credentials

If your demo password changes, edit `.env` directly and re-run `/demoflow:prep`. There's nothing cached — the scripts read fresh from `.env` on every invocation.

### Honest limits

1. **Selector drift.** Generic SaaS apps change their DOM. The seeder is regenerated from live exploration on every `/demoflow:prep` run, so this self-heals — but expect the occasional retry.
2. **Auth friction.** Apps with SSO, MFA, or captcha will block prep. Provision a non-MFA demo account.
3. **Founder-led demos.** Talking-head shots are not automatable. `/demoflow:record` warns and asks you to confirm before capturing screen-only.
4. **TTS uncanny valley.** OpenAI `alloy` is decent but recognisable. Bring your own voice via ElevenLabs if it matters.
5. **Polish ceiling.** Auto-edit cuts are clean but boring. Music, b-roll, kinetic typography belong in CapCut. Output is a watchable rough cut, not a viral hook.

## Future expansion

If real usage demands it:

- `/demoflow:variants` — A/B hook testing in bulk
- More templates (landing-page demo, before-after, problem-solution, feature-walkthrough)
- A second example for a non-finance product (e.g. devtool, B2B SaaS)
- Integration with a video-generation tool when one exists that's actually good
