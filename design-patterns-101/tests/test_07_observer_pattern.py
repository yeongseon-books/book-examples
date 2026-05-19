import gc
import importlib.util
from pathlib import Path


def load():
    p = Path(__file__).resolve().parents[1] / "ko/07-observer-pattern.py"
    s = importlib.util.spec_from_file_location("ep07", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_subscribe_publish_unsubscribe_and_weakref():
    m = load()
    bus = m.EventBus()
    r = m.Recorder()
    token = bus.subscribe("order", r.on_event)
    bus.publish("order", {"id": 1})
    bus.unsubscribe("order", token)
    bus.publish("order", {"id": 2})
    assert r.events == [{"id": 1}]
    tmp = m.Recorder()
    bus.subscribe("tmp", tmp.on_event)
    del tmp
    gc.collect()
    bus.publish("tmp", {"x": 1})
    assert len(bus._subs["tmp"]) == 0
