from __future__ import annotations

from collections.abc import Callable
from typing import cast

from conftest import load_module

mod = load_module("ko/08-monitoring/step01_monitoring_alarm.py", "ep08_ko")
fn = cast("Callable[..., object]", mod.create_alarm_plan)


def test_ep08_behavior() -> None:
    result_obj = fn(threshold=80.0, periods=5)
    result = cast("dict[str, object]", result_obj)
    payload = cast("dict[str, object]", result["payload"])
    assert payload["evaluation_periods"] == 5
    assert result["ok"] is True
