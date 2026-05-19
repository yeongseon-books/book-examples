from ko import _09_incident_and_oncall as ep09


def test_rotation_excludes_vacation_and_postmortem_sections() -> None:
    selected = ep09.pick_oncall(['alice', 'bob', 'carol'], vacation={'bob'}, offset=1)
    assert selected == 'carol'

    doc = ep09.build_postmortem(
        title='API outage',
        impact='12 minutes 5xx spike',
        timeline=[ep09.IncidentEvent('03:11', 'alert', 'pager triggered')],
        root_cause='Canary config typo',
        actions=['Add canary checklist'],
    )
    assert '## Impact' in doc
    assert '## Timeline' in doc
    assert '## Root Cause' in doc
    assert '## Action Items' in doc
