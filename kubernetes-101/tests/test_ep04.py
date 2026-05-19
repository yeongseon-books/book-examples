from common import ServiceResolver, ManifestParser
from pathlib import Path


def test_ep04_service_selector_matches_pods():
    svc = ManifestParser().parse(Path('ko/04-service/service.yaml').read_text())[0]
    pods = [
        {'metadata': {'name': 'p1', 'labels': {'app': 'web'}}},
        {'metadata': {'name': 'p2', 'labels': {'app': 'api'}}},
    ]
    matched = ServiceResolver().match_pods(svc, pods)
    assert [p['metadata']['name'] for p in matched] == ['p1']
