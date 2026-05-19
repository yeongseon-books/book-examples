# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep04_autogen_limits(load_module):
    m = load_module("ko/04-autogenerate-and-its-limits/step01_autogenerate_limits.py", "ep04")
    assert m.classify_autogen_change({"kind": "add_column"}) == "safe-auto"
    assert m.classify_autogen_change({"kind": "rename_column"}) == "manual-required"
    assert m.compare_options()["compare_type"]
