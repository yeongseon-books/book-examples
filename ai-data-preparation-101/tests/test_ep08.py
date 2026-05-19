from conftest import run_dict


def test_ep08_augmentation() -> None:
    result = run_dict("ko/08-data-augmentation/step01_light_augmentation.py")
    assert str(result["source"]) != ""
    assert str(result["augmented"]) != ""
