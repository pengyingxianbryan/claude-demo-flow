---
description: Regenerate a demo script for a specific angle, length, platform, or style.
argument-hint: [angle: <#|description>] [length: 15s|30s|45s] [style: founder-led|pain-led|before-after|contrarian|outcome-led|educational|social-proof] [platform: tiktok|reels|shorts|linkedin|landing-page] [tone: ...]
---

You are running `/demoflow:script`.

## Inputs

`$ARGUMENTS`

May include any of:
- `angle: <number from prior plan, or freeform description>`
- `length: 15s | 30s | 45s` (default 30s)
- `style: founder-led | pain-led | before-after | contrarian | outcome-led | educational | social-proof` (default founder-led)
- `platform: tiktok | reels | shorts | linkedin | landing-page` (use prior context if missing)
- `tone: <freeform>` (use prior context if missing)

## Context

1. Find the **most recent DemoFlow Context Block** in this conversation. Use it.
2. If no Context Block exists, infer one from the user's message and emit a fresh `demoflow-context` fenced block before producing the script. Mark assumptions clearly.
3. If the user references "angle 3" (or similar) and a prior `/demoflow:plan` exists, use that angle. If no prior plan exists or the angle number is out of range, generate a reasonable angle from the context and continue.

## Output

### Selected Angle

One short paragraph: which angle you're using and why it fits the requested style.

### Script ({length}, {style})

Same five-row table format as `/demoflow:plan`, scaled to the requested length:

| Time | Section | Voiceover | On-screen text | Screen / action |

For 15s: hook (0–2s) → problem (2–5s) → product action (5–11s) → result + CTA (11–15s).
For 30s: hook (0–3s) → problem (3–10s) → product action (10–22s) → result (22–27s) → CTA (27–30s).
For 45s: hook (0–3s) → problem (3–12s) → product action (12–32s) → result (32–40s) → CTA (40–45s).

Voiceover lines must sound like the chosen style:
- **founder-led:** "I built this because…" / "Here's how I…"
- **pain-led:** lead with the painful moment, no setup
- **before-after:** show the messy before, then the clean after
- **contrarian:** challenge a widely-held belief in the niche
- **outcome-led:** open on the result, then explain how
- **educational:** teach a small thing, product is the demonstration tool
- **social-proof:** open with a specific user/number

### 2 Alternative Hooks

Just the opening line + one-sentence reason it might outperform the main hook. Two options.

### 2 Alternative CTAs

Same format. Two options.

### Recommended Next Step

> **Next:** `/demoflow:review` — paste this script back to get a critique and rewrite before recording.

Or, if the user clearly wants to A/B test more angles:

> **Next:** `/demoflow:script angle:<N> style:<different>` — try another variant.

Pick one. Don't list both.

## Style rules

- Do not re-emit the full plan. Just the script + alternatives.
- Do not change the product context unless the user explicitly overrides a field.
- Lines under ~15 words.
- No "introducing" / "we're excited to" / "the all-in-one" phrasing.
- Specific over generic. Name the screen, name the action, name the outcome.
