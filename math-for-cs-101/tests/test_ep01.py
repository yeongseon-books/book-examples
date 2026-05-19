from tests.conftest import load_module


def test_ep01_big_o_ratio():
    m=load_module('ko/01-why-math-for-cs/step01_complexity_demo.py')
    assert m.operation_count_linear(40)/m.operation_count_linear(20)==2
    assert m.operation_count_quadratic(40)/m.operation_count_quadratic(20)==4
