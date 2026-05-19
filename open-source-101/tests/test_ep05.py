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

from en.ep05_readme_scorer import run_example as run_en
from ko.ep05_readme_scorer import run_example as run_ko


def test_ep05_behavior():
    assert run_ko() == 100
    assert run_en() == 100
    assert score_readme('# only title') == 0
