"""Technical Writing 101 - Episode 5: Code validator."""

from common import ep05_code_example_lint, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep05_code_example_lint(read_text(path))
