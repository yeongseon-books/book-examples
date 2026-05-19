from __future__ import annotations

import heapq
import random
from collections import deque
from dataclasses import dataclass, field
from typing import Any


class SimulatedClock:
    def __init__(self) -> None:
        self.now_ms = 0

    def tick(self, ms: int = 1) -> int:
        self.now_ms += ms
        return self.now_ms


@dataclass(order=True)
class ScheduledMessage:
    deliver_at: int
    src: str = field(compare=False)
    dst: str = field(compare=False)
    payload: dict[str, Any] = field(compare=False)


class FakeNetwork:
    def __init__(
        self,
        clock: SimulatedClock,
        seed: int = 42,
        drop_rate: float = 0.0,
        min_latency: int = 1,
        max_latency: int = 5,
    ) -> None:
        self.clock = clock
        self.random = random.Random(seed)
        self.drop_rate = drop_rate
        self.min_latency = min_latency
        self.max_latency = max_latency
        self.partitioned: set[tuple[str, str]] = set()
        self.q: list[ScheduledMessage] = []

    def block(self, a: str, b: str) -> None:
        self.partitioned.add((a, b))
        self.partitioned.add((b, a))

    def unblock(self, a: str, b: str) -> None:
        self.partitioned.discard((a, b))
        self.partitioned.discard((b, a))

    def send(self, src: str, dst: str, payload: dict[str, Any]) -> bool:
        if (src, dst) in self.partitioned:
            return False
        if self.random.random() < self.drop_rate:
            return False
        latency = self.random.randint(self.min_latency, self.max_latency)
        heapq.heappush(
            self.q, ScheduledMessage(self.clock.now_ms + latency, src, dst, payload)
        )
        return True

    def deliver_ready(self) -> list[ScheduledMessage]:
        out: list[ScheduledMessage] = []
        while self.q and self.q[0].deliver_at <= self.clock.now_ms:
            out.append(heapq.heappop(self.q))
        return out


class KVStore:
    def __init__(self) -> None:
        self.data: dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self.data[key] = value

    def get(self, key: str) -> Any:
        return self.data.get(key)


class ReplicaSet:
    def __init__(self, node_ids: list[str]) -> None:
        self.primary = node_ids[0]
        self.nodes = {node_id: KVStore() for node_id in node_ids}

    def write_async(
        self, key: str, value: Any, lagging: set[str] | None = None
    ) -> None:
        lagging = lagging or set()
        self.nodes[self.primary].put(key, value)
        for node_id, store in self.nodes.items():
            if node_id == self.primary or node_id in lagging:
                continue
            store.put(key, value)

    def write_sync(self, key: str, value: Any) -> None:
        for store in self.nodes.values():
            store.put(key, value)

    def write_quorum(self, key: str, value: Any, w: int) -> int:
        acks = 0
        for store in self.nodes.values():
            store.put(key, value)
            acks += 1
            if acks >= w:
                break
        return acks


class RaftNode:
    def __init__(self, node_id: str) -> None:
        self.node_id = node_id
        self.term = 0
        self.role = "follower"
        self.voted_for: str | None = None
        self.log: list[tuple[int, str]] = []
        self.commit_index = -1

    def become_candidate(self) -> None:
        self.term += 1
        self.role = "candidate"
        self.voted_for = self.node_id

    def become_leader(self) -> None:
        self.role = "leader"

    def append_entry(self, command: str) -> None:
        self.log.append((self.term, command))

    def commit_to(self, index: int) -> None:
        self.commit_index = max(self.commit_index, index)


def elect_leader(node_ids: list[str], alive: set[str]) -> str | None:
    candidates = [n for n in node_ids if n in alive]
    if len(candidates) <= len(node_ids) // 2:
        return None
    return sorted(candidates)[0]


class MessageQueue:
    def __init__(self) -> None:
        self.q: deque[dict[str, Any]] = deque()

    def publish(self, message: dict[str, Any]) -> None:
        self.q.append(message)

    def poll(self) -> dict[str, Any] | None:
        if not self.q:
            return None
        return self.q.popleft()


class EventStore:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def append(self, event: dict[str, Any]) -> int:
        self.events.append(event)
        return len(self.events) - 1

    def replay_balance(self, account_id: str) -> int:
        balance = 0
        for event in self.events:
            if event.get("account_id") != account_id:
                continue
            if event["type"] == "credit":
                balance += int(event["amount"])
            if event["type"] == "debit":
                balance -= int(event["amount"])
        return balance


class Participant:
    def __init__(self, name: str, can_commit: bool = True) -> None:
        self.name = name
        self.can_commit = can_commit
        self.state = "init"

    def prepare(self) -> bool:
        self.state = "prepared" if self.can_commit else "aborted"
        return self.can_commit

    def commit(self) -> None:
        self.state = "committed"

    def rollback(self) -> None:
        self.state = "rolled_back"


def two_phase_commit(parts: list[Participant]) -> bool:
    if not all(p.prepare() for p in parts):
        for p in parts:
            if p.state == "prepared":
                p.rollback()
        return False
    for p in parts:
        p.commit()
    return True


class CircuitBreaker:
    def __init__(self, threshold: int = 3) -> None:
        self.threshold = threshold
        self.failures = 0
        self.open = False

    def call(self, fn: Any) -> Any:
        if self.open:
            raise RuntimeError("circuit-open")
        try:
            result = fn()
            self.failures = 0
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.threshold:
                self.open = True
            raise
