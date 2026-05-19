from ko.ep08_interpreter_compiler import interpret, compile_bytecode

def test_ep08_interpret_and_compile():
    expr = ("add", ("num", 1), ("num", 2))
    assert interpret(expr) == 3
    assert compile_bytecode(expr)[-1] == ("ADD",)
