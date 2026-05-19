from conftest import load_module

ko = load_module("ko/06-dynamic-programming/step01_knapsack_dp.py", "ko_ep06")


def test_ep06_knapsack() -> None:
    assert ko.knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
