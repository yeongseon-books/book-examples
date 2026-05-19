import pytest

from ko.ep06_expectation_variance import run


def test_ep06_expect_var():
    out = run(250_000)
    assert out["mean_sim"] == pytest.approx(out["mean_exact"], abs=0.02)
    assert out["var_sim"] == pytest.approx(out["var_exact"], abs=0.03)
