"""Technical Writing 101 - Episode 1: Readability."""

from common import ep01_readability, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep01_readability(read_text(path), lang="en")
