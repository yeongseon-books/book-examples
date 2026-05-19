import copy
from dataclasses import dataclass


class ModuleSingleton:
    pass


MODULE_SINGLETON = ModuleSingleton()


def singleton_decorator(cls):
    cache = {}

    def get(*a, **k):
        if cls not in cache:
            cache[cls] = cls(*a, **k)
        return cache[cls]

    return get


@singleton_decorator
class DecoratedSingleton:
    pass


@dataclass
class PdfReport:
    kind: str = "pdf"


@dataclass
class HtmlReport:
    kind: str = "html"


class ReportFactory:
    def create(self, kind: str):
        return PdfReport() if kind == "pdf" else HtmlReport()


class Button:
    pass


class TextBox:
    pass


class MacButton(Button):
    pass


class MacTextBox(TextBox):
    pass


class WinButton(Button):
    pass


class WinTextBox(TextBox):
    pass


class MacFactory:
    def button(self):
        return MacButton()

    def textbox(self):
        return MacTextBox()


class WinFactory:
    def button(self):
        return WinButton()

    def textbox(self):
        return WinTextBox()


@dataclass
class Report:
    title: str
    body: str
    footer: str


class ReportBuilder:
    def __init__(self):
        self._title = ""
        self._body = ""
        self._footer = ""

    def title(self, v):
        self._title = v
        return self

    def body(self, v):
        self._body = v
        return self

    def footer(self, v):
        self._footer = v
        return self

    def build(self):
        return Report(self._title, self._body, self._footer)


@dataclass
class Template:
    fields: dict[str, list[int]]

    def clone(self):
        return copy.deepcopy(self)
