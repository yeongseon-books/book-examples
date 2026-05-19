from __future__ import annotations

from conftest import load_module


def test_scaling_strategy() -> None:
    mod = load_module("ko/07-scaling-101/step01_scaling_strategy.py", "ep07")
    assert mod.choose_scaling(40, 85, False) == "scale_up"
    assert mod.choose_scaling(75, 45, True) == "scale_out"
    assert mod.choose_scaling(75, 85, True) == "scale_up_then_out"
    assert mod.projected_db_connections(6, 20) == 120
