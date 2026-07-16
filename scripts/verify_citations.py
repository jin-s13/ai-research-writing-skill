#!/usr/bin/env python3
"""Resolve DOI/arXiv metadata and write a fail-closed citation lock."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from citation_lock import LOCK_SCHEMA, SUPPORT_TERMINAL, canonical_digest, load_requests
from paper_contract import ContractError


USER_AGENT = "ai-research-writing-skill/1.0"


class ProviderFailure(RuntimeError):
    def __init__(self, status: str, message: str) -> None:
        super().__init__(message)
        self.status = status


def fetch(url: str, *, mailto: str | None, timeout: float) -> bytes:
    headers = {"User-Agent": USER_AGENT + (f" (mailto:{mailto})" if mailto else "")}
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise ProviderFailure("not-found", f"HTTP 404 from {url}") from exc
        if exc.code == 429:
            raise ProviderFailure("rate-limited", f"HTTP 429 from {url}") from exc
        raise ProviderFailure("provider-error", f"HTTP {exc.code} from {url}") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise ProviderFailure("network-error", f"Cannot retrieve {url}: {exc}") from exc


def _year_from_crossref(message: dict[str, Any]) -> int | None:
    for field in ("published-print", "published-online", "issued", "created"):
        parts = message.get(field, {}).get("date-parts") if isinstance(message.get(field), dict) else None
        if isinstance(parts, list) and parts and isinstance(parts[0], list) and parts[0]:
            value = parts[0][0]
            if isinstance(value, int):
                return value
    return None


def crossref(doi: str, mailto: str | None, timeout: float) -> tuple[dict[str, Any], str]:
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded}"
    if mailto:
        url += "?" + urllib.parse.urlencode({"mailto": mailto})
    payload = json.loads(fetch(url, mailto=mailto, timeout=timeout))
    message = payload.get("message")
    if not isinstance(message, dict):
        raise ProviderFailure("provider-error", "Crossref response has no message object")
    metadata = {
        "title": " ".join(message.get("title", [])).strip(),
        "authors": [
            " ".join(part for part in (item.get("given", ""), item.get("family", "")) if part).strip()
            for item in message.get("author", []) if isinstance(item, dict)
        ],
        "year": _year_from_crossref(message),
        "doi": str(message.get("DOI", doi)).lower(),
        "type": message.get("type"),
    }
    return metadata, url


def datacite(doi: str, mailto: str | None, timeout: float) -> tuple[dict[str, Any], str]:
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.datacite.org/dois/{encoded}"
    payload = json.loads(fetch(url, mailto=mailto, timeout=timeout))
    attributes = payload.get("data", {}).get("attributes")
    if not isinstance(attributes, dict):
        raise ProviderFailure("provider-error", "DataCite response has no attributes object")
    titles = attributes.get("titles", [])
    metadata = {
        "title": " ".join(item.get("title", "") for item in titles if isinstance(item, dict)).strip(),
        "authors": [item.get("name", "") for item in attributes.get("creators", []) if isinstance(item, dict)],
        "year": attributes.get("publicationYear"),
        "doi": str(attributes.get("doi", doi)).lower(),
        "type": attributes.get("types", {}).get("resourceTypeGeneral")
        if isinstance(attributes.get("types"), dict) else None,
    }
    return metadata, url


def arxiv(arxiv_id: str, mailto: str | None, timeout: float) -> tuple[dict[str, Any], str]:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": arxiv_id})
    root = ET.fromstring(fetch(url, mailto=mailto, timeout=timeout))
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entry = root.find("atom:entry", ns)
    if entry is None:
        raise ProviderFailure("not-found", f"arXiv returned no entry for {arxiv_id}")
    published = entry.findtext("atom:published", default="", namespaces=ns)
    title = " ".join(entry.findtext("atom:title", default="", namespaces=ns).split())
    authors = [
        node.findtext("atom:name", default="", namespaces=ns)
        for node in entry.findall("atom:author", ns)
    ]
    return {
        "title": title,
        "authors": authors,
        "year": int(published[:4]) if published[:4].isdigit() else None,
        "arxiv_id": arxiv_id,
        "type": "preprint",
    }, url


def openalex(identifier: str, api_key: str, mailto: str | None, timeout: float) -> tuple[dict[str, Any], str]:
    if identifier.lower().startswith("doi:"):
        external = "https://doi.org/" + identifier.split(":", 1)[1]
    else:
        external = "https://arxiv.org/abs/" + identifier.split(":", 1)[1]
    url = "https://api.openalex.org/works/" + urllib.parse.quote(external, safe="")
    url += "?" + urllib.parse.urlencode({"api_key": api_key, **({"mailto": mailto} if mailto else {})})
    payload = json.loads(fetch(url, mailto=mailto, timeout=timeout))
    authorships = payload.get("authorships", [])
    return {
        "title": payload.get("title", ""),
        "authors": [
            item.get("author", {}).get("display_name", "")
            for item in authorships if isinstance(item, dict) and isinstance(item.get("author"), dict)
        ],
        "year": payload.get("publication_year"),
        "doi": str(payload.get("doi", "")).removeprefix("https://doi.org/").lower() or None,
        "type": payload.get("type"),
    }, url


def comparable(metadata: dict[str, Any]) -> tuple[str, object, object]:
    title = "".join(char for char in str(metadata.get("title", "")).casefold() if char.isalnum())
    return title, metadata.get("year"), metadata.get("doi")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--mailto")
    parser.add_argument("--openalex-api-key", default=os.environ.get("OPENALEX_API_KEY"))
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()
    root = args.project_path.resolve()
    try:
        requests = load_requests(root / "citation_requests.json")
    except ContractError as exc:
        print(f"Citation verification failed: {exc}", file=sys.stderr)
        return 2

    records: list[dict[str, Any]] = []
    for entry in requests:
        key = entry["key"]
        identifier = entry["identifier"]
        provider = ""
        request_url = ""
        metadata: dict[str, Any] = {}
        cross_check: dict[str, Any] | None = None
        error = ""
        status = "verified"
        try:
            if identifier.lower().startswith("doi:"):
                doi = identifier.split(":", 1)[1]
                try:
                    metadata, request_url = crossref(doi, args.mailto, args.timeout)
                    provider = "crossref"
                except ProviderFailure as exc:
                    if exc.status != "not-found":
                        raise
                    metadata, request_url = datacite(doi, args.mailto, args.timeout)
                    provider = "datacite"
            else:
                metadata, request_url = arxiv(identifier.split(":", 1)[1], args.mailto, args.timeout)
                provider = "arxiv"
            if not metadata.get("title") or not metadata.get("year") or not metadata.get("authors"):
                raise ProviderFailure("incomplete-metadata", "Primary provider returned incomplete title/author/year metadata")
            if args.openalex_api_key:
                oa_metadata, oa_url = openalex(identifier, args.openalex_api_key, args.mailto, args.timeout)
                cross_check = {"provider": "openalex", "request_url": oa_url, "metadata": oa_metadata}
                primary_title, primary_year, primary_doi = comparable(metadata)
                oa_title, oa_year, oa_doi = comparable(oa_metadata)
                if primary_title != oa_title or primary_year != oa_year or (primary_doi and oa_doi and primary_doi != oa_doi):
                    status = "conflict"
                    error = "OpenAlex metadata conflicts with the primary provider"
            if any(item["status"] not in SUPPORT_TERMINAL for item in entry["claim_support"]):
                status = "metadata-only"
                error = "One or more sentence-level claim-support records are non-terminal"
        except ProviderFailure as exc:
            status = exc.status
            error = str(exc)
        except (json.JSONDecodeError, ET.ParseError, KeyError, TypeError, ValueError) as exc:
            status = "provider-error"
            error = f"Cannot parse provider response: {exc}"
        records.append({
            "key": key,
            "identifier": identifier,
            "status": status,
            "provider": provider,
            "request_url": request_url,
            "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "metadata": metadata,
            "metadata_sha256": canonical_digest(metadata),
            "claim_support_sha256": canonical_digest(entry["claim_support"]),
            "cross_check": cross_check,
            "cross_check_sha256": canonical_digest(cross_check),
            "error": error,
        })

    lock = {"schema_version": LOCK_SCHEMA, "request_sha256": canonical_digest(requests), "records": records}
    (root / "citation_lock.json").write_text(json.dumps(lock, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    failures = [record for record in records if record["status"] != "verified"]
    for record in records:
        print(f"{str(record['status']).upper()}: {record['key']} via {record['provider'] or 'unresolved'}")
        if record["error"]:
            print(f"  {record['error']}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
