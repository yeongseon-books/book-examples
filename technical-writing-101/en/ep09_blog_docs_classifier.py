from common import ep09_blog_vs_docs, read_text


def analyze(path: str) -> dict:
    return ep09_blog_vs_docs(read_text(path))
