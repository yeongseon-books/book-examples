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

from en.ep01_license_detector import run_example as run_en
from ko.ep01_license_detector import run_example as run_ko


def test_ep01_behavior():
    assert run_ko() == 'MIT'
    assert run_en() == 'MIT'
    apache = Path('fixtures/LICENSE_APACHE.txt').read_text(encoding='utf-8')
    assert detect_spdx_license(apache) == 'Apache-2.0'
