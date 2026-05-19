# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep09_deploy_order(load_module):
    m = load_module("ko/09-deploy-ordering-and-blue-green/step01_deploy_ordering.py", "ep09")
    assert m.plan_deploy("add_column") == ["migration", "deploy"]
    assert m.plan_deploy("drop_column") == ["deploy", "migration"]
    assert m.blue_green_compatible("expand")
