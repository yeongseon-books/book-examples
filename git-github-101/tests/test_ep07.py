"""Tests for ep07 in Git Github 101."""

from conftest import load_module

run = load_module("ko/07-pull-request/step01_pull_request.py", "ep07").run


def test_ep07_pr_state_flow() -> None:
    """Test ep07 pr state flow."""
    result = run()
    assert result["state"] == "merged"
    assert result["reviews"] == "1"
