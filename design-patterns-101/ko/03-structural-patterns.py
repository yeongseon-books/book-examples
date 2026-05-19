"""Design Patterns 101 - Episode 3: Structural patterns."""


class LegacyWriter:
    """Legacy writer."""

    def write_line(self, text):
        """Write line."""
        return f"legacy:{text}"


class JsonLogger:
    """Json logger."""

    def log(self, text):
        """Log."""
        return {"message": text}


class WriterAdapter:
    """Writer adapter."""

    def __init__(self, legacy):
        self.legacy = legacy

    def log(self, text):
        """Log."""
        return {"message": self.legacy.write_line(text).split(":", 1)[1]}


class Renderer:
    """Renderer."""

    def render(self, text):
        """Render."""
        raise NotImplementedError


class PlainRenderer(Renderer):
    """Plain renderer."""

    def render(self, text):
        """Render."""
        return text


class HtmlBridge(Renderer):
    """Html bridge."""

    def __init__(self, impl):
        self.impl = impl

    def render(self, text):
        """Render."""
        return f"<{self.impl}>{text}</{self.impl}>"


class Node:
    """Node."""

    def size(self):
        """Size."""
        raise NotImplementedError


class File(Node):
    """File."""

    def __init__(self, n):
        self.n = n

    def size(self):
        """Size."""
        return self.n


class Folder(Node):
    """Folder."""

    def __init__(self, children):
        self.children = children

    def size(self):
        """Size."""
        return sum(c.size() for c in self.children)


class Notifier:
    """Notifier."""

    def send(self, msg):
        """Send."""
        return [msg]


class TimestampDecorator(Notifier):
    """Timestamp decorator."""

    def __init__(self, inner):
        self.inner = inner

    def send(self, msg):
        """Send."""
        return self.inner.send(f"ts:{msg}")


class CheckoutFacade:
    """Checkout facade."""

    def buy(self, user, item):
        """Buy."""
        return f"{user}:{item}:ok"


class DataSource:
    """Data source."""

    def __init__(self):
        self.calls = 0

    def get(self, key):
        """Get."""
        self.calls += 1
        return f"v:{key}"


class CacheProxy:
    """Cache proxy."""

    def __init__(self, real):
        self.real = real
        self.cache = {}

    def get(self, key):
        """Get."""
        if key not in self.cache:
            self.cache[key] = self.real.get(key)
        return self.cache[key]
