from common import MockAudioEncoder, synthetic_audio


def run() -> float:
    vec = MockAudioEncoder().encode(synthetic_audio())
    return float((vec**2).sum() ** 0.5)
