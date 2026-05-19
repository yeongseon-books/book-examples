from common import ClusterStateSimulator, ManifestParser
from pathlib import Path


def test_ep10_cluster_apply_delete_cycle():
    pod = ManifestParser().parse(Path('ko/10-kubernetes-in-operation/ops.yaml').read_text())[0]
    cluster = ClusterStateSimulator()
    cluster.apply(pod)
    assert cluster.get('Pod', 'web') is not None
    cluster.delete('Pod', 'web')
    assert cluster.get('Pod', 'web') is None
