from __future__ import annotations


def run() -> dict[str, object]:
    story = "As a student, I want to see timetable conflicts immediately"
    accept = ["입력 5초", "결과 1초", "에러 명확"]
    nf = ["mobile", "no_signup", "korean_first"]
    prio = {"core": "Must", "share": "Should", "ai": "Could"}
    trace = {"ST-1": ["F-1", "F-2"]}
    return {"story": story, "accept": accept, "nf": nf, "prio": prio, "trace": trace}


if __name__ == "__main__":
    print(run())
