"""Tests for ep07 in Type Hints Python 101."""

from ko.ep07_generics import Stack, call_with_log, clamp_to_zero


def test_ep07_generics_stack_and_paramspec() -> None:
    """Test ep07 generics stack and paramspec."""
    st: Stack[int] = Stack()
    st.push(10)
    assert st.pop() == 10
    assert clamp_to_zero(-3) == 0
    status, result = call_with_log(lambda x, y: x + y, 2, 5)
    assert status == "called"
    assert result == 7
