"""Tests for ep10 in Testing 101."""

from ko.ep10_test_strategy import analyze_test_pyramid, suggest_gap


def test_ep10_strategy_analyzer_and_suggestion():
    """Test ep10 strategy analyzer and suggestion."""
    counts = analyze_test_pyramid("tests")
    assert counts["integration"] >= 1
    assert counts["e2e"] >= 1
    assert suggest_gap(counts) in {
        "Balanced enough for current stage",
        "Increase unit tests",
        "Add at least one integration test",
        "Add at least one end-to-end test",
    }
