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

from en.ep09_portfolio_scorer import run_example as run_en
from ko.ep09_portfolio_scorer import run_example as run_ko


def test_ep09_behavior():
    score = run_ko()
    assert score == 150
    assert run_en() == 150
    assert score_portfolio('[]') == 0
