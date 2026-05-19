from conftest import load_episode


def test_07_bi_and_dashboard():
    mod = load_episode("ko", "07-bi-and-dashboard.py")
    res = mod["run_demo"]()
    assert res["total"] >= 0 and len(res["trend"]) > 0 and "#" in res["preview"]
