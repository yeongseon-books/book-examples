import importlib.util
from pathlib import Path


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent.parent / rel)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_packet_drop_occurs_when_queue_small():
    m = load("ep07", "ko/07-networks.py")
    delivered, dropped = m.simulate_line(packet_count=12, capacity=2, ticks=20)
    assert delivered <= 12
    assert dropped > 0
