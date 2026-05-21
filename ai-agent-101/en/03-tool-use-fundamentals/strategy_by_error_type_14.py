# Authentication errors, invalid parameters, permission denied
PERMANENT_ERRORS = [
    PermissionError,
    ValueError,
    KeyError,
]

def is_permanent(error: Exception) -> bool:
    """Determine if error is not retryable."""
    return any(isinstance(error, err_type) for err_type in PERMANENT_ERRORS)
