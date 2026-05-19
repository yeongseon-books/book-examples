# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep10_team_workflow(load_module):
    m = load_module("ko/10-production-and-team-workflow/step01_team_workflow.py", "ep10")
    checks = m.ci_checks()
    assert "alembic check" in checks
    assert m.health_payload("r1", "r1")["status"] == "ok"
    assert m.health_payload("r1", "r2")["status"] == "drift"
