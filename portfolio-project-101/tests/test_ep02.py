from ko.ep02_trait_checklist import validate_project_traits


def test_ep02_trait_validator() -> None:
    ok, missing = validate_project_traits(
        {"solving_real_problem": True, "scoped": True, "deployable": False}
    )
    assert ok is False
    assert missing == ["deployable"]
