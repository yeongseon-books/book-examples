from conftest import load_module

run = load_module("ko/06-audio-whisper/step01_audio_encoder.py", "ep06").run


def test_ep06_audio_encoder_norm() -> None:
    assert abs(run() - 1.0) < 1e-6
