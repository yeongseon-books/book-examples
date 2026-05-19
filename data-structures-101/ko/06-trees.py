"""Data Structures 101 - Episode 6: Trees."""

from __future__ import annotations

from collections import deque


class TreeNode:
    """Tree node."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.children: list[TreeNode] = []

    def add(self, child: TreeNode) -> TreeNode:
        """Add."""
        self.children.append(child)
        return child


def preorder(root: TreeNode) -> list[int]:
    """Preorder."""
    out = [root.value]
    for child in root.children:
        out.extend(preorder(child))
    return out


def postorder(root: TreeNode) -> list[int]:
    """Postorder."""
    out: list[int] = []
    for child in root.children:
        out.extend(postorder(child))
    out.append(root.value)
    return out


def inorder_binary(root: TreeNode | None) -> list[int]:
    """Inorder binary."""
    if root is None:
        return []
    left = inorder_binary(root.children[0] if len(root.children) > 0 else None)
    right = inorder_binary(root.children[1] if len(root.children) > 1 else None)
    return left + [root.value] + right


def levelorder(root: TreeNode) -> list[int]:
    """Levelorder."""
    q: deque[TreeNode] = deque([root])
    out: list[int] = []
    while q:
        node = q.popleft()
        out.append(node.value)
        for child in node.children:
            q.append(child)
    return out


def size(root: TreeNode) -> int:
    """Size."""
    return 1 + sum(size(child) for child in root.children)


def depth(root: TreeNode) -> int:
    """Depth."""
    if not root.children:
        return 0
    return 1 + max(depth(child) for child in root.children)


def diameter(root: TreeNode) -> int:
    """Diameter."""
    best = 0

    def walk(node: TreeNode) -> int:
        """Walk."""
        nonlocal best
        heights = sorted((walk(c) for c in node.children), reverse=True)
        a = heights[0] if heights else 0
        b = heights[1] if len(heights) > 1 else 0
        best = max(best, a + b)
        return a + 1

    walk(root)
    return best
