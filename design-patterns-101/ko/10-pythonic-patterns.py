"""Design Patterns 101 - Episode 10: Pythonic patterns."""

from contextlib import contextmanager
from dataclasses import dataclass


class FileLike:
    """File like."""

    def __init__(self):
        self.opened = False

    def open(self):
        """Open."""
        self.opened = True

    def close(self):
        """Close."""
        self.opened = False


@contextmanager
def managed_file(res):
    """Managed file."""
    res.open()
    try:
        yield res
    finally:
        res.close()


def classic_collect(values):
    out = []
    i = 0
    while i < len(values):
        out.append(values[i])
        i += 1
    return out


def pythonic_collect(values):
    return [x for x in values]


def classic_iterator(values):
    """Classic iterator."""
    return classic_collect(values)


def pythonic_iterator(values):
    """Pythonic iterator."""
    return pythonic_collect(values)


def strategy_class(kind, value):
    """Strategy class."""

    class AddOne:
        """Add one."""

        def apply(self, v):
            """Apply."""
            return v + 1

    class Double:
        """Double."""

        def apply(self, v):
            """Apply."""
            return v * 2

    if kind == "add":
        strategy = AddOne()
    elif kind == "double":
        strategy = Double()
    else:
        raise ValueError(f"unknown strategy kind: {kind}")
    return strategy.apply(value)


def strategy_function(kind, value):
    """Strategy function."""
    strategy = {"add": lambda v: v + 1, "double": lambda v: v * 2}[kind]
    return strategy(value)


@dataclass
class User:
    """User."""

    name: str
    age: int
