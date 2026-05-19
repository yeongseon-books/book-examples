from conftest import load_episode


def test_ep06_test_harness_records_pass_fail():
    m = load_episode('ko', '06-test-harness')
    rows = m.test_harness_example()
    assert rows[0]['passed'] is True
    assert rows[0]['name'] == 'json-case'
