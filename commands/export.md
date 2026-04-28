---
description: Bundle the current demo project as clean copy-paste markdown.
argument-hint: [type: full|script_only|shot_list_only|checklist_only] (default: full)
---

You are running `/demoflow:export`.

## Inputs

`$ARGUMENTS`

Optional `type`:
- `full` (default) — everything: context, demo plan, script, shot list, checklist
- `script_only` — just the recommended script table
- `shot_list_only` — just the shot list table
- `checklist_only` — just the recording checklist

## Context

Pull from the conversation:
1. The **most recent DemoFlow Context Block**
2. The **most recent script** (from `/demoflow:plan` or `/demoflow:script`, whichever is newer)
3. The **most recent shot list**
4. The **most recent recording checklist**
5. If `/demoflow:review` produced an "Improved Version", prefer that over the original.

If no Context Block exists, say so plainly and stop:

> **No DemoFlow project found in this conversation.** Run `/demoflow:plan` first.

## Output

Wrap everything in a single fenced markdown code block so the user can copy-paste cleanly into Notion / Google Docs / CapCut / Screen Studio.

Inside the code block, structure (for `type: full`):

```markdown
# {Product name} — Demo Plan

## Product context
- Audience: …
- Pain: …
- Demo goal: …
- Platform: …
- Tone: …
- CTA: …

## Recommended script ({length}, {style})

| Time | Section | Voiceover | On-screen text | Screen / action |
| --- | --- | --- | --- | --- |
| … |

## Shot list

| Shot | Timestamp | Screen | Action | Voiceover | Caption | Note |
| --- | --- | --- | --- | --- | --- | --- |
| … |

## Recording checklist

**Demo account**
- …

**Sample data**
- …

**Browser & screen**
- …

**Voiceover**
- …

**QC**
- …
```

For partial exports (`script_only`, `shot_list_only`, `checklist_only`), output only the relevant section, still wrapped in a copy-paste code block.

## After the code block

Outside the block, give the user two paths — automated and manual:

**Verify it (credentialed):**
- `/demoflow:prep` — log into the app from `.env`, seed the mock data the script describes, and screenshot every shot so you can walk the script against real screens before recording.

Then record the demo yourself in your tool of choice (Loom / Tella / Screen Studio / OBS / CapCut) using the verified script and checklist above.

**Iterate:** `/demoflow:review` once you have a draft, or `/demoflow:script` to try another angle.

## Style rules

- The exported markdown must render cleanly in Notion and Google Docs (standard tables, no nested fenced blocks inside the outer block).
- Do not add commentary inside the export block. The user wants to paste it as-is.
- Keep the plain "what to do next" line outside the block, not inside.
