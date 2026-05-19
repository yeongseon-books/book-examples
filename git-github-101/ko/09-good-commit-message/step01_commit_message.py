from __future__ import annotations

from common import CommitMessageLinter


def run(message: str) -> dict[str, object]:
    linter = CommitMessageLinter()
    return linter.lint(message)
