"""Generated from book-content article."""

import av
import numpy as np
from PIL import Image

def sample_uniform_frames(path: str, n_frames: int = 8) -> list[Image.Image]:
    container = av.open(path)
    stream = container.streams.video[0]
    total = stream.frames or int(stream.duration * stream.average_rate)
    indices = np.linspace(0, total - 1, n_frames).astype(int)

    frames = []
    target_set = set(indices.tolist())
    for i, frame in enumerate(container.decode(stream)):
        if i in target_set:
            frames.append(frame.to_image())
            if len(frames) == n_frames:
                break
    container.close()
    return frames

frames = sample_uniform_frames("clip.mp4", n_frames=8)
print(f"sampled {len(frames)} frames, first size = {frames[0].size}")
