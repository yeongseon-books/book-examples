from conftest import load_episode


def test_04_star_schema():
    mod = load_episode("ko", "04-star-schema.py")
    res = mod["run_demo"]()
    assert res["groups"] > 0 and abs(res["fact_total"] - res["grouped_total"]) < 0.01
