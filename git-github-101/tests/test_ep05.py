"""Tests for ep05 in Git Github 101."""

from conftest import load_module

run = load_module("ko/05-merge-and-conflict/step01_merge_conflict.py", "ep05").run


def test_ep05_conflict_markers() -> None:
    """Test ep05 conflict markers."""
    conflict = run()["conflict"]
    assert "<<<<<<<" in conflict
    assert "=======" in conflict
    assert ">>>>>>>" in conflict
