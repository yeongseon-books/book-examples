from __future__ import annotations

from datetime import datetime

from common import EventLog


def compute_dora_metrics(event_log: EventLog) -> dict[str, float]:
    commits = {}
    deployments = {}
    incidents = []

    for event in event_log.events:
        if event.kind == 'commit':
            commits[event.deployment_id] = event.timestamp
        elif event.kind == 'deploy':
            deployments[event.deployment_id] = event.timestamp
        elif event.kind == 'incident_resolved':
            incidents.append(event)

    lead_times = []
    for dep_id, deployed_at in deployments.items():
        committed_at = commits.get(dep_id)
        if committed_at is not None:
            lead_times.append((deployed_at - committed_at).total_seconds() / 60)

    failed_deployments = {e.deployment_id for e in incidents}
    mttr_values = [
        float(event.metadata['minutes_to_restore'])
        for event in incidents
        if 'minutes_to_restore' in event.metadata
    ]

    deployment_days = {timestamp.date() for timestamp in deployments.values()}
    deployment_frequency = len(deployments) / max(1, len(deployment_days))

    return {
        'lead_time_minutes': sum(lead_times) / max(1, len(lead_times)),
        'deployment_frequency_per_day': deployment_frequency,
        'change_fail_rate': len(failed_deployments) / max(1, len(deployments)),
        'mttr_minutes': sum(mttr_values) / max(1, len(mttr_values)),
    }
