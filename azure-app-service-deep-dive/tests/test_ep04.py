"""Tests for ep04 in Azure App Service Deep Dive."""

from conftest import load_module

build_deploy_plan = load_module(
    "ko/04-deployment-and-kudu/step01_deploy_contract.py", "ep04"
).build_deploy_plan


def test_ep04_zipdeploy_string_and_run_from_package_mode() -> None:
    """Test ep04 zipdeploy string and run from package mode."""
    plan = build_deploy_plan(
        app_name="my-app",
        resource_group="my-rg",
        zip_path="release.zip",
        app_settings={"WEBSITE_RUN_FROM_PACKAGE": "1"},
    )
    assert plan["run_from_package"] is True
    assert plan["target_mode"] == "readonly-mount-wwwroot"
    assert "config-zip" in str(plan["zipdeploy_cmd"])
