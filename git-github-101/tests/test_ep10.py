from conftest import load_module

run = load_module("ko/10-real-world-workflow/step01_real_world_workflow.py", "ep10").run


def test_ep10_workflow_and_tag() -> None:
    result = run()
    assert result["pr_state"] == "merged"
    assert result["issue_state"] == "closed"
    assert result["tag"].startswith("c")
