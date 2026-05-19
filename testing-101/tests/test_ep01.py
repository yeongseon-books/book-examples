from ko import ep01_testing_overview as sut


def test_ep01_add():
    assert sut.add(2, 3) == 5


def test_ep01_regression_guard_for_multiply():
    assert sut.multiply(4, 5) == 20
