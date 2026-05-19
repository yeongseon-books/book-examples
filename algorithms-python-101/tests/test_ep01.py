from tests.conftest import load_module


def test_find_max() -> None:
    mod = load_module("ko/01-what-are-algorithms/step01_intro_algorithms.py", "ep01")
    assert mod.find_max([3, 7, 2, 9, 4]) == 9
