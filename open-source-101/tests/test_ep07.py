from pathlib import Path

from common import (
    bump_semver,
    detect_spdx_license,
    initialize_python_project,
    is_license_compatible,
    parse_markdown_front_matter,
    score_portfolio,
    score_readme,
    triage_issues,
    validate_contributing_files,
    validate_pr_description,
    Issue,
)

from en.ep07_contributing_validator import run_example as run_en
from ko.ep07_contributing_validator import run_example as run_ko


def test_ep07_behavior():
    result = run_ko()
    assert result['has_steps'] is True
    assert result['has_code_of_conduct'] is True
    assert run_en()['has_code_of_conduct'] is True
