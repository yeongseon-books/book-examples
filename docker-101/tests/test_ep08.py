# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/08-database-with-app/step01_db_compose_check.py", "ep08").run


def test_ep08() -> None:
    result = run()
    assert result["success"] is True
    assert result["issues"] == []
