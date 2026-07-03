"""CSV parsing helpers."""

from __future__ import annotations

import csv
from io import StringIO
from typing import Any


def parse_csv_text(text: str) -> list[dict[str, Any]]:
    reader = csv.DictReader(StringIO(text))
    return [dict(row) for row in reader]
