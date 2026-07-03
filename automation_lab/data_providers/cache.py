"""Raw/normalized storage for reproducible provider runs."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def safe_slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())
    return value.strip("-._")[:80] or "subject"


def cache_key(provider_id: str, query: dict[str, Any], url: str | None = None) -> str:
    payload = json.dumps({"provider_id": provider_id, "query": query, "url": url}, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


class DataRunStorage:
    def __init__(
        self,
        root: str | Path | None = None,
        *,
        subject: str = "subject",
        timestamp: str | None = None,
        persist: bool = True,
    ):
        self.persist = persist
        default_root = Path(__file__).resolve().parents[1] / "data_runs"
        self.root = Path(root) if root else default_root
        self.timestamp = timestamp or datetime.now(timezone.utc).astimezone().strftime("%Y%m%d-%H%M%S%z")
        self.subject = safe_slug(subject)
        self.run_dir = self.root / f"{self.timestamp}-{self.subject}"
        self.raw_dir = self.run_dir / "raw"
        self.normalized_dir = self.run_dir / "normalized"
        if self.persist:
            self.raw_dir.mkdir(parents=True, exist_ok=True)
            self.normalized_dir.mkdir(parents=True, exist_ok=True)

    def save_raw_json(self, provider_id: str, query: dict[str, Any], data: Any, *, url: str | None = None) -> str | None:
        if not self.persist:
            return None
        path = self.raw_dir / f"{provider_id}-{cache_key(provider_id, query, url)}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        return str(path)

    def save_raw_text(
        self,
        provider_id: str,
        query: dict[str, Any],
        text: str,
        *,
        url: str | None = None,
        suffix: str = ".txt",
    ) -> str | None:
        if not self.persist:
            return None
        path = self.raw_dir / f"{provider_id}-{cache_key(provider_id, query, url)}{suffix}"
        path.write_text(text, encoding="utf-8")
        return str(path)

    def save_normalized(self, provider_id: str, query: dict[str, Any], data: Any, *, url: str | None = None) -> str | None:
        if not self.persist:
            return None
        path = self.normalized_dir / f"{provider_id}-{cache_key(provider_id, query, url)}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        return str(path)

    def write_run_artifacts(self, provider_results: list[dict[str, Any]]) -> dict[str, str | None]:
        if not self.persist:
            return {"run_dir": None, "provider_results": None, "source_inventory": None, "evidence_inputs": None}
        provider_path = self.run_dir / "provider_results.json"
        inventory_path = self.run_dir / "source_inventory.json"
        evidence_path = self.run_dir / "evidence_inputs.json"
        provider_path.write_text(json.dumps(provider_results, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        source_inventory = [
            {
                "provider_id": r.get("provider_id"),
                "provider_name": r.get("provider_name"),
                "source_tier": r.get("source_tier"),
                "source_type": r.get("source_type"),
                "url": r.get("url"),
                "status": r.get("status"),
                "access_status": r.get("access_status"),
                "source_date": r.get("source_date"),
                "retrieved_at": r.get("retrieved_at"),
                "raw_path": r.get("raw_path"),
                "normalized_path": r.get("normalized_path"),
            }
            for r in provider_results
        ]
        evidence_inputs = [claim for result in provider_results for claim in result.get("claims", [])]
        inventory_path.write_text(json.dumps(source_inventory, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        evidence_path.write_text(json.dumps(evidence_inputs, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        return {
            "run_dir": str(self.run_dir),
            "provider_results": str(provider_path),
            "source_inventory": str(inventory_path),
            "evidence_inputs": str(evidence_path),
        }
