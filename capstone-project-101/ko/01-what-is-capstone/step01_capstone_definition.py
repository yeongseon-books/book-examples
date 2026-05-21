"""Capstone Project 101 - 1편: what is capstone 예제."""

from __future__ import annotations


def run() -> dict[str, object]:
    """Run."""
    title = "강의 시간표 충돌 검사기"
    users = ["student", "advisor"]
    value = "수강 신청 시간을 줄인다"
    metric = "사용자가 충돌을 30초 안에 확인"
    demo = "demo.mp4 + readme.md"
    return {
        "title": title,
        "users": users,
        "value": value,
        "metric": metric,
        "demo": demo,
        "success": True,
    }


if __name__ == "__main__":
    print(run())
