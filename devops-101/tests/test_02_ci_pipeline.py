from xml.etree import ElementTree

from common import MockCommandRunner
from ko import _02_ci_pipeline as ep02


def test_pipeline_halts_on_first_failure_and_xml_is_valid() -> None:
    runner = MockCommandRunner({'lint': (1, '', 'lint failed'), 'test': (0, 'ok', ''), 'build': (0, 'ok', '')})
    pipeline = ep02.Pipeline([ep02.Stage('lint', 'lint'), ep02.Stage('test', 'test'), ep02.Stage('build', 'build')], runner)
    result = pipeline.run()
    assert result['status'] == 'failed'
    assert len(result['results']) == 1
    root = ElementTree.fromstring(result['junit_xml'])
    assert root.tag == 'testsuite'
