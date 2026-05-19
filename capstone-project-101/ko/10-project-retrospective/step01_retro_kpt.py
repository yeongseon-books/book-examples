from __future__ import annotations
from common import kpt_actionability

def run() -> dict[str, object]:
    kpt = {'keep': ['scope_first'], 'problem': ['no_ci'], 'try': ['add_ci_template']}
    actions = [{'who': 'A', 'what': 'add_ci', 'by': 'next_sprint'}]
    return {'kpt': kpt, 'metrics': {'velocity': 12, 'bugs': 5, 'review_time': 1.5}, 'whys': ['bug_at_demo', 'missed_test', 'no_ci', 'no_template', 'first_time'], 'actions': actions, 'lessons': ['scope_first', 'ci_early', 'demo_dryrun'], 'actionable': kpt_actionability(kpt, actions)}

if __name__ == '__main__':
    print(run())
