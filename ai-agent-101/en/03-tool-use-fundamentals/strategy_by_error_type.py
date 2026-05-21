# Network timeouts, temporary service outages
RETRYABLE_ERRORS = [
    ConnectionError,
    TimeoutError,
    requests.exceptions.Timeout,
]

def is_retryable(error: Exception) -> bool:
    """Determine if error is retryable."""
    return any(isinstance(error, err_type) for err_type in RETRYABLE_ERRORS)
