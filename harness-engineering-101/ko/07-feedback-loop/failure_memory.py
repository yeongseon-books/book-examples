"""Generated from book-content article."""

from datetime import datetime
import json
from pathlib import Path

@dataclass
class FailureRecord:
    task_type: str
    failed_approach: str
    failure_reason: str
    timestamp: str
    fixed_in_next_attempt: bool

class FailureMemory:
    """Accumulates failure records per task type."""

    def __init__(self, store_path: Path):
        self.store_path = store_path
        self.records: list[FailureRecord] = self._load()

    def _load(self) -> list[FailureRecord]:
        if not self.store_path.exists():
            return []
        data = json.loads(self.store_path.read_text())
        return [FailureRecord(**r) for r in data]

    def add(self, record: FailureRecord) -> None:
        self.records.append(record)
        self.store_path.write_text(json.dumps([r.__dict__ for r in self.records], indent=2))

    def warnings_for(self, task_type: str, recent: int = 5) -> list[str]:
        relevant = [r for r in self.records if r.task_type == task_type][-recent:]
        return [f"Previously failed: {r.failed_approach} (reason: {r.failure_reason})" for r in relevant]
