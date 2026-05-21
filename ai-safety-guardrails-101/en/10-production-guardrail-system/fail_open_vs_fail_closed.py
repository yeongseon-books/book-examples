"""Generated from book-content article."""

def safe_call(check_fn, request, on_error="closed"):
    try:
        return check_fn(request)
    except Exception as e:
        log_guardrail_error(check_fn.__name__, e)
        if on_error == "open":
            return GuardrailResult(allowed=True, stage=check_fn.__name__, reason="degraded")
        return GuardrailResult(allowed=False, stage=check_fn.__name__, reason="error")
