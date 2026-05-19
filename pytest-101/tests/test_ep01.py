from en.ep01_basic_math import add, factorial


def test_ep01_add_with_aaa_pattern(sample_numbers):
    a, b = sample_numbers
    result = add(a, b)
    assert result == 12


def test_ep01_factorial_base_and_regular_cases():
    assert factorial(0) == 1
    assert factorial(5) == 120
