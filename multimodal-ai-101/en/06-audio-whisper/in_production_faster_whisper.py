"""Generated from book-content article."""

from faster_whisper import WhisperModel

model = WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16",  # int8_float16 / int8 also available
)

segments, info = model.transcribe(
    "samples/meeting.m4a",
    language="en",
    beam_size=5,
    vad_filter=True,
    vad_parameters={"min_silence_duration_ms": 500},
)

print(f"Detected language: {info.language} (prob {info.language_probability:.2f})")
for seg in segments:
    print(f"[{seg.start:.1f}-{seg.end:.1f}] {seg.text}")
