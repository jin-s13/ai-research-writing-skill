#!/usr/bin/env python3
"""Record verified source and PDF hashes after a successful paper build."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shlex
import subprocess
import sys
from pathlib import Path

from paper_contract import ContractError, digest_file, digest_files, load_json_object, paper_input_files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--run", action="store_true", help="Execute build.command before recording hashes")
    parser.add_argument("--timeout", type=float, default=300.0)
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
        if args.run:
            command_value = build.get("command")
            if not isinstance(command_value, str) or not command_value.strip():
                raise ContractError("paper_state.json build.command must be a non-empty string.")
            try:
                command = shlex.split(command_value)
            except ValueError as exc:
                raise ContractError(f"Cannot parse build.command: {exc}") from exc
            if not command or any(token in {"|", "||", "&&", ";", "<", ">", ">>"} for token in command):
                raise ContractError("build.command must be one executable argv; shell operators are not allowed.")
            try:
                completed = subprocess.run(
                    command, cwd=main_tex.parent, text=True, capture_output=True,
                    check=False, timeout=args.timeout,
                )
            except FileNotFoundError as exc:
                raise ContractError(f"Build executable does not exist: {command[0]}") from exc
            except subprocess.TimeoutExpired as exc:
                raise ContractError(f"Build timed out after {args.timeout:g} seconds") from exc
            log_value = build.get("log", str(Path(main_value).parent / "build-attestation.log"))
            if not isinstance(log_value, str) or not log_value:
                raise ContractError("paper_state.json build.log must be a non-empty path when declared.")
            log_path = (root / log_value).resolve()
            try:
                log_path.relative_to(root)
            except ValueError as exc:
                raise ContractError("paper_state.json build.log escapes the project root.") from exc
            log_path.parent.mkdir(parents=True, exist_ok=True)
            log_path.write_text(
                f"$ {command_value}\n\n[stdout]\n{completed.stdout}\n[stderr]\n{completed.stderr}",
                encoding="utf-8",
            )
            build["log"] = str(log_path.relative_to(root))
            build["log_sha256"] = digest_file(log_path)
            build["exit_code"] = completed.returncode
            if completed.returncode != 0:
                build["status"] = "failed"
                state_path.write_text(json.dumps(state, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
                raise ContractError(f"Build command failed with exit code {completed.returncode}; see {build['log']}")
            try:
                version = subprocess.run(
                    [command[0], "--version"], cwd=main_tex.parent, text=True,
                    capture_output=True, check=False, timeout=min(args.timeout, 20.0),
                )
            except subprocess.TimeoutExpired as exc:
                raise ContractError(f"Build tool version probe timed out: {command[0]}") from exc
            version_text = version.stdout or version.stderr
            build["tool_version"] = version_text.strip().splitlines()[0][:300] if version_text.strip() else "unreported"
            build["attestation"] = "executed"
            build["ran_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
        else:
            build["attestation"] = "artifact-only"
            build["exit_code"] = None
            build["log"] = build.get("log", "")
            build["log_sha256"] = build.get("log_sha256", "")
            build["tool_version"] = build.get("tool_version", "unreported")
            build["ran_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
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
        if build.get("attestation") == "executed":
            external_records.append(
                json.dumps(
                    {"command": build.get("command"), "tool_version": build.get("tool_version")},
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
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
