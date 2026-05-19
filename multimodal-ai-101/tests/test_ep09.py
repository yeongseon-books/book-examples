from conftest import load_module

run = load_module("ko/09-video-understanding/step01_video_understanding.py", "ep09").run


def test_ep09_video_pooling_vector_dim() -> None:
    assert run() == 512
