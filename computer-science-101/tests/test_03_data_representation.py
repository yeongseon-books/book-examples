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


def test_utf8_and_float_behavior():
    m = load("ep03", "ko/03-data-representation.py")
    assert m.int_to_binary(42) == "101010"
    assert m.utf8_bytes("가") == [234, 176, 128]
    value, close = m.float_sum_issue()
    assert value != 0.3
    assert close is True
