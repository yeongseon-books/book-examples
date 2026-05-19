from common import ep08_tutorial_structure, read_text


def analyze(path: str) -> dict:
    return ep08_tutorial_structure(read_text(path))
