from pathlib import Path
from conftest import load_episode


def test_ep10_production_harness_pipeline(tmp_path: Path):
    m = load_episode('ko', '10-production-harness')
    result = m.production_harness_example(tmp_path / 'prod.jsonl')
    assert result['status'] == 'ok'
    assert result['tool']['value'].startswith('resolved:')
    assert len(result['context']) <= 3
