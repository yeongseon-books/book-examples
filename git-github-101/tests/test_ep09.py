"""Tests for ep09 in Git Github 101."""

from conftest import load_module

run = load_module("ko/09-good-commit-message/step01_commit_message.py", "ep09").run


def test_ep09_commit_message_lint() -> None:
    """Test ep09 commit message lint."""
    good = run("feat: add release checklist")
    bad = run("fix.")
    assert good["ok"] is True
    assert bad["ok"] is False
