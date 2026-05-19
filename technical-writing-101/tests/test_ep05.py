from en.ep05_code_validator import analyze


def test_ep05_code_rules():
    good = analyze("fixtures/ep05_good.md")
    bad = analyze("fixtures/ep05_bad.md")
    assert good["missing_language_tags"] == 0
    assert bad["missing_language_tags"] > 0 or bad["long_code_lines"] > 0
