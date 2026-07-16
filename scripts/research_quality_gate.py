#!/usr/bin/env python3
"""Run strict, mode-aware quality checks for a paper project or this skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from paper_contract import (
    ContractError,
    collect_bib_keys,
    collect_citation_keys,
    collect_tex_files,
    collect_tex_text,
    digest_file,
    digest_files,
    load_json_object,
    paper_input_files,
    read_utf8,
    resolve_graphics,
)
from check_numeric_evidence import verify_project as verify_numeric_evidence
from citation_lock import validate_lock


SCHEMA_VERSION = "ai-research-writing/paper-state-v1"
VALID_MODES = {"draft", "full-paper", "submission", "skill"}
STATE_FIELDS = {"schema_version", "mode", "stage", "target_venue", "main_tex", "bibliography", "required_artifacts", "blockers", "build"}
BUILD_FIELDS = {
    "status", "command", "pdf", "external_inputs", "input_sha256", "pdf_sha256",
    "attestation", "exit_code", "log", "log_sha256", "tool_version", "ran_at",
}
EXTERNAL_INPUT_FIELDS = {"name", "source", "archive_sha256"}
TERMINAL_STAGES = {"complete", "submission-ready"}
UNRESOLVED_RE = re.compile(
    r"\b(TODO|TBD|FIXME|XXX|PLACEHOLDER|CITATION\s+NEEDED|FILL\s+LATER)\b|"
    r"待回填|待替换|待补充|公式占位|算法占位",
    re.IGNORECASE,
)
PROCESS_RE = re.compile(
    r"write naturally|avoid ai|replace later|user should|this section is a template|"
    r"discussion prompt|figure position|table position|"
    r"写作要求|修改要求|请用户|用户替换|回填模板|讨论提示|图位|表位|实验目的",
    re.IGNORECASE,
)
STALE_PROGRESS_RE = re.compile(
    r"verification\s+(?:planned|pending)|to be recorded|not yet run|待验证|待运行|尚未验证",
    re.IGNORECASE,
)
OPEN_STATUS_RE = re.compile(r"needs evidence|pending|unknown|unverified|placeholder|待核验|待补充", re.IGNORECASE)
LOCAL_MD_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


@dataclass(frozen=True)
class Issue:
    level: str
    message: str


def add(issues: list[Issue], level: str, message: str) -> None:
    issues.append(Issue(level, message))


def require_nonempty(root: Path, relative: str, issues: list[Issue]) -> Path:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        add(issues, "failure", f"Required artifact escapes project root: {relative}")
        return path
    if not path.is_file():
        add(issues, "failure", f"Required artifact is missing: {relative}")
    elif path.stat().st_size == 0:
        add(issues, "failure", f"Required artifact is empty: {relative}")
    return path


def markdown_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    lines = read_utf8(path).splitlines()
    for index, line in enumerate(lines):
        if not line.strip().startswith("|") or index + 1 >= len(lines):
            continue
        separator = lines[index + 1]
        if not re.match(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$", separator):
            continue
        headers = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
        rows: list[list[str]] = []
        for candidate in lines[index + 2 :]:
            if not candidate.strip().startswith("|"):
                break
            cells = [cell.strip() for cell in candidate.strip().strip("|").split("|")]
            if len(cells) == len(headers):
                rows.append(cells)
        return headers, rows
    raise ContractError(f"No Markdown table found in required artifact: {path}")


def validate_skill(root: Path, issues: list[Issue]) -> None:
    skill_path = require_nonempty(root, "SKILL.md", issues)
    if not skill_path.is_file():
        return
    text = read_utf8(skill_path)
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        add(issues, "failure", "SKILL.md must start with YAML frontmatter.")
    else:
        keys = []
        for line in match.group(1).splitlines():
            if line and not line.startswith((" ", "\t")) and ":" in line:
                keys.append(line.split(":", 1)[0].strip())
        if keys != ["name", "description"]:
            add(issues, "failure", f"SKILL.md frontmatter must contain only name and description; found: {keys}")

    for raw in re.findall(r"`((?:references|scripts)/[^`]+)`", text):
        if any(char in raw for char in "*<>"):
            continue
        if not (root / raw).exists():
            add(issues, "failure", f"SKILL.md references a missing local resource: {raw}")

    for markdown in [root / "README.md", root / "README.zh-CN.md", root / "references/README.md"]:
        if not markdown.is_file():
            continue
        for raw in LOCAL_MD_LINK_RE.findall(read_utf8(markdown)):
            target = raw.split("#", 1)[0].strip()
            if not target:
                continue
            if not (markdown.parent / target).resolve().exists():
                add(issues, "failure", f"Broken local Markdown link in {markdown.relative_to(root)}: {raw}")

    for script in sorted((root / "scripts").glob("*.py")):
        try:
            compile(read_utf8(script), str(script), "exec")
        except SyntaxError as exc:
            add(issues, "failure", f"Python syntax error in {script.relative_to(root)}:{exc.lineno}: {exc.msg}")

    manifest_path = root / "templates/manifest.json"
    if not manifest_path.is_file():
        add(issues, "failure", "templates/manifest.json is required.")
    else:
        manifest = load_json_object(manifest_path)
        templates = manifest.get("templates")
        if not isinstance(templates, dict) or not templates:
            add(issues, "failure", "templates/manifest.json requires a non-empty templates object.")
        else:
            for key, item in templates.items():
                if not isinstance(item, dict):
                    add(issues, "failure", f"Template manifest entry {key} must be an object.")
                    continue
                for field in ("venue", "official_page", "license_status", "notes"):
                    if not isinstance(item.get(field), str) or not item[field]:
                        add(issues, "failure", f"Template manifest entry {key} requires {field}.")
                archive_url = item.get("archive_url")
                archive_sha = item.get("archive_sha256")
                if (archive_url is None) != (archive_sha is None):
                    add(issues, "failure", f"Template manifest entry {key} must declare archive_url and archive_sha256 together.")
                if archive_sha is not None and (not isinstance(archive_sha, str) or re.fullmatch(r"[0-9a-f]{64}", archive_sha) is None):
                    add(issues, "failure", f"Template manifest entry {key} has an invalid archive_sha256.")
    vendored = sorted(path.name for path in (root / "templates").iterdir() if path.is_dir())
    if vendored:
        add(issues, "failure", "Vendored template directories are not allowed; use the audited fetcher: " + ", ".join(vendored))


def state_string(state: dict[str, object], key: str, issues: list[Issue]) -> str | None:
    value = state.get(key)
    if not isinstance(value, str) or not value.strip():
        add(issues, "failure", f"paper_state.json requires a non-empty string field: {key}")
        return None
    return value


def external_build_records(build: dict[str, object], issues: list[Issue]) -> list[str]:
    value = build.get("external_inputs", [])
    if not isinstance(value, list):
        add(issues, "failure", "build.external_inputs must be a list.")
        return []
    records: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            add(issues, "failure", f"build.external_inputs[{index}] must be an object.")
            continue
        unknown = sorted(set(item) - EXTERNAL_INPUT_FIELDS)
        if unknown:
            add(
                issues,
                "failure",
                f"build.external_inputs[{index}] contains unknown fields: " + ", ".join(unknown),
            )
        name = item.get("name")
        source = item.get("source")
        sha256 = item.get("archive_sha256")
        if not isinstance(name, str) or not name or not isinstance(source, str) or not source:
            add(issues, "failure", f"build.external_inputs[{index}] requires non-empty name and source fields.")
            continue
        if not isinstance(sha256, str) or re.fullmatch(r"[0-9a-f]{64}", sha256) is None:
            add(issues, "failure", f"build.external_inputs[{index}].archive_sha256 must be 64 lowercase hex characters.")
            continue
        records.append(json.dumps(item, sort_keys=True, separators=(",", ":")))
    return records


def validate_verification_table(path: Path, cited: set[str], issues: list[Issue]) -> set[str]:
    try:
        headers, rows = markdown_rows(path)
    except ContractError as exc:
        add(issues, "failure", str(exc))
        return set()
    if "key" not in headers or "status" not in headers:
        add(issues, "failure", "citation_verification.md table requires Key and Status columns.")
        return set()
    key_index = headers.index("key")
    status_index = headers.index("status")
    verified: set[str] = set()
    scholarly: set[str] = set()
    open_keys: list[str] = []
    for row in rows:
        key = row[key_index].strip().strip("`")
        status = row[status_index].strip().lower()
        if status in {"verified", "software-doc", "repository-verified"}:
            verified.add(key)
            if status == "verified":
                scholarly.add(key)
        elif key:
            open_keys.append(f"{key} ({status or 'empty status'})")
    missing = sorted(cited - verified)
    if missing:
        add(issues, "failure", "Cited keys lack a verified citation record: " + ", ".join(missing))
    if open_keys:
        add(issues, "failure", "Citation verification has unresolved records: " + ", ".join(open_keys))
    return scholarly


def validate_claim_map(path: Path, terminal: bool, issues: list[Issue]) -> None:
    if not terminal:
        return
    try:
        headers, rows = markdown_rows(path)
    except ContractError as exc:
        add(issues, "failure", str(exc))
        return
    if "status" not in headers:
        add(issues, "failure", "claim_evidence_map.md table requires a Status column.")
        return
    status_index = headers.index("status")
    unresolved = [row[status_index] for row in rows if OPEN_STATUS_RE.search(row[status_index])]
    if unresolved:
        add(issues, "failure", "Claim/evidence map has unresolved statuses: " + ", ".join(unresolved))


def validate_manuscript(main_tex: Path, issues: list[Issue]) -> None:
    try:
        text = collect_tex_text(main_tex)
        resolve_graphics(main_tex)
    except ContractError as exc:
        add(issues, "failure", str(exc))
        return
    for lineno, line in enumerate(text.splitlines(), start=1):
        if UNRESOLVED_RE.search(line):
            add(issues, "failure", f"Manuscript contains unresolved marker near collected line {lineno}: {line.strip()[:140]}")
        if PROCESS_RE.search(line):
            add(issues, "failure", f"Process instruction leaked into manuscript near collected line {lineno}: {line.strip()[:140]}")


def validate_paper(root: Path, requested_mode: str | None, issues: list[Issue]) -> None:
    state_path = root / "paper_state.json"
    state: dict[str, object] = {}
    if state_path.is_file():
        try:
            state = load_json_object(state_path)
        except ContractError as exc:
            add(issues, "failure", str(exc))
            return

    state_mode = state.get("mode")
    mode = requested_mode or (state_mode if isinstance(state_mode, str) else "draft")
    if mode not in VALID_MODES - {"skill"}:
        add(issues, "failure", f"Unknown paper mode: {mode}")
        return
    if requested_mode and state_mode and requested_mode != state_mode:
        add(issues, "failure", f"Requested mode {requested_mode} conflicts with paper_state.json mode {state_mode}.")

    if mode in {"full-paper", "submission"} and not state_path.is_file():
        add(issues, "failure", f"{mode} mode requires paper_state.json.")
        return
    if not state:
        add(issues, "warning", "Draft mode has no paper_state.json; only manuscript checks can run.")
        candidates = sorted(root.rglob("main.tex"))
        if len(candidates) != 1:
            add(issues, "failure", "Draft mode without paper_state.json requires exactly one main.tex.")
            return
        validate_manuscript(candidates[0], issues)
        return

    if state.get("schema_version") != SCHEMA_VERSION:
        add(issues, "failure", f"paper_state.json schema_version must be {SCHEMA_VERSION}.")
    unknown_state = sorted(set(state) - STATE_FIELDS)
    if unknown_state:
        add(issues, "failure", "paper_state.json contains unknown fields: " + ", ".join(unknown_state))
    if state.get("mode") not in VALID_MODES - {"skill"}:
        add(issues, "failure", "paper_state.json mode must be draft, full-paper, or submission.")
    stage = state_string(state, "stage", issues)
    target_venue = state_string(state, "target_venue", issues)
    main_value = state_string(state, "main_tex", issues)
    bib_value = state_string(state, "bibliography", issues)
    del target_venue
    if not main_value or not bib_value:
        return

    main_tex = require_nonempty(root, main_value, issues)
    bibliography = require_nonempty(root, bib_value, issues)
    terminal = stage in TERMINAL_STAGES
    blockers = state.get("blockers")
    if not isinstance(blockers, list) or any(not isinstance(item, str) for item in blockers):
        add(issues, "failure", "paper_state.json blockers must be a list of strings.")
    elif terminal and blockers:
        add(issues, "failure", "A terminal stage cannot contain unresolved blockers: " + "; ".join(blockers))

    required = state.get("required_artifacts")
    if not isinstance(required, list) or any(not isinstance(item, str) or not item for item in required):
        add(issues, "failure", "paper_state.json required_artifacts must be a list of non-empty paths.")
        required = []
    baseline = ["paper_story.md", "claim_evidence_map.md", "citation_verification.md", "build_check.md", "plan/progress.md"]
    if mode == "submission":
        baseline.append("submission_readiness.md")
    for relative in sorted(set(baseline + list(required))):
        require_nonempty(root, relative, issues)
    packet_dir = root / "plan/task-packets"
    if not packet_dir.is_dir() or not any(packet_dir.glob("*.md")):
        add(issues, "failure", "Full-paper modes require at least one plan/task-packets/*.md file.")

    progress = root / "plan/progress.md"
    if terminal and progress.is_file() and STALE_PROGRESS_RE.search(read_utf8(progress)):
        add(issues, "failure", "plan/progress.md still describes verification as pending.")

    claim_map = root / "claim_evidence_map.md"
    if claim_map.is_file():
        validate_claim_map(claim_map, terminal, issues)

    if main_tex.is_file():
        validate_manuscript(main_tex, issues)
        numeric_registry = root / "numeric_evidence.json"
        if numeric_registry.is_file():
            try:
                findings = verify_numeric_evidence(root, main_tex, numeric_registry)
                if findings:
                    preview = "; ".join(
                        f"{item.value:g} in {item.section} (collected line {item.line})"
                        for item in findings[:8]
                    )
                    suffix = f"; plus {len(findings) - 8} more" if len(findings) > 8 else ""
                    add(issues, "failure", "Unverified manuscript numbers: " + preview + suffix)
            except ContractError as exc:
                add(issues, "failure", str(exc))
    if main_tex.is_file() and bibliography.is_file():
        try:
            cited = collect_citation_keys(main_tex)
            bib_keys = collect_bib_keys(bibliography)
            duplicates = sorted({key for key in bib_keys if bib_keys.count(key) > 1})
            missing = sorted(cited - set(bib_keys))
            if missing:
                add(issues, "failure", "Missing BibTeX keys: " + ", ".join(missing))
            if duplicates:
                add(issues, "failure", "Duplicate BibTeX keys: " + ", ".join(duplicates))
            verification = root / "citation_verification.md"
            if verification.is_file() and terminal:
                scholarly = validate_verification_table(verification, cited, issues)
                if scholarly:
                    requests_path = root / "citation_requests.json"
                    lock_path = root / "citation_lock.json"
                    if not requests_path.is_file() or not lock_path.is_file():
                        add(
                            issues,
                            "failure",
                            "Terminal scholarly citations require citation_requests.json and citation_lock.json.",
                        )
                    else:
                        for failure in validate_lock(root, main_tex, requests_path, lock_path):
                            add(issues, "failure", failure)
        except ContractError as exc:
            add(issues, "failure", str(exc))

    build = state.get("build")
    if not isinstance(build, dict):
        add(issues, "failure", "paper_state.json requires a build object.")
    else:
        unknown_build = sorted(set(build) - BUILD_FIELDS)
        if unknown_build:
            add(issues, "failure", "paper_state.json build contains unknown fields: " + ", ".join(unknown_build))
        if build.get("status") not in {"not-run", "blocked", "failed", "passed"}:
            add(issues, "failure", "build.status must be not-run, blocked, failed, or passed.")
        if not isinstance(build.get("command"), str) or not build["command"]:
            add(issues, "failure", "build.command must be a non-empty string.")
        external_records = external_build_records(build, issues)
    if isinstance(build, dict) and terminal:
        if build.get("status") != "passed":
            add(issues, "failure", "A terminal stage requires build.status = passed.")
        if stage == "submission-ready" and build.get("attestation") != "executed":
            add(issues, "failure", "submission-ready requires record_build.py --run attestation.")
        if build.get("attestation") == "executed":
            if build.get("exit_code") != 0:
                add(issues, "failure", "Executed build attestation requires exit_code = 0.")
            log_value = build.get("log")
            if not isinstance(log_value, str) or not log_value:
                add(issues, "failure", "Executed build attestation requires a build log path.")
            else:
                log_path = require_nonempty(root, log_value, issues)
                if log_path.is_file() and build.get("log_sha256") != digest_file(log_path):
                    add(issues, "failure", "Recorded build log digest does not match the current log.")
        pdf_value = build.get("pdf")
        input_digest = build.get("input_sha256")
        pdf_digest = build.get("pdf_sha256")
        if not isinstance(pdf_value, str) or not pdf_value:
            add(issues, "failure", "build.pdf must be a non-empty path.")
        else:
            pdf_path = require_nonempty(root, pdf_value, issues)
            if main_tex.is_file() and bibliography.is_file() and pdf_path.is_file():
                try:
                    if build.get("attestation") == "executed":
                        external_records.append(
                            json.dumps(
                                {"command": build.get("command"), "tool_version": build.get("tool_version")},
                                sort_keys=True,
                                separators=(",", ":"),
                            )
                        )
                    actual_input = digest_files(root, paper_input_files(root, main_tex, bibliography), external_records)
                    actual_pdf = digest_file(pdf_path)
                    if input_digest != actual_input:
                        add(issues, "failure", "Build input digest is stale; rebuild the PDF and record the new digest.")
                    if pdf_digest != actual_pdf:
                        add(issues, "failure", "Recorded PDF digest does not match the current PDF.")
                except ContractError as exc:
                    add(issues, "failure", str(exc))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--mode", choices=sorted(VALID_MODES), help="Override mode; must match paper_state.json when present")
    args = parser.parse_args()

    root = args.project_path.resolve()
    if not root.is_dir():
        print(f"Project directory does not exist: {root}", file=sys.stderr)
        return 2

    inferred_skill = (root / "SKILL.md").is_file() and (root / "references").is_dir()
    mode = args.mode or ("skill" if inferred_skill else None)
    issues: list[Issue] = []
    try:
        if mode == "skill":
            validate_skill(root, issues)
        else:
            validate_paper(root, mode, issues)
    except ContractError as exc:
        add(issues, "failure", str(exc))

    for level in ("warning", "failure"):
        selected = [issue.message for issue in issues if issue.level == level]
        if selected:
            print(f"{level.title()}s:")
            for message in selected:
                print(f"  - {message}")
    failures = [issue for issue in issues if issue.level == "failure"]
    if failures:
        print(f"Research quality gate failed with {len(failures)} failure(s).")
        return 1
    print("Research quality gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
