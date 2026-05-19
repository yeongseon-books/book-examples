from conftest import load_module


def test_ep03_cluster_bootstrap_command_flow() -> None:
    ko = load_module(
        "ko/03-first-cluster-and-deploy/step01_first_cluster_commands.py", "ep03_ko"
    )
    en = load_module(
        "en/03-first-cluster-and-deploy/step01_first_cluster_commands.py", "ep03_en"
    )
    for module in (ko, en):
        flow = module.build_bootstrap_flow()
        assert flow["create_cluster"][0:3] == ["az", "aks", "create"]
        assert flow["add_user_pool"][0:3] == ["az", "aks", "nodepool"]
        assert "get-credentials" in flow["get_credentials"]
