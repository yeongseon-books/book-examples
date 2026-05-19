from common import ep07_readme_score, read_text


def analyze(path: str) -> dict:
    return ep07_readme_score(read_text(path))
