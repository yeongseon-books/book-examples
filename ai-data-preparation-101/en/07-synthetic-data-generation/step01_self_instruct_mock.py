"""Ai Data Preparation 101 - Episode 7: synthetic data generation example."""

import random


def run(seed: int = 7) -> dict[str, object]:
    """Run."""
    rng = random.Random(seed)
    seeds = [
        {
            "instruction": "Summarize the sentence.",
            "input": "Data preparation drives model quality.",
            "output": "Data preparation is important.",
        },
        {
            "instruction": "Classify the sentence.",
            "input": "This text is an advertisement.",
            "output": "label=spam",
        },
    ]
    generated: list[dict[str, str]] = []
    for task in seeds:
        tone = rng.choice(["briefly", "in two steps", "with evidence"])
        generated.append(
            {
                "instruction": f"{task['instruction']} ({tone})",
                "input": task["input"],
                "output": task["output"],
            }
        )
    return {"count": len(generated), "samples": generated}


if __name__ == "__main__":
    print(run())
