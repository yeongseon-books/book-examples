"""Generated from book-content article."""

import threading
from collections import defaultdict, deque
from collections.abc import Callable
from typing import Dict, List


class MessageBroker:
    """A message broker."""

    def __init__(self):
        self.queues: dict[str, deque] = defaultdict(deque)
        self.handlers: dict[str, Callable] = {}
        self.lock = threading.Lock()
        self.running = False

    def register_agent(self, agent_name: str, handler: Callable) -> None:
        """Register an agent and its message handler."""
        with self.lock:
            self.handlers[agent_name] = handler
            if agent_name not in self.queues:
                self.queues[agent_name] = deque()

    def send(self, message: Message) -> None:
        """Send a message."""
        with self.lock:
            self.queues[message.receiver].append(message)

    def start(self) -> None:
        """Start the broker."""
        self.running = True
        threading.Thread(target=self._dispatch_loop, daemon=True).start()

    def stop(self) -> None:
        """Stop the broker."""
        self.running = False

    def _dispatch_loop(self) -> None:
        """Message dispatch loop."""
        import time
        while self.running:
            with self.lock:
                for agent_name, queue in self.queues.items():
                    if queue and agent_name in self.handlers:
                        message = queue.popleft()
                        try:
                            self.handlers[agent_name](message)
                        except Exception as e:
                            error_msg = Message(
                                sender="broker",
                                receiver=message.sender,
                                message_type=MessageType.ERROR,
                                content=str(e),
                                correlation_id=message.correlation_id
                            )
                            self.queues[message.sender].append(error_msg)
            time.sleep(0.01)

# Example usage
broker = MessageBroker()

def agent_a_handler(msg: Message):
    print(f"AgentA received: {msg.content}")

def agent_b_handler(msg: Message):
    print(f"AgentB received: {msg.content}")

# Register agents
broker.register_agent("AgentA", agent_a_handler)
broker.register_agent("AgentB", agent_b_handler)

# Start broker
broker.start()

# Send messages
broker.send(Message(
    sender="AgentA",
    receiver="AgentB",
    message_type=MessageType.REQUEST,
    content="Please analyze this data"
))

# Wait for processing
import time

time.sleep(1)
broker.stop()
