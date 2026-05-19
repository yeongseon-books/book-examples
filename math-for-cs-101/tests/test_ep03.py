from tests.conftest import load_module


def test_ep03_bijective_checker():
    m = load_module("ko/03-sets-and-functions/step01_sets_and_functions.py")
    inj, surj, bij = m.classify_mapping({1: "a", 2: "b", 3: "c"}, {"a", "b", "c"})
    assert inj and surj and bij
