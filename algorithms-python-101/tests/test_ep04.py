from tests.conftest import load_module


def test_merge_sort() -> None:
    mod = load_module("ko/04-sorting-algorithms/step01_sorting.py", "ep04")
    assert mod.merge_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
