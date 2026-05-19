from ko import _08_container_security as ep


def test_scan_flags_root_and_latest():
    dockerfile = "\n".join(
        ["FROM python:latest", "USER root", "ENV DB_PASSWORD=secret123"]
    )
    issues = ep.scan_security(dockerfile, "myorg/app:latest")
    assert any("root" in issue.lower() for issue in issues)
    assert any("latest" in issue.lower() for issue in issues)


def test_scan_flags_sensitive_ports():
    issues = ep.scan_security("FROM x\nEXPOSE 22\nUSER app", "x:1.0")
    assert any("Sensitive port exposed" == issue for issue in issues)
