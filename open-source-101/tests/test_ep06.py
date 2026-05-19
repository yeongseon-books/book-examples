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

from en.ep06_semver_bumper import run_example as run_en
from ko.ep06_semver_bumper import run_example as run_ko


def test_ep06_behavior():
    assert run_ko() == '1.3.0'
    assert run_en() == '1.3.0'
    assert bump_semver('1.2.3', 'patch') == '1.2.4'
