from en import ep03_authentication


def test_ep03_auth():
    result = ep03_authentication.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
