# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep05_branch_merge(load_module):
    m = load_module("ko/05-branches-and-merges/step01_branch_merge.py", "ep05")
    node = m.merge_heads("a", "b", "merge1")
    assert m.is_multi_head(["a", "b"]) is True
    assert node["down_revisions"] == ("a", "b")
