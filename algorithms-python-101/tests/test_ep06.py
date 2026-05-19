from tests.conftest import load_module


def test_climb_stairs() -> None:
    mod = load_module("ko/06-dynamic-programming-basics/step01_dp.py", "ep06")
    assert mod.climb_stairs(7) == 21
