from en import ep04_authorization


def test_ep04_authz():
    result = ep04_authorization.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
