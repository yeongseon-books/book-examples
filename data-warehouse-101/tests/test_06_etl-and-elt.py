from conftest import load_episode


def test_06_etl_and_elt():
    mod = load_episode("ko", "06-etl-and-elt.py")
    res = mod["run_demo"]()
    assert res["etl"] == res["elt"]
