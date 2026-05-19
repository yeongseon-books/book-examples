import pytest

from ko.ep04_bayes_theorem import run


def test_ep04_bayes():
    out = run(350_000)
    assert out["sim"] == pytest.approx(out["posterior"], abs=0.01)
