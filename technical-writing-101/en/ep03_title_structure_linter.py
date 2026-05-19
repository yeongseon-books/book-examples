"""Technical Writing 101 - Episode 3: Title structure linter."""

from common import ep03_structure_lint, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep03_structure_lint(read_text(path))
