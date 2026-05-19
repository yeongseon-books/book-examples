"""Mlops 101 - Episode 1: Model deployment."""

import pickle

from common import ModelRegistry, ModelServer, TrainingPipeline


def run_deployment_demo() -> dict[str, float | int]:
    """Run deployment demo."""
    registry = ModelRegistry()
    result = TrainingPipeline(registry).run()
    record = registry.get_by_stage("Staging")
    if record is None:
        raise RuntimeError("staging model missing")
    model = pickle.loads(record.path.read_bytes())
    response = ModelServer(model).predict([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    return {
        "version": result["version"],
        "prediction": response["prediction"],
        "latency_ms": response["latency_ms"],
    }


if __name__ == "__main__":
    print(run_deployment_demo())
