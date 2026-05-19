# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/10-production-docker/step01_production_policy_check.py", "ep10").run


def test_ep10() -> None:
    result = run()
    assert result["success"] is True
    assert result["missing_flags"] == []
