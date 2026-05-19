from ko.ep04_function_hints import run_op, sum_all


def test_ep04_callable_and_varargs() -> None:
    assert run_op(lambda a, b: a * b, 3, 4) == 12
    assert sum_all(1, 2, x=3, y=4, scale=2) == 20
