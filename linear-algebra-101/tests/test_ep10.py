import numpy as np
from conftest import load_episode


def test_ep10_ml_fits():
    out = load_episode("10-linear-algebra-in-ml").run()
    assert np.allclose(out["w_true"], out["w_hat"], atol=0.1)
    assert out["acc"] > 0.95
