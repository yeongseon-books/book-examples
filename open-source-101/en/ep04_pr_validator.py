from __future__ import annotations

from pathlib import Path

from common import (
    Issue,
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
)


def run_example() -> object:
    text = Path('fixtures/PR_TEMPLATE.md').read_text(encoding='utf-8')
    return validate_pr_description(text)


if __name__ == '__main__':
    print(run_example())
