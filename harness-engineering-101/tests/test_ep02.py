import pytest
from common import TaskHarness, TaskSpec
from conftest import load_episode


def test_ep02_task_harness_requires_output_key():
    m = load_episode("ko", "02-task-harness")
    assert m.task_harness_example()["status"] == "done"
    h = TaskHarness()
    spec = TaskSpec(goal="x", inputs={}, output_keys=["status"])
    with pytest.raises(ValueError):
        h.run(spec, lambda _: {"missing": True})
