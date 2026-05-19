"""Git Github 101 - Episode 1: Commit message."""

from __future__ import annotations

from common import CommitMessageLinter


def run(message: str) -> dict[str, object]:
    """Run."""
    linter = CommitMessageLinter()
    return linter.lint(message)
