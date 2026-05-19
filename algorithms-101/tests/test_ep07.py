from conftest import load_module

ko = load_module("ko/07-greedy-algorithms/step01_activity_selection.py", "ko_ep07")


def test_ep07_activity_selection() -> None:
    assert ko.run()["max_non_overlapping"] == 3
