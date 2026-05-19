from common import VolumeBinder, ManifestParser
from pathlib import Path


def test_ep07_pv_pvc_binding():
    docs = ManifestParser().parse(Path('ko/07-volume/volume.yaml').read_text())
    pv, pvc = docs[0], docs[1]
    assert VolumeBinder().bind([pv], pvc) == 'pv-gp3-10'
