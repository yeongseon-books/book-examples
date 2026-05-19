from tests.conftest import load_module


def test_longest_unique_substring() -> None:
    mod = load_module("ko/10-coding-test-strategies/step01_patterns.py", "ep10")
    assert mod.longest_unique_substring("abcabcbb") == 3
    assert mod.longest_unique_substring("bbbbb") == 1
