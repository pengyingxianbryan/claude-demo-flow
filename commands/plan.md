---
description: Turn product info into a full demo plan — angles, recommended script, shot list, recording checklist.
argument-hint: [product info — URL, description, audience, goal, format, platform, tone, CTA]
---

You are running `/demoflow:plan`, the entry point of the DemoFlow workflow.

## What the user gave you

`$ARGUMENTS`

(May include any of: product URL, product name, description, audience, features, demo goal, format, platform, tone, CTA. May be partial. May be a single sentence.)

## What to produce

Produce **all sections below in order**, in one response. Do not stop and ask for more info first. Make assumptions, name them, keep moving.

### 1. Product Snapshot

Compact list:
- Product name
- Product URL (or "not provided")
- Product type / category
- Target audience
- Main user pain (one sentence)
- Demo goal (one sentence)
- Preferred platform
- Tone
- CTA

### 2. Assumptions Made

Bullet every detail you inferred or guessed. If you only had a URL or product name, the list will be long — that is fine. Be honest about what is inferred. Do **not** invent specific features as if you saw them.

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

### 5. Top 5 Demo Angles

Markdown table with columns: `#`, `Angle title`, `Hook`, `Feature shown`, `Outcome shown`, `Best platform`, `Priority (1–10)`.

Angles must be distinct from each other (different hooks, different pain framings, different audiences within the niche). No generic "show the dashboard" angles. Each angle must connect a specific viewer pain to a specific product moment to a specific outcome.

### 6. Recommended 30-second Script

Pick the highest-priority angle. Write the script in this exact format:

| Time | Section | Voiceover | On-screen text | Screen / action |
|------|---------|-----------|----------------|-----------------|
| 0:00–0:03 | Hook | … | … | … |
| 0:03–0:10 | Problem | … | … | … |
| 0:10–0:22 | Product action | … | … | … |
| 0:22–0:27 | Result | … | … | … |
| 0:27–0:30 | CTA | … | … | … |

Voiceover should sound like a real founder talking to a real user. No "introducing X, the all-in-one platform for…" energy. Direct, specific, human.

### 7. Shot List

Markdown table for the recommended script. Columns: `Shot`, `Timestamp`, `Screen / page`, `Action shown`, `Voiceover line`, `On-screen caption`, `Recording note`. 4–7 shots is right.

Recording notes should be practical: cursor speed, where to zoom, what to hide, what sample data to load.

### 8. Recording Checklist

Five short groups. 3–5 bullets each. Demo-account, sample-data, browser/screen, voiceover, QC. Be specific to this product where possible (e.g. "load 6 fake freelance invoices, mix paid and unpaid").

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
- Scripts are short-form video, not pitch decks. Lines under ~15 words. No "we believe…" "our mission is…" type filler.
- If the product context is too thin to produce a strong demo, say so plainly in section 4 ("main risk") and recommend the user run `/demoflow:plan` again with the missing details — but **still produce sections 5–8 as best-effort drafts**.
