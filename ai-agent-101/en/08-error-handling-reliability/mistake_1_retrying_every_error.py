# Bad
for _ in range(5):
    try:
        return call_api(invalid_args)  # Bad args won't succeed on retry
    except Exception:
        time.sleep(1)

# Good
try:
    return call_api(args)
except (Timeout, ConnectionError):
    return retry_with_backoff(lambda: call_api(args))
except ValueError:
    raise  # Not retryable
