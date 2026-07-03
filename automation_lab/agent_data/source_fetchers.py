"""Public source fetch helpers for TASK-013 AGENT preflight."""

from __future__ import annotations

import csv
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from io import StringIO
from typing import Any


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def http_json(url: str, timeout: int = 15) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Financial Agent Automation Lab TASK-013 contact: local@example.com",
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = response.read().decode("utf-8")
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("expected JSON object")
    return data


def http_text(url: str, timeout: int = 15) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Financial Agent Automation Lab TASK-013 contact: local@example.com"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def sec_submissions(cik: str) -> dict[str, Any]:
    cik10 = "".join(ch for ch in cik if ch.isdigit()).zfill(10)
    url = f"https://data.sec.gov/submissions/CIK{cik10}.json"
    data = http_json(url)
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    filing_dates = recent.get("filingDate", [])
    accession_numbers = recent.get("accessionNumber", [])
    primary_documents = recent.get("primaryDocument", [])
    records = []
    for index, form in enumerate(forms[:250]):
        if form not in {"10-K", "10-Q", "8-K", "20-F", "6-K", "40-F"}:
            continue
        accession = accession_numbers[index] if index < len(accession_numbers) else None
        primary_doc = primary_documents[index] if index < len(primary_documents) else None
        compact_accession = str(accession).replace("-", "") if accession else None
        document_url = None
        if compact_accession and primary_doc:
            document_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik10)}/{compact_accession}/{primary_doc}"
        records.append({
            "form": form,
            "filing_date": filing_dates[index] if index < len(filing_dates) else None,
            "accession_number": accession,
            "primary_document": primary_doc,
            "document_url": document_url,
        })
    return {"url": url, "records": records, "raw_name": data.get("name")}


def sec_company_facts(cik: str) -> dict[str, Any]:
    cik10 = "".join(ch for ch in cik if ch.isdigit()).zfill(10)
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json"
    data = http_json(url)
    facts = data.get("facts", {}).get("us-gaap", {})
    wanted = [
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "OperatingIncomeLoss",
        "NetIncomeLoss",
        "NetCashProvidedByUsedInOperatingActivities",
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "CashAndCashEquivalentsAtCarryingValue",
        "LongTermDebtCurrent",
        "LongTermDebtNoncurrent",
        "CommonStocksIncludingAdditionalPaidInCapital",
        "PaymentsOfDividends",
        "PaymentsForRepurchaseOfCommonStock",
    ]
    extracted: dict[str, Any] = {}
    for tag in wanted:
        if tag not in facts:
            continue
        units = facts[tag].get("units", {})
        usd = units.get("USD") or units.get("shares") or []
        extracted[tag] = usd[-8:] if isinstance(usd, list) else []
    return {"url": url, "entity_name": data.get("entityName"), "facts": extracted}


def yahoo_chart(ticker: str, range_value: str = "1y", interval: str = "1d") -> dict[str, Any]:
    query = urllib.parse.urlencode({"range": range_value, "interval": interval})
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker.upper()}?{query}"
    data = http_json(url)
    result = (data.get("chart", {}).get("result") or [None])[0]
    if not isinstance(result, dict):
        raise ValueError("missing Yahoo chart result")
    meta = result.get("meta") or {}
    timestamps = result.get("timestamp") or []
    quotes = result.get("indicators", {}).get("quote") or [{}]
    quote = quotes[0] if quotes else {}
    closes = quote.get("close") or []
    points = []
    latest = None
    for index, close in enumerate(closes):
        if close is None or index >= len(timestamps):
            continue
        date_text = datetime.fromtimestamp(timestamps[index], tz=timezone.utc).date().isoformat()
        point = {"date": date_text, "close": round(float(close), 4)}
        points.append(point)
        latest = point
    if latest is None and meta.get("regularMarketPrice") is not None:
        ts = meta.get("regularMarketTime")
        date_text = datetime.fromtimestamp(ts, tz=timezone.utc).date().isoformat() if isinstance(ts, int) else None
        latest = {"date": date_text, "close": round(float(meta["regularMarketPrice"]), 4)}
    if latest is None:
        raise ValueError("missing Yahoo close price")
    return {"url": url, "currency": meta.get("currency", "USD"), "latest": latest, "history": points[-260:]}


def stooq_symbol_candidates(ticker: str) -> list[str]:
    normalized = ticker.strip().lower().replace("/", ".")
    suffix_map = {
        ".as": ".nl",
        ".sw": ".ch",
        ".l": ".uk",
        ".pa": ".fr",
        ".de": ".de",
        ".mi": ".it",
        ".to": ".ca",
        ".t": ".jp",
        ".hk": ".hk",
    }
    candidates: list[str] = []
    if "." in normalized:
        root, suffix = normalized.rsplit(".", 1)
        mapped = suffix_map.get(f".{suffix}")
        if mapped:
            candidates.append(f"{root}{mapped}")
        candidates.append(normalized)
    else:
        candidates.append(f"{normalized}.us")
        candidates.append(normalized)
    dash_symbol = normalized.replace(".", "-")
    if dash_symbol not in candidates:
        candidates.append(f"{dash_symbol}.us" if "." not in normalized else dash_symbol)
    return list(dict.fromkeys(candidates))


def stooq_quote(ticker: str) -> dict[str, Any]:
    errors = []
    for symbol in stooq_symbol_candidates(ticker):
        url = f"https://stooq.com/q/l/?s={symbol}&f=sd2t2ohlcv&h&e=csv"
        try:
            text = http_text(url)
            reader = csv.DictReader(StringIO(text))
            row = next(reader, None)
            if not row or not row.get("Close") or row.get("Close") == "N/D":
                raise ValueError("missing Stooq close price")
            return {"url": url, "symbol": symbol, "latest": {"date": row.get("Date"), "close": row.get("Close")}, "currency": "USD"}
        except Exception as exc:
            errors.append(f"{symbol}: {exc}")
    raise ValueError("; ".join(errors) or "missing Stooq close price")


def stooq_history(ticker: str) -> dict[str, Any]:
    errors = []
    for symbol in stooq_symbol_candidates(ticker):
        url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
        try:
            text = http_text(url)
            reader = csv.DictReader(StringIO(text))
            points = []
            for row in reader:
                close = row.get("Close")
                date_text = row.get("Date")
                if not close or close == "N/D" or not date_text:
                    continue
                points.append({"date": date_text, "close": float(close)})
            if not points:
                raise ValueError("missing Stooq history")
            return {"url": url, "symbol": symbol, "latest": points[-1], "history": points[-260:]}
        except Exception as exc:
            errors.append(f"{symbol}: {exc}")
    raise ValueError("; ".join(errors) or "missing Stooq history")
