"""에피소드 08: 의존성 오버라이드가 가능한 테스트 친화 앱 예제입니다."""

from fastapi import Depends, FastAPI
from pydantic import BaseModel


class MessageIn(BaseModel):
    text: str


class Sink:
    def __init__(self):
        self.events: list[str] = []

    def publish(self, event: str) -> None:
        self.events.append(event)


def get_sink() -> Sink:
    return Sink()


def build_app() -> FastAPI:
    app = FastAPI()

    @app.post("/messages")
    def create_message(payload: MessageIn, sink: Sink = Depends(get_sink)):
        sink.publish(f"message:{payload.text}")
        return {"stored": payload.text, "event_count": len(sink.events)}

    return app
