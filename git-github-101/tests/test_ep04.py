from conftest import load_module

run = load_module("ko/04-branch-basics/step01_branch_basics.py", "ep04").run


def test_ep04_branch_diverges() -> None:
    graph = run()["graph"]
    assert "feature/docs" in graph
    assert "main" in graph
