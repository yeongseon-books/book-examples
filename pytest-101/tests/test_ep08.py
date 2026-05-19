import pytest
from en.ep08_calculator import classify_score, discount_price


def test_ep08_discount_price():
    assert discount_price(100.0, 0.25) == 75.0


def test_ep08_discount_price_invalid_rate():
    with pytest.raises(ValueError):
        discount_price(100.0, 1.5)


def test_ep08_classify_score_boundaries():
    assert classify_score(95) == "A"
    assert classify_score(85) == "B"
    assert classify_score(75) == "C"
    assert classify_score(65) == "D"
