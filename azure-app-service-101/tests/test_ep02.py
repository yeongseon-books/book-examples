from __future__ import annotations

from conftest import load_module


def test_request_lifecycle_diagnosis() -> None:
    mod = load_module("ko/02-request-lifecycle/step01_request_lifecycle.py", "ep02")
    assert mod.build_hops() == ["client", "dns", "frontend", "worker", "app"]
    assert mod.diagnose_status(502, False) == "frontend_to_worker"
    assert mod.diagnose_status(504, True) == "timeout_or_dependency"
