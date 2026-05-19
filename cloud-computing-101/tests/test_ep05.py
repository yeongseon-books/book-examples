from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/05-storage/step01_storage_tiering.py", "ep05_ko")
fn = cast("Callable[..., object]", mod.storage_lifecycle_plan)


def test_ep05_behavior() -> None:
    result_obj = fn(hot_days=30)
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    transitions = cast("list[dict[str, object]]", payload["transitions"])
    assert transitions[1]["class"] == "GLACIER"
    assert result["ok"] is True
