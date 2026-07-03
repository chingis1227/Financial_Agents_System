"""Shared normalization helpers for parser outputs."""

from __future__ import annotations

from typing import Any


def to_float(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if text in {"", "N/A", "NA", "--", "-"}:
        return None
    negative = text.startswith("(") and text.endswith(")")
    text = text.strip("()")
    if text.endswith("%"):
        text = text[:-1]
    try:
        number = float(text)
        return -number if negative else number
    except ValueError:
        return None


def normalize_metric_name(value: str) -> str:
    return "_".join(str(value).strip().lower().replace("/", " ").replace("-", " ").split())


def first_present(row: dict[str, Any], names: list[str]) -> Any:
    lower = {str(k).strip().lower(): v for k, v in row.items()}
    for name in names:
        key = name.strip().lower()
        if key in lower and lower[key] not in (None, ""):
            return lower[key]
    return None
