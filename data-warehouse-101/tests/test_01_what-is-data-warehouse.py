from conftest import load_episode


def test_01_what_is_data_warehouse():
    mod = load_episode("ko", "01-what-is-data-warehouse.py")
    res = mod["run_demo"]()
    assert res["months"] > 0 and res["total_revenue"] > 0
