# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/05-docker-compose/step01_compose_validate.py", "ep05").run


def test_ep05() -> None:
    result = run()
    assert result["success"] is True
    assert result["issues"] == []
