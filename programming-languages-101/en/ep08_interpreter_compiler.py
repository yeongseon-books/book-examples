def interpret(expr):
    tag = expr[0]
    if tag == "num":
        return expr[1]
    if tag == "add":
        return interpret(expr[1]) + interpret(expr[2])
    raise ValueError("unknown")


def compile_bytecode(expr):
    code = []

    def walk(node):
        if node[0] == "num":
            code.append(("PUSH", node[1]))
        elif node[0] == "add":
            walk(node[1])
            walk(node[2])
            code.append(("ADD",))
        else:
            raise ValueError("unknown")

    walk(expr)
    return code
