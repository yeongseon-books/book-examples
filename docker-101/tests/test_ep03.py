# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/03-dockerfile/step01_dockerfile_lint.py", "ep03").run


def test_ep03() -> None:
    result = run()
    assert result["success"] is True
    assert result["issues"] == []
