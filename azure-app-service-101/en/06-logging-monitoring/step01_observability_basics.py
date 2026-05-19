"""Azure App Service 101 - Episode 1: Observability basics."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone


def correlation_id(inbound: str | None = None) -> str:
    """Correlation id."""
    return inbound or str(uuid.uuid4())


def json_log(message: str, **fields: object) -> str:
    """Json log."""
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": message,
        **fields,
    }
    return json.dumps(payload, ensure_ascii=False)


def kql_error_top_n(minutes: int = 30) -> str:
    """Kql error top n."""
    return (
        "AppTraces | where TimeGenerated > ago(" + str(minutes) + "m) "
        "| where SeverityLevel >= 3 | summarize count() by Message "
        "| order by count_ desc"
    )
