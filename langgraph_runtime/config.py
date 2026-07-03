from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

DEFAULT_MODEL = "gpt-5.3-codex"
DEFAULT_REASONING_EFFORT = "low"

@dataclass(frozen=True)
class RuntimeSettings:
    openai_api_key: str
    openai_model: str = DEFAULT_MODEL
    openai_reasoning_effort: str = DEFAULT_REASONING_EFFORT


def load_dotenv(path: str | Path = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def get_settings(*, require_api_key: bool = False) -> RuntimeSettings:
    load_dotenv()
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if require_api_key and not key:
        raise RuntimeError("OPENAI_API_KEY is required for live production mode.")
    return RuntimeSettings(
        openai_api_key=key,
        openai_model=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL,
        openai_reasoning_effort=os.environ.get("OPENAI_REASONING_EFFORT", DEFAULT_REASONING_EFFORT).strip() or DEFAULT_REASONING_EFFORT,
    )
