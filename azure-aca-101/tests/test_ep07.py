from conftest import load_module

run = load_module(
    "ko/07-monitoring-and-ops/step01_observability_queries.py", "ep07"
).run


def test_ep07_observability_outputs() -> None:
    data = run()
    assert data["errors"]["myapi--v2"] == 2
    assert "ContainerAppConsoleLogs_CL" in data["kql"][0]
    assert "summarize ErrorCount=count()" in data["kql"][1]
