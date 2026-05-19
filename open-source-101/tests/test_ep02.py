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

from en.ep02_license_compatibility import run_example as run_en
from ko.ep02_license_compatibility import run_example as run_ko


def test_ep02_behavior():
    assert run_ko() is True
    assert run_en() is True
    assert is_license_compatible('Apache-2.0', 'GPL-3.0-only') is False
