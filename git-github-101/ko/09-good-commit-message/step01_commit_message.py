"""Git Github 101 - 9편: good commit message 예제."""

from __future__ import annotations

from common import CommitMessageLinter


def run(message: str) -> dict[str, object]:
    """Run."""
    linter = CommitMessageLinter()
    return linter.lint(message)
