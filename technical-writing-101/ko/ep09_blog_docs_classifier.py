"""Technical Writing 101 - Episode 9: Blog docs classifier."""

from common import ep09_blog_vs_docs, read_text


def analyze(path: str) -> dict:
    """Analyze."""
    return ep09_blog_vs_docs(read_text(path))
