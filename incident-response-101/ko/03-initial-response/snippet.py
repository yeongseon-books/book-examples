"""Generated from book-content article."""

def initial_response(alert_id: str, team: list[str]) -> dict:
    return {
        "ack": {"alert": alert_id, "status": "acknowledged"},
        "roles": {
            "IC": team[0],
            "Ops": team[1],
            "Comms": team[2],
            "Scribe": team[3] if len(team) > 3 else team[0],
        },
        "next_update_minutes": 30,
    }
