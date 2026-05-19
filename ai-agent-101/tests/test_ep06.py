"""Tests for ep06 in Ai Agent 101."""

from conftest import load_module

supervisor = load_module(
    "ko/06-multi-agent-systems/step01_supervisor_handoff.py", "ep06"
).supervisor


def test_ep06_supervisor_selects_worker() -> None:
    """Test ep06 supervisor selects worker."""
    result = supervisor("시장 조사")
    assert result["worker"] == "ResearchWorker"
