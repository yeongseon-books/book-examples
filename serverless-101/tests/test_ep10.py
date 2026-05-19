from common import *
from en.ep10_app_design import run_demo


def test_ep10():
    out = run_demo()
    assert len(out["orders"]) == 1 and len(out["processed"]) >= 1
