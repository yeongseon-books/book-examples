import pytest
from en.ep08_correlation_regression import run_demo


def test_ep08_regression_signal():
    r = run_demo()
    assert r["pearson_r"] > 0.9
    assert r["beta1"] == pytest.approx(2.2, abs=0.2)
