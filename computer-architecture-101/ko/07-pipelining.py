"""Computer Architecture 101 - Episode 7: Pipelining."""

from __future__ import annotations


def non_pipelined_cycles(instruction_count: int, stages: int = 5) -> int:
    """Non pipelined cycles."""
    return instruction_count * stages


def pipelined_cycles(instruction_count: int, stages: int = 5, stalls: int = 0) -> int:
    """Pipelined cycles."""
    if instruction_count == 0:
        return 0
    return instruction_count + stages - 1 + stalls


def cpi(cycles: int, instructions: int) -> float:
    """Cpi."""
    return cycles / instructions if instructions else 0.0


def sample_comparison() -> dict[str, float]:
    """Sample comparison."""
    instructions = 20
    seq = non_pipelined_cycles(instructions)
    pipe = pipelined_cycles(instructions, stalls=2)
    return {
        "seq_cycles": float(seq),
        "pipe_cycles": float(pipe),
        "seq_cpi": cpi(seq, instructions),
        "pipe_cpi": cpi(pipe, instructions),
    }


if __name__ == "__main__":
    print(sample_comparison())
