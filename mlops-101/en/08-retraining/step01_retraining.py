from common import RetrainingTrigger


def run_retraining_demo() -> str | None:
    return RetrainingTrigger(drift_threshold=0.2, schedule_days=30).should_fire(psi_value=0.25, days_since_last_train=5)


if __name__ == "__main__":
    print(run_retraining_demo())
