from common import ep03_scheduler


def test_ep03_scheduler_orders():
    out = ep03_scheduler(["A", "B", "C"], quantum=2)
    assert out["fifo"] == ["A", "B", "C"]
    assert out["round_robin"].count("A") == 2
    assert out["round_robin"][0] == "A"
