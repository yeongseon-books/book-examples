from en.ep01_overview import run_demo


def test_ep01_create_insert_select():
    rows = run_demo()
    assert [r["label"] for r in rows] == ["hello", "sql"]
