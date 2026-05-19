"""Azure App Service Deep Dive - Episode 1: Deploy contract."""

from __future__ import annotations

from common import run_from_package_enabled, zipdeploy_command


def build_deploy_plan(
    app_name: str, resource_group: str, zip_path: str, app_settings: dict[str, str]
) -> dict[str, str | bool]:
    # az 명령은 문자열만 생성하고 실행하지 않습니다.
    """Build deploy plan."""
    command = zipdeploy_command(app_name, resource_group, zip_path)
    mounted = run_from_package_enabled(app_settings)
    target = "readonly-mount-wwwroot" if mounted else "sync-to-wwwroot"
    return {
        "zipdeploy_cmd": command,
        "target_mode": target,
        "run_from_package": mounted,
    }
