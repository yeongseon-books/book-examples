import numpy as np
from conftest import load_episode


def test_ep05_transform_shape():
    out = load_episode('05-linear-transformation').run()
    assert out['transformed'].shape == out['points'].shape
    det = np.linalg.det(out['rotation'])
    assert np.isclose(det, 1.0, atol=1e-12)
