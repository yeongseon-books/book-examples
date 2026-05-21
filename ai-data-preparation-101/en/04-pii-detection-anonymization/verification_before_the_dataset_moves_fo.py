"""Generated from book-content article."""

TEST_ROWS = [
    {"text": "Contact Alice at alice@example.com or 010-1234-5678."},
    {"text": "John Smith from Acme lives in Seoul."},
]

for row in TEST_ROWS:
    regex_hits = detect_regex(row["text"])
    ner_hits = detect_ner(row["text"], language="en")
    print({
        "text": row["text"],
        "regex_types": sorted(regex_hits.keys()),
        "ner_types": sorted({hit["type"] for hit in ner_hits}),
    })
