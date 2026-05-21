"""Generated from book-content article."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional


class MessageType(Enum):
    """Message types."""
    REQUEST = "request"
    RESPONSE = "response"
    NOTIFICATION = "notification"
    ERROR = "error"

@dataclass
class Message:
    """Standard message format."""
    sender: str
    receiver: str
    message_type: MessageType
    content: Any
    correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.message_type.value,
            "content": self.content,
            "correlation_id": self.correlation_id,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Message":
        """Create from a dictionary."""
        return cls(
            sender=data["sender"],
            receiver=data["receiver"],
            message_type=MessageType(data["type"]),
            content=data["content"],
            correlation_id=data["correlation_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            metadata=data.get("metadata", {})
        )

# Example usage
msg = Message(
    sender="AgentA",
    receiver="AgentB",
    message_type=MessageType.REQUEST,
    content={"action": "analyze", "data": "sample.csv"},
    metadata={"priority": "high"}
)

# JSON serialization (for network transport)
import json

serialized = json.dumps(msg.to_dict())

# Deserialize on the receiving end
received = Message.from_dict(json.loads(serialized))
