from __future__ import annotations

from typing import Callable, cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(Runner, load_module('ko/04-organizing-requirements/step01_requirement_table.py', 'ko_ep04').run)
en_run = cast(Runner, load_module('en/04-organizing-requirements/step01_requirement_table.py', 'en_ep04').run)

def test_ep04_ko_behavior() -> None:
    assert ko_run()['prio'] == {'core': 'Must', 'share': 'Should', 'ai': 'Could'}

def test_ep04_en_behavior() -> None:
    assert en_run()['prio'] == {'core': 'Must', 'share': 'Should', 'ai': 'Could'}
