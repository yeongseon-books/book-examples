from conftest import load_module


run = load_module("ko/01-platform-architecture/step01_architecture_map.py", "ep01").run


def test_ep01_has_expected_platform_boxes() -> None:
    result = run()
    assert result["front_end"].startswith("App Service Front-End")
    assert "Worker" in result["worker"]
    assert "/home" in result["storage"]
    assert "Kudu" in result["scm"]
