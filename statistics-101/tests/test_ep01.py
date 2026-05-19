from en.ep01_stats_overview import run_demo as en_run
from ko.ep01_stats_overview import run_demo as ko_run


def test_ep01_overview():
    e = en_run()
    k = ko_run()
    assert e["mean"] == k["mean"]
    assert e["mean"] == 8.428571428571429
