# Bad
try:
    result = risky_operation()
except Exception:
    pass  # Hidden — undebuggable

# Good
try:
    result = risky_operation()
except Exception as e:
    logger.error(f"risky_operation failed: {e}", exc_info=True)
    metrics.increment("risky_operation.failures")
    raise
