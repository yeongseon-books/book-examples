from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/07-identity-and-security/step01_iam_policy.py", "ep07_ko")
fn = cast("Callable[..., object]", mod.build_iam_policy)


def test_ep07_behavior() -> None:
    result_obj = fn(bucket="team-prod")
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    statements = cast("list[dict[str, object]]", payload["statements"])
    resources = cast("list[str]", statements[0]["Resource"])
    assert "team-prod" in resources[0]
    assert result["ok"] is True
