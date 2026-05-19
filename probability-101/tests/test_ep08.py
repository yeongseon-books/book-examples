import pytest
from ko.ep08_continuous_distributions import run


def test_ep08_continuous_distributions():
    out = run(120_000)
    assert out["normal_pdf_0"] == pytest.approx(0.39894228, rel=1e-6)
    assert out["normal_cdf_0"] == pytest.approx(0.5, rel=1e-9)
    assert out["normal_sample_mean"] == pytest.approx(0.0, abs=0.02)
    assert out["exp_sample_mean"] == pytest.approx(2.0, abs=0.03)
    assert out["uniform_sample_mean"] == pytest.approx(0.0, abs=0.02)
