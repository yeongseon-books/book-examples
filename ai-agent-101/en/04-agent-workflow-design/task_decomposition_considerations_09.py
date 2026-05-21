"""Generated from book-content article."""

def verify_step(step: str, result: Any) -> bool:
    """Verify step completion"""
    if step == "Collect data":
        return isinstance(result, list) and len(result) > 0
    elif step == "Clean data":
        return all("clean" in item for item in result)
    # ...
