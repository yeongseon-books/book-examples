from __future__ import annotations

from typing import Callable, cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(Runner, load_module('ko/01-what-is-capstone/step01_capstone_definition.py', 'ko_ep01').run)
en_run = cast(Runner, load_module('en/01-what-is-capstone/step01_capstone_definition.py', 'en_ep01').run)

def test_ep01_ko_behavior() -> None:
    assert ko_run()['success'] == True

def test_ep01_en_behavior() -> None:
    assert en_run()['success'] == True
