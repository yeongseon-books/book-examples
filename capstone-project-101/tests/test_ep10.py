from __future__ import annotations

from typing import Callable, cast

from conftest import load_module

Runner = Callable[[], dict[str, object]]
ko_run = cast(Runner, load_module('ko/10-project-retrospective/step01_retro_kpt.py', 'ko_ep10').run)
en_run = cast(Runner, load_module('en/10-project-retrospective/step01_retro_kpt.py', 'en_ep10').run)

def test_ep10_ko_behavior() -> None:
    assert ko_run()['actionable'] == True

def test_ep10_en_behavior() -> None:
    assert en_run()['actionable'] == True
