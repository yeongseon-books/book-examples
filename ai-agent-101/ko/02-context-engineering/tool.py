"""Generated from book-content article."""

tools = [
    {
        "name": "search_docs",
        "description": "Use for conceptual explanations from official docs.",
        "when_to_use": [
            "User asks what/why questions",
            "No local file path is provided"
        ],
        "when_not_to_use": [
            "User asks to modify repository files",
            "Answer requires current runtime state"
        ]
    },
    {
        "name": "run_tests",
        "description": "Run project tests and return summarized failures.",
        "when_to_use": [
            "User asks verification after code change",
            "Need regression confidence"
        ],
        "when_not_to_use": [
            "No code change occurred",
            "Command requires unavailable credentials"
        ]
    }
]
