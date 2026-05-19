"""Tests for ep02 in Azure Aks Deep Dive."""

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


def test_kubelet_cri_call_sequence_ko() -> None:
    """Test kubelet cri call sequence ko."""
    module = load_module(
        "ko/02-kubelet-and-containerd/step01_kubelet_cri_path.py", "ep02_ko"
    )
    assert module.cri_call_sequence() == [
        "RunPodSandbox",
        "PullImage",
        "CreateContainer",
        "StartContainer",
    ]


def test_runtime_chain_and_debug_command_en() -> None:
    """Test runtime chain and debug command en."""
    module = load_module(
        "en/02-kubelet-and-containerd/step01_kubelet_cri_path.py", "ep02_en"
    )
    assert module.runtime_chain()[0] == "kubelet"
    assert "kubectl debug node/aks-node" in module.debug_node_command("aks-node")
