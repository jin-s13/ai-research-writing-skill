#!/usr/bin/env python3
"""Fetch a pinned official venue template without vendoring it in this repo."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "templates/manifest.json"


def safe_members(archive: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    members: list[zipfile.ZipInfo] = []
    for info in archive.infolist():
        path = PurePosixPath(info.filename)
        if path.is_absolute() or ".." in path.parts:
            raise RuntimeError(f"Unsafe archive path: {info.filename}")
        if (info.external_attr >> 16) & 0o170000 == 0o120000:
            raise RuntimeError(f"Archive contains a symbolic link: {info.filename}")
        if "__MACOSX" in path.parts:
            continue
        members.append(info)
    return members


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", nargs="?", help="Template id from templates/manifest.json")
    parser.add_argument("--output", type=Path, help="New directory to create")
    parser.add_argument("--list", action="store_true", help="List audited template ids")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    templates = manifest["templates"]
    if args.list:
        for key, item in templates.items():
            print(f"{key}: {item['venue']} [{item['license_status']}]")
        return 0
    if not args.template or args.template not in templates:
        parser.error("provide a template id from --list")
    if args.output is None:
        parser.error("--output is required")
    if args.output.exists():
        print(f"Output path already exists; refusing to merge or overwrite: {args.output}", file=sys.stderr)
        return 2

    item = templates[args.template]
    url = item.get("archive_url")
    expected = item.get("archive_sha256")
    if not isinstance(url, str) or not isinstance(expected, str):
        print(
            f"No pinned archive is configured for {args.template}. Download it manually from {item['official_page']}",
            file=sys.stderr,
        )
        return 2

    request = urllib.request.Request(url, headers={"User-Agent": "ai-research-writing-skill/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = response.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"Template download failed: {url}: {exc}", file=sys.stderr)
        return 2
    actual = hashlib.sha256(payload).hexdigest()
    if actual != expected:
        print(
            f"Template archive hash mismatch for {args.template}: expected {expected}, received {actual}. "
            "The upstream package changed; audit it before updating templates/manifest.json.",
            file=sys.stderr,
        )
        return 2

    with tempfile.TemporaryDirectory() as directory:
        temp = Path(directory)
        archive_path = temp / "template.zip"
        archive_path.write_bytes(payload)
        extracted = temp / "extracted"
        extracted.mkdir()
        try:
            with zipfile.ZipFile(archive_path) as archive:
                archive.extractall(extracted, members=safe_members(archive))
        except (zipfile.BadZipFile, RuntimeError) as exc:
            print(f"Template archive validation failed: {exc}", file=sys.stderr)
            return 2
        prefix = item.get("strip_prefix")
        source = extracted / prefix if prefix else extracted
        if not source.is_dir():
            print(f"Configured archive prefix does not exist: {prefix}", file=sys.stderr)
            return 2
        shutil.copytree(source, args.output)

    print(f"Fetched {item['venue']} into {args.output}")
    print(f"Source: {url}")
    print(f"SHA-256: {actual}")
    print(f"License audit status: {item['license_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
