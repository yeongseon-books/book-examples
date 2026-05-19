from en import ep09_dependency_vuln


def test_ep09_dep_scan():
    result = ep09_dependency_vuln.run_demo()
    assert result.insecure_detected
    assert result.safe_ok
