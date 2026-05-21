"""Generated from book-content article."""

segments, _ = model.transcribe(
    "samples/medical.m4a",
    language="en",
    initial_prompt="patient, prescription, diagnosis, drug interaction, side effects.",
)
