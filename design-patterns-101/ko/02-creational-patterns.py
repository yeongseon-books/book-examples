"""Design Patterns 101 - Episode 2: Creational patterns."""

import copy
from dataclasses import dataclass


class ModuleSingleton:
    """Module singleton."""

    pass


MODULE_SINGLETON = ModuleSingleton()


def singleton_decorator(cls):
    """Singleton decorator."""
    cache = {}

    def get(*a, **k):
        """Get."""
        if cls not in cache:
            cache[cls] = cls(*a, **k)
        return cache[cls]

    return get


@singleton_decorator
class DecoratedSingleton:
    """Decorated singleton."""

    pass


@dataclass
class PdfReport:
    """Pdf report."""

    kind: str = "pdf"


@dataclass
class HtmlReport:
    """Html report."""

    kind: str = "html"


class ReportFactory:
    """Report factory."""

    def create(self, kind: str):
        """Create."""
        return PdfReport() if kind == "pdf" else HtmlReport()


class Button:
    """Button."""

    pass


class TextBox:
    """Text box."""

    pass


class MacButton(Button):
    """Mac button."""

    pass


class MacTextBox(TextBox):
    """Mac text box."""

    pass


class WinButton(Button):
    """Win button."""

    pass


class WinTextBox(TextBox):
    """Win text box."""

    pass


class MacFactory:
    """Mac factory."""

    def button(self):
        """Button."""
        return MacButton()

    def textbox(self):
        """Textbox."""
        return MacTextBox()


class WinFactory:
    """Win factory."""

    def button(self):
        """Button."""
        return WinButton()

    def textbox(self):
        """Textbox."""
        return WinTextBox()


@dataclass
class Report:
    """Report."""

    title: str
    body: str
    footer: str


class ReportBuilder:
    """Report builder."""

    def __init__(self):
        self._title = ""
        self._body = ""
        self._footer = ""

    def title(self, v):
        """Title."""
        self._title = v
        return self

    def body(self, v):
        """Body."""
        self._body = v
        return self

    def footer(self, v):
        """Footer."""
        self._footer = v
        return self

    def build(self):
        """Build."""
        return Report(self._title, self._body, self._footer)


@dataclass
class Template:
    """Template."""

    fields: dict[str, list[int]]

    def clone(self):
        """Clone."""
        return copy.deepcopy(self)
