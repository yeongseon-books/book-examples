import importlib.util
from pathlib import Path


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent.parent / rel)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_stack_machine_adds_values():
    m = load("ep05", "ko/05-computer-architecture.py")
    stack = m.run_program([("PUSH", 7), ("PUSH", 5), ("ADD",), ("HALT",)])
    assert stack == [12]
