from conftest import load_module

run = load_module("ko/09-good-commit-message/step01_commit_message.py", "ep09").run


def test_ep09_commit_message_lint() -> None:
    good = run("feat: add release checklist")
    bad = run("fix.")
    assert good["ok"] is True
    assert bad["ok"] is False
