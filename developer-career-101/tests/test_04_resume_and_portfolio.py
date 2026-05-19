from tests.test_01_what_is_developer_career import load


def test_04_missing_experience_flagged_and_star_detected():
    mod = load("04-resume-and-portfolio.py")
    no_exp = "## Summary\nA\n## Skills\nPython"
    result = mod.validate_resume(no_exp)
    assert "Experience" in result["missing"]

    with_star = """## Summary\nA\n## Experience\n- Cut p95 latency from 200ms to 80ms by adding caching, serving 5M req/day.\n## Skills\nPython\n## Projects\nX\n## Education\nY"""
    result2 = mod.validate_resume(with_star)
    assert result2["star_bullets"]
