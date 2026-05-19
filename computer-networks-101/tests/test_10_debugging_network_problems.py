from tests._loader import load_ko


def test_packet_analyzer() -> None:
    ep = load_ko("10-debugging-network-problems")
    raw = """
{"ts":0.00,"flow":"f1","seq":1,"event":"SYN","src":"10.0.0.1"}
{"ts":0.01,"flow":"f1","seq":1,"event":"SYN","src":"10.0.0.1"}
{"ts":0.02,"flow":"f1","seq":1,"event":"SYN","src":"10.0.0.1"}
{"ts":0.10,"flow":"f2","seq":7,"event":"SEND","src":"10.0.0.2"}
{"ts":0.20,"flow":"f2","seq":7,"event":"ACK","src":"10.0.0.3"}
{"ts":0.30,"flow":"f2","seq":7,"event":"SEND","src":"10.0.0.2"}
""".strip()
    out = ep.analyze_packet_log(raw)
    assert out["avg_rtt_ms"] == 100.0
    assert out["retransmits"] == 1
    assert out["syn_flood_sources"] == ["10.0.0.1"]
