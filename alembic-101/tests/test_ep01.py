# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep01_init(load_module):
    m = load_module("ko/01-why-alembic-and-init/step01_why_init.py", "ep01")
    out = m.run_init_demo()
    assert out["mental_model"] == "git-for-schema"
    assert out["version"] == "0001_init"
