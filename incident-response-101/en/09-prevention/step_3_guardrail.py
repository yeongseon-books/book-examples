"""Generated from book-content article."""

def guard(payload, limit=1000):
    if payload > limit:
        raise ValueError("blocked")
