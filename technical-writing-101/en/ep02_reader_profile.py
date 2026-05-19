"""Technical Writing 101 - Episode 2: Reader profile."""

from common import ep02_audience_profile, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep02_audience_profile(read_text(path))
