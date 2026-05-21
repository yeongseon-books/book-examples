"""Incident Response 101 - 4편: communication 예제."""

from common import CommsTemplateRenderer, Incident


def run() -> dict[str, str]:
    """Run."""
    inc = Incident(id="INC-004", title="search latency", severity="SEV2")
    renderer = CommsTemplateRenderer()
    return {
        "internal": renderer.render("internal", inc, "Investigating elevated p95."),
        "customer": renderer.render("customer", inc, "Some users may see delays."),
        "stakeholder": renderer.render("stakeholder", inc, "Next update in 30 min."),
    }


if __name__ == "__main__":
    print(run())
