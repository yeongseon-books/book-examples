import numpy as np
from conftest import load_episode


def test_ep07_eigen_equation():
    out = load_episode("07-eigenvalues-and-eigenvectors").run()
    v = out["vecs"][:, 0]
    l = out["vals"][0]
    assert np.allclose(out["a"] @ v, l * v)
    assert np.isclose(max(out["vals"]), out["lmax"], atol=1e-2)
