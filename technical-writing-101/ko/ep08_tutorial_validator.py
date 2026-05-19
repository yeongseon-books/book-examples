"""Technical Writing 101 - Episode 8: Tutorial validator."""

from common import ep08_tutorial_structure, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep08_tutorial_structure(read_text(path))
