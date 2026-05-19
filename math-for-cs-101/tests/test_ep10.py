from common import fast_power, gcd

from tests.conftest import load_module


def test_ep10_fast_power_matches_pow():
    m = load_module("ko/10-algorithms-and-math/step01_algorithms_and_math.py")
    assert gcd(252, 105) == 21
    assert fast_power(7, 20, 101) == pow(7, 20, 101)
    assert m.hash_mod(12345, 97) == 26
