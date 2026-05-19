"""Secure Coding 101 - Episode 9: Dependency vuln."""

from common import assert_demo

FAKE_CVE_DB = {
    "flask": {"0.12", "1.0"},
    "requests": {"2.19.0"},
}


def insecure_accept_all(requirements_text: str) -> bool:
    """Insecure accept all."""
    return True


def parse_requirements(requirements_text: str) -> list[tuple[str, str]]:
    """Parse requirements."""
    items = []
    for line in requirements_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "==" not in line:
            continue
        name, ver = line.split("==", 1)
        items.append((name.lower(), ver))
    return items


def find_vulnerable(requirements_text: str) -> list[str]:
    """Find vulnerable."""
    bad = []
    for name, ver in parse_requirements(requirements_text):
        if ver in FAKE_CVE_DB.get(name, set()):
            bad.append(f"{name}=={ver}")
    return bad


def run_demo():
    """Run demo."""
    reqs = "flask==0.12\nrequests==2.31.0"
    insecure_detected = insecure_accept_all(reqs) is True
    safe_ok = find_vulnerable(reqs) == ["flask==0.12"]
    return assert_demo(insecure_detected, safe_ok)
