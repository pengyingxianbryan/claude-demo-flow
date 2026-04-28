"""Generate one TTS clip for a DemoFlow voiceover line.

Usage:
    python scripts/tts.py "<voiceover line>" --out path/to/01.mp3 [--voice alloy]

Provider selection:
    - If ELEVENLABS_API_KEY is set, use ElevenLabs (also requires ELEVENLABS_VOICE_ID).
    - Else if OPENAI_API_KEY is set, use OpenAI tts-1 (default voice: alloy).
    - Else exit non-zero with a clear error.

Output is mono 24kHz mp3 suitable for ffmpeg muxing.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from util import load_env, log


def synth_openai(text: str, out: Path, voice: str) -> None:
    from openai import OpenAI

    client = OpenAI()
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=voice,
        input=text,
        response_format="mp3",
    ) as resp:
        resp.stream_to_file(str(out))


def synth_elevenlabs(text: str, out: Path, voice_id: str) -> None:
    import requests

    api_key = os.environ["ELEVENLABS_API_KEY"]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    body = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }
    r = requests.post(url, headers=headers, json=body, timeout=60)
    r.raise_for_status()
    out.write_bytes(r.content)


def main() -> int:
    load_env()
    p = argparse.ArgumentParser()
    p.add_argument("text")
    p.add_argument("--out", required=True)
    p.add_argument("--voice", default=os.environ.get("DEMOFLOW_TTS_VOICE", "alloy"))
    args = p.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if os.environ.get("ELEVENLABS_API_KEY") and os.environ.get("ELEVENLABS_VOICE_ID"):
        log(f"TTS via ElevenLabs → {out.name}")
        synth_elevenlabs(args.text, out, os.environ["ELEVENLABS_VOICE_ID"])
    elif os.environ.get("OPENAI_API_KEY"):
        log(f"TTS via OpenAI ({args.voice}) → {out.name}")
        synth_openai(args.text, out, args.voice)
    else:
        sys.stderr.write(
            "No TTS provider configured. Set OPENAI_API_KEY in .env, "
            "or ELEVENLABS_API_KEY + ELEVENLABS_VOICE_ID for ElevenLabs.\n"
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
