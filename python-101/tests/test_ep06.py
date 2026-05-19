from en.ep06_functions import combine_values


def test_combine_values() -> None:
    assert combine_values(1, 2, 3, scale=2, extra=4) == 20
