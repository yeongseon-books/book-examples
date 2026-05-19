"""Tests for 05 coding interview in Developer Career 101."""

from tests.test_01_what_is_developer_career import load


def test_05_two_sum_bruteforce_and_optimal_with_ops():
    """Test 05 two sum bruteforce and optimal with ops."""
    mod = load("05-coding-interview.py")
    nums = [1, 3, 8, 2, 9, 4]
    target = 13
    b_ans, b_ops = mod.two_sum_bruteforce(nums, target)
    o_ans, o_ops = mod.two_sum_optimal(nums, target)
    assert b_ans == [4, 5]
    assert o_ans == [4, 5]
    assert o_ops < b_ops
