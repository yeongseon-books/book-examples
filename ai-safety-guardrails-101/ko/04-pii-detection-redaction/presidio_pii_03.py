"""Generated from book-content article."""

from presidio_analyzer import Pattern, PatternRecognizer

custom_id = PatternRecognizer(
    supported_entity="EMPLOYEE_ID",
    patterns=[Pattern(name="emp_id", regex=r"\bEMP-\d{6}\b", score=0.95)],
    supported_language="en",
)
analyzer.registry.add_recognizer(custom_id)
