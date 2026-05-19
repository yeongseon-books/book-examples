import importlib.util
from pathlib import Path


def load(name, rel):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).parent.parent / rel
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_refactor_keeps_behavior():
    m = load("ep09", "ko/09-software-engineering.py")
    cases = [
        {"price": 100, "qty": 2, "user": "vip", "coupon": 20},
        {"price": 100, "qty": 1, "user": "member", "coupon": None},
        {"price": 50, "qty": 1, "user": "guest", "coupon": 100},
    ]
    for case in cases:
        assert m.price_bad(case) == m.price_refactored(case)
