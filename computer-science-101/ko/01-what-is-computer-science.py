"""에피소드 01: 튜링 기계로 이진수 +1 계산"""

from dataclasses import dataclass


@dataclass
class TuringMachine:
    tape: list[str]
    head: int
    state: str = "carry"

    def step(self) -> None:
        if self.state == "carry":
            symbol = self.tape[self.head]
            if symbol == "1":
                self.tape[self.head] = "0"
                self.head -= 1
            elif symbol == "0":
                self.tape[self.head] = "1"
                self.state = "halt"
            else:
                raise ValueError(f"알 수 없는 심볼: {symbol}")

    def run(self) -> str:
        while self.state != "halt":
            self.step()
        return "".join(self.tape).lstrip("0") or "0"


def increment_binary(binary: str) -> str:
    tape = ["0"] + list(binary)
    machine = TuringMachine(tape=tape, head=len(tape) - 1)
    return machine.run()


if __name__ == "__main__":
    for value in ["0", "1", "110", "1111"]:
        print(f"{value} + 1 = {increment_binary(value)}")
