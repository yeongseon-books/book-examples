from tests.conftest import load_module


def test_ep05_counting_values():
    m=load_module('ko/05-combinatorics/step01_combinatorics.py')
    assert m.ncr(5,2)==10
    assert m.npr(5,2)==20
    assert m.pigeonhole(11,10)
