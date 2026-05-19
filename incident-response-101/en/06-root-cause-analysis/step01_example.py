"""Incident Response 101 - Episode 1: Example."""

from common import RCAFramework


def run() -> dict[str, object]:
    """Run."""
    rca = RCAFramework()
    whys = rca.five_whys(
        "checkout timeout",
        [
            "DB CPU saturated",
            "missing query index",
            "index review skipped",
            "release checklist outdated",
            "ownership unclear",
        ],
    )
    fishbone = rca.fishbone(
        {
            "people": ["handoff gap"],
            "process": ["missing review"],
            "tooling": [],
            "system": ["no alert"],
        }
    )
    return {"five_whys": whys, "fishbone": fishbone}


if __name__ == "__main__":
    print(run())
