"""Incident Response 101 - Episode 8: postmortem example."""

from common import Incident, IncidentTimeline, PostmortemGenerator, PreventionTracker


def run() -> str:
    """Run."""
    incident = Incident(id="INC-008", title="api error spike", severity="SEV2")
    timeline = IncidentTimeline()
    timeline.append("monitor", "detected", "2026-05-01T01:00:00+00:00")
    timeline.append("oncall", "resolved", "2026-05-01T01:20:00+00:00")
    incident.events = timeline.events
    incident.close()

    tracker = PreventionTracker()
    a1 = tracker.add("add alert on p99", "sre-team", "2026-05-10")
    gen = PostmortemGenerator()
    return gen.generate(incident, [a1])


if __name__ == "__main__":
    print(run())
