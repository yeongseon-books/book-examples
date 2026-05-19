"""Tests for ep09 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep09_split() -> None:
    """Test ep09 split."""
    result = run_dict("ko/09-train-eval-test-splitting/step01_stratified_split.py")
    train = result["train"]
    test = result["test"]
    assert isinstance(train, dict)
    assert isinstance(test, dict)
    assert train["pos"] == train["neg"]
    assert test["pos"] == test["neg"]
