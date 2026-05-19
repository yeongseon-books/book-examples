from en.ep10_statistical_thinking_ab_test import run_demo


def test_ep10_ab_flow():
    r = run_demo()
    assert r["recommended_n_per_group"] > 1000
    assert -0.05 < r["lift"] < 0.1
    assert 0 <= r["p_value"] <= 1
