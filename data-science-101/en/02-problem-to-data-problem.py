from __future__ import annotations


def make_data_problem_spec() -> dict[str, object]:
    return {
        "business_question": "Which users are likely to churn within 30 days?",
        "prediction_type": "binary_classification",
        "target": "churn_30d",
        "features": [
            "days_since_last_login",
            "sessions_30d",
            "avg_order_value",
            "plan_type",
        ],
        "metric": "f1",
        "window_days": 30,
        "population": "paid_users",
    }


def validate_spec(spec: dict[str, object]) -> bool:
    required = {
        "business_question",
        "prediction_type",
        "target",
        "features",
        "metric",
        "window_days",
        "population",
    }
    missing = required.difference(spec)
    if missing:
        return False
    features = spec["features"]
    return (
        isinstance(features, list) and len(features) >= 3 and spec["window_days"] == 30
    )


if __name__ == "__main__":
    spec = make_data_problem_spec()
    print(spec)
    print({"valid": validate_spec(spec)})
