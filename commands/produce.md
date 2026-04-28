---
description: Synthesize voiceover, build captions, and render the final MP4 from the recording.
argument-hint: [optional: session_dir]
---

You are running `/demoflow:produce`. This finishes the video.

## Inputs

- `$ARGUMENTS` — optional session dir. If empty, use the most recent `.demoflow/<ts>/`.
- Session must contain `recording.webm` and `plan.json` from prior commands.
- `.env` must have `OPENAI_API_KEY` (default TTS) **or** both `ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_ID`.
- `ffmpeg` must be on PATH (`brew install ffmpeg` if missing).

## Step 1 — Resolve and validate

```bash
SESSION="${ARGUMENTS:-$(ls -1d .demoflow/*/ 2>/dev/null | sort | tail -n1)}"
test -d "$SESSION" || { echo "No session. Run /demoflow:prep + /demoflow:record first."; exit 2; }
test -f "$SESSION/recording.webm" || { echo "Missing recording.webm. Run /demoflow:record."; exit 2; }
test -f "$SESSION/plan.json" || { echo "Missing plan.json."; exit 2; }
which ffmpeg >/dev/null || { echo "ffmpeg not installed. Run: brew install ffmpeg"; exit 2; }
```

Then check that at least one TTS provider is configured:

```bash
grep -qE '^(OPENAI_API_KEY|ELEVENLABS_API_KEY)=' .env || { echo "No TTS provider in .env."; exit 2; }
```

## Step 2 — Synthesize voiceover

Read `plan.json` and walk `script.rows[]` in order. For each row with a non-empty `voiceover` field, call:

```bash
python "$CLAUDE_PLUGIN_ROOT/scripts/tts.py" "<voiceover text>" \
    --out "$SESSION/voiceover/$(printf '%02d' $N).mp3"
```

where `N` is the 1-indexed row number. Pass each row in a separate Bash call (parallelisable). If a row's voiceover is empty, skip it but still increment `N` so clip ordering matches script order.

After all clips synthesise, list them:

```bash
ls -la "$SESSION/voiceover/"
```

Confirm the count matches non-empty script rows.

## Step 3 — Render the final video

```bash
python "$CLAUDE_PLUGIN_ROOT/scripts/edit.py" "$SESSION"
```

This concatenates the VO clips, builds `captions.srt` (timed against measured TTS durations), and runs ffmpeg to scale/pad to the platform's target aspect ratio (9:16 / 16:9 / 1:1, picked from `plan.platform`), burn captions, and output `final.mp4`.

Stream output. On non-zero exit, surface the ffmpeg error and stop.

## Step 4 — Report

**Done.** `<session>/final.mp4` — `<size MB>`, `<duration s>`, aspect `<ratio>`.

Spot-check before sharing:
- Open `final.mp4` and watch the first 3 seconds (hook timing matters most).
- Confirm captions are readable and synced.
- Compare duration vs the planned script length — if drift > 20%, re-run with adjusted shot timings.

**Next:** `/demoflow:review` against the rendered video, or take it into CapCut for music + b-roll polish.

## Honest limits

- TTS is good, not great — if the demo is founder-led personal-brand material, record VO yourself instead.
- The auto-edit produces clean cuts but no music, no b-roll, no kinetic captions. That's the polish layer humans still own.
- Captions are timed against measured TTS durations (not the script's planned timestamps), so they always match the audio. The recording timing may not match — for v1 this is acceptable; the audio is what carries the video.

## Style rules

- Never log API keys. If a TTS call fails, surface the HTTP status code and message, not the headers.
- Do not retry TTS calls in a loop — fail fast and let the user fix `.env` or check provider quota.
- If `final.mp4` ends up under 5 seconds, something went wrong — flag it and recommend re-running `/demoflow:record`.
