from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/01-what-is-cloud-computing/step01_service_models.py", "ep01_ko")
fn = cast("Callable[..., object]", mod.classify_service_model)


def test_ep01_behavior() -> None:
    result_obj = fn(workload="api", manages_os=True, manages_runtime=True)
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    assert payload["model"] == "IaaS"
    assert result["ok"] is True
