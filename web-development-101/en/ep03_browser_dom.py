"""Web Development 101 - Episode 3: Browser dom."""

from __future__ import annotations

from html.parser import HTMLParser


class Node:
    """Simplified DOM node."""

    def __init__(self, tag: str, attrs: dict | None = None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: list[Node] = []


class DOMBuilder(HTMLParser):
    """Build a simplified DOM tree from HTML."""

    def __init__(self):
        super().__init__()
        self.root = Node("document")
        self._stack: list[Node] = [self.root]

    def handle_starttag(self, tag, attrs):
        """Create child node and push to stack."""
        node = Node(tag, dict(attrs))
        self._stack[-1].children.append(node)
        self._stack.append(node)

    def handle_endtag(self, tag):
        """Pop from stack."""
        if len(self._stack) > 1:
            self._stack.pop()


def query_by_tag(root: Node, tag: str) -> list[Node]:
    """Find all descendant nodes matching tag."""
    results: list[Node] = []
    for child in root.children:
        if child.tag == tag:
            results.append(child)
        results.extend(query_by_tag(child, tag))
    return results


def query_by_class(root: Node, class_name: str) -> list[Node]:
    """Find all descendant nodes with given class."""
    results: list[Node] = []
    for child in root.children:
        classes = child.attrs.get("class", "").split()
        if class_name in classes:
            results.append(child)
        results.extend(query_by_class(child, class_name))
    return results
