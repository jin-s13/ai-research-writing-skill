#!/usr/bin/env python3
"""Record verified source and PDF hashes after a successful paper build."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from paper_contract import ContractError, digest_file, digest_files, load_json_object, paper_input_files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    args = parser.parse_args()
    root = args.project_path.resolve()
    state_path = root / "paper_state.json"
    try:
        state = load_json_object(state_path)
        main_value = state["main_tex"]
        bib_value = state["bibliography"]
        build = state["build"]
        if not isinstance(main_value, str) or not isinstance(bib_value, str) or not isinstance(build, dict):
            raise ContractError("paper_state.json has invalid main_tex, bibliography, or build fields.")
        pdf_value = build.get("pdf")
        if not isinstance(pdf_value, str) or not pdf_value:
            raise ContractError("paper_state.json build.pdf must be a non-empty path.")
        main_tex = root / main_value
        bibliography = root / bib_value
        pdf = root / pdf_value
        inputs = paper_input_files(root, main_tex, bibliography)
        try:
            pdf_mtime = pdf.stat().st_mtime_ns
        except FileNotFoundError as exc:
            raise ContractError(f"Required file does not exist: {pdf}") from exc
        newer_inputs = [path for path in inputs if path.stat().st_mtime_ns > pdf_mtime]
        if newer_inputs:
            listed = ", ".join(str(path.relative_to(root)) for path in newer_inputs)
            raise ContractError(
                "PDF is older than one or more build inputs; run the declared build command before recording: "
                + listed
            )
        external_inputs = build.get("external_inputs", [])
        if not isinstance(external_inputs, list) or any(not isinstance(item, dict) for item in external_inputs):
            raise ContractError("paper_state.json build.external_inputs must be a list of objects.")
        external_records = [json.dumps(item, sort_keys=True, separators=(",", ":")) for item in external_inputs]
        build["status"] = "passed"
        build["input_sha256"] = digest_files(root, inputs, external_records)
        build["pdf_sha256"] = digest_file(pdf)
    except (ContractError, KeyError) as exc:
        print(f"Cannot record build: {exc}", file=sys.stderr)
        return 2

    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Recorded build hashes in {state_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
