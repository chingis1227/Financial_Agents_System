"""Small HTTP helpers shared by providers."""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from typing import Any

USER_AGENT = "Financial Agent Data Provider Layer contact: local@example.com"


def http_text(url: str, *, timeout: int = 15, headers: dict[str, str] | None = None) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def http_json(url: str, *, timeout: int = 15, headers: dict[str, str] | None = None) -> dict[str, Any]:
    text = http_text(url, timeout=timeout, headers={"Accept": "application/json,text/plain,*/*", **(headers or {})})
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("expected JSON object")
    return data


def urlencode(params: dict[str, Any]) -> str:
    return urllib.parse.urlencode({key: value for key, value in params.items() if value not in (None, "")})
