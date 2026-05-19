from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Call:
    service: str
    action: str
    payload: dict[str, object]


class MockCloud:
    def __init__(self) -> None:
        self.calls: list[Call] = []

    def record(self, service: str, action: str, **payload: object) -> dict[str, object]:
        call = Call(service=service, action=action, payload=payload)
        self.calls.append(call)
        return {"ok": True, "service": service, "action": action, "payload": payload}


def latest_call(mock: MockCloud) -> Call:
    if not mock.calls:
        raise RuntimeError("no recorded calls")
    return mock.calls[-1]
