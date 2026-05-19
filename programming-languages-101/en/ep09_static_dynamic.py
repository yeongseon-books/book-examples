from en.ep03_type_system import check_expr_type
from en.ep08_interpreter_compiler import interpret


def static_check(expr):
    if expr[0] == "add":
        left = ("int", expr[1][1]) if expr[1][0] == "num" else expr[1]
        right = ("int", expr[2][1]) if expr[2][0] == "num" else expr[2]
        return check_expr_type(("add", left, right))
    return "Unknown"


def dynamic_run(expr):
    return interpret(expr)
