"""Generated from book-content article."""

def decompose_goal(goal: str) -> list[TaskSpec]:
    """Decompose a Goal into executable Tasks."""
    # Goal: "Improve customer support quality"
    # → Tasks:
    return [
        TaskSpec(
            goal="Answer the 12 unanswered tickets from the past 24 hours",
            inputs={"queue": "support", "status": "unanswered", "max_age_hours": 24},
            outputs={"format": "ticket_reply", "destination": "zendesk"},
            completion_criteria=[
                "All 12 tickets have a reply",
                "Each reply uses an approved template",
                "Each reply links to a knowledge base article",
            ],
        ),
        TaskSpec(
            goal="Group last week's tickets by topic and produce statistics",
            inputs={"date_range": "last_week", "queue": "support"},
            outputs={"format": "json", "destination": "reports/topics.json"},
            completion_criteria=[
                "All tickets are assigned to a topic",
                "Each topic has count and percentage",
                "Top 5 topics include sample ticket IDs",
            ],
        ),
    ]
