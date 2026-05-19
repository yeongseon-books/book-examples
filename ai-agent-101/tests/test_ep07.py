"""Tests for ep07 in Ai Agent 101."""

from conftest import load_module

evaluate = load_module("ko/07-agent-evaluation/step01_eval_metrics.py", "ep07").evaluate


def test_ep07_eval_metrics() -> None:
    """Test ep07 eval metrics."""
    metric = evaluate([{"success": True, "steps": 2}, {"success": False, "steps": 4}])
    assert metric["success_rate"] == 0.5
    assert metric["avg_steps"] == 3.0
