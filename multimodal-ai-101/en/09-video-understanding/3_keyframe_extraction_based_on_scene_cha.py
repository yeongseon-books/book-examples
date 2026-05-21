"""Generated from book-content article."""

import av
import numpy as np

def extract_keyframes(path: str, threshold: float = 30.0) -> list:
    container = av.open(path)
    stream = container.streams.video[0]

    keyframes = []
    prev_hist = None
    for frame in container.decode(stream):
        img = frame.to_ndarray(format="rgb24")
        hist = np.histogram(img, bins=32, range=(0, 256))[0].astype("float32")
        hist /= hist.sum() + 1e-8

        if prev_hist is None:
            keyframes.append(frame.to_image())
        else:
            diff = np.sum((hist - prev_hist) ** 2 / (hist + prev_hist + 1e-8))
            if diff > threshold:
                keyframes.append(frame.to_image())
        prev_hist = hist
    container.close()
    return keyframes
