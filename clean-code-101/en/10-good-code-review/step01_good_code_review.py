"""Clean Code 101 - Episode 1: Good code review."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewComment:
    """Review comment."""

    level: str
    message: str


def classify_comment(level: str, message: str) -> ReviewComment:
    """Classify comment."""
    allowed = {"NIT", "SUGG", "MUST", "QUESTION"}
    if level not in allowed:
        raise ValueError("unknown review level")
    if len(message.strip()) < 10:
        raise ValueError("comment must be actionable")
    return ReviewComment(level=level, message=message)


def is_small_pr(changed_lines: int) -> bool:
    """Is small pr."""
    return changed_lines < 400
