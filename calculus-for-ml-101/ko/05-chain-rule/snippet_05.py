"""Generated from book-content article."""

def chain(*derivs):
    p = 1.0
    for d in derivs:
        p *= d
    return p
