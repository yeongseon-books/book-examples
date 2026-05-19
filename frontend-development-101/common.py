"""Shared utilities and domain models for Frontend Development 101."""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from html.parser import HTMLParser


class _TagCollector(HTMLParser):
    """Tag collector."""

    def __init__(self) -> None:
        super().__init__()
        self.tags: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Handle starttag."""
        self.tags.append({"tag": tag, "attrs": dict(attrs)})


class HTMLAnalyzer:
    """HTML analyzer."""

    def __init__(self, html: str) -> None:
        collector = _TagCollector()
        collector.feed(html)
        self.tags = collector.tags

    def has_semantic_tags(self, required: set[str]) -> bool:
        """Has semantic tags."""
        seen = {item["tag"] for item in self.tags}
        return required.issubset(seen)

    def missing_alt_images(self) -> int:
        """Missing alt images."""
        count = 0
        for item in self.tags:
            if item["tag"] == "img":
                attrs = item["attrs"]
                alt = attrs.get("alt")
                if alt is None or alt.strip() == "":
                    count += 1
        return count

    def aria_issues(self) -> int:
        """Aria issues."""
        issues = 0
        for item in self.tags:
            if item["tag"] in {"input", "button", "select", "textarea"}:
                attrs = item["attrs"]
                has_name = "aria-label" in attrs or "id" in attrs
                if not has_name:
                    issues += 1
        return issues


class CSSAnalyzer:
    """CSS analyzer."""

    RULE_RE = re.compile(r"([^{}]+)\{([^{}]+)\}")

    def __init__(self, css: str) -> None:
        self.css = css
        self.rules = self.RULE_RE.findall(css)

    def selector_specificity(self, selector: str) -> tuple[int, int, int]:
        """Selector specificity."""
        a = selector.count("#")
        b = selector.count(".") + selector.count("[")
        c = sum(
            1 for tok in re.split(r"\s+|>|\+|~", selector) if tok and tok[0].isalpha()
        )
        return a, b, c

    def unused_selectors(self, html: str) -> list[str]:
        """Unused selectors."""
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
            if (
                selector.startswith(".")
                and selector[1:] not in classes
                or selector.startswith("#")
                and selector[1:] not in ids
                or selector
                and selector[0].isalpha()
                and selector not in tags
            ):
                unused.append(selector)
        return unused

    def enforce_tokens(self, token_prefix: str = "--color-") -> list[str]:
        """Enforce tokens."""
        violations = []
        for _, body in self.rules:
            for line in body.split(";"):
                if "color" in line and "var(" not in line and "#" in line:
                    violations.append(line.strip())
        if token_prefix not in self.css:
            violations.append("missing token declaration")
        return [v for v in violations if v]


class JSAnalyzer:
    """JS analyzer."""

    def __init__(self, js: str) -> None:
        self.js = js

    def declaration_counts(self) -> dict[str, int]:
        """Declaration counts."""
        return {
            "var": len(re.findall(r"\bvar\b", self.js)),
            "let": len(re.findall(r"\blet\b", self.js)),
            "const": len(re.findall(r"\bconst\b", self.js)),
        }

    def async_patterns(self) -> dict[str, int]:
        """Async patterns."""
        return {
            "async": len(re.findall(r"\basync\b", self.js)),
            "await": len(re.findall(r"\bawait\b", self.js)),
            "fetch": len(re.findall(r"\bfetch\b", self.js)),
        }

    def component_names(self) -> list[str]:
        """Component names."""
        names = re.findall(r"function\s+([A-Z][A-Za-z0-9_]*)", self.js)
        return names


@dataclass
class ComponentSim:
    """Component sim."""

    props: dict[str, object]
    state: dict[str, object]
    renderer: Callable[[dict[str, object], dict[str, object]], str]

    def set_state(self, updates: dict[str, object]) -> None:
        """Set state."""
        self.state.update(updates)

    def render(self) -> str:
        """Render."""
        return self.renderer(self.props, self.state)


@dataclass
class RouterSim:
    """Router sim."""

    routes: dict[str, Callable[[dict[str, str]], str]]
    history: list[str] = field(default_factory=list)

    def navigate(self, path: str) -> str:
        """Navigate."""
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
                for a, b in zip(pp, cp, strict=False):
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
    """Mock fetch."""

    responses: dict[str, dict[str, object]]

    def get(self, url: str) -> dict[str, object]:
        """Get."""
        if url not in self.responses:
            raise KeyError(url)
        return self.responses[url]


@dataclass
class FormValidator:
    """Form validator."""

    def validate_email(self, value: str) -> str | None:
        """Validate email."""
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
            return "invalid email"
        return None

    def validate_password(self, value: str) -> str | None:
        """Validate password."""
        if len(value) < 8:
            return "password too short"
        return None


class DesignTokenChecker:
    """Design token checker."""

    def __init__(self, token_json: str) -> None:
        self.tokens = json.loads(token_json)

    def require_keys(self, keys: list[str]) -> list[str]:
        """Require keys."""
        missing = []
        for key in keys:
            if key not in self.tokens:
                missing.append(key)
        return missing


class BundleSimulator:
    """Bundle simulator."""

    def concat(self, files: list[str]) -> str:
        """Concat."""
        return "\n".join(files)

    def minify(self, content: str) -> str:
        """Minify."""
        return re.sub(r"\s+", " ", content).strip()

    def estimate_size(self, content: str) -> int:
        """Estimate size."""
        return len(content.encode("utf-8"))
