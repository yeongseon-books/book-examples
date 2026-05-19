from en.ep05_estimation_bias import run_demo


def test_ep05_bias_small():
    r = run_demo()
    assert abs(r["estimated_bias"]) < 0.1
