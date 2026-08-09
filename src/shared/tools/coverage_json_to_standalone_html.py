from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path
from typing import Any


def _as_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0


def _badge_class(percent: float) -> str:
    if percent >= 90.0:
        return "good"
    if percent >= 75.0:
        return "warn"
    return "bad"


def build_standalone_report(data: dict[str, Any], title: str) -> str:
    totals = data.get("totals", {})
    files = data.get("files", {})

    total_percent = _as_float(totals.get("percent_covered", totals.get("percent_covered_display", 0.0)))
    total_covered = int(totals.get("covered_lines", 0))
    total_missing = int(totals.get("missing_lines", 0))
    total_statements = int(totals.get("num_statements", total_covered + total_missing))

    file_rows: list[str] = []
    for file_path, payload in sorted(files.items(), key=lambda item: item[0]):
        summary = payload.get("summary", {})
        covered = int(summary.get("covered_lines", 0))
        missing = int(summary.get("missing_lines", 0))
        statements = int(summary.get("num_statements", covered + missing))
        percent = _as_float(summary.get("percent_covered", summary.get("percent_covered_display", 0.0)))
        missing_lines = payload.get("missing_lines", [])
        missing_text = ", ".join(str(line) for line in missing_lines) if missing_lines else "-"

        file_rows.append(
            "".join(
                [
                    "<tr>",
                    f"<td><code>{escape(file_path)}</code></td>",
                    f"<td>{statements}</td>",
                    f"<td>{covered}</td>",
                    f"<td>{missing}</td>",
                    f"<td><span class='pill {_badge_class(percent)}'>{percent:.2f}%</span></td>",
                    f"<td class='missing'>{escape(missing_text)}</td>",
                    "</tr>",
                ]
            )
        )

    table_body = "\n".join(file_rows) if file_rows else "<tr><td colspan='6'>No file coverage data found.</td></tr>"

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{escape(title)}</title>
  <style>
    :root {{
      --bg: #0b1020;
      --panel: #121a2f;
      --text: #e8ecf7;
      --muted: #98a1b8;
      --good: #179d5d;
      --warn: #e0a100;
      --bad: #c93c3c;
      --border: #243152;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 24px;
      font-family: Segoe UI, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
    }}
    h1 {{ margin: 0 0 12px 0; font-size: 1.5rem; }}
    .meta {{ color: var(--muted); margin-bottom: 20px; }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-bottom: 20px;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
    }}
    .label {{ color: var(--muted); font-size: 0.85rem; }}
    .value {{ margin-top: 6px; font-size: 1.2rem; font-weight: 600; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
    }}
    th, td {{
      text-align: left;
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }}
    th {{ color: var(--muted); font-weight: 600; }}
    tr:hover td {{ background: rgba(255,255,255,0.02); }}
    code {{ color: #b8c4e6; }}
    .pill {{
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #fff;
      display: inline-block;
      min-width: 72px;
      text-align: center;
    }}
    .pill.good {{ background: var(--good); }}
    .pill.warn {{ background: var(--warn); color: #1e1e1e; }}
    .pill.bad {{ background: var(--bad); }}
    .missing {{ color: var(--muted); font-size: 0.9rem; }}
  </style>
</head>
<body>
  <h1>{escape(title)}</h1>
  <div class=\"meta\">Standalone coverage report generated from JSON input.</div>

  <section class=\"stats\">
    <div class=\"card\">
      <div class=\"label\">Total Coverage</div>
      <div class=\"value\"><span class=\"pill {_badge_class(total_percent)}\">{total_percent:.2f}%</span></div>
    </div>
    <div class=\"card\">
      <div class=\"label\">Statements</div>
      <div class=\"value\">{total_statements}</div>
    </div>
    <div class=\"card\">
      <div class=\"label\">Covered Lines</div>
      <div class=\"value\">{total_covered}</div>
    </div>
    <div class=\"card\">
      <div class=\"label\">Missing Lines</div>
      <div class=\"value\">{total_missing}</div>
    </div>
  </section>

  <table>
    <thead>
      <tr>
        <th>File</th>
        <th>Statements</th>
        <th>Covered</th>
        <th>Missing</th>
        <th>Coverage</th>
        <th>Missing Line Numbers</th>
      </tr>
    </thead>
    <tbody>
      {table_body}
    </tbody>
  </table>
</body>
</html>
"""


def generate_standalone_report(input_path: Path, output_path: Path, title: str) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Coverage JSON not found: {input_path}")

    with input_path.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    report_html = build_standalone_report(payload, title)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_html, encoding="utf-8")


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a standalone single-file HTML coverage report from coverage JSON.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("reports/coverage/coverage.json"),
        help="Path to coverage JSON file produced by pytest-cov.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports/coverage/coverage-self-contained.html"),
        help="Output path for standalone HTML coverage report.",
    )
    parser.add_argument(
        "--title",
        type=str,
        default="Coverage Report",
        help="Title to render in the HTML report.",
    )
    return parser


def main() -> int:
    parser = _build_arg_parser()
    args = parser.parse_args()

    generate_standalone_report(args.input, args.output, args.title)
    print(f"Standalone coverage report written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

