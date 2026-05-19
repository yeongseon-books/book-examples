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

from en.ep08_maintainer_triage import run_example as run_en
from ko.ep08_maintainer_triage import run_example as run_ko


def test_ep08_behavior():
    result = run_ko()
    assert result == {'bug': 1, 'enhancement': 1, 'question': 1, 'other': 0}
    assert run_en()['bug'] == 1
    assert triage_issues([Issue(id=4, title='misc', labels=[])])['other'] == 1
