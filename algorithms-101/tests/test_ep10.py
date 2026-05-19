from collections.abc import Callable
from typing import cast

from conftest import load_module

ko = load_module(
    "ko/10-problem-solving-strategies/step01_problem_solving_playbook.py", "ko_ep10"
)
en = load_module(
    "en/10-problem-solving-strategies/step01_problem_solving_playbook.py", "en_ep10"
)

ko_max_subarray = cast("Callable[[list[int]], int]", ko.max_subarray)
en_max_subarray = cast("Callable[[list[int]], int]", en.max_subarray)


def test_ep10_kadane() -> None:
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert ko_max_subarray(sample) == 6
    assert en_max_subarray(sample) == 6
