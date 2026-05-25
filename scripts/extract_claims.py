#!/usr/bin/env python3
"""Bootstrap a claim-evidence map from Abstract/Introduction text.

This is a heuristic extractor. It finds likely claim sentences; a human/agent
must still verify evidence and revise unsupported claims.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CLAIM_RE = re.compile(
    r"\b("
    r"we\s+(propose|introduce|present|show|demonstrate|find|observe|achieve|enable|support)|"
    r"our\s+(method|system|approach|framework|workflow|results)|"
    r"outperform|improve|reduce|increase|achieve|enable|support|demonstrate|show|"
    r"first|novel|new|state-of-the-art|sota|robust|general|unified|end-to-end|"
    r"significant|substantial|effective|efficient"
    r")\b",
    re.IGNORECASE,
)

SECTION_RE = re.compile(
    r"\\section\*?\{(?P<title>[^}]*)\}(?P<body>.*?)(?=\\section\*?\{|\\appendix\b|\\bibliography\b|$)",
    re.DOTALL,
)
MACRO_RE = re.compile(r"\\(?:re)?newcommand\{\\([A-Za-z]+)\}\{([^{}]*)\}")
FLOAT_RE = re.compile(r"\\begin\{(?:figure|figure\*|table|table\*)\}.*?\\end\{(?:figure|figure\*|table|table\*)\}", re.DOTALL)


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        escaped = False
        out: list[str] = []
        for char in line:
            if char == "%" and not escaped:
                break
            out.append(char)
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def collect_macros(text: str) -> dict[str, str]:
    return {match.group(1): match.group(2) for match in MACRO_RE.finditer(text)}


def apply_macros(text: str, macros: dict[str, str]) -> str:
    for name, value in macros.items():
        text = re.sub(rf"\\{re.escape(name)}\b", value, text)
    return text


def latex_to_text(text: str, macros: dict[str, str] | None = None) -> str:
    if macros:
        text = apply_macros(text, macros)
    text = FLOAT_RE.sub(" ", text)
    text = re.sub(r"\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{[^}]*\}", "[CITE]", text)
    text = re.sub(r"\\ref\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", " ", text)
    text = text.replace("~", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_target_text(path: Path, sections: set[str]) -> list[tuple[str, str]]:
    raw = strip_comments(path.read_text(encoding="utf-8"))
    macros = collect_macros(raw)
    chunks: list[tuple[str, str]] = []

    abstract_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", raw, re.DOTALL)
    if abstract_match and "abstract" in sections:
        chunks.append(("Abstract", apply_macros(abstract_match.group(1), macros)))

    for match in SECTION_RE.finditer(raw):
        title = latex_to_text(match.group("title"), macros).lower()
        if title in sections:
            chunks.append((match.group("title"), apply_macros(match.group("body"), macros)))

    if not chunks:
        chunks.append((path.name, raw))
    return chunks


def split_sentences(text: str) -> list[str]:
    text = latex_to_text(text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text)
    return [part.strip() for part in parts if len(part.strip()) > 20]


def escape_md(text: str) -> str:
    return text.replace("|", "\\|").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="LaTeX or Markdown files to scan")
    parser.add_argument(
        "--sections",
        default="abstract,introduction",
        help="Comma-separated section names to scan; default: abstract,introduction",
    )
    parser.add_argument("--all-sentences", action="store_true", help="Output all sentences, not just likely claims")
    args = parser.parse_args()

    sections = {item.strip().lower() for item in args.sections.split(",") if item.strip()}
    rows: list[tuple[str, str, str]] = []

    for path in args.files:
        for section, body in extract_target_text(path, sections):
            for sentence in split_sentences(body):
                if args.all_sentences or CLAIM_RE.search(sentence):
                    rows.append((str(path), section, sentence))

    print("| ID | Source | Section | Claim | Evidence | Status | Revision |")
    print("|---|---|---|---|---|---|---|")
    for idx, (source, section, sentence) in enumerate(rows, start=1):
        print(
            f"| C{idx} | {escape_md(source)} | {escape_md(section)} | "
            f"{escape_md(sentence)} |  | needs evidence |  |"
        )

    if not rows:
        print("\nNo likely claims found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
