from common import ep02_audience_profile, read_text


def analyze(path: str) -> dict:
    return ep02_audience_profile(read_text(path))
