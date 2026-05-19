"""Programming Languages 101 - Episode 3: Type system."""


def check_expr_type(node: tuple) -> str:
    """Check expr type."""
    tag = node[0]
    if tag == "int":
        return "Int"
    if tag == "bool":
        return "Bool"
    if tag == "str":
        return "Str"
    if tag == "add":
        l = check_expr_type(node[1])
        r = check_expr_type(node[2])
        if l == "Int" and r == "Int":
            return "Int"
        if l == "Str" and r == "Str":
            return "Str"
        raise TypeError("invalid add")
    raise TypeError("unknown node")
