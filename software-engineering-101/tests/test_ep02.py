from pathlib import Path
from en.ep02_invest import invest_checklist


def test_ep02_invest_scores():
    rows = invest_checklist(Path('fixtures/ep02_user_stories.md').read_text(encoding='utf-8'))
    assert len(rows) == 2
    assert rows[0]['score'] >= 5
