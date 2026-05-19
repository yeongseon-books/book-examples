from en.ep02_variables_types import calculate_basics


def test_calculate_basics() -> None:
    result = calculate_basics(8, 2)
    assert result["sum"] == 10
    assert result["quotient"] == 4
