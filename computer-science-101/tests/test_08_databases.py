import importlib.util
from pathlib import Path


def load(name, rel):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).parent.parent / rel
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_select_where_join_behavior():
    m = load("ep08", "ko/08-databases.py")
    users = m.Table([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])
    orders = m.Table(
        [
            {"order_id": 10, "user_id": 1, "amount": 50},
            {"order_id": 11, "user_id": 1, "amount": 20},
        ]
    )
    rows = (
        users.join(orders, "id", "user_id")
        .where(lambda r: r["amount"] >= 30)
        .select("name", "amount")
        .rows
    )
    assert rows == [{"name": "Alice", "amount": 50}]
