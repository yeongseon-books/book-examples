"""Tests for ep07 in Ai Evaluation 101."""

from conftest import load_module


def test_ep07_agent_trajectory_matches_expected_plan() -> None:
    """Test ep07 agent trajectory matches expected plan."""
    module = load_module("ko/07-agent-evaluation/step01_agent_trajectory.py", "ep07")
    result = module.run()
    assert result["task_success"] == 1.0
    assert result["step_overhead"] == 1.0
