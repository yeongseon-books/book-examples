# pip install presidio-analyzer presidio-anonymizer
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()  # English default; Korean needs spaCy ko model
anonymizer = AnonymizerEngine()

def detect_ner(text: str, language: str = "en") -> list[dict]:
    results = analyzer.analyze(
        text=text,
        entities=["EMAIL_ADDRESS", "PHONE_NUMBER", "PERSON",
                  "LOCATION", "CREDIT_CARD", "IP_ADDRESS"],
        language=language,
    )
    return [{"type": r.entity_type, "start": r.start, "end": r.end,
             "score": r.score, "text": text[r.start:r.end]} for r in results]

text = "John Smith works at Acme Corp in Seoul. Email: john@acme.com"
for hit in detect_ner(text):
    print(hit)
