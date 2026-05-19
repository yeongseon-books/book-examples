from common import FeedbackLoop
from conftest import load_episode


def test_ep07_feedback_loop_stops_at_max_iterations():
    m = load_episode("ko", "07-feedback-loop")
    text, iters = m.feedback_loop_example()
    assert "improved" in text
    loop = FeedbackLoop(max_iterations=2)
    final, used = loop.run("draft", lambda _: "draft", lambda _: 0)
    assert final == "draft"
    assert used == 1
