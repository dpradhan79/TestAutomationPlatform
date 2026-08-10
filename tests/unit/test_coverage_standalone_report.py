import json
from pathlib import Path

import pytest

from src.shared.tools.coverage_json_to_standalone_html import generate_standalone_report


@pytest.mark.unit
def test_generate_standalone_report_creates_html(tmp_path: Path) -> None:
    input_file = tmp_path / "coverage.json"
    output_file = tmp_path / "coverage-self-contained.html"

    sample_payload = {
        "meta": {"version": "7.0"},
        "totals": {
            "covered_lines": 9,
            "missing_lines": 1,
            "num_statements": 10,
            "percent_covered": 90.0,
        },
        "files": {
            "src/shared/llm/factory.py": {
                "summary": {
                    "covered_lines": 8,
                    "missing_lines": 1,
                    "num_statements": 9,
                    "percent_covered": 88.89,
                },
                "missing_lines": [24],
            },
            "src/shared/config/llm_config.py": {
                "summary": {
                    "covered_lines": 1,
                    "missing_lines": 0,
                    "num_statements": 1,
                    "percent_covered": 100.0,
                },
                "missing_lines": [],
            },
        },
    }

    input_file.write_text(json.dumps(sample_payload), encoding="utf-8")

    generate_standalone_report(
        input_path=input_file,
        output_path=output_file,
        title="CI Coverage",
    )

    html_text = output_file.read_text(encoding="utf-8")

    assert output_file.exists()
    assert "CI Coverage" in html_text
    assert "Standalone coverage report generated from JSON input." in html_text
    assert "src/shared/llm/factory.py" in html_text
    assert "88.89%" in html_text
    assert "<style>" in html_text


@pytest.mark.unit
def test_generate_standalone_report_fails_on_missing_json(tmp_path: Path) -> None:
    missing_input = tmp_path / "missing.json"
    output_file = tmp_path / "coverage-self-contained.html"

    with pytest.raises(FileNotFoundError):
        generate_standalone_report(
            input_path=missing_input,
            output_path=output_file,
            title="Coverage Report",
        )

