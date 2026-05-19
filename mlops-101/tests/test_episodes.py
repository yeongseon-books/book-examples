from __future__ import annotations

import tempfile

import numpy as np
from conftest import load_module

common = load_module("common.py", "common")
DataVersionStore = common.DataVersionStore
DriftDetector = common.DriftDetector
ExperimentTracker = common.ExperimentTracker
FeatureStore = common.FeatureStore
ModelRegistry = common.ModelRegistry
Monitoring = common.Monitoring
ProductionSystem = common.ProductionSystem
RetrainingTrigger = common.RetrainingTrigger
TrainingPipeline = common.TrainingPipeline


def test_ep01_overview_bootstrap_runs() -> None:
    module = load_module("ko/01-what-is-mlops/step01_mlops_loop.py", "ep01")
    out = module.run_overview()
    assert out["version"].startswith("v")


def test_ep02_tracker_selects_best_run() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tracker = ExperimentTracker(root=common.Path(tmp))
        tracker.log_run({"C": 0.1}, {"accuracy": 0.7}, {})
        best_id = tracker.log_run({"C": 1.0}, {"accuracy": 0.9}, {})
        assert tracker.best_run("accuracy")["run_id"] == best_id


def test_ep03_dataset_hash_changes_when_data_changes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        store = DataVersionStore(root=common.Path(tmp))
        h1 = store.put(np.array([1.0, 2.0, 3.0]))
        h2 = store.put(np.array([1.0, 2.0, 4.0]))
        assert h1 != h2


def test_ep04_pipeline_registers_staging_model() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        registry = ModelRegistry(root=common.Path(tmp))
        out = TrainingPipeline(registry).run()
        assert out["accuracy"] > 0.5
        assert registry.get_by_stage("Staging") is not None


def test_ep05_registry_promotes_staging_to_production() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        registry = ModelRegistry(root=common.Path(tmp))
        version = TrainingPipeline(registry).run()["version"]
        registry.transition_stage(version, "Production")
        prod = registry.get_by_stage("Production")
        assert prod is not None and prod.version == version


def test_ep06_monitoring_computes_error_rate_and_latency_histogram() -> None:
    mon = Monitoring()
    mon.record(1, 10.0, ok=True)
    mon.record(0, 30.0, ok=False)
    assert mon.error_rate() == 0.5
    counts, _ = mon.latency_histogram()
    assert counts.sum() == 2


def test_ep07_drift_detector_triggers_above_threshold() -> None:
    rng = np.random.default_rng(42)
    base = rng.normal(0.0, 1.0, 1500)
    live = rng.normal(1.2, 1.0, 1500)
    result = DriftDetector().detect(base, live, psi_threshold=0.2, ks_threshold=0.2)
    assert result["drift"] is True


def test_ep08_retraining_trigger_fires_on_drift() -> None:
    trigger = RetrainingTrigger(drift_threshold=0.2, schedule_days=30)
    assert trigger.should_fire(psi_value=0.21, days_since_last_train=1) == "drift"


def test_ep09_feature_store_point_in_time_correctness() -> None:
    fs = FeatureStore()
    fs.ingest_offline({"entity_id": "u1", "event_ts": 100, "score": 1.0})
    fs.ingest_offline({"entity_id": "u1", "event_ts": 200, "score": 2.0})
    row = fs.get_historical("u1", 150)
    assert row is not None and row["score"] == 1.0


def test_ep10_production_system_composes_end_to_end() -> None:
    out = ProductionSystem().bootstrap()
    assert out["version"].startswith("v")
    assert out["error_rate"] == 0.0
