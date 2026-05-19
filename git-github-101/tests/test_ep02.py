"""Tests for ep02 in Git Github 101."""

from conftest import load_module

run = load_module("ko/02-first-commit/step01_first_commit.py", "ep02").run


def test_ep02_first_commit_created() -> None:
    """Test ep02 first commit created."""
    assert len(run()["head"]) >= 6
