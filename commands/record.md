---
description: Drive Playwright through the shot list and capture a screen recording.
argument-hint: [optional: session_dir]
---

You are running `/demoflow:record`. This captures the raw screen video.

## Inputs

- `$ARGUMENTS` — optional session dir. If empty, use the most recent `.demoflow/<ts>/`.
- The most recent **DemoFlow Context Block**, **shot list**, and **script** in the conversation.
- The session must already have `seed-script.py` and verified screenshots from `/demoflow:prep`.

## Step 1 — Resolve session

```bash
SESSION="${ARGUMENTS:-$(ls -1d .demoflow/*/ 2>/dev/null | sort | tail -n1)}"
test -d "$SESSION" || { echo "No session. Run /demoflow:prep first."; exit 2; }
test -f "$SESSION/plan.json" || { echo "Missing plan.json in $SESSION"; exit 2; }
echo "$SESSION"
```

## Step 2 — Confirm style is compatible

Read `plan.json` and check `demo_format` / `script.style`. If it mentions **founder-led** or **talking-head**, warn:

> This recording style needs a face on camera. `/demoflow:record` only captures the headless browser — you'll get the screen segments, not the talking head. Continue? (Or use the manual checklist instead.)

If the user confirms, proceed. Otherwise stop.

## Step 3 — Generate the recorder

Write `$SESSION/record-script.py` using the Write tool. It must:

1. Launch Playwright with `record_video_dir=session_dir, record_video_size={"width": 1280, "height": 800}`.
2. Re-use the login flow from `seed-script.py` (read those selectors back, or import from it).
3. Walk the shot list in order. For each shot:
   - `page.goto(shot.url_hint)` if available, else `page.click(...)` to navigate.
   - Wait for the screen to settle (`wait_for_load_state("networkidle")`).
   - Hold for `duration` seconds derived from the script row's `time` (parse `0:00-0:03` → 3 seconds; default 3s if absent).
   - Optionally trigger one cursor motion or click that matches the shot's `action` field, slowly (use `page.mouse.move` with steps).
4. After all shots, close the context — Playwright finalises the video to `<session>/<random>.webm`. Rename it to `recording.webm`.

Template:

```python
import json
import os
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

SESSION = Path(__file__).parent
plan = json.loads((SESSION / "plan.json").read_text())


def parse_duration(time_str: str, default: float = 3.0) -> float:
    if not time_str or "-" not in time_str:
        return default
    a, b = time_str.split("-")
    def to_sec(t):
        m, s = t.split(":")
        return int(m) * 60 + int(s)
    return max(0.5, to_sec(b) - to_sec(a))


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 800},
        record_video_dir=str(SESSION),
        record_video_size={"width": 1280, "height": 800},
    )
    page = ctx.new_page()

    page.goto(os.environ["DEMOFLOW_APP_URL"])
    page.fill("<<login-username-selector>>", os.environ["DEMOFLOW_USERNAME"])
    page.fill("<<login-password-selector>>", os.environ["DEMOFLOW_PASSWORD"])
    page.click("<<login-submit-selector>>")
    page.wait_for_load_state("networkidle")

    rows = plan.get("script", {}).get("rows", [])
    shots = plan.get("shot_list", [])
    for i, shot in enumerate(shots):
        url = shot.get("url_hint")
        if url:
            page.goto(url)
        page.wait_for_load_state("networkidle")
        # optional cursor motion / click matching shot.action
        dur = parse_duration(rows[i].get("time", "")) if i < len(rows) else 3.0
        page.wait_for_timeout(int(dur * 1000))

    ctx.close()  # finalise the video
    browser.close()

# Rename Playwright's auto-named webm
webms = sorted(SESSION.glob("*.webm"))
if webms:
    shutil.move(str(webms[-1]), str(SESSION / "recording.webm"))
    print(f"recording.webm written: {(SESSION / 'recording.webm').stat().st_size} bytes")
```

## Step 4 — Run the recorder

```bash
python "$CLAUDE_PLUGIN_ROOT/scripts/record.py" "$SESSION"
```

Stream output. If it exits non-zero, surface the error and stop.

## Step 5 — Report

**Recording captured.** `<session>/recording.webm` — `<size MB>`, `<duration s>` (target: `<script length>`).

If the duration is more than ±20% off target, flag it: too short means clicks failed; too long means the per-shot wait is too aggressive.

**Next:** `/demoflow:produce` to add voiceover and render the final MP4.

## Style rules

- Headless only — never open a visible browser window.
- If a click selector fails, the recorder should `page.screenshot` an error frame to `screenshots/error_shot_NN.png` and continue, not abort. Surface this in the report.
- Do not loop the recorder if it fails — diagnose and edit `record-script.py` instead.
