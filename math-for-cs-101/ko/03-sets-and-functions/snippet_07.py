"""Generated from book-content article."""

def trim(s: str) -> str:
    return s.strip()

def lower(s: str) -> str:
    return s.lower()

def remove_space(s: str) -> str:
    return s.replace(' ', '')

def compose(*funcs):
    def wrapped(x):
        for f in funcs:
            x = f(x)
        return x
    return wrapped

normalize = compose(trim, lower, remove_space)
