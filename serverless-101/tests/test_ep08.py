from common import *
from en.ep08_observability import run_demo


def test_ep08():
    out = run_demo()
    assert out["metrics"]["invocations"] == 1.0 and len(out["logs"]) == 1
