"""Design Patterns 101 - Episode 9: Avoiding pattern overuse."""


class AbstractGreeterFactory:
    """Abstract greeter factory."""

    def create_greeter(self):
        """Create greeter."""
        return FormalGreeter()


class FormalGreeter:
    """Formal greeter."""

    def greet(self, name):
        """Greet."""
        return f"Hello, {name}"


def over_engineered(name):
    """Over engineered."""
    return AbstractGreeterFactory().create_greeter().greet(name)


def simple(name):
    """Simple."""
    return f"Hello, {name}"
