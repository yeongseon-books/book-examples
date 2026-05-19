from en import ep08_xss_csrf


def test_ep08_xss_csrf():
    result = ep08_xss_csrf.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
