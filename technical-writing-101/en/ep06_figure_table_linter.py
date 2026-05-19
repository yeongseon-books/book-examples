from common import ep06_figure_table_lint, read_text


def analyze(path: str) -> dict:
    return ep06_figure_table_lint(read_text(path))
