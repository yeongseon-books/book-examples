from en import ep02_input_validation


def test_ep02_validation():
    result = ep02_input_validation.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
