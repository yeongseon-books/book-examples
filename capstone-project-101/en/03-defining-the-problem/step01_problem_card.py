from __future__ import annotations


def run() -> dict[str, str]:
    return {
        "observation": "Timetable conflicts happen frequently during enrollment",
        "user": "Freshmen and double-major students",
        "value": "Detect conflicts quickly",
        "assumption": "Users can input timetables as text",
        "metric": "Conflict detection time <= 30s",
    }


if __name__ == "__main__":
    print(run())
