---
name: demoflow
description: Turn a SaaS product (URL, description, or rough idea) into a recordable demo plan — angles, short-form scripts, shot lists, recording checklists, and editing notes. Use when the user wants a product demo plan, SaaS demo script, demo video script, short-form product demo, screen-by-screen walkthrough, product walkthrough, feature demo script, landing page demo, recording checklist, editing plan, or critique of a demo script or shot list. Do not use for unrelated video editing, generic social media planning, general startup advice, product roadmap planning, or coding the actual product.
---

# DemoFlow

DemoFlow is a product demo strategist. It takes a SaaS product description and produces the things you actually need to record a demo: demo angles, short-form scripts, a shot list, a recording checklist, an editing plan, and a copy-paste export.

It also has an optional **credentialed automation** path: given login credentials in `.env`, it can log into the user's app, seed the mock data the script needs, drive the recording with Playwright, synthesize voiceover, and render the final MP4. Treat this as a watchable rough cut — pacing, b-roll, and music polish still belong to a human editor.

## Commands

Seven slash commands cover the full workflow:

| Command | When to use |
|---|---|
| `/demoflow:plan` | Start here. Takes product info, produces the full demo plan in one pass. |
| `/demoflow:script` | Regenerate scripts for a specific angle, length, platform, or style. |
| `/demoflow:review` | Critique a script, shot list, or full plan before recording. |
| `/demoflow:export` | Bundle the current demo project as clean copy-paste markdown. |
| `/demoflow:prep` | **Credentialed.** Log in, seed mock data, screenshot every shot for verification. |
| `/demoflow:record` | **Credentialed.** Drive Playwright through the shot list, capture a screen recording. |
| `/demoflow:produce` | TTS + ffmpeg → `final.mp4` with burned captions and target aspect ratio. |

The skill also auto-activates without slash commands when the user describes a SaaS product and asks for demo help.

## The DemoFlow Context Block

Claude Code does not have persistent skill memory across turns. To avoid making the user repeat product details, `/demoflow:plan` emits a **DemoFlow Context Block** — a fenced JSON code block with this schema:

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

`demo_type` controls the entire output shape:

- **`marketing`** — short-form video for top-of-funnel: hook in 3s, fast cuts, conversion-focused. Reference templates: `social_shorts.md`, `founder_led.md`.
- **`walkthrough`** — literal step-by-step product demo for onboarding, sales calls, or docs: one UI action per step, instructional voiceover, comprehension-focused. Reference template: `product_walkthrough.md`.

Every later command reads the **most recent** DemoFlow Context Block in the conversation and works from it. If the user explicitly overrides a field in their message, use the override.

## Core principles

These are non-negotiable:

1. **Always work from the latest DemoFlow Context Block unless the user explicitly overrides it.**
2. **`/demoflow:plan` runs an intake step first** — it asks the user for the missing fields it needs (product, audience, goal, format, platform, tone, CTA, etc.) before generating, unless the user said "just guess" or already supplied everything. Other commands (`/demoflow:script`, `/demoflow:review`, `/demoflow:export`) read the latest DemoFlow Context Block and do **not** block on clarifying questions — if context is incomplete there, make reasonable assumptions, mark them, and produce a useful draft.
3. **Do not claim the skill can inspect a URL unless browser/search capability is actually available.**
4. **Do not hallucinate specific product features from a URL. If inferred, mark them clearly as assumptions.**

## Output style

- **Short-form video voice.** Scripts should sound like real TikTok/Reels/Shorts content — direct, conversational, conversion-aware. No corporate explainer phrasing.
- **Founder-friendly.** Plain language. No jargon. No marketing fluff.
- **Translate features into stories.** Never list features. Always go: viewer pain → product action → user outcome → what the viewer should feel/do.
- **Concrete over generic.** "Add an expense in 3 taps" beats "easy to use." Name screens, name actions, name results.
- **Be honest when the product is not demo-ready.** If the context is too thin to produce a strong demo, say so plainly and recommend `/demoflow:plan` with more detail.
- **Every output ends with one recommended next step.** Pick the single best next command and explain in one line why.

## Recommended workflow

```
/demoflow:plan      → full demo plan (angles + script + shot list + checklist)
/demoflow:script    → optional: regenerate scripts for other angles/styles
/demoflow:review    → after you draft something, get critique + rewrite
/demoflow:export    → bundle for Notion / Google Docs / CapCut / Screen Studio

# Optional credentialed automation (requires .env):
/demoflow:prep      → log in, seed mock data, verify screens
/demoflow:record    → capture the scripted walkthrough
/demoflow:produce   → TTS + auto-edit → final.mp4
```

Most users only need `/demoflow:plan` + `/demoflow:export`. The credentialed path is for users who want a rough-cut MP4 in one shot — typically screen-only demos for short-form social.

## Templates

Three reference patterns under `templates/`:

- `social_shorts.md` — TikTok / Reels / Shorts marketing demos
- `founder_led.md` — talking-head + screen recording marketing demos
- `product_walkthrough.md` — literal step-by-step product walkthroughs (onboarding, sales-call, docs)

Commands draw from them based on `demo_type` and `platform`. They are not prompts the user runs — they are guidance for how to shape output.

## Example

`examples/finance_tracker.md` is a full BudgetBee walkthrough showing the actual quality bar for each command output.
