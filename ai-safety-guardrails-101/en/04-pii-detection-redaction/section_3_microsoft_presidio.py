"""Generated from book-content article."""

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

text = "Alice Kim called from 555-123-4567 about her order."

results = analyzer.analyze(text=text, language="en")
# [<RecognizerResult PERSON, 0, 9, 0.85>, <PHONE_NUMBER, 22, 34, 0.75>, ...]

masked = anonymizer.anonymize(text=text, analyzer_results=results)
print(masked.text)
# "<PERSON> called from <PHONE_NUMBER> about her order."
