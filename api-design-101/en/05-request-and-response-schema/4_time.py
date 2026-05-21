# 4_time.py
from datetime import datetime, timezone

now = datetime.now(timezone.utc).isoformat()
print(now)   # "2026-05-04T12:00:00+00:00"
