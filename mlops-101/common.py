"""Shared utilities and domain models for Mlops 101."""

from __future__ import annotations

import hashlib
import json
import pickle
import time
from dataclasses import dataclass
from pathlib import Path
from tempfile import gettempdir
from typing import Any

import numpy as np
from numpy.typing import NDArray
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def _now_ms() -> int:
    """Now ms."""
    return int(time.time() * 1000)


class ExperimentTracker:
    """Experiment tracker."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(gettempdir()) / "mlops_101_tracker"
        self.root.mkdir(parents=True, exist_ok=True)

    def log_run(
        self,
        params: dict[str, Any],
        metrics: dict[str, float],
        artifacts: dict[str, Any],
    ) -> str:
        """Log run."""
        run_id = hashlib.sha1(f"{_now_ms()}-{params}".encode()).hexdigest()[:12]
        payload = {
            "run_id": run_id,
            "params": params,
            "metrics": metrics,
            "artifacts": artifacts,
            "ts_ms": _now_ms(),
        }
        (self.root / f"{run_id}.json").write_text(
            json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8"
        )
        return run_id

    def all_runs(self) -> list[dict[str, Any]]:
        """All runs."""
        runs: list[dict[str, Any]] = []
        for file in sorted(self.root.glob("*.json")):
            runs.append(json.loads(file.read_text(encoding="utf-8")))
        return runs

    def best_run(self, metric: str, higher_is_better: bool = True) -> dict[str, Any]:
        """Best run."""
        runs = [r for r in self.all_runs() if metric in r.get("metrics", {})]
        if not runs:
            raise ValueError("no runs for metric")
        return sorted(
            runs, key=lambda r: r["metrics"][metric], reverse=higher_is_better
        )[0]


class DataVersionStore:
    """Data version store."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(gettempdir()) / "mlops_101_data_store"
        self.root.mkdir(parents=True, exist_ok=True)

    def put(self, array: NDArray[np.float64]) -> str:
        """Put."""
        blob = pickle.dumps(array)
        digest = hashlib.sha256(blob).hexdigest()
        (self.root / f"{digest}.pkl").write_bytes(blob)
        return digest

    def get(self, digest: str) -> NDArray[np.float64]:
        """Get."""
        return pickle.loads((self.root / f"{digest}.pkl").read_bytes())


@dataclass
class RegisteredModel:
    """Registered model."""

    version: str
    stage: str
    path: Path
    metrics: dict[str, float]


