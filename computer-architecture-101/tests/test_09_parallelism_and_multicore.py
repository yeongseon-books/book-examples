from conftest import load_module

mod = load_module("ko/09-parallelism-and-multicore.py", "ep09")


def test_threaded_vector_add_matches_sequential() -> None:
    a = list(range(1000))
    b = list(range(2000, 3000))
    assert mod.vector_add_threaded(a, b, workers=4) == mod.vector_add_sequential(a, b)
