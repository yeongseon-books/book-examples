"""Tests for ep04 in Azure Aks Deep Dive."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str, module_name: str):
    """Load module."""
    spec = importlib.util.spec_from_file_location(module_name, ROOT / relative_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_scheduler_filters_tainted_nodes_ko() -> None:
    """Test scheduler filters tainted nodes ko."""
    module = load_module(
        "ko/04-scheduler-and-pod-placement/step01_scheduler_decision.py", "ep04_ko"
    )
    nodes = [
        {"name": "n1", "free_cpu": 2, "pod_count": 1, "tainted": True},
        {"name": "n2", "free_cpu": 4, "pod_count": 1, "tainted": False},
    ]
    assert module.choose_node(nodes, 2) == "n2"


def test_scheduler_returns_none_when_no_feasible_en() -> None:
    """Test scheduler returns none when no feasible en."""
    module = load_module(
        "en/04-scheduler-and-pod-placement/step01_scheduler_decision.py", "ep04_en"
    )
    nodes = [{"name": "n1", "free_cpu": 1, "pod_count": 1, "tainted": False}]
    assert module.choose_node(nodes, 2) is None
