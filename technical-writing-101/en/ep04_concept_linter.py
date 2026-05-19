from common import ep04_what_before_how, read_text


def analyze(path: str) -> dict:
    return ep04_what_before_how(read_text(path))
