from conftest import load_module

run = load_module("ko/08-issue-and-project/step01_issue_project.py", "ep08").run


def test_ep08_issue_closed_after_merge() -> None:
    result = run()
    assert result["issue_state"] == "closed"
    assert result["assignee"] == "alice"
