"""Generated from book-content article."""

from threading import RLock
from typing import Any, Dict, List


class SharedMemory:
    """Shared memory."""

    def __init__(self):
        self.data: dict[str, Any] = {}
        self.lock = RLock()
        self.access_log: list[dict] = []

    def write(self, key: str, value: Any, agent_name: str) -> None:
        """Write data."""
        with self.lock:
            old_value = self.data.get(key)
            self.data[key] = value
            self.access_log.append({
                "agent": agent_name,
                "operation": "write",
                "key": key,
                "old_value": old_value,
                "new_value": value,
                "timestamp": datetime.now().isoformat()
            })

    def read(self, key: str, agent_name: str) -> Any:
        """Read data."""
        with self.lock:
            value = self.data.get(key)
            self.access_log.append({
                "agent": agent_name,
                "operation": "read",
                "key": key,
                "value": value,
                "timestamp": datetime.now().isoformat()
            })
            return value

    def delete(self, key: str, agent_name: str) -> None:
        """Delete data."""
        with self.lock:
            if key in self.data:
                old_value = self.data[key]
                del self.data[key]
                self.access_log.append({
                    "agent": agent_name,
                    "operation": "delete",
                    "key": key,
                    "old_value": old_value,
                    "timestamp": datetime.now().isoformat()
                })

    def get_history(self, key: str = None) -> list[dict]:
        """View access history."""
        with self.lock:
            if key:
                return [log for log in self.access_log if log.get("key") == key]
            return list(self.access_log)

# Example usage
shared_mem = SharedMemory()

# AgentA executes a task
shared_mem.write("task_result", {"status": "completed"}, "AgentA")

# AgentB reads AgentA's result and continues work
result = shared_mem.read("task_result", "AgentB")
print(f"AgentB read: {result}")

# View memory access history
history = shared_mem.get_history("task_result")
for log in history:
    print(log)
