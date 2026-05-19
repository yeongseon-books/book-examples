from __future__ import annotations

from typing import Callable, cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(Runner, load_module('ko/06-designing-the-mvp/step01_mvp_scope.py', 'ko_ep06').run)
en_run = cast(Runner, load_module('en/06-designing-the-mvp/step01_mvp_scope.py', 'en_ep06').run)

def test_ep06_ko_behavior() -> None:
    assert ko_run()['success'] == {'happy_path': '<= 60s', 'errors': 0}

def test_ep06_en_behavior() -> None:
    assert en_run()['success'] == {'happy_path': '<= 60s', 'errors': 0}
