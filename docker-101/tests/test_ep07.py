# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/07-python-app-containerize/step01_python_container_check.py", "ep07").run


def test_ep07() -> None:
    result = run()
    assert result["success"] is True
    assert result["has_healthcheck"] is True
