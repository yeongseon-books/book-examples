from common import ep04_race_condition


def test_ep04_race_condition_structural_properties():
    out = ep04_race_condition(num_threads=10, increments=500)
    assert out["safe"] == out["expected"]
    assert out["unsafe"] < out["expected"]
