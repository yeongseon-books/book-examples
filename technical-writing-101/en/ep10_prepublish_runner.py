from common import ep10_prepublish, read_text


def analyze(path: str) -> dict:
    return ep10_prepublish(read_text(path))
