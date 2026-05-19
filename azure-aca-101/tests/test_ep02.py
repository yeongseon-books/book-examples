from conftest import load_module

mod = load_module("ko/02-environment-app-revision/step01_revision_model.py", "ep02")


def test_ep02_revision_rules() -> None:
    assert mod.classify_change("image") == "new_revision"
    assert mod.classify_change("traffic") == "same_revision"
    data = mod.run()
    assert data["weights"] == {"myapi--v1": 90, "myapi--v2": 10}
