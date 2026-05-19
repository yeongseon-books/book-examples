"""Tests for ep06 in Rag Deep Dive."""

from ko.ep06_evaluation import containment, evaluate, exact_match, reciprocal_rank


def test_ep06_metric_functions():
    """Test ep06 metric functions."""
    assert exact_match("A", "a") == 1.0
    assert containment("hello overlap", "overlap") == 1.0
    assert reciprocal_rank(["x", "y", "z"], "y") == 0.5


def test_ep06_eval_gate_passes():
    """Test ep06 eval gate passes."""
    metrics = evaluate(fixtures_dir="fixtures", threshold=0.3)
    assert metrics["containment"] >= 0.3
    assert metrics["pass_gate"] is True
