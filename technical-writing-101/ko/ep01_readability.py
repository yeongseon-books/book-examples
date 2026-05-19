from common import ep01_readability, read_text


def analyze(path: str) -> dict:
    return ep01_readability(read_text(path), lang="ko")
