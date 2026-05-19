"""Azure Aks Deep Dive - Episode 1: Kubelet cri path."""

from __future__ import annotations


def cri_call_sequence() -> list[str]:
    """Cri call sequence."""
    return ["RunPodSandbox", "PullImage", "CreateContainer", "StartContainer"]


def runtime_chain() -> list[str]:
    """Runtime chain."""
    return ["kubelet", "containerd", "containerd-shim", "runc", "process"]


def debug_node_command(node_name: str) -> str:
    """Debug node command."""
    return (
        f"kubectl debug node/{node_name} -it "
        "--image=mcr.microsoft.com/cbl-mariner/busybox:2.0 -- chroot /host"
    )
