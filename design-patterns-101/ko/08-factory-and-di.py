from dataclasses import dataclass


class Plugin:
    def run(self, text):
        raise NotImplementedError


class UpperPlugin(Plugin):
    def run(self, text):
        return text.upper()


class LowerPlugin(Plugin):
    def run(self, text):
        return text.lower()


def plugin_factory(name):
    table = {"upper": UpperPlugin, "lower": LowerPlugin}
    return table[name]()


class Container:
    def __init__(self):
        self._providers = {}

    def register(self, key, provider):
        self._providers[key] = provider

    def resolve(self, key):
        return self._providers[key]()


@dataclass
class Service:
    plugin: Plugin

    def process(self, text):
        return self.plugin.run(text)
