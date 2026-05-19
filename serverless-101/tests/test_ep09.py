from common import *
from en.ep09_cost_model import run_demo


def test_ep09():
    out = run_demo()
    assert out["total_cost"] > 0
