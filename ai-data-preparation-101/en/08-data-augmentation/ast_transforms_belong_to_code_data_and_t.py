"""Generated from book-content article."""

import ast

class VarRenamer(ast.NodeTransformer):
    def __init__(self, mapping: dict[str, str]):
        self.mapping = mapping

    def visit_arg(self, node: ast.arg) -> ast.arg:
        if node.arg in self.mapping:
            node.arg = self.mapping[node.arg]
        return node

    def visit_Name(self, node: ast.Name) -> ast.Name:
        if node.id in self.mapping:
            node.id = self.mapping[node.id]
        return node

def rename_vars(src: str) -> str:
    tree = ast.parse(src)
    names = sorted(
        {n.arg for n in ast.walk(tree) if isinstance(n, ast.arg)}
        | {n.id for n in ast.walk(tree) if isinstance(n, ast.Name) and not n.id.startswith("__")}
    )
    mapping = {name: f"v{i}" for i, name in enumerate(names)}
    new_tree = VarRenamer(mapping).visit(tree)
    ast.fix_missing_locations(new_tree)
    return ast.unparse(new_tree)

src = """
def add(left, right):
    total = left + right
    return total
"""

print(rename_vars(src))
# def add(v0, v1):
#     v2 = v0 + v1
#     return v2
