from tests.conftest import load_module


def test_bisect_search() -> None:
    mod = load_module("ko/03-linear-and-binary-search/step01_search.py", "ep03")
    assert mod.bisect_search([1, 3, 5, 7, 9], 7) == 3
    assert mod.bisect_search([1, 3, 5, 7, 9], 8) == -1
