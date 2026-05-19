from conftest import load_episode


def test_10_warehouse_design_example():
    mod = load_episode("ko", "10-warehouse-design-example.py")
    res = mod["run_demo"]()
    assert (
        res["mart_rows"] > 0
        and len(res["bi_top_months"]) == 3
        and "Grain" in res["design_doc"]
    )
