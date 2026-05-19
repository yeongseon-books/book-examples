"""Technical Writing 101 - Episode 7: Readme scorer."""

from common import ep07_readme_score, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep07_readme_score(read_text(path))
