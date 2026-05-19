from common import *
from en.ep02_faas_runtime import run_demo


def test_ep02():
    out = run_demo()
    assert out["echo"]["msg"] == "hi"
