"""Tests for ep04 in Ai Agent 101."""

from conftest import load_module

run_workflow = load_module(
    "ko/04-agent-workflow-design/step01_workflow_patterns.py", "ep04"
).run_workflow


def test_ep04_branching_path() -> None:
    """Test ep04 branching path."""
    result = run_workflow("report", 0.4)
    assert "search_more" in result["steps"]
