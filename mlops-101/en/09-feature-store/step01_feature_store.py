from common import FeatureStore


def run_feature_store_demo() -> dict[str, float | int | str] | None:
    fs = FeatureStore()
    fs.ingest_offline({"entity_id": "u1", "event_ts": 100, "f1": 1.0})
    fs.ingest_offline({"entity_id": "u1", "event_ts": 200, "f1": 2.0})
    fs.materialize_online()
    return fs.get_historical("u1", 150)


if __name__ == "__main__":
    print(run_feature_store_demo())
