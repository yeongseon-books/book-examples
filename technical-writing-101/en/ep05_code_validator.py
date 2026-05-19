from common import ep05_code_example_lint, read_text


def analyze(path: str) -> dict:
    return ep05_code_example_lint(read_text(path))
