"""Tests for ep10 in Ai Agent 101."""

from conftest import load_module

run = load_module("ko/10-building-first-agent/step01_capstone_agent.py", "ep10").run


def test_ep10_capstone_runs() -> None:
    """Test ep10 capstone runs."""
    result = run("도쿄 날씨를 확인하고 우산 필요 여부를 알려줘")
    assert result["success"] is True
    assert result["calc"] == 500.0
