from __future__ import annotations

from dataclasses import dataclass, field
from html.parser import HTMLParser
import json
import re
from typing import Callable


class _TagCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append({"tag": tag, "attrs": dict(attrs)})


class HTMLAnalyzer:
    def __init__(self, html: str) -> None:
        collector = _TagCollector()
        collector.feed(html)
        self.tags = collector.tags

    def has_semantic_tags(self, required: set[str]) -> bool:
        seen = {item["tag"] for item in self.tags}
        return required.issubset(seen)

    def missing_alt_images(self) -> int:
        count = 0
        for item in self.tags:
            if item["tag"] == "img":
                attrs = item["attrs"]
                alt = attrs.get("alt")
                if alt is None or alt.strip() == "":
                    count += 1
        return count

    def aria_issues(self) -> int:
        issues = 0
        for item in self.tags:
            if item["tag"] in {"input", "button", "select", "textarea"}:
                attrs = item["attrs"]
                has_name = "aria-label" in attrs or "id" in attrs
                if not has_name:
                    issues += 1
        return issues


class CSSAnalyzer:
    RULE_RE = re.compile(r"([^{}]+)\{([^{}]+)\}")

    def __init__(self, css: str) -> None:
        self.css = css
        self.rules = self.RULE_RE.findall(css)

    def selector_specificity(self, selector: str) -> tuple[int, int, int]:
        a = selector.count("#")
        b = selector.count(".") + selector.count("[")
        c = sum(1 for tok in re.split(r"\s+|>|\+|~", selector) if tok and tok[0].isalpha())
        return a, b, c

    def unused_selectors(self, html: str) -> list[str]:
        analyzer = HTMLAnalyzer(html)
        classes = set()
        ids = set()
        tags = set()
        for item in analyzer.tags:
            attrs = item["attrs"]
            tags.add(str(item["tag"]))
            if "class" in attrs and attrs["class"]:
                classes.update(str(attrs["class"]).split())
            if "id" in attrs and attrs["id"]:
                ids.add(str(attrs["id"]))
        unused: list[str] = []
        for raw_sel, _ in self.rules:
            selector = raw_sel.strip().split(",")[0].strip()
            if selector.startswith(".") and selector[1:] not in classes:
                unused.append(selector)
            elif selector.startswith("#") and selector[1:] not in ids:
                unused.append(selector)
            elif selector and selector[0].isalpha() and selector not in tags:
                unused.append(selector)
        return unused

    def enforce_tokens(self, token_prefix: str = "--color-") -> list[str]:
        violations = []
        for _, body in self.rules:
            for line in body.split(";"):
                if "color" in line and "var(" not in line and "#" in line:
                    violations.append(line.strip())
        if token_prefix not in self.css:
            violations.append("missing token declaration")
        return [v for v in violations if v]


class JSAnalyzer:
    def __init__(self, js: str) -> None:
        self.js = js

    def declaration_counts(self) -> dict[str, int]:
        return {
            "var": len(re.findall(r"\bvar\b", self.js)),
            "let": len(re.findall(r"\blet\b", self.js)),
            "const": len(re.findall(r"\bconst\b", self.js)),
        }

    def async_patterns(self) -> dict[str, int]:
        return {
            "async": len(re.findall(r"\basync\b", self.js)),
            "await": len(re.findall(r"\bawait\b", self.js)),
            "fetch": len(re.findall(r"\bfetch\b", self.js)),
        }

    def component_names(self) -> list[str]:
        names = re.findall(r"function\s+([A-Z][A-Za-z0-9_]*)", self.js)
        return names


@dataclass
class ComponentSim:
    props: dict[str, object]
    state: dict[str, object]
    renderer: Callable[[dict[str, object], dict[str, object]], str]

    def set_state(self, updates: dict[str, object]) -> None:
        self.state.update(updates)

    def render(self) -> str:
        return self.renderer(self.props, self.state)


@dataclass
class RouterSim:
    routes: dict[str, Callable[[dict[str, str]], str]]
    history: list[str] = field(default_factory=list)

    def navigate(self, path: str) -> str:
        self.history.append(path)
        for pattern, handler in self.routes.items():
            if ":" not in pattern and pattern == path:
                return handler({})
            if ":" in pattern:
                pp = pattern.strip("/").split("/")
                cp = path.strip("/").split("/")
                if len(pp) != len(cp):
                    continue
                params: dict[str, str] = {}
                ok = True
                for a, b in zip(pp, cp):
                    if a.startswith(":"):
                        params[a[1:]] = b
                    elif a != b:
                        ok = False
                if ok:
                    return handler(params)
        if "*" in self.routes:
            return self.routes["*"]({})
        raise KeyError(path)


@dataclass
class MockFetch:
    responses: dict[str, dict[str, object]]

    def get(self, url: str) -> dict[str, object]:
        if url not in self.responses:
            raise KeyError(url)
        return self.responses[url]


@dataclass
class FormValidator:
    def validate_email(self, value: str) -> str | None:
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
            return "invalid email"
        return None

    def validate_password(self, value: str) -> str | None:
        if len(value) < 8:
            return "password too short"
        return None


class DesignTokenChecker:
    def __init__(self, token_json: str) -> None:
        self.tokens = json.loads(token_json)

    def require_keys(self, keys: list[str]) -> list[str]:
        missing = []
        for key in keys:
            if key not in self.tokens:
                missing.append(key)
        return missing


class BundleSimulator:
    def concat(self, files: list[str]) -> str:
        return "\n".join(files)

    def minify(self, content: str) -> str:
        return re.sub(r"\s+", " ", content).strip()

    def estimate_size(self, content: str) -> int:
        return len(content.encode("utf-8"))
