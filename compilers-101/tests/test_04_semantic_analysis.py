import pytest
from conftest import load_module

mod = load_module("ko/04-semantic-analysis.py", "ep04")


def test_semantic_undefined_var() -> None:
    with pytest.raises(mod.SemanticError):
        mod.check_program([("expr", ("var", "y"))])
