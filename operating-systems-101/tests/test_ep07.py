from common import ep07_page_replacement


def test_ep07_page_faults():
    ref = [7, 0, 1, 2, 0, 3, 0, 4]
    out = ep07_page_replacement(ref, frame_size=3)
    assert out["fifo_faults"] >= out["lru_faults"]
    assert out["lru_faults"] > 0
