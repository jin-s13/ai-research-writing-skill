#!/usr/bin/env python3
"""Validate an upstream research-system handoff before paper writing starts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from check_numeric_evidence import load_registry
from paper_contract import ContractError, load_json_object, read_utf8


SCHEMA_VERSION = "ai-research-writing/research-handoff-v1"
ROOT_FIELDS = {
    "schema_version",
    "research_question",
    "paper_type",
    "target_venue",
    "quantitative",
    "artifacts",
    "blockers",
}
ARTIFACT_FIELDS = {
    "project_inventory",
    "analysis",
    "decision",
    "experiment_inventory",
    "numeric_evidence",
    "literature_inventory",
    "figure_inventory",
}
BASE_ARTIFACTS = {"project_inventory", "analysis", "decision"}


def _artifact_path(root: Path, name: str, raw: object) -> Path:
    if not isinstance(raw, str) or not raw:
        raise ContractError(f"research_handoff.json artifacts.{name} must be a non-empty path")
    path = (root / raw).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ContractError(f"research_handoff.json artifacts.{name} escapes project root: {raw}") from exc
    if not path.is_file():
        raise ContractError(f"research_handoff.json artifacts.{name} does not exist: {raw}")
    if path.stat().st_size == 0:
        raise ContractError(f"research_handoff.json artifacts.{name} is empty: {raw}")
    return path


def validate_handoff(root: Path, handoff_path: Path) -> list[str]:
    handoff = load_json_object(handoff_path)
    unknown = sorted(set(handoff) - ROOT_FIELDS)
    if unknown:
        raise ContractError("research_handoff.json contains unknown fields: " + ", ".join(unknown))
    if handoff.get("schema_version") != SCHEMA_VERSION:
        raise ContractError(f"research_handoff.json schema_version must be {SCHEMA_VERSION}")
    for field in ("research_question", "paper_type", "target_venue"):
        if not isinstance(handoff.get(field), str) or not str(handoff[field]).strip():
            raise ContractError(f"research_handoff.json requires a non-empty string field: {field}")
    quantitative = handoff.get("quantitative")
    if not isinstance(quantitative, bool):
        raise ContractError("research_handoff.json quantitative must be a boolean")
    blockers = handoff.get("blockers")
    if not isinstance(blockers, list) or any(not isinstance(item, str) or not item for item in blockers):
        raise ContractError("research_handoff.json blockers must be a list of non-empty strings")
    artifacts = handoff.get("artifacts")
    if not isinstance(artifacts, dict):
        raise ContractError("research_handoff.json artifacts must be an object")
    unknown_artifacts = sorted(set(artifacts) - ARTIFACT_FIELDS)
    if unknown_artifacts:
        raise ContractError(
            "research_handoff.json artifacts contains unknown fields: " + ", ".join(unknown_artifacts)
        )
    required = set(BASE_ARTIFACTS)
    if quantitative:
        required.update({"experiment_inventory", "numeric_evidence"})
    missing = sorted(required - set(artifacts))
    if missing:
        raise ContractError("research_handoff.json is missing required artifacts: " + ", ".join(missing))

    paths = {name: _artifact_path(root, name, raw) for name, raw in artifacts.items()}
    for name, path in paths.items():
        if path.suffix.lower() in {".md", ".txt", ".json", ".csv", ".tsv", ".yaml", ".yml"}:
            read_utf8(path)
    if "numeric_evidence" in paths:
        load_registry(root, paths["numeric_evidence"])
    return list(blockers)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--handoff", default="research_handoff.json", help="Handoff path relative to project")
    parser.add_argument(
        "--require-unblocked", action="store_true",
        help="Fail when the handoff declares blockers instead of only reporting them",
    )
    args = parser.parse_args()
    root = args.project_path.resolve()
    if not root.is_dir():
        print(f"Project directory does not exist: {root}", file=sys.stderr)
        return 2
    try:
        blockers = validate_handoff(root, root / args.handoff)
    except ContractError as exc:
        print(f"Research handoff check failed: {exc}", file=sys.stderr)
        return 2
    if blockers:
        print("Research handoff is structurally valid with declared blockers:")
        for blocker in blockers:
            print(f"  - {blocker}")
        if args.require_unblocked:
            return 1
    else:
        print("Research handoff check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
