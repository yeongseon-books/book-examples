"""Tests for ep08 in Model Evaluation 101."""

from conftest import load_module

run = load_module("ko/08-cross-validation/step01_cross_validation_demo.py", "ep08").run


def test_ep08_kfold_returns_n_scores() -> None:
    """Test ep08 kfold returns n scores."""
    out = run()
    assert out["n_scores"] == 5
    assert out["std"] >= 0.0
