# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep02_env(load_module, monkeypatch):
    m = load_module("ko/02-env-py-and-target-metadata/step01_env_target_metadata.py", "ep02")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./override.db")
    cfg = m.build_env_config()
    assert cfg["sqlalchemy.url"].endswith("override.db")
    assert cfg["render_as_batch"] is True
