"""Tests for ep03 in Ai Agent 101."""

from conftest import load_module

dispatch = load_module(
    "ko/03-tool-use-fundamentals/step01_tool_dispatch.py", "ep03"
).dispatch


def test_ep03_dispatch_calculate() -> None:
    """Test ep03 dispatch calculate."""
    result = dispatch("calculate", {"expression": "3*4"})
    assert result["success"] is True
    assert result["data"] == 12.0
