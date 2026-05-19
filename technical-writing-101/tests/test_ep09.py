from en.ep09_blog_docs_classifier import analyze


def test_ep09_classifier():
    blog = analyze("fixtures/ep09_blog.md")
    docs = analyze("fixtures/ep09_docs.md")
    assert blog["classification"] == "blog"
    assert docs["classification"] == "docs"
