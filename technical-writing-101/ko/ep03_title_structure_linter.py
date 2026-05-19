from common import ep03_structure_lint, read_text


def analyze(path: str) -> dict:
    return ep03_structure_lint(read_text(path))
