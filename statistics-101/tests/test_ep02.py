import pytest

from en.ep02_mean_median_variance_std_mode import run_demo as en_run
from ko.ep02_mean_median_variance_std_mode import run_demo as ko_run


def test_ep02_core_stats():
    e = en_run()
    k = ko_run()
    assert e["mean_manual"] == pytest.approx(e["mean_numpy"])
    assert e["var_manual"] == pytest.approx(e["var_numpy"])
    assert e["std_manual"] == pytest.approx(e["std_numpy"])
    assert e["mode_manual"] == 5.0
    assert e["mean_manual"] == k["mean_manual"]
