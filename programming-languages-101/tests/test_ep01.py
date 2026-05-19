from ko.ep01_repl import repl_once

def test_ep01_safe_repl_arith():
    assert repl_once("(1+2)*3") == 9
