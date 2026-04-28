"""Shared utilities for DemoFlow automation scripts.

Conventions:
- Sessions live under <user_cwd>/.demoflow/<YYYYMMDD-HHMM>/.
- The user's CWD is the demo project, not the plugin dir.
- .env is read from the user's CWD.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


REQUIRED_PREP_KEYS = ("DEMOFLOW_APP_URL", "DEMOFLOW_USERNAME", "DEMOFLOW_PASSWORD")
REQUIRED_PRODUCE_KEYS_OPENAI = ("OPENAI_API_KEY",)
REQUIRED_PRODUCE_KEYS_ELEVENLABS = ("ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID")


def project_root() -> Path:
    return Path.cwd()


def demoflow_root() -> Path:
    return project_root() / ".demoflow"


def load_env() -> None:
    if load_dotenv is None:
        return
    env_path = project_root() / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def require_env(keys) -> dict[str, str]:
    load_env()
    missing = [k for k in keys if not os.environ.get(k)]
    if missing:
        sys.stderr.write(
            "Missing required env vars in .env: " + ", ".join(missing) + "\n"
        )
        sys.exit(2)
    return {k: os.environ[k] for k in keys}


def session_stamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M")


def new_session_dir() -> Path:
    root = demoflow_root()
    root.mkdir(exist_ok=True)
    sess = root / session_stamp()
    sess.mkdir(parents=True, exist_ok=True)
    (sess / "screenshots").mkdir(exist_ok=True)
    (sess / "voiceover").mkdir(exist_ok=True)
    return sess


def latest_session_dir() -> Path | None:
    root = demoflow_root()
    if not root.exists():
        return None
    candidates = sorted(
        (p for p in root.iterdir() if p.is_dir()),
        key=lambda p: p.name,
        reverse=True,
    )
    return candidates[0] if candidates else None


def resolve_session(arg: str | None) -> Path:
    if arg:
        p = Path(arg).resolve()
        if not p.exists():
            sys.stderr.write(f"Session dir does not exist: {p}\n")
            sys.exit(2)
        return p
    latest = latest_session_dir()
    if latest is None:
        sys.stderr.write(
            "No .demoflow/ session found. Run /demoflow:prep first.\n"
        )
        sys.exit(2)
    return latest


def read_plan(session: Path) -> dict:
    plan_path = session / "plan.json"
    if not plan_path.exists():
        sys.stderr.write(f"plan.json missing in {session}\n")
        sys.exit(2)
    return json.loads(plan_path.read_text())


def write_plan(session: Path, plan: dict) -> None:
    (session / "plan.json").write_text(json.dumps(plan, indent=2))


def log(msg: str) -> None:
    print(f"[demoflow] {msg}", flush=True)
