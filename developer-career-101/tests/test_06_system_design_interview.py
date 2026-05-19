from tests.test_01_what_is_developer_career import load


def test_06_url_shortener_spec_has_required_sections():
    mod = load("06-system-design-interview.py")
    spec = mod.generate_spec("design url shortener")
    assert mod.is_complete_spec(spec)
