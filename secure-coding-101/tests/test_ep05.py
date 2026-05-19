from en import ep05_safe_storage


def test_ep05_storage():
    result = ep05_safe_storage.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
