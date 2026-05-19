import numpy as np
from conftest import load_episode


def test_ep06_rank_and_basis():
    out = load_episode('06-basis-and-dimension').run()
    assert out['rank'] == 2
    b = out['basis']
    assert np.allclose(b @ b.T, np.eye(b.shape[0]), atol=1e-10)
