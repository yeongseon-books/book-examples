from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module(
    "ko/03-region-and-availability-zone/step01_region_placement.py", "ep03_ko"
)
fn = cast("Callable[..., object]", mod.choose_region_placement)


def test_ep03_behavior() -> None:
    result_obj = fn(users="global", disaster_recovery=True)
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    regions = cast("list[str]", payload["regions"])
    assert len(regions) == 2
    assert result["ok"] is True
