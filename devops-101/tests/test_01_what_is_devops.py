from datetime import datetime

from common import Event, EventLog
from ko import _01_what_is_devops as ep01


def test_dora_lead_time_computes_from_fixture() -> None:
    events = EventLog(
        [
            Event(datetime(2026, 5, 1, 10, 0, 0), "commit", "d1", {}),
            Event(datetime(2026, 5, 1, 10, 30, 0), "deploy", "d1", {}),
            Event(
                datetime(2026, 5, 1, 11, 0, 0),
                "incident_resolved",
                "d1",
                {"minutes_to_restore": 20},
            ),
        ]
    )
    metrics = ep01.compute_dora_metrics(events)
    assert metrics["lead_time_minutes"] == 30.0
