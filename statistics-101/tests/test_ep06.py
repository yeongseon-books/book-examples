import pytest
from en.ep06_confidence_interval import run_demo


def test_ep06_ci_coverage():
    r = run_demo()
    assert r["z_ci_low"] < r["z_ci_high"]
    assert r["t_ci_low"] < r["t_ci_high"]
    assert r["coverage"] == pytest.approx(0.95, abs=0.03)
