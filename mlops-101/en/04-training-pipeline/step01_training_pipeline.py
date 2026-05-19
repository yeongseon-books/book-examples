from common import ModelRegistry, TrainingPipeline


def run_pipeline_demo() -> dict[str, float | str]:
    return TrainingPipeline(ModelRegistry()).run()


if __name__ == "__main__":
    print(run_pipeline_demo())
