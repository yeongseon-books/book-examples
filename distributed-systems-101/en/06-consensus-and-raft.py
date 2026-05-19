"""Distributed Systems 101 - Episode 6: Consensus and raft."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import RaftNode


def run_demo() -> dict[str, object]:
    # Leader replicates log and commits after majority acknowledgement.
    """Run demo."""
    leader = RaftNode("n1")
    f1 = RaftNode("n2")
    f2 = RaftNode("n3")
    leader.become_candidate()
    leader.become_leader()
    leader.append_entry("set x=1")
    f1.log = list(leader.log)
    f2.log = list(leader.log)
    leader.commit_to(0)
    return {
        "role": leader.role,
        "term": leader.term,
        "commit_index": leader.commit_index,
    }


if __name__ == "__main__":
    print(run_demo())
