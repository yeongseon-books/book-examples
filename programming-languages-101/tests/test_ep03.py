import pytest
from ko.ep03_type_system import check_expr_type

def test_ep03_type_checker():
    assert check_expr_type(("add", ("int", 1), ("int", 2))) == "Int"
    with pytest.raises(TypeError):
        check_expr_type(("add", ("int", 1), ("bool", True)))