class ModelRegistry:
    """Model registry."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path(gettempdir()) / "mlops_101_registry"
        self.root.mkdir(parents=True, exist_ok=True)
        self.meta_path = self.root / "registry.json"
        if not self.meta_path.exists():
            self.meta_path.write_text("[]", encoding="utf-8")

    def _load(self) -> list[dict[str, Any]]:
        """Load."""
        return json.loads(self.meta_path.read_text(encoding="utf-8"))

    def _save(self, items: list[dict[str, Any]]) -> None:
        """Save."""
        self.meta_path.write_text(
            json.dumps(items, ensure_ascii=True, indent=2), encoding="utf-8"
        )

    def register(
        self, model: Any, metrics: dict[str, float], stage: str = "Staging"
    ) -> str:
        """Register."""
        items = self._load()
        version = f"v{len(items) + 1}"
        model_path = self.root / f"{version}.pkl"
        model_path.write_bytes(pickle.dumps(model))
        items.append(
            {
                "version": version,
                "stage": stage,
                "path": str(model_path),
                "metrics": metrics,
            }
        )
        self._save(items)
        return version

    def transition_stage(self, version: str, new_stage: str) -> None:
        """Transition stage."""
        items = self._load()
        for item in items:
            if item["version"] == version:
                item["stage"] = new_stage
        self._save(items)

    def get_by_stage(self, stage: str) -> RegisteredModel | None:
        """Get by stage."""
        for item in self._load():
            if item["stage"] == stage:
                return RegisteredModel(
                    item["version"], item["stage"], Path(item["path"]), item["metrics"]
                )
        return None


class TrainingPipeline:
    """Training pipeline."""

    def __init__(self, registry: ModelRegistry, random_state: int = 42) -> None:
        self.registry = registry
        self.random_state = random_state

    def run(self) -> dict[str, Any]:
        """Run."""
        X, y = make_classification(
            n_samples=300, n_features=6, n_informative=4, random_state=self.random_state
        )
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=self.random_state
        )
        model = LogisticRegression(max_iter=1000, random_state=self.random_state).fit(
            X_train, y_train
        )
        pred = model.predict(X_test)
        acc = float(accuracy_score(y_test, pred))
        version = self.registry.register(model, {"accuracy": acc}, stage="Staging")
        return {"version": version, "accuracy": acc}


class ModelServer:
    """Model server."""

    def __init__(self, model: Any) -> None:
        self.model = model
        self.logs: list[dict[str, Any]] = []

    def predict(self, features: list[float]) -> dict[str, Any]:
        """Predict."""
        started = time.perf_counter()
        value = int(self.model.predict(np.array([features]))[0])
        latency_ms = (time.perf_counter() - started) * 1000
        row = {
            "features": features,
            "prediction": value,
            "latency_ms": latency_ms,
            "ok": True,
        }
        self.logs.append(row)
        return {"prediction": value, "latency_ms": latency_ms}


class Monitoring:
    """Monitoring."""

    def __init__(self) -> None:
        self.predictions: list[int] = []
        self.latencies_ms: list[float] = []
        self.errors: int = 0
        self.total: int = 0

    def record(self, prediction: int, latency_ms: float, ok: bool = True) -> None:
        """Record."""
        self.predictions.append(prediction)
        self.latencies_ms.append(latency_ms)
        self.total += 1
        if not ok:
            self.errors += 1

    def error_rate(self) -> float:
        """Error rate."""
        if self.total == 0:
            return 0.0
        return self.errors / self.total

    def latency_histogram(
        self, bins: int = 5
    ) -> tuple[NDArray[np.int64], NDArray[np.float64]]:
        """Latency histogram."""
        return np.histogram(np.array(self.latencies_ms), bins=bins)


class DriftDetector:
    @staticmethod
    def ks_statistic(base: NDArray[np.float64], live: NDArray[np.float64]) -> float:
        """Ks statistic."""
        b = np.sort(base)
        l = np.sort(live)
        values = np.sort(np.concatenate([b, l]))
        cdf_b = np.searchsorted(b, values, side="right") / max(len(b), 1)
        cdf_l = np.searchsorted(l, values, side="right") / max(len(l), 1)
        return float(np.max(np.abs(cdf_b - cdf_l)))

    @staticmethod
    def psi(
        base: NDArray[np.float64], live: NDArray[np.float64], bins: int = 10
    ) -> float:
        """Psi."""
        edges = np.quantile(base, np.linspace(0, 1, bins + 1))
        edges[0] = -np.inf
        edges[-1] = np.inf
        base_hist, _ = np.histogram(base, edges)
        live_hist, _ = np.histogram(live, edges)
        bp = base_hist / max(base_hist.sum(), 1) + 1e-8
        lp = live_hist / max(live_hist.sum(), 1) + 1e-8
        return float(np.sum((lp - bp) * np.log(lp / bp)))

    def detect(
        self,
        base: NDArray[np.float64],
        live: NDArray[np.float64],
        psi_threshold: float = 0.2,
        ks_threshold: float = 0.2,
    ) -> dict[str, Any]:
        """Detect."""
        ks = self.ks_statistic(base, live)
        psi = self.psi(base, live)
        return {"ks": ks, "psi": psi, "drift": ks > ks_threshold or psi > psi_threshold}


class RetrainingTrigger:
    """Retraining trigger."""

    def __init__(self, drift_threshold: float = 0.2, schedule_days: int = 30) -> None:
        self.drift_threshold = drift_threshold
        self.schedule_days = schedule_days

    def should_fire(self, psi_value: float, days_since_last_train: int) -> str | None:
        """Should fire."""
        if psi_value >= self.drift_threshold:
            return "drift"
        if days_since_last_train >= self.schedule_days:
            return "schedule"
        return None


class FeatureStore:
    """Feature store."""

    def __init__(self) -> None:
        self.offline_rows: list[dict[str, Any]] = []
        self.online: dict[str, dict[str, Any]] = {}

    def ingest_offline(self, row: dict[str, Any]) -> None:
        """Ingest offline."""
        self.offline_rows.append(row)

    def materialize_online(self) -> None:
        """Materialize online."""
        for row in sorted(self.offline_rows, key=lambda r: r["event_ts"]):
            self.online[row["entity_id"]] = row

    def get_online(self, entity_id: str) -> dict[str, Any] | None:
        """Get online."""
        return self.online.get(entity_id)

    def get_historical(self, entity_id: str, as_of_ts: int) -> dict[str, Any] | None:
        """Get historical."""
        candidates = [
            r
            for r in self.offline_rows
            if r["entity_id"] == entity_id and r["event_ts"] <= as_of_ts
        ]
        if not candidates:
            return None
        return sorted(candidates, key=lambda r: r["event_ts"])[-1]


class ProductionSystem:
    """Production system."""

    def __init__(self) -> None:
        self.registry = ModelRegistry()
        self.pipeline = TrainingPipeline(self.registry)
        self.monitoring = Monitoring()
        self.drift = DriftDetector()
        self.trigger = RetrainingTrigger()
        self.feature_store = FeatureStore()
        self.tracker = ExperimentTracker()

    def bootstrap(self) -> dict[str, Any]:
        """Bootstrap."""
        train = self.pipeline.run()
        model_record = self.registry.get_by_stage("Staging")
        if model_record is None:
            raise RuntimeError("staging model not found")
        self.registry.transition_stage(model_record.version, "Production")
        model = pickle.loads(model_record.path.read_bytes())
        server = ModelServer(model)
        for _ in range(5):
            out = server.predict([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
            self.monitoring.record(out["prediction"], out["latency_ms"], ok=True)
        self.tracker.log_run(
            {"seed": 42}, {"accuracy": train["accuracy"]}, {"version": train["version"]}
        )
        return {"version": train["version"], "error_rate": self.monitoring.error_rate()}
