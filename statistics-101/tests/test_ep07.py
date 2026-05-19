from en.ep07_hypothesis_testing import run_demo


def test_ep07_tests_run():
    r = run_demo()
    assert 0 <= r["one_sample_p"] <= 1
    assert 0 <= r["two_sample_p"] <= 1
    assert 0 <= r["chi2_p"] <= 1
