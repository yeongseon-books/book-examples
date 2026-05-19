from __future__ import annotations

from typing import Callable, cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(Runner, load_module('ko/08-schedule-management/step01_schedule_plan.py', 'ko_ep08').run)
en_run = cast(Runner, load_module('en/08-schedule-management/step01_schedule_plan.py', 'en_ep08').run)

def test_ep08_ko_behavior() -> None:
    assert ko_run()['progress'] == {'done': 12, 'todo': 8, 'blocked': 2}

def test_ep08_en_behavior() -> None:
    assert en_run()['progress'] == {'done': 12, 'todo': 8, 'blocked': 2}

def test_ep08_buffer_enabled() -> None:
    plan = ko_run()['plan']
    assert getattr(plan, 'has_buffer')() is True
