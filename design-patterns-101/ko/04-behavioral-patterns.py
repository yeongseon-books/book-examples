"""Design Patterns 101 - Episode 4: Behavioral patterns."""


class Handler:
    """Handler."""

    def __init__(self, nxt=None):
        self.nxt = nxt

    def handle(self, req):
        """Handle."""
        return self.nxt.handle(req) if self.nxt else "unhandled"


class AuthHandler(Handler):
    """Auth handler."""

    def handle(self, req):
        """Handle."""
        return super().handle(req) if req.get("auth") else "unauthorized"


class RouteHandler(Handler):
    """Route handler."""

    def handle(self, req):
        """Handle."""
        return f"route:{req['path']}"


class Command:
    """Command."""

    def execute(self):
        """Execute."""
        raise NotImplementedError


class AddCommand(Command):
    """Add command."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        """Execute."""
        return self.a + self.b


class Numbers:
    """Numbers."""

    def __init__(self, values):
        self.values = values

    def __iter__(self):
        """Iter."""
        yield from self.values


class Mediator:
    """Mediator."""

    def notify(self, sender, event):
        """Notify."""
        return f"{sender}:{event}"


class Memento:
    """Memento."""

    def __init__(self, state):
        self.state = state


class Originator:
    """Originator."""

    def __init__(self):
        self.state = ""

    def save(self):
        """Save."""
        return Memento(self.state)

    def restore(self, m):
        """Restore."""
        self.state = m.state


class DraftState:
    """Draft state."""

    def submit(self):
        """Submit."""
        return PublishedState()


class PublishedState:
    """Published state."""

    def submit(self):
        """Submit."""
        return self


class Article:
    """Article."""

    def __init__(self):
        self.state = DraftState()

    def submit(self):
        """Submit."""
        self.state = self.state.submit()


class Pipeline:
    """Pipeline."""

    def process(self, req):
        """Process."""
        parsed = self.parse(req)
        return parsed + self.transform(parsed)

    def parse(self, req):
        """Parse."""
        return ["parsed"]

    def transform(self, req):
        """Transform."""
        return ["transformed"]
