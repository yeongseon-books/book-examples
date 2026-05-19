"""Open Source 101 - Episode 8: Maintainer triage."""

from __future__ import annotations

from common import (
    Issue,
    triage_issues,
)


def run_example() -> object:
    """Run example."""
    issues = [
        Issue(id=1, title="Fix crash", labels=["bug"]),
        Issue(id=2, title="New idea", labels=["enhancement"]),
        Issue(id=3, title="How to install?", labels=["question"]),
    ]
    return triage_issues(issues)


if __name__ == "__main__":
    print(run_example())
