"""Technical Writing 101 - Episode 10: Prepublish runner."""

from common import ep10_prepublish, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep10_prepublish(read_text(path))
