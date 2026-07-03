"""SEC submissions/companyfacts normalization."""

from __future__ import annotations

from typing import Any

SUPPORTED_FORMS = {"10-K", "10-Q", "8-K", "20-F", "6-K", "40-F"}


def primary_document_url(cik10: str, accession: str | None, primary_doc: str | None) -> str | None:
    if not accession or not primary_doc:
        return None
    compact = str(accession).replace("-", "")
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik10)}/{compact}/{primary_doc}"


def normalize_submissions(data: dict[str, Any], cik: str, *, limit: int = 250) -> list[dict[str, Any]]:
    cik10 = "".join(ch for ch in str(cik) if ch.isdigit()).zfill(10)
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    filing_dates = recent.get("filingDate", [])
    accession_numbers = recent.get("accessionNumber", [])
    primary_documents = recent.get("primaryDocument", [])
    records = []
    for index, form in enumerate(forms[:limit]):
        if form not in SUPPORTED_FORMS:
            continue
        accession = accession_numbers[index] if index < len(accession_numbers) else None
        primary_doc = primary_documents[index] if index < len(primary_documents) else None
        records.append(
            {
                "form": form,
                "filing_date": filing_dates[index] if index < len(filing_dates) else None,
                "accession_number": accession,
                "primary_document": primary_doc,
                "document_url": primary_document_url(cik10, accession, primary_doc),
                "cik": cik10,
            }
        )
    return records


def latest_by_form(records: list[dict[str, Any]], forms: list[str]) -> dict[str, Any] | None:
    for form in forms:
        for record in records:
            if record.get("form") == form:
                return record
    return None


def normalize_companyfacts(data: dict[str, Any], tags: list[str] | None = None) -> dict[str, Any]:
    wanted = tags or [
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "OperatingIncomeLoss",
        "NetIncomeLoss",
        "NetCashProvidedByUsedInOperatingActivities",
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "CashAndCashEquivalentsAtCarryingValue",
        "LongTermDebtCurrent",
        "LongTermDebtNoncurrent",
        "PaymentsOfDividends",
        "PaymentsForRepurchaseOfCommonStock",
    ]
    facts = data.get("facts", {}).get("us-gaap", {})
    normalized: dict[str, Any] = {"entity_name": data.get("entityName"), "facts": {}}
    for tag in wanted:
        if tag not in facts:
            continue
        units = facts[tag].get("units", {})
        for unit_name, rows in units.items():
            if isinstance(rows, list):
                normalized["facts"].setdefault(tag, {})[unit_name] = rows[-8:]
    return normalized
