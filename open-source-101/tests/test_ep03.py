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

from en.ep03_issue_template_parser import run_example as run_en
from ko.ep03_issue_template_parser import run_example as run_ko


def test_ep03_behavior():
    result = run_ko()
    assert result.get('name') == 'Bug report'
    assert run_en().get('about') == 'Report a reproducible bug'
    assert parse_markdown_front_matter('no front matter') == {}
