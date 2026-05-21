"""Generated from book-content article."""

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cuda", compute_type="float16")
SR = 16000  # Whisper standard sample rate
buffer = np.zeros(0, dtype=np.float32)

def callback(indata, frames, time_, status):
    global buffer
    buffer = np.concatenate([buffer, indata[:, 0]])
    if len(buffer) >= SR * 5:  # transcribe every 5 seconds
        segs, _ = model.transcribe(buffer, language="en")
        text = " ".join(s.text for s in segs)
        print("[partial]", text)
        # sliding window: keep only last 1 second
        buffer = buffer[-SR:]

with sd.InputStream(callback=callback, channels=1, samplerate=SR):
    sd.sleep(60_000)
