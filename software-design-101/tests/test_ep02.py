from ko.ep02_separation_of_concerns import compute_total, parse_quantity


def test_ep02_good_functions_are_testable() -> None:
    assert parse_quantity("3") == 3
    assert compute_total(3, 120) == 360
