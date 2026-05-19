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

from en.ep04_pr_validator import run_example as run_en
from ko.ep04_pr_validator import run_example as run_ko


def test_ep04_behavior():
    assert run_ko() == []
    bad = '## Summary\nNo issue ref\n- [x] one'
    assert 'missing_closes' in validate_pr_description(bad)
    assert run_en() == []
