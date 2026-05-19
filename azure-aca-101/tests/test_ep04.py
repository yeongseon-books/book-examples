from conftest import load_module


mod = load_module("ko/04-ingress-and-traffic-split/step01_ingress_split.py", "ep04")


def test_ep04_ingress_modes_and_response() -> None:
    assert mod.ingress_hostname("myapi", "internal").startswith(
        "https://myapi.internal"
    )
    assert mod.ingress_hostname("myapi", "disabled") == "disabled"
    data = mod.run()
    assert data["served_by"] == "myapi--v1"
