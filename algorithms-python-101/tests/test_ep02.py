from tests.conftest import load_module


def test_linear_and_binary_search() -> None:
    mod = load_module(
        "ko/02-time-complexity-and-big-o/step01_complexity_basics.py", "ep02"
    )
    data = list(range(0, 20, 2))
    assert mod.linear_search(data, 10) == 5
    assert mod.binary_search(data, 10) == 5
