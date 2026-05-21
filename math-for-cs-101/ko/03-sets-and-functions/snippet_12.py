"""Generated from book-content article."""

from typing import Callable

def compose(f: Callable, g: Callable):
    return lambda x: f(g(x))

def strip_text(x: str) -> str:
    return x.strip()

def normalize_space(x: str) -> str:
    return " ".join(x.split())

def to_lower(x: str) -> str:
    return x.lower()

pipeline = compose(to_lower, compose(normalize_space, strip_text))
print(pipeline("  Hello   CS Math  "))
