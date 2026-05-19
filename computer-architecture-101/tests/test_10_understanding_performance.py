from conftest import load_module


mod = load_module("ko/10-understanding-performance.py", "ep10")


def test_amdahl_expected_value() -> None:
    assert abs(mod.amdahl(p=0.9, n=4) - 3.0769230769) < 1e-6


def test_benchmark_shapes() -> None:
    values = mod.benchmark()
    assert set(values.keys()) == {"loop", "comprehension"}
    assert values["loop"] > 0.0
    assert values["comprehension"] > 0.0
