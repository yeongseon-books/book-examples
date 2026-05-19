from common import HPAController


def test_ep08_hpa_scales_up_on_high_cpu():
    desired = HPAController().desired_replicas(
        3, current_cpu=90, target_cpu=60, min_replicas=2, max_replicas=10
    )
    assert desired == 5
