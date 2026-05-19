from conftest import load_episode


def test_ep09_pca_variance():
    out = load_episode("09-pca").run()
    assert out["ratio"][0] > 0.95
    assert out["z"].shape[1] == 1
