from conftest import load_module

mod = load_module("ko/05-symbol-table-and-scope.py", "ep05")


def test_nested_scope_lookup() -> None:
    g = mod.SymbolTable()
    g.insert("x", "global")
    l = mod.SymbolTable(g)
    l.insert("x", "local")
    assert l.lookup("x") == "local"
    assert g.lookup("x") == "global"
