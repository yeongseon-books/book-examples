"""Tests for ep04 in Cloud Computing 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/04-compute/step01_auto_scaling.py", "ep04_ko")
fn = cast("Callable[..., object]", mod.compute_scale_plan)


def test_ep04_behavior() -> None:
    """Test ep04 behavior."""
    result_obj = fn(baseline_rps=250, peak_rps=900)
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    assert cast("int", payload["max_instances"]) >= cast(
        "int", payload["min_instances"]
    )
    assert result["ok"] is True
