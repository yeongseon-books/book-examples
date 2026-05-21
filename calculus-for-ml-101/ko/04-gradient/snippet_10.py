"""Generated from book-content article."""

def sanity_cases(fn, cases):
    out=[]
    for c in cases:
        out.append(fn(*c) if isinstance(c, tuple) else fn(c))
    return out
