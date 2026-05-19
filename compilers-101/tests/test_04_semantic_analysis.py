"""Tests for 04 semantic analysis in Compilers 101."""

import pytest
from conftest import load_module

mod = load_module("ko/04-semantic-analysis.py", "ep04")


def test_semantic_undefined_var() -> None:
    """Test semantic undefined var."""
    with pytest.raises(mod.SemanticError):
        mod.check_program([("expr", ("var", "y"))])
