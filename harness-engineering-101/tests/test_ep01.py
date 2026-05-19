"""Tests for ep01 in Harness Engineering 101."""

from conftest import load_episode


def test_ep01_mock_llm_baseline():
    """Test ep01 mock llm baseline."""
    m = load_episode("ko", "01-what-is-harness-engineering")
    out = m.what_is_harness_engineering_example()
    assert out["answer"] == "ok"
