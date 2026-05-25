#!/usr/bin/env python3
"""Generate a booktabs LaTeX table from a CSV file."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


SPECIALS = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
}


def latex_escape(value: str) -> str:
    return "".join(SPECIALS.get(char, char) for char in value)


def to_float(value: str) -> float | None:
    try:
        num = float(value)
    except ValueError:
        return None
    if math.isnan(num) or math.isinf(num):
        return None
    return num


def format_value(value: str, precision: int | None) -> str:
    num = to_float(value)
    if num is not None and precision is not None:
        return f"{num:.{precision}f}"
    return latex_escape(value)


def choose_bold_values(rows: list[dict[str, str]], columns: list[str], mode: str, bold_columns: set[str]) -> dict[str, float]:
    chosen: dict[str, float] = {}
    if mode == "none":
        return chosen
    for column in columns:
        if bold_columns and column not in bold_columns:
            continue
        nums = [to_float(row.get(column, "")) for row in rows]
        nums = [num for num in nums if num is not None]
        if not nums:
            continue
        chosen[column] = max(nums) if mode == "max" else min(nums)
    return chosen


def build_table(
    rows: list[dict[str, str]],
    columns: list[str],
    caption: str,
    label: str,
    precision: int | None,
    bold: str,
    bold_columns: set[str],
) -> str:
    align = "l" + "c" * (len(columns) - 1)
    chosen = choose_bold_values(rows, columns, bold, bold_columns)
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        rf"\caption{{{latex_escape(caption)}}}",
        rf"\label{{{label}}}",
        rf"\begin{{tabular}}{{{align}}}",
        r"\toprule",
        " & ".join(latex_escape(column) for column in columns) + r" \\",
        r"\midrule",
    ]
    for row in rows:
        cells: list[str] = []
        for column in columns:
            raw = row.get(column, "")
            cell = format_value(raw, precision)
            num = to_float(raw)
            if column in chosen and num is not None and abs(num - chosen[column]) < 1e-12:
                cell = rf"\textbf{{{cell}}}"
            cells.append(cell)
        lines.append(" & ".join(cells) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--output", type=Path, help="Write table to file instead of stdout")
    parser.add_argument("--caption", default="Results.")
    parser.add_argument("--label", default="tab:results")
    parser.add_argument("--columns", help="Comma-separated columns; default uses CSV header")
    parser.add_argument("--precision", type=int, default=None, help="Decimal precision for numeric cells")
    parser.add_argument("--bold", choices=["none", "max", "min"], default="none")
    parser.add_argument("--bold-columns", default="", help="Comma-separated columns eligible for bolding")
    args = parser.parse_args()

    with args.csv_file.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        if reader.fieldnames is None:
            raise SystemExit("CSV file has no header row.")
        columns = [item.strip() for item in args.columns.split(",")] if args.columns else list(reader.fieldnames)

    bold_columns = {item.strip() for item in args.bold_columns.split(",") if item.strip()}
    table = build_table(rows, columns, args.caption, args.label, args.precision, args.bold, bold_columns)

    if args.output:
        args.output.write_text(table, encoding="utf-8")
    else:
        print(table, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
