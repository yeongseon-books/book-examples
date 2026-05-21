# Bad
while True:
    try:
        return call_api()
    except Exception:
        time.sleep(1)  # forever

# Good
return retry_with_backoff(call_api, max_attempts=5)
