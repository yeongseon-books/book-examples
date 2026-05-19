from __future__ import annotations

from typing import Callable, cast
from conftest import load_module

mod = load_module('ko/04-compute/step01_auto_scaling.py', 'ep04_ko')
fn = cast(Callable[..., object], getattr(mod, 'compute_scale_plan'))


def test_ep04_behavior() -> None:
    result_obj = fn(baseline_rps=250, peak_rps=900)
    result = cast(dict[str, object], result_obj)
    payload = cast(dict[str, object], result['payload'])
    assert cast(int, payload['max_instances']) >= cast(int, payload['min_instances'])
    assert result['ok'] is True
