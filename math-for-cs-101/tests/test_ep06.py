from tests.conftest import load_module


def test_ep06_monte_carlo_pi_tolerance():
    m=load_module('ko/06-probability/step01_probability.py')
    est=m.estimate_pi(n=100000,seed=7)
    assert abs(est-3.14159)<0.02
    assert round(m.bayes(0.99,0.01,0.02),3)==0.495
