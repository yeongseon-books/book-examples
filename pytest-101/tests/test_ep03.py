import pytest

from en.ep03_risky import divide_positive


def test_ep03_raises_value_error_on_zero_denominator():
    with pytest.raises(ValueError, match="denominator"):
        divide_positive(10, 0)


def test_ep03_warns_on_negative_input():
    with pytest.warns(UserWarning, match="negative"):
        assert divide_positive(-6, 2) == -3
