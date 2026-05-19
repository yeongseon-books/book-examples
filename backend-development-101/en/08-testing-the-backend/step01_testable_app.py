"""Episode 08: Test-friendly app with dependency override."""

from fastapi import Depends, FastAPI
from pydantic import BaseModel


class MessageIn(BaseModel):
    """Message in."""

    text: str


class Sink:
    """Sink."""

    def __init__(self):
        self.events: list[str] = []

    def publish(self, event: str) -> None:
        """Publish."""
        self.events.append(event)


def get_sink() -> Sink:
    """Get sink."""
    return Sink()


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()

    @app.post("/messages")
    def create_message(payload: MessageIn, sink: Sink = Depends(get_sink)):
        """Create message."""
        sink.publish(f"message:{payload.text}")
        return {"stored": payload.text, "event_count": len(sink.events)}

    return app
