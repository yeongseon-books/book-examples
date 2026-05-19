from __future__ import annotations

from typing import Callable, cast
from conftest import load_module

mod = load_module('ko/09-cost-management/step01_cost_guardrail.py', 'ep09_ko')
fn = cast(Callable[..., object], getattr(mod, 'cost_guardrail_plan'))


def test_ep09_behavior() -> None:
    result_obj = fn(monthly_budget_usd=500)
    result = cast(dict[str, object], result_obj)
    payload = cast(dict[str, object], result['payload'])
    assert payload['alert_threshold_percent'] == 80
    assert result['ok'] is True
