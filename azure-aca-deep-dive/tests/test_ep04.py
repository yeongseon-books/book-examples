from conftest import load_module

run = load_module("ko/04-keda-in-aca/step01_keda_translation.py", "ep04").run


def test_ep04_keda_translation_shape() -> None:
    result = run()
    assert result["episode"] == 4
    assert result["plan"]["keda_shape"]["minReplicas"] == 0
    assert result["plan"]["keda_shape"]["trigger"]["type"] == "azure-queue"
