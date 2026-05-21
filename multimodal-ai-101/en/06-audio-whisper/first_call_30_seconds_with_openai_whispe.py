"""Generated from book-content article."""

import whisper

model = whisper.load_model("small")  # tiny / base / small / medium / large-v3
result = model.transcribe("samples/meeting.m4a", language="en")
print(result["text"])
for seg in result["segments"][:3]:
    print(f"[{seg['start']:.1f}-{seg['end']:.1f}] {seg['text']}")
