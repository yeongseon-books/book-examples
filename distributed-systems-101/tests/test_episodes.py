"""Tests for episodes in Distributed Systems 101."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_ko(slug: str):
    """Load ko."""
    path = ROOT / "ko" / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ep01_latency_visible() -> None:
    """Test ep01 latency visible."""
    result = load_ko("01-what-is-a-distributed-system").run_demo()
    assert result["sent"] is True
    assert result["delivered_before"] == 0
    assert result["delivered_after"] == 1


def test_ep02_omission_and_partition() -> None:
    """Test ep02 omission and partition."""
    result = load_ko("02-failure-model").run_demo()
    assert result == {"omission": True, "partition": True}


def test_ep03_rpc_and_queue_models() -> None:
    """Test ep03 rpc and queue models."""
    result = load_ko("03-rpc-and-message-passing").run_demo()
    assert result["rpc"] == 7
    assert result["message_task"] == "ship-order"


def test_ep04_cp_rejects_partition_write() -> None:
    """Test ep04 cp rejects partition write."""
    result = load_ko("04-consistency-and-cap").run_demo()
    assert result["normal_write"] is True
    assert result["partition_write"] is False


def test_ep05_replication_shows_stale_read_and_quorum() -> None:
    """Test ep05 replication shows stale read and quorum."""
    result = load_ko("05-replication").run_demo()
    assert result["stale_read"] is None
    assert result["quorum_acks"] == 2


def test_ep06_raft_commits_after_replication() -> None:
    """Test ep06 raft commits after replication."""
    result = load_ko("06-consensus-and-raft").run_demo()
    assert result["role"] == "leader"
    assert result["term"] == 1
    assert result["commit_index"] == 0


def test_ep07_leader_election_converges() -> None:
    """Test ep07 leader election converges."""
    result = load_ko("07-leader-election").run_demo()
    assert result["leader"] == "a"
    assert result["stale_rejected"] is True


def test_ep08_event_replay_restores_state() -> None:
    """Test ep08 event replay restores state."""
    result = load_ko("08-message-queue-and-event-sourcing").run_demo()
    assert result["message_type"] == "order-created"
    assert result["balance"] == 70


def test_ep09_2pc_rolls_back_on_prepare_failure() -> None:
    """Test ep09 2pc rolls back on prepare failure."""
    result = load_ko("09-distributed-transaction").run_demo()
    assert result["committed"] is False
    assert result["states"] == ["rolled_back", "aborted"]


def test_ep10_circuit_breaker_opens_after_failures() -> None:
    """Test ep10 circuit breaker opens after failures."""
    result = load_ko("10-operable-distributed-patterns").run_demo()
    assert result["errors"] == 3
    assert result["open"] is True
