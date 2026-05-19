# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep03_upgrade_downgrade(load_module):
    m = load_module("ko/03-first-revision-upgrade-downgrade/step01_upgrade_downgrade.py", "ep03")
    out = m.apply_upgrade_and_downgrade()
    assert out["upgrade_cols"] == 3
    assert out["downgrade_cols"] == 2
