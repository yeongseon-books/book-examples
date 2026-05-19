from en.ep07_readme_scorer import analyze


def test_ep07_readme_score():
    good = analyze("fixtures/ep07_readme_good.md")
    bad = analyze("fixtures/ep07_readme_bad.md")
    assert good["required_score"] == 1.0
    assert bad["required_score"] < 1.0
