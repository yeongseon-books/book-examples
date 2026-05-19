import pytest
from ko.ep05_random_variable import run


def test_ep05_random_variable():
    out = run(250_000)
    assert out["pmf_sum"] == pytest.approx(1.0)
    assert out["empirical_mean"] == pytest.approx(out["exact_mean"], abs=0.02)
