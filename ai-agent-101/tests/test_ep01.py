"""Tests for ep01 in Ai Agent 101."""

from conftest import load_module

run = load_module("ko/01-what-is-an-ai-agent/step01_manual_loop.py", "ep01").run


def test_ep01_manual_loop_success() -> None:
    """Test ep01 manual loop success."""
    result = run("도쿄 날씨를 확인하고 우산 필요 여부를 알려줘")
    assert result["success"] is True
    assert "Umbrella" in str(result["answer"])
