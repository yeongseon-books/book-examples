"""Type Hints Python 101 - Episode 10: Best practices."""

import ast
from typing import TypeAlias

Score: TypeAlias = dict[str, int]


def score_module_typing(source: str) -> Score:
    """Score module typing."""
    tree = ast.parse(source)
    score: Score = {"annotated_functions": 0, "has_any": 0, "aliases": 0}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            has_ret = node.returns is not None
            has_args = all(a.annotation is not None for a in node.args.args)
            if has_ret and has_args:
                score["annotated_functions"] += 1
        if isinstance(node, ast.Name) and node.id == "Any":
            score["has_any"] += 1
        if isinstance(node, ast.ImportFrom) and node.module == "typing":
            for alias in node.names:
                if alias.name == "Any":
                    score["has_any"] += 1
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id.endswith("Alias"):
                score["aliases"] += 1
    return score
