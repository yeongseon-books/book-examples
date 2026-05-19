from conftest import load_module

run = load_module("ko/01-what-is-git/step01_what_is_git.py", "ep01").run


def test_ep01_git_available() -> None:
    result = run()
    assert result["version"].startswith("git version")
    assert result["default_branch"] == "main"
