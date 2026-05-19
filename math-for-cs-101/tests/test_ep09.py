from common import entropy, kl_divergence

from tests.conftest import load_module


def test_ep09_entropy_and_kl():
    assert abs(entropy([0.5, 0.5]) - 1.0) < 1e-9
    assert kl_divergence([0.5, 0.5], [0.75, 0.25]) > 0
    m = load_module("ko/09-information-theory/step01_information_theory.py")
    _, _, lengths = m.sample_metrics()
    assert min(lengths.values()) >= 1
