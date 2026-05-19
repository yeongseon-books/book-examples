import pytest
from en.ep04_sample_vs_population import run_demo


def test_ep04_sample_vs_population():
    r = run_demo()
    assert r["population_mean"] == pytest.approx(50.5)
    assert r["sample_mean"] != r["population_mean"]
    assert r["sample_var_unbiased"] > 0
