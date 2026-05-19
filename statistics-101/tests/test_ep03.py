import pytest
from en.ep03_distributions_data import run_demo


def test_ep03_distribution_arrays():
    r = run_demo()
    assert r["x_normal"].shape[0] == 121
    assert r["normal_pdf"].max() == pytest.approx(0.3989, rel=1e-2)
    assert r["binom_pmf"].sum() == pytest.approx(1.0, rel=1e-6)
    assert r["poisson_pmf"].sum() == pytest.approx(1.0, rel=2e-2)
