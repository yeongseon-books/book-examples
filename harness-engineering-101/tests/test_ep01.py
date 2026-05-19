from conftest import load_episode


def test_ep01_mock_llm_baseline():
    m = load_episode('ko', '01-what-is-harness-engineering')
    out = m.what_is_harness_engineering_example()
    assert out['answer'] == 'ok'
