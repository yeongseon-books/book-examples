from __future__ import annotations

from conftest import load_module


def test_hosting_decision() -> None:
    mod = load_module("ko/03-hosting-models/step01_hosting_decision.py", "ep03")
    assert (
        mod.choose_hosting_model(needs_windows_dependency=False, needs_os_control=False)
        == "linux-code"
    )
    assert (
        mod.choose_hosting_model(needs_windows_dependency=True, needs_os_control=False)
        == "windows-code"
    )
    assert mod.estimate_plan_strategy(3, False) == "shared-plan"
