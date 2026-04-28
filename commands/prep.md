---
description: Seed the demo account from .env credentials — log in, create the mock data the script describes, screenshot every shot so the script can be verified against the real app.
argument-hint: [optional: session_dir to reuse a previous prep]
---

You are running `/demoflow:prep`. This is the **credentialed** command — it logs into the user's app, creates mock data, and screenshots each shot so the script can be checked against real screens.

## Inputs

- `$ARGUMENTS` — optional. If empty, start a fresh session.
- The most recent **DemoFlow Context Block** in the conversation (from `/demoflow:plan`).
- The most recent **shot list** in the conversation.
- `.env` in the user's CWD with `DEMOFLOW_APP_URL`, `DEMOFLOW_USERNAME`, `DEMOFLOW_PASSWORD`.

If no Context Block or shot list exists in the conversation, stop:

> **No DemoFlow project found in this conversation.** Run `/demoflow:plan` first.

## Step 1 — Validate environment

Run:

```bash
test -f .env && grep -E '^DEMOFLOW_(APP_URL|USERNAME|PASSWORD)=' .env | wc -l
```

Expect `3`. If less, list which keys are missing and stop:

> Missing required keys in `.env`: `DEMOFLOW_APP_URL`, `DEMOFLOW_PASSWORD` (etc).
> Add them and re-run `/demoflow:prep`.

## Step 2 — Create the session directory

```bash
mkdir -p .demoflow
SESSION=".demoflow/$(date +%Y%m%d-%H%M)"
mkdir -p "$SESSION/screenshots"
echo "$SESSION"
```

Use this path in subsequent steps.

## Step 3 — Serialise the plan to disk

Build a `plan.json` from the most recent Context Block + shot list + script in the conversation:

```json
{
  "product_name": "...",
  "product_url": "...",
  "platform": "...",
  "demo_goal": "...",
  "shot_list": [
    { "shot": 1, "screen": "...", "url_hint": "...", "action": "...", "voiceover": "...", "caption": "..." }
  ],
  "script": {
    "rows": [
      { "time": "0:00-0:03", "section": "Hook", "voiceover": "...", "on_screen_text": "...", "screen": "..." }
    ]
  },
  "mock_data": {
    "needed": "Describe what data the demo screens need to render correctly. E.g. '30 days of transactions totalling $847 in food, $1.4k subscriptions; 4 budget categories.'"
  }
}
```

Write it to `$SESSION/plan.json` using the Write tool.

## Step 4 — Live exploration of the target app

This is the agentic part. Use the Chrome DevTools MCP tools to:

1. `mcp__chrome-devtools__new_page` to `${DEMOFLOW_APP_URL}` (read from .env via `bash -c 'source .env && echo $DEMOFLOW_APP_URL'`).
2. `take_snapshot` to inspect the login form structure.
3. `fill` username/password, `click` submit.
4. After landing post-login, navigate to each screen named in `plan.shot_list` via `navigate_page` or by clicking.
5. For each screen, `take_snapshot` to capture the DOM. Note the selectors that look stable (data-testid, ARIA roles, semantic IDs — avoid CSS class hashes).
6. Find the path to **create** the entities the demo needs (transactions, projects, etc.). Click into the create flow, take a snapshot of the form, note its selectors and required fields.

Keep notes as you go in a brief running log. **Do not generate the seeder until you have selectors for every shot.**

## Step 5 — Generate the seeder

Write `$SESSION/seed-script.py` using the Write tool. The file must:

1. Use Playwright sync API (`from playwright.sync_api import sync_playwright`).
2. Read credentials from `os.environ` (already loaded by `python-dotenv` upstream).
3. Log in.
4. Create the mock data described in `plan.mock_data.needed`. Make the data concrete, realistic, and consistent with the demo script (matching merchant names, dollar amounts, categories, dates).
5. For each entry in `plan.shot_list`, navigate to the screen and screenshot it to `screenshots/shot_<NN>.png`.
6. Print a one-line summary of what was created.

Template (adapt selectors to what you discovered in Step 4):

```python
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

SESSION = Path(__file__).parent
plan = json.loads((SESSION / "plan.json").read_text())

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 800})
    page = ctx.new_page()

    page.goto(os.environ["DEMOFLOW_APP_URL"])
    page.fill("<<login-username-selector>>", os.environ["DEMOFLOW_USERNAME"])
    page.fill("<<login-password-selector>>", os.environ["DEMOFLOW_PASSWORD"])
    page.click("<<login-submit-selector>>")
    page.wait_for_load_state("networkidle")

    # --- Seed mock data ---
    # (generated based on plan.mock_data.needed and your live exploration)

    # --- Verify each shot ---
    shots_dir = SESSION / "screenshots"
    shots_dir.mkdir(exist_ok=True)
    for i, shot in enumerate(plan["shot_list"], start=1):
        page.goto(shot.get("url_hint") or page.url)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(shots_dir / f"shot_{i:02d}.png"), full_page=False)
        print(f"shot {i:02d}: {shot['screen']}")

    browser.close()
```

## Step 6 — Run the seeder

```bash
# from the plugin install dir (CLAUDE_PLUGIN_ROOT) — call via the wrapper:
python "$CLAUDE_PLUGIN_ROOT/scripts/seed.py" "$SESSION"
```

Stream the output. If it exits non-zero, surface the error verbatim and stop.

## Step 7 — Report

Two short sections, plain text:

**Prep complete.** Session: `<path>`. Mock data created: `<one-line summary>`. Screenshots: `<count>`.

**Verify the script:** open the PNGs in `<session>/screenshots/` and walk them against the script row-by-row. If any screen disagrees with what the script claims (wrong button label, missing field, different empty state, etc.), refine the script via `/demoflow:script` or `/demoflow:review`, edit `seed-script.py` if the data needs adjusting, and re-run `python scripts/seed.py <session>`.

**Next:** record the demo yourself in your tool of choice (Loom / Tella / Screen Studio / OBS / CapCut) using the now-verified script and shot list, or run `/demoflow:export` to bundle everything for handoff.

## Style rules

- Never log credentials. Echo only the username if needed for confirmation.
- Use stable selectors when you find them (data-testid, ARIA). Fall back to text-content selectors before CSS class hashes.
- If MFA / SSO / captcha blocks login, say so plainly, do not retry, and recommend the user provision a non-MFA demo account.
