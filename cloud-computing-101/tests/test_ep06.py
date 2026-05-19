from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/06-network/step01_network_policy.py", "ep06_ko")
fn = cast("Callable[..., object]", mod.build_network_policy)


def test_ep06_behavior() -> None:
    result_obj = fn()
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    assert payload["db_ingress_from"] == "app-sg"
    assert result["ok"] is True
