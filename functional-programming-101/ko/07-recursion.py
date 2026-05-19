from __future__ import annotations


def tree_sum(node: dict[str, object]) -> int:
    value = int(node.get("value", 0))
    children = node.get("children", [])
    return value + sum(tree_sum(child) for child in children if isinstance(child, dict))


def factorial_tail(n: int, acc: int = 1) -> int:
    if n <= 1:
        return acc
    return factorial_tail(n - 1, acc * n)


if __name__ == "__main__":
    sample = {"value": 5, "children": [{"value": 3, "children": []}]}
    print(tree_sum(sample), factorial_tail(5))
