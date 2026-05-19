from __future__ import annotations

from dataclasses import dataclass
from xml.etree.ElementTree import Element, SubElement, tostring

from common import MockCommandRunner


@dataclass
class Stage:
    name: str
    command: str


class Pipeline:
    def __init__(self, stages: list[Stage], runner: MockCommandRunner) -> None:
        self.stages = stages
        self.runner = runner

    def run(self) -> dict[str, object]:
        results: list[dict[str, object]] = []
        status = 'passed'
        for stage in self.stages:
            code, out, err = self.runner.run(stage.command)
            item = {'name': stage.name, 'code': code, 'stdout': out, 'stderr': err}
            results.append(item)
            if code != 0:
                status = 'failed'
                break
        return {'status': status, 'results': results, 'junit_xml': self._to_junit(results)}

    def _to_junit(self, results: list[dict[str, object]]) -> str:
        suite = Element('testsuite', attrib={'name': 'ci-pipeline', 'tests': str(len(results))})
        failures = 0
        for result in results:
            case = SubElement(suite, 'testcase', attrib={'name': str(result['name'])})
            if int(result['code']) != 0:
                failures += 1
                fail = SubElement(case, 'failure', attrib={'message': 'stage failed'})
                fail.text = str(result['stderr'])
        suite.set('failures', str(failures))
        return tostring(suite, encoding='unicode')
