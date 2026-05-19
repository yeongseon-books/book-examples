"""Computer Networks 101 - Episode 10: Debugging network problems."""

from collections import defaultdict
from statistics import mean

from common import parse_json_lines


def analyze_packet_log(raw_json_lines: str) -> dict[str, object]:
    """Analyze packet log."""
    packets = parse_json_lines(raw_json_lines)
    sends: dict[tuple[str, int], float] = {}
    rtts: list[float] = []
    retransmits = 0
    syn_count = defaultdict(int)

    for packet in packets:
        flow = str(packet.get("flow", ""))
        seq = int(packet.get("seq", 0))
        event = str(packet.get("event", ""))
        ts = float(packet.get("ts", 0.0))
        src = str(packet.get("src", ""))

        if event == "SYN":
            syn_count[src] += 1
        if event == "SEND":
            key = (flow, seq)
            if key in sends:
                retransmits += 1
            sends[key] = ts
        if event == "ACK":
            key = (flow, seq)
            if key in sends:
                rtts.append(ts - sends[key])

    return {
        "avg_rtt_ms": round(mean(rtts) * 1000, 3) if rtts else 0.0,
        "retransmits": retransmits,
        "syn_flood_sources": sorted(
            [ip for ip, count in syn_count.items() if count >= 3]
        ),
    }


if __name__ == "__main__":
    demo = """{"ts":0.0,"flow":"a","seq":1,"event":"SEND","src":"10.0.0.1"}
{"ts":0.1,"flow":"a","seq":1,"event":"ACK","src":"10.0.0.2"}"""
    print(analyze_packet_log(demo))
