"""USDA WASDE lightweight text parser.

It extracts stable grain balance-sheet rows when text is table-like. If a
report is unparseable, providers must return Partial with explicit limitations.
"""

from __future__ import annotations

import re
from typing import Any

from .normalization import to_float

METRICS = {
    "production": re.compile(r"production", re.I),
    "domestic_use": re.compile(r"domestic\s+use|total\s+domestic", re.I),
    "exports": re.compile(r"exports?", re.I),
    "ending_stocks": re.compile(r"ending\s+stocks", re.I),
    "stocks_use": re.compile(r"stocks.?use", re.I),
}
COMMODITIES = ["corn", "wheat", "soybeans", "soybean", "rice"]


def parse_wasde_text(text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in text.splitlines():
        clean = " ".join(line.split())
        if not clean:
            continue
        commodity = next((item for item in COMMODITIES if re.search(rf"\b{re.escape(item)}\b", clean, re.I)), None)
        metric = next((name for name, pattern in METRICS.items() if pattern.search(clean)), None)
        if not commodity or not metric:
            continue
        numbers = re.findall(r"[+-]?\d[\d,]*(?:\.\d+)?%?", clean)
        if not numbers:
            continue
        value = to_float(numbers[-1])
        if value is None:
            continue
        rows.append(
            {
                "commodity": "soybeans" if commodity == "soybean" else commodity.lower(),
                "metric": metric,
                "period": None,
                "geography": "US/World as reported",
                "unit": "%" if numbers[-1].endswith("%") else "report unit",
                "value": value,
                "raw_line": clean,
            }
        )
    return rows
