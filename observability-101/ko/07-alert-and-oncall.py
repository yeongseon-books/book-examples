"""Observability 101 - Episode 7: Alert and oncall."""

from datetime import datetime, timedelta, timezone

from common import AlertEngine, AlertRule, OnCallRouter


def run_demo() -> tuple[list[dict[str, str]], str]:
    """Run demo."""
    engine = AlertEngine(dedup_window_s=60)
    engine.add_rule(AlertRule("high_error", "error_rate", 0.05, 120, "page"))
    now = datetime.now(timezone.utc)
    fired: list[dict[str, str]] = []
    for i in range(4):
        fired.extend(
            engine.evaluate(("error_rate", 0.10), now + timedelta(seconds=i * 40))
        )
    router = OnCallRouter(
        {"page": "primary-rotation", "ticket": "daytime-rotation", "default": "triage"}
    )
    return fired, router.route("page")
