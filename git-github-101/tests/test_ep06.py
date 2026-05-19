from conftest import load_module

run = load_module("ko/06-github-repository/step01_github_repository.py", "ep06").run


def test_ep06_remote_and_upstream_model() -> None:
    result = run()
    assert result["remote"].startswith("https://")
    assert result["upstream"] == "origin/main"
