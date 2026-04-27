---
description: Critique a demo script, shot list, or plan and produce a rewritten version.
argument-hint: [paste the script / shot list / plan to critique]
---

You are running `/demoflow:review`.

## What the user gave you

`$ARGUMENTS`

(May be a script, a shot list, a full plan, or a fragment. Treat whatever they pasted as the artifact under review.)

## Context

Find the latest **DemoFlow Context Block** in this conversation if one exists. Use it to judge whether the artifact actually matches the product, audience, pain, and CTA. If no Context Block exists, judge the artifact on its own and note that you don't have product context.

## Output

### Verdict

One line: **Strong / Okay / Weak** + a single-sentence reason.

### Scorecard

Markdown table. Columns: `Area`, `Score /10`, `What works`, `What's weak`, `Fix`.

Rows (use only the ones that apply to what was pasted):
- Hook
- Pain clarity
- Product action
- Outcome clarity
- Pacing
- Visual clarity
- CTA
- Trust / believability
- Platform fit

Be honest. If the hook is generic, say so. If the product action is vague, say so. Don't pad.

### What to cut

Bullets. Anything that's filler, slow, off-topic, or weakens the hook.

### What to make clearer

Bullets. Specific lines or shots that need sharper wording or visual proof.

### 5 Better Hooks

Numbered list. Each is a single opening line. Mix styles (pain-led, contrarian, outcome-led, social-proof, founder-led).

### 5 Better CTAs

Numbered list. Each is one short line. Vary the ask (free trial, free tool, waitlist, DM, comment, link in bio).

### Improved Version

Rewrite the artifact in the same shape it was pasted (table for a script, table for a shot list, full plan if a plan was pasted). Apply the fixes from the scorecard. Keep it under the same length as the original.

### Recommended Next Step

Pick one:
- If the rewrite is shippable → `/demoflow:export` to bundle the final plan.
- If the user might want to test more variants → `/demoflow:script style:<different>`.
- If the underlying angle is the real problem → `/demoflow:plan` again with sharper context.

Format:

> **Next:** `/demoflow:<command>` — one-sentence reason.

## Style rules

- Critique like a peer, not a coach. Direct, specific, actionable. No "consider exploring…" hedging.
- Name the line you're criticizing. Quote it.
- The improved version must be visibly better, not just reworded.
