from pathlib import Path

from common import read_json
from ko.ep09_star_points import generate_star_talking_points


def test_ep09_star_generator() -> None:
    points = generate_star_talking_points(
        read_json(Path("fixtures/project_metadata.json"))
    )
    assert len(points) == 4
    assert points[0].startswith("Situation:")
