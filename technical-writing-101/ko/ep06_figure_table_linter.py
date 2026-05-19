"""Technical Writing 101 - Episode 6: Figure table linter."""

from common import ep06_figure_table_lint, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep06_figure_table_lint(read_text(path))
