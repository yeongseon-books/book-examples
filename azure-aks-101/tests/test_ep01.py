from conftest import load_module


def test_ep01_aks_summary_tokens_and_responsibilities() -> None:
    ko = load_module("ko/01-what-is-aks/step01_aks_summary.py", "ep01_ko")
    en = load_module("en/01-what-is-aks/step01_aks_summary.py", "ep01_en")
    for module in (ko, en):
        data = module.build_example()
        assert data["control_plane_managed_by"] == "azure"
        assert data["command_tokens"][:3] == ["az", "aks", "create"]
        assert "node_pool" in data["user_responsibility"]
