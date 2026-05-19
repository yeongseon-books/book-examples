from en.ep08_toil_roi import automation_roi, toil_hours


def test_ep08_toil_roi():
    assert toil_hours(30, 10) == 5
    assert automation_roi(5, 10) == 26
