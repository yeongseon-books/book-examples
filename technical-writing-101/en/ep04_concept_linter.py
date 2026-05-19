"""Technical Writing 101 - Episode 4: Concept linter."""

from common import ep04_what_before_how, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep04_what_before_how(read_text(path))
