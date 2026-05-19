from _loader import load_module

m = load_module("03-data-collection.py")


def test_episode_03_collection_csv_schema(tmp_path) -> None:
    report = m.generate_collected_data(tmp_path, seed=42, n_users=120)
    assert report["rows"] == 120
    assert set(["user_id", "country", "signup_days_ago", "event_count", "total_amount"]).issubset(report["columns"])
