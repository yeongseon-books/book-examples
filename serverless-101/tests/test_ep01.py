from common import *
from en.ep01_serverless_overview import run_demo


def test_ep01():
    out = run_demo()
    assert out["ok"] is True and out["request_id"].startswith("demo-")
