from ko import _07_monitoring_and_alerting as ep07


def test_alert_rule_threshold_above_and_below() -> None:
    store = ep07.MetricStore(window=3)
    for sample in [0.02, 0.03, 0.025]:
        store.observe('error_rate', sample)
    fire = ep07.AlertRule('error_rate', threshold=0.01)
    assert fire.evaluate(store) is True

    calm_store = ep07.MetricStore(window=3)
    for sample in [0.001, 0.002, 0.0015]:
        calm_store.observe('error_rate', sample)
    assert fire.evaluate(calm_store) is False
