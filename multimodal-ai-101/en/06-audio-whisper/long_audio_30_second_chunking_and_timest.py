"""Generated from book-content article."""

segments, info = model.transcribe(
    "samples/lecture.mp3",
    language="en",
    word_timestamps=True,
)

for seg in segments:
    for w in seg.words:
        print(f"[{w.start:.2f}-{w.end:.2f}] {w.word}")
