from en import ep10_safe_logging


def test_ep10_safe_logging():
    result = ep10_safe_logging.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
