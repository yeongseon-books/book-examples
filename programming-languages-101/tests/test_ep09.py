from ko.ep09_static_dynamic import static_check, dynamic_run

def test_ep09_static_dynamic_compare():
    expr = ("add", ("num", 1), ("num", 2))
    assert static_check(expr) == "Int"
    assert dynamic_run(expr) == 3
