from common import ep06_bump_version


def test_ep06_semver_bump_minor_with_prerelease() -> None:
    assert ep06_bump_version("1.2.3", "minor", prerelease="beta.1") == "1.3.0-beta.1"
