#!/usr/bin/env python3
"""Citation request and lock contracts shared by online and offline checks."""

from __future__ import annotations

import hashlib
import datetime as dt
import json
from pathlib import Path
from typing import Any

from paper_contract import ContractError, collect_citation_keys, load_json_object


REQUEST_SCHEMA = "ai-research-writing/citation-requests-v1"
LOCK_SCHEMA = "ai-research-writing/citation-lock-v1"
REQUEST_FIELDS = {"schema_version", "entries"}
ENTRY_FIELDS = {"key", "identifier", "claim_support"}
SUPPORT_FIELDS = {"claim", "relation", "status", "evidence", "source"}
RELATIONS = {"direct", "background", "contrast", "software", "partial", "weak", "metadata-only"}
SUPPORT_TERMINAL = {"verified", "software-doc"}
LOCK_TERMINAL = {"verified"}


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_requests(path: Path) -> list[dict[str, Any]]:
    root = load_json_object(path)
    unknown = sorted(set(root) - REQUEST_FIELDS)
    if unknown:
        raise ContractError("citation_requests.json contains unknown fields: " + ", ".join(unknown))
    if root.get("schema_version") != REQUEST_SCHEMA:
        raise ContractError(f"citation_requests.json schema_version must be {REQUEST_SCHEMA}")
    entries = root.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ContractError("citation_requests.json requires a non-empty entries list")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ContractError(f"citation_requests.json entries[{index}] must be an object")
        unknown_entry = sorted(set(entry) - ENTRY_FIELDS)
        if unknown_entry:
            raise ContractError(
                f"citation_requests.json entries[{index}] contains unknown fields: " + ", ".join(unknown_entry)
            )
        key = entry.get("key")
        identifier = entry.get("identifier")
        support = entry.get("claim_support")
        if not isinstance(key, str) or not key:
            raise ContractError(f"citation_requests.json entries[{index}].key must be a non-empty string")
        if key in seen:
            raise ContractError(f"citation_requests.json contains duplicate key: {key}")
        seen.add(key)
        if not isinstance(identifier, str) or not (
            identifier.lower().startswith("doi:") or identifier.lower().startswith("arxiv:")
        ):
            raise ContractError(
                f"citation_requests.json entries[{index}].identifier must begin with doi: or arxiv:"
            )
        if not isinstance(support, list) or not support:
            raise ContractError(f"citation_requests.json entries[{index}].claim_support must be non-empty")
        for support_index, item in enumerate(support):
            if not isinstance(item, dict):
                raise ContractError(
                    f"citation_requests.json entries[{index}].claim_support[{support_index}] must be an object"
                )
            unknown_support = sorted(set(item) - SUPPORT_FIELDS)
            if unknown_support:
                raise ContractError(
                    f"citation_requests.json entries[{index}].claim_support[{support_index}] contains unknown fields: "
                    + ", ".join(unknown_support)
                )
            for field in ("claim", "status", "evidence", "source"):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    raise ContractError(
                        f"citation_requests.json entries[{index}].claim_support[{support_index}].{field} "
                        "must be a non-empty string"
                    )
            if item.get("relation") not in RELATIONS:
                raise ContractError(
                    f"citation_requests.json entries[{index}].claim_support[{support_index}].relation is invalid"
                )
        normalized.append(entry)
    return normalized


def validate_lock(
    project: Path,
    tex: Path,
    requests_path: Path,
    lock_path: Path,
    *,
    max_age_days: int = 180,
) -> list[str]:
    del project
    if max_age_days <= 0:
        raise ContractError("Citation lock max_age_days must be positive")
    requests = load_requests(requests_path)
    requested = {entry["key"]: entry for entry in requests}
    lock = load_json_object(lock_path)
    if set(lock) != {"schema_version", "request_sha256", "records"}:
        raise ContractError("citation_lock.json must contain only schema_version, request_sha256, and records")
    if lock.get("schema_version") != LOCK_SCHEMA:
        raise ContractError(f"citation_lock.json schema_version must be {LOCK_SCHEMA}")
    if lock.get("request_sha256") != canonical_digest(requests):
        raise ContractError("citation_lock.json is stale for citation_requests.json")
    records = lock.get("records")
    if not isinstance(records, list):
        raise ContractError("citation_lock.json records must be a list")
    by_key: dict[str, dict[str, Any]] = {}
    failures: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ContractError(f"citation_lock.json records[{index}] must be an object")
        required = {
            "key", "identifier", "status", "provider", "request_url", "checked_at",
            "metadata", "metadata_sha256", "claim_support_sha256", "cross_check",
            "cross_check_sha256", "error",
        }
        if set(record) != required:
            raise ContractError(f"citation_lock.json records[{index}] has an invalid field set")
        key = record.get("key")
        if not isinstance(key, str) or key in by_key:
            raise ContractError(f"citation_lock.json records[{index}].key is empty or duplicated")
        by_key[key] = record
        request = requested.get(key)
        if request is None:
            failures.append(f"lock record has no request: {key}")
            continue
        if record.get("identifier") != request["identifier"]:
            failures.append(f"identifier changed for {key}")
        if record.get("metadata_sha256") != canonical_digest(record.get("metadata")):
            failures.append(f"metadata digest mismatch for {key}")
        if record.get("claim_support_sha256") != canonical_digest(request["claim_support"]):
            failures.append(f"claim-support digest mismatch for {key}")
        if record.get("cross_check_sha256") != canonical_digest(record.get("cross_check")):
            failures.append(f"cross-check digest mismatch for {key}")
        if record.get("status") not in LOCK_TERMINAL:
            failures.append(f"citation is not verified: {key} ({record.get('status')})")
        else:
            if not record.get("provider") or not record.get("request_url") or record.get("error"):
                failures.append(f"verified citation has incomplete provider provenance: {key}")
            checked_at = record.get("checked_at")
            if not isinstance(checked_at, str):
                failures.append(f"verified citation has no checked_at timestamp: {key}")
            else:
                try:
                    checked = dt.datetime.fromisoformat(checked_at)
                    if checked.tzinfo is None:
                        raise ValueError("timezone missing")
                    age = dt.datetime.now(dt.timezone.utc) - checked.astimezone(dt.timezone.utc)
                    if age < dt.timedelta(days=-1):
                        failures.append(f"citation lock timestamp is in the future: {key}")
                    elif age > dt.timedelta(days=max_age_days):
                        failures.append(f"citation lock is older than {max_age_days} days: {key}")
                except ValueError:
                    failures.append(f"citation lock has an invalid checked_at timestamp: {key}")
        for support in request["claim_support"]:
            if support["status"] not in SUPPORT_TERMINAL:
                failures.append(f"claim support is not terminal: {key} ({support['status']})")
    cited = collect_citation_keys(tex)
    missing_requests = sorted(cited - set(requested))
    missing_locks = sorted(cited - set(by_key))
    missing_requested_records = sorted(set(requested) - set(by_key))
    unexpected_records = sorted(set(by_key) - set(requested))
    if missing_requests:
        failures.append("cited keys missing from citation_requests.json: " + ", ".join(missing_requests))
    if missing_locks:
        failures.append("cited keys missing from citation_lock.json: " + ", ".join(missing_locks))
    if missing_requested_records:
        failures.append("requested keys missing from citation_lock.json: " + ", ".join(missing_requested_records))
    if unexpected_records:
        failures.append("citation_lock.json has unexpected keys: " + ", ".join(unexpected_records))
    return failures
