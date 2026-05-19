from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AppServiceLayers:
    front_end: str
    worker: str
    storage: str
    scm: str


def architecture_layers() -> AppServiceLayers:
    return AppServiceLayers(
        front_end="App Service Front-End + ARR",
        worker="Worker instances in an App Service Plan",
        storage="Shared /home content store",
        scm="Kudu SCM buddy site",
    )


def build_arr_routing_headers(enable_affinity: bool) -> dict[str, str]:
    headers = {"x-app-host": "my-app.azurewebsites.net"}
    if enable_affinity:
        headers["Cookie"] = "ARRAffinity=worker-2"
    return headers


def sandbox_constraints(os_type: str) -> dict[str, object]:
    if os_type == "windows":
        return {
            "boundary": "iis-w3wp-sandbox",
            "registry_write_allowed": False,
            "gdi_restricted": True,
        }
    if os_type == "linux":
        return {
            "boundary": "container",
            "registry_write_allowed": False,
            "gdi_restricted": False,
            "startup_contract": [
                "WEBSITE_WARMUP_PATH",
                "WEBSITES_CONTAINER_START_TIME_LIMIT",
            ],
        }
    raise ValueError("unsupported os_type")


def zipdeploy_command(app_name: str, resource_group: str, zip_path: str) -> str:
    return (
        "az webapp deployment source config-zip "
        f"-n {app_name} -g {resource_group} --src {zip_path}"
    )


def run_from_package_enabled(app_settings: dict[str, str]) -> bool:
    return app_settings.get("WEBSITE_RUN_FROM_PACKAGE", "0") in {"1", "true", "True"}


def autoscale_decision(
    metrics: dict[str, float],
    *,
    out_threshold: float = 70.0,
    in_threshold: float = 30.0,
) -> str:
    cpu = metrics.get("cpu", 0.0)
    queue = metrics.get("http_queue", 0.0)
    if cpu >= out_threshold or queue >= 100.0:
        return "scale_out"
    if cpu <= in_threshold and queue <= 10.0:
        return "scale_in"
    return "hold"


def warmup_is_ready(status_code: int, allowed_statuses: set[int]) -> bool:
    return status_code in allowed_statuses
