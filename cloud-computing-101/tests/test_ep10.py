"""Tests for ep10 in Cloud Computing 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module(
    "ko/10-cloud-architecture-basics/step01_architecture_review.py", "ep10_ko"
)
fn = cast("Callable[..., object]", mod.well_architected_review)


def test_ep10_behavior() -> None:
    """Test ep10 behavior."""
    result_obj = fn(
        scores={
            "operational_excellence": 80,
            "security": 85,
            "reliability": 90,
            "performance_efficiency": 75,
            "cost_optimization": 70,
        }
    )
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    assert payload["grade"] == "pass"
    assert result["ok"] is True
