from __future__ import annotations

from fastapi import FastAPI

app = FastAPI()


def control_plane_model() -> dict[str, list[str]]:
    return {
        "control_plane": [
            "kube-apiserver",
            "etcd",
            "kube-scheduler",
            "kube-controller-manager",
        ],
        "data_plane": ["kubelet", "containerd"],
    }


def az_show_command(cluster_name: str, resource_group: str) -> str:
    return (
        f"az aks show -n {cluster_name} -g {resource_group} "
        "--query '{kubernetes:kubernetesVersion, sku:sku, apiServer:apiServerAccessProfile}'"
    )


@app.get("/control-plane")
def read_control_plane() -> dict[str, object]:
    return {
        "managed_by": "microsoft",
        "observable_surface": "kube-apiserver",
        "model": control_plane_model(),
    }
