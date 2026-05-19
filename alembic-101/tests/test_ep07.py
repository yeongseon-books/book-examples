# pyright: reportUnknownParameterType=false, reportMissingParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
def test_ep07_online_offline(load_module):
    m = load_module("ko/07-online-vs-offline-and-batch/step01_online_offline_batch.py", "ep07")
    sql = m.render_upgrade_sql("a1", "b1")
    assert "BEGIN;" in sql and "COMMIT;" in sql
    assert m.requires_batch("sqlite") is True
