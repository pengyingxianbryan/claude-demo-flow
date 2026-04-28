"""ffmpeg pipeline: assemble final.mp4 from recording + voiceover + captions.

Usage:
    python scripts/edit.py [<session_dir>]

Inputs (in session_dir):
    recording.webm           # screen recording from /demoflow:record
    voiceover/NN.mp3         # one TTS clip per script row, in order
    plan.json                # has script.rows[] with .voiceover and .time

Outputs (in session_dir):
    voiceover.mp3            # concatenated audio
    captions.srt             # captions, timed against measured TTS durations
    final.mp4                # H.264, AAC, scaled+padded to target aspect ratio
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from util import log, read_plan, resolve_session


ASPECT_FOR_PLATFORM = {
    "tiktok": "9:16",
    "reels": "9:16",
    "shorts": "9:16",
    "instagram": "9:16",
    "linkedin": "1:1",
    "twitter": "16:9",
    "youtube": "16:9",
    "landing": "16:9",
}

DIMS = {
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
    "1:1": (1080, 1080),
}


def get_aspect(plan: dict) -> str:
    platform = (plan.get("platform") or "").lower()
    for key, ar in ASPECT_FOR_PLATFORM.items():
        if key in platform:
            return ar
    return "9:16"


def probe_duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(path),
        ]
    )
    return float(out.decode().strip())


def srt_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds - h * 3600 - m * 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def build_srt(vo_clips: list[Path], script_rows: list[dict], out_path: Path) -> None:
    blocks: list[str] = []
    t = 0.0
    for i, clip in enumerate(vo_clips):
        d = probe_duration(clip)
        row = script_rows[i] if i < len(script_rows) else {}
        text = (row.get("voiceover") or "").strip()
        start, end = t, t + d
        if text:
            blocks.append(
                f"{i + 1}\n{srt_ts(start)} --> {srt_ts(end)}\n{text}\n"
            )
        t = end
    out_path.write_text("\n".join(blocks), encoding="utf-8")


def concat_audio(vo_clips: list[Path], out_path: Path) -> None:
    list_file = out_path.parent / "_concat.txt"
    list_file.write_text(
        "\n".join(f"file '{p.resolve()}'" for p in vo_clips), encoding="utf-8"
    )
    subprocess.run(
        [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", str(list_file),
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(out_path),
        ],
        check=True,
    )
    list_file.unlink(missing_ok=True)


def render_final(
    recording: Path, audio: Path, srt: Path, aspect: str, out: Path
) -> None:
    w, h = DIMS[aspect]
    srt_arg = str(srt).replace(":", r"\:").replace("'", r"\'")
    vf = (
        f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
        f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:black,"
        f"subtitles='{srt_arg}':force_style='"
        f"Fontsize=22,Alignment=2,MarginV=80,"
        f"BorderStyle=1,Outline=2,Shadow=0,"
        f"PrimaryColour=&Hffffff&,OutlineColour=&H000000&'"
    )
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", str(recording),
            "-i", str(audio),
            "-vf", vf,
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(out),
        ],
        check=True,
    )


def main() -> int:
    session = resolve_session(sys.argv[1] if len(sys.argv) > 1 else None)
    plan = read_plan(session)

    recording = session / "recording.webm"
    if not recording.exists():
        sys.stderr.write(
            f"recording.webm missing in {session}. Run /demoflow:record first.\n"
        )
        return 2

    vo_clips = sorted((session / "voiceover").glob("*.mp3"))
    if not vo_clips:
        sys.stderr.write(
            f"No VO clips in {session}/voiceover/. Run the TTS step first.\n"
        )
        return 2

    script_rows = plan.get("script", {}).get("rows", []) or plan.get("script_rows", [])
    if len(script_rows) != len(vo_clips):
        log(
            f"WARN: {len(vo_clips)} VO clips vs {len(script_rows)} script rows — "
            "aligning by index, captions may be incomplete"
        )

    aspect = get_aspect(plan)
    log(f"Target aspect: {aspect} (platform: {plan.get('platform')!r})")

    audio = session / "voiceover.mp3"
    log(f"Concatenating {len(vo_clips)} VO clip(s) → {audio.name}")
    concat_audio(vo_clips, audio)

    srt = session / "captions.srt"
    log(f"Building captions → {srt.name}")
    build_srt(vo_clips, script_rows, srt)

    final = session / "final.mp4"
    log(f"Rendering → {final.name}")
    render_final(recording, audio, srt, aspect, final)

    size_mb = final.stat().st_size / 1024 / 1024
    dur = probe_duration(final)
    log(f"Done: {final} ({size_mb:.1f} MB, {dur:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
