from __future__ import annotations

from typing import Callable, cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(Runner, load_module('ko/05-splitting-team-roles/step01_role_split.py', 'ko_ep05').run)
en_run = cast(Runner, load_module('en/05-splitting-team-roles/step01_role_split.py', 'en_ep05').run)

def test_ep05_ko_behavior() -> None:
    assert ko_run()['review'] == 'weekly'

def test_ep05_en_behavior() -> None:
    assert en_run()['review'] == 'weekly'
