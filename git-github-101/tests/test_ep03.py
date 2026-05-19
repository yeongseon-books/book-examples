from conftest import load_module

run = load_module("ko/03-status-diff-log/step01_status_diff_log.py", "ep03").run


def test_ep03_status_diff_log() -> None:
    result = run()
    assert result["status"].startswith("M")
    assert "+world" in result["diff"]
    assert "feat: add notes" in result["log"]
