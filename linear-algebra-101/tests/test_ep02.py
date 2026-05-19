import numpy as np
from conftest import load_episode


def test_ep02_vector_ops():
    out = load_episode("02-vectors").run()
    assert out["dot"] == -5.0
    assert np.allclose(out["unit"], np.array([0.6, 0.8]))
