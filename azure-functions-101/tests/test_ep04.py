from conftest import run_script


def test_ep04() -> None:
    output = run_script("ko/04-first-deploy/step01_deploy_plan.py")
    assert "func azure functionapp publish" in output
