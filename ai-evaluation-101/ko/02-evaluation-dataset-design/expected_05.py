"""Generated from book-content article."""

examples = [
    EvalExample(
        id="qa-001",
        input={"question": "What is the capital of Korea?"},
        expected={"style": "exact", "answer": "Seoul"},
        category="happy_path",
    ),
    EvalExample(
        id="summary-001",
        input={"text": "..."},
        expected={"style": "keywords", "must_include": ["microservice", "latency"]},
        category="happy_path",
    ),
    EvalExample(
        id="advice-001",
        input={"question": "How should I structure my React app?"},
        expected={"style": "rubric"},
        category="edge_case",
    ),
]
