"""Tests for ep05 in Harness Engineering 101."""

import pytest
from common import ToolHarness, ToolSpec
from conftest import load_episode


def test_ep05_tool_harness_rejects_unknown_tool():
    """Test ep05 tool harness rejects unknown tool."""
    m = load_episode("ko", "05-tool-harness")
    assert m.tool_harness_example()["value"] == "resolved:customer-1"
    h = ToolHarness([ToolSpec("known", {"k"}, {"value"}, lambda k: {"value": k})])
    with pytest.raises(ValueError):
        h.invoke("unknown", {"k": "v"})
