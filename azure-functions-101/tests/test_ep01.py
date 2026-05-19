from conftest import run_script


def test_ep01() -> None:
    output = run_script("ko/01-what-is-azure-functions/step01_hello_http.py")
    assert "Hello, Sisyphus!" in output
