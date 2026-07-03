from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any

from .config import RuntimeSettings


class OpenAIAdapter:
    """Minimal OpenAI Responses API adapter.

    The adapter is only constructed in live mode after the caller has verified
    `OPENAI_API_KEY`. Dry-run code paths never instantiate it and never make API calls.
    """

    def __init__(self, settings: RuntimeSettings, *, max_retries: int = 2, timeout_seconds: int = 60) -> None:
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is required for live OpenAI calls.")
        self.settings = settings
        self.max_retries = max_retries
        self.timeout_seconds = timeout_seconds

    def responses_text(self, *, system: str, user: str) -> str:
        payload: dict[str, Any] = {
            "model": self.settings.openai_model,
            "reasoning": {"effort": self.settings.openai_reasoning_effort},
            "input": [
                {"role": "system", "content": [{"type": "input_text", "text": system}]},
                {"role": "user", "content": [{"type": "input_text", "text": user}]},
            ],
        }
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            "https://api.openai.com/v1/responses",
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.settings.openai_api_key}",
                "Content-Type": "application/json",
            },
        )
        last_error: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                    body = json.loads(response.read().decode("utf-8"))
                return self._extract_text(body)
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
                last_error = exc
                if attempt >= self.max_retries:
                    break
                time.sleep(0.5 * (2 ** attempt))
        raise RuntimeError(f"OpenAI API call failed after retries: {last_error}")

    @staticmethod
    def _extract_text(body: dict[str, Any]) -> str:
        if isinstance(body.get("output_text"), str):
            return body["output_text"]
        chunks: list[str] = []
        for item in body.get("output", []) or []:
            for content in item.get("content", []) or []:
                text = content.get("text")
                if isinstance(text, str):
                    chunks.append(text)
        if chunks:
            return "\n".join(chunks)
        return json.dumps(body, ensure_ascii=False)
