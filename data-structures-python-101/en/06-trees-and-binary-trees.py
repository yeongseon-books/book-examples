"""Data Structures Python 101 - Episode 6: Trees and binary trees."""

import xml.etree.ElementTree as ET
from collections import deque
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    """Tree node."""

    name: str
    children: list["TreeNode"] = field(default_factory=list)


def bfs_names(root: TreeNode) -> list[str]:
    """Bfs names."""
    q: deque[TreeNode] = deque([root])
    out: list[str] = []
    while q:
        node = q.popleft()
        out.append(node.name)
        q.extend(node.children)
    return out


def dfs_names(root: TreeNode) -> list[str]:
    """Dfs names."""
    out = [root.name]
    for child in root.children:
        out.extend(dfs_names(child))
    return out


def xml_tags(xml_text: str) -> list[str]:
    """Xml tags."""
    root = ET.fromstring(xml_text)
    return [elem.tag for elem in root.iter()]


if __name__ == "__main__":
    root = TreeNode("root", [TreeNode("a"), TreeNode("b", [TreeNode("c")])])
    print(bfs_names(root))
    print(dfs_names(root))
    print(xml_tags("<root><item/><item><name/></item></root>"))
