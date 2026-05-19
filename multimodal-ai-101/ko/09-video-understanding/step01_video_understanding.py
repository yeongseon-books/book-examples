from common import MockImageEncoder, VideoSummarizer, synthetic_image


def run() -> int:
    encoder = MockImageEncoder()
    frames = [encoder.encode(synthetic_image(i)) for i in range(9, 12)]
    clip = VideoSummarizer().pool(frames, mode="mean")
    return int(clip.shape[0])
