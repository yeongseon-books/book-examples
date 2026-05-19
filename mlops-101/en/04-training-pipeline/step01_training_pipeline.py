"""Mlops 101 - Episode 1: Training pipeline."""

from common import ModelRegistry, TrainingPipeline


def run_pipeline_demo() -> dict[str, float | str]:
    """Run pipeline demo."""
    return TrainingPipeline(ModelRegistry()).run()


if __name__ == "__main__":
    print(run_pipeline_demo())
