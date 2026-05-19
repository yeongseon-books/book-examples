from ko.ep10_test_strategy import analyze_test_pyramid, suggest_gap


def test_ep10_strategy_analyzer_and_suggestion():
    counts = analyze_test_pyramid("tests")
    assert counts["integration"] >= 1
    assert counts["e2e"] >= 1
    assert suggest_gap(counts) in {
        "Balanced enough for current stage",
        "Increase unit tests",
        "Add at least one integration test",
        "Add at least one end-to-end test",
    }
