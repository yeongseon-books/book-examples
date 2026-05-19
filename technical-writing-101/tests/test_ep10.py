from en.ep10_prepublish_runner import analyze


def test_ep10_combined_report():
    assert analyze("fixtures/ep10_good.md")["pass"]
    assert not analyze("fixtures/ep10_bad.md")["pass"]
