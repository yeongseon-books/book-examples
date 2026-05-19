"""Tests for ep02 in Cloud Computing 101."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/02-iaas-paas-saas/step01_shared_responsibility.py", "ep02_ko")
fn = cast("Callable[..., object]", mod.shared_responsibility)


def test_ep02_behavior() -> None:
    """Test ep02 behavior."""
    result_obj = fn(model="PaaS")
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    assert payload["customer_scope"] == ["app"]
    assert result["ok"] is True
