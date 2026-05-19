"""Design Patterns 101 - Episode 8: Factory and di."""

from dataclasses import dataclass


class Plugin:
    """Plugin."""

    def run(self, text):
        """Run."""
        raise NotImplementedError


class UpperPlugin(Plugin):
    """Upper plugin."""

    def run(self, text):
        """Run."""
        return text.upper()


class LowerPlugin(Plugin):
    """Lower plugin."""

    def run(self, text):
        """Run."""
        return text.lower()


def plugin_factory(name):
    """Plugin factory."""
    table = {"upper": UpperPlugin, "lower": LowerPlugin}
    return table[name]()


class Container:
    """Container."""

    def __init__(self):
        self._providers = {}

    def register(self, key, provider):
        """Register."""
        self._providers[key] = provider

    def resolve(self, key):
        """Resolve."""
        return self._providers[key]()


@dataclass
class Service:
    """Service."""

    plugin: Plugin

    def process(self, text):
        """Process."""
        return self.plugin.run(text)
