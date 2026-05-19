# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/01-what-is-docker/step01_manual_loop.py", "ep01").run


def test_ep01() -> None:
    result = run()
    assert result["success"] is True
    assert "image" in result["report"]["keywords"]
