from common import *
from en.ep07_queue_worker import run_demo


def test_ep07():
    out = run_demo()
    assert "m1" in out["processed"] and out["dead_letter"] == []
